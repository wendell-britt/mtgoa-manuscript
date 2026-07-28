# manuscripts/ AGENTS.md — MTGOA Book Editing

## Primary Identity

MTGOA manuscript — lives in `/home/workspace/manuscripts/`
Syncs to Obsidian via `The-Library/The Library/` (workspace) → Mac

## Canonicality

**As of 2026-07-28 this changed. Read this section before trusting any older doc.**

**Rule:** `manuscript/ch1.md` – `ch9.md` **in this git repository** are the canonical book. Edit these. Nothing supersedes them.
**Rule:** Obsidian and the Claude project are no longer canonical for chapter content. They are upstream history.
**Rule:** No canonical write happens without Wendell's conscious approval.
**Rule:** If an agent drafts or rewrites text without approval, that text is a proposal, not canon.
**Rule:** Anything outside `manuscript/` — including everything in `chapters/`, `compiled/`, and the root-level specs — is process history, a verification surface, or a derived artifact.

## Editing Protocol

When asked to edit, run the WAVE Editing Spiral:
**Full spec:** `The-Library/The Library/07 Book OS/SPEC_BOOK_EDITING_PROCESS.md`

**Rule:** ALWAYS do pre-session 321 somatic practice (https://wendellbritt.zo.space/321)
**Rule:** ALWAYS git commit before and after editing
**Rule:** ALWAYS update tracker after session

## Git (CRITICAL)

```bash
# WRONG — workspace git ignores manuscripts/
cd /home/workspace && git add manuscripts/...

# RIGHT
cd /home/workspace/manuscripts && git add chapters/... && git commit -m "edit: [description]"
```

## Canonical Chapter Files

| Ch | File | Title |
|---|---|---|
| 1 | `manuscript/ch1.md` | The Infinite Arcade |
| 2 | `manuscript/ch2.md` | The Forest |
| 3 | `manuscript/ch3.md` | The Shaman |
| 4 | `manuscript/ch4.md` | The Challenger |
| 5 | `manuscript/ch5.md` | The Regent |
| 6 | `manuscript/ch6.md` | The Architect |
| 7 | `manuscript/ch7.md` | The Diplomat |
| 8 | `manuscript/ch8.md` | The Sage |
| 9 | `manuscript/ch9.md` | The Player |

Numbering is 1-indexed. The retired `chapters/ch[N]-[FACE]/` drafts were
0-indexed, so every reference in an older doc is off by one. Conversion table in
`chapters/README.md`.

**Rule:** Every number quoted about this manuscript comes from running an
instrument in `instruments/` against these files. Planning documents have been
wrong.
**Rule:** Edits go through `instruments/spec_edit.py`, which aborts and writes
nothing on a missed or duplicated anchor.
**Rule:** Run `instruments/dupes.py` on new prose before insertion. Sentences
have been accidentally duplicated across five chapters before.

## Companion Files

- `specs/MANUSCRIPT_FILE_CANON.md` — canon, standing editorial rules, the voice gate
- `specs/MTGOA_INSTRUMENTS_TOOLKIT.md` — the reviewer gate and measurement tools
- `chapters/README.md` — what survives in `chapters/`, and the renumbering
- `MANIFEST.md` — export index and per-chapter word counts
- `MTGOA_BOOK_WORK_TRACKER.md` — updated after every session

## EA Standards

Every move in the book:
**[DISSATISFACTION → SATISFACTION] Transcend [X] — Emotion Name → Alchemical Outcome**

Energy economy (+2/+1/-1) — context for writer only, NOT in book content.
