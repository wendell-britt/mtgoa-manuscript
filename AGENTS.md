# manuscripts/ AGENTS.md — MTGOA Book Editing

## Primary Identity

MTGOA manuscript — lives in `/home/workspace/manuscripts/`
Syncs to Obsidian via `The-Library/The Library/` (workspace) → Mac

## Canonicality

**Rule:** Obsidian is the canonical home for MTGOA manuscript content and editorial state.
**Rule:** No canonical write happens without Wendell's conscious approval.
**Rule:** Files in `/home/workspace/manuscripts/` are working exports, verification surfaces, or derived artifacts unless explicitly marked otherwise.
**Rule:** If an agent drafts or rewrites text outside Obsidian without approval, that text is a proposal, not canon.

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

Each chapter lives at:
`chapters/ch[N]-[FACE]/CHAPTER[N]_[FACE]_FULL_DRAFT_MASTER.md`

These chapter files are the current workspace export surface. Do not treat them as co-equal canon with Obsidian.

## Companion Files

- `SPEC.md` in each chapter folder — read before editing
- `MTGOA_BOOK_WORK_TRACKER.md` — updated after every session
- `07 Book OS/SPEC_BOOK_EDITING_PROCESS.md` — this spec (in Obsidian)

## EA Standards

Every move in the book:
**[DISSATISFACTION → SATISFACTION] Transcend [X] — Emotion Name → Alchemical Outcome**

Energy economy (+2/+1/-1) — context for writer only, NOT in book content.
