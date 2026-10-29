# Motion-Graphic Video Pipeline (HyperFrames + Motion Pack + Whisper)

> Saved 2026-06-21 to run next session. Provide: voiceover MP3 (or shot video), topic, target platform. Then Claude runs steps 1–10 end-to-end without asking between steps.

## STACK
- **HyperFrames** (github.com/heygen-com/hyperframes) — HTML → MP4 render engine. Already cloned at `Skills/video-production/motion-pack`'s sibling engines (`VideoStudio/hyperframes`, `Amplend/hyperframes`).
- **Remotion** — used to stitch/trim/sync scenes (ffmpeg concat as fallback).
- **IBRA Motion Pack** (github.com/halicotampa-crypto/motion-pack) — cloned at `Skills/video-production/motion-pack`. Templates in `templates/` + `community-templates/`.
- **OpenAI Whisper API** — word-level transcription (`verbose_json`, `timestamp_granularities[]=word`). ~$0.006/min.
- **ffmpeg** — mux + concat.

## WORKFLOW (run end-to-end)
1. If video given: `ffmpeg -y -i <input> -vn -ac 1 -ar 16000 audio.wav`
2. Whisper transcribe → word-level timestamps.
3. Strip dead air (>0.6s, -38dB) on BODY scenes only (not intro/outro). Re-transcribe trimmed.
4. Break transcript into scenes (1 idea, 3–8s each). Map phrase → visual.
5. Pick template: `motion-pack/templates/` (IBRA originals) → `community-templates/` → `npx hyperframes add <component>` → else write fresh HTML/CSS/GSAP.
6. Render: `node motion-pack/render-scene.js <scene.html> <out.mp4> <seconds>` @ 1080x1920 (vert) or 1920x1080 (land), 30fps, CRF 17–18, preset slow.
7. Mux audio per scene: `ffmpeg -i <silent.mp4> -i <audio.wav> -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -b:a 192k -shortest <final.mp4>`
8. Concat (Remotion preferred; ffmpeg concat fallback — normalize fps/sar/sample-rate first, first_pts=0).
9. Face-on-camera hook → render scenes as TRANSPARENT PNGs (Puppeteer omitBackground:true), overlay. IG safe zones: keep graphics OUT of top 0–220px and bottom 1500–1920px; if face in frame, graphics in lower-half only (y>1100), never cross face.
10. Output `final.mp4`, open it.

## BRAND TOKENS
ink `#0A0808` bg · cream `#EDD9BC` text · coral `#D97757` accent · success green `#4CD964` · success blue `#4080F0` · topographic line bg · font -apple-system/Inter, JetBrains Mono/ui-monospace.

## LOGOS — fetch real, never draw from memory
- iOS icons: `https://itunes.apple.com/lookup?id=<APP_ID>` → artworkUrl512 (swap `512x512bb.jpg`→`1024x1024bb.png`).
- Adobe: Wikimedia Commons SVGs. Convert: `rsvg-convert -w 1024 -h 1024 in.svg > out.png`.

## PITFALLS
1. Mux without explicit `-map 0:v:0 -map 1:a:0` → grabs wrong video stream.
2. silenceremove on clean intro/outro → breaks lip-sync. Body scenes only.
3. GSAP `tl.from()` on opacity:0 target → reverts to 0. Use `fromTo()` with explicit end state.
4. Infinite yoyo tweens on the timeline → playhead drift. Put on `gsap.to()` directly.
5. Animations in IG safe zones → covered by UI.

## NEW TEMPLATES ON REQUEST
Any animation I describe → build from scratch as a new HyperFrames scene. One self-contained HTML (inline style + single GSAP timeline), brand tokens, fromTo() with explicit ends, infinite tweens off the main timeline, render-deterministic at any seek time. Save new `.html` into `motion-pack/templates/` so the pack grows. Show a preview frame before full render.

---
## ⚠️ WINDOWS SETUP GAPS — resolve these BEFORE running tomorrow
This machine is **Windows**, not Mac. The prompt's setup commands are mac-flavored:
- `brew install ffmpeg` → N/A. ffmpeg is already used elsewhere in this workspace; verify with `ffmpeg -version`. `rsvg-convert` (for SVG→PNG logos) likely NOT installed — install or substitute (e.g. Inkscape CLI / sharp / resvg).
- **OPENAI_API_KEY** — Whisper needs it. Confirm it's in `~/.env` or `.env` before step 2. (Workspace `.env` has GOOGLE/ANTHROPIC keys; OpenAI key unconfirmed.)
- **Template count mismatch:** prompt says "32 IBRA templates"; the cloned `motion-pack/templates/` actually has **10** (01-audio-waveform … 10-progress-bar) + `community-templates/{helper-kit,student-kit}`. Verify before relying on a specific template.
- **Remotion** as a "built-in Claude Code skill, no install" — not confirmed registered in this session's skill list. May need actual install / fall back to ffmpeg concat.
- **`npx hyperframes add <component>`** — needs the hyperframes CLI; the engine copies live in `VideoStudio/hyperframes` and `Amplend/hyperframes`. Confirm CLI resolves from `Skills/video-production/motion-pack`.
- **Path note:** if the video-tooling consolidation moves `motion-pack` out of `Skills/`, update `render-scene.js` invocations accordingly. See memory `project_video_tooling_consolidation`.
