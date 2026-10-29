# -*- coding: utf-8 -*-
"""영상 프로젝트 폴더를 깐다. 정본 = ../references/folder-structure.md

먼저 정할 것 — **웹사이트 첫 화면에 들어가는 영상인가, 아닌가.** 이거 하나뿐이다.

  web         웹 히어로 — 무음 · 5~8초 · 컷 전환 0 · 심리스 루프 제약이 붙는다
  standalone  그 외 전부 (광고 · 브랜드 필름 · 캠페인)

뿌리는 경로를 보고 알아서 잡는다. 위에 브랜드 프로젝트가 있으면 그 밑으로 들어간다.
브랜드냐 단독이냐는 **묻지 않는다** — 결과물이 똑같고 폴더 위치만 다르기 때문이다.

사용:
    python new_video_project.py "<경로>"                      # 자동 판정
    python new_video_project.py "<경로>" --placement web --name hero
    python new_video_project.py "<경로>" --brand Ffern --title "Summer 26" --sec 30 --ar 9:16 --client

이미 있는 파일은 건드리지 않는다. 여러 번 돌려도 안전하다.
"""
import argparse
import sys
from pathlib import Path

DIRS = [
    "01_brief/client",
    "02_refs/clips", "02_refs/frames",
    "03_locks/product", "03_locks/character", "03_locks/space", "03_locks/_rejected",
    "04_shotlist",
    "05_images/_rejected",
    "06_clips/_rejected",
    "07_edit/audio", "07_edit/work",
    "08_deliver",
]
CLIENT_DIRS = ["01_brief/contract/초안_md"]

# 폴더는 「영어 (한국어)」로 만든다 — 수강생·발주자가 열었을 때 바로 알아보게.
# 코드 안에서는 영어 키로만 다루고, 실제로 만들 때 이 표로 이름을 붙인다.
SEG = {
    "01_brief":    "01_brief (브리프)",
    "02_refs":     "02_refs (레퍼런스)",
    "03_locks":    "03_locks (락)",
    "04_shotlist": "04_shotlist (컷 표)",
    "05_images":   "05_images (이미지)",
    "06_clips":    "06_clips (영상)",
    "07_edit":     "07_edit (편집·검수)",
    "08_deliver":  "08_deliver (납품)",
    "client":      "client (받은 자료)",
    "contract":    "contract (계약)",
    "clips":       "clips (영상)",
    "frames":      "frames (프레임)",
    "product":     "product (제품)",
    "character":   "character (인물)",
    "space":       "space (공간)",
    "audio":       "audio (오디오)",
    "work":        "work (중간 렌더)",
    "_rejected":   "_rejected (반려)",
}


def real(rel: str) -> str:
    """'01_brief/client' -> '01_brief (브리프)/client (받은 자료)'"""
    return "/".join(SEG.get(seg, seg) for seg in rel.split("/"))

KEEP = {
    "01_brief/client": "받은 자료를 받은 날짜 폴더째로 둔다. 손대지 않는다.\n예) 2026-09-25_기획서/\n",
    "01_brief/contract/초안_md": "계약 초안 md. 현행 계약서(docx/pdf)는 한 단계 위에.\n",
    "02_refs/clips": "실제로 받은 레퍼 영상. 토픽만 같은 건 레퍼가 아니다 — 포맷까지 같아야 한다.\n",
    "02_refs/frames": "레퍼에서 뜯어낸 프레임.\n",
    "03_locks/product": "제품 락. 실물 사진이면 LOCKS.md 에 「합성·생성 금지」를 명시한다.\n",
    "03_locks/character": "인물 락. 얼굴은 이미지와 프롬프트를 둘 다 건다.\n",
    "03_locks/space": "공간·세트 락.\n",
    "03_locks/_rejected": "반려한 락. 지우지 않는다. 파일명 앞에 이유 — _rejected_L_europe.png\n",
    "05_images/_rejected": "반려한 이미지. 파일명 앞에 이유.\n",
    "06_clips/_rejected": "반려한 클립. 파일명 앞에 이유.\n",
    "07_edit/audio": "나레이션 · 음악 · SFX.\n",
    "07_edit/work": "중간 렌더. 여기 있는 건 납품이 아니다.\n",
    "08_deliver": "최종본만. 변형은 파일명으로 — _30s_1920x1080_nosub_v1.mp4\n"
                  "루트에 production/ final/ 을 또 만들지 않는다.\n",
}

PLACEMENT_NOTE = {
    "web": "웹사이트 첫 화면에 들어가는 영상입니다.\n"
           "- **무음 · 5~8초 · 컷 전환 0 · 심리스 루프 · 첫 프레임이 poster · 글자 자리 비우기**\n"
           "- 사이트 브리프는 `../../00_brief/brief.md` — **영상 브리프는 여기 따로 씁니다**\n"
           "- 완성본은 `08_deliver (납품)/` 에 두고, 사이트에는 거기서 복사해 갑니다\n"
           "  (사이트가 쓰는 파일은 `../../site/media/` 로. 원본은 여기 남깁니다)",
    "standalone": "단독 영상 건입니다.",
}
BRAND_NOTE = ("\n- 브랜드 프로젝트 안입니다 — 색·서체는 `../../00_Brand/brand-dna.md` 에서 가져옵니다.\n"
              "  여기서 새로 정하지 않습니다. 브리프 2번 블록은 그걸 옮겨 적는 칸입니다.")


def detect(path: Path) -> str:
    """웹 히어로인지 아닌지만 본다."""
    for base in (path, *path.parents[:3]):
        if (base / "site").is_dir() and (base / "00_brief").is_dir():
            return "web"
    return "standalone"


def brand_root(path: Path):
    """위에 브랜드 프로젝트가 있으면 그 뿌리를 돌려준다. 없으면 None."""
    for base in (path, *path.parents[:3]):
        if (base / "00_Brand").is_dir():
            return base
    return None


def resolve_root(path: Path, placement: str, name: str) -> Path:
    """placement 에 맞는 실제 뿌리를 돌려준다."""
    if placement == "web":
        # 이미 02_assets 밑이면 그대로, 아니면 웹프로젝트 밑으로 내려보낸다
        if any(x.startswith("02_assets") for x in path.parts):
            return path
        if (path / "site").is_dir():
            return path / "02_assets" / f"video_{name}"
        return path
    # standalone — 위에 브랜드 프로젝트가 있으면 그 09_Video 밑으로 들어간다
    if any(x.startswith("09_Video") for x in path.parts):
        return path
    b = brand_root(path)
    if b is not None:
        return b / "09_Video" / name
    return path


def readme(brand, title, sec, ar, placement, under_brand=False):
    note = PLACEMENT_NOTE[placement] + (BRAND_NOTE if under_brand else "")
    return f"""# {brand} — {title}

| | |
|---|---|
| 길이 | {sec}초 |
| 비율 | {ar} |
| 어디에 붙나 | **{placement}** |
| 지금 | 01_brief |

{note}

구조 정본 — `Skills/video-production/ad-video-pipeline/references/folder-structure.md`

## 진행

- [ ] 1 브리프 `01_brief/`
- [ ] 2 레퍼런스 `02_refs/`
- [ ] **3 락 `03_locks/`** — 여기가 안 끝나면 4로 안 간다
- [ ] 4 컷 표 `04_shotlist/`
- [ ] 5 이미지 `05_images/`
- [ ] 6 영상 `06_clips/`
- [ ] 7 편집 · 검수 `07_edit/`
- [ ] 8 얹기 · 납품 `08_deliver/`
"""


FILES = {
    "01_brief/brief.md": """# 영상 브리프 — 발주자에게 받는 것

**이건 내가 상상해서 채우는 문서가 아니라 클라이언트에게 받아내는 목록이다.**
받은 건 그대로 옮기고, 못 받은 건 맨 아래 체크리스트에 남긴다.
웹사이트 안에 들어가는 영상이어도 **영상 브리프는 따로 쓴다.** 묻는 게 다르다.

원본 수령: `client/<받은날짜>_<무엇>/` — 원본은 손대지 않는다

---

## 1. 캠페인 브리프

| 항목 | 내용 |
|---|---|
| 목표 | 인지 / 신제품 출시 / 전환 / 이벤트 / 리텐션 |
| 타겟 | 나이대 · 라이프스타일 · 관심사 |
| 게재 채널 | Reels / TikTok / YouTube / 메타 광고 / 웹사이트 |
| 길이 | 15 / 30 / 60초 |
| 비율 | 9:16 / 16:9 / 1:1 / 4:5  (메인 + 베리에이션) |
| 톤 | 에너제틱 / 감성 / 시네마틱 / 럭셔리 / 유머 |
| 스토리 아이디어 | 발주자가 짜 온 안이 있나 |
| 핵심 메시지 (1개) | |
| 태그라인 | |
| CTA | 영상 안에 넣나, 광고 세팅에서 거나 |

## 2. 브랜드 아이덴티티

| 항목 | 받음? | 내용 |
|---|---|---|
| 컬러 hex | ⬜ | |
| 폰트 파일 · 폰트명 | ⬜ | 자막 · 텍스트 오버레이용 |
| 로고 원본 (AI/SVG/투명 PNG) | ⬜ | |
| 가이드라인 | ⬜ | 금지 컬러 · 로고 사용 규칙 · 보이스앤톤 |
| 그레이딩 방향 | | 저채도 / 비비드 / 웜 / 쿨 |

**금지 목록** (발주자가 명시한 것 그대로)
-

## 3. 제품 자료

| 항목 | 받음? | 내용 |
|---|---|---|
| 고해상도 사진 — 정면·측면·후면·디테일 | ⬜ | |
| 착용컷 · 사용컷 | ⬜ | |
| 컬러 옵션 · 소재 · 마감 | | 무광 / 유광 / 원단 |
| 씬별로 어떤 제품을 보여주나 | | |
| 라벨 · 표기 | | 실물과 다른 표기가 있나 |

**제품 절대 조건** — 씬마다 달라지면 안 되는 것 (형태 · 비율 · 캡 · 라벨 위치)
-

⚠️ 실물 제품이면 **합성·생성 금지**인지 확인하고 `03_locks/LOCKS.md` 에 옮겨 적는다.

**공간·장소 광고라면**
| 항목 | 받음? |
|---|---|
| 매장 · 호텔 · 현장 실사진 | ⬜ |
| 평면 · 동선 | ⬜ |

## 🟡 4. 모델 — 나오는 경우에만

| | |
|---|---|
| 실존 / AI 가상 | |

**실존이면** — ⬜ 얼굴·전신 사진 여러 장 · ⬜ 초상권 동의서 · ⬜ **AI 합성 사용 동의**
**가상이면** — 나이 · 인상 · 체형 · 헤어 방향:

의상 — 씬(Act)별로 정해져 있나. **의상 락은 Act 단위로 건다.**
| Act | 의상 |
|---|---|

## 🟡 5. 오디오 — 소리가 들어가는 경우에만

| 항목 | 내용 |
|---|---|
| 음악 | 브랜드 라이선스 곡 있나 / 생성 음악 |
| 음원 파일 | ⬜ (뮤비면 필수) |
| 나레이션 | 있음 / 없음 |
| 대본 초안 | ⬜ |
| 브랜드명 · 제품명 발음 | |
| 성우 톤 · 기존 광고 목소리 | |

⚠️ 웹사이트 첫 화면 영상이면 **무음**이다. 이 블록을 건너뛴다.

---

## 내가 정한 것

발주자가 안 정해 준 것, 또는 내가 바꾸자고 한 것. **근거를 같이 쓴다.**
-

## 제작 리스크

지금 보이는 위험. 나중에 일정·견적 협의의 근거가 된다.
1.

## ⬜ 아직 못 받은 자료

기획서에 "첨부"라고 돼 있는데 실제로 없는 것까지 전부.
**여기 남은 게 있으면 그만큼 일정이 밀린다는 걸 발주자에게 먼저 알린다.**

- [ ]
""",
    "01_brief/scope.md": """# 스코프 — 견적의 근거

| 항목 | 값 |
|---|---|
| 컷 수 | |
| 수정 횟수 | |
| 납품 형식 | 길이 · 해상도 · 비율 · 자막 유무 |
| 사용 범위 | 채널 · 기간 |
| 포함 안 되는 것 | |

★ 여기서 정한 게 나중에 추가 견적의 근거가 된다. 빈칸으로 두지 않는다.
""",
    "02_refs/teardown.md": """# 레퍼 해부

**토픽만 같으면 레퍼가 아니다. 포맷까지 같아야 한다.**
실황·예고편·리뷰는 레퍼가 아니다. 긁지 말고 열어서 끝까지 본다.

## 레퍼 1 — (제목 / 링크)
| | |
|---|---|
| 길이 · 컷 수 | |
| 첫 3초에 뭐가 나오나 | |
| 카메라 | |
| 색 · 톤 | |

**가져올 것 (2~3개)** — 각각 「왜 가져오나」 한 줄
-

**버릴 것** — 각각 「왜 버리나」 한 줄
-
""",
    "03_locks/LOCKS.md": """# 락 대장

**컷보다 락이 먼저다.** 락이 어정쩡한 채로 컷을 뽑으면 결국 전부 버린다.

| 락 | 파일 | 생성 / 실물 | 규칙 |
|---|---|---|---|
| 제품 | `product/` | | |
| 인물 | `character/` | | |
| 공간 | `space/` | | |

## 앵커 문장 — 모든 프롬프트에 똑같이 붙인다

지울 것만 적고 **남길 것을 안 적으면** 그 부분은 매번 새로 그려진다.

```
(같은 방 / 같은 얼굴이라고 못 박기)
(카메라 위치 · 프레임 안에서 무엇이 중앙인지)
(바뀌면 안 되는 것 — 개수 · 위치 · 색)
Do NOT move X, do NOT add or remove Y, do NOT rotate the camera.
```

## 반려 기록
| 파일 | 왜 반려했나 |
|---|---|
""",
    "04_shotlist/shotlist.md": """# 컷 표

★ **락 칸이 비면 그 컷은 아직 못 찍는다는 뜻이다.**
「필요 이미지」는 `05_images/` 폴더 이름과 글자까지 같게 쓴다.

| ID | 초 | 락 | 필요 이미지 | 생성 | 상태 |
|---|---|---|---|---|---|
| 01 |  |  |  | 이미지→영상 | ⬜ |

상태 — ⬜ 대기 · 🔄 재작업 · ✅ 확정
""",
    "04_shotlist/concept.md": """# 컨셉

**한 줄:**

**톤:**

**왜 이 컨셉인가** — 브리프의 「목표」와 「핵심 메시지 1개」를 어떻게 받는가:

**발주자가 안을 짜 왔다면** — 그 안을 그대로 적고, 바꾼 데만 표시한다.
시사오처럼 발주자가 씬 구성을 직접 써 오는 경우가 실제로 있다.
그럴 땐 우리 시안 = 그 안을 무드보드와 핵심 컷 이미지로 시각화하는 것이다.
""",
    "04_shotlist/storyboard.md": "# 스토리보드\n\n안이 여러 벌이면 파일을 나눈다 — `storyboard_30s.md` / `storyboard_40s.md`.\n**폴더를 파지 않는다.**\n\n| 초 | 무엇이 보이나 | 무슨 소리 | 왜 이 컷 |\n|---|---|---|---|\n|  |  |  |  |\n",
    "04_shotlist/continuity.md": """# 연속성 표

구조가 단계마다 쌓이는 영상(시공·조립·성장)에서만 쓴다. 아니면 이 파일은 지운다.
**이 표를 프롬프트에 그대로 넣는다.**

| 항목 | 1 | 2 | 3 | 4 | 종류 |
|---|---|---|---|---|---|
|  |  |  |  |  | 영구 / 가설 |

- **영구** — 한 번 생기면 끝까지 남는다
- **가설** — 한 번 빠지면 다시 안 나온다
- **절대 고정** — 카메라 · 개구부 · 마감

검수 = 단계별 프레임을 나란히 놓고 각 행을 왼쪽에서 오른쪽으로 읽는다.
영구 항목이 ● 뒤에 빈칸이면 다시 뽑는다.
**전체 화면으로 보면 안 보인다.** 의심되는 부분만 잘라서 이어 붙여야 보인다.
""",
    "07_edit/CHECK.md": """# 검수 — 보여주기 전에 내가 먼저 본다

- [ ] 락이 끝까지 지켜졌나 (얼굴 · 제품 · 문·창 개수)
- [ ] 한 번 생긴 게 사라지지 않나 — **의심 부분만 잘라서 이어 붙여 본다**
- [ ] 앞뒤에 구도가 튀는 구간이 없나 (scene 검출로 찾는다)
- [ ] 화면에 글자·로고가 끼어들지 않았나
- [ ] 비율이 브리프대로인가
- [ ] 소리 — 웹 첫 화면이면 **무음**인가

```bash
# 구도 튐 찾기
ffmpeg -t 1.5 -i in.mp4 -filter_complex "select='gt(scene,0.06)',metadata=print:file=-" -f null -
```
""",
    "07_edit/edl.md": "# 편집 순서\n\n| # | 클립 | 인 | 아웃 | 길이 | 비고 |\n|---|---|---|---|---|---|\n|  |  |  |  |  |  |\n",
    "08_deliver/DELIVERY.md": """# 납품

변형은 **파일명으로** 푼다. 폴더를 새로 파지 않는다.
`{brand}_{길이}_{WxH}_{sub|nosub}_v1.mp4`

| 파일 | 길이 | 해상도 | 자막 | 용도 |
|---|---|---|---|---|
|  |  |  |  |  |

사용 범위 · 기간:
포트폴리오 게시 권리:
""",
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--placement", choices=["web", "standalone"], default=None,
                    help="웹 히어로인가 아닌가. 생략하면 경로를 보고 판정한다")
    ap.add_argument("--name", default="hero", help="web/brand 일 때 하위 폴더 이름")
    ap.add_argument("--brand", default="(브랜드)")
    ap.add_argument("--title", default="(캠페인)")
    ap.add_argument("--sec", default="30")
    ap.add_argument("--ar", default="16:9")
    ap.add_argument("--client", action="store_true", help="외주 건 — 계약 폴더도 깐다")
    a = ap.parse_args()

    given = Path(a.path)
    placement = a.placement or detect(given)
    auto = a.placement is None
    root = resolve_root(given, placement, a.name)

    root.mkdir(parents=True, exist_ok=True)
    dirs = DIRS + (CLIENT_DIRS if a.client else [])
    for d in dirs:
        p = root / real(d)
        p.mkdir(parents=True, exist_ok=True)
        note = p / "_README.txt"
        if d in KEEP and not note.exists():
            note.write_text(KEEP[d], encoding="utf-8")

    files = dict(FILES)
    under_brand = placement == "standalone" and brand_root(given) is not None
    files["README.md"] = readme(a.brand, a.title, a.sec, a.ar, placement, under_brand)
    made, skipped = [], []
    for rel, body in files.items():
        p = root / real(rel)
        if p.exists():
            skipped.append(rel)
            continue
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(body, encoding="utf-8")
        made.append(rel)

    print(f"placement = {placement}" + ("  (경로 보고 자동 판정 — 틀리면 --placement 로 지정)" if auto else ""))
    if under_brand:
        print("브랜드 프로젝트 안이라 09_Video/ 밑에 깝니다")
    print(f"뿌리 = {root}")
    for f in sorted(made):
        print("  +", real(f))
    if skipped:
        print("  (이미 있어서 건너뜀: " + ", ".join(sorted(skipped)) + ")")
    print("\n다음 — 01_brief/brief.md 부터. 락이 끝나기 전에는 04로 가지 않는다.")


if __name__ == "__main__":
    sys.exit(main())
