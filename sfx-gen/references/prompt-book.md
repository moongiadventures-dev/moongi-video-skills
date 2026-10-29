# SFX 프롬프트북

ElevenLabs Sound Effects는 **묘사에 반응하지 이름에 반응하지 않는다.** "whoosh sound"보다
"fast air movement past a microphone, cloth-like texture, short tail"이 훨씬 정확하다.

## 공식

```
[소리 종류/역할] + [음원·재질] + [동작·세기] + [공간·잔향] + [감쇠] + [네거티브]
```

예시:

| 요구 (한국어) | 재작성한 프롬프트 |
|---|---|
| 문 묵직하게 닫히는 소리 | `heavy wooden door closing, solid latch click, low thud, small room reverb, short decay. no music` |
| 화면 전환 휘슬 | `fast air whoosh passing left to right, soft cloth texture, no impact at the end, quick fade. no music, no melody` |
| 버튼 누르는 톡 | `single soft UI click, small plastic tactile switch, dry, no room, very short. no music` |
| 카페 배경 | `seamless ambient loop of a quiet cafe interior, distant murmur, occasional cup on saucer, low espresso machine hum, no speech. no music` |
| 유리 깨짐 | `glass bottle shattering on a concrete floor, sharp initial crack then scattered shards, medium room, natural decay. no music` |
| 긴장 고조 | `rising tension riser, low synth swell building in intensity, no cymbals, no impact at the end. no melody` |

## 카테고리별 어휘

| 역할 | 쓸 단어 | 길이 |
|---|---|---|
| **motion / 전환** | air movement, whoosh, swish, cloth texture, doppler, pass-by | 0.6–1.5s |
| **impact / 강조** | thud, slam, hit, low-end body, sub drop, tail, room reverb | 0.8–2s |
| **snap / UI** | click, tick, tactile switch, dry, no room, tiny | 0.2–0.5s |
| **riser / 긴장** | rising swell, build, tension, crescendo, no cymbals | 2–4s |
| **chime / 보상** | soft bell, glassy tone, positive, gentle bloom, sparse | 1–2.5s |
| **foley** | footsteps on <재질>, cloth rustle, paper flip, keys jingling, liquid pour | 0.5–3s |
| **mechanical** | servo, motor whir, latch, ratchet, metal-on-metal, hydraulic hiss | 0.5–3s |
| **nature** | wind through <대상>, rain on <재질>, water flow, birds distant | 루프 10–22s |
| **ambience** | seamless ambient loop of…, room tone, distant, no speech | 루프 10–22s |

## 파라미터 감각

- **duration** — 생략하면 모델이 내용에 맞춰 정한다. 원샷은 **생략이 기본**이고, 길이를 정확히
  맞춰야 할 때만 지정한다. 앰비언스 루프는 10–22초로 명시.
- **prompt_influence** — 0.3(기본)은 자연스럽고 변형이 다양하다. 프롬프트를 문자 그대로 따르길
  원하면 0.6–0.8. 1.0에 가까울수록 부자연스럽고 합성 티가 난다.
- **count** — 3개가 실용적 기본. SFX는 "골라 쓰는" 물건이라 한 방에 맞추려 하지 말 것.

## 안티패턴

- ❌ **한 프롬프트에 두 사건** — "문 닫히고 발소리 멀어짐" → 둘 다 흐릿해진다. 따로 뽑아 섞어라.
- ❌ **음악 단어** — `cinematic`, `epic`, `trailer`, `dramatic`, `soundtrack`은 배경음악을 부른다.
  끝에 `no music, no melody`를 습관적으로 붙여라.
- ❌ **감정 형용사만** — "무서운 소리"는 아무거나 나온다. 무엇이 무서운지(저주파 럼블? 금속 삐걱?)를
  써라.
- ❌ **루프에 후처리** — 앞뒤 무음 트림이 이음매를 깬다. 루프는 원본 그대로 쓴다.
- ❌ **말소리 기대** — 이건 TTS가 아니다. 사람 목소리가 필요하면 `no speech`를 넣고 목소리는 따로.

## 레이어링 (프로 결과가 나오는 지점)

단일 생성으로 "묵직하고 고급스러운" 소리는 거의 안 나온다. 실제 사운드 디자인은 겹치는 것:

```
임팩트 =  [transient]  날카로운 초기 어택 (0.2s, dry)
        + [body]      저역 thud (0.8s, 약간의 room)
        + [tail]      잔향/공기 (1.5s, 크게 낮춰서)
```

각각 따로 생성해서 ffmpeg `amix`로 겹치고, tail을 −12dB쯤 깔면 한 방에 뽑은 것과 질이 다르다.

```bash
ffmpeg -i transient.mp3 -i body.mp3 -i tail.mp3 \
  -filter_complex "[2:a]volume=-12dB[t];[0:a][1:a][t]amix=inputs=3:duration=longest:normalize=0" \
  -c:a libmp3lame -q:a 2 impact-layered.mp3
```

## 참고: 톤 계약

브랜드가 있는 작업이면 그 프로젝트의 사운드 톤을 먼저 확인한다. MOONGI/Amplend 계열은
차분·프리미엄(Linear/Anthropic/Vercel 결) — **들리는 게 아니라 느껴지는** 수준. 트레일러 슬램,
심벌 라이저, MrBeast식 과장은 쓰지 않는다.
