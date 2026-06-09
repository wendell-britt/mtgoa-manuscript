# EOD Draft Target Shape and Source Alignment

## Purpose

This memo establishes the working shape for the 2026-06-09 EOD manuscript draft on branch:

`codex/book-eod-draft-2026-06-09`

The goal is to keep book work in one clean lane while other environments continue evolving around it.

## Branch Rule

All EOD draft work happens in `mtgoa-manuscript` on the draft branch.

Do not merge product, deck, vault-import, or zo.computer work directly into the manuscript branch unless the change has been translated into a manuscript-facing decision.

The manuscript branch can read other surfaces as context, but it should only commit:

- chapter drafts
- editorial reports
- source alignment notes
- manuscript support files required to make the draft coherent

## Locked Book Promise

Mastering the Game of Allyship helps people who want to show up more effectively as allies learn why allyship keeps failing, see the game underneath the term, and use the Effective Allyship Formula to build real-world relationships, reduce harm, and create the trust that leads naturally into bars-engine and coaching.

## EOD Draft Target

The EOD draft is not trying to become the most complete version of the manuscript.

It is trying to become the clearest complete draft that can be read end-to-end without the reader losing the thread.

The draft should feel like:

1. a concise invitation into the problem
2. a plain definition of allyship
3. a chapter-by-chapter build of the Effective Allyship Formula
4. a set of usable practices, not a theory textbook
5. a clean handoff into bars-engine, decks, and coaching

## Master Chapter Rhythm

Every chapter should follow this rhythm unless there is a strong reason not to:

1. Promise
2. Diagnosis
3. Tool
4. Example
5. Practice
6. Summary / handoff

The controlling rule is:

**one chapter, one idea, one tool, one main example, one handoff.**

## Source Authority Stack

### Tier 1: Manuscript Promise and Shape

These are binding for the EOD draft:

- `MTGOA_BOOK_WORK_TRACKER.md`
- `editorial_reports/2026-06-09/CHAPTER_BY_CHAPTER_SIMPLIFICATION_BRIEF_2026-06-09.md`
- `editorial_reports/2026-06-06/BOOK_PROMISE_AND_CH7_COMPRESSION_PLAN_2026-06-06.md`
- `editorial_reports/2026-06-06/MTGOA_SIMPLIFICATION_PROTOCOL_FOUR_BOOKS_2026-06-06.md`
- `editorial_reports/2026-06-09/BARS_ENGINE_BOOK_COLLISION_SURFACE_MAP_2026-06-09.md`

### Tier 2: Source Lineage

These govern the intellectual ancestry and citation posture:

- `appendices/ON_THE_SHOULDERS_OF.md`
- `EDITING_PLAN.md`
- root Library source corpus at `The Library/manuscripts/sources/`

The active manuscript repo currently carries distilled source authority more than the full source corpus. Treat the root Library source corpus as read-only reference context for this draft branch.

### Tier 3: Current Draft Inputs

These are draft material, not final authority:

- current chapter drafts in `chapters/`
- `Inkwell Upload - 2026-06-04/` as an untracked comparison bundle only
- older draft backups

Use them to recover language and scenes, but do not let them override the locked promise.

## Source Alignment by Function

| Function | Primary source authority | What it governs in the EOD draft |
|---|---|---|
| Chapter rhythm | 10,000 Hours of Play; ILP | one promise, one teaching, one practice, short handoff |
| Practice process | Gerard Egan, The Skilled Helper | current picture -> preferred picture -> way forward; reader agency; implementation |
| Shadow / gates | Big Mind; Existential Kink | parts work, shadow as protective pattern, gate repair without bypass |
| Developmental architecture | Wilber / Integral Life Practice; Spiral Dynamics as background | Six Faces, altitude, transcend-and-include; keep jargon mostly offstage |
| Emotional/body intelligence | Gendlin, Levine, van der Kolk, Porges; wu xing as remixed channel model | felt sense, charge, emotional alchemy, body-state literacy |
| Polarity | Barry Johnson | both/and tensions; ongoing management rather than false resolution |
| Game frame | Watts, Carse, Yu-kai Chou | infinite play, quest grammar, tokens/tickets, motivation mechanics |
| Burnout / activist cost | Maslach; Gorski | exhaustion, depersonalization, inefficacy, identity fusion |
| Wendell voice and internal canon | Igniting Joy; Wendell source corpus | WAVE-Spiral, emotional alchemy voice, personal confession, non-generic phrasing |
| Product collision | bars-engine collision map; CH1 engine contract; BAR/deck specs | handoff to BARs, deck, app, and coaching without turning chapters into software docs |

## Chapter Target Shape

| Chapter | EOD job | One tool | Main source alignment | Collision note |
|---|---|---|---|---|
| Ch0 Infinite Arcade | Wake the reader up to the failure of current allyship and show that the game matters | game frame / token-ticket preview | Watts, Carse, Yu-kai Chou, burnout sources | introduce practice surfaces lightly; do not become app onboarding |
| Ch1 Shaman | Define allyship as relational, consent-based, trust-earned | consent / receptivity / gate of relationship | Gendlin, Big Mind, Egan, ON_THE_SHOULDERS_OF | preserve CH1-to-engine contract when editing structure |
| Ch2 Shaman | Help reader identify their superpower through emotional literacy | emotional alchemy / body-state read | Igniting Joy, wu xing remix, somatic sources | keep BAR capture as evidence, not card product yet |
| Ch3 Challenger | Help reader find where their superpower should actually be applied | discernment / right target | Egan, polarity, Challenger voice canon | protect real-world usefulness over heroic challenge language |
| Ch4 Regent | Show how roles, responsibilities, and structure make return easier | stewardship / support structure | Egan, polarity, developmental architecture | keep allyship relational, not institutional theory for its own sake |
| Ch5 Architect | Teach leverage, strategy, and environment design | design the conditions | ILP modularity, Yu-kai Chou mechanics | keep systems human-facing; do not become product architecture |
| Ch6 Diplomat | Make allyship relational, honest, and sustainable with others | honest terms / negotiation / boundaries | Egan, polarity, relational practice | consent and privacy are core mechanics, not edge cases |
| Ch7 Sage | Show how seeing from Sage altitude solves the specific problems that make allyship fail | see -> switch -> serve -> release -> return | Wilber / ILP, Egan, Ch7 compression reports | highest compression target; Ch7 is proof chapter, not second book |
| Ch8 Player | Turn the whole thing into ongoing practice | keep playing / quest loop | Carse, Yu-kai Chou, ILP practice-life frame | hand off cleanly into bars-engine, deck, and coaching |

## What Must Stay Visible

- Allyship is relational, consent-based, and trust-earned.
- You can support a movement, but you ally with people.
- The Effective Allyship Formula is the strongest reader-facing tool.
- The book teaches transformation; BARs preserve evidence; decks give handholds; bars-engine sustains the loop.
- Source authority should support the reader's trust, not become citation theater.

## What Must Shrink

- long altitude explanations
- repeated game-frame justification
- citation stacks in the main flow
- full forest travelogue in Ch7
- any section that asks the reader to hold more than one main framework at once

## EOD Draft Acceptance Test

Before calling the EOD draft coherent, verify:

1. Each chapter has one main job.
2. Each chapter has one named tool or practice.
3. Each chapter hands off to the next chapter plainly.
4. The allyship definition is clear near the front.
5. The Effective Allyship Formula remains visible across the book.
6. Ch7 is compressed around Sage as usable allyship altitude.
7. The book points toward bars-engine and coaching without becoming a product manual.
8. Source lineage is honored in back matter or light inline attribution where needed.

## Immediate Drafting Order

1. Lock Ch7 simplified shape first because it is the biggest collision and compression risk.
2. Add or refine the front-of-book allyship definition.
3. Sweep Ch0-Ch6 only for promise / handoff / formula alignment.
4. Make Ch8 the clean practice-loop handoff.
5. Run one end-to-end read for thread loss.

