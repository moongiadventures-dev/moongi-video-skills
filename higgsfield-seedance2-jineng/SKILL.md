---
name: higgsfield-seedance2-jineng
description: >-
  Collection of 15 Seedance 2.0 × Higgsfield prompt-engineering skills. Each turns
  Claude into a prompt engineer for one video style and outputs a large, detailed,
  paste-ready Seedance prompt with a 2-second scroll-stopping hook, beat-by-beat
  timeline (up to 15s), and a camera-movement vocabulary. Styles: cinematic, 3D/CGI,
  cartoon, comic-to-video, fight scenes, motion-design ad, ecommerce ad, anime action,
  product 360, music video, social hook, brand story, fashion lookbook, food & beverage,
  real estate. Trigger when the user wants a Seedance 2.0 / Higgsfield video prompt in
  any of these styles ("시네마틱 씨드댄스 프롬프트", "product 360 video prompt", etc.).
  This is a router — read the matching skills/NN-<style>/SKILL.md for the full skill.
---

# higgsfield-seedance2-jineng — Router

15 specialized prompt-engineering skills for **Seedance 2.0 on Higgsfield**. Each
produces a paste-ready prompt with a 2-second hook, per-beat timeline, and camera
vocabulary.

## How to use
1. Match the user's request to a style below.
2. Open `skills/<folder>/SKILL.md` and follow it to build the prompt.
3. If the request spans two styles (e.g. a cinematic product 360), read both and merge.
4. Paste the final prompt at https://higgsfield.ai/create/video?model=seedance_2_0

## Style → folder map
| Style | Folder |
|---|---|
| Cinematic / film look | `skills/01-cinematic/` |
| 3D / CGI | `skills/02-3d-cgi/` |
| Cartoon | `skills/03-cartoon/` |
| Comic → video | `skills/04-comic-to-video/` |
| Fight / action choreography | `skills/05-fight-scenes/` |
| Motion-design ad | `skills/06-motion-design-ad/` |
| E-commerce ad | `skills/07-ecommerce-ad/` |
| Anime action | `skills/08-anime-action/` |
| Product 360 spin | `skills/09-product-360/` |
| Music video | `skills/10-music-video/` |
| Social hook / short | `skills/11-social-hook/` |
| Brand story | `skills/12-brand-story/` |
| Fashion lookbook | `skills/13-fashion-lookbook/` |
| Food & beverage | `skills/14-food-beverage/` |
| Real estate | `skills/15-real-estate/` |

> Korean/other-language variants live under each folder's `zh-CN/` etc. and the repo
> `README.<lang>.md`. English `skills/NN-*/SKILL.md` is the canonical entry point.
