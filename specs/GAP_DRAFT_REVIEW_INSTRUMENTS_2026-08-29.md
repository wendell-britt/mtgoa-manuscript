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
  - .claude/skills/mtgoa-review/SKILL.md
  - marketing/KDP_LISTING_2026-08-29.md
---

# Why the review passes prose Wendell then catches by eye

**Wendell, 2026-08-29:** *"how are our skills not catching this? Make a note that we need to solve
for this."*

**A note with a diagnosis, not a plan.** The KDP description went through the review, came back
`clean`, and he then caught six separate defects in it by reading. That happened four times this
month. **This is why, checked against the code rather than reasoned about.**

---

## The finding, in one line

**Four instruments already exist for exactly the patterns he keeps catching, and none of them can
read a draft file.** They are hardcoded sweeps over `manuscript/ch[1-9].md` and none is wired into
`review.py`.

## What he caught, and which instrument should have caught it

| his catch, 2026-08-29 | the instrument that exists for it | why it stayed silent |
|---|---|---|
| *"fragments are bad. I speak in complete sentences"* | **`fragment.py`** — written for this, and its own docstring says *"Wendell has caught it by eye twice"* | Not in `review.py`. Cannot take a file |
| *"what person? what is it? We're handwaving again"* | **`antecedent.py`** — written for this, after *"We are REALLY bad at this 'it' thing"* | Not in `review.py`. Cannot take a file |
| *"'that was never what was missing' — classic slop"* | **`notstack.py`** | Not in `review.py`. No argv handling at all |
| *"which is the training nobody gets"* | **`faux_insight.py`** — the pattern is in its docstring by name | Not in `review.py`. No argv handling at all |
| *"'the noise of doing the work' — what is 'this work'?"* | `empty_head.py`, which **is** wired | Its `EMPTY` list has no entry for `work`. See below |

**Five catches, four of them covered by an instrument that was built for the exact defect.**

## Verified, not assumed

```
$ grep -o "instruments/[a-z_]*\.py" instruments/review.py | sort -u
citation_audit  copyedit  dupes  emdash  empty_head  gate
prose_diet  ranking  seam_sweep  voice_surfaces  xref
```

**`fragment`, `antecedent`, `notstack` and `faux_insight` do not appear.**

```
$ python3 instruments/fragment.py SOME_DRAFT.md
… manuscript/ch8.md:728 … back_matter/glossary.md:112 …
```

**It ignored the argument and scanned the book.** `fragment.py` and `antecedent.py` read `-v` and
`--write` off `sys.argv` and have no FILE branch. `notstack.py` and `faux_insight.py` reference
`sys.argv` zero times and glob `manuscript/ch[1-9].md` at import.

## Three separate causes, and they need different fixes

**1 · The instruments were built as sweeps, not as checks.** Each one was written to clean the
manuscript once, ran, found its sites, and was fixed. **A sweep is a job; a check is a habit**, and
nothing converted them. The five always-on constraints in `REVISION_INSTRUMENT.md` Part 1 are
supposed to be always on, and `fragment.py` opens by saying it is the fifth of the five — so the
gap is not that nobody knew.

**2 · `review.py` step 3 is the only step on the honour system.** Every other step runs code. Step
3 prints:

```
8 slop    run /no-ai-slop by hand, then re-run this
```

**And that is the step that keeps failing.** It failed by omission on 2026-08-29 (`KDP_LISTING`
correction — I ran one check out of one file and called it the step), and it fails by degree every
time, because a human reading is not repeatable. **Four of the five catches above are patterns
`no-ai-slop` names in text — so wiring the four instruments in is the same as making step 3 partly
mechanical.**

**3 · `empty_head.py`'s vocabulary is too small.** The `EMPTY` list is
`thing / something / version / stuff / way / part / aspect / element / area / piece / room` and
their plurals. **It does not contain `work`**, which is the word he caught, and it does not contain
the family around it: `process`, `practice`, `approach`, `system`, `space`, `level`, `point`,
`issue`, `situation`, `experience`, `material`, `dynamic`, `factor`, `context`. Each of those takes
a definite article and names nothing.

**The list grew by anecdote.** `room` went in because he said *"I'm starting to hate the word
'room'"*; `thing` the same way. **Growing a blocklist one complaint at a time guarantees it lags
the complaints**, which is the shape of the problem rather than a criticism of the list.

## What solving it looks like, cheapest first

**1 · Give the four instruments a FILE argument and wire them into `review.py`.** `empty_head.py`
and `gate.py` already have the pattern to copy — a `FILES` list that takes `sys.argv[1:]` when
present and globs the manuscript otherwise. **This is an afternoon and it closes four of the five
holes**, and it is the only item here that would have caught the fragments before he did.

**2 · Widen `EMPTY` by category rather than by anecdote.** Add the abstract-noun family in one
pass, measure the manuscript, and accept a higher soft count rather than tuning the list down to
where the book already sits. **Report only, as it does now**, so a wider list cannot block a build.

**3 · Make step 3's report name what it checked.** The step should print the list of `no-ai-slop`
patterns and require an explicit verdict per pattern, so *"I ran the fabrication check"* cannot be
recorded as *"I ran step 3."* **The failure mode is naming a fraction after the whole**, and the
remedy is a checklist that shows its own gaps.

**4 · Leave the eye in the loop.** None of the above would have caught *"the noise of doing the
work"* → *"the noise of seeming like you're doing a good job."* **The instruments find candidates;
the judgement about which noun a reader can point at is his.** The goal is to stop spending his
reading on the four mechanical patterns so it lands on the fifth.

## The honest scope of this note

**It does not fix anything.** It records a diagnosis he asked for, with the code checked rather
than recalled, so that the fix can be scheduled against the print deadline rather than instead of
it. **Nothing here gates the proof copy**, and the KDP description is clean under the pass as it
stands plus the manual reading he did.
