---
type: gap
title: "Instrument defects found by the ch4 proof pass — what the boards were measuring instead"
aliases:
  - instrument defects
  - fragment tagger gap
  - why the board was green
tags:
  - instruments
  - review
  - process
  - fragment
created: 2026-09-15
review: 2026-09-22
source:
  - instruments/fragment.py
  - instruments/draft_lines.py
  - instruments/dupes.py
  - instruments/trailing_and.py
  - specs/PROOF_MARKS_CH4_2026-09-15.md
status: open. None of these is fixed. Wendell is marking manually until they are.
---

# Instrument defects, found by reading ch4 against a marked proof

**Wendell, 2026-09-15: "You haven't earned enough trust for me to not have to do this
manually."** That is the correct posture until the rows below are closed. Every one of these
was found by a person with a highlighter, not by a board.

**Order is by damage, not by effort.**

---

## 1. `fragment.py` — the tier that was driven to zero is a tagger artefact

**The board said:** `Drawdown: fragment 54 -> 0 (1 rewritten, glossary excluded, rest ledgered)`.

**What is actually true:** run `python3 instruments/fragment.py -v manuscript/ch4.md` and read the
18 sites it reports. Among them:

```
MID   9w  ch4.md:263   A Line without a Reckoning lands as a request.
MID  12w  ch4.md:311   Stand fails by adding words in the four seconds after the line.
MID  15w  ch4.md:561   Every live moment sits somewhere on that axis, and where it sits
                       calls for judgment.
MID   9w  ch4.md:375   *That community deserves to be spoken about with accuracy.*
```

Every one of those has a subject and a finite verb. **They are complete sentences.** Reading
all 18 by hand, roughly 7 are genuine no-main-clause sites; the rest are the tagger mistaking a
past-tense verb for a participle, or losing the main clause behind a subordinator.

The file's own docstring concedes the mechanism: *"the whole design rests on aggregating 6,000
sentences to survive a tagger that is unreliable per instance."* That aggregate defence holds
for a **rate**. It does not hold for a **site list**, and the drawdown consumed it as a site
list.

**So `54 -> 0` did not measure fragments. It measured a tagger**, and the 33 ledger entries
record acceptances of findings that were substantially not findings. Meanwhile the real
fragments Wendell marked on pp.96-97 — `Slights.` / `Moments where...` / `To have conversations
about boundaries. To schedule dialogues. To bring in a facilitator.` — were shipping.

**Fix:** precision has to be measured before the tier is used for sites again. Take 100 sentences
the file calls fragments, adjudicate by hand, publish the number. If precision is below roughly
0.9 the tier reports a rate and nothing else, and any drawdown against it is withdrawn. A
specific suspected cause worth testing first: `VBD` mistagged as `VBN`, and no depth
decrement when a subordinate clause closes.

**Until then the ledger's 33 fragment acceptances are not evidence of anything** and should not
be cited as "reviewed".

---

## 2. `draft_lines.APPARATUS` — the frame is invisible to eight instruments

```python
APPARATUS = re.compile(r"^\s*(?:#{1,6}\s|\||>\s|[-*+]\s|\d+\.\s)")
```

A line opening `>` is classified *not prose*. Per `instruments/book/README.md`, **all five frame
devices wear a blockquote** — MARGINALIA, EPIGRAPH-BYLINE, HANDBOOK, POSTCARD, RECORDS. Verified:
`ch4.md:6` and `ch4.md:12`, the two epigraphs, both return `is_apparatus=True`.

**Eight instruments inherit it:** `trailing_and`, `telling`, `light_verb`, `polysyndeton`,
`slop_shapes`, `fragment`, `antecedent`, `presupposed` — every drawdown driven to zero.

**Unmeasured:** 7,446 words, 6.9% of ch1-ch9, carrying 51 trailing-and sites that
`trailing_and.py`'s own `joins_two_clauses` would report if it read them. The second sentence of
ch4 is one of them.

**Fix:** a frame mode, the way `marginalia/review.py` already has one. Boards report body and
frame separately rather than silently dropping the frame.

---

## 3. `dupes.py:82` — cross-file duplication cannot be seen

```python
if f2 != f or abs(n2 - n) > 400:
    continue
```

Same file only, within 400 lines. A paragraph shipping in three chapters is invisible by
construction. The polarity definition ships verbatim at `ch4:198` and `ch7:198` and one clause
apart at `ch5:245`; the board reports `0 pair(s) — clean`.

Running the same comparison with the guard removed: **14 cross-file exact pairs and 19 near pairs
in shipping text**, over 1,775 paragraphs. Most are deliberate per-chapter frames and should be
recorded as such; the polarity definition is not one.

**Fix:** a cross-file board, separate from the merge-twin board, plus exclusion of
`APPENDIX_C_KEY_TERMS_backup_*` which does not ship and accounts for 20 of the pairs.

---

## 4. `trailing_and.py` — two recall gaps, each hiding a marked site

**`SUBORDINATOR` swallows demonstrative `that`.** `...today's clothes, and that question is what
the whole chapter turns on.` The tail opens `that`, read as a subordinating conjunction. Here it
is a determiner on `question`. `DEMONSTRATIVE` covers `that` + copula, not `that` + noun + copula.

**`BARE_PREDICATE` cannot reach a verb behind a participial subject.** `...has finished, and the
hand holding the instrument escapes it.` Subject is `the hand holding the instrument`; the finite
verb sits four words in, past the window.

Both were marked by Wendell and both read `0` on the board. Both are bounded fixes.

---

## 4b. `compile.py --verify` passes over an unregistered frame block

Found 2026-09-16 while moving a paragraph into a MARGINALIA block in ch5. The block was written
into `manuscript/ch5.md` and not yet added to `marginalia/insertions.py`.

- **`--regen` caught it**: `ch5: frame kinds differ: 11 live, 10 held. REFUSED`.
- **`--check` said** `All anchors resolve`, because it checks the anchors insertions.py knows about.
- **`--verify` said** `Body text round-trips byte-identical and every frame block matches
  insertions.py` — true of the ten it compared, and silent about the eleventh.

**The hazard is data loss.** `--apply` writes only what `insertions.py` holds, so an unregistered
block is deleted the next time anyone applies the frame, and `--verify` reads clean until then.

`--verify` should compare counts as well as contents, the way `--regen` already does.

## 5. No board states its denominator

No line in `review.py` says what it scanned. `trailing_and 0` is a true and useful statement
about 93% of the book and is read as a statement about the book.

**Fix, and the cheapest one here:** every instrument prints its scope.
`0 findings in 11,015 of 12,055 words; 1,040 words of frame not scanned.` This retroactively
makes every past board honest.

---

## 6. Closed-by-acceptance and closed-by-repair render identically

`fragment 54 -> 0 (1 rewritten, ... rest ledgered)` and `light_verb 52 -> 0 (51 rewritten)` both
print as zero. They are not the same event.

**Fix:** split the board.

---

## 7. Nothing fires on commit

`shipcheck.py` and `review.py` both print it themselves. A sequence that runs when somebody
remembers runs when somebody wants a green board.

---

## What a sweep is allowed to do, pending the above

The ch4 pass produced three cases of a drawdown damaging prose it could not read:

- **`a8db0ca`** deleted `was the one who`, a copula that was the antecedent for the next two
  sentences, leaving `Who said... Who stood...` orphaned. The telling pass reads one sentence at
  a time.
- **`a8db0ca`** rewrote one shared boilerplate sentence two different ways across chapters:
  `How big does the charge run` in ch4, `feel` in ch5, ch6, ch7. Parity that existed before the
  sweep does not exist after it.
- **`40077a6`** split `gets braced against, and it should be named` into two sentences and left
  both agentless passives standing. Wendell wrote *"By who?"* on that exact line.

- **`a8db0ca`** replaced two copulas and took the nouns with them. `It is a request you haven't
  stopped making yet. It is the hope that someone will respect your line...` became `It keeps
  asking past the point where you meant to stop. It hopes someone will respect your line...`
  Naming the thing is what the sentences were for, and the pass left the payoff orphaned: *"Hope,
  in the domain of boundaries, is not a strategy"* lands on a noun the previous sentence no longer
  supplies. **This is the say-the-noun failure that `marginalia/review.py` already has as its own
  BLOCK category** — one instrument manufactured a defect another instrument exists to catch, and
  neither board noticed.

- **`40077a6`** de-passivised `I was told that at nineteen, by people who meant well, and I
  believed them...` into `I was nineteen when people who meant well told me that. I believed
  them...` The de-passivising was right; the result pushed the demonstrative `that` four words
  further from the list it refers to and wrapped the sentence in a clumsy temporal frame. A
  correct rule, applied without reading, produced a worse sentence.

**Proposed rule:** a sweep that rewrites more than some threshold of sites gets a sampled read
before it commits. The telling pass changed 491 lines across nine chapters with no recorded read.
