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

## Open items that block or shape print

| ID | Location | Reader problem | Evidence | Decision | Intended result | Status |
|---|---|---|---|---|---|---|
| DL-8 | Appendix C | Glossary carries retired canon (1 eight-gate def, 3 Vulnerable Child refs, 4 `[Ch0]` tags, 11 trigram refs) | `MANIFEST.md` | Keep repaired glossary, or retire it and give C to the Five Channels | One coherent Appendix C | OPEN |
| DL-9 | `ch3:400` | Reader sent to an appendix that has no letter | `build_book.py` UNPLACED every run; prose written, 1,176 words, `drafts/appendix_channels.md` | Assign a letter or remove the reference | No dangling reference | OPEN |
| DL-10 | Line marginalia | "Head Sura" vs Corin Ash, Head of the Line | `FACE_AUTHORS.md` canon conflict | Predecessor, lieutenant, or leftover — name it | No contradicted name in print | OPEN |
| DL-12 | four `⟦…⟧` register tokens | None in canon | `MANIFEST.md` | Due only if the register pass extends to the other five Heads | — | DEFERRED, not gating |

## This session (2026-07-31)

| ID | Location | Reader problem | Evidence | Decision | Intended result | Status |
|---|---|---|---|---|---|---|
| DL-13 | `SPEC_EDITORIAL_OS_INTEGRATION` §4 | Editorial passes lack a one-page brief to judge against | Lean OS anchor 1; pieces existed in `THESIS_DRAFT.md` + Jordan ICA | Confirm or amend the assembled book brief | Every role prompt gets the same brief | OPEN, awaiting Wendell |
| DL-14 | Part 2 register | Voice guarding compares to statistics, not to the book at its best | Lean OS anchor 2 | Wendell selects 3–5 passages as the Part-2 voice anchor | Edits cannot become flatter than the anchor set | OPEN, awaiting Wendell |
| DL-15 | this file | Rulings scattered across seven-plus specs get re-argued | Lean OS anchor 3; July precedent | Adopt this log as the single ledger; spec rulings sections feed it | Rediscovery loops end | OPEN, awaiting Wendell |
