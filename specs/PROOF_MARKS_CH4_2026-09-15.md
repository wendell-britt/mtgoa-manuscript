---
type: readnotes
title: "Proof marks for ch4 — The Challenger, Wendell's highlighter flags, located and diagnosed"
aliases:
  - ch4 proof marks
  - Challenger marks
tags:
  - editorial
  - mtgoa
  - proof
  - ch4
created: 2026-09-15
source:
  - manuscript/ch4.md
  - specs/MARK_PATTERN_TABLE_2026-09-09.md
  - specs/PROOF_READNOTES_V2_2026-09-01.md
status: batch 1 intaken (proof pp.120-129). More batches expected; append, do not replace.
---

# Proof marks — Chapter 4, The Challenger

**Nothing in this file is applied.** Every proposed fix is a draft for approval. The manuscript is
untouched. Applied only per Wendell's call, span by span. Same discipline as `PROOF_READNOTES_V2`.

**The proof is NOT in sync with the manuscript.** This is new, and it changes how to read every
mark below. `ch4.md` changed in nineteen commits between 2026-08-29 and 2026-09-14 — the fragment
ban, the P5/P3 sweeps, and the five drawdowns (polysyndeton, light_verb, slop_shapes, telling,
trailing_and). The physical proof predates all of it.

Of 58 marks in batch 1, **34 are live** (the marked words are still in `ch4.md` verbatim) and
**24 have already been rewritten**. A mark landing on already-rewritten text is not noise: it says
the shape was real, and the question becomes whether the rewrite satisfied the objection.

---

## The finding that matters more than any single span

**The drawdown removed the token and often left the shape.** `trailing_and.py` counts a comma, a
coordinating conjunction, and a second independent clause. The drawdown drove that count to zero.
The construction Wendell's highlighter is actually catching is **a clause tacked on to tell the
reader what the first clause meant** — P1 in the mark-pattern table. The `, and` is how it usually
arrives, not what it is.

Where the two came apart, the board went green and the mark stayed true:

| proof (p.127) | `ch4.md` now | verdict |
|---|---|---|
| The move gets run, **and** the output gets called a finding. | The move gets run, **then** its output gets called a finding. | **fixed** — `then` commits to sequence, which is Strunk's actual instruction |
| ...goes into escrow until the verdict, **and** the verdict does not release it. | ...goes into escrow until **a verdict that** does not release it. | **defect gone, cost incurred** — the definite anaphora to the verdict named upstream is lost |
| (p.129) ...almost everyone skips, **and** the standing is the stage almost everyone collapses at, four seconds of not adding a sentence, where most lines get taken back... | ...almost everyone skips the aim stage, **while** almost everyone collapses at the standing stage, four seconds of not adding a sentence, where most lines get taken back... | **worse** — 60 words, `;` then `while` then an appositive then `where`. The `and` left; the tacking-on grew |
| (p.129) ...following the right people, **and** its defensibility is what makes it durable. | It stands as the most defensible myth in the book. **That defensibility is what makes it durable.** | **half** — `and` gone, verdict stamp intact |

The third row is the one to look at. A sweep that scores the token can trade a banned `and` for a
longer chain and register as progress.

## Two detector gaps, measured

`trailing_and.py` reports ch4 at **6 LOOSE / 752 sentences (0.8%)**, all six ledgered. Marked
sites that are textbook trailing coordination and that the detector does not see:

**1. `SUBORDINATOR` swallows demonstrative `that`.** (L664)

> ...an old charge wearing today's clothes, **and that question is what the whole chapter turns on.**

The tail opens `that`, read as a subordinating conjunction introducing a subordinate clause. Here
`that` is a determiner on `question`. `DEMONSTRATIVE` covers `that` + copula, not `that` + noun +
copula, so nothing catches it.

**2. `BARE_PREDICATE` cannot reach a verb behind a participial subject.** (L755)

> What resists being seen gets located outside you before the noticing has finished, **and the hand holding the instrument escapes it.**

Subject is `the hand holding the instrument`; the finite verb `escapes` sits four words in, past the
window. Any subject carrying a participial or prepositional modifier hides its own clause.

Both are recall bugs with a bounded fix, and both would have flagged a live marked site. Neither
is P1's "UNSEARCHABLE" verdict: the shape is searchable, the detector is just short.

---

## Batch 1 — live marks, by diagnosis

`L` is the line in `manuscript/ch4.md`.

### A. Interprets the observation — the tacked-on clause (P1)

| p. | L | span | note |
|---|---|---|---|
| 123 | 664 | ...today's clothes, **and that question is what the whole chapter turns on** | detector gap 1 |
| 127 | 755 | ...before the noticing has finished, **and the hand holding the instrument escapes it** | detector gap 2 |
| 121 | 632 | Talk it down **and you aim the smaller charge** | bare `and`, no comma — outside the scanner entirely |
| 122 | 646 | ...**and which one you are actually carrying decides what comes out** | |
| 120 | 620 | She did not ask you to name it, **and that risk is yours** | |

### B. Concludes for the reader — the verdict stamp (P2)

| p. | L | span | note |
|---|---|---|---|
| 123 | 664 | **Named, you choose.** | two words doing a paragraph's work |
| 124 | 688 | **That's usually all it takes.** | |
| 125 | 704 | ...you did not make the Challenger's move. **You described it.** | |
| 127 | 765 | **It bites hardest at Clean Up.** | |
| 128 | 779 | **The tell that a quest is alive is not enthusiasm.** | |
| 129 | 794 | **That defensibility is what makes it durable.** | survived the `and` fix as its own sentence |

### C. `because` carrying an assertion that was not earned

| p. | L | span |
|---|---|---|
| 124 | 702 | An assessment costs nothing, **because being right is not a position anybody has to argue with** |
| 122 | 648 | ...lands hard and lands clean, **because Fire asks for agency** |
| 122 | 652 | ...does not defend, **because a defense answers an accusation and Water made a report** |
| 121 | 638 | ...you will know, **because the sentence was about a person instead of about a line** |

Not trailing coordination — `because` commits to cause, which is what Strunk asks for. The mark is
landing on something else: the cause asserted is the *interpretation*, so the sentence still tells
the reader what to conclude. Worth a ruling on whether C is its own row or a variant of A.

### D. Remaining live marks, awaiting diagnosis

p.120 L602, L612, L618 · p.121 L628, L634 · p.123 L668, L670 · p.124 L686, L702 ·
p.125 L704, L714 (×2), L718 · p.126 L726 · p.127 L749 · p.128 L769 · p.129 L796

---

## Batch 1 — marks on text already rewritten

Check whether the rewrite answered the objection. Where it did not, the mark stays live against the
new words.

p.121 L634 · p.122 · p.123 (`Four words each, no explanation` — gone entirely) · p.124 ·
p.125 · p.126 (`Same grid as the Shaman's` — gone) · p.127 (the Skeptic's five, four of five
rewritten) · p.128 (`That is the gift` → `That names the gift`; `one card` → `one pass`) ·
p.129 (both recap marks rewritten, one improved, one worse)

---

## Open questions for Wendell

1. **Is C a row?** If `because` + interpretation counts, the sweep surface is much larger than
   trailing coordination and no current instrument addresses it.
2. **Does the p.129 recap sentence get taken apart?** It is the clearest case of a drawdown making
   a sentence longer, and it sits in the chapter's closing argument.
3. **Fix the two detector gaps before the next batch?** They are bounded, and every later chapter
   gets the benefit.
