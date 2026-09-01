---
type: checklist
title: "The physical proof — what to check when the box lands"
aliases:
  - proof checklist
  - physical proof
  - when the proof arrives
tags:
  - print
  - mtgoa
  - kdp
  - production
created: 2026-08-29
review: 2026-09-12
source:
  - instruments/book/design.typ
  - marketing/DECISION_ISBN_2026-08-29.md
  - specs/SPEC_PRINT_READINESS_2026-07-29.md
---

# The physical proof — what to check when the box lands

**Wendell, 2026-08-29:** *"got those proofs being sent to me."*

**`SPEC_FINAL_PROOF_2026-08-07.md` is the editorial deep read of the text. This is not that.**
This is the pass only a physical copy can run — what a PDF is structurally unable to
tell you, checked in the order that decides whether you reprint.

**Do it in one sitting, with a pencil, in daylight.** Screen light flattens ink density and
warm indoor light hides a colour cast on the cover.

---

## The numbers this book was built to, so you know what you are looking at

| | |
|---|---|
| trim | **6 × 9 in**, US trade paperback |
| pages | **387** |
| inside margin | **0.95 in** — KDP requires **0.625 in** at 301–500 pages, so there is **0.325 in of headroom** |
| outside · top · bottom | 0.70 · 0.85 · 0.90 in |
| body | justified, hyphenation on, `runt` cost raised to 400% |
| components | **28**, front matter through the index |

**The margin headroom is the most reassuring number here.** The single most common reason a
proof comes back wrong is a gutter that swallows text at high page counts, and this interior
was set half an inch wider than the minimum on purpose. **Check it anyway** — the point of a
proof is that computed and printed are different claims.

## Pass 1 · Before you open it — two minutes, and it is the one that costs money

**1 · The spine.** Hold it closed and look straight down the spine. **The title should be
centred in the spine panel**, not creeping onto the front or back face. A wrap built to the
right page count and then printed with normal bindery drift is the failure mode, and it is
**invisible in the PDF because the PDF does not have a fold.**

**2 · Which paper did you get.** Cream or white. Note it, because **it changes the spine
width** — cream is thicker — and the wrap has to match the one you actually ship. If you
ordered before deciding, this is where you find out.

**3 · The cover, in daylight.** Colour against what you designed, and glossy versus matte
against what you chose. Matte shows fingerprints; gloss shows every scuff in shipping.

**4 · Squareness.** Set it on a flat surface. A visible lean or a cover that will not sit
flat is a binding fault, not a design fault, and it is worth reordering a proof to see
whether it repeats before you conclude anything.

## Pass 2 · The gutter, and this is where 387 pages bites

**Open the book flat at page 200 — the deepest part of the block — and push it open.**

- **Can you read the last word of every line on the left page** without cracking the spine?
- **Can you read the first word of every line on the right page?**
- **Does the running head or folio disappear into the fold** on any spread?

**Perfect binding at 387 pages does not open flat**, and that is normal. What you are testing
is whether *reading* requires force. If it does at 0.95 in, the fix is not the margin — it is
the page count or the paper.

**Then run the same three checks at page 40 and page 350.** The gutter behaves differently
at the ends of the block than in the middle, and a proof read only in the middle misses it.

## Pass 3 · Ink, paper and show-through

**Hold a text page up against a lamp.** How much of the reverse side reads through? Some is
normal on KDP's stock. **Enough to distract while reading is a paper decision** — cream is
usually kinder here than white, which is a second reason to note which you got.

**Compare a heavy page against a light one.** Find a page of solid prose and a page with a
table or an apparatus frame, and look at whether the black is the same black. **Uneven
density across a spread** is a press issue worth a reorder before you conclude it is the file.

**The five apparatus frames each have a hairline rule at 0.4pt.** `MARGINALIA`,
`EPIGRAPH-BYLINE`, `POSTCARD`, `HANDBOOK`, `SIGNATURE`. **A 0.4pt rule at 140 grey is the
finest mark in the book and the first one a press drops.** Find one of each and check
the rule actually printed, and printed as grey rather than black.

**One risk that does not apply here, so you can stop looking for it.** Marginalia in this
design are **inline indented blocks with a left rule**, not notes set in the outer margin. So
there is nothing sitting near the trim edge that a 1/8 in cutting drift could clip. That is
the usual disaster with a marginalia-heavy book and this design does not have it.

## Pass 4 · Structure — mostly already checked, so do not spend the proof on it

**Three of the four structural checks are run by the build and you would be redoing them by
hand.** `build_pdf.py` reads a verification record the template writes into the document and
confirms **every chapter and appendix opened on a recto**, that **the copyright page landed
on a verso** where it backs the title page, and that **the folio sequence is unbroken** —
roman through the front matter, arabic from Chapter 1. Every component except the half title and the
copyright page forces a recto in the template, and those two are deliberate exceptions.

**So spot-check, do not audit.** Thumb to three openers — Chapter 1, Chapter 7, Appendix A —
and confirm each is on a right-hand page. **You are testing that the printed object matches
the verified PDF**, not re-deriving the verification. If those three are right, the rest are.

**Two structural faults the build cannot see, and these are worth real attention:**

**Blanks must be truly blank.** The template suppresses the running head and folio on every
leaf it inserts to reach a recto, and a press or a converter can put them back. **Find two
blanks and look at them properly** — a folio on a blank page is a printing error repeated
throughout the book.

**The index, on three entries.** Pick three at random, turn to the page, confirm the term is
actually there. `xref.py` verifies references against the source; **nothing verifies them
against the printed page numbers**, and the index is the one component whose correctness only
exists in the final pagination.

## Pass 5 · Typography — read four pages properly, not four hundred

**The body is justified with hyphenation on, at roughly a 4.35 in measure.** That combination
produces exactly three defects, and all three are visible only on paper:

- **Stacked hyphens.** Three or more consecutive lines ending in a hyphen. Two is fine, three
  is a ladder the eye trips on.
- **Rivers.** Squint at a full page of prose until the words blur. **White channels running
  down through the block** are what you are looking for; they only appear when you stop
  reading the words.
- **A widow or an orphan** — one line of a paragraph alone at the top or bottom of a page.

**One of these is already handled and you should confirm the fix took.** The `runt` cost is
raised to 400% because the last proofread found **three paragraphs closing on the back half
of a hyphenated word** — *situ-* / *ation.* alone under a full page of argument. **Look for
that specific shape.** If it is gone, the fix worked.

**Where to read.** The first spread of Chapter 1, one dense spread in the middle of Chapter 7,
one page with a table, and the last spread of Chapter 9. Four spreads finds nearly everything
typographic; reading all 387 finds the same defects an hour later.

## Pass 6 · What you can only judge holding it

**None of these has a right answer, and the proof is the only way to have the conversation.**

- **Does it feel like a book you would pick up**, at 387 pages and this thickness?
- **Is the body type big enough** for the reader described in `IDEAL_READER_MATRIX` — someone
  exhausted, reading at the end of a day, possibly over forty?
- **Do the chapter openers look like the book the cover promises?**
- **Where does it fall open on its own?** A perfect-bound book has a natural opening, and if
  it is the middle of Chapter 5, that spread had better hold up.

## What to do with what you find

| what you found | what it means |
|---|---|
| spine title off-centre | **wrap or bindery.** Reorder one proof before touching the file — drift repeats or it does not |
| text lost in the gutter | margin or page count. The file change is real work, so measure before deciding |
| a hairline rule missing | press, almost certainly. Check the same frame elsewhere in the book before changing the design |
| stacked hyphens or a river | a `costs` adjustment in `design.typ` and a rebuild. Cheap |
| an opener on a verso | a build bug. Cheap to fix, embarrassing to ship |
| an index entry pointing at the wrong page | a build bug, and it means the index was built against a stale pagination |
| show-through | paper. Cream, or nothing |

**Any fault in the file means a rebuild and a new proof.** Budget for that — the first proof is
rarely the last one, and ordering a second is much cheaper than shipping 247 wrong ones.

## The one page this proof cannot check

**The copyright page has no ISBN**, by the decision recorded at
`SPEC_PRINT_READINESS_2026-07-29.md` B3, and the proof prints *Not For Resale* regardless.
**So the proof cannot check the line that will be on the backer edition.** When the Bowker
ISBN is bought, the copyright page gets edited, the book gets rebuilt, and **that page in
particular wants looking at again** — it is the one page in the book that will be different
from the copy in your hands.
