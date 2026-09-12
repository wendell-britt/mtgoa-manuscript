---
type: decision
title: "Two rulings — the paperback lists at $40, and the course code goes in the book"
aliases:
  - paperback price
  - course code
  - oq-1
tags:
  - product
  - mtgoa
  - pricing
  - funnel
created: 2026-09-12
review: 2026-09-19
source:
  - specs/SPEC_PDF_2.0_2026-08-31.md
  - specs/SPEC_BOOK_PAGE_2026-09-08.md
  - marketing/ANALYSIS_BACKER_OBLIGATIONS_2026-08-24.md
  - marketing/DECISION_FUNNEL_2026-09-01.md
---

# Two rulings, 2026-09-12

**Wendell:** *"Paperback list price is $40. Print and kindle will have a code in the book
for the course."*

---

## 1 · The paperback lists at $40 — OQ-1 closed

KDP pays 60% of list minus the printing cost. At $40 against the confirmed $5.60 print cost
that is **$18.40 a copy**, against $12.40 at the $30 list the spec carried as provisional.

**It also holds the Kindle where it was put.** The 70% royalty tier requires the ebook list
sit at least 20% below the print list. Twenty percent below $40 is $32, so $9.99 clears it
with room, and the gap between the two editions is now fourfold — which is the property the
spec wanted from the Kindle in the first place: the cheap way in rather than the real
product.

### A correction to a number given in chat on 2026-09-08

**I said a 500-copy run at $40 returns $9,200. That treats all 500 as Amazon sales and it
is wrong.**

`ANALYSIS_BACKER_OBLIGATIONS_2026-08-24` puts the obligation at **247 printed books owed to
Kickstarter backers**, fulfilled with author copies at cost rather than sold. So a 500-copy
run is 247 obligations and **253 sellable copies**.

| | |
|---|---|
| 253 sellable copies at $40 on Amazon | **$4,655.20** |
| 247 backer copies at $5.60 author cost | **$1,383.20** plus shipping |

**The run size is not settled by this ruling and should be argued against 247 rather than
500.** `ANALYSIS_BACKER_OBLIGATIONS` already says so: *"a run of 500 covers the 247 I owe
and leaves stock to sell."*

### Where the $30 still stands

**The Gumroad floor is unchanged.** D-1 and D-2 are about the digital edition and this
ruling does not touch them.

---

## 2 · Print and Kindle carry a code — the entitlement gap closed

`SPEC_BOOK_PAGE` §5 named this as the one unsolved part of course access, because Amazon
does not say who bought. **The ruling takes the printed-code option over the manual claim
form.**

### It is one code per edition, not one per copy

**KDP does not print variable data.** Every copy of an edition carries the same string, so
the code is a shared secret from the moment one reader posts it. That is a property of the
decision rather than a defect in it, and it wants a deliberate answer on the `bars-engine`
side rather than a surprise later: **one redemption per account, and a rate limit.** The
grant itself already exists — `src/lib/book-access.ts` gates on `book-digital` via
`hasCapability`.

### It must not appear in the shareable PDF

**A code printed in the share PDF is public the first time somebody forwards the file**, and
forwarding is the whole design. The PDF reader does not need it: they reach the course
through `/book`, which is what that page is for.

So the code is a **print-and-Kindle** element, and that is a third target rather than a
second. `SPEC_CLOSING_SEQUENCE` §5 already asks for components that are share-only; this
asks for one that is everything-but-share.

### `back_matter/enrollment.md` is where it goes

That page is already on the spine, already titled "What Comes Next," and already
**print-only** under the 2026-09-08 ruling that moved the ladder to `/book`. Putting the
code there adds no component and needs no new spine entry — it only needs enrollment
restored to the Kindle target as well as print.

**One mechanism note.** `build_pdf.py` and `build_epub.py` both read the single intermediate
`typeset.py` resolves, so print, share PDF and EPUB currently share one spine. **Including a
component in two targets and excluding it from the third is a spine change**, not a
template variable.

### Two checks before the print run

**Repagination.** The print interior sits at 387 pages with a proof ordered against it.
Adding lines to enrollment reflows that page and may push the count. Build and compare
before committing to the run.

**The code has to exist first.** The string printed in the book cannot change afterwards,
so `bars-engine` needs to hold it before the interior is final — the same constraint that
governs the `/book` route, arriving earlier because print has a longer lead time than a web
page.

---

## 3 · What this leaves open

**OQ-2, fulfillment for direct print orders.** Untouched. At a $40 list the Amazon copy nets
$18.40, which is the number any direct-channel alternative now has to beat.

**Run size.** Argue it against 247.

**The `/book` path split**, and **per-chapter course links**, both still open in
`SPEC_BOOK_PAGE`.
