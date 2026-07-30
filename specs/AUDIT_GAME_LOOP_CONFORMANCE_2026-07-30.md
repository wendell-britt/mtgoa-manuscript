# AUDIT — Can the game in *Mastering the Game* actually be played?

**2026-07-30. Commissioned by Wendell against `Mastering the Game of Allyship —
Canonical Game Loop`, on the instruction to test conformance before writing any
more prose: "If the book is called mastering the game, but the game loop can't be
played that's an issue. Think about this as anticipating objections."**

Measured against `manuscript/ch1.md`–`ch9.md` (93,810 words) and the shipping
appendices. Every count in this document is a grep, not an impression.

---

## 0 · The finding, in one paragraph

The book teaches **station 5 (Move)** superbly and **station 6 (Commitment)**
well. It has partial versions of Context and Superpower. **Six of the twelve
stations do not exist in the book at all** — Depth, Milestone, Resistance,
Counterspell, Visibility, Campaign board — and two more (the internal practices
that would serve as Counterspells) are present but sequenced as pre-work rather
than as a branch off a live commitment. Separately, `BAR` names three different
objects across ch1, ch2 and the loop doc, and **ch1 teaches the exact object the
loop's own edge-case table forbids.** And ch1 makes a forward promise —
*"the loop you meet in the next chapter"* — that ch2 does not keep.

The good news is structural: **the missing Depth station and the missing ethical
frame are the same hole**, and Wendell's own reframe fills both at once (§5).

---

## 1 · Station-by-station conformance

| # | loop station | status | evidence |
|---|---|---|---|
| 1 | **Context** | partial | `APPENDIX_A:8` opens *"Which allyship problem is actually alive for you right now?"* Each chapter's Exile/Distortion sections situate **the Face's** story, and `Drawing Against the Shadow` asks the reader to *"bring the last time you…"*. The reader is never asked to name and hold a context of their own before the chapter prescribes. |
| 2 | **Depth** | **absent** | 0 hits for any scope-choice mechanism. Nothing anywhere lets the reader pick a level of engagement, and nothing says a smaller scope is not failure. |
| 3 | **Superpower** | defined, never selected | 21 hits / 9 files. `ch2:394` defines it well and in the loop's own terms: *"the reliable capacity you built to survive your wounds, once that capacity is made conscious, ethical, and usable in service of others."* `ch3:392` gives one per channel. It is never selected, confirmed, or carried into a commitment. |
| 4 | **Milestone** | **absent** | 1 hit, incidental. No intermediate outcome exists between a chapter's teaching and a single move. |
| 5 | **Move** | **strong — the book's best station** | 5 named Moves × 6 chapters, now in WAVE order. `Drawing Against the Shadow` (ch3–ch8) runs the five stages against one card in 90 seconds. |
| 6 | **Commit + deadline** | **present, and better than expected** | `### From Card to Quest`, six instances (ch3–ch8). The quest grammar is the loop's Commitment: *"One line, four things: what you will do, **who it reaches**, by when, and what it costs you."* It already carries the beneficiary field. |
| 7 | **Resistance check** | **absent as a station** | **0 prompts** matching *what would stop you / what might make this hard / what gets in the way.* The materials exist — Gates, the chapter daemon, `3-2-1`, `Name the Voice`, `Polarity Encounter` — but every one of them sits in Section 4 (The Practice), i.e. **before the quest exists.** They are pre-work, not a branch off a live commitment. |
| 8 | **Counterspell** | same, unlinked | 0 hits for the term. The three practices above are counterspells in everything but name and attachment. The loop's guardrail — *"a counterspell must link to an active commitment"* — has nothing to link to at the point they are taught. |
| 9 | **Complete action** | implied only | Quests carry a date. Nothing in the book marks a move complete or asks for evidence. |
| 10 | **Create BAR** | present, three incompatible definitions | §2 below. |
| 11 | **Visibility** | **absent** | 0 hits. The loop's anti-performance mechanic — *"visibility is consent-based, private action is valid action"* — is the one design rule that answers the flex problem, and the book never states it. |
| 12 | **Campaign board** | **absent** | 0 hits. |

**Score: 2 solid, 2 partial, 6 absent, 2 present-but-mis-sequenced.**

The shape of the failure is consistent and it is not random. **The book is
excellent at the middle of the loop (what to do) and empty at both ends** — it
never helps the reader enter (Context, Depth, Milestone) and never helps them
finish (Complete, BAR-as-receipt, Visibility, Board).

## 2 · `BAR` names three different objects, and they escalate

| where | what a BAR is | fields |
|---|---|---|
| `ch1:249` **Your First BAR** | a reading capture. *"Something in this chapter hit you… write it down."* One or two sentences. *"That is the whole move."* | **1** |
| `ch2:530` **Section 9: The First BAR** — *Breakthrough → Action → Reflection* | a three-part form written across time. **B** = the pattern you noticed. **A** = *"What one concrete move will I take in the next 24 hours?"* **R** = *"After the action, what changed."* | **3** |
| Canonical loop | the immutable record minted **from a completed commitment**, with queryable provenance back through move, milestone, superpower, depth and context | derived |

**ch1's BAR is the object the loop's edge-case table explicitly forbids.** The
loop says: *"Internal work is completed but action is not → Record the
counterspell; **do not create BAR or completion credit**."* And the
non-negotiable invariant: *"A BAR references exactly one completed commitment."*
A reader who does ch1 exactly as written has produced pure internal processing
and been told *"that is the whole move."*

**The reconciliation is cheap, and it does not touch ch2's template.** ch2's
three fields map onto the loop cleanly: **B** is Context plus Superpower, **A**
is the Commitment, **R** is CompletionEvidence. So the *name is on the wrong
object*. The three-field thing is the **capture**; the **BAR is what the capture
becomes once Reflection is filled in.** That keeps ch2 verbatim, makes ch1's
one-field version an openly incomplete capture rather than a finished move, and
makes the app's BARs and the book's BARs the same object for the first time.

Also: **there is no `BAR` entry in the shipping glossary.** Five entries in
`APPENDIX_C` cross-reference `BAR` and none defines it. The expansion
*Breakthrough → Action → Reflection* appears exactly once in the book, as a
section subtitle at `ch2:531`.

Third collision, and this one is mine: `deck/BAR_GRIDS.md` uses "BAR grid" for
the 5×4 card tables I pulled in the Seam 1 pass. That is a third meaning and the
cheapest of the three to rename.

## 3 · The forward promise ch2 does not keep

`ch1:193` — *"You already have the process that runs every one of these faces:
**the loop you meet in the next chapter.** Each Game Master takes a chapter to
teach you their game, and the loop is how you play it."*

**ch2 has no loop section.** Its only occurrence of the word is `ch2:172`, and
there it is the *pathology*: *"A familiar loop keeps running: the moment after a
hard conversation spent rehearsing what you should have said… That loop is the
edge of the Forest."*

What the reader is handed instead, one chapter later, is the WAVE-Spiral: five
stages of running **one** move. That is station 5 of twelve, not the loop.

**This is the objection, and it is quotable.** A book titled *Mastering the Game*
names the loop on page one of chapter one, points forward to it, and never prints
it.

## 4 · The target gap — Wendell is right that it is load-bearing

What the book has for *whom you are helping*:

- **Four domains** (`APPENDIX_A`): Gather Resources, Skillful Organizing, Direct
  Action, Raise Awareness. These are **which allyship problem**, i.e. the arena.
  Not a person.
- `ch1:189` — *"Sometimes the friend, the coworker, the kid, the community you
  show up for needs a Challenger."* Generic, and the only place it appears.
- `ch1:191` — *"The reason to widen your range is the person in front of you —
  the one who needed a move you did not have."* This is the closest the book
  comes, and it is one sentence.
- The quest grammar's **who it reaches** field (six instances). The field exists;
  nothing teaches the reader how to fill it.

**Nothing in the book says who needs which Face.** Wendell's proposal is that
each Game Master has a target type, which is correct and is a property of the
Face rather than a new axis — six new units, not another multiplication of the
deck. It also gives the Examples their missing constraint: an Example is a
**scenario class** the reader is likely to meet, chosen so the book does not have
to teach every kind of issue.

### The number that makes this urgent

**`marginaliz*` appears once in 93,810 words**, in ch1. Zero identity-specific
scholarship is cited anywhere in the book. `ON_THE_SHOULDERS_OF` cites Watts,
Carse, Chou, Wilber, Egan, Meadows, Johnson, Maslach, Gorski and Rice — a
**mechanics** lineage, complete and honest on its own terms, with no source a
reader could follow into any specific community's experience.

For a book that has to be credibly about allyship, that is the first thing a
hostile reviewer opens with, and it is also the cheapest thing to fix: a citations
apparatus is the move that *earns* the leeway Wendell wants, because it says
plainly that the book teaches capacity and points elsewhere for content.

## 5 · The reframe fixes the missing station

Wendell, 2026-07-30:

> *"Allyship isn't about learning how to help everyone, but learning how to be
> more helpful and how to expand your circle of helpfulness at the speed of your
> skill and capacity."*

Set that beside the loop's definition of the station the book is missing:

> **Depth** — *"the player-selected level of engagement for this pass through the
> loop. It sets the scale and intensity of what is reasonable now, **without
> ranking the player's worth or commitment**."* And the design rule: *"A player
> may choose a scope that fits their present capacity; **lower depth is not
> failure**."*

**These are the same idea.** The reframe is the *rationale* for Depth; Depth is
the *mechanic* of the reframe. The book is missing both, which means one piece of
writing closes the largest structural hole and answers the ethical problem at the
same time:

- it explains why the book does not teach every group (capacity, not coverage);
- it gives the reader a legitimate small scope, which is what stops the loop
  from being a guilt engine;
- it makes *expanding the circle* the progress metric, which is exactly what a
  cyclical loop needs and what a checklist cannot have;
- and it pairs with **Visibility** (station 11), the other absent station, to
  make performance structurally unavailable: a move that costs the player,
  requires nothing of the person it reaches, and need never be shown to anyone
  cannot be flexed.

`ch1:191` already states half of it. It needs to become the frame rather than a
line.

## 6 · Tickets and tokens stop after ch3

| chapter | hits |
|---|---|
| ch1 | `## The Token System — What You're Spending`, `## The Ticket System — What You're Earning` |
| ch3 | `ch3:434` *"These are the five renewable tokens"*; `ch3:454` closes the ch1 loop explicitly |
| **ch4–ch8** | **0** |
| ch9 | token economy mentioned only as the author's build history |

The economy is introduced, connected to Emotional Alchemy, and dropped for five
of nine chapters. It has an obvious home in each: every Move's `**The test:**`
beat is already asking what the move paid, without naming the currency.

## 7 · What this audit does not decide

- Whether the six absent stations get **named** in the book or only **taught**.
  Naming them adds six units to a book just cut from 219 named units to 99 on
  Wendell's ergonomics ruling. Recommendation is in §8, but it is his call.
- Which of the three `BAR` definitions is canonical. §2 recommends; it is a
  doctrinal call, not an editorial one.
- The six per-Face targets. These are Wendell's to name; the audit only
  establishes that the slot is empty and load-bearing.

## 8 · Recommendation, in priority order

1. **Depth + the reframe, in ch1**, folded together per §5. Largest return, and
   it converts a commercial discomfort into the book's ethical spine.
2. **Reconcile `BAR`** per §2, and add the missing glossary entry. Cheap,
   mechanical, and it is currently a contradiction with a stated invariant.
3. **Fix the ch1:193 promise** — either ch2 prints the loop or ch1 stops pointing
   at ch2 for it. Printing it in ch2 is the stronger book.
4. **Six per-Face targets**, one line each, plus the citations apparatus. This is
   what makes the Examples writable, which is what this audit was blocking.
5. **Resistance check + Counterspell**, attached to the quest at `From Card to
   Quest` rather than taught as Section 4 pre-work. Six sites, one pattern.
6. **Visibility**, one paragraph, wherever the quest is committed.
7. **Tickets and tokens** back into ch4–ch8 via the existing `The test:` beat.

## 9 · How this gets checked

```
grep -c "loop" manuscript/ch2.md                       # must find the printed loop after (3)
grep -rc "marginaliz" manuscript/                      # 1 today
grep -rc "Breakthrough → Action → Reflection" manuscript/   # 1 today, in a subtitle
grep -rn "what would stop you\|might make this hard" manuscript/   # 0 today
grep -rc "token\|ticket" manuscript/ch4.md manuscript/ch8.md      # 0 today
grep -c "^\*\*BAR\*\*" appendices/APPENDIX_C_KEY_TERMS.md         # 0 today
```
