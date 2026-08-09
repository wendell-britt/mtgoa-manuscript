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

## Showing the work (standing rule, 2026-07-29)

**Paste every prose change into the console, before and after, in the reply that
makes it.** Wendell reviews in the conversation, not by opening files or reading
diffs. A change he cannot see in the console has not been shown to him.

- Quote the **old text and the new text**, in full, for every line touched. Not
  a summary of the change, not a file path and line number, not "updated ch5's
  opener."
- For a batch, use a table or a per-site before/after block. Group by chapter.
- Drafts for review go in the console **and nowhere else** — do not write them
  into `manuscript/` and ask him to look. Apply only what he has approved.
- Counters and test output still get reported, but they do not replace the
  prose. `BLOCK 39 -> 38` says nothing about whether the sentence is any good.

## Editing Protocol

When asked to edit, run the WAVE Editing Spiral:
**Full spec:** `The-Library/The Library/07 Book OS/SPEC_BOOK_EDITING_PROCESS.md`

**Practice:** The 321 somatic practice is author-led and optional. Do not access
or require the Zo surface as an automated precondition for analysis, planning,
drafting, review, or canonical edits. It never blocks editorial work. Wendell may
choose to do a somatic practice independently or request one explicitly.
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
**Alchemy N — Emotion Name → Alchemical Outcome**

**DEPRECATED — do not write the bracketed tag.** This line used to read
`**[DISSATISFACTION → SATISFACTION] Transcend [X] — …**` and that bracket is a
production tag, not a chapter voice. It was deprecated 2026-06-03, and it has
come back into the book twice since, because **this instruction is where it is
generated from.** The verb also changed: the book says *Alchemy 1* / *Alchemy 2*
and the word *Transcend* appears nowhere in the body.

`instruments/gate.py` now hard-fails on any `[ALLCAPS]` tag in `manuscript/`, so
a move written to the old pattern cannot ship. See
`specs/SPEC_BRACKET_TAGS_2026-07-29.md` for the full history.

Energy economy (+2/+1/-1) — context for writer only, NOT in book content.
