# SPEC — The Em-Dash Ruling, and the Word-Density Pass

**2026-07-29. Book-wide. Two passes, opened by two different findings on the
same day.**

---

## Part 1 · Em-dashes

### 1.1 The ruling

Wendell, on reading the em-dash count:

> *"I personally don't even know how to use emdashes which is how I know they
> are outside of my style."*
>
> *"I will struggle to recognize in myself writing that makes any use of
> emdashes."*

That settles a question the numbers could not. The copula ruling was genuinely
open — a workbook may earn short declaratives. **This one is not open.** An
author who does not use a mark cannot have written 1,072 of them. They came from
the machine, and every one is a place where a drafting model reached for rhythm
instead of choosing a comma, a colon, a period, or a parenthesis.

The second quote is the operationally important one. **Wendell cannot catch this
by reading**, the way he caught *rooms* and the *which is* fragments in ch5. A
mark you never learned is a mark you do not see. So this pass cannot be run the
way the register pass was — numbers, then read it, then approve. The reading
check does not work here, and the tooling has to carry the whole load.

### 1.2 What is actually there

Measured on prose only. Earlier counts of 1,290 and 1,274 were wrong: they swept
in the ASCII axis diagrams (`←——●——→`), the BAR-grid table rows, and list
bullets, none of which is prose.

| ch | headings | prose | prose /1k |
|---|---|---|---|
| 1 | 7 | 58 | 8.7 |
| 2 | 2 | 34 | **5.2** |
| 3 | 8 | **207** | **15.3** |
| 4 | 4 | 106 | 11.6 |
| 5 | 4 | 101 | 12.9 |
| 6 | 3 | 100 | 11.4 |
| 7 | 11 | **181** | **17.2** |
| 8 | 8 | 150 | 12.5 |
| 9 | 2 | 135 | 11.9 |
| | **49** | **1,072** | 12.4 |

Headings are a separate question and are **not** in scope. `# Chapter 1 — The
Infinite Arcade` is title typography, not a sentence, and nothing about the
ruling reaches it.

**ch2 at 5.2 is the proof of concept.** It is the most recently rewritten
chapter and it is less than a third the rate of ch7. The book can already do
this; ch2 shows what it reads like.

### 1.3 The shapes, so the pass is not freehand

Classifying all 1,072:

| shape | count | share | what replaces it |
|---|---|---|---|
| single tail, capital or clause continuation | 433 | 39% | comma, or a full stop |
| single tail, lowercase continuation | 398 | 36% | comma, or a colon if the tail names |
| opens a parenthetical pair | 125 | 11% | comma pair, or parentheses |
| closes a parenthetical pair | 76 | 7% | the matching close |
| introduces an italic quote | 27 | 2% | colon |
| other | 13 | 1% | read it |

**75% are single tails.** That is the whole finding. The manuscript does not use
the em-dash for its one defensible job — a genuine interruption of the sentence's
own logic — it uses it as a general-purpose joint that avoids deciding between a
comma and a period.

Which is exactly what `no-ai-slop` names: *"Do not use them as a default rhythm
crutch… Remove clusters and decorative dashes."*

### 1.4 The rule for the pass

For every dash, ask **what decision the dash avoided**, then make it:

1. **Two independent clauses?** Full stop. This is the most common answer and
   the one the drafting model was avoiding, because a period commits.
2. **A modifier, list, or aside?** Comma, or a comma pair.
3. **The tail names or defines what came before?** Colon.
4. **A true interruption — a different voice cutting in?** This is the only
   licensed use, and it should survive at roughly ch2's rate.

**The trap, and it is the same one W7 hit.** The register pass produced a
formula (9 of 12 copula openings) and needed a fourth pass to break it. Converting
1,072 dashes to periods would raise the ≤6-word sentence share, trading one
defect for another. **Every batch reports em-dash count, copula/1k, and ≤6-word
share together, or it is reporting a win it did not get.**

### 1.4a One ruler, three commits

Run 2026-07-29 with a single script over the same three measures, because the
figures scattered across the specs were each taken with a different sentence
splitter and are not comparable to one another.

| | copula /1k | ×IJ | ≤6 words | em-dash | words |
|---|---|---|---|---|---|
| `e662f84` before the register fan-out | 57.8 | 2.01× | 26.2% | 1,278 | 97,738 |
| `2d7d866` after the fan-out | 41.3 | 1.44× | 25.6% | 1,290 | 97,006 |
| after the W8 and W9 batches | 40.9 | 1.42× | 25.7% | 1,222 | 96,835 |

The word column is a historical record, not the current figure. The decline
continued to 96,468 by `ebf5fda`; body text stands at **97,013** as of
2026-07-30. `MANIFEST.md` and `specs/MANUSCRIPT_FILE_CANON.md` carried the
`e662f84` figure until then.

Two things fall out of that table, one reassuring and one not:

- **The register fan-out did not buy its copula win with short sentences.**
  ≤6-word share moved 26.2% → 25.6%. The trade-off that the ch8 Section 2 test
  predicted did not happen at book scale. That worry is closed.
- **The fan-out added twelve em-dashes.** 1,278 → 1,290. Splitting a sentence
  and reaching for a dash to rejoin the halves is precisely the reflex this
  spec exists to stop, and the register pass had no counter watching for it.
  That is why the budget in §3 ratchets rather than merely reports.

**On the 19.4% figure in `SPEC_REGISTER`:** that number and the 26.2% above
describe nearly the same text. The gap is the splitter, not the prose. Neither
is wrong; they are not comparable, and no pass should ever chase one against a
baseline taken with the other. Numbers in this spec use
`re.split(r'(?<=[.!?])\s+', text)` on marginalia-stripped body, and any future
figure that wants to sit in this table uses the same.

### 1.5 The comparison that is blocked

*Existential Kink* is the right comparison and Wendell asked for it. It cannot be
run here: `sources/` is gitignored and is not in this container. `SPEC_REGISTER`
and `SPEC_REPETITION_AND_CUTS` record Elliott's copula, sentence length, burstiness
and first-person rates, but **no source in this repo records an em-dash rate for
Elliott, Chou, or *Igniting Joy*.**

The *Igniting Joy* figure of 5.4/1k quoted in conversation on 2026-07-29 came
from an in-session computation against a corpus that is no longer present, and
whether it was measured on prose or raw text is not recorded. **Treat it as
unconfirmed.** Do not build a target on it.

Restore `sources/` and the comparison takes one command. Until then the ruling
stands on its own — it does not need a comparable, because it is a statement about
whose hand wrote the mark.

### 1.6 Order

**ch7 (17.2), ch3 (15.3), ch5, ch8, ch9, ch4, ch6, ch1.** ch2 is done at 5.2 and
is the reference, not a target.

---

## Part 2 · Word density

### 2.1 *actually* — 260 uses, 2.7/1k

Run through `no-ai-slop`, which lists *actually* as an often-empty adverb.
**It is not empty here**, and the pass has to start by saying so, because a
mechanical cut would strip the book's thesis word:

> *what the moment actually needed* · *watch what people actually do rather than
> what they say* · *which game is actually being played* · *who you actually are*

The whole book is about the gap between the stated and the real, and *actually*
is the word that opens that gap. 109 of the 260 sit in a sentence carrying an
explicit contrast marker; most of the remaining 151 carry it implicitly.

**So the defect is density, not slop.** One use every 373 words book-wide, and
one every 240 in ch7. A word that does real work stops doing it when the reader
starts seeing it.

| ch | *actually* | /1k | *just* | /1k |
|---|---|---|---|---|
| 1 | 19 | 2.5 | 9 | 1.2 |
| 2 | 11 | 1.5 | 12 | 1.7 |
| 3 | 53 | 3.5 | 15 | 1.0 |
| 4 | 20 | 1.8 | 21 | 1.9 |
| 5 | 15 | 1.7 | 6 | 0.7 |
| 6 | 19 | 1.9 | 10 | 1.0 |
| 7 | **53** | **4.2** | 9 | 0.7 |
| 8 | 38 | 2.9 | 12 | 0.9 |
| 9 | 32 | 2.7 | 18 | 1.5 |
| | **260** | 2.7 | **112** | 1.2 |

**Target ch2's 1.5/1k**, the same chapter that anchors the em-dash pass. That is
about 115 cuts, concentrated in ch7 and ch3.

**The method is substitution, not deletion.** Where the contrast is the point,
name it: *what the moment needed, against what you offered* · *watch what people
do rather than what they say* (already carries its own contrast — the *actually*
is redundant there) · *which game is being played under the one they named*.
Where the sentence already carries an explicit contrast marker, the *actually* is
doing that work twice and simply comes out.

Two sentences use it twice inside themselves. Those come out first.

### 2.2 What `no-ai-slop` cleared

Recorded so nobody re-opens it:

- **`leverage`, 22 uses.** All 22 are *leverage point* in the systems-design
  sense, including the named ch6 move **Find the Leverage Point**. None is the
  banned corporate verb. **Not a finding.**
- **Banned phrases: 3 in 96,896 words**, all fixed 2026-07-29 (*here's the
  thing*, *at its core*, *in terms of*). The list mostly exonerates the prose.
- **Superficial `-ing` clauses: 0.** No *highlighting*, *underscoring*,
  *showcasing*, *reflecting*.
- **Importance puffery, weasel attribution, summary-recap endings: 0.**

One place the skill and this book disagree, noted so the next pass does not
thrash: `no-ai-slop` says *"Prefer 'is' and 'has' when they are clearer"*, and
`SPEC_REGISTER` is removing 3,222 copulas. **`SPEC_REGISTER` wins.** The skill is
guarding against fake-strong verbs substituted for plain ones; the register work
is removing copulas that have no verb at all behind them. Different defects.

---

## 3 · How this gets checked

```
python3 instruments/emdash.py            # per chapter, prose only, with the budget
python3 instruments/emdash.py -v         # quote every dash with its shape
python3 instruments/prose_diet.py        # copula and short-sentence share, both directions
python3 instruments/gate.py              # the ratcheting budget fails the build on regression
python3 instruments/test_toolchain.py    # before trusting any number above
```

The gate carries a **ratcheting budget** rather than a flat ban, because a
handful of true interruptions are licensed and a flat ban would be a lie. The
budget only ever goes down. It cannot be raised to make a batch pass — raising it
is the one edit to `gate.py` that requires Wendell.

That mechanism exists because of §1.1: **the author has said he cannot see this
defect in his own prose.** Every other rule in this book has a human backstop.
This one does not, so the tool is the backstop, and it has to be unable to drift.
