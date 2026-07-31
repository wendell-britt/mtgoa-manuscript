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
| **P0** | `ch7:467`, `ch1:179`, `ch1:267` | **Three placeholders print verbatim, including an authoring note addressed to Wendell** | `[[TESTIMONY SLOT — WENDELL…]]`, `*[visual: the six Game Masters]*`, `**[ URL / QR ]**`; all verified in `build/MTGOA_PRINT_2026-07-31.md`. `gate.py` passes clean — it has no placeholder rule | Fill or cut all three | Nothing addressed to the author reaches a reader | **OPEN — blocks print** |
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
| **A6** | `ch1:191`, `ch2:476`, `ch3:242`, `ch3:824` | **The book's one process is promised in ch2, delivered in ch3, and then asserted as already known.** Outranks A1–A5 | ch1 promises "the loop you meet in the next chapter"; ch2 delivers five *different* moves; WAVE-Spiral defined `ch3:244`; the five stage names read **0 in ch1 and ch2**; `ch3:824` says "you already know all five" | Repoint ch1, rename ch2's five, cut the false prior knowledge | The book's central claim about itself is true | OPEN — recommend all three |
| ~~A7~~ | `ch3:228`, `appendices/ON_THE_SHOULDERS_OF.md` | **CLOSED 2026-07-31 — already fixed on `claude/mtgoa-manuscript-changes-swmp78`**, found independently by their citation audit. Kishimi and Koga credited in Appendix G with the disagreement named. Do not duplicate. Their audit found four further Appendix G credits pointing at absent sources — Wendell's call | — | — | CLOSED elsewhere |
| ~~A7-orig~~ | `ch3:228`, `front_matter/copyright.md` | A named outside source carries no credit anywhere in the shipping book | *The Courage to Be Disliked* is quoted at `ch3:228`; returns **zero hits** in the copyright page's Sources and permissions, Appendix G, and all back matter | Credit it, or cut the attribution | Every source the book owes is credited | OPEN — print-relevant |

## This session (2026-07-31)

| ID | Location | Reader problem | Evidence | Decision | Intended result | Status |
|---|---|---|---|---|---|---|
| DL-13 | `SPEC_EDITORIAL_OS_INTEGRATION` §4 | Editorial passes lack a one-page brief to judge against | Lean OS anchor 1; pieces existed in `THESIS_DRAFT.md` + Jordan ICA | Confirm or amend the assembled book brief | Every role prompt gets the same brief | OPEN, awaiting Wendell |
| DL-14 | Part 2 register | Voice guarding compares to statistics, not to the book at its best | Lean OS anchor 2 | Wendell selects 3–5 passages as the Part-2 voice anchor | Edits cannot become flatter than the anchor set | OPEN, awaiting Wendell |
| DL-15 | this file | Rulings scattered across seven-plus specs get re-argued | Lean OS anchor 3; July precedent | Adopt this log as the single ledger; spec rulings sections feed it | Rediscovery loops end | OPEN, awaiting Wendell |
