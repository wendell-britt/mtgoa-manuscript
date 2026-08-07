# Hostile review — the readability pass

**Wendell, 2026-08-01:** *"you're reporting the book is too easy to read and I'm
having the experience it is difficult to read because of how the sentences make
people's minds work."*

He is right, the pass was wrong, and the way it was wrong is worth writing down.

---

## 1 · The pass disproved its own headline and then printed it anyway

`READABILITY.md` opens by explaining, correctly and at length, that readability
formulas measure two surface proxies — word length and sentence length — and
cannot see cohesion. It cites the literature saying a more cohesive text can score
harder and read easier.

Then it makes **"Flesch-Kincaid 7.2 against the control's 10.6"** the headline,
titles the section *"The headline: the book is too easy, not too hard,"* and
anchors every recommendation to closing that gap.

That is the whole error. Having established the instrument could not see the
construct, the pass reported the instrument's number as the finding. Worse, the
recommendation that follows from it — *get closer to 10.6* — means **lengthen
sentences**, and sentence length is not what is costing the reader anything here.

## 2 · The Igniting Joy baseline is good, and it was being used for the wrong job

Wendell: *"connecting it to Igniting Joy's readability level WHICH IS a good
baseline, but we really haven't solved for the deeper issue."*

Correct on both halves. *Igniting Joy* is the right control for **voice** — that
is what `SPEC_REPETITION_AND_CUTS` established it for, and the short-declarative
drift finding stands. It is the wrong control for **reading experience**, because
the only thing the comparison produces is a grade level, and the grade level is
the number that cannot see the problem.

## 3 · What the sentences are actually doing

Measured with real part-of-speech tagging, on the construct that predicts reading
time. Kintsch and Keenan, 1973: **the number of propositions in a sentence, not
the number of words, determines reading time.**

### My hypothesis was also wrong, and the result is better than it was

I predicted the short sentences would be propositionally *dense* — many ideas
crammed into few words. Measured, they are the **thinnest** in the book:

| Sentence band | share | P-density |
|---|---|---|
| ≤6 words | 23.4% | **0.417** |
| 7–14 | 36.3% | 0.445 |
| 15–25 | 26.7% | 0.459 |
| 26–40 | 11.5% | **0.469** |

Whole body **0.456**, against roughly 0.50 for ordinary English prose. The book is
*below* normal density. So the cost is not per-sentence load.

### The cost is integration, and here is the measure of it

A sentence whose opening carries no content word from the sentence before it
starts on new information: the reader has nothing to attach it to and must
re-anchor. Against Wendell's own five `VOICE_ANCHOR.md` passages — the prose he
selected as the book at its best:

| | starts on new information |
|---|---|
| The five anchor passages | **57%** |
| The whole body | **79%** |

**Twenty-two points, measured against his own standard.** And the anchor passages
are also *denser* than the book — 0.500 against 0.456 — not sparser.

### The mechanism, stated plainly

Each sentence is short, propositionally thin, and opens on new material, with few
connectives between. Nothing is hard to decode. Everything has to be assembled.
The reader is handed a sequence of finished assertions and has to work out the
relations between them herself, because the prose states rather than connects.

That produces exactly the profile observed: **scores easy, reads hard.** The
formulas measure decoding load, which is genuinely low. The felt cost is
integrative load, which no formula counts.

Three earlier findings turn out to be the same defect seen from different angles,
which is why they all pointed at the same chapters:

- referential overlap 0.12 between adjacent paragraphs
- connectives at 13.8 and 14.5 per thousand in ch1 and ch9, against 17–19 mid-book
- 23.4% of sentences at six words or fewer, against the control's 4.2%

## 4 · What survives from the readability pass, and what does not

| Finding | Verdict |
|---|---|
| R1 · nine drift runs, 13 anaphora, 4 rosters | **Stands, and is now central.** The device/drift split is the useful half of that pass. |
| R2 · 19 single-sentence paragraphs of 40+ words | **Stands.** Independent of all this. |
| R4 · connectives thin in ch1 and ch9 | **Promoted.** Ranked third; it is part of the core mechanism. |
| R5 · ch4 lowest on referential cohesion | **Promoted**, same reason. |
| R3 · 45 grade-13.8 paragraphs | **Withdrawn as a priority.** Measured on the construct that does not apply. |
| The headline, and the target of 10.6 | **Withdrawn.** |

## 5 · What follows

**The direction of the fix reverses.** A readability pass says shorten and
simplify. This says the opposite: the book needs *more* subordination, *more*
connective, and sentences that open on something the reader already holds. That is
what the anchor passages do, and it is why they read as the book at its best.

**The unit of work is the transition, not the sentence.** The 79% figure is about
sentence *joins*. A pass that rewrote individual sentences to be better sentences
would not move it.

**One instrument, one construct.** `readability.py` keeps the formulas because a
publisher will ask for them, but its headline now points here.

Nothing in the manuscript changed.
