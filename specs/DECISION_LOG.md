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
| DL-16 | `back_matter/kickstarter_backers.md` | Backers promised a credit do not find one | `build_book.py` — GAP, spine assembles with 2 gaps | Supply the list, or drop the component | Spine builds with no gaps | OPEN — needs Wendell |
| DL-17 | `back_matter/enrollment.md` | Reader finishes the book with no next step | `build_book.py` — GAP; `MANIFEST.md` notes it waits on R1 | Write it, or ship without it | Spine builds with no gaps | OPEN — needs Wendell |
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
| A2 | `ch1:207`, `ch2:480`, `ch9:669`; silent ch3–ch8 | The sheet ch9 turns back to is nearly empty | *"a line added in every chapter ahead"* — promised 8, delivered 2 | Narrow the promise, or seat one line per chapter using ch2:480 as the template | The reader's record of her own change actually accumulates | OPEN — structural decision |
| A3 | `ch1:68`, `ch1:73` | *Helping the less powerful* — the paternalism myth — is named and never taken apart | 9 of 10 myths map to a teardown; this one returns 0 hits ch2–ch9 | Soften *"each one"*, or assign the orphan | The stated inventory is accurate | OPEN — fix locally |
| A4 | `ch8:138` | Five-term developmental scale, undefined, 100k words in, in her integration chapter | *"all the altitudes — Red, Amber, Orange, Green, Teal"*; `termdebt.py` NEVER DEFINED; Magenta absent book-wide | Define, cut the colour names, or route to a definition | No jargon without translation | OPEN — recommend cut |
| A5 | `ch3:680`, `699`, `703`, `707` | "One of the four" back-references a set she has not met | Domains NEVER DEFINED in body; defined only in Appendix A; ch3's own italic routing convention at `415`/`560`/`589` is not applied here | Add the pointer in the existing convention | Prerequisite reachable where needed | OPEN — fix locally |

## This session (2026-07-31)

| ID | Location | Reader problem | Evidence | Decision | Intended result | Status |
|---|---|---|---|---|---|---|
| DL-13 | `SPEC_EDITORIAL_OS_INTEGRATION` §4 | Editorial passes lack a one-page brief to judge against | Lean OS anchor 1; pieces existed in `THESIS_DRAFT.md` + Jordan ICA | Confirm or amend the assembled book brief | Every role prompt gets the same brief | OPEN, awaiting Wendell |
| DL-14 | Part 2 register | Voice guarding compares to statistics, not to the book at its best | Lean OS anchor 2 | Wendell selects 3–5 passages as the Part-2 voice anchor | Edits cannot become flatter than the anchor set | OPEN, awaiting Wendell |
| DL-15 | this file | Rulings scattered across seven-plus specs get re-argued | Lean OS anchor 3; July precedent | Adopt this log as the single ledger; spec rulings sections feed it | Rediscovery loops end | OPEN, awaiting Wendell |
