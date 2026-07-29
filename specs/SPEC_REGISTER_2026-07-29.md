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
removing 3,222 of them, which is rewriting roughly half the copula sentences in
the book. That is a register rewrite, not a pass. **It cannot happen before
August 1 and this spec does not pretend otherwise.**

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
