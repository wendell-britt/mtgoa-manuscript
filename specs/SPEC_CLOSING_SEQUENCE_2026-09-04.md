---
type: spec
title: "The last page — where FR-5 goes, and what it does to the enrollment page"
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
review: 2026-09-11
source:
  - specs/SPEC_PDF_2.0_2026-08-31.md
  - marketing/PDF_BLOCKS_2026-09-01.md
  - marketing/DECISION_FUNNEL_2026-09-01.md
  - back_matter/enrollment.md
  - instruments/build_book.py
---

# The last page

**The prose for FR-5 is written and gated. Where it goes is not decided, and the obvious
answer is wrong twice over.** This spec covers the placement and the one defect it exposes
in a page that already ships.

---

## 1 · FR-5's own placement instruction does not fit this book

`SPEC_PDF_2.0` puts the closing ask at *"the final content pages, before any appendix."*

**This book's spine runs front matter, chapters, appendices A–H, then back matter** —
Kickstarter backers, About the Author, the enrollment page, Key Terms, the index. Following
the instruction literally would seat the ask ahead of eight appendices, a glossary and an
index, so a reader would meet it roughly sixty pages before the end and finish the book on
an index entry.

**The instruction was written for a book whose appendices come last. This one's do not.**
The ask belongs in the back matter, which puts it next to `back_matter/enrollment.md`.

---

## 2 · The collision, stated accurately

**They are not redundant, and the first version of this finding said they were.** The two
pages make different offers:

| | `enrollment.md` | FR-5 |
|---|---|---|
| what it offers | coaching, speaking, the deck, *Igniting Joy* | the thirty-day course |
| what it costs | money, all of it | nothing, or what the book turned out to be worth |
| who it is for | a reader who wants more than the book | a reader who wants to run what the book gave them |
| where it ships | print and PDF | PDF only |

**The problem is order.** Enrollment first means the reader closes 387 pages, meets four
paid offers, and is then told there is something free. That is the pitch ahead of the gift,
and it is the sequence most likely to leave a buyer feeling worked — which is `EC-5`
arriving from a direction `FR-4`'s two-branch framing does not guard, because FR-4 guards
against being asked twice for money and this is being sold to before being given to.

**Reversed, it reads as the architecture Wendell described.** A person holding the PDF
already has the book; the course is the offer they do not have. Give that first, then the
ladder for anyone who wants more.

---

## 3 · A defect in a page that already ships

`enrollment.md` closes on:

> **masteringallyship.com.** All of it lives here.

**In the print book that is correct.** In the PDF edition it sends a reader holding the book
to the page that sells the book — precisely the wrong offer `DECISION_FUNNEL_2026-09-01`
was written to prevent, and by his own reasoning there: *selling them the book is the wrong
offer; the course is the one offer you have that they do not.*

**So enrollment already needs to differ between the two builds**, independently of anything
FR-5 does. The PDF reader's address is `/book`.

---

## 4 · Two terminal lines, and only one last position

Both pages end on a closer that is written to be last.

> *…because you just spent a whole book learning to spot that move when somebody else makes
> it.* — enrollment

> *Pass it on. That was always the plan.* — FR-5

**Whichever runs second keeps its landing and the other one loses it.** This is not a
sequencing preference that can be deferred; putting them back to back in either order
damages one of them.

---

## 5 · The recommendation

**One merged component on the share path. `enrollment.md` unchanged on the print path.**

The arc, in order:

1. **The course.** What the reader already has, named as something received.
2. **The free ways in.** Signup, review, forward — FR-6 and P-5, and the signup is the
   strongest of the three.
3. **The ladder.** Coaching, speaking, the deck, *Igniting Joy* — enrollment's material,
   kept, and now arriving after the gift rather than before it.
4. **One closer.** *Pass it on.*

**This gives the gift before the ask, keeps every paid offer, and leaves one terminal line
instead of two.** It also resolves §3 by construction: the merged page carries `/book`, and
the print page keeps the bare domain.

**The build shape already exists.** `PDF_BLOCKS_2026-09-01` records that both blocks belong
on the share fork and not in the print interior — *"if somebody handed you this file"* is
false in a paperback. A spine that differs between the two builds is therefore already
required; this adds one component to that difference rather than inventing the mechanism.

### What it costs

**New customer-facing prose, through the full review pass.** The merged page is not a
paste of two existing texts — the ladder has to be shortened to survive following the
course, and enrollment's closer has to go. That is Wendell's voice and his call, and it is
the reason this spec stops here rather than shipping a draft.

### The cheaper alternative, argued fairly

**Drop `enrollment.md` from the share build and let FR-5 stand alone.** No merge, no new
prose, one page, and §3 and §4 both dissolve because only one page is present.

**The case against it is revenue.** Coaching, speaking, the deck and *Igniting Joy* would
appear nowhere in the PDF edition, and the PDF reader is the most engaged reader in the
catalogue — the one who chose to pay above a floor when a $9.99 Kindle existed. Removing
the ladder from the edition whose readers are most likely to climb it is the wrong
economy. **Recorded because it is genuinely cheaper and the choice is his, not mine.**

---

## 6 · What this does not settle

**The print edition's own closing sequence is untouched here.** Enrollment stays where it
is, after About the Author and before Key Terms, and nothing in this spec argues with that.

**Per-chapter course links** remain the open question `DECISION_FUNNEL` names. If the
campaign template gets a link per chapter, the closing page's job changes and this
sequencing should be revisited rather than assumed to survive.
