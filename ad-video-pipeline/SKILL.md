---
name: ad-video-pipeline
description: >-
  Complete ad / commercial video production pipeline (Stage 0–5+): brief → concept
  → shot list → storyboard images → video generation → edit. Covers commercial and
  brand ads, K-pop / talent / fashion-model ads, music videos, short films, and
  narrative. Also covers website hero videos, scroll-driven video, and construction /
  process time-lapses. Generates paste-ready image + video prompts; image and video
  generation runs on bbanana (free web images + paid Seedance) or Higgsfield + Kling.
  Trigger when the user wants to create a commercial, ad video, marketing / campaign
  video, brand film, short film, music video, advertisement, website hero video, or a
  time-lapse, or says "광고 영상 / 커머셜 / 브랜드 필름 / 뮤직비디오 / 홍보 영상 /
  제품 영상 / 타임랩스 / 웹사이트에 들어갈 영상 / 히어로 영상 만들어줘".
  Not for editing existing footage — use video-edit for that.
---

# Ad Video Production Pipeline — Complete Skill
# Version 2.5 | For any brand, any campaign, any platform

## TRIGGER

**슬래시로 직접** — `/ad-video-pipeline`

**말로 부를 때** — 아래 중 하나가 들어가면 켜집니다.
`광고 영상` · `커머셜` · `브랜드 필름` · `캠페인 영상` · `뮤직비디오` · `홍보 영상`
· `제품 영상` · `타임랩스` · `히어로 영상` · `웹사이트에 들어갈 영상`
· `commercial` · `ad video` · `campaign video` · `brand film` · `time-lapse`

예) 「인테리어 시공 업체 **광고 영상** 만들어줘」
　　「카페 시공 과정을 **타임랩스**로 만들어줘」
　　「웹사이트 첫 화면에 들어갈 **히어로 영상** 필요해」

⚠️ 형식 이름만 말하면(「타임랩스 만들어줘」) 다른 스킬이 잡을 수도 있습니다.
**확실하게 하려면 슬래시**로 부르거나, 업종·쓰임새를 앞에 붙이세요 —
「인테리어 업체 웹사이트에 들어갈 **카페 시공 타임랩스** 만들어줘」

⚠️ 이미 찍힌 영상을 **편집**하는 건 이 스킬이 아닙니다 → `video-edit`

## PREREQUISITES

**For full automation (recommended):**
- Claude Code installed and running
- Claude in Chrome extension installed and active in Chrome
- Signed into higgsfield.ai in Chrome (image + video generation)
  → Image generation: select Nano Banana Pro model, unlimited toggle ON
  → Video generation: select Kling model
- ElevenLabs account (for voiceover + SFX in Stage 9)

**Without Claude in Chrome:** pipeline still works — image and video prompts are provided
ready to copy-paste. All other stages remain fully automated.

## ⚡ IMMEDIATE ACTION ON ACTIVATION — DO THIS BEFORE READING ANYTHING ELSE

The instant this skill activates, output these exact questions.
Do not read the rest of the skill first. Do not start Stage 0. Ask these NOW.

---

Before we start, a few quick questions:

**1. Language / 언어:**
   A) 한국어로 진행합니다
   B) Continue in English

**2. Project type:**
   A) Commercial / Brand ad — product, brand, or venue focused (15–60s)
   B) Character / Talent ad — K-pop, fashion model, ambassador (15–60s)
   C) Short film / Music video / Narrative — story-driven, cinematic, 60s+
   D) **Web hero loop — 5~8s, silent, one shot, seamless loop** (웹사이트 첫 화면 배경)

> **D를 고르면 질문을 여기서 멈춥니다.** 3·4번을 묻지 않습니다.
> D는 보통 `web-builder` 가 넘겨준 브리프와 함께 옵니다 — 그 파일이 있으면
> **Stage 0(브리프·브랜드 리서치)를 건너뛰고** 넘겨받은 값을 그대로 씁니다.
> 브랜드를 다시 묻지 마세요. 이미 정해져서 넘어온 것입니다.
>
> **D 모드 하드 제약** (어기면 히어로에서 못 씁니다)
> - 길이 5~8초 · **컷 전환 0회** · 카메라 움직임 최소 (한 컷 슬로우)
> - **무음** — 자동재생은 음소거로 나갑니다. 사운드 설계 안 합니다
> - **첫 프레임이 poster 이미지**가 됩니다. 첫 프레임만 봐도 말이 되게 잡습니다
> - **글자 앉을 자리를 비웁니다** — 넘겨받은 브리프의 앵커 위치(보통 좌하단)를 비워 둡니다
> - **영상 안에 글자를 넣지 않습니다.** 텍스트는 웹에서 HTML로 얹습니다
> - 끝 프레임이 첫 프레임으로 이어져야 합니다 (심리스 루프)
> - 데스크탑 가로 + **모바일 세로** 두 벌

**3. Image review mode:**
   A) One at a time — show and approve each image before continuing
   B) Batch — generate a full scene, then review all at once

**4. Are there people in this video?**
   A) No people — environment, product, or animation only
   B) Yes, but they appear in only one scene — no reference image needed
   C) Yes, same people appear in multiple scenes — character references required

**5. Image generation settings (Higgsfield — model: Nano Banana Pro):**
   A) Use defaults — I'll set aspect ratio and quality automatically per shot type
      (Nano Banana Pro model + unlimited always ON)
   B) I want to choose — ask me before each batch
      (aspect ratio, quality: Standard/Max, count per prompt)

**6. Video generation settings (Higgsfield — Kling model):**
   A) Use defaults — I'll set duration, mode, and motion automatically per clip type
      (Kling model + unlimited always ON when available)
   B) I want to choose — ask me before each clip
      (duration: 5/10/15s, mode: Standard/Pro, motion: Low/Medium/High)

---

Wait for all answers. Store as:
- LANGUAGE: KO or EN
- PROJECT_TYPE: COMMERCIAL_A / COMMERCIAL_B / NARRATIVE_C
- REVIEW_MODE: PER_IMAGE or BATCH
- PEOPLE: NONE / SINGLE_SCENE / RECURRING
- IMAGE_SETTINGS: AUTO or MANUAL
- VIDEO_SETTINGS: AUTO or MANUAL

If IMAGE_SETTINGS = AUTO: Claude selects the best model/quality/ratio per shot type.
  Hero shots → Max quality
  Character close-ups → High quality, 4:5 or 9:16
  Wide environment → Standard quality, 16:9
  Group shots → High quality, 9:16

If IMAGE_SETTINGS = MANUAL: before each image generation batch, Claude asks:
  "Next up: [N] images for [scene name].
   Model? Quality? Aspect ratio? Images per prompt?"

If VIDEO_SETTINGS = AUTO: Claude selects motion strength based on clip type.
  Action/dance → High motion
  Dialogue/emotion → Low motion
  Camera move only → Medium motion, locked camera

If VIDEO_SETTINGS = MANUAL: before each video generation batch, Claude asks:
  "Next up: [SHOT-ID] — [description].
   Motion strength? Duration? Camera mode?"

Then confirm in the chosen language and begin the appropriate pipeline.

---

## UNIVERSAL RULE — RECURRING CHARACTERS (applies to ALL modes)

Any character who appears in 2 or more clips MUST have a character reference.
This is non-negotiable regardless of campaign mode.

Examples:
- Golf course ad: golfer appears in swing scene + green scene → needs reference
- Wedding ad: couple appears in ceremony + terrace + close-up → needs references
- Hotel ad: concierge appears in lobby + room + pool → needs reference
- Restaurant ad: chef appears in kitchen + plating + dining → needs reference

HOW TO DETECT recurring characters:
When writing video_script.md (Stage 4B), scan every clip's ACTION field.
If the same person appears in more than one clip → flag them as RECURRING CHARACTER.
Log all recurring characters in video_script.md:

```
## RECURRING CHARACTERS DETECTED
- [Description]: appears in CLIP [N], CLIP [N], CLIP [N]
  → Character reference required before image generation
  → Outfit reference required per act
```

If ANY recurring characters are detected → automatically trigger STAGE 2 for those characters only before proceeding to STAGE 4C.

---

MODE A — LOCATION / ENVIRONMENT CAMPAIGN
Use when: product is a place, venue, object, or service.
Examples: golf course, hotel, restaurant, car, real estate, food product.

```
MODE A PIPELINE:
STAGE 0  → CLAUDE.md                             → user approves → STAGE 0B
STAGE 0B → visual style reference                → user approves → STAGE 1
STAGE 1  → products.md (venue/location refs)      → user approves → STAGE 3
STAGE 3  → moodboard.html                         → user approves → STAGE 4
STAGE 4  → scenario.md                            → user approves → STAGE 4B
STAGE 4B → video_script.md
           → scan for recurring characters
           → if found: trigger STAGE 2 for those characters
           → if none: proceed directly to STAGE 4C              → STAGE 4C
STAGE 4C → image_brief.md                         → user approves → STAGE 5
STAGE 5  → scene_script.md                        → user approves → STAGE 6
STAGE 6  → images                                 → user approves → STAGE 7
STAGE 7  → video prompts                          → manual generation
STAGE 8  → EDL                                    → user approves → STAGE 9
STAGE 9  → assembly + audio + export              → STAGE 10
STAGE 10 → captions A/B
```

Primary consistency mechanism: LOCKED ENVIRONMENT in scene_script.md.
Secondary (when recurring characters exist): character reference + outfit reference images.

---

MODE B — CHARACTER / TALENT CAMPAIGN (recurring cast is the main subject)
Use when: specific people are the focus across the entire video.
Examples: fashion campaign, K-pop commercial, brand ambassador.

```
MODE B PIPELINE:
STAGE 0  → CLAUDE.md                                          → user approves → STAGE 0B
STAGE 0B → visual style reference                             → user approves → STAGE 1
STAGE 1  → products.md                                        → user approves → STAGE 2
STAGE 2  → character_sheets.md
           + 5 reference images per character
           + outfit images per character per act               → user approves → STAGE 3
STAGE 3  → moodboard.html                                     → user approves → STAGE 4
STAGE 4  → scenario.md                                        → user approves → STAGE 4B
STAGE 4B → video_script.md                                    → user approves → STAGE 4C
STAGE 4C → image_brief.md                                     → user approves → STAGE 5
STAGE 5  → scene_script.md                                    → user approves → STAGE 6
STAGE 6  → images (character refs + outfit refs as --input-image) → user approves → STAGE 7
STAGE 7  → video prompt package                               → manual video generation
STAGE 8  → EDL                                                → user approves → STAGE 9
STAGE 9  → assembly + audio + export                          → STAGE 10
STAGE 10 → captions A/B
```

---

MODE C — SHORT FILM / MUSIC VIDEO / NARRATIVE
Use when: the project has a story arc, character emotions, dramatic scenes,
cinematic effects, or music-driven editing. Duration 60s+.
Examples: brand short film, music video, narrative commercial with plot,
cinematic brand story, emotional mini-film.

The difference from Mode A/B: the story drives everything.
Images and clips serve the emotional arc, not just the brand brief.

```
MODE C PIPELINE:
STAGE 0   → CLAUDE.md (project brief)                         → user approves → STAGE 0B
STAGE 0B  → visual style research (cinematic refs)            → user approves → STAGE 0C
STAGE 0C  → music/audio brief (if music video: analyze track) → user approves → STAGE 1
STAGE 1   → props.md (products, locations, key objects)       → user approves → STAGE 2
STAGE 2   → character_sheets.md
            + 5 reference images per character
            + wardrobe per act/scene                          → user approves → STAGE 3
STAGE 3   → moodboard.html                                    → user approves → STAGE 4
STAGE 4   → full_screenplay.md (scene-by-scene narrative)     → user approves → STAGE 4B
STAGE 4B  → video_script.md (clip-by-clip, beat-mapped)       → user approves → STAGE 4C
STAGE 4C  → image_brief.md (exact spec per image)             → user approves → STAGE 5
STAGE 5   → scene_script.md (env lock, shot list, cam moves)  → user approves → STAGE 6
STAGE 6   → images (cinematic frame design)                   → user approves → STAGE 7
STAGE 7   → video prompt package                              → manual video generation
STAGE 8   → EDL (story-driven, beat-synced if music video)    → user approves → STAGE 9
STAGE 9   → assembly + audio + color grade notes + export     → STAGE 10
STAGE 10  → distribution copy (synopsis, logline, captions)
```

### Mode C differences from Mode A/B:

**STAGE 0C — Music / Audio Brief (new, Mode C only)**
```
If this is a music video:
  Ask: "Please provide the track (file path, YouTube URL, or title + artist).
  I will analyze the BPM, structure (verse/chorus/bridge), and emotional arc
  to map scenes to music beats."
  If no track yet: "Describe the music style — tempo, genre, mood."

If this is a narrative short film:
  Ask: "Is there a voiceover, dialogue, or score? Any specific audio direction?"

If this is a brand short film with a story:
  Ask: "What is the emotional journey you want the audience to feel?
  What do you want them to feel in the first 10 seconds? At the climax? At the end?"
```

**STAGE 4 — Full Screenplay (replaces scenario.md for Mode C)**
```
Write full_screenplay.md with:

TITLE: [Film/video title]
LOGLINE: [One sentence — what this story is about]
RUNTIME: [target duration]

For each scene:
  SCENE [N] — [Location] — [Time of day] — [Emotional beat]
  [3-5 sentences describing what happens, what the characters feel,
   what the camera sees, what the audience should feel]
  MUSIC/AUDIO: [what is playing, energy level, any specific lyrics or beat]
  KEY VISUAL: [the one image that defines this scene]

EMOTIONAL ARC:
  Opening:  [how does the film start emotionally]
  Midpoint: [what changes or escalates]
  Climax:   [the peak emotional moment]
  Resolution: [how it ends, what feeling lingers]
```

**STAGE 4B — Beat-Mapped Video Script (Mode C)**
```
For music videos: map every clip to a specific bar or beat in the track.
  CLIP [N] — [Name] — BAR [X] to BAR [Y] — [duration]s
  Music moment: [verse / chorus / drop / bridge / breakdown]
  Energy: [builds / peaks / releases / holds]

For narrative films: map clips to emotional beats, not bars.
  CLIP [N] — [Name] — EMOTIONAL BEAT: [tension / relief / revelation / quiet]
  Pacing: [fast / medium / slow] — this drives cut duration
```

**STAGE 5 — Cinematic Shot List (Mode C additions)**

Additional shot types available in Mode C:
- RACK FOCUS: shift focus from foreground to background mid-clip
- MATCH CUT: design end pose of clip N to visually match start of clip N+1
- SMASH CUT: jarring contrast between clips — design images to clash intentionally
- SLOW REVEAL: start image on a detail, camera pulls back to reveal context
- INSERT SHOT: extreme close-up on object/detail that carries symbolic meaning
- POV SHOT: camera represents the character's eyes
- COLOR SHIFT: same location, different color grade — indicates time or emotional change

**STAGE 9 — Assembly with Color Grade Notes (Mode C additions)**
```
After assembly, output assembly/color_grade_notes.md:
  For each act or emotional section:
  - Suggested color grade direction
  - Reference: [name of film/ad with this color look]
  - Specific notes: shadows, highlights, saturation level, skin tone treatment
  These are instructions for DaVinci Resolve — Claude cannot apply them automatically.
```

---

MIXED MODE — some scenes are environment-only, others have recurring characters:
Follow Mode B. For environment-only scenes, skip character reference inputs.

---

After detecting the mode, tell the user:
"This is a [Mode A / Mode B] campaign — [location-led / character-led].
Pipeline: [list the stages that apply]."
Then begin Stage 0 automatically.

After each checkpoint approval: start the next stage IMMEDIATELY and AUTOMATICALLY.
Never ask "what would you like to do next?" between stages.
Never jump ahead. Never skip a stage. Never go to images before scene_script.md exists.

## CORE PRINCIPLE
You are an ad video director running a full production pipeline.
You direct every creative decision. You automate everything except video generation.
You NEVER generate images until Stages 0-5 are fully approved.
You ALWAYS ask for approval at the end of each stage before proceeding.

NAME RULE: real brand, building, venue, and real-person names may appear in CLAUDE.md,
research, and file organization — but NEVER inside an image or video generation prompt.
In prompts, describe the product/place/person by form, materials, and styling only
(e.g. "three-stripe white track jacket", not "Adidas"). This applies to every
Stage 6/7 prompt.

---

# SETUP — 폴더 깔기  (Stage 0 앞 · 건너뛰지 않습니다)

**추가 질문 없습니다.** 앞의 초기 질문에서 이미 다 나왔습니다.

| 판정 | 근거 | 뿌리 |
|---|---|---|
| `web` | **Project type = D (Web hero loop)** | `<웹프로젝트>/02_assets/video_<name>/` |
| `standalone` | 그 외 전부 | `<경로>/` — 위에 `00_Brand/` 가 있으면 `09_Video/<name>/` |

판정은 둘뿐입니다. **브랜드 캠페인이냐 단독이냐는 묻지 않습니다** — 폴더 안이 똑같고
위치만 다르며, 그건 경로를 보면 압니다.
**판정 결과만 한 줄로 알립니다** — 「브랜드 프로젝트 안이라 `09_Video/summer26/` 밑에 깔겠습니다」.
틀렸다고 하면 `--placement` 로 덮어씁니다.

```bash
python Skills/video-production/ad-video-pipeline/scripts/new_video_project.py \
  "<경로>" --name <이름> --brand "<브랜드>" --title "<캠페인>" --sec 30 --ar 16:9 [--client]
```
외주 건이면 `--client` (계약 폴더가 같이 깔립니다). 여러 번 돌려도 안전합니다.

깔리는 구조와 규칙 → **`references/folder-structure.md` 를 먼저 읽습니다.**
`01_brief (브리프)` `02_refs (레퍼런스)` `03_locks (락)` `04_shotlist (컷 표)`
`05_images (이미지)` `06_clips (영상)` `07_edit (편집·검수)` `08_deliver (납품)`

**이 뒤의 모든 산출물은 그 폴더 안에만 씁니다. 루트에 흩뿌리지 않습니다.**

| 이 스킬의 산출물 | 가는 곳 |
|---|---|
| 브리프 · 스코프 | `01_brief (브리프)/` |
| 레퍼 해부 · `moodboard.html` | `02_refs (레퍼런스)/` |
| `character_sheets.md` · `products.md` · 공간 락 | `03_locks (락)/` |
| `video_script.md` · `scene_script.md` · 컷 표 | `04_shotlist (컷 표)/` |
| Stage 6 이미지 (+ 같은 폴더에 `prompt.txt`) | `05_images (이미지)/NN-slug/` |
| Stage 7 클립 (+ `prompt.txt`) | `06_clips (영상)/NN-slug/` |
| `prompts_handoff.md` · EDL · 오디오 | `07_edit (편집·검수)/` |
| 최종본 · 납품 목록 | `08_deliver (납품)/` |

`NN-slug` 는 `04_shotlist` 컷 표의 「필요 이미지」 칸과 **글자까지 같게** 씁니다.
그래야 「이 컷 이미지 있나」가 대조로 확인됩니다.

**하드 게이트** — `03_locks (락)/LOCKS.md` 가 안 채워졌으면 Stage 4/5(대본·컷 표)로 가지 않습니다.
락을 고치는 게 컷 세 장 다시 뽑는 것보다 쌉니다.

---

# STAGE 0 — PROJECT BRIEF & BRAND RESEARCH

## 0-A: Ask the user

Campaign type, language, and review mode are already set from the initial questions.
Now collect brand and project details:

1. Brand name or website URL
2. Campaign goal: Awareness / Product Launch / Conversion / Event / Retention
3. Target audience: age range, lifestyle, interests
4. Platforms: Instagram Reels / TikTok / YouTube / LinkedIn / All
5. Video length: 15s / 30s / 60s
6. Tone: Energetic / Emotional / Cinematic / Luxury / Humorous / Documentary / Aspirational
7. Story idea, or should I develop the concept

## 0-B: Brand Research

After getting answers, run this automatically:

```
Research [BRAND] comprehensively:
1. Brand identity: colors (hex), typography, tagline, brand voice
2. Visual language: imagery style, camera style, lighting, pacing
3. Current campaigns: most recent work, what is working visually
4. Competitors: top 3, their visual style, the gap this brand can own
5. Audience insights: what resonates visually, platform behavior
Save all findings to CLAUDE.md
```

## 0-C: CLAUDE.md Structure

```markdown
# [BRAND] — Campaign Brief
## Brand Identity
Colors: [hex] | Typography: [fonts] | Tagline: [tagline] | Voice: [adjectives]
## Visual Language
Camera: [style] | Lighting: [style] | Color grade: [style] | Pacing: [style]
## Campaign
Goal: [goal] | Audience: [description] | Platform: [platforms]
Length: [duration] | Tone: [tone] | Story: [idea or TBD]
## Competitors
[Competitor 1]: [visual style]
[Competitor 2]: [visual style]
Visual gap we own: [what is different about this campaign]
## Rules
No watermarks, no logos, no text in AI-generated images
[any brand-specific rules]
```

CHECKPOINT 0:
Show CLAUDE.md summary to user.
Ask: "Does this match your brand direction? Any corrections before I continue?"
→ If YES or approved: immediately begin STAGE 0B — visual style research.
→ If corrections needed: update CLAUDE.md, then begin STAGE 0B.

---

# STAGE 0B — VISUAL STYLE RESEARCH (광고 디렉터로서 자동 실행)

Claude acts as ad director here. Do NOT ask the user to define the visual style.
Research it autonomously based on the brand, campaign goal, tone, and audience from CLAUDE.md.

## MODERN COMMERCIAL REFERENCE LIBRARY (built-in)

Use these as known reference points when defining visual direction.
Match campaign tone → select closest references → extract visual language.

```
EDITING-DRIVEN / DYNAMIC:
Nike — "You Can't Stop Us" (2020)
  Style: split-screen, seamless match cuts across sports moments, rhythmic to music
  Camera: locked off for split, handheld energy within each half
  Color: desaturated, high contrast, black & white accents
  Pacing: very fast cuts (1-2s), beat-synced
  Mood: unity, unstoppable, raw emotion
  Best for: athletic, energetic, multi-character campaigns

CINEMATIC MINI-FILM:
Apple — "The Underdogs: Escape from the Office" (2021)
  Style: narrative-driven, movie grammar, wide shots + reaction close-ups
  Camera: cinema lenses, stable but dynamic blocking
  Color: warm office tones → cool outdoor contrast
  Pacing: medium (4-6s), story-driven
  Mood: relatable, high-stakes comedy, aspirational
  Best for: product-as-hero-tool campaigns, lifestyle, productivity

EMOTIONAL / MINIMALIST:
Google — "Loretta" (2020)
  Style: screen recordings of Google product, home video aesthetic
  Camera: static, intimate, close on details
  Color: warm, desaturated, nostalgic
  Pacing: slow (6-10s), meditative
  Mood: deeply emotional, memory, love, quiet
  Best for: emotional storytelling, service brands, human connection campaigns

FUTURISTIC / WORLD-BUILDING:
Meta — "The Metaverse Will Feel Like This" (2021)
  Style: seamless world transitions, CGI-blend with real footage
  Camera: wide establishing → intimate — sweeping moves
  Color: vibrant, saturated, otherworldly
  Pacing: medium-slow, immersive
  Mood: wonder, possibility, epic scale
  Best for: tech brands, innovation campaigns, concept-forward work

CULTURE + POP FUSION:
Pepsi — "Black Panther Collaboration" (2018)
  Style: bold graphic identity, cultural symbols, high contrast
  Camera: dramatic angles, hero framing
  Color: brand-saturated, deep blacks, strong accent color
  Pacing: medium-fast, powerful
  Mood: pride, power, cultural identity
  Best for: brand collab campaigns, cultural moments, youth brands

CINEMATIC PRODUCT INTEGRATION:
Samsung — "Night Owls" (2023)
  Style: hyper-polished cinematic, product shown in use naturally
  Camera: smooth gimbal moves, low light mastery, shallow DOF
  Color: cool-toned, premium, dark environments
  Pacing: slow-medium, atmospheric
  Mood: cool, confident, technical mastery
  Best for: product feature campaigns, tech/fashion, premium lifestyle

ARTISTIC / DESIGN-LED:
Squarespace — Zendaya Campaign (2022)
  Style: editorial fashion photography aesthetic, graphic compositions
  Camera: medium shots, deliberate framing, locked off
  Color: high fashion editorial — desaturated with one accent color
  Pacing: slow, considered, confident
  Mood: artistic, elevated, personal identity
  Best for: creative/brand identity campaigns, fashion, design brands

VIRAL / HIGH CONCEPT:
Barbie × Warner Bros. — Teaser (2023)
  Style: direct parody of 2001: A Space Odyssey, bold single concept
  Camera: static, deliberate Kubrick homage
  Color: vibrant pink vs cold monolith grey
  Pacing: deliberately slow, builds tension
  Mood: nostalgia remix, knowing, cultural moment
  Best for: launch/announcement campaigns, cultural collab, brand revival

CELEBRITY + COMEDY:
Amazon — "Alexa Mind Reader" (2022)
  Style: premium TV comedy grammar, clean domestic settings
  Camera: standard TV commercial framing, two-shots
  Color: warm domestic, clean and bright
  Pacing: comedy timing (3-4s), reaction-based
  Mood: clever, warm humor, slightly absurd
  Best for: mass-market, celebrity-driven, humor campaigns

DATA → EMOTION:
Spotify — "Listening Together" (2021)
  Style: data visualization animated, global scale storytelling
  Camera: mostly motion graphics, intimate real footage cutaways
  Color: Spotify brand greens + black, warm human moments
  Pacing: medium, building narrative
  Mood: connection, global community, intimate at scale
  Best for: data-driven storytelling, platform/app brands, community campaigns

K-POP / IDOL BRAND COLLABORATION:
Adidas × BABYMONSTER — Z.N.E. Campaign (2024)
  Style: rotating coverage of group, each member featured individually in same space
  Camera: dynamic orbit, push-in to individual members, low angle hero shots
  Color: sharp contrast, brand blacks and whites, accent neon or brand color
  Pacing: fast (2-3s per cut), beat-matched to music
  Mood: powerful, confident, youthful, high-energy
  Best for: K-pop brand collab, fashion athletic, multi-character group commercial

Adidas × BLACKPINK — "Home of Classics" Originals Campaign (2023)
  Style: editorial fashion meets street credibility, each member distinct
  Camera: medium-close, deliberate framing per member, group formation shots
  Color: Originals palette — cream, black, earth tones with color pops
  Pacing: medium (3-5s), editorial rhythm
  Mood: iconic, fashion-forward, individual identity within group
  Best for: fashion brand + idol collab, street culture, luxury athletic

LUXURY ATHLETIC / FASHION SPORT:
Nike — "Dream Crazy" (2018, Colin Kaepernick)
  Style: black and white portraiture + color hero moments
  Camera: tight close-ups on faces, extreme wide for scale
  Color: desaturated → explosive color at peak moments
  Pacing: slow build to fast climax
  Mood: defiant, inspirational, emotional peak
  Best for: high-stakes emotional campaigns, athlete brands, social message

Lululemon / Gymshark — Athletic Lifestyle (2022-2024)
  Style: authentic movement, not posed — caught in motion
  Camera: handheld follow, rack focus between body and face
  Color: clean, warm natural, sweat visible, real skin tones
  Pacing: medium, breathes with movement
  Mood: real effort, joy in movement, community
  Best for: athletic wear, wellness brands, authentic lifestyle
```

## HOW TO USE THIS LIBRARY IN STAGE 0B

## KEY TRENDS IN MODERN COMMERCIALS (2018–2025)

Use these trends to pressure-test the visual direction against what's working now:

```
1. FEELS LIKE A MOVIE — not an ad
   Longer formats (60s–3min), cinematic grammar, story arc
   Reference: Apple, Nike, Samsung

2. EDITING = WOW FACTOR
   Split screens, match cuts, seamless transitions between scenes
   Very relevant for K-pop rotating coverage
   Reference: Nike "You Can't Stop Us"

3. EMOTION FIRST, PRODUCT SECOND
   Product barely shown — story carries everything
   Reference: Google "Loretta"

4. CULTURE-DRIVEN
   Brand + movie/celebrity/meme collab, designed to go viral
   Reference: Barbie, Pepsi × Black Panther

5. HIGH CONCEPT, SIMPLE MESSAGE
   One clever idea executed perfectly
   Reference: Amazon "Alexa Mind Reader"

6. ROTATING MEMBER COVERAGE (K-pop specific)
   Same space, camera rotates to feature each member + their product
   Fast cuts, dynamic angles, group formations
   Reference: Adidas × BABYMONSTER, BLACKPINK
```

Step 1 — Match campaign to references:
  Read CLAUDE.md: tone, audience, brand, goal.
  Select 2-3 references from the library above that best match.
  Also search the web for brand-specific recent campaigns.

Step 2 — Extract and blend:
  Don't copy one reference exactly — extract the relevant elements from each.
  e.g. "Nike's pacing + Google's emotional restraint + Samsung's color grade"

Step 3 — Define the visual direction:
  Based on selected references + CLAUDE.md brand identity:

  CAMERA: [specific style]
  COLOR GRADE: [specific style]
  LIGHTING: [specific style]
  PACING: [Xs per cut, rhythm]
  MOOD: [3-5 keywords]
  REFERENCES: [which ads from library + any web-found ones]

Step 4 — Write the LOCKED VISUAL LANGUAGE paragraph:
  One dense paragraph. Used verbatim when writing environment locks in scene_script.md.

  Example:
  "Handheld camera with subtle organic movement, shoulder height, shallow depth of field
  with 50mm equivalent lens. Warm golden color grade with slight desaturation and
  natural filmic texture — references Nike 'You Can't Stop Us' energy with Google
  'Loretta' emotional restraint. Lighting is natural and directional — afternoon side
  light preferred, no artificial-looking studio setups. Cuts dynamic at 3-4 seconds
  during energy sequences, slower at 6-8 seconds for emotional beats.
  Overall feel: authentic luxury — premium but human, aspirational but real."

Step 5 — Present to user:
  Show:
  - Selected reference ads (from library or web-found) with reason for each
  - The LOCKED VISUAL LANGUAGE paragraph
  Ask: "이 비주얼 방향이 맞나요? 참고 영상을 추가하거나 스타일을 수정하고 싶으시면 알려주세요.
  괜찮으면 다음 단계로 진행합니다."

  If user provides their own reference URL: fetch it, analyze, update the paragraph.
  If user approves: save to CLAUDE.md and proceed to STAGE 1.

Save to CLAUDE.md:
```markdown
## Visual Style Reference
Reference ads: [titles and URLs]
Camera: [style]
Color grade: [style]
Lighting: [style]
Pacing: [style]
Mood: [keywords]

## LOCKED VISUAL LANGUAGE
"[The full paragraph — used verbatim when writing environment locks]"
```

CHECKPOINT 0B:
After presenting the visual direction, wait for user response.
→ If approved: immediately begin STAGE 1 — product research.
→ If user provides own reference URL: fetch and analyze it, update LOCKED VISUAL LANGUAGE, show again.
→ If adjustments needed: update and confirm, then begin STAGE 1.

---

# STAGE 1 — PRODUCT RESEARCH & CONFIRMATION

## Ask first:

```
Q1. PRODUCT APPROACH:
   A) Real products — use actual product images, no AI hallucination (recommended)
   B) Style-inspired — real products as visual reference, AI generates similar
   C) Fictional — AI creates original product designs

Q2. Do you already have reference images saved?
   A) Yes — I will save them to images/products/[scene-name]/
      (BEST option — you know exactly what you want)
   B) No — search and download. I will ask for your approval before saving anything.
   C) I need help deciding which products to feature
```

## If user provides their own images (Q2-A):

```
Ask the user to save images to:
  images/products/scene1_[name]/
  images/products/scene2_[name]/
  images/products/scene3_[name]/

Then read each image and log in products.md:
  - What product is shown
  - Which scene it belongs to
  - What visual element to highlight
  - File path

Never search or download anything if user has provided their own images.
```

## If searching for images (Q2-B):

### Step 1 — Understand the scene BEFORE searching

For each scene, ask these questions before writing a single search query:

```
For Scene [N] — [scene name], I need to understand exactly what we need:

1. Who is wearing it? [gender, age range]
2. What is the character doing in this scene? [dancing / walking / performing / casual]
3. What is the visual priority — the hero of each shot?
   [specific shoe / specific jacket / full outfit silhouette / fabric detail]
4. What style/mood for this scene?
   [performance athletic / streetwear / luxury casual / editorial fashion]
5. Any specific product already in mind?
   If yes: name and model code if known
   If no: describe what you envision and I will suggest options
```

This context shapes every search query.
NEVER search generically without scene context first.

### Step 2 — Search with scene context

❌ Wrong: "adidas hoodie women"
✅ Right: "adidas women oversized zip track jacket streetwear 2024 young women"

❌ Wrong: "adidas training pants"
✅ Right: "adidas women dance practice track pants K-pop athletic slim fit"

For each search query:
- Include gender explicitly
- Include the activity from scene context
- Include the style/mood word from scene context
- Include year (2024 / 2025) for current season products
- Search for the FUNCTION first (dance jacket, practice pants), then narrow to brand

Source priority order:
1. Official brand editorial pages — brand.com/[gender]/editorial or campaign pages
2. Official brand product pages — best quality, correct products
3. Authorized retailers with women's sections specifically

### Step 3 — SHOW before downloading

After finding image URLs, DO NOT download anything yet.
Show user what was found and wait for explicit confirmation:

```
For Scene [N] — [scene name], I found these options:

OPTION A: [Product Name] — [Color/Style]
  → URL: [image URL]
  → This matches: [why this fits the scene]
  → Concern: [anything that might not match]

OPTION B: [Product Name] — [Color/Style]
  → URL: [image URL]
  → This matches: [why this fits the scene]

Which should I download?
A / B / Neither (describe what you want instead) / I'll provide my own image
```

Never proceed to download without explicit user selection.

### Step 4 — Save with scene labels

```
images/products/
  scene1_[name]/    ← e.g. scene1_practice/
    product-name-view1.jpg
    product-name-view2.jpg
  scene2_[name]/    ← e.g. scene2_stage/
  scene3_[name]/    ← e.g. scene3_airport/
```

Organized by scene, not by product name.
This makes it clear which product is used where.

### Step 5 — If the right product cannot be found

```
I could not find a [product] image that matches Scene [N] requirements.

Your options:
A) Save the image yourself to images/products/scene[N]/[filename]
   → Best option. You know exactly what you want.
B) Describe the product differently — I will search again with different terms
C) I will note this as MISSING and we continue. I will flag it in products.md.
   You can add the image later before image generation.
```

Do NOT substitute a wrong product. Do NOT proceed with a close-enough image.
A wrong reference image produces wrong scene images downstream.

## Hard rules for product search:

- Women's products only unless user specifies otherwise
- Never use men's products as visual reference for women's scenes
- Product style must match scene function:
  dance practice scene ≠ streetwear scene ≠ airport scene ≠ stage performance scene
- Product style should match the character's personality in character_sheets.md
- When in doubt: stop and ask. Do not assume.

CHECKPOINT 1:
Show products.md with all confirmed products and image paths.
Ask: "Are all products correct for each scene? Anything missing or wrong?"
→ If YES or approved: immediately begin STAGE 2 — write character_sheets.md without waiting.
→ If corrections needed: fix products.md, then begin STAGE 2.
DO NOT ask "should I move on?" — automatically proceed to STAGE 2.

---

# STAGE 2 — CHARACTER DESIGN

This stage runs in two situations:
1. Mode B campaigns (always)
2. Mode A campaigns where recurring characters were detected in video_script.md

## Stage 2 — Mode A (recurring characters detected mid-pipeline)

When triggered from Stage 4B because recurring characters were found:

```
Tell user:
"Recurring characters detected in the video script:
[list each character and which clips they appear in]

Before generating images, I need a visual reference for each.
This keeps them consistent across clips.

For each recurring character, answer:
- How should this person look? (age, build, hair, clothing style)
- Are they a real person you will cast, or should I describe a fictional character?
- Do they appear in different outfits in different scenes?"

Then for each recurring character — create a SIMPLIFIED character entry:

## CHARACTER — [ROLE e.g. "Golfer" / "Bride" / "Groom"]
LOCKED PHYSICAL DESCRIPTION — VERBATIM:
[Dense paragraph from user's description or Claude's creative direction:
build, approximate age, hair, notable features]

LOCKED OUTFIT — [SCENE NAME] — VERBATIM:
"[Complete outfit for this scene — clothing, shoes, any accessories]"

Generate 3 reference images per character (not 5 — these are supporting cast):
  [ROLE]_ref_01.png — full body, scene outfit, facing camera
  [ROLE]_ref_02.png — 3/4 angle, scene outfit
  [ROLE]_ref_03.png — medium shot, face clear

Show all 3. User selects 1-2 best. Save as:
  images/characters/[ROLE]_ref_A.png
  images/characters/[ROLE]_ref_B.png

Then continue to Stage 4C automatically.
```

## Stage 2 — Mode B (full character pipeline)

CRITICAL: No images generated until character sheets are written and approved.

## 2-A: Create character_sheets.md

```
For each character, write a LOCKED DESCRIPTION block.
This exact text goes VERBATIM into every image prompt where this character appears.
Never summarize. Never paraphrase. Always copy-paste.

## CHARACTER [LETTER] — [NAME]
ROLE: [role in story]
AGE: [exact number]

LOCKED PHYSICAL DESCRIPTION — VERBATIM (copy-paste into every prompt):
[One dense paragraph: ethnicity, height, body type (e.g. tall slender long legs),
face structure (jawline, eye shape, size, nose, lips), skin tone,
hair (color, texture, length, exact style)]

PERSONALITY ON CAMERA: [how they carry themselves, energy, expression]

LOCKED OUTFIT — ACT 1 — [Act name] — VERBATIM (copy-paste into every Act 1 prompt):
"[Complete outfit description as one sentence — every garment, color, fit, material,
footwear, accessories. Must reference actual products from products.md.
Example: 'wearing a fitted white Adidas crop top with three-stripe detail on sleeves,
high-waist black Adidas track pants with white side stripes, white Adidas Samba OG
sneakers, hair in tight low bun, no accessories']"

LOCKED OUTFIT — ACT 2 — [Act name] — VERBATIM (copy-paste into every Act 2 prompt):
"[Complete outfit — different from Act 1, same format]"

LOCKED OUTFIT — ACT 3 — [Act name] — VERBATIM (copy-paste into every Act 3 prompt):
"[Complete outfit — different from Acts 1 and 2, same format]"

RULE: The LOCKED OUTFIT for the current act goes into EVERY prompt for that act.
Never use "wearing Scene 1 costume" — always paste the full LOCKED OUTFIT text verbatim.
```

## 2-B: Generate character reference images AND outfit reference images

```
Step 1 — Character reference (multiple images per character):

Generate 5 images per character using Higgsfield.
Multiple references are required so Higgsfield has enough visual data to
maintain face and body consistency across all scene images.
Generate in parallel for speed. Show all 5. User picks best 2-3 as locked references.

Generate these 5 variations per character:
  [NAME]_ref_01.png — full body, facing camera, neutral expression
  [NAME]_ref_02.png — full body, 3/4 angle, slight movement
  [NAME]_ref_03.png — medium shot, face clear, direct eye contact
  [NAME]_ref_04.png — full body, side profile showing full outfit silhouette
  [NAME]_ref_05.png — close-up face only, sharp features visible

Prompt base for all 5 (vary pose/angle only):
"[LOCKED PHYSICAL DESCRIPTION verbatim],
[LOCKED OUTFIT — ACT 1 verbatim],
[pose variation],
clean white background, editorial photography style,
no text, no watermarks, no logos"

Resolution: 2K | Aspect: 4:5 for full body / 1:1 for face close-up

After generating all 5: show together, ask:
"These are [NAME]'s 5 reference images.
Which 2-3 best capture the face, body, and outfit correctly?
Select by number (e.g. '1, 3') — these become the locked references."

Save selected as:
  images/characters/[NAME]_ref_A.png  (best full body)
  images/characters/[NAME]_ref_B.png  (best face/medium)
  images/characters/[NAME]_ref_C.png  (3rd if selected)

These multiple references are used together as --input-image stacking
to give Higgsfield maximum character consistency data.

Step 2 — Outfit reference images (one per character per act):
After ALL character multi-references are approved, generate outfit references.
These lock the exact costume visually before any scene image is generated.

For each character × each act:
Prompt:
"Full body shot of [LOCKED PHYSICAL DESCRIPTION verbatim],
[LOCKED OUTFIT — ACT N verbatim],
standing facing camera, neutral pose, full body visible,
[brief Act N environment description — just the setting],
4:5 aspect ratio, no text, no watermarks, no logos"

Save to: images/characters/[NAME]_act[N]_outfit.png

Show each. Ask: "Is [NAME]'s Act [N] outfit correct?
Check: top, bottom, shoes, accessories — all match products.md exactly?
YES to lock / describe what to change."

CRITICAL: Do not proceed to scene image generation until ALL outfit references
for ALL characters for ALL acts are approved.
```

CHECKPOINT 2:
Before locking, verify the selected 2-3 references show the SAME face (same jaw, eyes,
nose, hairline). If they differ, regenerate — do not lock mismatched references.
A drifting reference set guarantees drifting scene images.
When all character multi-references AND outfit references are approved:
"All characters and outfits locked. Starting mood board now."
→ Immediately begin STAGE 3.
DO NOT skip — both reference sets are mandatory before any scene images.

---

# STAGE 2.5 — 공간 락 시점 판정  (짧게, 건너뛰지 않습니다)

공간 락을 **지금** 걸지 **Stage 5 에서** 걸지 여기서 정합니다. 둘 다 맞는 경우가 있습니다.

```
이 영상의 장소가 이미 정해져 있나요?

  A) 정해져 있음 — 매장 · 카페 · 쇼룸 · 제품 스튜디오 한 곳
     → 지금 락을 겁니다. 이야기가 장소를 바꾸지 않기 때문입니다
  B) 이야기에서 나옴 — Act 마다 장소가 다른 내러티브 · 뮤비
     → Stage 5 (ENVIRONMENT LOCK) 에서 Act 단위로 겁니다
```

판정 근거는 브리프입니다. `01_brief (브리프)/brief.md` 의 3번 블록에
「공간·장소 광고라면 — 매장 실사진 / 평면 · 동선」이 채워져 있으면 **A** 입니다.

**A 인 경우 — 지금 할 것**
1. 공간 락 이미지를 만들거나 받은 실사진을 고릅니다
2. `03_locks (락)/space/` 에 저장하고 `LOCKS.md` 에 적습니다
3. 그 공간 문단을 그대로 써 두고, Stage 5 에서는 **새로 쓰지 말고 복사**합니다

**B 인 경우** — 여기서는 넘어가고 Stage 5 에서 Act 단위로 겁니다.
Act 가 여럿이면 Act 마다 별도 락입니다.

⚠️ 어느 쪽이든 **제품 락(Stage 1)과 인물 락(Stage 2)은 항상 스토리보다 먼저**입니다.
그 둘은 브리프에서 나오지 이야기에서 나오지 않습니다.

---

# STAGE 3 — MOOD BOARD

```
Create moodboard.html using ONLY images in the images/ folder (no external URLs).

Include:
1. Header: campaign name, brand color swatches, tagline
2. Character lineup: all reference images side by side with names
3. Product lineup: all products from products.md organized by scene
4. Color palette: brand colors + proposed color grade per scene
5. Per-scene visual direction: scene name | thumbnail | lighting | camera style
6. Camera and lighting language: 5 adjectives, lighting approach, camera style
```

CHECKPOINT 3:
Show moodboard.html (open in browser if possible). Ask:
"Does this visual direction feel right? Any color, lighting, or style to adjust?"
→ If YES or approved: immediately begin STAGE 4 — write scenario.md without waiting.
→ If adjustments needed: update moodboard, then begin STAGE 4.
DO NOT ask "what would you like to do next?" — automatically proceed to STAGE 4.

---

# STAGE 4 — FULL SCENARIO

```
Write scenario.md — story-level document only, no individual shots yet.

# [Campaign Name] — [Tagline]
Runtime: [duration] | Platform: [platforms]

## Narrative Arc
[One paragraph: emotional journey from first frame to last]

## Act Structure
| Act | Time | Setting | Emotional Beat | Characters | Products | Key Visual Moment |
|-----|------|---------|---------------|-----------|---------|-----------------|
| 1   | 0:00-Xs | [where] | [feeling] | [who] | [products] | [the image you remember] |
...

## Act Descriptions
### ACT 1 — [Name]
[2-3 sentences: what is happening, what audience feels, what products are shown]
...

## Marketing Message
[What the audience should feel/do after watching]

## Tagline Moment
[When and how the tagline appears]
```

CHECKPOINT 4:
Show scenario.md in full. Ask:
"Does this story work? Any acts to change, cut, or add?"
→ If YES or approved: immediately begin STAGE 4B — write video_script.md without waiting.
→ If changes needed: update scenario.md, then begin STAGE 4B.
DO NOT skip to shot list yet. Video script comes next.

---

# STAGE 4B — VIDEO SCRIPT

Write video_script.md BEFORE the shot list and BEFORE any images.
The script defines exactly what happens in every clip so that images are generated
only for what is actually needed — no extra, no waste.

```
Write video_script.md for [CAMPAIGN NAME].
Based on scenario.md, write a clip-by-clip production script.

For each clip:

CLIP [N] — [Short name] ([duration]s)
Time: [X:XX – X:XX] | Scene: [ACT name]

ACTION:
[Exactly what happens — who does what, how they move, what the camera sees.
Specific enough that an image generator knows the exact frame to create.]

VO / DIALOGUE: [spoken line or NONE]
TEXT OVERLAY: [on-screen text or NONE]

PRODUCT FOCUS:
[Specific product + how it is shown in this clip]
[e.g. "Adidas Samba OG — full shoe visible as YUNA steps forward, shoe fills lower third"]

REQUIRED IMAGES:
[List ONLY the images needed to generate this clip. No extras.]
- [SHOT-ID].png         ← ONLY-FRAME (STATIC or MOTION-FREE — no last frame needed)
- [SHOT-ID]-first.png   ← FIRST-FRAME (MOTION-GUIDED — start pose)
- [SHOT-ID]-last.png    ← LAST-FRAME (MOTION-GUIDED — end pose, must connect to next clip)

CLIP TYPE: STATIC / MOTION-FREE / MOTION-GUIDED
CONTINUITY NOTE: [Does end of this clip need to match start of next clip?]
[If YES: describe the exact pose the last frame must hold to connect smoothly]
```

RULES for video_script.md:
- Every REQUIRED IMAGES entry must be justified by the clip's action
- MOTION-GUIDED clips always list BOTH first and last frame — never just one
- MOTION-FREE clips list ONLY the first frame — AI handles the rest
- Continuity notes drive whether LAST-FRAME images are needed
- Never list "extra" or "backup" images — only what production requires

CLIP DURATION & IMAGE LIMITS — enforced at script writing stage:
  All clips: 5–15 seconds. No clip shorter than 5s, no clip longer than 15s.
  5–10 second clip:  max 2 images
  11–15 second clip: max 2 images
  If more than 2 images are needed → break the scene into multiple 5-second clips
  A 20-second idea = two 10-second clips, not one clip with 4 images

TRANSITION TYPE — required for every clip:
  CLIP TYPE: HARD_CUT / BLACK_FADE / CONTINUOUS_FROM_PREV / CONTINUOUS_TO_NEXT
  CONTINUOUS means: this clip shares the same scene with adjacent clip,
  character pose at boundary must be designed to flow between them.

RECURRING CHARACTER SCAN — mandatory at end of video_script.md:

After writing all clips, scan every ACTION field and list every person who appears.
Count how many clips each person appears in.

```
## RECURRING CHARACTERS IN THIS VIDEO
| Character | Appears in | Reference needed? |
|-----------|-----------|-----------------|
| [Golfer]  | CLIP 2, 4, 6, 8 | YES — 4 clips |
| [Bride]   | CLIP 5, 7, 9 | YES — 3 clips |
| [Caddie]  | CLIP 3 only | NO — 1 clip only |
```

Rule: appears in 2+ clips → reference required.
Rule: appears in 1 clip only → no reference needed, describe in prompt only.

If any recurring characters are found AND this is a Mode A campaign:
  → Trigger Stage 2 (lightweight path) before Stage 4C.
  → Do not skip this. The golfer in clip 2 must look exactly like the golfer in clip 8.

CHECKPOINT 4B:
Show video_script.md including the RECURRING CHARACTERS table. Ask:
"Does each clip tell the right story? Are the required images correct?
Any clips to change or add?"

→ If recurring characters found → tell user:
  "I detected [N] recurring characters who appear in multiple clips.
  I will create character references for them before the image brief.
  Starting Stage 2 for: [list names/roles]"
  → Immediately begin Stage 2 (lightweight) for those characters.
  → After Stage 2 approved: begin Stage 4C.

→ If no recurring characters → begin Stage 4C immediately.

---

# STAGE 4C — IMAGE PRODUCTION BRIEF

This is the critical bridge between the video script and image generation.
image_brief.md is a flat list of EVERY image that will be generated,
with the exact specification of what each image must show and why.

During Stage 6, Claude reads image_brief.md — not the shot list, not the video script.
Every image is generated to match its brief entry exactly.

```
Write image_brief.md from video_script.md.
Compile every REQUIRED IMAGES entry into one document.

For each image file:

IMAGE: [SHOT-ID].png (or -first.png / -last.png)
Serves: CLIP [N] — [clip name]
Frame role: ONLY-FRAME / FIRST-FRAME / LAST-FRAME
Clip type: STATIC / MOTION-FREE / MOTION-GUIDED

CHARACTERS IN FRAME:
PRIMARY — [NAME]: [exact body position, limb positions, weight, direction, expression]
BACKGROUND — [NAME]: [blurred, 1-2m behind, what they are doing]

EXACT POSE REQUIRED:
[One precise sentence. Body position, which limbs doing what, eye direction,
where in frame. Specific enough to evaluate pass/fail.]

PRODUCT VISIBILITY:
[Exact product name + exactly how it appears in frame]
[e.g. "White Adidas Samba OG in lower-left third, full shoe visible at 30° angle,
laces and sole detail clear"]

WHAT KLING DOES WITH THIS IMAGE:
ONLY-FRAME:  "Single source — Higgsfield animates [camera movement] from this frame"
FIRST-FRAME: "Start pose — Higgsfield moves character from this position to last frame"
LAST-FRAME:  "End pose — must match [energy/direction of first frame]"

CONNECTS TO:
[LAST-FRAME only: what the next clip's FIRST-FRAME will show — pose that carries over]
[Otherwise: NONE]

PASS CRITERIA:
[Specific list of what must be true for this image to pass]
[e.g. PASS if: face visible and clear, shoe fills lower third, 2 background figures
visible blurred, track pants stripe on both legs. REJECT if: face blurred or cut off,
shoe not visible, isolated portrait]
```

RULES for image_brief.md:
- Every REQUIRED IMAGES entry from video_script.md must have an entry here
- No image is generated without an entry in this brief
- EXACT POSE must be specific enough to evaluate pass/fail
- WHAT KLING DOES links the image back to its video purpose
- Connection frames must describe what they connect to

CHECKPOINT 4C:
Print image_brief.md as a summary table:
| Image file | Clip | Frame role | Clip type | What Higgsfield does | Pass criteria (short) |
Ask: "Does every image have a clear purpose and exact spec?
Any images missing, wrong, or with unclear poses?"
→ If YES or approved: immediately begin STAGE 5 — environment lock and shot list.
→ If changes: update image_brief.md, then begin STAGE 5.

---

# STAGE 5 — ENVIRONMENT LOCK & SHOT LIST

Read image_brief.md in full first.
Every shot maps to an IMAGE entry in image_brief.md — not the other way around.
Do not create shots for images not in the brief.

## 5-0: Stage 2.5 에서 A 로 판정했으면

이미 `03_locks (락)/space/` 에 락이 있습니다. **새로 쓰지 말고 그 문단을 그대로 복사**해서
`scene_script.md` 의 ENVIRONMENT 에 넣습니다. 여기서 다시 쓰면 문장이 미묘하게 달라져
컷마다 공간이 흔들립니다.

B 로 판정했으면 아래 5-A 를 Act 마다 수행합니다.

## 5-A: Lock environment and camera per act

```
For each act, write and LOCK:

ENVIRONMENT [ACT N] — LOCKED (copy-paste verbatim into every image prompt for this act):
"[Dense paragraph: location, surfaces, background elements, light sources,
time of day, atmosphere, color temperature, what is in mid and deep background]"

CAMERA STYLE [ACT N] — LOCKED (copy-paste verbatim into every image prompt for this act):
"[Lens character, camera height, angle tendency, movement quality, depth of field]"

Save to scene_script.md.
```

## 5-B: Shot list

```
For each shot in scene_script.md:
- Shot ID: A1-01, A1-02 etc — must match a REQUIRED IMAGES entry in video_script.md
- Maps to: CLIP [N] in video_script.md
- Frame role: ONLY-FRAME / FIRST-FRAME / LAST-FRAME
- Shot type: WIDE / MEDIUM / CLOSE-UP / EXTREME CLOSE-UP
- Angle: EYE LEVEL / LOW ANGLE / HIGH ANGLE / DUTCH TILT / OVERHEAD
- Movement: STATIC / HANDHELD DRIFT / PUSH IN / PULL OUT / ORBIT
- Primary subject: character + exact action/pose
- Background: other characters blurred 1-2m behind — describe what they are doing
- Duration: seconds
- Cut logic: from CONTINUITY NOTE in video_script.md
- Clip type: STATIC / MOTION-FREE / MOTION-GUIDED
- Product: which product and exactly how it is shown
- Boundary pose (LAST-FRAME only): exact pose that must match next clip's FIRST-FRAME
```

SHOT LIST RULES:
1. One-to-one — every shot maps to a REQUIRED IMAGES entry. Nothing extra.
2. Background always present — no isolated portraits
3. Vary angles — never same angle two consecutive shots
4. Group scenes: WIDE establishing → MEDIUM per character → WIDE close-out
5. Products must be visible — specify exactly how in each shot
6. Duration: fast ad = 3-6s per shot / emotional = 5-10s

CLIP DURATION & IMAGE LIMITS — strictly enforced:
  All clips: 5s minimum, 15s maximum. No clip under 5s or over 15s.
  5–15 second clip: MAX 2 images
  If more than 2 images needed → split into multiple 5-second clips instead.
  Do not exceed 15 seconds. Do not go under 5 seconds.

DO NOT OVER-FRAGMENT CLIPS:
  Each clip should be a complete visual idea — one camera movement, one emotional beat.
  If you find yourself planning 3+ images for a single clip → stop → split the clip.
  Better to have more clips than more images per clip.
  Fragmented images = choppy video. Fewer, better-composed images = smoother video.

## SHOT LIST EXAMPLE — K-POP GROUP ROTATING CAMERA COVERAGE

Use this pattern when: multiple characters are in the same space together, and the
camera rotates coverage to each member individually while others stay in background.
This is the K-pop music video style — one shared scene, one rotating camera.

The key principle: every shot takes place in the SAME environment at the SAME moment.
The camera is the only thing that moves between members. This is what makes it feel
like one continuous scene rather than separate clips.

```
EXAMPLE: Adidas dance studio commercial — 4 members, one room, rotating coverage

LOCKED ENVIRONMENT (copy-paste into ALL shots below):
"Large professional dance studio, polished hardwood floor reflecting cool light,
full-length mirror wall spanning the entire left side of frame, industrial metal
ceiling with warm-tinted overhead strip lights, one wide window on the far right
casting diagonal afternoon light across the floor, slight atmospheric haze,
muted grey walls, other members visible in soft focus throughout"

LOCKED CAMERA STYLE (copy-paste into ALL shots below):
"Handheld, shoulder height, slightly low angle, shallow depth of field,
50mm lens equivalent, cinema verité quality, moves organically between subjects"

---

A1-01 | WIDE | LOW ANGLE | STATIC
Primary: All 4 members in V-formation mid-choreography, facing mirror
Background: N/A — all members in frame
Cut logic: Camera pushes toward YUNA for next shot
Clip type: MOTION-FREE
Product: Full outfits visible on all members — establishing all 4 looks at once

A1-02 | MEDIUM | EYE LEVEL | ORBIT left-to-right past YUNA
Primary: YUNA — sharp arm extension toward mirror, Adidas jacket sleeve crisp
Background: SORA and LUMI blurred 1.5m behind, still dancing in sync
Cut logic: Jacket sleeve movement leads eye to SORA's track pants in next shot
Clip type: MOTION-FREE
Product: YUNA's Adidas jacket — sleeve, logo, silhouette

A1-03 | MEDIUM | LOW ANGLE 20° | PUSH IN toward SORA
Primary: SORA — explosive crouch-and-rise, track pants stripe lines sharp
Background: LUMI and REIA blurred behind, mid-movement
Cut logic: SORA's upward body movement launches into LUMI's spin
Clip type: MOTION-FREE
Product: SORA's Adidas track pants — stripe detail and fit during movement

A1-04 | CLOSE-UP | HIGH ANGLE | DUTCH TILT 10°
Primary: LUMI's feet and lower legs — Adidas sneakers on hardwood floor, mid-step
Background: Other members' legs/feet softly blurred
Cut logic: Cut upward to REIA's face at same energy beat
Clip type: STATIC (camera angle change only)
Product: LUMI's Adidas sneakers — sole, silhouette, color

A1-05 | MEDIUM | EYE LEVEL | TRACKING alongside REIA
Primary: REIA — mid-jump, oversized jacket catching air, pure energy
Background: YUNA and SORA blurred in background, continuing choreography
Cut logic: REIA's landing energy matches the wide group reset
Clip type: MOTION-FREE
Product: REIA's Adidas jacket — movement, fit, energy

A1-06 | WIDE | HIGH ANGLE overhead | PULL OUT
Primary: All 4 members — end pose, catching breath, facing mirror
Background: N/A — all members in frame
Cut logic: Final breath → act transition
Clip type: STATIC
Product: All outfits visible from above — full Adidas look coordination
```

Why this works:
- Every shot shares the EXACT same environment description → same room every time
- Background members are always present → never isolated portraits
- Each MEDIUM shot focuses on ONE member's specific Adidas product
- Camera angles rotate: LOW → EYE LEVEL → LOW → HIGH → EYE LEVEL → OVERHEAD
- The products are the heroes, the members are the vehicle

## 5-C: Scene continuity groups

```
GROUP-A: [shot IDs] — [same location/scene — must stay together in order]
GROUP-B: [shot IDs] — [same location/scene]
SOLO: [shot IDs] — standalone, can be reordered in editing

Save to scene_script.md.
```

CHECKPOINT 5:
Show complete scene_script.md with environment locks, shot list, and groups.
Ask: "Review each shot. Does the sequence tell the story?
Products shown clearly? Any shots to add, remove, or change?"
→ If YES or approved: immediately begin STAGE 6 — generate FIRST shot of Act 1 only.
→ If changes needed: update scene_script.md, then begin STAGE 6.

CRITICAL: This is the last checkpoint before any image is created.
After this approval, generate only A1-01 first. Show it. Get approval. Then continue.
DO NOT generate all images at once without showing first results.

---

# STAGE 6 — IMAGE GENERATION

GATE: Do not enter this stage unless video_script.md AND scene_script.md are saved
and Checkpoint 5 is approved.

Read video_script.md and scene_script.md and character_sheets.md in full before writing any prompt.
Also read products.md. For every shot whose PRODUCT FOCUS names a real product with a
saved image path, pass that image as an --input-image reference. Never generate a real
product from text description alone.
Generate ONLY the images listed in REQUIRED IMAGES in video_script.md.

## TOOL — 어느 경로로 뽑을지 먼저 정합니다

```
이미지·영상을 어디서 뽑나요?

  A) 빠나나 (bbanana)   — 이미지는 웹 Free 로 무료, 영상은 Seedance 유료
                          수업 · 수강생 · 예산 없는 건은 전부 이쪽
  B) Higgsfield + Kling — Claude in Chrome 이 직접 조종. 계정과 확장이 있어야 함
```
`TOOL_MODE` 로 저장하고 해당 절만 따릅니다.
**두 경로의 프롬프트 본문은 같습니다** — 다른 건 어디에 붙여 넣느냐뿐입니다.

---

### TOOL_MODE = A · 빠나나  (기본값)

**이미지 — 웹 Free 토글로만.** MCP 로 이미지를 뽑지 않습니다(유료로 나갑니다).
- 빠나나 웹 → 모델 Nano Banana 2 → **`FREE` 토글 ON**
- ⚠️ **모델을 바꾸면 토글이 리셋됩니다.** 누르기 전에 화면에 `GENERATE | FREE` 가 떠 있는지
  눈으로 확인합니다. 부모 패널의 모델도 같이 봅니다
- 결과는 `05_images (이미지)/NN-slug/` 에 저장하고 같은 폴더에 `prompt.txt` 를 씁니다

**영상 — MCP 로, 유료.** 누르기 전에 `check_credits` 로 잔액을 보고,
**개수 × 모델 × 금액을 사용자에게 말하고 승인을 받습니다.** 승인 없이 누르지 않습니다.
- 구조가 변하는 타임랩스는 **한 컷으로** 뽑습니다. 여러 컷을 이어 붙이면 이음매에서 틀어집니다
- 락을 `image_urls`(시작)와 `end_image_url`(끝)에 물립니다. 끝을 안 박으면 마지막에 딴 장면이 됩니다
- 받은 클립은 **앞뒤를 잘라 씁니다.** 첫 프레임에서 구도가 한 번 흔들립니다:
  ```bash
  ffmpeg -t 1.5 -i in.mp4 -filter_complex "select='gt(scene,0.06)',metadata=print:file=-" -f null -
  ```

---

### TOOL_MODE = B · Higgsfield + Kling

⚠️ CRITICAL: Do NOT run nano-banana CLI commands. Do NOT use the nano-banana-pro skill.
All image generation happens inside Higgsfield's web browser interface.
Claude in Chrome controls Higgsfield directly.

Inside Higgsfield: select "Nano Banana Pro" from the model dropdown.
This is a model name in Higgsfield's UI — not a CLI tool or script.
Unlimited toggle: always ON before generating.

PREREQUISITE CHECK — before starting image generation:
```
Ask: "Is Claude in Chrome active and are you signed into higgsfield.ai?
  A) Yes — I'll control Higgsfield automatically
  B) No — I'll provide prompts for manual copy-paste"
Store as CHROME_MODE: AUTO or MANUAL
```

If B: generate no images here. Output every image prompt and every Stage 7 video prompt
to a single handoff file (prompts_handoff.md), then tell the user to render clips,
name them per shot ID, and drop them into clips/ before Stage 8. Do not proceed to
Stage 8 until clips exist.

If CHROME_MODE = AUTO — for each image in image_brief.md (in video order):

  Step 1 — Navigate:
  Navigate to higgsfield.ai → Image Generation tab → New Generation

  Step 2 — Set parameters (every time, no exceptions):
  ```
  Model:     select "Nano Banana Pro" from Higgsfield's model dropdown
  Unlimited: ON                ← enable toggle before generating
  Aspect:    [from image_brief.md]
  Quality:   Standard (drafts) / Max (hero or campaign shots)
  Count:     4 per prompt
  ```

  Step 3 — Upload reference images (Mode B / recurring characters):
  ```
  Upload 1: images/characters/[NAME]_act[N]_outfit.png   ← outfit anchor
  Upload 2: images/characters/[NAME]_ref_A.png            ← face ref
  Wait for both uploads before typing prompt.
  ```

  Step 4 — Enter prompt from image_brief.md EXACT POSE section. Generate.

  Step 5 — Evaluate against PASS CRITERIA. Download best result.
  Save to: images/act[N]_[name]/[SHOT-ID].png
  Move to next image without stopping.

If CHROME_MODE = MANUAL:
  Print each prompt. User selects Nano Banana Pro + enables unlimited,
  generates, saves. Says "done" → Claude continues.

IMAGE SETTINGS (from initial questions):
  If IMAGE_SETTINGS = AUTO:
    Hero/campaign shots → Max quality, aspect from brief
    Character close-ups → Standard, 4:5
    Wide environment   → Standard, 16:9
    Group shots        → Standard, 9:16

  If IMAGE_SETTINGS = MANUAL: before each batch, ask:
    "Next: [N] images for [scene]. Aspect ratio? Quality (Standard/Max)?"

Never delete existing images. Regenerate failures as [SHOT-ID]-v2.png.

## NEVER DELETE EXISTING IMAGES

Before generating anything:
```
List all existing files in images/act[N]/ folder.
Compare against REQUIRED IMAGES in video_script.md.
Only generate images that are MISSING.
Do not overwrite or delete any existing image file.

If regenerating a specific frame (user requested a redo):
  Save with a version suffix: [SHOT-ID]-v2.png
  Keep the original: [SHOT-ID].png
  Ask user: "Which version would you like to use?"
  Only delete the old one after explicit user confirmation.
```

## Every image prompt must include ALL of:

```
[SHOT TYPE] — [ANGLE] — [FRAME ROLE: ONLY-FRAME / FIRST-FRAME / LAST-FRAME]

[CHARACTER LOCKED PHYSICAL DESCRIPTION verbatim from character_sheets.md]
[LOCKED OUTFIT — ACT N verbatim from character_sheets.md]

[Primary action — specific pose, mid-movement if MOTION-FREE]
[For LAST-FRAME: exact boundary pose that matches next clip's FIRST-FRAME]
[Expression — specific, not generic]

Background: [other characters — what they are doing, blurred 1-2m behind]

[LOCKED ENVIRONMENT from scene_script.md — copy-paste verbatim]
[LOCKED CAMERA STYLE from scene_script.md — copy-paste verbatim]

[Product note: how product is featured/visible]

Cinematic, editorial quality, [aspect ratio], no text, no watermarks, no logos.
```

CRITICAL: "wearing [costume description]" is NOT acceptable.
Always paste the full LOCKED OUTFIT — ACT N block verbatim, exactly as written
in character_sheets.md. Never summarize, never paraphrase, never omit any item.

## CHARACTER REFERENCE IN HIGGSFIELD — MODE A vs MODE B

```
MODE A (location / environment campaign — no characters):
  No character or outfit reference images exist or are needed.
  --input-image: use product or location reference images from images/products/
  These anchor the visual style (color grade, product appearance, venue look).

  For each scene image:
    --input-image images/products/[scene]/[product-ref].jpg  ← product/venue style anchor
    (one image is sufficient for environment-led shots)

  Consistency is maintained through LOCKED ENVIRONMENT in scene_script.md,
  not through character references.

MODE B (character campaign — recurring cast):
  For SOLO character shots:
    --input-image [NAME]_act[N]_outfit.png   ← outfit reference FIRST (primary anchor)
    --input-image [NAME]_ref_A.png           ← face reference SECOND
    --input-image [NAME]_ref_B.png           ← additional face reference THIRD

  For GROUP shots:
    --input-image [LEAD]_act[N]_outfit.png
    --input-image [CHAR2]_act[N]_outfit.png
    --input-image [CHAR3]_act[N]_outfit.png
    --input-image [CHAR4]_act[N]_outfit.png  ← up to 4 inputs

  Why outfit first: Higgsfield uses first --input-image as primary style anchor.
  NEVER use character_reference.png alone — always use act-specific outfit reference.
```

## OUTFIT CONSISTENCY CHECK (Mode B only — skip in Mode A)

```
Before writing the image prompt for any Mode B shot, verify:
1. What act is this shot in? → Act [N]
2. Who is the primary character? → [NAME]
3. What is their LOCKED OUTFIT — ACT [N]? → copy verbatim from character_sheets.md
4. Is images/characters/[NAME]_act[N]_outfit.png saved and approved? → yes/no
If the outfit reference is missing → STOP. Generate it first. Then continue.
```

## CHARACTER REFERENCE — HOW IT ACTUALLY WORKS

The character reference image is used during IMAGE GENERATION (Higgsfield stage),
NOT during video generation in Higgsfield.

Why: Higgsfield MOTION-GUIDED only accepts 2 images — first frame and last frame.
There is no slot for a third character reference image.

The solution: bake the character's face into the generated images themselves.
When Higgsfield generates first/last frame images using --input-image with the
character reference, the correct face is embedded in those images.
Higgsfield then receives frames that already have the right character — no separate upload needed.

```
IMAGE GENERATION (Higgsfield) — character reference used here:
  MOTION-FREE:   --input-image [character_reference.png]
                 → generates 1 frame with correct face baked in
                 → Higgsfield upload: scene image + character reference (2 slots available)

  MOTION-GUIDED: --input-image [character_reference.png]
                 → generates first frame with correct face baked in
                 → same --input-image for last frame generation
                 → Higgsfield upload: first frame + last frame only (no room for reference)
                 → face is already correct inside both frames

VIDEO GENERATION (Higgsfield):
  MOTION-FREE:   Upload 1) scene image  2) character reference  ← 2 slots, both used
  MOTION-GUIDED: Upload 1) first frame  2) last frame           ← 2 slots, both used
                 Character reference is NOT uploaded separately — it's inside the frames
```

FACE VISIBILITY REQUIREMENT for MOTION-GUIDED images:
Because the character reference cannot be uploaded to Higgsfield separately,
the generated first and last frame images must have:
- Face clearly visible and large enough to identify
- Not blurred, not turned away, not too small in frame
- At minimum: face occupies 15-20% of frame height for medium shots
- For wide group shots: generate a SEPARATE close-up reference frame of just the
  character's face to include alongside the first/last frames in Higgsfield
  (use this as a style reference, not as a third video input — paste it in the prompt notes)

If a shot is CLOSE-UP or EXTREME CLOSE-UP:
  → Face will be large enough naturally — no extra steps needed
  → Use Higgsfield for these shots (better face consistency than Higgsfield)

If a shot is WIDE and face is small:
  → Either switch to Higgsfield (handles wide shots with face tracking better)
  → Or note in production file: "face may drift — check output before saving"

## MOTION-GUIDED — First and Last Frame rules

```
When a shot is MOTION-GUIDED in video_script.md:

Generate FIRST-FRAME image:
  - Shows start pose of the movement
  - Character in position they begin the motion from
  - Save as [SHOT-ID]-first.png

Then generate LAST-FRAME image:
  - Shows end pose of the movement
  - Character in position they end the motion at
  - Save as [SHOT-ID]-last.png

BOUNDARY CONTINUITY — when two clips must connect smoothly:
  If CLIP [N] ends with character in pose X,
  and CLIP [N+1] begins with character in pose Y,
  and the video_script.md says these clips must be continuous:
    → CLIP [N] LAST-FRAME and CLIP [N+1] FIRST-FRAME must show matching poses.
    → Generate them together and verify they connect before proceeding.
    → Show both side by side and ask: "Do these connect without a jump?"

LAST-FRAME prompt must include:
  "End pose: [exact description from video_script.md CONTINUITY NOTE]
  This frame must match the start of [CLIP N+1] — same position, same body angle."

Safety check before generating last frame:
  "Does [start pose description] → [end pose description] connect naturally
  without any awkward middle state?"
  If any doubt → downgrade to MOTION-FREE, delete last frame plan.
```

## Generation order — SEQUENTIAL, TREAT AS ONE CONTINUOUS FILM

```
CRITICAL PRINCIPLE: These images are not independent. They are frames of a single
continuous film. Every image must be generated with awareness of what comes before
and after it. Never generate an image in isolation.

BEFORE generating any image:
1. Read image_brief.md completely — understand the full sequence
2. Print the full clip sequence as a timeline:
   CLIP 1 (5s) → CLIP 2 (7s) → CLIP 3 (5s) → CLIP 4 (8s) → ...
   Show which clips are continuous (same scene), which are transitions.
3. List existing files in images/ — generate only MISSING ones.

TRANSITION PLANNING — before generating any image:
For every clip boundary, identify the transition type:
  HARD_CUT:    no pose matching needed — images are independent
  BLACK_FADE:  no pose matching needed — black frame between
  CONTINUOUS:  clips share same scene — character pose at end of clip N
               must flow naturally into start of clip N+1
               → CLIP N last image and CLIP N+1 first image must be designed together

For CONTINUOUS transitions:
  Generate CLIP N last image and CLIP N+1 first image in the SAME generation session.
  Show them side by side immediately. Confirm connection before saving either.

GENERATION SEQUENCE — strictly in video order:
  Generate images clip by clip, in the order they appear in the video.
  Never jump around. Complete CLIP 1's images before starting CLIP 2.

  For each clip:

  Step A: Read image_brief.md entry. Note EXACT POSE, PRODUCT, PASS CRITERIA.
          Note transition type to next clip — HARD_CUT / BLACK_FADE / CONTINUOUS.

  Step B: Build prompt including ALL of:
    [FRAME ROLE: ONLY-FRAME / FIRST-FRAME / LAST-FRAME]
    [CHARACTER LOCKED PHYSICAL DESCRIPTION verbatim from character_sheets.md]
    [LOCKED OUTFIT — ACT N verbatim from character_sheets.md]
    [EXACT POSE from image_brief.md]
    [PRODUCT VISIBILITY from image_brief.md]
    Background: [BACKGROUND from image_brief.md]
    [LOCKED ENVIRONMENT verbatim from scene_script.md]
    [LOCKED CAMERA STYLE verbatim from scene_script.md]
    Cinematic, editorial quality, [aspect ratio], no text, no watermarks, no logos.

    For LAST-FRAME of CONTINUOUS clip, add:
    "End pose must lead naturally into: [description of next clip's first frame]"

  Step C: --input-image stack:
    Slot 1: [NAME]_act[N]_outfit.png  ← primary anchor (outfit locks the look)
    Slot 2: [NAME]_ref_A.png          ← face reference
    Slot 3: [NAME]_ref_B.png          ← second face reference for consistency
    For group shots: all character outfit references for this act.

  Step D: Show and evaluate — behavior depends on REVIEW_MODE setting:

    If REVIEW_MODE = PER_IMAGE:
      Show the generated image immediately.
      Print pass/fail against PASS CRITERIA from image_brief.md.
      If ALL pass → ask user: "✓ [SHOT-ID] looks good? YES to continue / describe what to fix."
      Wait for explicit YES before generating next image.
      If user says fix → regenerate → show again → wait for YES.

    If REVIEW_MODE = BATCH:
      Save image silently. Print one line: "✓ [SHOT-ID] saved."
      Check PASS CRITERIA internally — if ANY criterion clearly fails:
        Save as [SHOT-ID]-draft.png with a note: "⚠ flagged for review — [reason]"
      Continue generating remaining images for this Act without stopping.

WITHIN A CLIP — duration and image count enforcement:
  All clips must be 5–15 seconds. Generate max 2 images per clip.
  If a clip needs 3+ images → stop and split it into multiple 5-second clips first.
  Update video_script.md and image_brief.md before generating any images for that scene.
```

## Clip types:

STATIC: camera moves, subject still. 1 image (ONLY-FRAME).

MOTION-FREE (DEFAULT for human movement):
- 1 image (FIRST-FRAME only). AI generates motion freely from it.
- Use for: walking, dancing, sports, natural gestures, expressions.
- The video prompt describes the motion in words.

MOTION-GUIDED:
- 2 images (FIRST-FRAME + LAST-FRAME).
- Only when: start AND end positions are clearly defined, AND they connect naturally.
- If any doubt → MOTION-FREE.

CHECKPOINT 6 (per act):

If REVIEW_MODE = PER_IMAGE:
  Each image was already reviewed during generation.
  Show any CONTINUOUS clip pairs side by side for a final connection check.
  Ask: "Act [N] done. Do any adjacent clips look like they won't connect smoothly?
  Any changes before video prompts?"

If REVIEW_MODE = BATCH:
  Show ALL images for this Act together in sequence.
  Then show CONTINUOUS clip pairs side by side — images where one scene flows into the next.
  List any flagged ⚠ draft images.
  Ask: "Review Act [N] — [N] images total.
  Flagged: [list]. CONTINUOUS pairs shown above — do they connect?
  Tell me which images to redo, or say 'all good'."
  Regenerate requested images → show again → confirm.
  Then move to Act [N+1].

→ If approved: begin STAGE 7 automatically.

---

# STAGE 7 — VIDEO PROMPT PACKAGE

Read video_script.md and full_screenplay.md (Mode C) for each clip.
Create one file per clip: production/[SHOT-ID].md

Each file must be completely self-contained — open it, follow the instructions, done.
No need to cross-reference other files.

The file format is designed for direct copy-paste use in Higgsfield.
Claude opens Higgsfield automatically before Stage 7 begins.

---

## PRODUCTION FILE FORMAT — production/[SHOT-ID].md

```
╔══════════════════════════════════════════════════════════════╗
║  CLIP [N] — [SHOT-ID] — [Short name]
║  [Duration]s | [STATIC / MOTION-FREE / MOTION-GUIDED] | Tool: Higgsfield
╚══════════════════════════════════════════════════════════════╝

━━━ STEP 1: UPLOAD THESE IMAGES ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[If MOTION-FREE or STATIC]
  Upload slot 1 → images/act[N]_[name]/[SHOT-ID].png          ← SCENE IMAGE (primary)
  Upload slot 2 → images/characters/[NAME]_ref_A.png           ← CHARACTER FACE REFERENCE

[If MOTION-GUIDED]
  Upload slot 1 → images/act[N]_[name]/[SHOT-ID]-first.png     ← FIRST FRAME (start pose)
  Upload slot 2 → images/act[N]_[name]/[SHOT-ID]-last.png      ← LAST FRAME (end pose)
  Note: character face is already baked into both images — no separate reference needed

━━━ STEP 2: PASTE THIS PROMPT (copy everything below the line) ━━━

[PASTE START ▼]
[Full video generation prompt — everything Higgsfield/Higgsfield needs in one block:
- Camera movement: e.g. "Slow push in from medium to close-up"
- Character motion: e.g. "YUNA raises her arm slowly, jacket sleeve catches light"
- Character description verbatim from character_sheets.md
- Atmosphere: lighting, particles, depth of field, color
- Product visibility: how the product stays in frame
- If MOTION-GUIDED: "Animate smoothly from first frame pose to last frame pose"]
[PASTE END ▲]

━━━ DIALOGUE / VOICEOVER ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[If this clip has spoken dialogue or VO from video_script.md:]
  Character speaking: [NAME]
  Line: "[exact dialogue line]"
  Delivery: [tone — e.g. "warm and quiet", "urgent whisper", "confident declaration"]
  Note: Higgsfield/Higgsfield do not generate dialogue audio — this line goes to ElevenLabs
        in Stage 9. Include it here as reference for the actor's expression/lip movement.
        In the video prompt above, add: "[NAME]'s lips move as if speaking quietly"
        or "[NAME] opens mouth to speak, slight movement" depending on shot type.

[If this clip has voiceover only (not on-screen character speaking):]
  VO text: "[exact voiceover line from video_script.md]"
  This VO is generated separately by ElevenLabs and mixed in Stage 9.

[If no dialogue or VO:]
  No dialogue. No voiceover. Visual only.

━━━ SETTINGS ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Duration: [X] seconds
  Aspect:   [9:16 / 16:9 / 1:1 / 4:5]
  Quality:  Standard (adjust in tool settings)

━━━ AFTER GENERATING ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Download → rename to [SHOT-ID].mp4 → save to video-clips/

━━━ CONTINUITY NOTE ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Connects to: [next SHOT-ID] → [CONTINUOUS / HARD_CUT / BLACK_FADE]
  [If CONTINUOUS: describe the boundary — what pose/position this clip must end on]
```

---

## MASTER CHECKLIST — production/MASTER-CHECKLIST.md

After all production files are created, generate a checklist:

```
# Production Checklist — [Campaign Name]

| Clip | Shot ID | Type | Tool | Images Ready | Dialogue | Generated | Saved |
|------|---------|------|------|-------------|---------|-----------|-------|
| 1    | A1-01   | MOTION-FREE | Higgsfield | ✓ | None | ☐ | ☐ |
| 2    | A1-02   | MOTION-GUIDED | Higgsfield | ✓ | "[line]" | ☐ | ☐ |
...

Total clips: [N]
Clips with dialogue: [N] — audio generated separately by ElevenLabs in Stage 9
```

## HIGGSFIELD CHARACTER CONSISTENCY

```
Higgsfield is used for all image AND video generation.

For character reference in image generation:
  Upload character reference image(s) in Higgsfield's reference/style input.
  Higgsfield uses the reference to maintain face consistency across images.

For video generation:
  MOTION-FREE: upload scene image + character reference (2 inputs)
  MOTION-GUIDED: upload first frame + last frame (2 inputs)
               Character face is already baked into both frames from image generation step.

For face-critical shots (close-up, zoom):
  Generate the image with face large and clearly visible in frame.
  Use Higgsfield's face mode or portrait mode for video generation.
  If face is small in a wide shot → generate a separate close-up reference frame first.
```

## Higgsfield — Shot Type Guide

All shots use Higgsfield for both image and video generation.
Different shot types use different Higgsfield modes:

Face / character close-up   → Higgsfield Image Gen → Higgsfield Video (img2vid, face mode)
Group / multi-character     → Higgsfield Image Gen → Higgsfield Video (img2vid)
Sports / athletic movement  → Higgsfield Image Gen → Higgsfield Video (motion mode)
Fashion / walk              → Higgsfield Image Gen → Higgsfield Video (motion mode)
Product close-up / detail   → Higgsfield Image Gen → Higgsfield Video (camera mode)
Drone / wide environment    → Higgsfield Image Gen → Higgsfield Video (camera mode)
MOTION-GUIDED (first+last)  → Higgsfield Image Gen → Higgsfield Video (start+end frame)

## VIDEO GENERATION — HIGGSFIELD (KLING MODEL) VIA CLAUDE IN CHROME

After all images for an Act are approved, Claude immediately triggers Higgsfield video
generation using Kling as the selected model — no separate instruction needed.

Image approval → Stage 7 production files ready → Higgsfield opens → Kling selected → videos generated

PREREQUISITE CHECK — at start of Stage 7:
```
Check: "Is Claude in Chrome active and are you signed into higgsfield.ai?
  A) Yes — I'll control Higgsfield automatically and select Kling as the model
  B) No — I'll provide production files for manual generation"

Store as CHROME_MODE: AUTO or MANUAL
```

If CHROME_MODE = AUTO:

For each clip in MASTER-CHECKLIST.md order (video order):

  Step 1 — Open Higgsfield:
  ```bash
  # Mac
  open "https://higgsfield.ai"
  # Windows
  start "https://higgsfield.ai"
  ```
  Navigate to Video Generation → Image to Video

  Step 2 — Upload reference images:
  ```
  Read production/[SHOT-ID].md → STEP 1 for exact image paths.

  MOTION-FREE or STATIC:
    Upload 1: images/act[N]_[name]/[SHOT-ID].png          ← scene image
    Upload 2: images/characters/[NAME]_ref_A.png           ← character reference

  MOTION-GUIDED:
    Upload 1: images/act[N]_[name]/[SHOT-ID]-first.png    ← first frame (start pose)
    Upload 2: images/act[N]_[name]/[SHOT-ID]-last.png     ← last frame (end pose)
    Note: character face already baked into both frames
  ```

  Step 3 — Set parameters:
  ```
  Unlimited: toggle ON (always, before selecting anything else)
  Duration:  from production/[SHOT-ID].md
  Mode:      Standard or Pro — see guide below

  KLING VERSION — select automatically based on clip type:

  Kling 2.1 (or latest available):
    → Hero shots, campaign shots, emotional close-ups
    → Any shot where face detail and motion quality matter most
    → MOTION-GUIDED clips needing precise start-to-end control

  Kling 2.0:
    → Standard character shots, fashion, athletic movement
    → Group scenes with multiple people
    → General MOTION-FREE clips

  Kling 1.6:
    → Wide environment shots, drone-style, landscape
    → STATIC clips with only camera movement
    → Background/B-roll clips with no characters

  Kling 1.5:
    → Fallback if newer versions are unavailable
    → Quick test generations before committing to Pro mode

  If VIDEO_SETTINGS = MANUAL — before each clip ask:
    "Next: [SHOT-ID] — [description] — [clip type]
     Kling version? (1.5 / 1.6 / 2.0 / 2.1 / latest)
     Mode? (Standard / Pro)
     Duration? (from brief: Xs)"

  MODE guide:
    Standard → most clips, MOTION-FREE, environment shots
    Pro      → hero shots, face close-ups, MOTION-GUIDED, campaign shots
  ```

  Step 4 — Enter video prompt:
  ```
  Copy everything between [PASTE START ▼] and [PASTE END ▲] from production/[SHOT-ID].md
  Paste into Kling's prompt field.

  If dialogue: add to end of prompt → "[CHARACTER] lips move as if speaking [line]"
  ```

  Step 5 — Generate → download → save:
  ```
  Click Generate. Wait for completion.
  Download → rename to [SHOT-ID].mp4 → save to video-clips/
  Update MASTER-CHECKLIST.md: ✓ Generated ✓ Saved
  ```

  Step 6 — Auto-continue:
  ```
  Move to next clip without user input.
  Complete all clips → automatically begin Stage 8.
  ```

If CHROME_MODE = MANUAL (fallback):
  Open production/[SHOT-ID].md — everything you need is in that file.
  STEP 1: upload images in listed order
  STEP 2: copy-paste prompt
  Open production/[SHOT-ID].md, go to higgsfield.ai → Video → select Kling model.
After all clips: tell Claude "All clips saved. Files: [list]"
  Claude begins Stage 8 automatically.

---

# STAGE 8 — EDITORIAL ANALYSIS & EDL

After user confirms all clips are saved.

## Ask user three questions:

```
Q1. TRANSITIONS (default: BLACK FADE 0.5s):
   A) Black fade 0.5s — clean, cinematic (default)
   B) Hard cut — energy, impact
   C) Crossfade — smooth, emotional
   D) Mix — I decide per cut based on pacing

Q2. AUDIO:
   A) Strip all original audio
   B) Keep original
   C) Add SFX via ElevenLabs

Q3. EXPORT FORMATS (select all that apply):
   A) 9:16 — Reels / TikTok / Shorts
   B) 16:9 — YouTube
   C) 1:1  — Feed
   D) 4:5  — Feed optimized
```

## Clip inventory:

```
Analyze all clips in video-clips/:
- Actual duration
- Content: subject, action, energy level (LOW / MEDIUM / HIGH)
- Usable range: does whole clip work or just a portion
- Quality issues
```

## Editorial decisions:

```
Rules:
1. CONTINUITY GROUPS: never split or reorder. Treat as one locked unit.
2. Hook: first 3 seconds must stop the scroll
3. Emotional arc: build to the key message
4. Pacing: alternate energy levels
5. Platform: Reels/TikTok 3-5s per cut / YouTube 5-8s
6. Duration: within plus or minus 2 seconds of target
```

## Speed decisions:

```
NORMAL — original speed
SLOW [x] — e.g. 0.5x for drama
FAST [x] — e.g. 1.5x for montage
RAMP-OUT [start>end] — e.g. 1.0x>0.3x for impact slowdown
RAMP-IN [start>end] — e.g. 0.3x>1.0x for slow build
RAMP-CUSTOM [segments] — define time segments with different speeds
RAMP-MANUAL — complex bezier curve, flag for DaVinci/Premiere

Use RAMP-OUT for athletic peak moments
Use FAST for establishing/B-roll that drags
Use RAMP-IN for product reveals
Use SLOW for emotional close-ups
```

## Text overlay plan:

```
For each clip:
- Content: marketing copy from scenario.md
- Position: BOTTOM-THIRD / CENTER / TOP-CENTER
- Style: HEADLINE (72px bold) / SUBTITLE (48px) / CTA (56px accent)
- Animation: FADE-IN-OUT 0.5s each side
- Timing: start second to end second in assembled video

Principles:
- Not every clip needs text — emotional peaks often need silence
- Two-line text: second line 0.5s after first
- CTA always last, with URL if applicable
```

## EDL format:

```
Save to assembly/edit_decision_list.md

[N]. [filename] | [GROUP/SOLO] | in:[X]s out:[Y]s | [TRANSITION] | speed:[SPEED] | audio:[STRIP/KEEP/SFX] | text:[TEXT-ID or NONE] | [reason]

Example:
1. A1-01.mp4 | SOLO    | in:0.0 out:5.0 | BLACK-FADE 0.5s | speed:NORMAL        | audio:STRIP | text:TEXT-01 | strong opening
2. A1-02.mp4 | GROUP-A | in:0.0 out:5.0 | BLACK-FADE 0.5s | speed:NORMAL        | audio:STRIP | text:NONE   | group enters
3. A1-03.mp4 | GROUP-A | in:0.5 out:5.0 | BLACK-FADE 0.5s | speed:RAMP-OUT 1.0x>0.3x | audio:SFX | text:TEXT-02 | impact slowdown
```

CHECKPOINT 8: Print full EDL + text plan. Ask: "Review the edit.
Any clip to move, speed to change, or text to adjust?
Type APPROVED to begin assembly."

---

# STAGE 9 — ASSEMBLY, AUDIO, TEXT, EXPORT

## 9-A: Rough cut first

```
Build rough cut using ffmpeg:
- Trim each clip to EDL in/out points
- Apply speed transformations (setpts for video, atempo for audio pitch)
- Apply transitions between clips
- Concatenate in EDL order
- Save to assembly/rough-cut.mp4

Tell user: "Rough cut ready at assembly/rough-cut.mp4
Open and check the sequence before I add text and audio."
```

## 9-B: Full assembly after rough cut approval

```
Step 1 — Speed ramps
  Split RAMP clips into segments
  Apply setpts per segment, concatenate
  Flag RAMP-MANUAL in assembly/manual_notes.md

Step 2 — Text overlays (ffmpeg drawtext)
  Apply text from text_overlay_plan.md at specified timecodes
  Burn into video
  Save to assembly/with-text.mp4

Step 3 — Remove original audio
  ffmpeg -i assembly/with-text.mp4 -an assembly/silent.mp4

Step 4 — Sound effects (if SFX selected)
  Generate via ElevenLabs Sound Effects API:
    Analyze each scene, identify impact moments, ambient sounds, transitions
    Describe each sound in plain English
    Generate .mp3, save to audio/sfx/
  Mix at timecodes using ffmpeg adelay + amix
  SFX impact: 70% | SFX ambient: 25-30%
  Save to assembly/with-sfx.mp4

Step 5 — Voiceover (auto-generate)
  Read scenario.md for VO lines
  Match timing to EDL order
  Auto-select ElevenLabs voice matching campaign tone:
    Energetic/Athletic: younger, clear, upbeat
    Luxury: warm, measured, confident
    Emotional: soft, intimate
    Documentary: neutral, authoritative
  Print selected voice name + reason, wait for approval
  Generate to audio/vo-full.mp3

Step 6 — Final audio mix
  VO: 100%
  SFX impact: 70% | SFX ambient: 25-30%
  Music: 20% under VO, 80% on non-VO sections
  Fade in 1s / fade out 2s
  Save to assembly/final-mix.mp4

Step 7 — Export only user-selected formats
  9:16: scale=1080:1920 pad > delivery/reel.mp4
  16:9: scale=1920:1080 pad > delivery/youtube.mp4
  1:1:  scale=1080:1080 pad > delivery/feed.mp4
  4:5:  scale=1080:1350 pad > delivery/feed-45.mp4
  Thumbnail: strongest frame from EDL > delivery/thumbnail.jpg
  Report: list each file with size and duration
```

---

# STAGE 10 — CAPTIONS & COPY

```
Write captions for [CAMPAIGN NAME].
Source: CLAUDE.md (brand voice) + scenario.md + EDL

INSTAGRAM REELS:
- Hook line 1: stops scroll (question, bold claim, or negation)
- Body: 100-150 words max, brand voice, emotional then informational
- CTA: one clear action
- Hashtags: 5-8, mix of broad + niche + brand
- Save: copy/instagram-a.md and copy/instagram-b.md (2 variants)

TIKTOK:
- Hook: casual, trend-aware
- Body: 60-100 words, conversational
- CTA: native-feeling
- Hashtags: 3-5
- Save: copy/tiktok-a.md + copy/tiktok-b.md

YOUTUBE:
- Title: keyword-front, 60 chars max
- Description: 150-200 words, CTAs throughout
- Tags: 10-15 keywords
- Save: copy/youtube.md

LINKEDIN (if selected):
- Professional framing, problem-solution
- 150-200 words
- Save: copy/linkedin.md

For each: 2 A/B variants with different hooks.
Save summary to copy/COPY-SUMMARY.md
```

---

# COMPLETE FILE STRUCTURE

```
[Campaign]/
├── CLAUDE.md
├── products.md
├── character_sheets.md
├── scenario.md
├── scene_script.md
├── moodboard.html
├── images/
│   ├── products/[product-name]/
│   ├── characters/
│   ├── act1_[name]/
│   ├── act2_[name]/
│   └── act3_[name]/
├── production/
│   ├── [SHOT-ID].md
│   └── MASTER-CHECKLIST.md
├── video-clips/
│   └── [SHOT-ID].mp4
├── audio/
│   ├── vo-full.mp3
│   ├── music.mp3
│   └── sfx/
├── assembly/
│   ├── edit_decision_list.md
│   ├── text_overlay_plan.md
│   ├── rough-cut.mp4
│   ├── with-text.mp4
│   ├── with-sfx.mp4
│   ├── final-mix.mp4
│   └── manual_notes.md
├── delivery/
│   ├── reel.mp4
│   ├── youtube.mp4
│   ├── feed.mp4
│   ├── feed-45.mp4
│   └── thumbnail.jpg
└── copy/
    ├── instagram-a.md
    ├── instagram-b.md
    ├── tiktok-a.md
    ├── tiktok-b.md
    ├── youtube.md
    ├── linkedin.md
    └── COPY-SUMMARY.md
```

---

# HARD RULES — NEVER BREAK

1. No images before Stage 5 is approved.
2. Every stage needs user approval before the next begins.
3. Character descriptions are VERBATIM always. Never summarize or paraphrase.
4. Environment and camera style are VERBATIM per act. Lock once, copy everywhere.
5. Images are video frames. Background characters must be present. No isolated portraits.
6. Real products = no AI hallucination. Reference images exist, use them.
7. MOTION-FREE is default. MOTION-GUIDED only when frames clearly connect.
8. Continuity groups are locked. Never reorder inside a group.
9. EDL first, rough cut, then full assembly. Never skip rough cut.
10. Only export formats user selected. Do not render unneeded formats.
11. Captions = 2 A/B variants per platform always.
12. Music is manual. User sources licensed track. Claude does not generate music.

---

# WHAT IS AUTOMATIC vs MANUAL

Automatic (Claude Code):
- Brand research and CLAUDE.md
- Product image download (if accessible)
- Character sheets (Claude writes, user approves)
- Character reference images (Higgsfield)
- Mood board HTML
- Scenario writing
- Shot list and environment lock
- Scene images (Higgsfield, user approves per act)
- Video prompt package
- EDL with sequence decisions
- Rough cut (ffmpeg)
- Full assembly with speed ramps (ffmpeg)
- Text overlays (ffmpeg drawtext)
- SFX generation (ElevenLabs Sound Effects API)
- Voiceover (ElevenLabs TTS, auto voice selection)
- Final audio mix (ffmpeg)
- Multi-format export (ffmpeg)
- Captions A/B per platform

Manual (user does):
- VIDEO GENERATION — Higgsfield / Higgsfield require browser
- Music — source licensed track from Artlist / Musicbed
- Color grade precision — ffmpeg applies basic LUT, DaVinci for precision
- Platform upload — Claude cannot access social media accounts

---

## 외주 건 — 견적과 계약

**`quote-and-contract` 스킬로 갑니다.** 이 스킬은 만드는 것만 다룹니다.

세는 단위(컷 · 길이 · 변형 · 자막 · 락) · 수정 vs 변경 · **생성 실비 분리** ·
**락 승인 게이트** · 묶음 견적이 전부 거기 있습니다.
