---
type: gap
title: "Why the review passes prose Wendell then catches by eye"
aliases:
  - review gap
  - instrument gap
  - why the skills miss it
tags:
  - instruments
  - review
  - process
created: 2026-08-29
review: 2026-09-05
source:
  - instruments/review.py
  - instruments/fragment.py
  - instruments/antecedent.py
  - instruments/slop_shapes.py
  - marketing/KDP_LISTING_2026-08-29.md
---

# Why the review passes prose Wendell then catches by eye

**Wendell, 2026-08-29:** *"how are our skills not catching this? Make a note that we need to
solve for this."* Then: *"wire those four instruments into review.py."*

**Both are done. This is the diagnosis, the three places the first version of it was wrong,
and what shipped.**

---

## The finding

**The KDP description went through the review, came back `clean`, and he then found six
defects in it by reading.** Instruments existed for four of the six. **None of them could
read a draft** — `fragment.py` and `antecedent.py` had no FILE branch and scanned the
printed book whatever you passed them; `notstack.py` had no argument handling at all.

## Corrected — three things the first version of this note got wrong

**These matter more than the original finding, because two of them were flattering.**

**1 · `fragment.py` would not have caught his fragments, even wired in.** Run against
*"The meeting where somebody gets talked over. The decision that lands on whoever can least
afford it."* it returned **zero**, and correctly on its own terms. It flags a string in
which no token is ever a verb anywhere in the book, and every one of those has a good verb
— `gets`, `lands`, `stops` — sitting inside a relative clause. **So the file existed and
the defect was outside its design**, which is a worse finding than a missing call site and I
recorded the better-sounding one.

**2 · `faux_insight.py` is not an instrument.** It is a spent one-shot edit script: four
hardcoded before/after strings from 2026-08-03, already applied, that rewrite the manuscript
when run. **Wiring it into a review would edit the book during a check.** Listing it as one
of four instruments to wire in was a filename read as a capability.

**3 · `empty_head.py` did catch *"the noise of doing the work."*** It was SOFT site 2 of 8,
and `review.py` printed the number **8** over it. My claim that its list had no entry for
`work` was wrong — `work` is in its SOFT tier and has been since it was written. I was
looking at `prose_diet.py`'s `EMPTY` list, which is a different list in a different file.

**That third one is the most useful thing in this document.** The instrument fired, the
review printed a count, and the count is a number nobody reads. **A finding rendered as a
digit is a finding that did not happen.**

## What shipped

| step | what it does | measured |
|---|---|---|
| **`draft_lines.py`** | reads any file into the record shape the instruments expect, stripping YAML front matter, code fences and commentary headers | new |
| **`fragment.py` 3a** | FILE mode, plus a second tier for the shape that actually ships — a headed noun phrase whose only verbs are inside a relative clause | catches all three fragments he rejected; the shipped copy stays clean |
| **`antecedent.py` 3b** | FILE mode, plus an exclusion for relative `that` between a noun and a verb | book board 202 → 194, all eight relative clauses that were never findings |
| **`slop_shapes.py` 3c** | ten `/no-ai-slop` patterns that are a vocabulary list or a fixed shape, so step 3 stops being honour-system. Absorbs `notstack.py`'s pattern by import | catches *"the training nobody gets"*; 44 sites book-wide |
| **`empty_head.py` 7** | draft path now passes `--sites`, so SOFT prints its hits instead of its count | surfaces *"the noise of doing the work"* |
| **`empty_head.py`** | `-v` no longer crashes it — a single-dash flag was being read as a path | bug |

**The measure that matters.** Run against the version he rejected, the pass now fails three
steps and names, by line, **five of the six defects he found by reading**:

```
  7 head    old_kdp.md   0  0  8      SOFT … the noise of doing the work
  3a frag   old_kdp.md   MID 3  NEG 1     The meeting where somebody gets talked over.
  3b pron   old_kdp.md   orphan 1         This is a field guide.
  3c slop   old_kdp.md   FAUXINSIGHT:1    the training nobody
```

**The sixth is still uncaught**, and it is the one no instrument here will get:
*"the meeting where the same person absorbs it again."* `antecedent.py` clears it because
that paragraph is full of nouns, and the defect is that **none of them is the person**. That
needs a reader who asks *which person*, which is his question and stays his.

## Two design decisions worth carrying

**The second fragment tier is draft-only, and that is measured rather than cautious.**
Book-wide it takes the board from 115 candidates to 296. A board nobody reads is worse than
a smaller one that gets worked. On a 500-word draft the asymmetry inverts — a false positive
costs one glance and a false negative ships — so `--deep` opts the book in deliberately and
the draft path has it on.

**SOFT means opposite things in the two modes, and `empty_head.py` said so first.** Its own
docstring: *"`the work` is canon in the manuscript and suspicious in a line I added ten
minutes ago."* Book-wide, 283 legitimate sites. On a draft, the tier that catches a filler
noun a repair pass just reached for. **The instrument had the analysis and the caller had
one output for both.**

## What is still open

**1 · `slop_shapes.py`'s `BINARY` rule fires on the book's own constraint.** *Ranking rather
than denying* produces a two-part contrast on purpose, which is 30 of the 44 book-wide sites.
It reports rather than gates, so the decision is recorded rather than skipped — but the rule
will never be more than a candidate finder and should not be promoted.

**2 · Colon reveals and em dashes are unchecked here on purpose.** Colons introduce every
list and every gloss in this book, so the rule would fire hundreds of times on correct prose.
Em dashes have `emdash.py` and a ratcheting budget already.

**3 · The reading is still the reading.** Steps 3a–3c run the vocabulary and the fixed
shapes. Beat-or-claim, real-or-manufactured, and *which person* are not mechanical, and
`review.py` now says so where it used to say *"run /no-ai-slop by hand."* **The goal was
never to replace his eye. It was to stop spending it on the four patterns a regex can find.**
