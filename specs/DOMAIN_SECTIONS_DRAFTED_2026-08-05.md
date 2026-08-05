# The five domain sections, drafted — what the set shows

**2026-08-05.** ch4 written and reviewed here, ch5–ch8 fanned out in parallel per
Wendell's instruction. Template: `ch3:810`–`:896`. Brief and findings:
`specs/REVIEW_DOMAIN_SECTION_CH4_2026-08-05.md`.

| | Face | the noun | goes after | words | insertion verified |
|---|---|---|---|---|---|
| ch4 | Challenger | **the Line** | `ch4:708` | 1,128 | yes |
| ch5 | Regent | **the Inheritance** | `ch5:613` | 1,386 | yes |
| ch6 | Architect | **the Design** | `ch6:530` | 1,374 | yes |
| ch7 | Diplomat | **the Close** | `ch7:692` | 1,360 | yes |
| ch8 | Sage | **the View** | `ch8:683` | 1,351 | yes |

**6,599 words.** ch3's is 1,980, so the set roughly quadruples the book's four-domain
practice material. All five: `gate` PASS · `fragment` clean · `preempt` clean.

| | be | copula | waste | zombie | expletive | passive | empty | inchoative |
|---|---|---|---|---|---|---|---|---|
| ch4 | 0.75 | 1.19 | 1.03 | 0.94 | **1.60** | 0.57 | 0.76 | 0.00 |
| ch5 | 0.74 | 1.19 | 1.20 | 0.96 | 0.76 | 0.93 | 0.72 | 0.00 |
| ch6 | 0.61 | 0.90 | 0.99 | 1.16 | 0.73 | 0.47 | 0.52 | 0.00 |
| ch7 | 0.61 | 1.13 | 1.04 | 1.03 | 0.72 | 0.00 | 0.78 | 0.00 |
| ch8 | 0.98 | 1.21 | 0.96 | 0.34 | 0.77 | 0.24 | 0.42 | 0.00 |
| **ch3, control** | 0.86 | 1.16 | 0.87 | 0.87 | 1.14 | **1.79** | **1.58** | **1.68** |

**ch4's expletive 1.60 is the only heavy counter in the set**, and it is two
sentence-initial occurrences: the anchor-1 turn *It is only more satisfying*, and ch3's
own *It is also the easiest thing in the world to lie to yourself about*, carried into
all five so the sections read as a set. Ruled and kept.

**Measuring against the control was load-bearing.** ch3's shipped template runs heavy on
passive, empty and inchoative; the book baseline alone would have called it a defect
three times. Three of the five drafts opened above the control on passive (ch5 1.98, ch7
2.21, ch6 waste 1.40) and **all three were rewritten rather than ruled inherited**, which
is the right call: a class the control also fires does not license every instance of it.

---

## 1 · The instrument gap, and it invalidated a reading in every report

`gate.py` globbed the manuscript and discarded any path handed to it. **Three of the five
drafts reported GATE PASS on a reading of the shipped book; measured properly they had
fifteen hits.** Recorded in full in the ch4 review. Fixed the same day.

Two of the five agents caught it independently and worked around it by importing
`gate.score`. Neither was told to. **The instrument was the weakest link, not the
process.**

The fifteen:

- **`room` ×12 and `quietly` ×2**, both banned, and **neither word appears once anywhere
  in the manuscript.** The book says *the table*, *the meeting*, *where it gets decided*.
  Four agents reached for a word the book has never used, which is what a banned list is
  for.
- **One `stacks` hit, mine**, in the very move written that morning to repair F1:
  *not a line, a note. Not now, later. Not you, somebody closer to it.* Three stacked
  fragments carrying claims mid-paragraph — a beat-placement violation as well as a gate
  failure. Recast as one sentence.

---

## 2 · The finding the set produced that no single section could — **needs a ruling**

**All five read their parable as Skillful Organizing. ch3's canon reads its own as Direct
Action.** So the callback opens on the same domain five chapters running.

Nobody was told which domain to pick and no two agents could see each other's work. Each
quoted its parable:

| | the quote it worked from | how solid |
|---|---|---|
| ch4 | `:70` *the Challenger would speak first at councils* | solid |
| ch5 | `:78` *the roles that passed from person to person, so that when one person left, the role stayed* | **solid, unarguable** |
| ch6 | `:68` *design the meeting format… build the role that made accountability real* | **solid, unarguable** |
| ch7 | `:69` *surfaced what each side protected and named what staying would actually require* | **contestable** — this is also ch7's own Direct Action gloss, *the terms said to the person they bind* |
| ch8 | `:77` *name which game the meeting was really playing… the village would pause* | **contestable** — also reads as Raise Awareness, *the real agenda said out loud at the table running it* |

**Three of the five are simply correct and it is not a convergence artifact.** Every
Section 1 parable is a Face inside a village, so the structural domain is genuinely what
most of them show. **The pattern is real. Whether it is readable five times is the
question**, and it belongs to Wendell.

Three ways out, in ascending cost:

1. **Leave it.** The repetition is honest and each callback names a different mechanism.
2. **Re-read ch7 as Direct Action and ch8 as Raise Awareness.** Both are defensible on
   the same quotes; two callbacks and two opening sentences change, nothing else.
3. **Have the callback name the domain the parable shows *and* the one the chapter's
   Section 5 shows.** More words in every section, and it makes part 1 do two jobs.

**Option 2 is the recommendation.** It costs the least, it is honest to both quotes, and
it puts three different domains in five openers.

---

## 3 · What the fan-out proved about the template

**The template survives being handed to five different writers with no shared context.**
Every variable slot varied and every fixed slot held:

| slot | ch3 | ch4 | ch5 | ch6 | ch7 | ch8 |
|---|---|---|---|---|---|---|
| the noun | Read | Line | Inheritance | Design | Close | View |
| part 3's turn | *You practiced it.* | *described* | *maintained* | *drafted* | *rehearsed* | *mapped* |
| the Tell's verb | *said* | *drew* | *kept* | *built* | *closed* | *named* |

**One collision, caught by measuring the set rather than the section:** ch6 closed part 3
on *You drew it*, and ch4's entire section is built on drawing — its noun is the Line, its
heading is *How to Draw It So It Holds*. Two chapters apart, the same verb does different
work in each. Changed to **You drafted it.**

**Each section built its three universal moves on three of its own chapter's five stages**,
which nobody specified — the brief only said *drawn from the chapter*:

- ch4: **Charge · Aim · Stand**, from `Charge → Aim → Act → Stand → Exit`
- ch5: **Inherit · Steward · Entrust**, from `Inherit → Honor → Steward → Reform → Entrust`
- ch6: **Observe · deploy · Hand Off**, from `Observe → Model → Design → Deploy → Hand Off`
- ch7: **Translate · Negotiate · Repair**, from `Bridge → Translate → Hold → Repair → Negotiate`
- ch8: **Switch · Serve · Return**, from `See → Switch → Serve → Release → Return`

**That is the strongest evidence the sections belong to their chapters** rather than being
five copies of one form.

---

## 4 · Open, and all three are Wendell's

1. **The Skillful Organizing repetition.** §2 above. Recommendation: option 2.
2. **First person.** `VOICE_ANCHOR` records that three of its five passages carry the
   admission inside the teaching, and 6,599 new words of instruction carry none.
   **ch7's section has one**, sourced entirely to `ch5:314`–`:322` — *I held back some of
   what I knew. I wore the crown under my hood* — re-read from the Diplomat's side. It
   invents no biography; the only new material is the interpretation. **It lifts cleanly
   if it is not wanted.** ch5's, ch6's and ch8's agents all declined to write one
   unauthorised rather than invent, and all three named where one would sit.
3. **Length.** Four of five came in at 1,350–1,390 against a 1,100 target. Each named its
   own cheapest cuts and each said the overage is in the four three-part markers, which
   the spec forbids shortening to two parts. **Either the target moves to ~1,350 or the
   marker form gives**, and the marker form is the part §4 of the spec calls unskippable.
