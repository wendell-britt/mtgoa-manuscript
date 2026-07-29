# SPEC — The Register Problem

**2026-07-29. Book-wide. Opened because it kept being filed as somebody's prose
instead of as a defect.**

## 1 · The problem, measured

The manuscript builds sentences as **X is Y** at roughly twice the rate of any
comparison text, including Wendell's own previous book.

| | MTGOA | *Igniting Joy* | Elliott | Chou |
|---|---|---|---|---|
| copula /1k | **61.4** | 28.8 | 40.9 | 41.1 |
| sentences ≤6 words | **19.4%** | 4.2% | 12.4% | 12.8% |
| mean sentence length | 16.0 | 18.8 | 23.7 | 22.5 |
| hedges /1k | 2.3 | 2.8 | 12.2 | 5.9 |

**6,056 copulas.** Note the manuscript is above Elliott and Chou too, so this is
not an artifact of comparing against one book.

`SPEC_REPETITION_AND_CUTS` established the direction in June and named the
short-declarative register **drift rather than voice**, with the reason it stays
invisible: *"Calling it yours converts a defect into an asset and protects it
from the pass that should be removing it."* Two months later the copula has
moved 62.8 → 61.4. **Hedging was fixed in that window and this was not**, which
is the evidence that it is being protected rather than worked on.

### Per chapter

| ch | copula /1k | ×IJ | ≤6 words | copulas | to reach IJ |
|---|---|---|---|---|---|
| 1 | 50.2 | 1.74× | 13.1% | 378 | 162 |
| 2 | 52.6 | 1.83× | 17.1% | 378 | 172 |
| 3 | 61.1 | 2.12× | 16.4% | 932 | 493 |
| 4 | 62.8 | 2.18× | 25.8% | 709 | 385 |
| 5 | 54.9 | 1.91× | 18.9% | 494 | 235 |
| 6 | 64.3 | 2.23× | 21.0% | 640 | 354 |
| 7 | 64.2 | 2.23% | 13.7% | 823 | 455 |
| 8 | **68.5** | **2.38×** | 21.8% | 912 | **529** |
| 9 | 64.4 | 2.24× | 22.2% | 790 | 437 |
| | | | | **6,056** | **3,222** |

Heaviest: **ch8, ch9, ch6, ch7.** Lightest: ch1, ch2 — which are also the two
shortest and the two most recently rewritten.

## 2 · Why there is no cheap fix

The obvious hope is a high-yield subset. There isn't one. Decomposing all 6,056:

| pattern | count | share |
|---|---|---|
| expletive *It is / There is* opener | 144 | 2.4% |
| copula + article-nominalization | 122 | 2.0% |
| defining a named term (**licensed**) | 106 | 1.8% |
| copula inside a ≤6-word sentence | 490 | 8.1% |
| **ordinary `X is Y`, distributed** | **~5,200** | **86%** |

**86% are ordinary sentences with no marker.** Reaching *Igniting Joy* means
removing 3,222 of them.

### Tested, rather than asserted

An earlier draft of this spec said a register rewrite "cannot happen before
August 1." That was asserted without measurement, which is the same mistake the
finishing-pass spec made about W7 and had to withdraw. So it was tested.

**ch8 Section 2, 1,145 words, chosen for being representative** — 2.18×, against
a book average of 2.13×.

| | copula /1k | ×IJ | ≤6 words | mean | words |
|---|---|---|---|---|---|
| original | 62.9 | 2.18× | 17.9% | — | 1,145 |
| after pass 1 (14 edits) | 41.6 | **1.45×** | 25.0% | — | 1,105 |
| after pass 2 (4 rejoins) | 43.2 | **1.50×** | 20.3% | 15.8 | 1,110 |

**One pass moved a representative section from 2.18× to 1.50×** — past Elliott
and Chou, which sit at 1.42× and 1.43×. Two passes and about twenty minutes.

Three findings that change the plan:

- **Copula and short-sentence load trade against each other.** Pass 1 cut the
  copula by splitting sentences, and drove ≤6-word sentences from 17.9% to
  **25.0%** — swapping one register defect for the other, which is worse at
  4.62× the control. Pass 2 rejoined four of them and gave back 0.05× of copula
  to recover 4.7 points of short-sentence share. **Any register pass has to
  watch both numbers or it will report a win it did not get.**
- **Most of the yield came from frames, not from copulas as such.** *This is
  what happens when*, *what never gets named is*, *the trap is specific:*,
  *what's actually happening is*. Each carries a colon or a nominalization and
  none carries an action. They are findable and there are a lot of them.
- **The gate caught a banned word I wrote into the manuscript** — *"the people
  who have metabolized their pain go **quiet**"* — within one run. New prose is
  where the banned list earns its keep.

**Revised estimate.** Nine chapters, roughly 45 substantive sections. At two
passes per section this is real work and it is not impossible; it is a few days
of focused effort, which is more than remains before August 1 but far short of
"a second-edition project." The honest framing is a **priority order**, not a
verdict: ch8, ch9, ch6, ch7 first, and as far down the list as the calendar
allows.

## 3 · What ships for August 1

**S1 — the mechanically safe subsets.** 266 sites where the fix is determinate
rather than a judgment call:

- **144 expletive openers.** *It is / There is* fills the subject slot with a
  placeholder. Lanham's question resolves every one: who is kicking whom.
- **122 copula + nominalization.** Turn the noun back into a verb and the
  copula leaves with it — the three grammar moves are one problem.

Run through `instruments/prose_diet.py` and the four moves. Worth ~4.4% of the
total, which is honest and small.

**S2 — the section audit carries the rest.** Wendell's read-aloud pass is the
only instrument that can judge the other 86%, because *"X is Y"* is not a defect
in isolation — it is a defect in density. Per section, the question is not *is
this sentence wrong* but *how many sentences in a row have no verb in them.*

Give each section its `prose_diet` number before reading it. A section at 2.4×
should be read expecting the problem; one at 1.3× probably has other problems.

**S3 — ch8 first.** Heaviest at 2.38×, and 529 of the 3,222. If only one chapter
gets a register pass, it is this one.

## 4 · What does not ship

Full register conversion. `SPEC_REPETITION_AND_CUTS` already scoped the adjacent
piece of this — 464 restatement pairs, 67 true, worth ~810 words — and rated the
wider pass at 1,500–2,000 words of return. That work is real and it is second
edition, with this spec as its brief.

## 5 · The ruling this needs

**Is 2.13× acceptable for this book?**

The case that it is: this is a workbook. Short declaratives land instructions.
The reader is meant to stop and do something, not to be carried by a paragraph.
*Igniting Joy* is a different genre and Elliott and Chou are trade nonfiction.

The case that it is not: the manuscript is above **all three**, not just the
one; 19.4% of sentences at six words or fewer is 4.6× the control; and the June
spec already ruled the register a drift the manuscript fell into rather than a
choice anyone made.

**This is Wendell's call and nobody else's.** Everything in §3 is worth doing
either way, since expletives and zombie nouns are defects at any register. What
the ruling decides is whether §4 becomes second-edition work or gets dropped.

## 6 · How this gets checked

```
python3 instruments/prose_diet.py            # per chapter against Igniting Joy
python3 instruments/prose_diet.py -v         # quote the expletive openers
python3 instruments/test_toolchain.py        # before trusting any number above
```

The baseline is external on purpose. An earlier version of `prose_diet`
normalised against the manuscript's own average, which made the book incapable
of failing its own test and reported a tidy column of 1.00s. **Never let a tool
grade against its own subject.**
