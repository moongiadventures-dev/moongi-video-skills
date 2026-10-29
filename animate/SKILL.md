---
name: animate
description: Turn a style reference + a rough idea into a finished animated video where every frame is drawn in code (SVG, canvas, WebGL) and rendered to MP4 with HyperFrames — explainers, animated stories, motion graphics, product ads, in any style. Use when the user says "animate", "make an animation", "animated explainer", "make a video in this style", uploads reference frames/videos and gives a topic, a length and an aspect ratio, or runs /animate.
---

# /animate — the code animation studio

You are the whole studio: researcher, art director, animator, sound designer, editor and QA. Everything you show is **drawn by code**: no video model, no stock footage, no AI images, unless the user explicitly adds them. Code places every line exactly where it is told, so text stays sharp, shapes keep their form, and the style holds from the first shot to the last.

## Inputs (ask once, in one message, only for what is missing)
1. **Style references:** images, video frames or a short clip the user uploaded. They guide the look only. Never trace or embed them.
2. **Topic or story:** a rough idea is enough.
3. **Duration and aspect ratio:** e.g. 15 s at 9:16 (1080×1920), 30 s at 16:9 (1920×1080) or 1:1.
4. Optional: narration (yes/no, voice), on-screen words, an ending or CTA.

## 0 · Setup (first run only)
- Check for Node 22+ and FFmpeg (`node -v`, `ffmpeg -version`). If either is missing, install it for the user if you can (for example `brew install node ffmpeg` on a Mac with Homebrew), otherwise give them the one command and stop.
- HyperFrames (the open-source HTML-to-video renderer by HeyGen, Apache 2.0) must be installed as a Claude Code plugin:
  `claude plugin marketplace add heygen-com/hyperframes` and then `claude plugin install hyperframes@hyperframes`. After a fresh install, ask the user to restart Claude Code.
- Create `./<kebab-title>/` with `npx hyperframes@latest init` (or copy an existing project), then `npx hyperframes@latest doctor`.

## 1 · Research (explainers and anything factual)
- Find 2–4 reliable sources (official sites, encyclopaedias, papers). Write `RESEARCH.md` with the facts you will show and their sources.
- Only put a fact on screen if it is in RESEARCH.md. If a claim is uncertain, simplify it or leave it out.

## 2 · Style bible (`STYLE.md`)
Study every reference and write down:
- **Palette:** 5–8 hex colours with roles (background, ink, accent, highlights).
- **Line and shape:** stroke weight, wobble, corners, outlines or none.
- **Texture:** paper grain, watercolour bleed, halftone, felt, gouache flatness.
- **Light:** flat, soft gradient, rim light, caustics.
- **Type:** families and sizes. Use Google Fonts or system fonts and embed them with `@font-face`.
- **Motion personality:** springy, floaty, snappy, slow and heavy; easing names; camera habits.
Then add one paragraph: "how we draw this in code". For example: SVG with an feTurbulence displacement for a wobbly line; canvas for many organic moving things; a WebGL fragment shader for water, light or grain.

## 3 · Beats and shot list (`SHOTS.md`)
- One idea per shot, 2–4 s each (a 15 s piece has about 5 shots). Write one table row per shot: time · what we see · what moves · camera (push-in, track a subject, pull back, pan) · words on screen · sound cue.
- The first second must already move and show the subject. No title cards before the action.
- Camera language: open wide, move in and track the subject, then glide to a second subject, then pull back to reveal. Never hold a still frame. Let big moments breathe: a reveal should take 2–3 s, not 0.5 s.
- Pure animation beats UI. Don't add info cards, badges, progress bars or label pills unless the user asks for them. Show the idea through the picture and the camera.
- If there is narration, write it first, generate it, then get word timings (Whisper) and cut every shot on a word.

## 4 · Build
- One HyperFrames project; one sub-composition per shot or scene. Read `/hyperframes-core` before writing composition HTML.
- **Everything is a function of time.** Drive canvas/WebGL drawing from one GSAP proxy tween (`tl.to(proxy, { t: DUR, ease: "none", onUpdate: () => draw(proxy.t) })`). Use seeded random numbers only. Never use `Math.random()`, `Date.now()` or requestAnimationFrame loops. Then every frame renders the same every time.
- Tool choice:
  - SVG for illustration, labels and diagrams.
  - canvas 2D for creatures, particles and anything with dozens of moving parts.
  - WebGL shaders for water, light, clouds and paper grain.
  - CSS/DOM for UI and type.
- Make living things feel alive: bodies follow a spline and bend, fins and wings lag behind, and everything has a slow idle motion (sway, bob, drift).
- Keep text inside the safe area (60 px margins on 9:16). Captions sit in the lower third and never cover the subject.

## 5 · Sound (music in code, effects optional)
- Synthesise the music and SFX in code (Python + numpy, or an OfflineAudioContext script) and write a WAV: a short motif, a pad, soft percussion and hits on the big moments. Keep the mix around −14 LUFS, with narration −3 dB over the music if there is a voice.
- Keep the music low under any narration (about 20 dB below the voice). If the user has a sound-effects tool (for example ElevenLabs Sound Effects), add effects that match what's on screen: water, wings, paper, clicks, whooshes on cuts.
- Add the WAV to the root composition as `<audio id="music" …>`.

## 6 · Self-check loop (do this, don't skip it)
1. `npx hyperframes@latest lint` → fix every error.
2. `npx hyperframes@latest snapshot --at <one time per shot>` → open the contact sheet and look at every frame against STYLE.md and the references. Check:
   - Does it match the palette, line and texture?
   - Is any text cut off, overlapping or unreadable?
   - Is anything off-screen that shouldn't be, or any stray shape?
   - Is the spacing even?
   - Is the subject readable in the first second?
3. Fix what is off: change the instruction and re-render, never "regenerate and hope". At most 3 loops, and each loop states what it fixed.
4. Render: `npx hyperframes@latest render -q delivery -o renders/<name>.mp4`. Extract 8 frames from the **rendered MP4** with ffmpeg and check motion continuity, with no frozen or blank frames. Check the audio with `ffprobe`.

## 7 · Deliver
- Give the MP4 path, its duration and resolution, a one-line summary per shot, and "easy tweaks you can ask for" (3 bullets).
- Keep the project folder, so any change is one instruction plus a re-render.

## Example brief
```
/animate
Story/Topic: a cool explainer video on how a hummingbird hovers
15 sec, 9:16
```
