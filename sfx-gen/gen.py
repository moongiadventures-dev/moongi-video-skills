#!/usr/bin/env python3
"""
gen.py — generate an arbitrary sound effect with the ElevenLabs Sound Effects API.

Standalone: no palette, no catalog, no project layout. One prompt in, N mp3 variations out,
silence-trimmed and loudness-normalized, with a JSON sidecar recording what was asked for.

Usage:
  python gen.py --prompt "heavy wooden door closing, low thud, short decay. no music" \
                --out "D:/Claude - od/Projects/Foo/audio/sfx" --name door-close --count 3

  python gen.py --prompt "seamless ambient loop of quiet rain on a window" \
                --out ./sfx --name rain --duration 18 --loop

  python gen.py --prompt "..." --out ./sfx --dry-run     # show params, no API call, no billing

Key: ELEVEN_API_KEY (env, or "D:/Claude - od/.env/.env"). ffmpeg/ffprobe on PATH for post-processing.
"""
import argparse
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request

API_URL = "https://api.elevenlabs.io/v1/sound-generation"
MODEL = "eleven_text_to_sound_v2"
SHARED_ENV = r"D:\Claude - od\.env\.env"

TARGET_LUFS = -18.0
CEILING_DBFS = -1.5
SILENCE_DB = "-45dB"


def load_key():
    for var in ("ELEVEN_API_KEY", "ELEVENLABS_API_KEY"):
        if os.environ.get(var):
            return os.environ[var]
    if os.path.exists(SHARED_ENV):
        with open(SHARED_ENV, encoding="utf-8", errors="replace") as fh:
            for line in fh:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                if k.strip() in ("ELEVEN_API_KEY", "ELEVENLABS_API_KEY"):
                    v = v.strip().strip('"').strip("'")
                    if v:
                        return v
    sys.exit("ELEVEN_API_KEY not found (checked env and %s)" % SHARED_ENV)


def run(cmd):
    return subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                          text=True, encoding="utf-8", errors="replace").stdout


def have_ffmpeg():
    try:
        run(["ffmpeg", "-version"])
        run(["ffprobe", "-version"])
        return True
    except FileNotFoundError:
        return False


def probe_duration(path):
    out = run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
               "-of", "default=nw=1:nk=1", path]).strip()
    try:
        return round(float(out), 3)
    except ValueError:
        return None


def peak_db(path):
    m = re.search(r"max_volume:\s*(-?[\d.]+) dB",
                  run(["ffmpeg", "-hide_banner", "-i", path, "-af", "volumedetect",
                       "-f", "null", os.devnull]))
    return float(m.group(1)) if m else None


def postprocess(path):
    """Trim leading/trailing silence, then loudness-normalize with a peak ceiling."""
    tmp = path + ".post.mp3"
    filters = (
        "silenceremove=start_periods=1:start_duration=0.03:start_threshold=%s"
        ":stop_periods=-1:stop_duration=0.05:stop_threshold=%s,"
        "loudnorm=I=%s:TP=%s:LRA=11" % (SILENCE_DB, SILENCE_DB, TARGET_LUFS, CEILING_DBFS)
    )
    run(["ffmpeg", "-y", "-hide_banner", "-nostdin", "-i", path, "-af", filters,
         "-c:a", "libmp3lame", "-q:a", "2", tmp])
    if os.path.exists(tmp) and os.path.getsize(tmp) > 0:
        os.replace(tmp, path)
        return True
    if os.path.exists(tmp):
        os.remove(tmp)
    return False


def generate(key, prompt, duration, influence, loop):
    body = {"text": prompt, "model_id": MODEL, "prompt_influence": influence, "loop": loop}
    if duration is not None:
        body["duration_seconds"] = duration
    req = urllib.request.Request(
        API_URL, data=json.dumps(body).encode("utf-8"),
        headers={"xi-api-key": key, "Content-Type": "application/json", "Accept": "audio/mpeg"},
        method="POST")
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            return resp.read()
    except urllib.error.HTTPError as e:
        sys.exit("ElevenLabs %s: %s" % (e.code, e.read().decode("utf-8", "replace")[:400]))


def slugify(text):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", text.lower())).strip("-")[:40] or "sfx"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt", required=True)
    ap.add_argument("--out", required=True, help="output directory")
    ap.add_argument("--name", help="file slug (default: derived from prompt)")
    ap.add_argument("--count", type=int, default=3, help="1-4 variations (default 3)")
    ap.add_argument("--duration", type=float, help="0.5-30s; omit to let the model decide")
    ap.add_argument("--influence", type=float, default=0.3, help="0-1 prompt adherence")
    ap.add_argument("--loop", action="store_true", help="seamless loop; disables post-processing")
    ap.add_argument("--no-post", action="store_true", help="skip trim + normalize")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    if not 1 <= a.count <= 4:
        sys.exit("--count must be 1-4")
    if a.duration is not None and not 0.5 <= a.duration <= 30:
        sys.exit("--duration must be 0.5-30")
    if not 0 <= a.influence <= 1:
        sys.exit("--influence must be 0-1")

    name = a.name or slugify(a.prompt)
    post = not (a.no_post or a.loop)

    print("prompt     : %s" % a.prompt)
    print("out        : %s" % os.path.abspath(a.out))
    print("name/count : %s x%d" % (name, a.count))
    print("duration   : %s" % ("auto" if a.duration is None else "%.2fs" % a.duration))
    print("influence  : %.2f   loop: %s   postprocess: %s" % (a.influence, a.loop, post))

    if a.dry_run:
        print("\n[dry-run] no API call made, nothing billed.")
        return

    if post and not have_ffmpeg():
        print("\n! ffmpeg/ffprobe not on PATH — writing raw audio without trim/normalize")
        post = False

    key = load_key()
    os.makedirs(a.out, exist_ok=True)
    files = []

    for i in range(1, a.count + 1):
        path = os.path.join(a.out, "%s-%d.mp3" % (name, i))
        print("\n-> %s" % os.path.basename(path))
        audio = generate(key, a.prompt, a.duration, a.influence, a.loop)
        with open(path, "wb") as fh:
            fh.write(audio)
        entry = {"file": path, "postprocessed": False}
        if post:
            entry["postprocessed"] = postprocess(path)
        if have_ffmpeg():
            entry["duration_s"] = probe_duration(path)
            entry["peak_dbfs"] = peak_db(path)
            print("   %.3fs  peak %.1f dBFS" % (entry["duration_s"] or 0, entry["peak_dbfs"] or 0))
        files.append(entry)

    sidecar = os.path.join(a.out, "%s.json" % name)
    with open(sidecar, "w", encoding="utf-8") as fh:
        json.dump({"prompt": a.prompt, "model": MODEL, "count": a.count,
                   "duration_seconds": a.duration, "prompt_influence": a.influence,
                   "loop": a.loop, "postprocessed": post,
                   "target_lufs": TARGET_LUFS if post else None,
                   "files": files}, fh, ensure_ascii=False, indent=2)

    print("\ndone: %d file(s) + %s" % (len(files), os.path.basename(sidecar)))


if __name__ == "__main__":
    main()
