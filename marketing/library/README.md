---
type: index
title: "Marketing Library — extractions"
aliases:
  - marketing library
  - the library extractions
tags:
  - marketing
  - mtgoa
  - library
created: 2026-08-21
review: 2026-09-01
---

# Marketing Library — extractions

**Wendell, 2026-08-21:** *"put them in `marketing/library/` but only as markdown extractions."*

**Markdown only.** No PDFs, no EPUBs, no scans, no source files of any kind in this tree. One
`.md` per book, named `<AUTHOR-SURNAME>_<SHORT-TITLE>.md`.

**These are extractions, not reproductions.** Each file carries the strategy, the mechanism, and
the application — in our own words, with quotation held to the short passages that have to be
quoted to be discussed. A file that reads like a substitute for the book has failed at its job as
well as overstepping. **The test: could someone run the move from this file without needing the
book, and would they still be better off reading it?** Both answers should be yes.

**Written for the vault.** Frontmatter follows the convention `OPSBACKLOG.md` uses — `type`,
`title`, `aliases`, `tags`, `source`, `created`, `review` — so a file can be moved into
`The Library/` and behave like everything already there. The vault is not reachable from this
repo, so these are written here and carried across.

---

## What goes in each file

**The unit is a move, not a summary.** A summary tells you what the author thinks. We need what
to *do*, in a form that can be run against a 388-page book on allyship sold to a Green reader.

```markdown
---
type: extraction
title: "<Book Title>"
author: <Author>
aliases: []
tags: [marketing, mtgoa, library, <method-tag>]
source: <book, edition/year — or "reconstructed, not read" if so>
created: <date>
review: <date>
---

# <Book Title> — <Author>

**The one-line thesis.** What this book argues, in a sentence that survives being disagreed with.

**Why it is in this library.** The specific reason it applies to MTGOA rather than to marketing
in general.

## The moves

For each: **what it is** · **the mechanism** — why it works, not that it works ·
**applied to MTGOA** — the concrete version, named surfaces and named copy ·
**cost** — what it asks of you, in hours or in voice.

## What this collides with

**The part that earns the file.** Name the advice that dies against our constraints and say why,
rather than dropping it silently. Test every move against:

- `MTGOA_Copy_Strategy_Spec` §5 — the banned phrases, and the ban on any sentence that sounds
  like an apology
- `IDEAL_READER_MATRIX` — the *what loses her* column. Stacked CTAs that feel like a funnel,
  and pure armor, both lose the ICA
- **No Orange substrate** — optimisation/leverage framing is the Architect's material inside the
  book and is not the book's own ground
- **Hero and guide** — the reader is the hero. Copy that makes Wendell the hero is a defect
- The **371 backers** were promised roughly four broadcasts a year and no funnel. That promise is
  enforced in code (`list-contract.ts`), so any sequence-shaped tactic has to say who it is for

## What I could not check

Say plainly whether the book was read, skimmed, or reconstructed from secondary sources.
```

## The constraint that shapes everything here

**Most marketing advice is written for a reader who is not ours.** The ICA is Green, allergic to
hierarchy, and trained by nine chapters of this book to spot a move being made on her. So the
useful output of this library is often *this technique, minus the part that would work on someone
else* — and that subtraction is the finding, not a caveat on it.

The prior art already in `marketing/`:
`ANALYSIS_SALES_PAGE_2026-08-13.md` did this against Gumroad and book-description research, and
its §2 — the four things the draft already did better than most pages — is the shape to aim for.

## Status

**Empty, awaiting the book list.** Destination and format are ruled; the titles have not arrived
yet. When they do, one file per book, then a synthesis file if the moves start to overlap.
