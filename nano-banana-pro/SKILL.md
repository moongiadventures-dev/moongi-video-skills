---
name: nano-banana-pro
description: >-
  Generate, edit, or compose images with Google's Gemini Image API (Nano Banana)
  via scripts/generate_image.py (uv). Supports draft gemini-3.1-flash-image-preview
  and final gemini-3-pro-image-preview, resolutions 512px–4K, any aspect ratio, and
  --input-image (-i) reference images for product/model-lock workflows. This is the
  generation engine that brand-os / image-os / carousel-os call for every image.
  Trigger: /nano-banana-pro <prompt>, or direct requests to generate / create / edit
  an image with Gemini or Nano Banana ("나노바나나로 이미지 생성해줘").
---

# Nano Banana Pro: Image Generation with Gemini

Use this skill to generate, edit, or compose images using Google's Gemini Image API.

## Invocation

Trigger on: `/nano-banana-pro <prompt>` or when the user asks to generate/create/edit an image.

## How to Run

Execute the generation script via uv:

```bash
source $HOME/.local/bin/env && uv run ~/.claude/skills/nano-banana-pro/scripts/generate_image.py \
  --prompt "<PROMPT>" \
  --output "<OUTPUT_PATH>" \
  [OPTIONS]
```

Always `source $HOME/.local/bin/env` before calling `uv` to ensure it is on PATH.

## Key Options

| Flag | Values | Default | Notes |
|------|--------|---------|-------|
| `--prompt` / `-p` | Any text | required | The image description |
| `--output` / `-o` | File path (.png) | required | Where to save the result |
| `--resolution` / `-r` | `512px`, `1K`, `2K`, `4K` | `1K` | Output resolution |
| `--aspect-ratio` / `-a` | `1:1`, `16:9`, `9:16`, `4:5`, `21:9`, etc. | `1:1` | Aspect ratio |
| `--model` / `-m` | See below | `gemini-3.1-flash-image-preview` | Model choice |
| `--preset` | `photorealistic`, `social-media`, `social-story`, `product`, `banner`, `thumbnail`, `illustration`, `cinematic` | none | Style preset |
| `--input-image` / `-i` | Image path | none | For editing; repeatable up to 14 |
| `--dry-run` | flag | off | Show cost estimate without generating |

## Models

- `gemini-3.1-flash-image-preview` — Fast, high quality, supports up to 4K (recommended)
- `gemini-3-pro-image-preview` — Premium quality, higher cost
- `gemini-2.5-flash-image` — Budget, 1K only

## Cost Guide (per image)

| Model | 512px | 1K | 2K | 4K |
|-------|-------|-----|-----|-----|
| 3.1 Flash | $0.045 | $0.067 | $0.101 | $0.151 |
| 3 Pro | — | $0.134 | $0.134 | $0.240 |
| 2.5 Flash | — | $0.039 | — | — |

Run `--dry-run` before generating if resolution is 2K or higher.

## Output

The script prints JSON to stdout:
```json
{
  "status": "complete",
  "outputPath": "/absolute/path/to/image.png",
  "resolution": "1K",
  "model": "gemini-3.1-flash-image-preview",
  "cost": "$0.067"
}
```

After generation:
1. Show the user the saved file path
2. Display the image if the IDE supports it
3. Report the cost

## Example Usage

```bash
# Basic generation
source $HOME/.local/bin/env && uv run ~/.claude/skills/nano-banana-pro/scripts/generate_image.py \
  --prompt "A panoramic view of a championship golf course at golden hour, Mt. Rainier in the background" \
  --output ~/Downloads/ncg_concept.png \
  --preset cinematic

# Social media square
source $HOME/.local/bin/env && uv run ~/.claude/skills/nano-banana-pro/scripts/generate_image.py \
  --prompt "Elegant wedding reception at a luxury golf clubhouse" \
  --output ~/Downloads/ncg_wedding.png \
  --preset social-media

# Edit existing image
source $HOME/.local/bin/env && uv run ~/.claude/skills/nano-banana-pro/scripts/generate_image.py \
  --prompt "Add a dramatic sunset sky" \
  -i ~/input.png \
  --output ~/Downloads/edited.png
```

## Requirements

- `uv` installed at `~/.local/bin/uv`
- `GOOGLE_API_KEY` set in `~/.claude/.env`
