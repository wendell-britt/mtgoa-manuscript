# Book Work Tracker — MTGOA
**Created:** 2026-04-14
**Last Updated:** 2026-08-03
**Status:** All 8 chapters complete — Editorial Pass Phase

---

## Session — 2026-08-06 · Ch2 placement bridge, SIM-001 rerun

**Approved and applied.** A Pilot 0 desk simulation found one repeated failure
in Ch2's Second Move: a reader could either avoid speaking or turn a body-read
into self-aware disclosure that made the listener contain them. The approved
bridge now asks whether the statement is theirs to name in that context, whether
it helps or burdens the listener, and which condition, need, or boundary it
identifies. When trust is insufficient, it offers a smaller move instead of
forced intimacy.

**Rerun:** P-03 moved from private consolation to a condition-focused agenda
ask; P-04 moved from urgency disclosure to a permission-based, feedback-scoped
prototype request. Both counterpart paths included a credible no or redirection.
This is a desk-simulation result, not human-reader validation.

**Verification:** Exact insertion anchor matched once; `dupes.py` clean; `git
diff --check` clean. `gate.py` remains at four body hits, all pre-existing in
Ch9 and none introduced by this edit. Full rerun record:
`editorial_reports/2026-08-06/SIM_001_CH2_PLACEMENT_RERUN_2026-08-06.md`.

---

## Session — 2026-08-06 · Pilot 0 resumed, P-06 spectator test

**Desk pilot complete.** P-06 begins with no invitation, role, or standing in
the local library group. The revised Ch2 bridge distinguishes that
insufficient-trust condition from avoidance and routes the reader to a smaller,
permission-based first contact. The coordinator redirects the persona from a
strategy conversation to a routine shift or unrestricted donation; the persona
accepts the redirect without seeking a more flattering role.

**Result:** no new repeated action-conversion failure across the three fictional
cards. This is not validation with actual readers. Next research layer is
voluntary human-reader calibration. Full trace:
`editorial_reports/2026-08-06/PILOT_0_P06_RESUMED_2026-08-06.md`.

---

## Session — 2026-08-06 · Mindset shift and action-scaffold audit

**Desk analysis complete; no canonical prose changed.** The audit traced the
mindset shift, scaffold, and first consequential action in every canonical
chapter. Ch1–Ch2 establish interior agency; Ch9 establishes an accountable
feedback loop. The recurring Ch3–Ch8 quest instruction is the pressure point:
it makes action concrete but does not consistently carry forward the relational
placement test developed in Ch2 and made operational in Ch7 and Ch9.

**Next desk test:** run a no-standing card across Ch3–Ch8. A valid result may
be a permission request, bounded contribution, appropriate support, or a
deliberate step-back; it should not be mislabeled avoidance. No revision is
proposed for canonical application until that cross-Face simulation identifies
a repeated failure.

**Post-ship v2 backlog:** voluntary human-reader calibration of the desk
findings, with pre-read context, post-chapter checks, and a 7–14-day follow-up.
It is intentionally not a release gate. Full audit:
`editorial_reports/2026-08-06/MINDSET_SHIFT_AND_ACTION_SCAFFOLD_AUDIT_2026-08-06.md`.

---

## Session — 2026-08-06 · Pilot 1, no-standing cross-Face test

**Desk simulation complete; no canonical prose changed.** P-07, an adjacent
nonprofit convenor with resources but no coalition role, was run across Ch3–8.
Ch7's explicit trust prerequisite and Ch8's correction/usefulness tests route
the reader to a narrow resource offer or clean step-back. Ch3, Ch4, and Ch6
repeatedly risk converting a valid read into an unearned mandate to speak,
confront, or redesign.

**Finding:** relational placement is a repeated action-conversion issue, not a
Ch2-only edge case. The next editorial hypothesis is a short portable gate
before the first recurring Ch3 quest instruction; it requires a rerun against
P-03, P-04, P-06, and P-07 before any canonical proposal is made. Full trace:
`editorial_reports/2026-08-06/PILOT_1_P07_NO_STANDING_CROSS_FACE_2026-08-06.md`.

---

## Session — 2026-08-06 · SIM-002, Ch3 relational-placement gate rerun

**Desk rerun passes; no canonical prose changed.** A proposal-level gate before
Ch3's first recurring quest instruction was tested against P-03, P-04, P-06,
and P-07. It routes readers with standing to the smallest accountable action
they control, and readers without the relationship or mandate to a
permission-based first contact, bounded contribution, appropriate preparation,
or clean step-back.

**Regression watch:** the gate must not make a permission request into a demand
for unpaid education, reassurance, or a bespoke role. If proposed for canonical
use, include a bounded-offer/refusal-safe example and rerun P-04 and P-07.
Full rerun record:
`editorial_reports/2026-08-06/SIM_002_CH3_RELATIONAL_PLACEMENT_GATE_RERUN_2026-08-06.md`.

---

## Session — 2026-08-06 · Ch3 relational-placement gate

**Approved and applied.** The four-card SIM-002 rerun established a repeated
placement failure in the recurring quest form: readers could collapse standing,
authority, first contact, and lack of mandate into a single demand to act. The
approved gate now asks what the reader can name, offer, or change; who can say
no, redirect, or correct the read; and routes readers with standing to the
smallest action they control. When the relationship is absent, it directs a
permission ask, one bounded offer, appropriate preparation, or clean step-back.

**Final wording:** “do not seize the decision” replaces the proposed “do not
take the room,” which tripped the manuscript's banned-term gate. The semantic
rule is unchanged.

**Verification:** exact anchor matched once; `dupes.py` clean; `git diff
--check` clean. `gate.py -v` has four pre-existing body hits in Ch9, all for
“thing”; the new Ch3 prose introduced none. The applied safe-edit script is
`instruments/apply_ch3_relational_placement_gate.py`.

---

## Session — 2026-08-03 · Jordan arc, Chapters 7–9

**Approved and applied.** Nine review-approved replacements across Diplomat,
Sage, and Player make the final developmental movement explicit:
Invitation → Accountability → Transfer.

- **Ch7:** Terms can be accepted, refused, or counteroffered; unequal power
  limits the freedom of an answer; a source can refuse translation.
- **Ch8:** Perspective is tested against the people it concerns; naming a game
  becomes a corrigible offer; Kit determines what help is useful.
- **Ch9:** Affected people can correct the problem definition; feedback is an
  invitation rather than extracted labor; handoff includes the means to alter
  or end the practice.

**Verification:** All nine exact source anchors matched once. `dupes.py`,
`gate.py`, and `git diff --check` passed. `prose_diet.py` remains clear for the
touched chapters except the pre-existing Ch7 passive-voice flag (1.43).

---

## Session — 2026-08-01 · ch2 leaves the fiction

Branch `claude/treatise-wendell-content-boundaries-78sq54`. Full ruling in
`specs/SPEC_CH2_FRAME_2026-08-01.md`.

**The defect.** Ch2 was claimed twice and reconciled never: DL-19 names it as Wendell's frame
and the only legal home for his real biography, while `HANDOFF.md` says Bram Tull writes it.
`SPEC_TWO_HANDS` moved all six treatise bylines to the close of Section 3 so a document would
stop overclaiming the chapter under it — ch2 was not in that set, so it kept the last
top-of-chapter byline in the book, over the chapter that is most unmistakably the author's.

**Never measured.** `seam_sweep.py` hardcodes `CHAPTERS = [3..8]`. Its own tiers run over ch2:
**BOOK 28, AUTHOR 13, CREDIT 2**, against 2/37/0 for all six cleaned treatises combined. Under
Bram's signature sat the 420-word George Floyd origin story, the only self-naming of the book
in the manuscript body (`ch2:241`), and credits to Carolyn Elliott, Robin Rice and Gerard Egan.

**Applied.** Bram removed entirely — `FRONT[2]`, `BYLINE_NOTE[2]`, `NOTES[2]` dropped;
`compile.py` `CHAPTERS` `[2..9]` → `[3..9]`; frame blocks 54 → 47. The 43 sites are not fixed,
they are made legal: with nobody fictional claiming the chapter, every one is Wendell writing
his own frame. Bram survives at `ch8:584` and in the ch9 postcard, a pair that never depended
on ch2.

**The Headmaster's letter is boxed** — body in a blockquote under `<!-- LETTER -->`, heading
left outside so `build_book.title_of()` still finds it for the contents page.

**+340 body words to ch2**, two passages setting up the school as a teaching device, split as
Wendell ruled: Section 5 carries why the device exists, Section 10 carries how to read it. The
ch8 reveal is deliberately not set up in either — `MARGIN_ARC` rule 2 says nothing may pay for
it in advance.

Book-wide review clean on all six; shipcheck's four blockers are all pre-existing and none
touches ch2.

---

## Session — 2026-07-30 · the developmental beliefs, and the five-element confession

Branch `claude/self-sabotage-ally-beliefs-a9lhzu`.

**ch3 §5 — "What You Install Instead" (new subsection, +427 body words).** The six
Controller verdicts now come with the developmental belief that replaces each one,
in a three-column table: the verdict, the flat inversion that re-enters the same
court, and the belief that installs because it names a process rather than a
standing. Sits between the don't-argue-with-the-verdict paragraph and the
Feeling/Function hinge, whose opening pronoun was repointed at the named move. The
Section 7 recap names the second set, and its "separating them" got its noun.

**The six stay six.** "I'm not safe" was drafted in as a seventh and pulled back
out: sabotage begins with the Controller, and safety is the Protector's ruling.

**ch2 §6 — blanket bracing vs. vigilance (+93 body words).** Answers "not safe"
behaviorally instead, in "The Protector, up close": bracing everywhere is the
cheap way to do the job, and vigilance costs aim. Connects ch2's untargeted
vigilance that "just hums" to the threat-discrimination move already written four
paragraphs later. Chosen over a seventh belief on the ICA evidence — the 8 Gates
are the book's biggest stay-stuck risk, Protector is the gate this reader is
likeliest to claim as hers, and ch5 is praised in the ideal-reader report for
dropping the 6-beliefs block rather than extending it.

**ch3 §4 — the five-element confession (+202 body words).** Before the channel
table, in Wendell's first person: the five channels come from **wu xing**, the job
they were bent to, the correspondences moved, grief and fear not filed where the
tradition files them, and the tie back to Chapter 1's own admission about fluency
opening doors it closes for other people. Modelled on ch6's "A Note Before the
Concept" — name the suspicion, do not argue it away.

This closes the highest-severity defense trigger in the ideal-reader report, and
it was the only item on the open list that no branch was working. Half of it was
already closed: `appendices/ON_THE_SHOULDERS_OF.md` carries a strong wu xing and I
Ching credit and points at Kaptchuk. That appendix says *"As I confess in that
chapter"* — a confession that did not exist in any of the nine chapters until now.
Deliberately not duplicating the appendix's wording; the chapter admits, the
appendix sources.

**Word counts: deferred, not measured away.** They are wrong in `MANIFEST.md` and
`MANUSCRIPT_FILE_CANON.md` — 97,738 was true at `e662f84` and the register
fan-out plus the W8/W9 passes cut it to 96,468 without either doc being re-run.
`82898f5` on `claude/book-print-readiness-august-ar95mo` already fixed all four
docs more thoroughly than this branch did, and added `instruments/build_book.py`.
This session's own correction was reverted rather than left to conflict. **The two
branches report different totals (97,013 here, 98,332 there) because they measure
different trees**, and neither figure survives a merge — see below.

**Two parallel finishing passes are unmerged, and both edit all nine chapters.**
`claude/book-print-readiness-august-ar95mo` is 22 ahead of master and 35 behind,
last commit 39 seconds before master's. It closed front matter, back matter, the
generated TOC, the Five Channels appendix taking letter C, and the appendix
renumbering — none of which is on master. It also independently found the same
word-count error and the same "both hard blockers are already written" correction.
Deciding which line is canon is Wendell's call and blocks re-measurement.

**Both "hard print blockers" were already written and the docs said otherwise.**
`appendices/APPENDIX_F_POLARITY_MAP.md` (933 words) and
`appendices/APPENDIX_E_321_SHADOW_PROCESS.md` (1,063) are on master.
`MANUSCRIPT_FILE_CANON.md`'s "Still missing" section says they exist "not in the
project, not on any disk." `SPEC_PRINT_READINESS_2026-07-29.md` §1 found this
first, on the other branch.

**Gates, every counter against the pre-session commit:** `gate.py` body 0/0/0/0/0
plus the 2 pre-existing ch4 Ash token placeholders; `review.py` voice BLOCK 1 /
WARN 18 / INFO 3 and body BLOCK 28 / WARN 43 / INFO 162, both identical; anchors
clean; `compile.py --verify` byte-identical; `dupes.py` clean. New prose scored
under baseline on all five `prose_diet.py` measures. `/no-ai-slop` run on both
drafts before insertion.

**Still open after this session:** front matter, back matter and the TOC, all
drafted on the print-readiness branch and none on master. The ten front-matter
facts and R8 are Wendell-only. `⟦ASH-AGE⟧` and `⟦ASH-SPAN⟧` were filled
2026-07-30 and the gate now reads 0 on all four surfaces.
The retired 0-indexed chapter numbering survives in appendix cross-references on
master; the print-readiness branch has already renumbered them.

---

## New Direction — Compression and Promise Clarification

First-round editorial feedback says the manuscript is doing too much at once. The next pass is now about simplifying the promise, tightening the sellable core, and reducing Chapter 7 to its key allyship milestones.

Current north star:

**Mastering the Game of Allyship helps people who want to show up more effectively as allies learn why allyship keeps failing, see the game underneath the term, and use the Effective Allyship Formula to build real-world relationships, reduce harm, and create the trust that leads naturally into bars-engine and coaching.**

Key doctrine:

- allyship is relational, consent-based, and trust-earned
- you can support a movement, but you ally with people
- each chapter should teach one idea, one tool, and one real-world test
- the book should feel like a concise transformation path, not a comprehensive textbook

Reference memo:

- `editorial_reports/2026-06-09/CHAPTER_BY_CHAPTER_SIMPLIFICATION_BRIEF_2026-06-09.md`
- `editorial_reports/2026-06-09/CH7_CUT_LIST_AND_REWRITE_MAP_2026-06-09.md`
- `editorial_reports/2026-06-09/CH7_SECTION_BY_SECTION_REWRITE_PLAN_2026-06-09.md`
- `editorial_reports/2026-06-06/BOOK_PROMISE_AND_CH7_COMPRESSION_PLAN_2026-06-06.md`
- `editorial_reports/2026-06-06/BOOK_STRUCTURE_AND_FUNNEL_AUDIT_2026-06-06.md`
- `editorial_reports/2026-06-06/BOOK_STRUCTURE_COMPARISON_AND_SIMPLIFICATION_2026-06-06.md`
- `editorial_reports/2026-06-06/BOOK_STRUCTURE_COMPARISON_WILBER_ILP_AND_SIMPLIFICATION_2026-06-06.md`
- `editorial_reports/2026-06-06/BOOK_STRUCTURE_COMPARISON_EGAN_SKILLED_HELPER_AND_SIMPLIFICATION_2026-06-06.md`
- `editorial_reports/2026-06-06/BOOK_STRUCTURE_COMPARISON_ELLIOTT_EXISTENTIAL_KINK_AND_SIMPLIFICATION_2026-06-06.md`
- `editorial_reports/2026-06-06/MTGOA_PEDAGOGY_FUSION_PLAN_2026-06-06.md`
- `editorial_reports/2026-06-06/MTGOA_SIMPLIFICATION_PROTOCOL_FOUR_BOOKS_2026-06-06.md`
- `editorial_reports/2026-06-06/CH7_REVERSE_OUTLINE_TO_SIMPLIFIED_STRUCTURE_2026-06-06.md`
- `editorial_reports/2026-06-06/CH7_SIMPLIFIED_DRAFT_2026-06-06.md`
- `editorial_reports/2026-06-06/MTGOA_CHAPTER_JOURNEY_MATRIX_2026-06-06.md`
- `editorial_reports/2026-06-06/MTGOA_ALLYSHIP_WELLBEING_AND_FIVE_JOURNEYS_2026-06-06.md`
- `editorial_reports/2026-06-09/BARS_ENGINE_BOOK_COLLISION_SURFACE_MAP_2026-06-09.md`

Working decision:

- keep the Effective Allyship Formula as the strongest reader-facing promise
- keep the distortion/exile explanation and personal stories
- compress the long Sage/forest altitude journey into a shorter allyship-focused arc
- add a plain-language allyship definition near the front of the book
- keep bars-engine collision surfaces visible so the manuscript can hand off cleanly into deck and coaching products

Next editorial action:

- use the chapter-by-chapter simplification brief as the active pass guide for the final simplification round
- use the Ch7 cut list and rewrite map as the immediate editing guide for the Sage chapter
- use the Ch7 section-by-section rewrite plan as the line-level guide for the Sage chapter
- draft a Chapter 7 condensation spec that maps each remaining section back to the core allyship promise
- use the local source corpus as the chapter-structure model set
- simplify each chapter to a promise -> diagnosis -> teaching -> example -> practice -> summary rhythm where possible
- use the ILP modular pattern as the clearest model for chapter entry speeds and condensed practice layers
- preserve MTGOA's layered feel while assigning one main idea and one main tool per chapter
- synthesize the four-source structure set into one simplification protocol before touching more prose
- use the simplification protocol as the editing rulebook for Chapter 7 and for any other chapter that still feels overstuffed
- apply the Chapter 7 reverse outline first when simplifying the Sage chapter
- compare the simplified Sage draft against the current source draft before deciding what to merge back
- use the chapter journey matrix to keep each chapter focused on one milestone and one primary journey
- use the allyship / well-being memo to keep the book's definition of allyship relational, consent-based, and trust-earned

---

## Current Handoff — 2026-06-04

### Ch2-Ch8: Energy Ecology Continuity

Ch2-Ch8 now have the old numeric energy economy reconciled into the current ecology/capacity frame:

- Ch2 establishes **Energy Ecology** as the living-field question: which moves replenish, sustain, or hollow out the field
- Ch3 localizes the frame as **Will Ecology**
- Ch4 localizes the frame as **Stewardship Ecology**
- Ch5 updates the outcome table label to **Integrated Outcome**
- Ch6 replaces the old move labels and numeric **Energy cost** labels with **Alchemy 1/2** plus sustaining/costly capacity language
- Ch7 replaces **Move 1-5** with **Alchemy Move 1-5**
- Ch8 required no live cleanup

Decision:

- Keep **Energy Ecology** as the master term.
- Keep local ecology names only where they clarify a chapter's native face.
- Use sustaining/costly capacity language in later chapters instead of point totals.
- Do not reintroduce numeric energy scoring as a formal mechanic.
- Current terminology sweep note: Ch0 now bridges with a **fuel budget**; Ch2 and Ch4 use **skip** instead of the old rise-above language; Ch7 now prefers **escape / completion / alchemy** over the old rise-above language.

Supporting notes:

- `The Library/07 Book OS/07 Book OS/Spec Inbox/SPEC_CH2_ENERGY_ECOLOGY_REPLACEMENT_2026-06-04.md`
- `The Library/07 Book OS/07 Book OS/Spec Inbox/SPEC_CH3_CH4_ENERGY_RECONCILIATION_2026-06-04.md`
- `The Library/07 Book OS/07 Book OS/Spec Inbox/CH2_CH4_ECOLOGY_SEQUENCE_READBACK_2026-06-04.md`
- `The Library/07 Book OS/07 Book OS/Spec Inbox/SPEC_CH5_CH8_ENERGY_LANGUAGE_SWEEP_2026-06-04.md`
- `The Library/07 Book OS/07 Book OS/Spec Inbox/CH5_CH8_ENERGY_LANGUAGE_READBACK_2026-06-04.md`
- `The Library/07 Book OS/07 Book OS/Spec Inbox/APPENDIX_TERMS_ENERGY_ECOLOGY_AUDIT_2026-06-04.md`
- `The Library/07 Book OS/07 Book OS/Spec Inbox/CH6_PROSE_RHYTHM_PASS_2026-06-04.md`

Next focus:

- Run a Ch6 focused readback after the prose rhythm pass, then decide whether to continue chapter-level rhythm work.

### Ch0: Tutorial + Benevolence Bridge

Ch0 now has:

- a live tutorial object: the issue that made the reader buy the book
- micro-moves through myths, resistance, Token, Ticket, Three Games, Six Faces, and first BAR
- a benevolence reframe bridge: care does not have to hurt to count; depletion is not proof that care is real

Decision:

- Do not cut Ch0 onboarding yet. The tutorial frame improved Capability trust and made the chapter feel more playable.
- Remaining Ch0 note: later light compression should target Token/Ticket density and repeated game-frame justification, not the tutorial object or micro-moves.
- Add one Ticket benevolence callback if returning to Ch0: "A real ticket is not private profit. It is the return of capacity: more life in you, more agency in them, more truth in the field."

Next focus:

- Move to Ch1 work before further Ch0 polishing.

### Ch1: Humane Teaching + Gates Tutorial Alignment

Ch1 now has:

- a humane teaching/consent frame that names how this game teaches: map -> move -> feedback -> try again
- a brief Genpo Roshi / Big Mind attribution that preserves lineage without interrupting play
- Gates framed as the mechanism of receptivity: help is received through the part guarding the door
- Gate 2 Controller aligned as standard-setter and polarity-holder, not only grip/control
- Gate 6/7 distinction protected: Victim tells stories about harm; Damaged Self holds the record of harm
- Gate 7 prompt revised to preserve first-person practice while keeping the allyship application

Decision:

- Do not compress the Gates sequence yet. The length is justified by the onboarding function.
- Compression, if needed later, should target repeated grip/exhaustion language in Gate 2 or transition density, not the playable Gate structure.
- Ch1's current editorial question is flow: does Section 6 move cleanly through Section 8 as a playable onboarding arc?

Supporting notes:

- `The Library/07 Book OS/07 Book OS/Spec Inbox/SPEC_CH1_HUMANE_TEACHING_CONSENT_FRAME_2026-06-03.md`
- `The Library/07 Book OS/07 Book OS/Spec Inbox/SPEC_GATE2_CONTROLLER_CONSISTENCY_2026-06-03.md`
- `The Library/07 Book OS/07 Book OS/Spec Inbox/CH1_HUMANE_TEACHING_TO_GATE4_READBACK_2026-06-03.md`
- `The Library/07 Book OS/07 Book OS/Spec Inbox/CH1_FULL_GATES_PLAYABLE_SEQUENCE_READBACK_2026-06-03.md`

Next focus:

- Run Section 6-8 readback before deciding whether to pause Ch1 or make one final micro-edit.

### Copy-Edit Runway: Editorial Style Inputs

The next-week copy-edit pass now has two new editorial style inputs in the repo:

- `editorial_reports/2026-06-04/MTGOA_Developmental_Editorial_Specification.pdf`
- `editorial_reports/2026-06-04/deep-research-report.md`

They line up with the editorial docs already in the repo:

- `SPEC_MANUSCRIPT_INTEGRATION.md`
- `MTGOA_EDITORIAL_AGENT_SPEC_v3.md`
- `EDITORIAL_PIPELINE_ALL_ENVIRONMENTS.md`
- `GATE_VOICES_CANONICAL.md`
- `CROSSCHAPTER_SPEC.md`

Backlog decision:

- Treat these two documents as the style baseline for the copy-edit week.
- Build or confirm the Wendell anchor corpus before broad copy-editing starts.
- Use the deep research report to drive the style-lint / Voice Anchoring Pass.
- Use the developmental editorial spec as the manuscript-level style reference.

Next focus:

- Convert these style inputs into a chapter-by-chapter copy-edit checklist and run it next week.

### Merged Editorial Strategy — old spine + new style layer

The repo now treats the new style materials as an added layer on top of the existing editorial spine, not as a replacement for it.

Reference memo:

- `editorial_reports/2026-06-04/EDITORIAL_GAP_ANALYSIS_AND_MERGE_PLAN_2026-06-04.md`

What stays authoritative:

- manuscript integration and chapter placement
- pipeline and human cold read workflow
- gate ontology and cross-chapter pattern rules
- tracker sequencing and backlog state

What the new materials govern:

- style-lint categories
- anti-AI artifact cleanup
- Wendell anchor corpus
- voice anchoring
- line-level repair for the copy-edit week

Backlog order for the merged strategy:

1. Confirm or assemble the Wendell anchor corpus.
2. Convert the deep research report into a usable style-lint checklist.
3. Run voice anchoring before broad copy-editing.
4. Keep detector scores as triage only.
5. Preserve structure unless a line-level repair reveals a real structural issue.

### Final Push Plan — AI artifact cleanup first, voice punch second

Before closing shop for today, the finishing plan is:

1. Strip AI artifacts from the manuscript using the research report as the lint source.
2. Apply the voice-anchoring pass to the cleaned spans.
3. Manually punch the voice up chapter by chapter.
4. Keep structural fixes limited to the few items that still protect the spine.

Reference file:

- `editorial_reports/2026-06-04/AI_ARTIFACT_CLEANUP_AND_VOICE_PUNCH_PLAN_2026-06-04.md`

### Chapter 7 Inkwell review notes

The Inkwell review comments for Chapter 7 are now folded into a concrete revision plan.

Reference file:

- `editorial_reports/2026-06-04/CH7_INKWELL_REVIEW_NOTES_RESPONSE_PLAN_2026-06-04.md`
- `editorial_reports/2026-06-04/CH7_IMPLEMENTATION_SPEC_2026-06-04.md`

Working order:

1. Thesis paragraph near the start.
2. Clean definitions for Shadow, distortion, and cost.
3. Gate signposting tied back to the thesis.
4. Short limit-case paragraph for urgent external action.
5. Tradition mapping for Big Mind, shamanic training, and the Faces.
6. Do-not-do examples for over-introspection and avoidance.
7. One institutional example.
8. Vocabulary normalization for Shaman / Forest language.
9. Quick-reference box for the eight Gates and five moves.
10. Comedy and Emotional Alchemy pass to make the chapter land as release, not lecture.

Implementation rule:

- Apply the spec to `chapters/ch7-sage/CHAPTER7_SAGE_FULL_DRAFT.md` first, then mirror the same final chapter state into the Inkwell upload copy if needed.

Status:

- Chapter 7 implementation applied to the source draft and mirrored into `Inkwell Upload - 2026-06-04/chapters/CHAPTER7_SAGE_FULL_DRAFT.md`.

---

## Chapter Completion Table

| Chapter | Face | Draft File | Lines | Sections | State |
|---------|------|-----------|-------|----------|-------|
| Ch1 | Shaman | `ch1-SHAMAN/CHAPTER1_FULL_DRAFT.md` | 534 | 11 (old template) | 🟡 EDITORIAL |
| Ch2 | Shaman | `ch2-SHAMAN/CHAPTER2_SHAMAN_FULL_DRAFT.md` | 900 | 7/7 | 🟡 EDITORIAL |
| Ch3 | Challenger | `ch3-CHALLENGER/CHAPTER3_CHALLENGER_FULL_DRAFT.md` | 673 | 7/7 | 🟡 EDITORIAL |
| Ch4 | Regent | `ch4-REGENT/CHAPTER4_REGENT_FULL_DRAFT.md` | 542 | 7/7 | 🟡 EDITORIAL |
| Ch5 | Architect | `ch5-ARCHITECT/CHAPTER5_ARCHITECT_FULL_DRAFT.md` | 482 | 7/7 | 🟡 EDITORIAL |
| Ch6 | Diplomat | `ch6-diplomat/CHAPTER6_DIPLOMAT_FULL_DRAFT_MASTER.md` | 566 | 7/7 | 🟡 EDITORIAL |
| Ch7 | Sage | `ch7-sage/CHAPTER7_SAGE_FULL_DRAFT.md` | 668 | 7/7 | 🟡 EDITORIAL |
| Ch8 | Player | `ch8-player/CHAPTER8_PLAYER_FULL_DRAFT.md` | 540 | 7/7 | 🟡 EDITORIAL |

**All chapters: ✅ SHIPPED → 🟡 EDITORIAL PASS. No chapters in DRAFTING state.**

---

## Editorial Pass Queue (Ordered by Priority)

### P0 — Must Fix Before Any Other Editorial Work

**🔴 A10 — the Examples teach self-advocacy, not allyship. Brief for the 15 unwritten.**
- Wendell 2026-07-29: "the biggest opportunity to give Jordan the gory details of how
  someone advocates for themselves vs advocating for other people."
- Counted all 20 existing `**Example:**` beats: **10 show the reader's own interests,
  8 show an abstract system, 1-2 show advocating for another person.** ch6's five are
  all systems design; ch9's five are all building your own thing; ch7's three are
  first-person lines about your own position.
- Jordan's craving is "show up for others without losing myself." The Examples teach
  the second half and barely touch the first, in a book about allyship.
- **15 Examples are still unwritten** (ch4 x5, ch5 x5, ch7 x2, ch8 x3), so this is a
  brief rather than a repair — received at the cheapest possible moment.
- Brief per Example, full version in WAVE spec §11.3: name who benefits; name the
  specific cost in the currency of the scene; show where the two kinds of advocacy
  diverge (self-advocacy risks reading as self-interest, other-advocacy risks reading
  as saviourism and risks getting it wrong on their behalf, which is Jordan's stated
  fear); at least two of each chapter's five should have another person as beneficiary.
- Does NOT license rewriting the 20 that exist to hit a ratio. ch3's attribution
  example is correctly self-facing. The imbalance is a gap in what was written.


**🔴 A9 — the Move template is inconsistent four ways; ch8 has none. DO FIRST.**
- Found auditing the STRONG Moves against the ICA per Wendell's ask.
- Jordan "will stop for a named move with a practice", so the practice must be
  findable. Measured:

      ch3, ch6, ch9   **What it is** / **Why it matters** / **Example** / **The test**, bolded  -> scannable
      ch4             The Situation / The Move / Why it works / In practice, UNBOLDED  -> partly
      ch5             **The test** only  -> weak
      ch7             **Why it works** only  -> weak
      ch8             NO LABELS AT ALL, continuous prose  -> not scannable

- ch8's Move 1 has every beat — situation, practice, payoff — and labels none of
  them, so Jordan must read the block to find the do-this.
- **The 11 STRONG Move NAMES all pass the ICA**: plain, verb-first, jargon-free.
  The problem is the container, not the naming.
- Fix: normalise to ch3/ch6/ch9's four bolded beats across all seven chapters.
  Editing, not authoring — the content exists in every chapter already.
- **Highest reader-value, lowest-risk item in the whole WAVE spec, and it is the
  prerequisite for the 12 new Moves**, which need a form to be written into.

**RULED — Show Up is the promise, not an over-weighting.** Wendell 2026-07-29:
"Show up is the impactful moves... the promise is that they will show up better. The
process of completing the process is teaching them about the other moves and how NOT
knowing those moves is stopping them from showing up." This closes the open question
in WAVE spec §6: action-weighting is a CHOICE. The five stages are a diagnosis plus a
payoff, not a balanced taxonomy — Wake/Open/Clean/Grow each name a reason the Show Up
misses. So 17 Show Ups is not 17 mislabelled Moves, it is COMPETING PAYOFFS, and the
12 new Moves each name what blocks that chapter's Show Up. Recorded as WAVE spec §8.


**✅ A7 — Seam 1 DONE 2026-07-29: the six BAR grids left the book**
- Wendell: "Taking them out makes sense, but let's keep em in the repo as things
  that we can design against." Done: `deck/BAR_GRIDS.md`.
- 6 grids, 120 cards, out of ch3-ch8. **Book load 219 -> 99 named units.**
- Kept on purpose: the framing paragraph naming the five basic moves as the
  WAVE-Spiral (that is the book stating its own spine), and `Drawing Against the
  Shadow`, which teaches the five stages in prose.
- Frame round-tripped, gate at the two R9 tokens, suite green.

**🔴 A8 — the 35 Moves do not run the WAVE. Spec drafted, needs a ruling.**
- `specs/SPEC_WAVE_REALIGNMENT_2026-07-29.md`. Wendell's Seam 3 ruling: each
  chapter should bring Jordan through Wake/Open/Clean/Grow/Show. ch3 already SAYS
  this on the page. Zero of the 35 Section 5 Moves is tagged to a stage.
- Payoff: 35 differently-named moves become ONE sequence seen seven times. Largest
  single reduction left, and it deletes no content.
- Map scored: **11 STRONG, 12 MEDIUM, 12 WEAK** (corrected from 14/12/9). Move 1 is already Wake Up in all
  seven chapters, so the structure is one-fifth built consistently book-wide.
- **The finding that outranks the realignment: Show Up carries 17 of 35 Moves;
  Open Up and Grow Up carry 3 each, with ZERO strong fits between them.** The book
  under-teaches Open Up — its own addition to Wilber's four, the Shaman's whole
  contribution, the stage ch7:540 calls "the move this chapter's daemon exists to
  prevent", and the stage APPENDIX_C drops entirely (A6).
- True scope is not relabelling: it is **12 new Moves**, each an Open Up or Grow Up
  written where a duplicate Show Up now sits. That is authoring, not editing.
- Recommended split: tag the 11 STRONG now (ships, claims only what the map
  supports); the 12 framings and 12 replacements are second edition with the Open Up
  gap as the brief.
- Open question for Wendell (spec §6): is action-weighting a flaw or a choice? For a
  reader who fears doing harm and wants to show up without losing herself, the
  missing stages are the ones serving the second half of that sentence.


**🔴 A4 — ch3 does not teach the two operations. LOAD BEARING.**
- Wendell 2026-07-29: "We need to make sure chapter 3 actually teaches emotional
  alchemy. This is load bearing." Audit: `specs/SPEC_SYSTEM_COLLISIONS_2026-07-29.md`
- ch3 is titled "Emotional Alchemy as the Foundation of Real Allyship", says
  *emotional alchemy* 10 times, and contains `Transmute` 0, `translate` 0,
  "two operations" 0. The chapter that exists to teach EA teaches neither operation.
- It answers "how do you do it" with the WAVE-Spiral instead. So the WAVE-Spiral
  occupies the slot canon assigns to Transmute/Translate, and the book never says
  how they relate. **This IS the WAVE/EA collision Wendell asked about, and it has
  not been dealt with or named.**
- Sound already: the five channels, all five completions, charge-first, the
  Controller, the five-stage spiral. The gap is only the operations layer.
- F1: ch3 names the two operations and states which layer WAVE occupies. The
  three-layer reading (Process / operations / WAVE-as-practice) is in the audit §1
  — the WAVE-to-operation mapping there is an inference and needs Wendell's check.
- F5: the Emotional Process lands in ch3 too. RULED IN by Wendell — see A5.

**🔴 A5 — the Emotional Process enters the book. RULED.**
- Wendell 2026-07-29: "The emotional process is part of emotional alchemy. It's
  gotta be in the book." E6 is closed, answer yes.
- Stimulus -> Emotional Activation -> Impulse -> Controller -> Skeptic ->
  Conscious Action. Currently absent: *Stimulus* and *Impulse* appear 0 times.
- Doctrinal, not editorial: canon puts Controller and Skeptic inside the HEALTHY
  sequence ("Wisdom emerges from cooperation rather than domination") where the
  book runs them mainly as daemons. Emphasis rather than contradiction — ch3 and
  ch4 both carry the healthy reading, so there are anchors.
- Home: ch3, with A4. The Process reframes the Controller chapter-work as a stage
  seized rather than a villain, which strengthens what is already there.

**🟠 A6 — WAVE is four moves in the glossary, five in every chapter**
- `APPENDIX_C:34` and `:60` both say four (Show/Clean/Wake/Grow), dropping
  **Open Up**. ch3-ch8 BAR grids all use five. ch3:235 says five stages. The deck
  arithmetic needs five: 5 x 4 domains = 20 cards, 120 total; four would give 96.
- The four are Wilber's original; Open Up is this book's addition and the stage
  ch7:540 says its daemon exists to prevent.
- Fix: both glossary entries to five, naming Open Up as the extension. Mechanical.


**🔴 A0 — Emotional Alchemy canon is LOCKED; reconcile the drift**
- **Priority: HIGH.** Locked 2026-07-29 by Wendell: "we need to lock in the
  canonical version of emotional alchemy because it's drifted."
- Canon: `specs/SPEC_EMOTIONAL_ALCHEMY_CANON.md` §1, verbatim. Single authority.
- Supersedes: `EMOTIONAL_ALCHEMY_TRANSLATOR.md`,
  `SPEC_EMOTIONAL_ALCHEMY_TRANSLATOR.md`, `AGENTS.md` EA Standards,
  `LEARNING_METABOLISM_CH6` §14, and ch6/ch7's local taxonomies.
- **Canon has TWO operations: Transmute and Translate.** Four different
  taxonomies are currently live in the repo, three of them with three operations
  each. `Generative` and `Control` were never operations — they were the two
  directions of Translate (the Wu Xing nourishing and overcoming cycles).
- Sound already, measured: the five element/emotion pairs, all five satisfied
  states, the three operating ranges, charge-first, and all nine of ch7's
  Translate keyings. The drift is in the operation vocabulary only.
- Steps: E1 settle names (retire `Transcend` x4, `neutralize` x3, `Control` as an
  operation x15). **E2 — SIX-FACE PANEL REPORTED 2026-07-29**,
  `specs/PANEL_E2_CONTROL_MOVES_2026-07-29.md`. 5-1 these are a third category,
  not an alchemy operation. `Control` dead 6-0, because canon's own closing line
  reads "Many self-help systems teach emotional control. Emotional Alchemy teaches
  emotional cooperation." Name split 2-2-1-1, so evidence decides: **Discipline**
  recommended — covers all 12 where Check covers 8, already shipped at ch7:286,
  and keeps the cost connotation both chapters already carry. **Awaiting Wendell:**
  ratify `Discipline`, or take the Regent's fallback `Practice`. E3 rewrite ch7:175, the book's own definition, which names
  the three ranges as if they were operations. E4 put the two axes in ch3 via the
  figure. E5 carry the Core Function column into ch3's table. **E6 Wendell:** does
  the cooperative Emotional Process sequence (Stimulus -> ... -> Controller ->
  Skeptic -> Conscious Action) enter the book? It reframes Controller and Skeptic
  from antagonists to stages — doctrinal, not a copy-edit. E7 point every
  superseded file here, or all of the above regenerates.
- Figure: `figures/FIGURE_3_1_TWO_AXES_BW.html` — black and white per Wendell,
  channel identity by dot fill not hue so it prints in one colour.
- Check: `grep -rin "transcend\|neutralize" manuscript/` and
  `grep -rn "\[CONTROL\]\|Control Move\|Neutral Channel" manuscript/` both 0.

**✅ A3 — "The Face" means two different sets of six — FIXED 2026-07-29**
- Priority: MEDIUM-HIGH. Same class of bug as Neutral Channel, found while
  locking EA canon.
- `appendices/APPENDIX_C_KEY_TERMS.md` defines **The Face** as "one of six
  interior voices (Protector, Controller, Skeptic, Fixer, Victim, Damaged Self)."
  The manuscript uses "the six Faces" **26 times** to mean Shaman, Challenger,
  Regent, Architect, Diplomat, Sage.
- Two different sets of six share the name, and the glossary — the one place a
  confused reader looks — defines it as the other one.
- RESOLVED. Not a judgment call: the correct definition was overwritten by the
  2026-06-04 trailing-promote pass and the pre-pass backup still carries it.
  Restored from `APPENDIX_C_KEY_TERMS_backup_2026-06-04_pre-trailing-promote.md`.
  The displaced text was a **Gate** definition: `APPENDIX_C:36` says each of the
  eight Gates "has a specific voice", `ON_THE_SHOULDERS_OF:44` lists exactly those
  voices as the Gates', and the entry's own cross-reference read "See also: Gate,
  Vulnerable Child". Check: `grep -c "Shaman, Challenger, Regent"` reads 1.


**🔴 A1 — Strip the deprecated bracket move tags (28) and settle *Neutral Channel***
- **Priority: HIGH. Print blocker.** Set 2026-07-29 by Wendell.
- Spec: `specs/SPEC_BRACKET_TAGS_2026-07-29.md`
- Files: `manuscript/ch7.md` (23 tags), `manuscript/ch8.md` (5 tags), `AGENTS.md`
- Issue: `**[DISSATISFACTION → SATISFACTION]**`, `**[TRANSLATE]**` and
  `**[CONTROL]**` are production tags in shipped prose. Deprecated 2026-06-03 by
  `SPEC_WB8_ARTIFACT_SWEEP`, signed off as complete, and still in the book: the
  fix landed in the retired `chapters/` tree and the acceptance grep only looked
  there. ch1–ch6 and ch9 carry none, so two of nine chapters ship a mechanic the
  rest of the book does not use.
- Reader impact: none of the terms in the tag is ever defined in the manuscript.
  Jordan's logged number-one drop-off trigger is jargon without translation.
- Steps, in order:
  1. **ANSWERED 2026-07-29 by six-face panel** — `specs/PANEL_NEUTRAL_CHANNEL_2026-07-29.md`.
     6-0 that ch7 must change; 5-1 that the name belongs to Earth/Neutrality.
     Awaiting Wendell's ratification (Q1), plus two independent scope calls: does
     the move taxonomy go into ch3 (Q2, the Architect's dissent), and does ch7's
     `Channel 1-5` become `Mode 1-5` (Q3, the Sage's addition). Original question,
     kept for the record: **Wendell's call.** Does the name *Neutral Channel* belong to
     Earth/Neutrality (the emotional channel taught in ch3) or to the structural
     Control move type (ch7's 11 uses)? The April ruling in
     `LEARNING_METABOLISM_CH6` §14 says *"NOT an emotion type."* The July ruling
     says *"one of the emotional alchemy channels."* Both cannot describe the same
     eleven lines. **Nothing else here should be edited until this is answered**,
     because the answer decides whether step 4 is one sentence or eleven headers.
  2. Strip all 28 brackets. Mechanical, one script, abort-before-write.
  3. Settle the ch7 format split in the same pass: Bridge-Builder uses
     `Translate 1` / `Control 1`, the other four channels use `— From X to Y` /
     `— Neutral Channel: X Pattern`. Both forms currently ship. Recommend the
     numbered form throughout, to match `Alchemy 1` / `Alchemy 2` beside it.
  4. Define or relabel per step 1.
  5. Fix `AGENTS.md` EA Standards, which still documents the bracket as canon.
     **Without this the tags regenerate** and step 2 is temporary.
- Check: `grep -c "\[DISSATISFACTION\|\[TRANSLATE\]\|\[CONTROL\]" manuscript/ch*.md`
  reads 0, and the same grep on `AGENTS.md` reads 0. Against `manuscript/`, never
  against a parallel tree — that scoping error is what hid this for two months.

**🔴 A2 — Re-verify every WB-* artifact sweep against `manuscript/`**
- **Priority: HIGH.** Opened by A1, same root cause.
- Issue: `SPEC_WB8_ARTIFACT_SWEEP` was fully signed off and fully false where the
  book lives, because its acceptance greps were scoped to `chapters/`. That tree
  is now retired, so any sweep verified the same way is unverified today.
- Fix: re-run each sweep's acceptance greps against `manuscript/` and record what
  fails. Do not assume a checked box means a fixed book.

**NOTE — the two P0 items below predate the `manuscript/` canon and cite retired
paths.** `chapters/` was retired at `4172d7a`. Both need re-scoping against
`manuscript/` before anyone works them, and both may already be done — this is
exactly the A2 problem.


**Ch6 Channel Reorder + Format Normalization**
- File: `ch6-diplomat/CHAPTER6_DIPLOMAT_FULL_DRAFT_MASTER.md`
- Issue: Channels out of sequence (Channel 5 written before Channel 2); H1 headers instead of H2
- Fix: Reorder to Bridge→Translate→Hold→Repair→Price; normalize to `## Section N:` format
- Size: Reorder only, no new content
- Owner: Editorial pass

**Ch0 Rewrite (New)**
- File: `ch0-infinite-arcade/CHAPTER0_DRAFT.md`
- Issue: Content from drafts needs consolidation into single chapter file; GM section v3 exists
- Fix: Consolidate GM_SECTION_v3 into CHAPTER0_DRAFT, write missing sections
- Status: PARTIAL (147-line GM section exists, rest needs writing)

### P1 — Hedge Reduction (tracker metric)

| Chapter | Hedge ratio (per 1K words) | Priority |
|---------|---------------------------|----------|
| Ch8 | 2.64 | 🔴 High |
| Ch7 | 1.41 | 🟠 Medium-High |
| Ch1 | 1.0–1.2 | 🟡 Medium |
| Ch2–Ch6 | 0.5–1.0 | 🟢 Low |

### P2 — Template Normalization

Ch1 uses 11-section template (old). Ch2–Ch8 use 7-section template. Ch1 is complete for its template — not a gap, just different format. No changes needed to Ch1 structure.

---

## What "Editorial Pass" Means Here

The editorial pass is **formatting + ordering cleanup**, not new content writing. Specifically:
- Ch6: channel reorder + header format
- Ch0: consolidate drafts + write missing sections
- All chapters: hedge reduction (language, not content)

**What is NOT needed:**
- No chapters need new sections written
- No chapters need new EA moves written
- No "gap analysis" — all 7 sections exist in all 8 chapters

---

## Running the Audit Yourself

Before declaring any chapter "needs work," run:

```bash
# Check section count
grep -c "^## Section\|^# SECTION" manuscripts/chapters/<ch>/CHAPTER*FULL*.md

# Expected: Ch1=11, Ch2-Ch8=7
# If count matches → state is "EDITORIAL PASS"
# If count doesn't match → log the missing section
```

**Rule:** "Section count matches template" = "EDITORIAL PASS." Only "section missing" = "DRAFTING."

---

## Active Editorial Items

### Ch6: Channel Sequence Fix
- Current: Bridge(1) → Price-Namer(5) → Translator(2) → Field-Holder(3) → Repairer(4)
- Target: Bridge(1) → Translator(2) → Field-Holder(3) → Repairer(4) → Price-Namer(5)
- Action: Reorder the 5 channel sections within S3; change H1 `# SECTION` to H2 `## Section`
- No new content needed

### Ch0: Consolidation + Missing Sections
- GM section v3 draft exists: `GM_SECTION_v3_2026-04-22.md`
- Missing: Token System, Ticket System, Three Game Types, Why Gamify, Six Faces Ladder, Entering the Arcade
- Action: Consolidate v3 into CHAPTER0_DRAFT; write remaining sections

---

## Night Research Loop

| Status | PAUSED |
|--------|--------|
| Note | Resume when editorial pass is complete |

---

## Key Files
- `CHAPTER_COMPLETION_AUDIT.md` — root cause analysis of the false-loop pattern
- `MTGOA_6FACE_CHAPTER_STRUCTURE.md` — 7-section template (Ch2–Ch8)
- `MTGOA_BOOK_WORK_TRACKER.md` — this file

---

## ❌ Do Not Use Old Gap Analysis Language

The following tracker language is now **stale** and incorrect:
- "Gap Analysis — In progress"
- "Missing Systems"
- "Chapter-by-Chapter Coverage — Gaps"
- "Write Big Mind Voices chapter"
- "Write Fred Taxonomy chapter"

These were accurate during DRAFTING. All chapters are now in EDITORIAL state. The tracker has been updated to reflect this.

**Updated: 2026-04-27**
