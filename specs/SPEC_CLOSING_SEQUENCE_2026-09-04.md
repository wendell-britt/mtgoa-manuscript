---
type: spec
title: "The last page — where FR-5 goes, and why the ladder leaves the book"
aliases:
  - closing sequence
  - enrollment collision
  - fr-5 placement
tags:
  - product
  - mtgoa
  - pdf
  - back-matter
created: 2026-09-04
updated: 2026-09-08
review: 2026-09-15
source:
  - specs/SPEC_PDF_2.0_2026-08-31.md
  - marketing/PDF_BLOCKS_2026-09-01.md
  - marketing/DECISION_FUNNEL_2026-09-01.md
  - specs/SPEC_BOOK_PAGE_2026-09-08.md
  - back_matter/enrollment.md
  - instruments/build_book.py
---

# The last page

**The prose for FR-5 is written and gated. Where it goes was not decided, and the first
version of this spec got the answer wrong.** Wendell ruled on 2026-09-08; §5 carries the
ruling and §6 carries what it replaced.

---

## 1 · FR-5's own placement instruction does not fit this book

`SPEC_PDF_2.0` puts the closing ask at *"the final content pages, before any appendix."*

**This book's spine runs front matter, chapters, appendices A–H, then back matter** —
Kickstarter backers, About the Author, the enrollment page, Key Terms, the index. Following
the instruction literally would seat the ask ahead of eight appendices, a glossary and an
index, so a reader would meet it roughly sixty pages before the end and finish the book on
an index entry.

**The instruction was written for a book whose appendices come last. This one's do not.**
The ask belongs in the back matter.

**This finding survives the 2026-09-08 ruling unchanged.** It is the only one that does.

---

## 2 · What sat next to it, and why that looked like a problem

`back_matter/enrollment.md` — "What Comes Next" — offers coaching, speaking, the deck and
*Igniting Joy*, and closes by sending the reader to `masteringallyship.com`. It ships in
both editions today.

Three defects follow from putting FR-5 beside it:

**Order.** Enrollment first means the reader closes 387 pages, meets four paid offers, and
is then told there is something free. That is selling ahead of giving.

**A wrong address in the PDF.** Enrollment's closer sends the reader to the page that sells
the book. In print that is correct. In the PDF it is the offer `DECISION_FUNNEL` ruled
against — *a person holding the PDF already has the book.*

**Two terminal lines.** Both pages end on a closer written to be last. Back to back, in
either order, one of them stops closing.

---

## 3 · The ruling — the ladder is not the book's job

**Wendell, 2026-09-08, on the merged page this spec first proposed:** *"your solution is
wack, but the problem is fine. This is the point of the /book page."*

**The book's closing page carries one move: go to `/book`.** Coaching, speaking, the deck
and *Igniting Joy* live on that page, not inside the file. See
`specs/SPEC_BOOK_PAGE_2026-09-08.md`.

### Why the ladder cannot stay in the file

**Anything set in 387 pages is frozen.** Rates change, availability changes, the deck runs
out or gets reprinted, *Igniting Joy* gets a second edition. A ladder printed inside a file
that keeps getting forwarded for years is a ladder nobody can correct. A ladder on `/book`
changes once and every copy ever sent to anyone picks up the change.

**This is FR-7's own reasoning applied to content instead of destination.** FR-7 requires
the printed URL be a redirect under Wendell's control, because the file is permanent and the
destination must not be. The offers behind that URL are permanent in exactly the same way
and want the same treatment.

---

## 4 · What the ruling settles

| defect from §2 | status |
|---|---|
| order — paid offers ahead of the free one | **gone.** No paid offers in the PDF's closing page at all. |
| enrollment's address is wrong in the PDF | **gone.** `enrollment.md` is not in the PDF, so its store link is only ever read in print, where it is correct. |
| two terminal lines | **gone.** One closing page per edition. |

**No new prose is required.** FR-5 as drafted already ends on `/book`; nothing in it has to
be rewritten to carry a ladder it no longer carries.

---

## 5 · The shape

**PDF edition:** FR-5 alone, seated in the back matter. `enrollment.md` off the share spine.

**Print edition:** `enrollment.md` alone, where it is now — after About the Author, before
Key Terms. Unchanged.

**The build already forks.** `PDF_BLOCKS_2026-09-01` records that FR-4 and FR-5 belong on
the share path and not in the print interior — *"if somebody handed you this file"* is false
in a paperback. This adds one exclusion to that same fork rather than inventing a mechanism.

**Exact spine work, both to be made against `instruments/build_book.py`:**

1. FR-4 and FR-5 become components on the share path only.
2. `("back", "Enrollment page", "back_matter/enrollment.md", GAP)` becomes print-only.

**Neither is made yet, and both repaginate the edition they touch.** The print interior sits
at 387 pages with a proof ordered against it, so the print spine must come out of this
unchanged — which it does, since every change above lands on the share path.

---

## 6 · The rejected alternative, and why it was wrong

**Rejected 2026-09-08: one merged closing component on the share path** — course, then the
free ways in, then the ladder, then a single closer.

It resolved the same three defects and cost more to get there: new customer-facing prose
through the full review pass, a shortened ladder written to survive following the course,
and every one of those offers frozen into the file at the moment of the build. **It solved
in print a problem a web page solves permanently.** Recorded because it was this spec's
recommendation for four days and anyone reading the commit history will find it.

---

## 7 · What this does not settle

**The print edition's own closing sequence is untouched here.**

**Per-chapter course links** remain the open question `DECISION_FUNNEL` names. A link per
chapter changes the closing page's job and would reopen this.
