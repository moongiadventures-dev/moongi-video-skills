---
name: video-watch
description: Actually watch a video (YouTube URL or local file) instead of guessing from the title — downloads it with yt-dlp, pulls the real captions (or transcribes with Whisper when there are none), and slices it into timestamped frames + labeled contact sheets that Claude reads directly. Trigger whenever the user pastes a video link and asks to watch / analyze / summarize / review it, asks "what does this video say", wants a tutorial's steps extracted, or says "이 영상 봐줘", "영상 분석해줘", "유튜브 요약해줘".
---

# video-watch

Turns a video into the only two things Claude can actually read: **words and pictures.**
Captions give you what was said; frames give you what was on screen (UI, code, dashboards, prices) —
the half a transcript-only summary always misses.

## Run it

```bash
python "D:/Claude - od/Skills/video-production/video-watch/scripts/watch.py" "<url-or-file>"
```

Prints JSON with the output paths. Everything lands in `~/.claude/video-watch/<video_id>/`:

```
transcript.md   # timestamped, deduped, grouped into ~30s paragraphs
meta.json       # title, channel, duration, views, description
frames/         # 000120s_02-00.jpg  ← filename IS the timestamp
sheets/         # sheet_01.jpg ... 3x3 grids, each cell labeled [MM:SS]
```

### Then read it

1. **Read `transcript.md` first.** It's cheap and carries the argument.
2. **Read the contact sheets** (`sheets/*.jpg`) — 9 frames per image, so a 30-frame video is 4 reads instead of 30.
3. **Read individual frames only where it matters** — a moment the transcript points at but doesn't explain
   ("as you can see here", a pricing table, a config screen). Filenames are timestamps, so jump straight to it.

Never summarize from the title, the description, or search results about the video. Watch it.

## Options

| flag | default | when to change it |
|---|---|---|
| `--max-frames N` | 30 | 60+ for a dense UI demo; 10 for a talking head |
| `--interval N` | auto | force a fixed cadence (seconds) |
| `--no-frames` | off | podcast / interview — words are all there is |
| `--force-whisper` | off | captions exist but are garbage |
| `--model` | base | `small` / `medium` for accented or technical audio |
| `--langs` | `en,ko` | caption preference order |
| `--width` | 640 | raise for small on-screen text |
| `--outdir` | cache | pin output into a project folder |

## How it works

`yt-dlp` downloads the video + any captions → `ffmpeg` slices frames at an interval derived from duration →
Pillow tiles them into labeled sheets. If there are no captions, `faster-whisper` transcribes the audio locally
(CPU, int8 — no API cost). Auto-caption rolling duplicates get collapsed, so the transcript reads like prose
rather than a stutter.

Already installed on this machine: yt-dlp, ffmpeg, faster-whisper, Pillow.

## Notes

- **Long videos:** frame interval auto-scales to stay under `--max-frames`, so a 2-hour video still costs ~4 sheet reads.
- **Local files** work the same way (`watch.py "D:/path/clip.mp4"`) — it skips straight to Whisper + frames.
- Re-running on the same URL reuses the downloaded `video.mp4`; delete the folder to force a fresh pull.
- Content behind a login won't download. Say so rather than fabricating a summary.
