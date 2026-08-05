# 6-Face GM Analysis — Superpower Placement: Link Out vs Seat In Text
## *Where does Jordan find hers?*

**Created:** 2026-08-04
**Updated 2026-08-04, two rulings by Wendell:** the Regent's superpower is the **Storyteller** and the
Architect's is the **Strategist**, both now bound to the word *superpower* in the prose. And the
superpower page has a **stable URL**, which closes condition 1 below — the permanence risk that was
the only thing standing against option A.
**Question:** Route the reader to the superpower page at masteringallyship.com, **or** seat a section / appendix in the book explaining the six superpowers.
**Origin:** A2 residual. `ch1:209` promises the character sheet fills in with *"a superpower you will only spot in motion."* The line is never written. See `specs/DECISION_LOG.md` A2.
**Companions:** `SPEC_6_SABOTAGING_BELIEFS.md`, `SOURCES/SELF_SABOTAGING_BELIEFS.md`, `specs/SPEC_CH3_CH8_POLISH_LEDGER_2026-08-03.md` (P1), `specs/DECISION_LOG.md` DL-20.

---

## The finding that reframes the question

**The six superpowers are already in the book, one per chapter, each at its own altitude.**

| Face | Chapter | The superpower, as the book already names it |
|---|---|---|
| Shaman | `ch3:756` | **The Alchemist** — takes the charge the Controller called a foul and spends it |
| Challenger | `ch4:597` | **The Disruptor** — willingness to be unwelcome on a charge you have checked |
| Regent | `ch5:597` | **The Storyteller** — what you received put in a form the next person can receive |
| Architect | `ch6:464` | **The Strategist** — where the push goes and when, then built so the next person runs it without you |
| Diplomat | `ch7:592` | **The Connector** — connection that has survived being told the truth |
| Sage | `ch8:639` | **Escape Artist + Coach**, a compound: get out cleanly, stay useful to those still inside |

And `ch2:334` already defines the reader's *personal* superpower with a formula and two worked
examples: *adaptation under pressure → conscious integration → intentional contribution.*

**So the book does not have a superpower explanation gap. It has a superpower *diagnosis* gap.**
Jordan can read six chapters, meet six superpowers, hold the formula, and still not know which
one is hers or what hers is made of. That is the transfer gap this session already named in ch2,
appearing again one level up: she has the concept and cannot run it on herself.

This changes what the options are. *Explain the six superpowers in a new section or appendix* is
the fourth telling of material already told three ways, and it collides head-on with the polish
ledger's **P1 — one full explanation per teaching unit** (`SPEC_CH3_CH8_POLISH_LEDGER_2026-08-03.md`).
The live question is where the **diagnostic** lives.

---

## The three positions

| Option | What the book carries | What the page carries | Cost in words |
|---|---|---|---|
| **A — Route out** | the six as they stand, plus one sheet line pointing at the page | the diagnostic that names hers | ~40 |
| **B — Body section** | a new section teaching the six as a set, plus the diagnostic | nothing required | ~900–1,400 |
| **C — Appendix H** | the six as a reference table plus a self-scoring procedure | nothing required | ~700–1,100 |

**There is already a precedent, and it is exact.** `ch1:83` routes the reader off-page for the
*Myths Read*:

> (A short, unflattering diagnostic at masteringallyship.com marks which of these are yours and
> hands each one back with the page that takes it apart. It scores how you actually behave, and
> it has no score for which kind of ally you are, because that question belongs to the trap.)

Same shape as the ask: a book-taught inventory, a diagnostic held off-page, a parenthetical that
does not interrupt. It survived the app-removal sweep that took 57 routing sites down to 1, so
**a masteringallyship.com diagnostic is already an approved routing target** and is a different
object from bars-engine, the app DL-20 is about.

---

## Anchor (design intent)

Jordan's craving in `EDITING_PLAN.md` is *"I want to show up for others without losing myself."*
Her drop-off triggers are **jargon without translation, claims without practice, moralizing.**
She *"will skim theory, will not skip a story, will stop for a named move with a practice."*

The superpower is the book's one positive claim about her — the wound-to-capacity formula. Everything
else on her character sheet is a problem: a myth, a daemon, a skipped channel, an undrawn line, an
inherited rule, a harm she keeps fixing, a walk-away price, a game she drops to. **Eight problems and
no capacity.** Whatever we choose has to put the capacity on the sheet, because the sheet is what she
carries into Chapter 9 and designs from.

---

## 🧠 Architect — Structure and integrity

**A — Working:** Costs ~40 words in a book that has a word problem, not a word budget. Uses a
routing pattern already proven at `ch1:83`. The teaching stays distributed at the altitude where
each superpower means something, which is the whole reason the six-chapter structure exists.

**A — Cost:** Creates a second load-bearing external dependency. DL-20's rule is the hard one:
**a wrong pointer in a printed book cannot be patched.** The page must exist, be stable, and stay
at a URL that survives the book's shelf life. That is a permanence commitment, not a link.

**B — Working:** Self-contained. No external dependency, no permanence risk.

**B — Breaking:** Violates P1 outright. The six are taught six times already; a seventh section
teaching them as a set is exactly the "restate the model's entire logic" the ledger forbids. It
also has nowhere to live — after `ch2:334` it pre-empts six chapters; after ch8 it arrives once the
material is spent.

**C — Working:** An appendix is the honest home for a reference table, and appendices are where this
book already puts procedures.

**C — Breaking:** A–G are clean and singly assigned; this opens H. And the reader who most needs the
diagnostic is the one least likely to turn to an appendix — the Architect's own objection from
`TOOL_PLACEMENT_6FACE_ANALYSIS.md`: *"Reader may never open appendix."*

---

## 🏛 Regent — What to preserve

**Preserve:** the per-chapter seating of each superpower at its altitude. That arrangement is
inherited from the six-chapter design and it is load-bearing: the Alchemist means something *after*
ch3 teaches charge, and nothing before it.

**A — Working:** Preserves it entirely. Adds a pointer, breaks no inheritance.

**B/C — Cost:** Both create a second home for material that already has one, and a second home is
how canon splits. The repo has already paid this bill once — `APPENDIX_C_KEY_TERMS.md` had to be
retired by ruling when C changed hands.

**Regent's warning on A:** the page is outside the repo, so it is outside every instrument. `gate.py`
cannot read it, `citation_audit.py` cannot check it, `compile.py --verify` cannot round-trip it.
Whatever it says about the six superpowers can drift from what the book says, and nothing here will
catch it. **If A is chosen, the page's six definitions should be pasted into the repo as a source
file so drift is at least visible.**

---

## ⚔️ Challenger — What gets wrong

The Challenger's objection is to **B and C both, and it is the strongest objection in this document.**

A section titled "The Six Superpowers" is the book teaching *about* superpowers a fourth time. Jordan
has read the six. What she cannot do is name hers. Adding 1,200 words of explanation answers a
question she did not ask and leaves hers unanswered — **more concept, no transfer.** That is the exact
failure ch2 now diagnoses by name, committed by the book, in the chapter that diagnoses it.

**The Challenger's objection to A:** routing out at the moment of the reader's one positive claim can
read as the book withholding the good part behind a link. `ch1:83` gets away with it because it routes
her to a diagnostic about her *myths* — unflattering material, and it reads as generous. Routing her
off-page for her superpower reads differently unless the book has already given her the formula, which
`ch2:334` does. **A survives this objection only because ch2:334 exists.** If that section ever moves
or thins, A breaks.

---

## 🎭 Diplomat — What bridges

**A — Working:** The parenthetical form at `ch1:83` is the bridge that already works: it does not
break the read, does not make the page a prerequisite, and does not moralize about doing the work.

**A — Requirement:** the pointer must be **optional in fact, not just in tone.** Jordan must be able
to write a superpower line without visiting the page, or the sheet has a hole in it for every reader
who does not go. This means the sheet line has to be answerable from the book alone, with the page as
the sharper version. `ch9:664`'s Face count already gives her an answerable version: the Face she just
watched run six times, named as a capacity.

**B/C — Cost:** both make the book longer for every reader in order to serve the fraction who would
have gone to the page. The Diplomat prices that as a bad trade at 1,000+ words.

---

## 🌊 Shaman — Felt sense

The superpower is the one place in this book where Jordan is told the thing she built out of what
happened to her is worth something. That is grief material handled from underneath, and it lands in
the body or it does not land.

**A — Risk:** a URL at that moment can flatten the beat. **Mitigation:** the pointer must come *after*
the felt claim, never as the claim. `ch2:334`'s *"The wound does not become your identity. It becomes
signal, then skill, then contribution"* is the beat. A pointer belongs downstream of it, at the sheet,
not beside it.

**B — Risk, and it is worse:** a section explaining six superpowers as a set is a taxonomy, and a
taxonomy arriving at the moment of her one positive claim is exactly the *"body-knowing set aside for
the consensus"* move ch2 already names. Six named capacities in a table are easier to skim than to feel.

**Shaman's verdict: A, with the pointer placed after the beat, not inside it.**

---

## 📖 Sage — Panoramic view

Three altitudes are in play and they want different things.

- **The book** wants fewer words, one explanation per unit, no new appendix.
- **The game version** is where the superpower content is going to live heavily, by Wendell's own
  account. Content built for the game does not need to be pre-paid in the book.
- **The page** is the join between them, and it is the only one of the three that can be revised
  after print.

The Sage's read: **B and C spend book words on material whose real home is the game.** Putting 1,200
words of superpower taxonomy in the manuscript now means maintaining two canonical versions through
the game's development, and the book's copy is the one that cannot be changed.

**The Sage's caution on A:** DL-20 is currently at **1 remaining site** and shipcheck ranks app routing
as blocker one. Adding a routing site while that category is still open needs to be a deliberate
exception, not a quiet addition — the exception being that this points at a **page**, not at
bars-engine, and `ch1:83` is the precedent that the distinction is already ruled.

---

## Summary table

| Face | A — Route out | B — Body section | C — Appendix H |
|---|---|---|---|
| Architect | ✅ cheapest, proven pattern | ❌ violates P1, no home | ⚠️ opens H, low reach |
| Regent | ✅ preserves seating | ❌ splits canon | ❌ splits canon |
| Challenger | ⚠️ survives only because ch2:334 exists | ❌ more concept, no transfer | ❌ same |
| Diplomat | ✅ if answerable without the page | ❌ bad word trade | ❌ bad word trade |
| Shaman | ✅ if placed after the beat | ❌ taxonomy at the wrong moment | ⚠️ neutral, unread |
| Sage | ✅ leaves the depth to the game | ❌ pre-pays the game in print | ❌ same |

**6 of 6 land on A.** No Face argues for B. C draws two neutrals and no advocate.

---

## Recommended decision: **A, with three conditions**

Route to the page, and close A2's residual with the sheet line — but the recommendation is not
"add a link." It is **route out and make the sheet line answerable from the book alone**, so the
page sharpens an answer she already has rather than supplying one she lacks.

1. **The sheet line is answerable without the page.** At `ch9:664` she has just counted her Faces
   across six moments. The Face that showed up four or more times, named as a capacity rather than a
   habit, *is* her superpower spotted in motion — which is what `ch1:209` promised in those exact words.
2. **The pointer sits at the sheet, not at the felt claim.** `ch2:334`'s beat stays clean. The pointer
   goes where she is writing, in the `ch1:83` parenthetical register.
3. **The page's six definitions get pasted into the repo** as a source file, so the instruments can see
   drift between the page and the book even though they cannot see the page.

---

## Tests (acceptance)

1. **Offline test:** a reader with no internet can write a superpower line on her sheet. If she cannot, A has failed and C is back.
2. **P1 test:** no superpower is explained a fourth time anywhere in the manuscript.
3. **Beat test:** `ch2:334` still ends on *signal, then skill, then contribution*, with no URL inside the section.
4. **Sheet test:** the character sheet carries at least one capacity, not only problems.
5. **DL-20 test:** shipcheck's app-routing count does not rise. The pointer names a page, not bars-engine, and is exempted by name the way `ch1:83` is.
6. **Drift test:** the page's six definitions exist in the repo and match the six chapter sites in the table above.

---

## Open questions for Wendell

1. ~~**Does the superpower page have a stable URL that will outlive the print run?**~~ **CLOSED 2026-08-04: it does.** Recommended that the pointer still name `masteringallyship.com` the way `ch1:83` does rather than printing a deep link, so a later path change cannot strand the book.
2. **Does the page diagnose the six Faces' superpowers, or the personal wound-to-capacity formula at `ch2:334`?** They are different instruments and the pointer's wording depends on which.
3. **Sheet line wording** — the A2 candidate at `ch9:664` is drafted and measured, awaiting the same ruling.

---

*Analysis complete. Recommend A with the three conditions. B is opposed by all six Faces; C has no advocate. Nothing applied — this document changes no prose.*
