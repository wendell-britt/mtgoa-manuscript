# Chapter 8 — the cut sections against the rewrite

**2026-09-23.** Developmental comparison with instrument readings. Nothing in `manuscript/` was changed. Both versions were read in full.

- **Cut version:** `3b37e4d:manuscript/ch8.md`, 15,143 words. Sections 4–6 and the bites/quest block run lines 307–828.
- **Rewrite:** `origin/claude/allyship-book-download-xh85rs` @ `8e1ec2b`, 9,670 words. The same region runs lines 307–507.
- Lines 1–306 (5,430 words) are identical in both apart from one word at 265. Every defect there is present in both versions.

**The number the tracker reports is wrong.** `MTGOA_BOOK_WORK_TRACKER.md` gives 13,789 words and a net change of −46 for the rewrite. The commits give 15,143 → 12,294 (`64150e6`) → 9,661 (`1defe50`) → 9,670 (final). The tracker also files `1defe50` under "sections 4-5" when its message says section 6.

---

## Verdict

As a replacement for sections 4–6 the rewrite is the weaker chapter. It carries one idea worth keeping, the altitude scene. The five Moves, the domain section, both 3-2-1s and the attributions it displaced are still owed to the reader. Reasons below, each with its evidence.

What the rewrite has that the cut version lacks:

- One through-line. The cut version hands the reader four overlapping five-item sets (July diagnosis ST-3, still open at `3b37e4d`). The rewrite has none.
- One sustained scene with a fork. The hiring-meeting scene (ch8:325–359, about 1,000 words) runs three versions of one moment and includes a turn where the Sage's reading was wrong: *"You were reading it wrong. You stay anyway."* The cut version's worked examples (Ellis, Sam, Kit, nine years, Ade) run three to five sentences each.
- The cost of the role stated in one place (ch8:363–375).
- Less jargon on the page. The EA table and alchemy block are gone.

---

## Findings, ranked by reader cost

**1. Section 7 recaps material the chapter no longer teaches.** The chapter's handoff to the Player says *"Four capacities carry forward"*, then *"which makes the return most of the practice rather than its epilogue"*, then *"Putting a game down is not giving up"* (ch8:534). The rewrite's own close says *"Two capacities come out of this practice"* (ch8:395) and teaches no return practice and no put-down.

**2. The rewrite contradicts the chapter's opening.**

| Rewrite | Unchanged first half |
|---|---|
| *"The Sage stands in the forest. She can visit the table, but she does not belong there."* (ch8:397) | *"I see all of it and I'm still here, still setting the table, still in relationship."* (ch8:90) |
| *"The cost is that you will know you do not belong at the table."* (ch8:365) | *"The view didn't lift you up and out. It let you stand more fully in."* (ch8:297) |
| *"Most of what you see will be invisible to them."* (ch8:367) | *"Somebody in the power game may be a person of enormous developmental range having a bad week. If your map can't hold that, your map is running you."* (ch8:291) |
| *"You serve from an altitude they do not have to understand."* (ch8:359) | The Sage in distortion *"projects their own vantage onto people who aren't standing there."* (ch8:189) |

The Polarity Encounter at ch8:287 names the collapse "contempt with a diagram attached." The rewrite makes the altitude difference a permanent fact about the table.

**3. The chapter's promise goes unpaid.** The subtitle and the Section 3 thesis (ch8:237) say *"Mastery is knowing which game you're playing and being able to put it down."* The cut version pays it in Move 4. The rewrite contains no put-down practice (0 hits against 5).

**4. Book-level commitments now point at nothing.**
- The domain section. Wendell ruled 2026-08-03 that the domains be *"a move that people can practice"* in every chapter, and `SPEC_DOMAIN_SECTIONS_2026-08-03.md` lists ch8 as owing one. The cut version delivered it (Direct Action, Raise Awareness, Gather Resources, Skillful Organizing, 1,108 words). The rewrite deletes it.
- `manuscript/ch9.md:615` cites **Name the Game** and **Switch Games Deliberately** by name and by chapter.
- `back_matter/index.md` places Name the Game at Ch 8 §1, §2, §4 and §6, Hold the Meta at §6, and Egan and Merzel at §4. The rewrite carries none of those names.
- `appendices/APPENDIX_I_SUPERPOWERS.md:17` lists *Escape Artist and Coach (the Sage, Chapter 8)*. Ch8 defined both in "What You Take Out of the Forest", now cut.
- `appendices/ON_THE_SHOULDERS_OF.md` says Big Mind is a source *"which Chapter 8 names in the text"* and that Egan *"runs the spine of the Sage chapter."* The rewrite names neither. Its attribution paragraph (Genpo Roshi, Wilber, Laloux, Egan, Chou) is gone, and `front_matter/copyright.md` credits the same Big Mind lineage.
- `SPEC_CH9_REWRITE_V1_2026-07-31.md` picks ch9's Sage move from ch8's five Moves by line number.

**5. The rewrite removes material the 2026-08-09 compression pass protected.** `CUTS_ARCHIVE_2026-08-09.md` (Tier 2, ch8) lists as untouched: *"The Sight Ecology block. The EA table and every alchemy move. Both 3-2-1 blocks. Draw the Axis. The four Walk Back moves, in count and in order. Every fix-question. Every named distortion game."* It called the Walk Back's mass *"the section she stays for."*

**6. Marginalia continuity breaks.** Irix Vale and Corin Ash are gone. Orr's closing marginalia says *"Five of them and Bram, all in my margin"* and *"six people have now put the opposite in writing."* The rewrite has three teachers plus Bram. Corin's plant is gone too: *"You know the sound he makes when he says he is fine. We are counting on you having noticed,"* which is what Orr's *"I am fine"* pays off.

**7. The rewrite fails the house voice checks.**
- `marginalia/review.py`: 1 BLOCK, a denying negation (ch8:139, *"The marker is not whether they thanked you. The marker is whether the work moved."*). The cut region reads clean.
- The scanner reads 38 plain-negation paragraphs in the rewrite (10.6 per 1,000 words) against 28 in the cut region (3.1 per 1,000).
- The rewrite repeats itself: *altitude* runs 10.2 per 1,000 words against 2.3; *"Most of what…"* opens 6 sentences; the answer to *"why do I have this gift"* appears twice (ch8:375 and 503); *"That sentence is what every move in this chapter is for"* closes two different sentences (ch8:401 and 532); two adjacent sections are titled *What Winning Looks Like*.
- ch8:503 breaks grammatically: *"The Damaged Self will tell you that if you see this clearly… why do you have this gift?"*
- The tracker reports all hard gates clean. The gate is clean. The voice linter is a separate step.

**8. The chapter has one exercise left.** Cut version: two 3-2-1 blocks, two "Try this now," four BAR captures, Draw the Axis, Read to Quest. Rewrite: one four-step practice, no BAR capture.

**9. "Forest" is overloaded.** ch8:203 uses *the Forest* for the inner landscape where the daemons sit. The rewrite uses *the forest* nine times for the Sage's altitude.

---

## What was lost, by component

| Component | Words | What it did |
|---|---|---|
| Sources note + Five Modes defined | 360 | Credit to Genpo Roshi, Wilber, Laloux; names the five capacities |
| Draw the Axis | 142 | The Which Game ↔ Which Altitude exercise, routed to Appendix F |
| EA table + five alchemy moves | 1,030 | Fear→Wonder, Anger→Triumph, Neutrality→Peace, Joy→Bliss, Sadness→Poignance |
| Five distortions with pre-action checks | 467 | "Before you switch, check…" |
| Stage Sequence + Sight Ecology | 388 | The loop as a lived minute; the tie to Ch1 and Ch3 |
| 3-2-1 Reclaim the One Who Went Anyway | 249 | Exercise |
| The Walk Back (Egan) | 703 | Four return moves |
| Damaged Self Up Close + 3-2-1 | 875 | The author's load-bearing-wall confession; the one-map limit; Irix and Corin marginalia |
| Game/Altitude mechanism + What You Take Out | 667 | Why the defect story sounds like humility; Escape Artist and Coach |
| Section 6 opener + Moves 1–5 with examples | 2,202 | Each move: what it is, example, working vs performed, the test |
| Domain section | 1,108 | Where to spend the view; four winning markers; the Tell |
| Damaged Self Bites + Read to Quest + One Rep | 864 | Five-Move Form run through the daemon; quest conversion |

Replaced by 3,598 words: scene 1,012 · cost 406 · Damaged Self 298 · carry-forward 309 · winning 618 · practice 945.

---

## The issues in the cut sections (measured)

Reading at `3b37e4d`, region lines 307–828, 9,070 words:

- **Hard gate:** 0. **Voice linter:** clean. **Diet:** 0.38–1.04 on every counter. Every counter is under the 1.30 heavy line.
- **Scanner, by paragraph:** 28 plain negation, 23 *X rather than Y*, 12 and-chain, 6 definite article with no referent, 3 *never*, 3 *X, not Y*, 2 trailing qualifier, 1 each of *not X but Y*, universal assertion, dangling transitive. One BINARY (*"not pleasant, but it is fun"*).
- **Soft:** 12 fragments, 11 dead verbs, 28 empty head nouns, 2 orphan *this*.
- **July diagnosis flags still open at `3b37e4d`:**
  - ST-3: four overlapping five-item sets.
  - ST-4: Return precedes Release at ch8:644 against See → Switch → Serve → Release → Return at 463–467.
  - CN-4: the Walk Back is the book's only four-move sequence.
  - CN-9: "EA" unexpanded in the table heading.
- **Fixed since July and worth keeping:** examples and tests on Moves 3–5, six games → four, the Appendix F route, the gate-walk locator, the domain section (CN-8).
- **Present in both versions (first half, untouched):** CN-1 the Vulnerable Child at ch8:251 (and `ch9:508`) *(Corrected 2026-09-23 by the open-items panel: the Vulnerable Child is canon. `back_matter/glossary.md` defines her as the Player at the center of the Forest and says her gift is "carried up at Ch 8 §3." Ch2:393 names her. The July flag calling ch8:251 a retired term was wrong.)*; CN-2 the daemon roster that omits the Emotional Body and still says "seventh"; ST-6 the Horizon digression ahead of the definition.

---

## Filling the difference

Chapters 3–7 run 12,228–15,724 words. Chapter 8 at 9,670 is the shortest Face chapter by about 2,500 words. A count is a poor target. The August record shows the book was judged long at 404 pages and the Sage chapter was left alone on purpose. The target is the list of functions in findings 1–8.

Any restored text goes through the review pass, and each hit is rewritten in the prose or ledgered with a reason. Nothing is handed back as "yours."

**The axis:** what the Sage does (moves a reader can copy) ↔ where the Sage stands (the altitude and the ground).

Word counts below are estimates from the component table.

- **A. Restore and repair (the "does" pole).** Return sections 4–6 from `3b37e4d`. Clear the scanner hits and close ST-3, ST-4, CN-4, CN-9. The altitude scene is dropped. Roughly 15,000 words before the hit-clearing trims it.
- **B. Rebuild on the rewrite (the "stands" pole).** Keep the rewrite as the spine. Write the domain section, five Moves, Five-Move bite, quest conversion, exercises and marginalia fresh in the altitude frame. That is new prose in bulk, and findings 2 and 7 have to be fixed in it. Roughly 13,000 words.
- **C. Altitude as the frame, Moves as the practice (both).** Restore the cut structure. Keep the rewrite's cost section and hiring-meeting scene and move them. The scene serves as Move 1's extended example. The claims that the Sage does not belong at the table get reworded so Section 1 and Section 3 stand. 13,200 to 14,700 words, depending on whether the EA alchemy block (1,030) and Walk Back (703) come back in full.

**Recommendation: C.** It answers finding 2 and keeps the rewrite's one strong passage. A restores the structure and loses that passage. B takes the most new writing. Wendell picks before anything is built.
