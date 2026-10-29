# Seedance 2.5 공식 전문 (ByteDance 공식 가이드 기준)

각 모드 공식 + 그대로 쓸 수 있는 템플릿. 대괄호는 채우고 지운다 — 출력물에 대괄호를 남기지 마라.

---

## § A. 기본 공식 — Omni Reference, 4~15초

> 완전한 프롬프트 = **[소재 설명] + [한 줄 요약] + [구체 플롯] + [전역 보충(엔딩)]**

| 블록 | 내용 |
|---|---|
| 소재 설명 | 소재 번호(업로드 순서) + 구체적 용도 — 이 소재가 뭔지: 인물 / 음색 / 동작 / 장면. 레퍼런스 없으면 생략 |
| 한 줄 요약 | 주체 + 장소 + 사건 + 테마·스타일 + 특수 카메라무빙 |
| 구체 플롯 | 타임라인 또는 스토리라인으로. 슬라이스마다 ➕ 화면 내용 + 카메라무빙 + 동작 + 대사 + 효과음 / ➖ 원치 않는 요소 |
| 전역 보충 | 영상 전체에 반드시 있어야 할 것을 다시 강조: 카메라 포지션 + 환경·씬 특징 + 전체 사운드/분위기 + 조명. 전역 금지도 여기서 반복 |

### 템플릿

```
[Style line]. [Lighting line].
@image1 provides [what], @image2 provides [what], @audio1 provides [what].

[One-sentence summary: subject + place + event + style + special camera move.]
[Subject description — use § B if human.]
[Environment description.]
[Base camera setup: angle, shot size, movement, what stays centered.]

0s-Xs: [action / physical beats]. [camera behavior]. [light/atmosphere event]. No subtitles, no BGM.
Xs-Ys: [action]. [camera behavior]. [sound]. No subtitles, no BGM.

[Global closing: camera position + environment + overall sound/atmosphere + lighting + depth of field.]
Negative: no subtitles, no on-screen text, no background music, no watermark, no extra characters.
```

### 공식 예시 (가이드 원문 요지)

```
Realistic nature documentary style, cinematic realistic lighting. In the morning mist, within a vast
wetland reed bed @image1, an elegant red-crowned crane is spreading its wings and dancing @image2.
The crane features snow-white feathers, a bright red crown, a slender upright posture. The scene is a
shallow autumn wetland, sparkling water, golden reeds, duckweed. Out-of-focus background of distant
morning mist and rising sun. The camera uses a low-angle medium shot with a slight handheld feel,
generally steady, keeping the crane centered at all times.

0s-3s: The crane stands quietly in shallow water. It slowly unfolds its broad black-and-white wings.
The airflow creates ripples on the water. Sunlight slants in from the horizon, piercing the mist to
create a Tyndall effect.
3s-8s: The crane leaps lightly on the water, feet alternately tapping the surface, splashing crystal
droplets. Its slender neck tilts backward, beak to the sky. Then it lands lightly, folds its wings,
head looking around, letting out a clear long call.

Low-angle, slight handheld feel, moving up and down to follow the jumping trajectory. Natural depth of
field, foreground reeds slightly blurred, crane in sharp focus, background mist softly blurred. Natural
environmental sound: flowing water, wing flaps, the crane's call. Peaceful, ethereal, highly aesthetic.
```

---

## § B. 실사 인물 공식 — 8차원 (AI티 제거용)

> Character = [나이/인종] + [피부톤/피부질감] + [이목구비] + [눈빛/영혼] + [헤어] + [의상/소재] + [체형/감정/기질] + [기타]

애니 캐릭터도 같은 공식을 쓴다.

| # | 차원 | 세부 공식 | 핵심 |
|---|---|---|---|
| 1 | 나이/인종 | [구체 나이] + [국적·인종] + [스타일 형용사] + [얼굴형 명사] | "22-year-old East Asian woman with a classical, gentle movie face" |
| 2 | 피부톤/질감 | [쿨/웜톤] + [피부톤 명사] + [질감 형용사] + **리얼리즘 강제 접미사** | 접미사 필수: `retaining true micro pores and skin texture` (주근깨·잡티 추가 가능) |
| 3 | 이목구비 | [눈 모양] + [눈썹뼈] + [콧대] + [입술] + [턱선/골격] — **최소 3~4개** | 인식성을 결정 |
| 4 | 눈빛 | [눈빛 형용사] + [눈이 전하는 정보/은유] + [드러나는 저층 감정] | 감정을 결정 |
| 5 | 헤어 | [정확한 색] + [상태/질감] + [헤어스타일 명사] + [환경 상호작용: 바람에 날림 등] | "그냥 검은 머리" 금지 |
| 6 | 의상 | [패턴/재단] + [색] + [의상 명사] + [원단/신구 상태] + [착용 방식/디테일] | 낡음·마모까지 써야 리얼 |
| 7 | 체형/기질 | [골격/어깨] + [구도·샷 요구] + [동작/시선] + [전체 분위기어] | 플롯에 구도·동작이 이미 있으면 가운데 둘은 생략 |
| 8 | 기타 | 필요 시 | — |

### 완성 예

```
A 22-year-old East Asian woman with a classical, gentle movie face. Cool-toned fair skin with a
delicate warm sheen, retaining true micro pores and skin texture. Slender peach-blossom eyes with
slightly moist sockets, gently stretched brows, a small straight nose bridge, full lips with a soft
smile at the corners, a soft jawline. Her gaze is deeply affectionate, as if a pool of spring water
sits at the bottom of her eyes — gentle and focused, revealing attachment and a hint of reluctance.
Black hair tied into a casual, elegant low bun fixed with a plain jade hairpin, a few fine strands
resting at her cheeks, swaying in the breeze. She wears a minimalist plain-white cross-collar
hanfu of soft silk with a light sheen, collar slightly loose, no embroidery. Slim build, slender
shoulders. Chest-up close composition, eye contact with the camera. Overall a gentle, graceful,
classical-romantic temperament.
```

### 다인물일 때

- 인물마다 **별도 이미지**를 업로드하고 `@image1 is A, @image2 is B`로 바인딩을 명시한다.
- 각자 8차원을 **따로** 쓴다. 특히 의상은 분리해서 써야 "옷까지 섞이는" 현상이 안 난다.
- 프롬프트에 관계·위치를 못 박는다: `A sits on the left, B on the right; A hands B a glass of water.`
- 주체 1~5명이 안정적. 6~10명은 뽑기 운.

---

## § C. 30초 장편 공식 — 3모듈 구조

20초를 넘기면 § A가 아니라 이걸 쓴다.

> **한 문장 톤 선언** → **모듈1 멀티모달 레퍼런스 레이어** → **모듈2 글로벌 세팅** → **모듈3 타임스탬프 스토리보드**

### 맨 앞 한 문장
전체 톤을 한 줄로. 예: `29-second one-shot take — a woman in hanfu says farewell by the river.`

### 모듈 1 — 멀티모달 레퍼런스 레이어 (소재 없으면 생략)

> `Based on the uploaded [소재 타입], strictly keep [X] consistent, strictly lock [Y].`

```
Based on the uploaded images: strictly maintain the consistency of the character's face and features
in @image1; maintain the composition / white-model spatial relationship in @image2; strictly lock the
character's position in frame.
```
본문 안에서도 @를 반복하면 정확도가 올라간다.

### 모듈 2 — 글로벌 세팅 (세계관 + 붕괴 방지)

> [기본 환경·질감] + [비주얼 스타일] + [렌즈 언어] + [캐릭터 조형] + [연기 코어] + [금지 사항]

1. **기본 환경·질감** — [시간] + [장소] + [분위기] + `emphasize ultimate real physical texture`
2. **비주얼 스타일** — [시네마틱/실사/2D 등] + [심도 통제] + [조명 방식]
3. **렌즈 언어** — [샷 사이즈/시점] + [상세 서술]
4. **캐릭터 조형** — § B를 쓰거나 @레퍼런스 + 그 이미지 서술.
   사물이면: [수량] + [색] + [형태/디자인] + [사물 명사] + [소재/마모 상태] + [상징적 특징]
5. **연기 코어** — 완성본에서 반드시 살아야 할 포인트
6. **금지 사항** — [사운드] + [자막] + [행동] + [무너지기 쉬운 부분]
   예: `no large body movements, no extra dialogue, no BGM, no subtitles`

### 모듈 3 — 타임스탬프 스토리보드

긴 영상을 시간 슬라이스로 쪼갠다. 슬라이스마다 4줄:

1. `[시작s-끝s]` + [코어 단계/테마]
2. [동작/표정 등 물리적 지시] — [씬] + [구도] + [인물 디테일 동작]
3. [감정 해설 또는 카메라 스케줄링] — 물리 지시의 깊은 의도를 AI에게 설명
4. (컷이 필요하면) `transitions.md`의 3줄 트랜지션 공식을 여기 삽입

```
[00-06s] Arrival
She steps onto the wet stone bridge, fingertips brushing the wooden railing, breath visible in the
cold. Medium shot, camera slowly dollies in from her back to her profile.
Emotionally this is restrained anticipation — the camera stays behind her so the audience shares her
hesitation rather than reading her face. No subtitles, no BGM.
```

---

## § D. 초장편 공식 — Long Video, 30~180초

기본 공식과 비슷하되 맨 앞에 **글로벌 파라미터**가 추가된다.

> 완전한 프롬프트 = **[글로벌 파라미터] + [소재 설명] + [한 줄 요약] + [구체 플롯] + [전역 보충]**

- **글로벌 파라미터**: UI에서 이미 고른 값이라도 프롬프트 맨 앞에서 다시 못 박는다.
  `Total duration 3 minutes. Aspect ratio 9:16. Cinematic realistic quality, retro healing tone.`
- 나머지 블록은 § A와 동일하되, 플롯을 **씬 단위**로 길게 쓴다.
- 3분짜리는 씬당 10~20초로 쪼개고 각 씬 안에 다시 타임스탬프를 넣는다.

---

## § E. 영상 연장 공식 — Extend Video

**전제:** 원본이 30초 이내여야 연장 가능. 1회 연장은 4~30초. 결과물이 30초 이내면 또 연장 가능 → 최대 누적 60초.
입력한 프롬프트는 **새로 늘어난 구간에만** 적용된다. 원본 구간은 그대로 보존된다.

### E-1. 자연스럽게 이어가기 (원테이크 연장)

필수 어휘를 반드시 포함: `extend / continue / continuation`

```
Continue and extend the video. [what happens next].
Require natural extension, smooth motion continuation, seamless action connection.
Forbid rigid hard cuts. Forbid objects appearing out of thin air.
```

### E-2. 컷/전환으로 연장

> 컷 설정 = **[트랜지션 타입 가이드] + [기본 제약 요구] + [컷 로직 요구]**

```
1. At the cut point, use a "[타입]" transition (forbid rigid hard cuts, forbid objects appearing out
   of thin air).
2. Maintain a coordinated sense of breathing and duration in the camera, leaving enough time for the
   switch. Shot A shows [내용], then naturally transitions to Shot B, where [내용].
3. The scene change must be natural. [필요하면: and the shot size changes from C to D.]
```

모델에게 고르게 해도 된다:
`Choose the most suitable one for this film's style from: natural shot switching / mask transition / ink transition / similar-object transition.`

타입 11종과 문장은 `transitions.md`.

---

## § F. 편집 공식 — Smart Edit / Edit with marks / Edit Video

셋 다 문법이 같다. 차이는 마킹 도구가 붙느냐뿐.

- **Smart Edit** — 텍스트만으로 편집
- **Edit with marks** — 업로드한 영상에 박스/브러시/화살표/앵커 마킹 + 텍스트
- **Edit Video** — 이미 생성된 영상에 같은 방식으로

### 텍스트만 (Smart Edit)

> **[구체 수정 대상/무엇] + [동작·변화 서술] + [적용 시간 구간]**

필수 어휘: `edit / add / delete / remove / replace / change to`

```
In the first 8 seconds of the video, replace the boy's jeans with dark black suit trousers.
Keep everything else unchanged — same composition, same camera movement, same style.
```

### 마킹 포함 (Edit with marks / Edit Video)

> **[마킹 도구 + 방향] + [구체 수정 대상] + [동작·변화 서술] + [적용 시간 구간]**

| 블록 | 쓰는 법 | 예 |
|---|---|---|
| 마킹 도구·방향 | 무슨 도구로 그렸는지 + AI가 **안쪽/바깥쪽** 중 어디를 볼지 명시 | `inside the red box`, `along the direction the red arrow points`, `at the anchor point`, `to the left of the red line` |
| 수정 대상 | 그 영역의 무엇 | `the boy's jeans`, `the dead tree in the background`, `the coffee cup in her hand` |
| 변화 서술 | 무엇으로 바꿀지 / 추가·제거 | `replace with dark black suit trousers`, `turn into a blooming cherry tree`, `erase and inpaint the background seamlessly` |
| 적용 구간 | 전체인지 특정 초인지 | `throughout the entire 15-second clip, keep it consistent`, `only between 5s and 8s`, `fade in gradually from 3s` |

```
Replace the sheep inside the red box with a brown horse. Keep the motion trajectory identical to the
original. Apply only between 7s and 15s of the video. Keep composition, camera movement and style
unchanged.
```

### BGM 분리
`Remove the background music, keep only the characters' speaking voices. Preserve the original on-screen subtitles and all visual elements unchanged.`

### 그린스크린
`Replace the green screen background with [새 배경 서술], with matching light direction and color
temperature so the subject integrates naturally. Keep the subject's motion unchanged.`
또는 배경 레퍼런스를 업로드하고 `naturally integrate the green-screen subject into @image1`.

### 공간·시점 변경
`Change the eye-level shot to a high-altitude overhead shot, with the camera slowly pushing downward.`
`Change the third-person view to a first-person view of the character moving through the forest.`

---

## § G. 화이트모델(Clay Renderer) 공식

Maya/Blender 플러그인으로 카메라 경로를 짠 화이트모델 영상을 업로드해서 렌더링한다. **거친(coarse) 화이트모델이 현재 결과가 더 좋다.**

### G-1. 거친 화이트모델 — 구·원기둥·박스 조합, 동적 골격만 제공

> **[레퍼런스 선언] + [대응관계 매핑] + [플롯 디테일] + [씬 처리] + [전체 마무리]**

1. **레퍼런스 선언** — `Refer to the {camera movement | action | blocking | light-and-shadow change | character positioning | music and SFX | pacing} of @video1.`
2. **대응관계 매핑** — 어떤 모델이 어떤 레퍼런스인지:
   `Replace the {색/형태} model in @video1 with {인물명} from @image1; the {색/형태} model with {인물명} from @image2; the {색/형태} model with {소품명} from @image3.`
3. **플롯 디테일** — 시간·논리 순으로 동작·표정·대사·조명 변화
4. **씬 처리** — 텍스트로 쓰거나 `use the {씬 서술} in @image4 for the background`
5. **전체 마무리** — 전체 스타일 / 화질 요구 / 일관성 제약 / 오디오 처리

> ⚠️ 거친 화이트모델에 **팔다리나 날개가 있으면** 그 사지의 완전한 동작 시퀀스를 다 써줘야 뻣뻣해지지 않는다. 베스트는 **사지·날개 있는 모델을 아예 안 올리는 것.**

### G-2. 정밀 화이트모델 — 모델링·구조가 이미 완성, 재질/조명/스타일만 입힘

> **[렌더 커맨드] + [구간별 렌더 서술] + [씬 처리] + [전체 마무리]**

1. `Render the white-model animation of @video1 into the final film.`
2. 구간별: `0-{N}s: {배경 환경, 톤·분위기, 캐릭터 재질, 광影 효과}` / `{N}s {전환 트리거와 방식}: {전환 후 새 씬의 렌더 서술}`
3. 씬 처리 — 텍스트 또는 `@image1`
4. 전체 마무리 — 새 씬에서 환경·캐릭터 렌더가 유지되는지 변하는지 + 오디오 처리

> ⚠️ 정밀 화이트모델은 업로드 전에 **궤적선 / 좌표축 / 카메라 콘** 같은 간섭 정보를 지워라.

---

## § H. 멀티그리드 스토리보드

여러 칸으로 나뉜 스토리보드 이미지를 플롯 레퍼런스로 넣으면 그 순서대로 영상을 만든다.

- **단순 선화 / 졸라맨 스토리보드**를 권장한다 (디테일한 그림일수록 오히려 방해).
- 구도·샷 사이즈·카메라 무빙·동작은 **프롬프트로** 통제한다 — 그림은 순서와 배치만 담당.

```
@image1 is a 6-panel storyboard. Generate one continuous video following panels 1 to 6 in order.
Panel 1 is a wide establishing shot, panel 2 a medium two-shot, panel 3 an over-the-shoulder...
```

---

## § I. 심리스 영상 전환 (두 영상 잇기)

영상 2개를 업로드하고 사이 간극을 모델이 생성하게 한다. **원본 클립은 수정되지 않는다.**

```
Splice @video1 and @video2 into one continuous shot. Generate the connecting frames between them.
Use [초점거리 전환 / 회전 착장 전환 / 다이빙 전환] — connect via [action trigger / eyeline pull /
occlusion wipe]. Forbid rigid hard cuts.
```
