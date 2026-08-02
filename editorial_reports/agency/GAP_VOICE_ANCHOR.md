# Gap analysis — why the voice canon produces unearned agency, and how to fix it

**Ruled by Wendell, 2026-08-02:** the voice canon is not a shield for the village
construction. The voice must make the work better, not hold it in unworkable patterns.

This document diagnoses **how** the voice system produces the defect and proposes the
repair. It changes no prose and amends no canon; C2 reserves that to Wendell.

---

## The finding in one sentence

**`VOICE_ANCHOR.md` names the effect each passage protects and never names the mechanism
that produces it — so anyone matching the anchor, human or agent, copies the mechanism
along with the effect, and at anchor 3 the mechanism is reified agency.**

This is not an accident of one badly-chosen passage. The Jerk archetype's own targeting
rule creates grammatical pressure toward the defect. The voice system manufactures it.

---

## Gap 1 — the anchor protects effects, not mechanisms

Every anchor carries a `**Protects:**` line. All five name an *effect*:

| # | passage | Protects (effect) | mechanism actually used | agency-safe? |
|---|---|---|---|---|
| 1 | ch1:10 | ending heavy on something small and dry | first person; *I* holds every verb | ✅ |
| 2 | ch1:119 | naming your own bad prose inside good prose | first person, parenthetical | ✅ |
| 3 | **ch4:115** | **the humor** (Jerk archetype) | **collective-as-mind: the village *learned*, the workshops *teach*** | ❌ |
| 4 | ch5:516 | named interior parts treated as people | named part — Grade 2, licensed, mechanism in canon | ✅ |
| 5 | ch8:342 | compression as argument | *the view*, *the triumph* — no agent claimed | ✅ |

Four of five anchors deliver their effect through a subject that can hold a verb. One
does not. And because the anchor is explicitly *"a comparison set, not a style
checklist"* — quoted at paragraph length with no marking of which span is load-bearing —
**everything inside the quotation reads as canonized.** A writer matching anchor 3 has no
way to know that the humor is protected and the collective subject is incidental.

**Repair:** every anchor gets a second line, `**Delivers via:**`, naming the mechanism —
and the load-bearing span gets marked inside the quotation. An anchor that names only its
effect licenses whatever produced it.

---

## Gap 2 — the Jerk archetype's targeting rule creates the pressure

The anchor defines the Jerk as *"mocking the process that took someone's joystick, never
the person."*

That is a **targeting rule**, and it is correct — the book must not mock the reader or
the people in its examples. But satire needs a target in the subject slot. If the person
is forbidden there and no other licensed carrier is named, **the process arrives as the
subject by default.** The archetype forbids the only obvious agent and supplies no
replacement.

That is the whole mechanism. It explains why the defect concentrates in exactly the
passages the book is proudest of, why the most-revised chapter (ch3) carries it, and why
it survived every existing gate.

**The fix is already inside the anchor set.** Anchor 4 is *also* the Jerk archetype —
it mocks a process, the endless repair — and it delivers the mockery through a named
part:

> *"More than once, I have watched myself hand him to the Fixer. **The Fixer is happy to
> take him.**"*

The Fixer is Grade 2. Licensed for intention, mechanism in canon, and the line is funnier
than anchor 3 because the agent is specific. **Anchor 4 does anchor 3's job without
anchor 3's cost.**

**Repair:** the Jerk archetype gets a completion clause. Mock the process, never the
person — **and seat the mockery on a subject that can hold the verb.** Four licensed
carriers, in order of preference:

1. **a named part** (Grade 2) — the Fixer, Mr. Inadequate. Funniest, most specific.
2. **the author's chair** (Grade 1) — *I wrote whole chapters standing at it.*
3. **the persons, plural** (Grade 1) — the villagers, the trainers, the people in the room.
4. **a machine, mechanical verbs only** (Grade 4) — *the structure pays out nothing for optics.*

---

## Gap 3 — no role in the stack asks who holds the verb

`VOICE_ANCHOR.md:96–99` gives the Guardian its rubric: *specificity, rhythm, authority,
emotional temperature, natural syntax.* Nothing about agency.

Lines 101–103 then state that the gate, `prose_diet.py` and `/no-ai-slop` **do not do
this job** — the Guardian is the sole authority on liveness.

So: the instruments count things and cannot see agency; the Guardian sees liveness and is
not asked about agency. **A reified sentence that is specific, rhythmic, authoritative,
warm and naturally-syntaxed passes every check in the system.** That is how 131 sites
accumulated in a manuscript with four linters and a green gate.

`prose_diet.py:91` does carry an `AGENT` regex — 22 nouns × 18 verbs, commented *"a
candidate finder rather than a counter"* — and `MANIFEST.md` reports it firing 25 times.
It found roughly a fifth of what is there and nothing in the stack was obliged to act on it.

**Repair:** add one question to the Guardian's rubric — **who holds the verb?** — ruled
in the same sentence as the other five. Not a new instrument. A sixth word in an existing
sentence.

---

## Gap 4 — the anchor set has no negative space

Five passages showing the register at its best, and nothing showing the register at its
worst. The file's own logic explains why this matters: *"an anchor with no comedy in it
will let the Voice Guardian approve a book that has stopped being funny, because nothing
in its comparison set would show that anything was lost."*

The same argument applies in the other direction. An anchor set with no failure in it
lets the Guardian approve prose that has stopped being **traceable**, because nothing in
its comparison set shows that anything was lost.

**Repair:** add one **counter-anchor** — a passage that scores well on all five existing
criteria and fails on agency. `ch7:138` is the ideal candidate, because it is the
chapter's own definition of its own key term:

> *"a term is a statement… offered as information, once, to a field that is then free to
> answer."*

Specific, rhythmic, authoritative, warm, naturally-syntaxed. And the field answers.

---

## The repair that costs the least prose: change the number, not the sentence

The audit's default remediation was **R1 — restore human agent**, which fired 96 times
and carries C5's scolding guard. R1 is the wrong primary op for the fables, and there is
a cheaper move that no R-op in the spec covers.

In the fables, *the village* is not a Grade 6 pattern at all. It is **a fictional
population**. Its members are persons. So the repair is often not a rewrite — it is a
**number change**:

| current | repaired | what changed |
|---|---|---|
| The village **learned** to make its nos sound like yeses because yeses cost less. | The villager**s** learned to make **their** nos sound like yeses because yeses cost less. | plural |
| The village **had made a rule**: if you can see the pattern of the game, you must stop playing. | The villager**s** had a rule: if you can see the pattern of the game, you must stop playing. | plural |
| The village **forgot** that the Faces were a map, not a menu. | The villager**s** forgot that the Faces were a map, not a menu. | plural |
| The village **became afraid** of conflict the way a body becomes afraid of a low-grade fever. | The villager**s** became afraid of conflict the way a body becomes afraid of a low-grade fever. | plural |

The turn survives in every one. *Yeses cost less* · *you must stop playing* · *a map, not
a menu* · *a low-grade fever.* The rhythm moves by one syllable. The fable conceit is
untouched. The humor is untouched. And the subject becomes Grade 1 persons, which is
licensed for everything.

**It is not R1**, which is why it does not drumbeat. R1 restructures a sentence into
*people did this to each other*. This changes a suffix. Ninety-six R1s were never
ninety-six restructurings — most of them were this.

**Proposed as R8 — pluralize the collective.** Precedence: above R1, below R4.

### Where the number change is not enough

Roughly one site in five needs real work. The hard shape is a village that **possesses**
its members, because pluralizing produces a group acting on itself:

> ch4:127 — *"it taught its people that the clean no no longer belonged to them"*

*The villagers taught their people* is nonsense. This needs generational transmission —
*one generation taught the next that the clean no was not theirs* — which is R6, dissolve
to transmission, and which is also **more true**.

> ch3:316 — *"The village trains everyone to turn feeling down. It hands you a dial in
> childhood and teaches one direction: lower it."*

Same problem: the villagers cannot train everyone, because they are everyone. The repair
is compression — drop the abstract first sentence, keep the concrete second: *The
villagers hand you a dial in childhood and teach one direction: lower it.* The turn,
*lower it*, is untouched, and the paragraph gets shorter, which anchor 5 rewards.

---

## What this does to the audit's numbers

If R8 carries the fables:

- **R1 drops from 96 to roughly 25**, and the scolding risk that was the audit's central
  execution problem mostly disappears.
- The village work stops being a rebuild of five fables and becomes **a suffix pass plus
  ~20 real rewrites**.
- W-3 becomes estimable, and print scope becomes plausible rather than edition-two.

That is the difference between a voice that holds the work in an unworkable pattern and a
voice that makes it better — and it is reachable without cutting one joke, one turn, or
one line of the register.

---

## Proposed amendments — Wendell's alone under C2

1. `VOICE_ANCHOR.md` — add `**Delivers via:**` to all five anchors; mark the load-bearing
   span inside each quotation.
2. `VOICE_ANCHOR.md` §3 — complete the Jerk archetype's targeting rule with the four
   licensed carriers; cross-reference anchor 4 as the same archetype done clean.
3. `VOICE_ANCHOR.md:96–99` — add **who holds the verb?** to the Guardian's rubric.
4. `VOICE_ANCHOR.md` — add one counter-anchor (`ch7:138` proposed).
5. `agency_registry.yaml` — add **R8, pluralize the collective**, between R4 and R1; add
   the three missing entities (`the village`, `the field`, and whatever `DAEMON_CANON.md`
   turns out to be).
