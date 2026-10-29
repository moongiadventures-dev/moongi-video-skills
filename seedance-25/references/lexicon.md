# 어휘 사전 — 공식의 빈칸을 채우는 말들

사용자에게 묻지 말고 여기서 뽑아 쓴다. 전부 영어로 정리 — 묘사문은 영어로 쓰는 게 최적화 1순위라서.

---

## 1. 샷 사이즈 / 시점

| 한국어 | 영어 | 쓸 때 |
|---|---|---|
| 익스트림 와이드 | extreme wide shot / establishing shot | 공간 소개, 스케일 |
| 와이드 | wide shot, full-body composition | 전신 동작 |
| 미디엄 | medium shot, waist-up | 대화 기본 |
| 바스트 | chest-up close composition | 감정 |
| 클로즈업 | close-up | 표정·디테일 |
| 익스트림 클로즈업 | extreme close-up, macro | 눈·질감·제품 |
| 오버숄더 | over-the-shoulder shot | 관계·대화 |
| 로우앵글 | low-angle shot | 위압·영웅화 |
| 하이앵글 | high-angle shot | 취약·관찰 |
| 부감/항공 | overhead shot, top-down, aerial shot | 배치·규모 |
| 1인칭 | first-person perspective (POV) | 몰입 |
| 더치 앵글 | dutch angle, canted frame | 불안 |

## 2. 카메라 무빙

| 무빙 | 영어 |
|---|---|
| 밀기/당기기 | slow dolly-in / dolly-out, push-in, pull-back |
| 팬 | pan left, pan right |
| 틸트 | tilt up, tilt down |
| 궤도 | orbit around the subject, arc shot |
| 따라가기 | tracking shot, follow shot |
| 크레인 | crane up, jib down |
| 핸드헬드 | slight handheld feel, generally steady |
| 흔들림 | rapid whip pan with motion blur |
| 나선 | descending spiral orbit |
| 고정 | locked-off static shot |
| 줌 | slow zoom-in, snap zoom |
| 스테디캠 | smooth steadicam glide |

**쓰는 법:** 항상 "무엇을 프레임 어디에 유지하며"까지 붙인다.
`Low-angle medium shot with a slight handheld feel, generally steady, keeping the subject centered at all times.`

## 3. 조명

| 무드 | 영어 |
|---|---|
| 자연 아침빛 | soft morning light slanting from the horizon |
| 골든아워 | warm golden-hour backlight, long shadows |
| 볼류메트릭 | Tyndall effect, volumetric light shafts piercing the mist |
| 실내 창광 | soft north-facing window light, gentle falloff |
| 하드 키 | hard single key light, deep contrast, chiaroscuro |
| 링 | even ring-light beauty lighting, catchlight in the eyes |
| 네온 | cyan-and-magenta neon rim light, wet reflective surfaces |
| 실루엣 | strong backlight, subject rendered as a silhouette |
| 캔들 | flickering warm candlelight, unstable shadow edges |
| 형광 | cold overhead fluorescent, slightly green cast |
| 달빛 | cool moonlight, low-key, deep blue shadows |
| 폭발/섬광 | brief burst of white light washing out the frame |

## 4. 질감 · 리얼리즘 강제어 (AI티 제거)

프롬프트에 이 문구들을 꼭 섞어라. 공식 가이드가 "AI 느낌 약화"의 핵심으로 지목한 것들이다.

```
retaining true micro pores and skin texture
native skin texture, no plastic sheen, no greasy highlights
hair roots distinct, fluffy and natural fur
real wear creases on the leather, faint scuffing
emphasize ultimate real physical texture
faint real freckles across the nose bridge
natural depth of field, foreground slightly blurred, subject in sharp focus
subtle lens breathing, mild film grain
```

**금지어 개념:** `beautiful`, `stunning`, `perfect`, `8k masterpiece` 류는 넣지 마라 — 화질 안 오르고 AI티만 올린다.

## 5. 비주얼 스타일

| 스타일 | 영어 |
|---|---|
| 시네마틱 실사 | cinematic realistic, film-grade photography |
| 자연 다큐 | realistic nature documentary style |
| 커머셜 광고 | authentic commercial advertising look, clean product lighting |
| 레트로 필름 | retro film stock, halation, slight color shift |
| 사이버펑크 | cyberpunk, neon-drenched, high-contrast |
| 2D 애니 | 2D anime style, cel shading, clean line art |
| 3D CG | 3D CG render, subsurface scattering, ray-traced reflections |
| 한국적 미감 | East Asian aesthetic, ink-wash tonality, restrained palette |
| 브이로그 | handheld vlog look, natural available light |
| 화이트모델 | pure white clay-model render, no materials |

## 6. 사운드 지시

영상 안에서 나는 소리를 명시하면 오디오가 같이 나온다.

```
Natural environmental sound: flowing water, wings flapping, a clear long call.
Diegetic sound only — footsteps on wet stone, distant traffic, cloth rustling.
The character says in Korean: "여기서 기다릴게."
No background music. No narration. No subtitles.
```

- 대사는 말할 언어 그대로 쓴다.
- BGM을 원하면 명시적으로 요청한다 — 안 쓰면 안 붙는 게 2.5의 기본 동작이다.

## 7. 네거티브 기본 세트

슬라이스마다 짧게, 전역 보충에서 한 번 더 길게.

```
슬라이스용:  No subtitles, no BGM.
전역용:      Negative: no subtitles, no on-screen text, no watermark, no background music,
             no narration, no extra characters entering frame, no sudden appearance of objects,
             no rigid hard cuts, no distorted hands, no duplicated limbs.
```

상황별 추가:
- 인물 흔들림 방지 → `no large body movements`
- 얼굴 섞임 방지 → `each character must keep independent, distinct facial features`
- 화이트모델 유지 → `keep the pure white clay look, no materials, no textures`
- 그린스크린 유지 → `keep the green screen background unchanged`
