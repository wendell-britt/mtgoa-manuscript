# ch5 and ch7 — Modes vs Moves

## *Same symptom, two different diseases. Two different fixes.*

**Created:** 2026-08-01
**Decided upstream:** B-plus adopted — WAVE anchor stripped from ch3/ch4 move headings, Twenty Cards relocated to appendix with the ch3 teach retained, ch4's stage sequence renamed. Stage sequence cut in ch5, ch7, ch8.
**Question:** ch5 and ch7 both present a Section 4 five-item instrument whose names collide with their Section 6 moves. Cut the modes, cut the moves, or rename?
**Companion:** `MOVES_VS_STAGES_6FACE_ANALYSIS.md`

---

## The overlap, measured

### ch5 — Regent

| Mode (§4, ~15 lines) | Move (§6, ~50 lines) | Overlap |
|---|---|---|
| The Custodian — *what have I been given that still works?* | Honor What Still Serves | near-identical |
| The Inheritor — *what came with my inheritance that I didn't choose?* | Name the Inheritance | near-identical |
| The Reformer — *what needs to change so this survives?* | Reform Without Erasing | **identical** |
| The Keeper of Vows — *what did I say I would do?* | Keep the Vows | **identical, same words** |
| The Teacher — *who is coming after me?* | Entrust Without Clinging | close |

**5 of 5.** And the moves cite the modes by name inside themselves:

> **Move 3:** *"**The Reformer** changes the tradition while honoring the lineage."*
> **Move 4:** *"**The Keeper of Vows** does the unsexy work."*

The chapter already knows they are the same thing. It just never says so.

### ch7 — Diplomat

| Channel (§4, ~250 lines) | Move (§6, ~135 lines) | Overlap |
|---|---|---|
| Channel 2 — Translator | Translate Across Camps | **name collision** |
| Channel 4 — Repairer | Repair After Rupture | **name collision** |
| Channel 5 — Integrative Negotiator | Close with Honest Terms | **substance collision** — the Stake-Surfacing Close is taught inside Channel 5 |
| Channel 1 — Bridge-Builder | *(no counterpart)* | — |
| Channel 3 — Field-Holder | *(no counterpart)* | — |
| *(no counterpart)* | Name the Field | — |
| *(no counterpart)* | Refuse False Equivalence | — |

**3 of 5, and the unmatched items on both sides are strong.**

---

## Why these are different diseases

**ch5 has one instrument wearing two hats.** The modes are a *role inventory* — five nouns, fifteen lines, no technique. They give Jordan nothing to do alone. The moves do the same five things with examples and tests attached. There is no second instrument to preserve; there is a label set and the thing itself.

**ch7 has two real instruments that happen to share three names.** The channels are 250 lines of actual technique. The moves carry something no other chapter has — **a dependency graph**:

> *Prerequisite: Move 2. You have not earned a refusal until you can translate the position you are refusing.*
> *Prerequisite: some real trust has been built. This move requires a history.*

That is the only place in the manuscript where the moves state their own ordering logic, and it is better than a sequence because it is conditional rather than linear. Cutting ch7's moves would destroy the best-structured move set in the book to solve a naming problem.

**The book's own definition of the split**, from ch3:

> *Everything in Section 4 was the instrument. These five are what you do with the instrument when other people are present and the clock is running… These five are what it costs to run it where somebody is watching.*

Section 4 = the instrument, learned alone. Section 6 = the cost under witness. Test both chapters against it: **ch5's modes fail** (a role inventory is not an instrument). **ch7's channels pass, and three of ch7's moves fail** — `Translate Across Camps` re-teaches the Translator rather than naming what translating costs you in the room.

---

## Recommendation — ch5: delete the modes section, keep the modes

**Cut `### The Five Modes of Loyalty` (ch5.md:340–353).** Fifteen lines.

The five modes do **not** disappear. They already exist, with a full defining paragraph each, inside the EA Channel Alignment table twenty lines below:

> **The Custodian** (Earth/Neutrality): Caring for what exists begins as a surrender: you did not choose this. The alchemy moves obedience (compliance) into true allegiance (chosen loyalty)…

So the modes survive **as the EA table's rows** — which is the job they are actually doing — and stop being presented as a standalone instrument competing with the moves.

**One thing is lost and must be carried over:** the standalone section holds the five guiding questions (*What have I been given that still works?*), which the table paragraphs lack. Fold each question into its table paragraph. Five sentences.

**Result:** ch5 goes from four fives to two — the EA channel mapping (a cross-reference, not an instrument) and the moves. No content lost. ~15 lines cut, ~5 added.

**Why not the reverse (cut the moves, promote the modes):** the moves carry every example and every test in the chapter. The modes carry none. Promoting the modes means writing five examples and five tests that already exist elsewhere.

---

## Recommendation — ch7: keep both, rename three moves

The channels stay. The moves stay. **Three move names get replaced** so each names the public act rather than the private role.

| Now | Problem | Direction |
|---|---|---|
| Move 2 — **Translate Across Camps** | restates Channel 2 | The act is voicing the other camp's case *accurately, while your own side watches*. That is the cost. → **Carry the Other Camp's Case** |
| Move 3 — **Close with Honest Terms** | Channel 5 already teaches the Stake-Surfacing Close | The chapter's own thesis is *"The Diplomat wins by being the one at the table who knows what they're willing to lose,"* and the move's marginalia says *"half the time you will find you do not have a walk-away term at all."* The move is the walk-away, said out loud. → **Name What You'd Walk Away From** |
| Move 4 — **Repair After Rupture** | restates Channel 4 | Channel 4 teaches how repair works. The move is being the one who reopens it first, before the other person does. → **Go Back First** |

`Name the Field` and `Refuse False Equivalence` already do the Section 6 job and stay as they are.

**This is a rename plus a re-aimed opening paragraph per move, not a rewrite.** The examples, prerequisites, and tests underneath survive. The prerequisite graph survives — it references move *numbers*, not names.

**Why not cut ch7's three duplicating moves:** it leaves the chapter with two moves and breaks the five-move pattern held across ch3–ch9.

**Why not cut the channels:** 250 lines of the chapter's only technique, including the Stake-Surfacing Close, which is referenced elsewhere in the book.

---

## Also decided upstream, recorded here

**ch4's stage sequence — rename.** It survives on merit (Charge → Aim → Act → Stand → Exit is a distinct execution protocol; ch4.md:319 explicitly defends Stand and Exit as separate failure modes), but "stage sequence" is the retired vocabulary everywhere else, and leaving one behind makes it read as an oversight rather than a decision. Candidates:

1. **The Confrontation Protocol** — matches the chapter's existing "30-Second Protocol" language
2. **The Five Beats** — signals timing, which is what Stand and Exit are actually about
3. **Charge to Exit** — names it by its endpoints, no category noun at all

Recommend **(1)**. The chapter already uses *protocol*, and it is the only word that says *run this in order, every time* without reintroducing "stage."

---

## Net effect on the four fives

| Ch | Before | After |
|----|--------|-------|
| 5 | modes, stage seq, moves, deck rows | EA mapping, moves |
| 7 | channels, stage seq (prose), moves, deck rows | channels, moves *(names disambiguated)* |

---

## Open question

**ch7's Field-Holder and Bridge-Builder have no move.** Two of five channels never surface in Section 6. Under the instrument/cost split that is legitimate — not every channel has a public act worth its own move. But it is worth a deliberate yes rather than an accident. Same question in reverse for `Name the Field`, which has no channel.

---

*Recommend: ch5 delete-and-fold (cheap, no loss). ch7 rename-three (cheap, preserves both instruments). Draft ch5 first — it is fifteen lines and proves the pattern.*
