---
type: ruling
title: "The Effective Allyship Formula — five steps"
aliases:
  - the formula
  - effective allyship formula
tags:
  - course
  - mtgoa
  - canon
created: 2026-08-18
review: 2026-09-01
source:
  - course/SURVEY_SUBSTRATE_2026-08-18.md
  - bars-engine src/lib/technique-library/canonical-operations.ts
---

# The Effective Allyship Formula — five steps

**Wendell, 2026-08-18, three rulings:**

> *"This needs another step which would include working through any blocks to showing up with
> that superpower."*
> *"the formula will enter the book in a later printing"*
> *"The course is self paced and there is a live version that works through the material as well"*

---

## 1 · The fifth step is not an addition. It is the missing Clean Up.

**With the new step in place, the Formula is the Five-Move Form run at campaign scale.** One step
per move, in the Form's own order:

| # | the Formula | the move | what the book already says the move does |
|---|---|---|---|
| 1 | **Identify your superpower.** | **Wake Up** | *"You sit with the sadness. You let your body feel it."* — notice what is actually true, in the body, before deciding anything |
| 2 | **Identify who needs that superpower.** | **Open Up** | *"You stop bracing and let it reach its real size — including whatever is tangled up with it that you would rather not find."* |
| 3 | **Work through what blocks you from using it.** | **Clean Up** | *"You ask: What am I grieving? You let the answer come."* — name what is actually there |
| 4 | **Enroll allies to help you help those people.** | **Grow Up** | *"You integrate… That's true even though it hurts."* — take on the capacity the situation asks for |
| 5 | **Show up consistently.** | **Show Up** | *"You take action to protect what's still here."* |

Move glosses quoted from `appendices/APPENDIX_C_FIVE_CHANNELS.md:70-74`, the worked Water pass.

**So the four-step version was missing the move the book spends the most instrument on.** Clean Up
owns Appendix C's five channels, Appendix D's alchemy practices, Appendix E's 3-2-1, and the
shadow work in every Face chapter. **A four-step Formula skipped all of it**, which is why the
gap was felt from the outside before it was located. The engine's own tagging shows the same
shape: `canonical-operations.ts` tags the Formula `moves: ['grow_up', 'show_up']` — the last two
only.

**This is the strongest available argument for the later printing.** The Formula is not new
material bolted onto a finished book. **It is the book's own spine, stated as a sequence a person
runs rather than a practice a person learns.** A reader who owns the first printing already has
all five moves; what the printing adds is the name for what they are for.

## 2 · The wording of step 3

**Proposed:** *"Work through what blocks you from using it."*

Matches the other four — imperative, one clause, no jargon. **Gate clean:** no banned word, no
sentence-initial *And*/*But*, no stack, no em-dash collision. Wendell's own phrasing was *"working
through any blocks to showing up with that superpower"*; this is that, tightened to the register
of its four siblings.

**The alternative worth considering:** *"Clean up what blocks you from using it."* It makes the
mapping legible in the words themselves, and the capitalisation rule permits it — a move name is
lowercase when the sentence tells you to do it. **The cost is that it teaches the mapping before
the reader is ready to see it**, and the concealed architecture has been protected everywhere
else. Recommend the neutral version in the Formula and let the mapping be discovered.

**Not yet reviewed for the manuscript.** This is the course's working wording. Entering the book
means the full `mtgoa-review` pass on whatever prose introduces it, not just the step itself.

## 3 · What the five steps do to the course

**Five steps, five modules, one artifact each.** The Formula stops being a spine and starts being
the syllabus:

| module | ends when the learner has | already exists |
|---|---|---|
| 1 · your superpower | their Face named, and the one they avoid | **nearly shippable** — the quiz, `SUPERPOWER_DEFS`, the result email, the character sheet |
| 2 · who needs it | **actual people named**, not categories | the four domains, Appendix A, Appendix B quests |
| 3 · what blocks you | one block worked, by 3-2-1 or a channel pass | Appendices C/D/E, `emotional-first-aid`, the alchemy engine |
| 4 · enrolling allies | one real ask made of one real person | `introductions.ts`, the consent gate — **but every surface is single-player** |
| 5 · showing up | a cadence that survived a missed week | BARs, the deck, `ThreadProgress` |

**Module 3 is the one that changes the completion problem.** The 2020 course finished under ten
percent. A course whose middle module is *work one real block* has a different failure mode than
one whose middle module is *watch four videos* — and the book's own claim is that the block is
what stops people, not the information. **Module 3 is where the course either proves that or
does not.**

## 4 · Self-paced plus a live version

**Ruled: both, running the same material.** That answers the survey's §5.2 and it resolves the
step-3 problem — enrollment needs a second human, and the live version is where the second human
is.

**The design consequence, stated plainly: the two versions must not be two products.** The live
cohort works through the same five modules, so the material is authored once and the live version
is a *facilitation layer over it* rather than a parallel curriculum. Anything authored only for
live is content the self-paced learner is missing; anything authored only for self-paced is
content the room has to improvise around.

**What the split gets you, per module:**

- **Module 4 works live and is hard alone.** Enrolling an ally in a room where somebody will ask
  you next week whether you did it is a different act from enrolling one in private.
- **Module 5 needs someone who notices you stopped.** That is the live floor, or the Dojo, or it
  is nothing. **No lesson platform supplies it**, which is worth remembering when the tooling
  research starts.
- **Modules 1–3 work self-paced** and are where the artifact model carries the weight alone.

**The open question this ruling creates:** does a self-paced learner get a path into the live
floor at module 4, or does the self-paced version have a different answer for enrollment? Those
are different products at the price level. **Not ruled, and it is the next thing to decide.**

## 5 · What changes in the engine

**One canon edit, and it is small.** `src/lib/technique-library/canonical-operations.ts`,
`tech-allyship-formula`: add step 3 to `steps`, and widen `moves` from `['grow_up', 'show_up']` to
all five. **The `essence` line also needs a look** — it calls this *"the book's master four-step
procedure"* for a book that does not yet name it, and the count is now wrong twice over.

**Deliverable as a patch**, the same way `0001` and `0002` went across, since `bars-engine` cannot
be pushed to from a manuscript session.
