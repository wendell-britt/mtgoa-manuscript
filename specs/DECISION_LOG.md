# DECISION LOG — the single editorial ledger

**Created 2026-07-31** per `specs/EDITORIAL_OPERATING_SYSTEM.md` and
`specs/SPEC_EDITORIAL_OS_INTEGRATION_2026-07-31.md`. Only items in this log
become editing work. Rejected ideas stay rejected. New rulings in spec
documents get entered here the day they are made; this file is the index, the
specs hold the argument.

Format: `ID | location | reader problem | evidence | decision | intended result | status`

## Standing rulings (seeded from the specs, decided)

| ID | Location | Reader problem | Evidence | Decision | Intended result | Status |
|---|---|---|---|---|---|---|
| DL-1 | book-wide | Voice defects flattening the prose | `MANUSCRIPT_FILE_CANON.md` standing rules | Banned: *room*, *quiet(ly)*, *genuinely*; no sentence-initial And/But; no negation stacks; A0 patterns banned | `gate.py` reads 0 on four surfaces | DECIDED, enforced |
| DL-2 | book-wide | Denying negations stage a beat instead of holding an axis | `MANUSCRIPT_FILE_CANON.md`, ruled 2026-07-29 | Four-move fix (cut / essence / synthesize / voice), run as one pass | 2 remaining book-wide | DECIDED |
| DL-3 | 536 construction sites | Constructions substituting for content | Three keep-tests, Wendell's ruling | Every site presumed cut; survives only on Function · Earned · Non-substitutable | Burden of proof on keeping | DECIDED |
| DL-4 | all treatises | Register drift read as defect | `FACE_AUTHORS.md`, ruled 2026-07-28 | The Face authors every section; bylines, not re-voicing | Drift converts to characterization | DECIDED |
| DL-5 | Head material | Heads read as exhibits, not people | `HEAD_VOICE_DIAL.md`, Wendell 2026-07-30 | Craft mastered, satisfaction still reaching, learning edge open and adjacent | Masters still learning, per the book's ethos | DECIDED |
| DL-6 | marginalia | Margin held to a lower bar than body | Ruled 2026-07-29 | The gate applies to the margin as its own scored surface | Both surfaces at 0 | DECIDED |
| DL-7 | book-wide register | Short-declarative register defended as voice | `SPEC_REPETITION_AND_CUTS.md`, three outside controls + *Igniting Joy* | It is drift, not voice; `prose_diet.py` targets *Igniting Joy*, never the book's own average | The bar is Wendell's voice working | DECIDED |
| DL-11 | book-wide | Copula density 2.14× the control | `SPEC_REGISTER_2026-07-29.md` | — | — | OPEN, awaiting Wendell |

## Closed — verified by instrument 2026-07-31

**These three were seeded from `MANIFEST.md` and were already ruled.** The
manifest was stale; `build_book.py` and `grep` settle all three. This is the
repo's own standing lesson arriving on the first day the log existed: *do not
plan from a claim in a planning document without running the instrument.*

| ID | Location | Evidence | Ruling | Status |
|---|---|---|---|---|
| DL-8 | Appendix C | `appendices/APPENDIX_C_KEY_TERMS.md` header: retired 2026-07-30 by Wendell, off the spine, unreferenced. `build_book.py` seats Appendix C = `APPENDIX_C_FIVE_CHANNELS.md`, 1,206 words | Glossary retired; C is The Five Channels in Practice | CLOSED |
| DL-9 | `ch3:415` (was cited as `ch3:400`) | Reference reads *Appendix C: The Five Channels in Practice*; that letter now exists; `build_book.py` reports no UNPLACED | Lettered. Reference resolves | CLOSED |
| DL-10 | "Head Sura" | Appears in **zero** chapter files and **zero** marginalia insertions. Only `FACE_AUTHORS.md` quoting a note that never shipped | Not a canon conflict and not a print blocker. Spec hygiene only | CLOSED |

## Open items that block or shape print

| ID | Location | Reader problem | Evidence | Decision | Intended result | Status |
|---|---|---|---|---|---|---|
| **P0** | `ch1:181`, `ch1:269`, `ch7:500` | **Three placeholders print verbatim, including an authoring note addressed to Wendell** | `placeholders.py` on merged master 2026-08-01: **3 hits, all still present.** `gate.py` passes clean on all four surfaces — it has no placeholder rule | ch7 testimony slot **CUT** (ruled; DL-19 Move 4 relocates the passage to `ch9:342`); ch1 visual marker **CUT**; ch1 app CTA **DEFERRED by Wendell**, links still being set up | Nothing addressed to the author reaches a reader | **BLOCKS PRINT — 3 sites.** Two are ruled with approved drafts and **unapplied**; the log previously read *2 of 3 closed*, which was a ruling mistaken for an edit. Application is held by DL-18 |
| **P0-b** | six shipping appendices — A, B, C, D, E, F | **Internal production metadata prints in the book** — file paths, approval records, a *Draft* status flag, and an instruction to the production team | 15 lines verified in `build/MTGOA_PRINT_2026-07-31.md`; `gate.py` and `build_book.py` both pass. `placeholders.py` extended and now reports 21 | **FIXED 2026-07-31.** `build_book.py` strips provenance in `read()`, the single funnel every component passes through. `placeholders.py` applies the same strip and keeps the rule as a regression guard — silent normally, fires if the strip breaks | Provenance stays in the repo, never reaches a reader | **CLOSED — 0 metadata lines in the build** |
| DL-16 | `back_matter/kickstarter_backers.md` | Backers promised a credit do not find one | `build_book.py` — GAP, spine assembles with 2 gaps | Supply the list, or drop the component | Spine builds with no gaps | OPEN — needs Wendell |
| DL-17 | `back_matter/enrollment.md` | Reader finishes the book with no next step | `build_book.py` — GAP; `MANIFEST.md` notes it waits on R1 | Write it, or ship without it | Spine builds with no gaps | OPEN — needs Wendell |
| DL-18 | branch protocol | Two sessions editing the same nine files produce work that cannot be cheaply reconciled | `editorial_reports/2026-07-31/BRANCH_COLLISION_CHECK.md`; swmp78 shares our merge-base and edited ch1–ch8 today; both branches merge clean at **0 conflicts** because file sets are disjoint | **This branch stays apparatus-only.** Merge it first (pure addition), then apply A2/A4 where the chapters are owned | No repeat of the 91-hunk collision | RULED |
| DL-12 | four `⟦…⟧` register tokens | None in canon | `gate.py` tokens column reads 0 on all four surfaces | Due only if the register pass extends to the other five Heads | — | DEFERRED, not gating |

## Book Architect scan — 2026-07-31

Full report with quoted evidence and disproof tests:
`editorial_reports/2026-07-31/ARCHITECT_WHOLE_BOOK.md`. Diagnosis only; no prose
was changed and the gate stayed green. Each of these is a Chapter 1 promise
measured against the eight chapters after it, or a prerequisite arriving after
the reader needs it.

| ID | Location | Reader problem | Evidence | Decision | Intended result | Status |
|---|---|---|---|---|---|---|
| A1 | `ch1:149`, `ch1:173`; 0 hits ch2–ch9 | Jordan sorts her quest into Chance/Skill/Passion and the taxonomy never returns | *"Everything ahead is built to strengthen your hand in all three"* — measured 0 occurrences in eight chapters | Narrow the ch1 claim, or seat the taxonomy | The book's stated spine is true | OPEN — recommend fix locally |
| A2 | `ch1:207`, `ch2:560`, `ch9:682`; silent ch3–ch8 | The sheet ch9 turns back to is nearly empty | *"a line added in every chapter ahead"* — promised 8, delivered 2 | Narrow the promise, or seat one line per chapter using ch2:560 as the template | The reader's record of her own change actually accumulates | OPEN — structural decision |
| A3 | `ch1:68`, `ch1:73` | *Helping the less powerful* — the paternalism myth — is named and never taken apart | 9 of 10 myths map to a teardown; this one returns 0 hits ch2–ch9 | Soften *"each one"*, or assign the orphan | The stated inventory is accurate | OPEN — fix locally |
| A4 | `ch8:183`, `213`, **`223`**, `297`, `307`, `327` | Five-term developmental scale, undefined, at **six sites**; `ch8:223` uses it as the answer-set to the Sage's central diagnostic | *"all the altitudes — Red, Amber, Orange, Green, Teal"*; `termdebt.py` NEVER DEFINED; Magenta absent book-wide | **Wendell 2026-07-31: CUT.** Replacement must carry the same weight — the six Faces are the taught answer-set, per `ch8:213`/`ch8:185` | No jargon without translation, and *which altitude is this?* still answerable | **RULED — cut, replacement required at `ch8:223`** |
| ~~A5~~ | `ch2:558`, `ch3:786`–`800` | **WITHDRAWN 2026-07-31 — the finding was wrong.** Domains are named with an Appendix A pointer in ch2 and defined in ch3 with a *You're winning when* test each. `termdebt.py`'s bold-gloss rule cannot match a gloss inside the bold span, so other NEVER DEFINED rows are suspect | — | — | — | CLOSED — no work |
| ~~A5-orig~~ | `ch3:772`, `791`, `795`, `799` | "One of the four" back-references a set she has not met | Domains NEVER DEFINED in body; defined only in Appendix A; ch3's own italic routing convention at `415`/`560`/`589` is not applied here | Add the pointer in the existing convention | Prerequisite reachable where needed | OPEN — fix locally |
| **A6** | `ch1:193` only | **RULED + DRAFTED 2026-07-31. Scope collapsed from three edits to one.** *The loop* is not this book's name for anything — every use means a different cycle, and `ch9:103` rules that the WAVE does *not* loop. ch2's labelling is honest; ch3's recall is earned 582 lines after the teaching. The referent was never missing; the **name** was never adopted | *loop* means a rumination pathology (`ch2:172`), a four-stage cycle (`ch6:269`), and the five modes (`ch8:438`, `ch9:103`). The WAVE runs 10–18 times in every Face chapter | **Name it the WAVE in ch1 and point at ch3.** One edit, two sentences | The book's central promise is named correctly at first mention | **DRAFTED — in the approved set** |
| ~~A7~~ | `ch3:228`, `appendices/ON_THE_SHOULDERS_OF.md` | **CLOSED 2026-07-31 — already fixed on `claude/mtgoa-manuscript-changes-swmp78`**, found independently by their citation audit. Kishimi and Koga credited in Appendix G with the disagreement named. Do not duplicate. Their audit found four further Appendix G credits pointing at absent sources — Wendell's call | — | — | CLOSED elsewhere |
| ~~A7-orig~~ | `ch3:228`, `front_matter/copyright.md` | A named outside source carries no credit anywhere in the shipping book | *The Courage to Be Disliked* is quoted at `ch3:228`; returns **zero hits** in the copyright page's Sources and permissions, Appendix G, and all back matter | Credit it, or cut the attribution | Every source the book owes is credited | OPEN — print-relevant |

## This session (2026-07-31)

| ID | Location | Reader problem | Evidence | Decision | Intended result | Status |
|---|---|---|---|---|---|---|
| DL-13 | `SPEC_EDITORIAL_OS_INTEGRATION` §4 | Editorial passes lack a one-page brief to judge against | Lean OS anchor 1; pieces existed in `THESIS_DRAFT.md` + Jordan ICA | Confirm or amend the assembled book brief | Every role prompt gets the same brief | OPEN, awaiting Wendell |
| ~~DL-14~~ | `specs/VOICE_ANCHOR.md` | — | Lean OS anchor 2 | **CLOSED 2026-07-31.** Wendell selected five: `ch1:10` · `ch1:119` · `ch4:115` · `ch5:516` · `ch8:342`. `ch4:115` is in deliberately to keep humor in the comparison set | Voice Guardian can run; first pass done — 22 ACCEPT, 2 REVISE, 1 accepted with a recorded loss | **CLOSED** |
| **DL-19** | `ch3:258`, `ch5:308`, `ch5:516`, `ch6:365`, `ch7:508` | **Two first-person authors share the body text with nothing to tell them apart.** In ch7 the collision is total: Elian Cross recounts cases with a cost at `ch7:130`–`136` (*"Forty-one cases and I have not said it once"*), which is the exact shape a Wendell testimony would take | `specs/SPEC_DL19_AUTHOR_COLLISION_2026-07-31.md`. Full scan: four sites in ch3–ch8, none in ch4/ch7/ch8. Two comply already (Face writing under the chapter's assigned daemon, per `FACE_AUTHORS.md` field 3); two carry real-world referents a Face cannot own. Marginalia is not the destination — the annotator is an in-world character, revealed as Headmaster at `MARGIN_ARC.md:141` | **Wendell 2026-07-31: enforce DL-4.** Four moves: ch3:258 to second person; ch5:308 re-voiced in two phrases; ch5:516 and ch6:365 unchanged with the reasoning recorded; ch7:508 slot cut and the shame passage relocated to `ch9:354` | One author per surface. Wendell's biography lives in the frame — ch1, ch2, ch9 | **RULED — drafts filed, application blocked on DL-18** |
| DL-15 | this file | Rulings scattered across seven-plus specs get re-argued | Lean OS anchor 3; July precedent | Adopt this log as the single ledger; spec rulings sections feed it | Rediscovery loops end | OPEN, awaiting Wendell |

## 2026-08-01 — ship day

| ID | Location | Reader problem | Evidence | Decision | Intended result | Status |
|---|---|---|---|---|---|---|
| **DL-20** | all shipping surfaces | **The book routes readers to a product that is not shipping with v1.** A wrong pointer in a printed book cannot be patched, which is what separates this from every other open finding. | `instruments/shipcheck.py` returns **51 sites**: 13 `→ app` tags in Appendix B, the B2 formula ×6, three practice-prompt tails, ch3's App Layer section, ch1's six-site cluster including the thirty-day trial, ch9's eleven bars-engine references, `about_the_author`. | **Wendell 2026-08-01: the app removal is blocker one.** It outranks placeholders, build gaps and every quality finding. `SPEC_REMOVE_APP_V1` §5's three open rulings are now the critical path. | The shipped book points at nothing it cannot deliver. | **OPEN — top priority.** Ruled and drafted portion applied 2026-08-01 (57 → 20 in `manuscript/`); the rest needs rulings 3, 4, 5. |
| **DL-21** | `instruments/shipcheck.py` | The editorial system ranks findings by what they cost to fix, not by whether they stop the book. On ship day those are different questions and only one of them was instrumented. | `rescan.py --list` orders by claim-error → blocked → continuity → verify → structural → line. Nothing in the repo reported ship state as a single board. | Adopt `shipcheck.py` as the ship-goal view, running alongside `rescan.py` rather than replacing it: six categories, ordered by DL-20, each answering "does this reach the reader wrong." | One command answers whether the book can ship, and quality work stops competing with blockers for attention. | **ADOPTED 2026-08-01.** |
| **DL-19** | `ch3:258`, `ch5:308`, `ch5:516`, `ch6:365`, `ch7:508` | (see above) | — | — | — | **APPLIED 2026-08-01** on `swmp78`. M1, M2 and M4 seated; M3 confirmed no-change. M2 needed a third site the spec did not scope. |
| **DL-22** | `APPENDIX_D`, `APPENDIX_E`, `ON_THE_SHOULDERS_OF` | **Internal provenance reaches print through gaps in the strip.** Corrected 2026-08-01: the first version of this row said six appendices print `Status:` / `Authority:` / `Location in book:` blocks. They do not. `build_book.py` grew `strip_provenance()` on 2026-07-31 and it works, and `placeholders.py` imports the same function. The 15-line leak was real when measured and has been closed since. | What still leaks is three lines, because the strip is keyed on the shape `**Known-Label:**` inside the header block, so internal text in another costume walks through: Appendix D's no-somatic note (a blockquote, addressed to the editor), Appendix E's `**Book body:**` line (label not in `META_KEY`, carrying `ch3.md:545` and a renumbering note), and `ON_THE_SHOULDERS_OF`'s opening words *Back matter.* | **Strip all three. Add `Book body` to both scanners.** Appendix E keeps its cross-reference, rewritten to Appendix C's reader-facing form. Appendix D's `*Source:*` line stays: that is attribution, not provenance. | Nothing internal survives assembly. | **APPLIED 2026-08-01** on `swmp78`. Re-scan reports 0 leaks. |
| **DL-23** | `manuscript/ch4.md:2` | **Two consecutive chapters each claimed to be the foundation.** ch3 read *Emotional Alchemy as the Foundation of Real Allyship* and ch4 read *The Clean "No" as the Foundation of Real Allyship*. | The book had already ruled it in the admissions handbooks: the School of the Body (ch3:45) is the only school whose entry clause reads *"None. Everyone begins here"* — every other school requires standing at the one before it. ch4's subtitle contradicted ch4's own admissions page at ch4:32, *"You will be unwelcome in small ways, more often than you have budgeted."* | **ch3 keeps the foundation claim. ch4 becomes *The Willingness to Be Unwelcome***, the chapter's own named gift at ch4:585, ch4:753 and ch4:761, and its EA table's dissatisfaction pole at ch4:270 (*Fear of being unwelcome → Wonder*). Wendell 2026-08-01: *"willingness to be unwelcome hits. It connects to the courage to be disliked in a way that's quite powerful."* | One foundation, and a subtitle that says what its chapter teaches. | **APPLIED 2026-08-01** on `swmp78`, adopting the ruling recorded as DL-31 on `book-pdf-epub-production-ybxa11`, which never reached master. One live copy: `insertions.py` returns 0 for the old string. Book-wide review clean on all six, round-trip byte-identical. |
