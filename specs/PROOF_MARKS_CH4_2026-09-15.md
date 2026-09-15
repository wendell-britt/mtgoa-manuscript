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
status: batches 1-3 intaken (proof pp.100-129). More batches expected; append, do not replace.
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


---

# Batch 2 — proof pp.110-119

62 marks. **41 live, 21 already rewritten.** Four marks are in pen, and they are worth more than
the highlights: a highlight reports a symptom, these name a defect.

## The pen marks

### 1. "By who?" + "Passive" — p.113, L425

The sentence in the proof, and the sentence now:

```
proof   A version of this chapter gets braced against, and it should be named before we go further.
now     A version of this chapter gets braced against. It should be named before we go further.
```

Commit `40077a6`, *"Land the trailing_and pass on the proof line: 0 unresolved"*, made that change.
**The sweep had this exact sentence in its hands, scored it clean, and left both agentless passives
standing.** Who braces? Who should name it? Two sentences, two hidden agents, and the drawdown's
answer was to split them into two.

This is the whole problem in one line, and it is now on the record rather than inferred. The `and`
was never the defect. It was the seam where the defect was easiest to count.

**No instrument covers this.** `prose_diet.py` has a `passive` column and ch4 scores 1.04, dead on
baseline, because the chapter's passives are local to passages like this one and average away
across 12,097 words.

### 2. "Stop telling people things are real" — p.112, L421 and passim

> The fire was real. The line was real. Without the practice to draw it clean, the fire just burned
> everything down.

Assertion by repetition: the prose insists on a quality instead of showing it. **This one measures,
and ch4 is an outlier:**

| ch | hits | per 1k words |
|---|---:|---:|
| 1 | 2 | 0.22 |
| 2 | 4 | 0.45 |
| 3 | 6 | 0.40 |
| **4** | **13** | **1.07** |
| 5 | 5 | 0.43 |
| 6 | 4 | 0.34 |
| 7 | 7 | 0.50 |
| 8 | 9 | 0.63 |
| 9 | 2 | 0.18 |

Counting `is/was/are/were/stay/feels + real` and `real + harm|stakes|one|line|charge|thing` over
body text with the frame stripped. **ch4 runs 1.7x the next-highest chapter and roughly 5x ch1.**
A new row for the mark-pattern table, and unlike P1 and P2 it is trivially searchable.

### 3. "incorrect" — p.115, L510

Wendell is right, and it is a contradiction inside four lines, not a wording problem.

```
L510   The Skeptic decides something narrower and more damaging than either:
       whether what you reacted to was ever real.

L514   The question changes shape without announcing that it has changed,
       from *is this real* to *are you the one who gets to say it is real.*
```

L514 is the chapter's own mechanism: `is this real` is the **legitimate** auditor question, and the
corruption is the shift to **standing**. L510 names the legitimate question as the damaging one.
L512 then calls a near-identical question *"the single useful question"*, and p.129 describes the
daemon as *"the judge that audits your standing instead of your..."* — every other passage agrees
with L514 and against L510.

**Proposed fix, for approval:** L510 becomes the standing question, e.g. *"The Skeptic decides
something narrower and more damaging than either: whether you are the one who gets to say it was
real."* One sentence, and it puts the daemon's definition where the rest of the section already has it.

`review.py` step 7k reports `CLAIMS PASS`. It checks that guarded spans sit where their ruling left
them; this span is not guarded, so the pass is true and silent about the contradiction.

### 4. "Questions aren't answered" — p.116

**The obvious reading does not hold up.** ch4 runs 28 question marks, 2.31 per 1k words, which is
below ch5 (3.59), ch6 (3.74), ch7 (3.11), ch8 (3.93) and ch9 (3.82). It is not a volume problem.

Best reading of the note, offered for correction: on this page the interrogative does two unrelated
jobs and neither resolves. The daemon's voice is punctuated as statement — *"Am I overreacting.
Other people have it worse. I'm probably being dramatic."* (never carried a question mark in this
repo's history) — while *"Ask yourself whether you feel certain"* is a real prompt to the reader
that the page answers on the reader's behalf one clause later. **Needs Wendell's call on what the
note meant before anything is drafted.**

## Batch 2 — live highlight marks

p.110 L335, L367 · p.111 L375, L385 · p.112 L401, L419, L421 · p.113 L425, L427 (x2), L429, L438 ·
p.114 L462, L466, L472 · p.115 L510, L512 (x3) · p.116 L512 (x2), L514, L518 (x2), L522 ·
p.117 L524 (x2), L528, L532 (x3), L534 · p.118 L559, L565 · p.119 L565, L571, L575, L577, L585,
L596, L598

Same A/B/C split as batch 1 holds. Heaviest concentration is L512 and L532, where several marks
land on one long line.

## Running total, batches 1-2

**120 marks · 75 live · 45 on rewritten text.**

## Open questions, updated

1. **C (`because` + interpretation) — is it a row?** Carried from batch 1.
2. **Agentless passive — is it a row?** The pen says yes. Nothing measures it locally.
3. **Real-insistence — promote to an instrument?** It measures, ch4 is 1.7x the next chapter, and
   it would take an afternoon.
4. **L510 — approve the standing-question fix?** This one is a factual error in the book's own
   model, not a line-quality call.
5. **What did "Questions aren't answered" mean?**


---

# Batch 3 — proof pp.100-109

59 marks. **38 live, 21 already rewritten.** One pen mark, and it opens a hole nothing in the repo
was looking at.

## The pen mark: "Repeat of polarity?" — p.104

Yes. Verbatim, in three chapters:

| file | line | |
|---|---|---|
| `manuscript/ch4.md` | 198 | byte-identical to ch7 |
| `manuscript/ch7.md` | 198 | byte-identical to ch4 |
| `manuscript/ch5.md` | 245 | one clause apart (`stuck on one so long that the other` / `stuck there so long the other pole`) |

> A polarity is not a problem to solve. It has two poles, both of them right. The charge comes not
> from one side being wrong but from getting stuck on one so long that the other stops existing for you.

**`review.py` step 7c reports `dupes ok 0 pair(s) — clean`.** It is not wrong about what it checks.
`instruments/dupes.py:82` reads:

```python
if f2 != f or abs(n2 - n) > 400:
    continue
```

**Same file only, and within 400 lines.** A paragraph that ships in three different chapters is
structurally invisible to it. The instrument was written 2026-08-07 against three pairs that all sat
inside one file, and the guard that made it fast for that case is the guard that blinds it here.

### What the cross-file scan finds

Same `MIN_WORDS = 25` and `NEAR = 0.90`, same surfaces, with only the `f2 != f` guard removed.
1,775 paragraphs compared:

| | pairs | of those, shipping text |
|---|---:|---:|
| cross-file EXACT | 31 | **14** |
| cross-file NEAR | 22 | **19** |

The remainder (17 exact, 3 near) are `APPENDIX_C_KEY_TERMS.md` against its own
`_backup_2026-06-04_pre-trailing-promote.md`, which does not ship. That file should be excluded the
way `profile.corpus` already excludes non-shipping appendices.

### Most of the 33 is deliberate, and saying otherwise would be wrong

`dupes.py`'s own docstring anticipates this: *"The book repeats deliberately and often... Those are
structure, not duplication."* Holding to that:

- **`You drew the [X ↔ Y] axis earlier in this chapter. Here is why the [daemon] is nearly
  impossible to catch standing on it`** — ch4 Force↔Restraint/Skeptic (L559), ch6
  Structure↔Agency/Emotional Body (L464), ch7 Care↔Impact/Victim (L611). A frame, filled per
  chapter. Correct by design.
- **`3 · FACE IT.`** — twice per chapter, ch3 through ch8, chapter-specific question each time.
- **`Chapter 1 taught you to read your own fuel...`** — ch3 L439 through ch8 L457, each naming its
  own Face. The ladder is the point.
- **`A reading that ends in a notebook stays a reading you had...`** — ch3 L897 through ch8 L814,
  six chapters, byte-identical. Deliberate, though six is worth a look on its own.

**The polarity definition is not one of these.** It is expository prose that defines a concept from
scratch, and it defines it three times as though the reader has not met it. No slot is filled, no
noun changes. That is the difference Wendell's pen found and the instrument could not.

## A third case of the sweep doing the damage

Before commit `a8db0ca` (*"Telling drawdown via fan-out: 661 -> 85"*), every chapter carried the
same boilerplate:

```
all chapters   How big is the charge, and where does it sit in you?
```

After it:

```
ch4.md:452     How big does the charge run,  and where does it sit in you?
ch5.md:456     How big does the charge feel, and where does it sit in you?
ch6.md:344     How big does the charge feel, and where does it sit in you?
ch7.md:532     How big does the charge feel, and where does it sit in you?
```

The drawdown targets the copula, so it had to rewrite `is`. **Fanned out per chapter, it rewrote one
shared sentence two different ways** — `run` in ch4, `feel` everywhere else. Parity that existed
before the sweep does not exist after it, `run` is worse English than either alternative, and
`dupes.py` cannot report the divergence for the same cross-file reason as above.

Batches 1, 2 and 3 have now each produced an instance: **the sweep removed the token and left the
shape** (p.129 recap), **the sweep split the sentence and left the passives** (p.113, commit
`40077a6`), **the sweep broke shared boilerplate into variants** (p.107 3-2-1, commit `a8db0ca`).

## Batch 3 — live highlight marks

p.100 L97 (x2), L108 (x3) · p.101 L118, L122 (x2), L128 · p.102 L139, L141, L151 (x2) ·
p.103 L166 (x2), L170, L176 (x2) · p.104 L198, L208 (x3) · p.105 L220, L238 · p.106 L277 (x2) ·
p.107 L279, L281 (x4), L283 (x2) · p.108 L305 · p.109 L311, L323, L329 (x2)

## Running total, batches 1-3

**179 marks · 113 live · 66 on rewritten text.**

## Open questions, updated

1. **C (`because` + interpretation) — is it a row?** (batch 1)
2. **Agentless passive — is it a row?** (batch 2)
3. **Real-insistence — promote to an instrument?** ch4 at 1.07/1k vs 0.18-0.63. (batch 2)
4. **L510 — approve the standing-question fix?** A factual error in the book's own model. (batch 2)
5. **What did "Questions aren't answered" mean?** (batch 2)
6. **The polarity definition — cut to one, or make ch5 and ch7 point back to ch4?** It is introduced
   in ch4, where the Force ↔ Restraint axis is drawn.
7. **Drop the `f2 != f` guard in `dupes.py`?** Cross-file is a different question from merge twins
   and probably wants its own board, plus the backup-file exclusion.
8. **`How big does the charge run` — revert ch4 to match, or rule one wording for all five?**
