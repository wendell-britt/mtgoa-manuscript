# chapters/ — process docs only. The book is not here.

As of 2026-07-28, the manuscript lives in **`manuscript/ch1.md` – `ch9.md`**.
See `specs/MANUSCRIPT_FILE_CANON.md` for the canonical file list and the
standing editorial rules.

The superseded chapter prose that used to live here — the nine `*_FULL_DRAFT.md`
files and their dated intermediates — was retired in the same commit that added
`manuscript/`. All of it remains in git history; nothing was lost.

## Numbering changed

The retired drafts used 0-indexed chapter numbers. `manuscript/` is 1-indexed,
so every reference in the remaining docs here is off by one:

| Old (`chapters/`) | New (`manuscript/`) | Chapter |
|---|---|---|
| ch0-infinite-arcade | ch1.md | The Infinite Arcade |
| ch1-SHAMAN | ch2.md | The Forest |
| ch2-SHAMAN | ch3.md | The Shaman |
| ch3-CHALLENGER | ch4.md | The Challenger |
| ch4-REGENT | ch5.md | The Regent |
| ch5-ARCHITECT | ch6.md | The Architect |
| ch6-diplomat | ch7.md | The Diplomat |
| ch7-sage | ch8.md | The Sage |
| ch8-player | ch9.md | The Player |

## What is still here, and why

The per-chapter `SPEC.md`, editorial specs, metaphor audits, gap analyses, and
`PLAN`/`TASKS` files were kept. They are process history, and nothing in
`manuscript/` replaces them. Check any claim they make against the chapter files
before planning from it — several predate the July line-edit.

`ch0-infinite-arcade/` is the one folder whose **prose** was also kept. The
Chapter 0 → Chapter 1 rewrite dropped material rather than revising it: the
Monopoly origin story appears in two files there and in zero chapters of the
current manuscript. `MONOPOLY_ORIGIN_STORY.md`, `BRIDGE_1_DRAFT.md`, and the
`GM_SECTION` drafts are therefore the only surviving copies of that prose in the
working tree.
