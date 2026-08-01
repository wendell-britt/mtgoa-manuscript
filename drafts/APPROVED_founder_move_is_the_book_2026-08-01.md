# APPROVED — the Founder move is the book, not the app

**Ruled by Wendell 2026-08-01:** *"we need to rewrite the autobiography. There's
a note that has us using writing the book as the founder's move."*

**The note exists and is already drafted.** `specs/SPEC_CH9_REWRITE_V1_2026-07-31.md`
§9, from his own pushback of 2026-07-31: *"Instead of bars-engine let's say that
the book itself was created off of my own page filled in… The person I'm allying
with IS Jordan."* The spec's own conclusion, written before this ruling:

> bars-engine leaves without taking anything with it, because the worked example
> was never the app. It was the book.

**Correction of record.** On 2026-08-01 I recommended keeping seven of the
bars-engine sites as autobiography. That was wrong, and the spec above already
said so. Every site goes.

---

## Scope, measured on `origin/claude/mtgoa-manuscript-changes-swmp78`

**Eleven sites, in three groups.** Section 5's eight are covered by the specced
replacement. Three are not, and they are drafted below.

| Group | Sites | Covered by |
|---|---|---|
| Section 4 — the Founder-move claim | `ch9:153` | **Edit A, below** |
| Section 5 — Journey to the Center | `300`, `360`, `368`, `396`, `402`, `442`, `472`, `494` | `SPEC_CH9_REWRITE_V1` §9 — ~260 words replacing 5,144 |
| Section 6 — The Game | `610`, `612` | **Edits B and C, below** |

---

## Edit A · `ch9:153` — the sentence the ruling overturns

**BEFORE**

> Bars-engine is my Founder move. I built the thing I needed and couldn't find:
> an actual game system that lets people practice the WAVE, that makes the
> emotional alchemy mechanical, that gives the six Faces a practice context
> instead of just a conceptual one. I didn't design it as a product. I designed
> it because I could see the gap and I couldn't stop seeing it.

**AFTER**

> This book is my Founder move. I built the thing I needed and couldn't find: a
> practice you could actually run, that makes the emotional alchemy mechanical,
> that gives the six Faces a context instead of a vocabulary. I didn't design it
> as a product. I designed it because I could see the gap and I couldn't stop
> seeing it.

Three words swapped in the first sentence, the middle clause re-aimed at the
book. The rest stands, including *"you build it yourself or it stays missing."*
Sits four lines under `ch9:151`'s own definition — *"The Founder says, at the end
of it: I've been through all of this. Here's what I made with it"* — which the
book now answers with itself.

## Edit B · `ch9:610` — the five moves, re-anchored

Every replacement below is already canon. Nothing is invented.

**BEFORE**

> Bars-engine has cost me all five of these. *Cut the field*: it is not about
> allyship in general; it is about the gap between people who understand the
> theory and people who can run it when something lands hard. *Put it in front of
> one person*: it went in front of players before it was good, and the sessions
> that failed are the reason the current version works. *Take the note that costs
> you the design*: the token economy did not get adjusted, it got rebuilt, three
> times, because each time the note was structural. *Run it again with one thing
> changed*: every failed session became the next session with something named and
> different in it. *Hand someone the pen*: the goal is for bars-engine to outlive
> its founder, which means whoever runs it later gets to change it, not just
> operate it.

**AFTER**

> This book has cost me all five of these. *Cut the field*: it is not about
> allyship in general; it is about the gap between people who understand the
> theory and people who can run it when something lands hard. *Put it in front of
> one person*: the course went in front of hundreds of people before it was good,
> and the ones who did not finish are the reason this exists. *Take the note that
> costs you the design*: a stack of chapters written at the applause counter did
> not get revised, they got thrown out. *Run it again with one thing changed*:
> every version that failed became the next one with something named and
> different in it. *Hand someone the pen*: the point is for this to live in more
> hands than mine, which means whoever runs it later gets to change it, not just
> repeat it.

Provenance, site by site:

| Clause | Source |
|---|---|
| *Cut the field* | unchanged; already true of the book |
| the course before it was good, the ones who did not finish | `ch9:338`, `ch9:340` — *"less than a ten percent completion rate"* |
| chapters at the applause counter, thrown out | `ch1:119` names the applause counter; `SPEC_CH9_REWRITE_V1` §9 cites the thrown-out chapters |
| every version that failed | `ch9:368`'s structure, with the subject changed |
| live in more hands than mine | `ch9:157`, **verbatim** — *"I wrote this down so the map would live in more hands than mine"* |

*operate it* → *repeat it*, because a book is repeated rather than operated.

## Edit C · `ch9:612` — the teaching sentence

**BEFORE**

> You don't have to build bars-engine. You have to build your version of what
> bars-engine is for your specific problem. That's the Player's move.

**AFTER**

> You don't have to write a whole book about it. You have to build your version
> of what this book is for the specific problem you want to solve for the people
> you want to help. That's the Player's move.

**Wendell's line edit, 2026-08-01, and both halves of it are corrections.** My
draft read *"You don't have to build this book"* — you do not build a book, you
write one, and the verb collision made the sentence read as a riddle. And
*"your specific problem"* was thinner than the book's own definition of a quest.

**The expansion lands the quest.** `ch1:205`: *"Your quest. A cause. The specific
fight, community, or person you are actually in this for. Name them. **This is
who your range is for.**"* *The people you want to help* is that field, restated
in the last section that can still ask for it. A problem with nobody attached is
the Architect's failure mode, which `ch9:151` already separates from the
Founder's.

It is the chapter's whole teaching move, and pointing it at the object in her
hands closes the loop `SPEC_CH9_REWRITE_V1` §9 describes: *"ch1 and ch9 become
the same form, filled and blank."*

---

## Verification after all three plus the Section 5 replacement

    grep -rniE "bars-engine|→ app|\bthe app\b" manuscript/ appendices/ front_matter/ back_matter/

Must return **0** except `shipcheck.py`'s one standing exemption, *"takes a
mindfulness app"*, which is generic prose and not this product. Then `gate.py` at
0 on all four surfaces.

## What does not change

**One parallel for whoever applies Section 5.** `ch9:442` runs the same
construction — *"You don't have to build bars-engine. You don't have to start a
nonprofit."* It falls inside the replaced block, so it needs no separate edit,
and the replacement should carry Wendell's corrected verb: **write**, not build.

The **coaching** paragraphs at `ch9:155`–`157` stand. They never named the app,
they are a real offer in the stack, and `ch9:157` supplies the *hand someone the
pen* line Edit B borrows.
