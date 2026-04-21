# CHAPTER_LOCATION_SPEC.md

Canonical location policy for MTGOA chapter assets.

## Canonical root

All chapter specs and full drafts belong under:

`manuscripts/chapters/chN-<face>/`

Root-level `manuscripts/CHAPTER*.md` files are working notes or legacy migration sources, not canonical full-draft storage.

## Canonical chapter map

| Chapter | Canonical folder | Canonical draft file |
|---|---|---|
| 0 | `manuscripts/chapters/ch0-infinite-arcade/` | `CHAPTER0_DRAFT.md` |
| 1 | `manuscripts/chapters/ch1-SHAMAN/` | `CHAPTER1_FULL_DRAFT.md` |
| 2 | `manuscripts/chapters/ch2-SHAMAN/` | `CHAPTER2_SHAMAN_FULL_DRAFT.md` |
| 3 | `manuscripts/chapters/ch3-CHALLENGER/` | `CHAPTER3_CHALLENGER_FULL_DRAFT.md` |
| 4 | `manuscripts/chapters/ch4-REGENT/` | `CHAPTER4_REGENT_FULL_DRAFT.md` |
| 5 | `manuscripts/chapters/ch5-ARCHITECT/` | `CHAPTER5_ARCHITECT_FULL_DRAFT.md` |
| 6 | `manuscripts/chapters/ch6-diplomat/` | `CHAPTER6_DIPLOMAT_FULL_DRAFT.md` |
| 7 | `manuscripts/chapters/ch7-sage/` | `CHAPTER7_SAGE_FULL_DRAFT.md` |
| 8 | `manuscripts/chapters/ch8-player/` | `CHAPTER8_PLAYER_FULL_DRAFT.md` |

## Migration status (2026-04-20)

- Chapters 1-6 full drafts copied to canonical folders and verified
- Legacy root full drafts archived to `manuscripts/_legacy_root_drafts/`
- Chapters 0, 7, 8 were already canonical
- Root-level `CHAPTER1_URGENCY_DRAFT.md` remains as a component draft, not the full chapter draft

## Naming normalization note

Folder names currently mix case styles (e.g., `ch2-SHAMAN` and `ch7-sage`).

Recommendation: keep current folder names until chapter drafting/review is stable, then run a single controlled rename migration with path updates.