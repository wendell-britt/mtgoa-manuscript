---
type: retro
title: "What it took to fix one chapter, and what carries to the next eight"
aliases:
  - ch4 retro
  - proof pass retro
tags:
  - process
  - review
  - ch4
created: 2026-09-16
source:
  - specs/PROOF_MARKS_CH4_2026-09-15.md
  - specs/GAP_INSTRUMENT_DEFECTS_2026-09-15.md
  - .claude/skills/mtgoa-review/SKILL.md
---

# The ch4 proof pass

## Where it started

Wendell asked for the most recent build. There was none — `build/` is gitignored and the newest
committed artefact was a review-only markdown surface from 2026-05-29. Built fresh, then asked
whether it had been through editorial review, **I answered with the boards: `SHIPPABLE`, every
drawdown at `unresolved=0`, `CLAIMS PASS`, `COHERENCE PASS`.**

He then read 33 pages on paper and marked roughly 190 spans.

**That gap is the whole retro.** The boards were not lying. They were answering a narrower
question than the one asked, in language that did not say so.

## What actually found things

| finder | real defects |
|---|---|
| Wendell, on paper, with a highlighter | all of them |
| the boards | none |
| me, unprompted | none |

Every instrument gap in `GAP_INSTRUMENT_DEFECTS` was found *after* he handed me a marked page.
Four sweep-damage mechanisms, the blockquote filter hiding 7,446 words, `dupes.py` never
comparing across files, two `trailing_and` recall bugs, `fragment.py` flagging complete
sentences — none of it surfaced on its own, and I had the same repo access the entire time.

## The four things that cost the most

**1. Reading a board as a fact about the book.** `trailing_and 0` is true about 93% of the text.
No line in `review.py` prints its denominator.

**2. Sweeps applied without reading the result.** The telling drawdown changed 491 lines across
nine chapters with no recorded read. It deleted an antecedent two sentences downstream needed,
rewrote one shared sentence two different ways in different chapters, stripped nouns and orphaned
the payoff that named them, and split a passive sentence into two passive sentences. Each edit
followed a correct rule.

**3. Closing a board by acceptance and calling it review.** `fragment 54 -> 0 (1 rewritten, rest
ledgered)` renders identically to `light_verb 52 -> 0 (51 rewritten)`.

**4. My own corrections, twice on one word.** On `spend` I first argued the book's economics were
incoherent — they are not, and Wendell said so — then proposed `spending yourself` as the fix for
`spending a line`, which was the exact defect he had just named. **Two wrong confident answers
before the right one.** The rule now lives in a note so it does not need a third.

## What compounds, and what does not

**Compounds:**
- the ten named patterns, now in `mtgoa-review` §6, checked at generation rather than at proof
- the three rules with tests: person-as-commodity, unearned intimacy, `the clean no`
- `build_markup.py` — one chapter, stable page numbers across rebuilds
- knowing which four boards lie, and how

**Does not compound:** the reading. Every site still needs a judgment, and the judgment is the
work. ~190 marks resolved to 47 applied edits in ch4; the other 140 were read and kept, or were
already fixed, or were my own false positives.

## The inventory for the remaining eight chapters

Raw candidates, before reading. ch4's residual numbers calibrate the noise: it shows 15 stamps
and 11 tack-ons *after* cleaning, because those survived a read.

| pattern | book-wide | ch4 share |
|---|---:|---:|
| verdict stamps | 81 | 19% |
| trailing-and tack-ons | 110 | 10% |
| negation-opening fragments | 26 | 27% |
| real-insistence | 50 | 22% |
| subject-dropped fragments | 23 | 4% |
| unearned intimacy | 61 | 7% |
| `run`/`land` | 433 raw | 11% |
| person-as-commodity | 2 | 0% (ch4 clear) |
| `Not because A. Because B.` | **0** | cleared book-wide 2026-09-16 |

**Roughly half of any raw count is legitimate.** A sweep against these numbers would repeat 2026-09.

## The method that worked

Wendell set it, and it is the only part worth copying:

> take as input the lines I'm marking · identify the pattern · isolate the problematic lines ·
> rewrite them · put them in front of me · then change them, rereading to make sure we don't
> break the logic

**The approval gate is load-bearing.** He overruled me on four of my own judgment calls —
a fragment chain I said was building, a keep on `ch4:172`, the `spend` economics, and `spending
yourself`. Each would have shipped.

**The gates are load-bearing too, in the one job they are good at.** They caught five of my own
regressions: an em-dash over budget, a comma that manufactured a trailing-and, three copula
labels I wrote while removing verdict stamps, a deleted claim carrier, and a second comma doing
the same thing in ch5. **Not one of them told me what to cut. All of them caught what I broke.**

That is the division of labour: **reading finds the defect, instruments catch the regression.**
Running it the other way round is what produced the book we started with.
