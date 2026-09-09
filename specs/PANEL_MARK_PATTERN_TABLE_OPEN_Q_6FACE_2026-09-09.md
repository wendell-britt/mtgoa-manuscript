---
type: panel
title: "Six-Face panel — the three open questions in the mark-pattern table"
aliases:
  - pattern table open questions
  - P6 refrain or repetition
  - table scope
  - P5 and light_verb
tags:
  - mtgoa
  - editorial
  - proof
created: 2026-09-09
source:
  - specs/SPEC_MARK_PATTERN_TABLE_2026-09-09.md
  - specs/PROOF_MARKS_CH2_CH3_2026-09-09.md
  - instruments/light_verb.py
status: ruled, six of six
---

# The three open questions

**Q1.** P6 is *"repeats a line as a refrain until it stops carrying weight."* Today's `the read`
finding — one word 23 times in one chapter — is arguably the same defect at word scale. One row or
two?
**Q2.** Does the table cover front matter, back matter and the appendices, or only ch1–ch9?
**Q3.** P5, the nothing-word verb, overlaps `light_verb.py`. Is the row a new search or a reading
of an existing counter's output?

## Measured before anybody argues

**Q1, word frequency, every chapter, stopwords removed:**

| chapter | densest content word | `the read` in the same chapter |
|---|---|---|
| ch8 | **game, 175 — 1 per 85 words** | — |
| ch4 | **line, 141 — 1 per 88 words** | — |
| ch6 | design, 94 — 1 per 130 | — |
| ch3 | move, 100 — 1 per 154 | **23 — 1 per 670** |

**`the read` is not in ch3's top twenty.** A frequency counter ranks it far below *move*, *feeling*
and *something*, and its top line book-wide would be *game 175*.

**Q1, refrain, within a chapter:** a search for a sentence repeated 3+ times inside one chapter
returns **four hits, all of them `"Two minutes to capture it as a BAR."`** — the exercise
apparatus, deliberately identical. Across chapters it returns **37 sentences**, topped by
`"RECEIPT. Sit thirty seconds."` twelve times: the 3-2-1 protocol, a form. **P6's own named
instance, `"The world is not fine."`, now stands twice in ch2, not three times.**

**Q2, signposts outside the chapters:** front matter **0**, back matter **1**, appendices **8**.

**Q3, `light_verb.py` against P5's six marked phrases:** it flags *"praise lands warm"* (DEAD). It
misses *"runs clean"*, *"trades contact for control"*, *"buys aim"*, *"metabolize"*. **Four of six
invisible**, in an instrument whose own docstring quotes Wendell on *"land is another one of those
nothing words."* The P5 vocabulary appears **74 times** across the nine chapters.

---

## SHAMAN · the Body — *Wendell did not count anything*

Q1 is the one that matters and the measurement answers it flatly.

**He did not notice `the read` because it was frequent. It is not frequent** — one per 670 words,
outranked in its own chapter by *move*, *feeling* and *something*. He noticed it because he read
the same word doing three unrelated jobs and one of them was hollow. **That is a reading, and a
counter cannot have it.**

Build the frequency counter and the first thing it says is *game, 175 times*. That is ch8's
subject. Then *line, 141* — ch4's subject. **A counter whose top two findings are the two chapters'
titles is the 455-hit machine with a new coat**, and `article.py`'s docstring already carries that
tombstone.

So the Shaman refuses the second row, and refuses it on the strongest ground available: **the thing
it would measure is not the thing Wendell saw.**

**Votes:** Q1, one row. No word-frequency row, no counter.

## CHALLENGER · the Line — *P6 has already dissolved and nobody said so*

Look at what the refrain search returns. **Four hits inside chapters and every one is
`"Two minutes to capture it as a BAR."`** Across chapters, 37, topped by the 3-2-1 protocol twelve
times over.

Those are **forms**. A worksheet instruction repeated identically in six chapters is not a refrain
losing weight; it is a form the reader learns to recognise. Marking them would be vandalism.

And **P6's own instance is down to two**. *"The world is not fine."* stood three times on three
pages when Wendell marked it. It stands twice now. **The pattern was already fixed and nobody
recorded it against P6.**

So the Challenger's position is harder than the Shaman's: **P6 is not a row that opens work. It is
a row that closes CLEAR**, and it closes on two findings — the instances were fixed, and every
remaining repeat is deliberate form. Write that down and stop.

**Votes:** Q1 one row, and that row is **CLEAR**, not OPEN. No counter.

## REGENT · the Inheritance — *the appendices are not the chapters*

Q2 is about what the marks are evidence *of*.

Wendell marked chapter pages. His marks are evidence about **the reading voice** — the one that
walks a reader through an argument. **The appendices are reference material.** *"Appendix G says
where to read her"* is a signpost in a chapter, where the reader is being steered. The same
sentence in an appendix is what an appendix is for.

Eight signpost sites in sixteen appendix files, one in back matter, zero in front matter. **That
distribution is exactly what it should be** — the front matter is voice, the appendices are
apparatus.

So the Regent's answer is not simply *chapters only*. It is: **the table covers ch1–ch9, and it
records the outside count in the same cell without a verdict on it.** The number is cheap and it is
evidence for later. A verdict on it would be applying chapter standards to reference pages, which is
the DL-85 mistake — a category taken from a spec and never tested against the text.

**Votes:** Q2 ch1–ch9 ruled; front, back and appendices counted and left unruled, in the same row.

## ARCHITECT · the Design — *Q3's answer is a defect report, not a design choice*

The Q3 measurement is worse than an overlap question.

`light_verb.py` **exists because of P5**. Its docstring opens with Wendell on *"lands warm"* and
*"land is another one of those nothing words."* It catches that one. It misses *runs clean*,
*trades contact for control*, *buys aim*, and *metabolize* — **four of the six phrases in the
pattern that produced it.**

That is not a scope decision. **That is an instrument that was built from a complaint and does not
cover the complaint**, and the reason nobody noticed is that it has been reporting a healthy-looking
DELEXICAL rate this whole time. Same shape as `--verify` reporting *round-trip OK* over eight stale
blocks: **a green number over an unlooked-at half.**

So P5's row is neither a new search nor a reading of the counter. It is **a row whose finding is
that the counter has a hole**, and its verdict is OPEN with that named. Whether the fix is to widen
`light_verb.py`'s DEAD list is a separate ruling and the Architect will not take it inside a table
build — but the row must say it, or the hole closes over again.

**Votes:** Q3 the row reports the gap. 74 sites counted, `light_verb` coverage stated per phrase,
verdict OPEN. Widening the instrument is its own ruling.

## DIPLOMAT · the Table — *what the reader of this table is for*

Somebody has to ask who reads it. Wendell does, once, to decide which rows become work.

That means **a row's cell must be readable without running anything**, and it means the table must
not be so long that reading it is a project. Seven rows. Six fields. Anything else is a second
document pretending to be a column.

The Diplomat's condition on Q2 follows: **counting front matter and appendices is fine; giving them
verdicts is not**, because a verdict invites a decision, and Wendell has not asked for decisions
about reference pages. A number in a cell asks nothing.

And on Q1, the Diplomat agrees with the Challenger and adds the practical half: **if P6 closes
CLEAR, say in the row that its named instance was already fixed.** Otherwise the next person reads
CLEAR as *never was a problem*, which is not what happened.

**Votes:** Q1 one row, CLEAR, with the history in the cell. Q2 counted, not ruled. Q3 as the
Architect.

## SAGE · the Board — *two of three questions dissolved on measurement*

Worth naming what just happened, because it is the third time today.

**Q1 asked whether to build something and the measurement said the something would not find the
thing.** Q3 asked how a row relates to an instrument and the measurement said the instrument is
broken. **Neither was a design question. Both were facts nobody had checked.**

That is the same shape as this morning's DL-89 — carried through three documents as a question
about truth, answered in June by behaviour — and the same shape as `--verify`. **The pipeline keeps
producing questions that are already answered by a number nobody ran.**

So the Sage's contribution is the rule, again, sharpened: **before a question reaches a panel, run
the cheapest measurement that could dissolve it.** Two of three did, in under ten minutes, and the
panel's real work was Q2 alone.

**Votes:** all three as above. And the standing addition: **an open question in a spec must carry
the measurement that would settle it, or it is not an open question, it is an unrun search.**

---

## Consensus, six of six

**Q1 · One row, and it closes CLEAR.** P6 stays a single row about a repeated *line*. **There is no
word-frequency row and no counter**, because the measurement shows frequency does not isolate what
Wendell saw: `the read` is one per 670 words and does not reach ch3's top twenty, while a frequency
counter's top findings would be *game 175* and *line 141* — the two chapters' own subjects. He found
it by reading one word doing three jobs, and a counter cannot do that. P6 itself closes CLEAR on two
findings: the refrain search returns only deliberate form — `"Two minutes to capture it as a BAR."`
and the 3-2-1 protocol — and **P6's named instance is already down from three to two.** The row
records that history so CLEAR is not misread as *never was a problem*.

**Q2 · ch1–ch9 ruled; front matter, back matter and appendices counted and left unruled.** The marks
are evidence about the reading voice, and the appendices are apparatus. The distribution says so:
0 signposts in front matter, 1 in back matter, 8 across sixteen appendix files, which is what an
appendix is for. **A number in a cell asks nothing; a verdict invites a decision Wendell has not
asked for.**

**Q3 · The row's finding is that `light_verb.py` has a hole.** It was built from P5 — its docstring
opens on *"land is another one of those nothing words"* — and it catches *lands warm* while missing
*runs clean*, *trades contact for control*, *buys aim* and *metabolize*: **four of the six phrases
in the pattern that produced it**, while reporting a healthy DELEXICAL rate over the gap. The row
counts the 74 sites, states coverage per phrase, and stands **OPEN**. **Widening the instrument is
its own ruling and is not taken inside a table build.**

**One rule out of the Sage, which outlives this panel.** Two of three questions dissolved on a
measurement that took minutes and had never been run. **An open question in a spec must carry the
measurement that would settle it, or it is not an open question — it is an unrun search.**

## What the panel refuses

It does not build a word-frequency counter whose first finding would be the title of the chapter it
is reading. It does not mark a form as a refrain. It does not give verdicts to reference pages. It
does not widen `light_verb.py` inside a table build. And it does not let P6 close CLEAR without its
history in the cell.
