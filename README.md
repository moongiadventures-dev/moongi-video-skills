# MOONGI Video Skills

> **PM 출신 1인 AI 스튜디오가 2년 동안 쓰고 만든 공짜 Claude Code 스킬 모음.**
> AI 영상 유료 서비스(Tella · Higgsfield · CapCut Pro) 끊고 Claude Code + 공짜 스킬로 돌리는 작업 흐름을 공개합니다.

**— [moongi.studio](https://moongi.studio) · [@moongi_adventures](https://instagram.com/moongi_adventures)**

---

## 🎬 9개 스킬

| # | 스킬 | 하는 일 | 비용 |
|---|------|---------|------|
| 1 | **[video-shotcraft](./video-shotcraft)** | 웹사이트 · 앱을 시네마틱 제품 영상으로 (스크린샷+카메라워크) | 🆓 |
| 2 | **[motion-pack](./motion-pack)** | HTML+GSAP 모션 그래픽 템플릿 10종 (파형·지도·토글·카운터·9:16) | 🆓 |
| 3 | **[animate](./animate)** | SVG+Canvas+WebGL로 프레임마다 코드로 그린 영상 (스타일 레퍼 복제) | 🆓 |
| 4 | **[sfx-gen](./sfx-gen)** | 효과음 자동 생성 (ElevenLabs Sound Effects) | 💰 ElevenLabs API |
| 5 | **[seedance-25](./seedance-25)** | Dreamina Seedance 2.5 프롬프트 공식 자동 생성 (5개 모드 전부) | 🆓 (Dreamina 서비스는 유료) |
| 6 | **[higgsfield-seedance2-jineng](./higgsfield-seedance2-jineng)** | Higgsfield × Seedance 15종 서브 (시네마틱·MV·광고·UGC) | 🆓 (Higgsfield 서비스는 유료) |
| 7 | **[nano-banana-pro](./nano-banana-pro)** | Gemini Nano Banana 이미지 생성·편집 CLI (레퍼 체이닝) | 🎁 Gemini (Flash 공짜) |
| 8 | **[video-watch](./video-watch)** | 영상을 "진짜로" 봄 — yt-dlp + Whisper + 프레임 그리드로 레퍼 뜯어보기 | 🆓 |
| 9 | **[ad-video-pipeline](./ad-video-pipeline)** | Stage 0~5 광고 영상 전체 파이프라인 (브리프→컨셉→샷→이미지→영상→편집) | 💰 중간 영상 생성 콜 |

> **코드·스킬 자체는 전부 공짜.** 서비스 유료 호출(ElevenLabs·Higgsfield·Dreamina 등)은 선택이고, 공짜 대안으로도 다 돌아갑니다.

---

## ⚙️ 설치

### Claude Code 사용자

```bash
# 1. 레포 clone
git clone https://github.com/<your-handle>/moongi-video-skills.git
cd moongi-video-skills

# 2. 쓰고 싶은 스킬을 ~/.claude/skills/에 심볼릭 링크
# (Mac/Linux)
ln -s "$(pwd)/video-shotcraft" ~/.claude/skills/video-shotcraft

# (Windows PowerShell — 관리자 모드)
New-Item -ItemType Junction -Path "$env:USERPROFILE\.claude\skills\video-shotcraft" -Target "$PWD\video-shotcraft"
```

### 특정 스킬만 받기 (zip 다운로드)
GitHub 레포 메인 페이지에서 **Code → Download ZIP** → 원하는 폴더만 복사.

각 스킬 폴더 안의 `SKILL.md`가 **설치·사용·예제** 매뉴얼입니다.

---

## 🧰 전제 도구

스킬마다 다르지만, 공통으로 많이 쓰는 것:

| 도구 | 용도 | 설치 |
|------|------|------|
| **Claude Code** | 스킬 실행 환경 | [claude.com/claude-code](https://claude.com/claude-code) |
| **uv** | Python 스크립트 실행 (`uv run`) | [astral.sh/uv](https://docs.astral.sh/uv/) |
| **ffmpeg** | 영상·오디오 처리 | `brew install ffmpeg` / `choco install ffmpeg` |
| **Node.js 20+** | HyperFrames · motion-pack 렌더 | [nodejs.org](https://nodejs.org/) |
| **Playwright** | HTML→영상 렌더링 | `npx playwright install chromium` |

각 스킬의 `SKILL.md`에 **필요한 도구와 API 키**가 명시돼 있습니다.

---

## 🪪 라이선스

MIT License — 자유롭게 쓰고, 바꾸고, 재배포하세요.
상업적 사용 OK. 크레딧 안 달아도 됨 (달아주면 고마움 🙏).

---

## 🧑‍💻 MOONGI는 누구?

- **Amazon Senior PM** (2026 종료) → **UC Berkeley MBA** → 현재 **MOONGI Studio** 전업 CEO
- 1인 AI 스튜디오로 광고 영상 · 브랜드 · 숏폼 전부 혼자 만듭니다
- Instagram [@moongi_adventures](https://instagram.com/moongi_adventures)에서 "직접 다 써본" AI 스킬·자동화를 공유합니다

**뉴스를 전달하는 사람이 아니라, 실제로 쓰고 만드는 사람입니다.**

---

## 🔗 더 보기

- IG: [@moongi_adventures](https://instagram.com/moongi_adventures)
- Threads: [@moongi_adventures](https://threads.net/@moongi_adventures)
- Studio: [moongi.studio](https://moongi.studio)
- 수업: Class 101 — "AI로 수익화하는 1인 스튜디오"
- 컨설팅 · 협업 문의: moongi.adventures@gmail.com

---

**🙏 Star ⭐ 하나면 다음 EP 제작 동기 2배.**
