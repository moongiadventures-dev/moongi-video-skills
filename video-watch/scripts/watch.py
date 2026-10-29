#!/usr/bin/env python3
"""Turn a video (YouTube URL or local file) into things Claude can read:
a timestamped transcript + timestamped frames + labeled contact sheets.

Pipeline: yt-dlp (download + captions) -> ffmpeg (frames/audio) -> faster-whisper (only if no captions).
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

DEFAULT_CACHE = Path.home() / ".claude" / "video-watch"


def run(cmd, **kw):
    return subprocess.run(cmd, check=True, capture_output=True, text=True, encoding="utf-8", errors="replace", **kw)


def hms(seconds):
    seconds = int(seconds)
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


# ---------- fetch ----------

def probe(url):
    out = run(["yt-dlp", "-J", "--no-playlist", url]).stdout
    d = json.loads(out)
    return {
        "id": d.get("id", "video"),
        "title": d.get("title", ""),
        "channel": d.get("channel") or d.get("uploader", ""),
        "duration": d.get("duration") or 0,
        "upload_date": d.get("upload_date", ""),
        "view_count": d.get("view_count"),
        "webpage_url": d.get("webpage_url", url),
        "description": d.get("description", ""),
    }


def fetch_captions(url, outdir, langs):
    """Download captions. Returns path to best .vtt or None."""
    try:
        run([
            "yt-dlp", "--no-playlist", "--skip-download",
            "--write-subs", "--write-auto-subs",
            "--sub-langs", ",".join(f"{l}.*" for l in langs),
            "--sub-format", "vtt",
            "-o", str(outdir / "cc"), url,
        ])
    except subprocess.CalledProcessError as e:
        print(f"[warn] caption fetch failed: {e.stderr[-300:]}", file=sys.stderr)
        return None
    vtts = sorted(outdir.glob("cc.*.vtt"))
    if not vtts:
        return None
    # Prefer the caller's language order; within a language, manual subs sort before auto ones only by name,
    # so just take the first match per preference order.
    for lang in langs:
        for v in vtts:
            if f".{lang}" in v.name:
                return v
    return vtts[0]


def fetch_video(url, outdir, height):
    dst = outdir / "video.mp4"
    if dst.exists():
        return dst
    run([
        "yt-dlp", "--no-playlist",
        "-f", f"bv*[height<={height}]+ba/b[height<={height}]/bv*+ba/b",
        "--merge-output-format", "mp4",
        "-o", str(dst), url,
    ])
    return dst


# ---------- transcript ----------

TAG_RE = re.compile(r"<[^>]+>")
CUE_RE = re.compile(r"(\d{2}:\d{2}:\d{2}[.,]\d{3})\s+-->\s+(\d{2}:\d{2}:\d{2}[.,]\d{3})")


def ts_to_sec(t):
    t = t.replace(",", ".")
    h, m, s = t.split(":")
    return int(h) * 3600 + int(m) * 60 + float(s)


def parse_vtt(path):
    """Return [(start_sec, text)] with YouTube's rolling-caption duplicates collapsed."""
    cues = []
    start = None
    buf = []
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        m = CUE_RE.search(raw)
        if m:
            if start is not None and buf:
                cues.append((start, " ".join(buf)))
            start = ts_to_sec(m.group(1))
            buf = []
            continue
        line = TAG_RE.sub("", raw).strip()
        if not line or line.startswith(("WEBVTT", "Kind:", "Language:", "NOTE")):
            continue
        buf.append(line)
    if start is not None and buf:
        cues.append((start, " ".join(buf)))

    # Auto-captions repeat the previous cue as the top row of the next one. Keep only the new words.
    out = []
    prev = ""
    for start, text in cues:
        text = re.sub(r"\s+", " ", text).strip()
        if not text or text == prev:
            continue
        new = text[len(prev):].strip() if prev and text.startswith(prev) else text
        if new:
            out.append((start, new))
        prev = text
    return out


def whisper_transcribe(media, model_size, lang):
    from faster_whisper import WhisperModel
    print(f"[whisper] transcribing with model={model_size} (no captions available)", file=sys.stderr)
    model = WhisperModel(model_size, device="cpu", compute_type="int8")
    segments, _ = model.transcribe(str(media), language=lang, vad_filter=True)
    return [(seg.start, seg.text.strip()) for seg in segments if seg.text.strip()]


def group_cues(cues, window):
    """Merge cues into ~`window`-second paragraphs so the transcript reads like prose."""
    blocks = []
    cur_start, cur = None, []
    for start, text in cues:
        if cur_start is None:
            cur_start = start
        cur.append(text)
        if start - cur_start >= window:
            blocks.append((cur_start, " ".join(cur)))
            cur_start, cur = None, []
    if cur:
        blocks.append((cur_start or 0, " ".join(cur)))
    return blocks


# ---------- frames ----------

def extract_frames(video, outdir, interval, width):
    frames_dir = outdir / "frames"
    if frames_dir.exists():
        shutil.rmtree(frames_dir)
    frames_dir.mkdir(parents=True)
    run([
        "ffmpeg", "-nostdin", "-y", "-i", str(video),
        "-vf", f"fps=1/{interval},scale={width}:-2",
        "-q:v", "4", str(frames_dir / "f_%04d.jpg"),
    ])
    # ffmpeg's fps filter emits the frame at the midpoint of each interval bucket.
    out = []
    for i, f in enumerate(sorted(frames_dir.glob("f_*.jpg"))):
        t = int(i * interval)
        dst = frames_dir / f"{t:06d}s_{hms(t).replace(':', '-')}.jpg"
        f.rename(dst)
        out.append((t, dst))
    return out


def contact_sheets(frames, outdir, cols=3, rows=3):
    from PIL import Image, ImageDraw
    sheets_dir = outdir / "sheets"
    if sheets_dir.exists():
        shutil.rmtree(sheets_dir)
    sheets_dir.mkdir(parents=True)
    per = cols * rows
    made = []
    for n in range(0, len(frames), per):
        chunk = frames[n:n + per]
        thumbs = [(t, Image.open(p).convert("RGB")) for t, p in chunk]
        tw, th = thumbs[0][1].size
        bar = 26
        sheet = Image.new("RGB", (cols * tw, rows * (th + bar)), "black")
        draw = ImageDraw.Draw(sheet)
        for i, (t, im) in enumerate(thumbs):
            c, r = i % cols, i // cols
            x, y = c * tw, r * (th + bar)
            sheet.paste(im, (x, y))
            draw.text((x + 6, y + th + 5), f"[{hms(t)}]", fill="white")
        dst = sheets_dir / f"sheet_{n // per + 1:02d}.jpg"
        sheet.save(dst, quality=85)
        made.append(dst)
    return made


# ---------- main ----------

def main():
    ap = argparse.ArgumentParser(description="Make a video readable by Claude.")
    ap.add_argument("source", help="YouTube/site URL or local video path")
    ap.add_argument("--outdir", help="output dir (default: ~/.claude/video-watch/<id>)")
    ap.add_argument("--max-frames", type=int, default=30, help="cap on frames (default 30)")
    ap.add_argument("--interval", type=int, default=0, help="seconds between frames (0 = auto from duration)")
    ap.add_argument("--width", type=int, default=640, help="frame width px")
    ap.add_argument("--height", type=int, default=720, help="max download height")
    ap.add_argument("--langs", default="en,ko", help="caption language preference, comma-separated")
    ap.add_argument("--window", type=int, default=30, help="transcript paragraph size in seconds")
    ap.add_argument("--no-frames", action="store_true", help="transcript only")
    ap.add_argument("--force-whisper", action="store_true", help="ignore captions, transcribe audio")
    ap.add_argument("--model", default="base", help="whisper model: tiny/base/small/medium")
    args = ap.parse_args()

    langs = [l.strip() for l in args.langs.split(",") if l.strip()]
    local = Path(args.source)
    is_local = local.exists()

    if is_local:
        meta = {"id": local.stem, "title": local.name, "channel": "", "duration": 0,
                "webpage_url": str(local.resolve()), "description": "", "upload_date": "", "view_count": None}
    else:
        meta = probe(args.source)

    outdir = Path(args.outdir) if args.outdir else DEFAULT_CACHE / re.sub(r"[^\w.-]", "_", meta["id"])
    outdir.mkdir(parents=True, exist_ok=True)

    # 1. transcript
    cues, source = [], None
    if not args.force_whisper and not is_local:
        vtt = fetch_captions(args.source, outdir, langs)
        if vtt:
            cues = parse_vtt(vtt)
            source = f"captions ({vtt.name})"

    video = None
    if not args.no_frames:
        video = local if is_local else fetch_video(args.source, outdir, args.height)

    if not cues:
        media = video or (local if is_local else fetch_video(args.source, outdir, args.height))
        cues = whisper_transcribe(media, args.model, langs[0] if len(langs) == 1 else None)
        source = f"whisper ({args.model})"

    if not meta["duration"] and cues:
        meta["duration"] = int(cues[-1][0]) + 30

    blocks = group_cues(cues, args.window)

    # 2. frames
    frames = []
    if video and not args.no_frames:
        interval = args.interval or max(5, round(meta["duration"] / args.max_frames / 5) * 5 or 5)
        frames = extract_frames(video, outdir, interval, args.width)
        if len(frames) > args.max_frames:  # keep an evenly-spaced subset
            step = len(frames) / args.max_frames
            keep = {frames[int(i * step)][1] for i in range(args.max_frames)}
            for _, p in frames:
                if p not in keep:
                    p.unlink()
            frames = [(t, p) for t, p in frames if p in keep]
        sheets = contact_sheets(frames, outdir) if frames else []
    else:
        sheets = []

    # 3. write transcript.md
    md = [f"# {meta['title']}", ""]
    if meta["channel"]:
        md.append(f"**Channel:** {meta['channel']}  ")
    if meta["duration"]:
        md.append(f"**Duration:** {hms(meta['duration'])}  ")
    if meta.get("view_count"):
        md.append(f"**Views:** {meta['view_count']:,}  ")
    md += [f"**URL:** {meta['webpage_url']}  ", f"**Transcript source:** {source}", ""]
    if meta["description"]:
        md += ["## Description", "", "```", meta["description"].strip()[:3000], "```", ""]
    md += ["## Transcript", ""]
    for start, text in blocks:
        md.append(f"**[{hms(start)}]** {text}")
        md.append("")
    (outdir / "transcript.md").write_text("\n".join(md), encoding="utf-8")
    (outdir / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps({
        "outdir": str(outdir),
        "transcript": str(outdir / "transcript.md"),
        "transcript_source": source,
        "words": sum(len(t.split()) for _, t in cues),
        "frames": len(frames),
        "sheets": [str(s) for s in sheets],
        "title": meta["title"],
        "duration": hms(meta["duration"]) if meta["duration"] else "?",
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
