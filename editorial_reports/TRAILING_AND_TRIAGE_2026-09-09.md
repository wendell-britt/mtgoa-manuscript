# trailing_and triage — what 775 actually is

**Ruled 2026-09-09** by a six-Face pass (cast seed 5182, 62 → 31): *"Triage MTGOA's `trailing_and`
by sample, not by grind. If the false-positive rate matches Flirtcraft's, most of that number is
regex and the honest resolution is a rule in the ledger, not 775 rewrites. **You do not currently
know which, and that is the cheapest thing to learn.**"*

Sample of **100 of 769 unique keys**, drawn with `random.seed(775)` so it is reproducible.
Classified by reading each one.

---

## The answer

| | share | of 775 |
|---|---|---|
| **genuine loose coordination** | **63%** | ~488 |
| regex over-catch | 35% | ~271 |
| ambiguous, needs the full line | 2% | ~16 |

**The Challenger's hypothesis was wrong and it was worth testing.** Flirtcraft ran at ~83%
over-catch; MTGOA runs at 35%. **Roughly 490 sentences in this book are genuinely two independent
clauses joined by a bare `and` with the relation left unnamed.** No ledger rule dissolves that.
It is a voice pattern in a book near launch.

---

## The over-catch, broken out — because four of the seven classes are fixable in code

| class | in 100 | example | fixable? |
|---|---|---|---|
| **serial lists** — predicates, appositives, noun series with an Oxford comma | 13 | *It surfaces what each party protects, names stakes and sacrifices honestly, and closes toward terms people can accept* | hard |
| **coordinate subordinate clauses** — two `that` / `because` / `why` clauses, not two sentences | 7 | *Skill earns one because it improves, and because you can carry it somewhere else* | **yes** |
| **shared-subject compound predicates** | 5 | *A hull that treats every century as the dangerous one never misses a threat, and never has to work out which threat is here* | **yes** |
| **non-`and` conjunctions** — `but`, `or`, `so` | 3 | *The move costs something, but it returns capacity* | **yes** |
| **reflow / apparatus artifacts** — glossary entries, keys starting mid-sentence | 3 | *it, and that person will not have been selected.* | **yes** |
| **quoted or italicised speech** | 2 | *here is why this keeps breaking, and here is how to redesign it* | hard |
| **deliberate anaphora** | 2 | *So it reads, and reads, and never gets to speak.* | hard |

**The four fixable classes are 18 of 100 — about 140 sites of the 775.** Tightening the instrument
removes them at no cost to the ledger, the same way `polysyndeton`'s subject test was tightened
when it was over-matching plural nouns as verbs.

## The mismatch inside the instrument

`trailing_and.py`'s own docstring carries the argument for the zero target:

> **`and` represents no relation.** Every other connective commits — `because` to cause, `once` to
> sequence, `though` to concession. `and` says only *here is another one*, so reaching for it is
> declining to say how two ideas relate.

**And then its regex counts `but`, `or`, `so` and `yet`** — every one of which commits. `but` names
concession, `or` names alternative, `so` names cause. By the instrument's own reasoning those are
not defects, and they are ~7% of the sample.

Strunk's Rule 14 does cover loose sentences generally, so counting them is not wrong *on Strunk's
terms*. But the zero target was not justified on Strunk's terms — it was justified on the
relation-naming argument, and that argument exonerates four of the five conjunctions the regex
matches. **The rationale and the pattern disagree, and the number inherits the disagreement.**

## What this means for the 775

**Ledgering ~271 false positives one at a time is the wrong move**, and it was the plan before this
sample existed. Three steps instead, in order:

1. **Tighten the instrument** on the four mechanical classes — coordinate subordinate clauses,
   shared-subject predicates, non-`and` conjunctions, reflow artifacts. Expect 775 → ~630.
2. **Rule on `but`/`or`/`so`/`yet`.** A voice decision, not a code decision: either the regex
   narrows to `and` and matches the docstring, or the docstring is rewritten to Strunk's broader
   claim. **It cannot stay as it is.**
3. **Then the ~490 genuine sites are a launch decision**, chapter by chapter, and they want the
   per-chapter targets the Regent asked for. `ch8` and `ch3` carry the most in this sample.

## What the sample says about the prose itself

Read as prose rather than as counts, the 63% is one habit with a clear shape: **a claim, then its
consequence, joined by `and`.**

> *That voice is a memory, and it reports accurately.*
> *It arrives with a condition, and the condition sounds responsible.*
> *Those are the owners, and keeping that shelf stocked is how they collect.*
> *That is a judge now, and it holds court in you.*

Every one of those is two beats where the second lands the point, and in every one the `and` is
standing where a full stop would hit harder — the same finding as chapter 1 of the AI Psychologist,
where 21 of 22 rewrites were exactly this move. **It is a consistent, mechanical, and highly
repairable pattern.**

---

# Re-triage on the new 789 — after v20 and v21

The population changed twice since the first sample: **v20** narrowed the regex to `and` and
tightened three over-catch classes; **v21** fixed the apparatus filter, which put MTGOA's entire
glossary and every `**Term** — …` line into scope for the first time. A fresh sample of 100,
`random.seed(789)`, classified the same way.

## The answer

| | first triage (775) | now (789) |
|---|---|---|
| **genuine loose coordination** | 63% · ~488 | **88% · ~694** |
| regex over-catch | 35% · ~271 | **10% · ~79** |
| ambiguous | 2% | 2% |

> **CORRECTED 2026-09-09.** This table first read 84% / 14%, because I filed *coordinate objects*
> — `The view has four domains, and one cheap habit that is none of them` — as a regex over-catch
> and proposed tightening the instrument to stop flagging them. **Wendell: *"this is no good."***
> He is right, and it inverts the recommendation: the construction is a defect, the instrument is
> correct to flag it, and four points move from over-catch to genuine. See below.

**Over-catch fell from 35% to 14%.** And the four classes the tightening targeted — coordinate
subordinate clauses, shared-subject compound predicates, non-`and` conjunctions, split artifacts —
appear **zero times in the new sample.** They are gone, not merely reduced.

**The genuine count went up, from ~488 to ~663.** Both causes are real and they pull the same way:
precision improved, and roughly 180 sentences that had never been scanned entered the corpus. **The
number got worse because the instrument got honest.**

## What the remaining 14% is

| class | in 100 | example |
|---|---|---|
| **serial lists** — appositives, three-clause series ending in `and` | 5 | *the auditor that makes your no expensive, the judge that audits your standing, and the one breaking…* |
| **quoted scripts, paired questions, interior voice** | 4 | *Who is coming after me, and what do they actually need?* |
| **fragment head** — a verbless first half | 1 | *Twenty cards, and these are the Regent's.* |

**Coordinate objects are a DEFECT class, and the instrument should keep flagging them.** I had this
backwards. `The X has four domains, and one cheap habit that is none of them` is one verb with two
objects, and the comma-and reads as a clause boundary that is not there — worse, **`and` announces
another item of the same kind while the clause it introduces says *none of them*.** A fifth thing is
added and excluded in the same breath.

It was a refrain across six chapters, identical in each. Now:

> ~~The view has four domains, and one cheap habit that is none of them.~~
> **The view has four domains. One cheap habit imitates them and is none of them.**

*Imitates* is not invented for the repair; every one of the six paragraphs goes on to say it —
*"it looks exactly like taking the problem more seriously"*, *"it feels almost identical to courage
from the inside."* The refrain survives, in all six.

The other three classes are the ones the first triage already called hard, and they are hard for the
same reason: telling a deliberate series from a loose join needs a reader.

## What this changes about the plan

Step 1 of the first triage is **done** and slightly over-delivered. Step 2, the `but/or/so/yet`
ruling, is **done**. Step 3 stands, with a bigger number under it than before:

**~663 genuine sites, and one habit.** The re-sample confirms the shape the first one found — a
claim, then its consequence, joined by `and` where a full stop lands harder:

> *That part has a name, and you have met it before.*
> *That is burnout, and every step of it is you playing hard.*
> *It does not cover the case, and that is the point.*
> ~~The council had the right words, and the right words were the wall.~~
> **The council had the right words. The right words were the wall.**

I argued for keeping that one on the grounds that the repetition was the pivot. **Wendell: *"this
one shouldn't stay."*** Splitting it keeps the repetition and sharpens the pivot, so the defence was
wrong on its own terms — and it was a taste claim I had no standing to make, one message after
writing down that ranking sentences is not mine to do.

**The lesson the two corrections share:** I reach for *"the instrument is over-catching"* and
*"this one earns its place"* at exactly the moments a sentence looks odd and I have not worked out
why. Both times the odd-looking sentence was simply bad.
