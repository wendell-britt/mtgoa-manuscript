# SPEC — Integrating the Lean Editorial Operating System

**2026-07-31. Digital delivery is tomorrow.** Wendell delivered
`specs/EDITORIAL_OPERATING_SYSTEM.md` (the "Lean OS") and asked for it to be
applied to the book, integrated with whatever editorial system already exists
here. This spec is that integration: what already exists, where the two systems
agree, where the repo's measured lessons override the Lean OS defaults, and what
was missing that the Lean OS supplies.

Read `specs/MANUSCRIPT_FILE_CANON.md` first, as always. Nothing here overrides
canon. The six Heads' assessment of the system is in
`specs/PANEL_HEADS_EDITORIAL_OS_2026-07-31.md`.

---

## 1 · The system already present in this repo

There is one, and it is substantial. It grew in layers rather than being
designed at once, which is exactly why the Lean OS is useful: it names the
architecture this repo converged on independently, and exposes the one piece
this repo never built.

| Layer | Where it lives | State |
|---|---|---|
| **Canon + standing rules** | `AGENTS.md`, `specs/MANUSCRIPT_FILE_CANON.md` — canonical files, banned words, the three grammar moves, the four-move negation fix, show-the-work console rule, no canonical write without Wendell's approval | Active, ruled |
| **Hard gate** | `instruments/gate.py` — four printed surfaces, every counter must read 0. GATE PASS since 2026-07-30 | Active, green |
| **Candidate finders** | `marginalia/review.py` (AI shapes, say-the-noun, hedges, per-Head genre markers), `instruments/prose_diet.py` (measured against *Igniting Joy*, not against the book's own drift) | Active; findings adjudicated, never auto-fixed |
| **Measurement instruments** | `instruments/` — stylometry, term debt, duplicates, chain check, practice surfaces, repetition. Doctrine: *measure, do not recall* | Active |
| **Safe-edit discipline** | `instruments/spec_edit.py` — write at the end, abort on missed or duplicated anchor; `dupes.py` before insertion | Active, mandatory |
| **Voice doctrine** | `marginalia/specs/SEVEN_VOICES.md`, `HEAD_VOICE_DIAL.md`, `HEAD_REGISTERS.md`, `RULE_COLLISIONS.md`; `/no-ai-slop` with ruled precedence (`SPEC_FINISHING_PASS_2026-07-29.md` §2b) | Active; blind test passing |
| **Human track** | `MTGOA_EDITORIAL_AGENT_SPEC_v3.md` — Wendell's cold read as first-class input; convergence rule: human wins on meaning/voice, machine on mechanics | Ruled 2026-04-21, still correct |
| **Reader model** | Jordan, the ICA (`EDITING_PLAN.md`; chapter numbering there is stale, the avatar is not). `practice.py` and `termdebt.py` already test on Jordan's behalf | Active |
| **Process discipline** | Three-Context Protocol (`BOOK_WORKFLOW_SYSTEM.md`) — never generate and review in one response; the three keep-tests (Function · Earned · Non-substitutable, burden on keeping); specs end in rulings sections awaiting Wendell | Active |

## 2 · The mapping — Lean OS roles onto repo machinery

The four roles are not new hires. Three of the four already exist here as
instruments plus adjudication doctrine; the Lean OS gives them names, scope
boundaries, and a sequencing rule this repo had been keeping informally.

| Lean OS role | Repo implementation | Adaptation |
|---|---|---|
| **Book Architect** (structure only, ≤5 findings, start and end) | `instruments/build_book.py` + `chain2.py` + `termdebt.py` + the structural specs (`SPEC_STRUCTURAL_DELIVERY.md`, `MARGIN_ARC.md`). The 2026-05-29 whole-book reviews were Architect runs before the name existed | The "once near the end" run is due now. Its prompt runs as written, fed the book brief (§4) and `build_book.py --write` output. Findings go to the decision log, capped at five |
| **Continuity & Claims Auditor** | `termdebt.py`, `repeat.py`, `dupes.py`, the structural-facts section of `MANUSCRIPT_FILE_CANON.md`, the copyright page as permission ledger. Precedent: Appendix B's quest numbers each one short, F contradicting `ch3:486`, the Carolyn Elliott credit correction | Runs mechanically first, judgment second: instruments find drift, the auditor prompt rules VERIFY vs ERROR on what instruments cannot (claims, quotations, case studies) |
| **Line Editor** (readability only, ≤10 flags, after structure settles) | `marginalia/review.py` + `prose_diet.py` find candidates; `/no-ai-slop` detect mode adjudicates | `review.py` returns hundreds of candidates; the Lean OS's 10-flag cap governs **what goes in front of Wendell per session**, which is the show-the-work console rule restated as a number. The finder is unbounded; the ask is bounded |
| **Voice Guardian** (final gate on changed passages) | `instruments/gate.py` (hard, mechanical) + the *Igniting Joy* stylometric control + the SEVEN_VOICES blind test + `/no-ai-slop` edit-mode with ruled precedence | **The one structural difference: this book has seven voices, the Lean OS assumes one.** The Guardian must be told which voice governs a passage before it rules — Wendell's Part-2 register, a named Head, or the unsigned margin. Already ruled in FINISHING_PASS §2b: never run voice judgment on a treatise without naming the Head. The voice anchor (§4) is therefore per-voice, not singular |

### The four rules, against repo doctrine

1. **Diagnosis before revision** — already law here: `review.py` BLOCK means
   *adjudicate before Wendell sees it*, never auto-fix; ITD doctrine says audit
   first, writing second. Adopted as written.
2. **One job at a time** — the Three-Context Protocol, older and stricter
   (never combine generate+review in one response). Adopted; the repo version
   governs where they differ.
3. **Evidence or silence** — *measure, do not recall*, which this repo learned
   by burning days on wrong planning documents. Adopted as written. "No
   material issue found" is a valid instrument result and always has been.
4. **No unearned change** — the three keep-tests already put the burden of
   proof on keeping; the Lean OS adds the sharper phrasing: name the reader
   problem or do not touch the sentence. The reader has a name here. The
   question is always *what does this fix for Jordan.*

## 3 · Where the repo's measured lessons override the Lean OS

Three of the Lean OS defaults are adapted, each against evidence already paid for:

1. **Git cadence.** The Lean OS proposes concern-based branches
   (`edit/reader-promise`). The July collision — two branches running book-wide
   passes over the same nine files, 91 conflicting hunks — ruled harder:
   *localized section work merges; book-wide passes collide.* Adopted as: one
   editorial concern per branch **and** scoped to named sections, with
   book-wide passes sequenced, never parallel. One coherent editorial decision
   per commit is already this repo's commit style.
2. **Paste-prompts vs instruments.** The Lean OS assumes prose passes run as
   chat prompts. Where a runnable instrument exists, the instrument governs —
   it is reproducible and the planning documents have been wrong. The Lean OS
   role prompts govern the judgment layer instruments cannot reach.
3. **The author-decides rule is already stricter here.** No canonical write
   without Wendell's conscious approval; every prose change pasted before/after
   into the console. The Lean OS's "author owns every final sentence" is the
   same rule with less enforcement. The repo enforcement stands.

## 4 · What the Lean OS supplies that was missing — the three anchors

1. **The decision log — the one missing piece, now created.** Rulings here live
   scattered across seven-plus specs, each ending in a rulings section, and
   settled questions have been re-argued because no single ledger held them.
   `specs/DECISION_LOG.md` now exists, seeded with the standing rulings and the
   open ones. Rule adopted as written: **only items in the log become editing
   work**, and rejected ideas stay rejected.
2. **The book brief — existed in pieces, never on one page.** Proposed
   assembly below, drafted entirely from ruled material; needs Wendell's
   confirmation (DL-13).
3. **The voice anchor — exists as an instrument, not as passages.** The
   *Igniting Joy* control is a statistical anchor; the Lean OS wants 3–5 chosen
   passages as a comparison set. Wendell selects these — the system is explicit
   that the author picks them, and the CONVICTION notes from cold reads ("this
   is perfect, don't change it") are the natural source. Per §2, the anchor is
   layered: Wendell's passages anchor Part 2; the pass-3 handbook drafts
   (`marginalia/new_prose/HEAD_FACTS_pass3.md`) already anchor the six Heads.

### Proposed book brief (pending DL-13)

```text
Working title: Mastering the Game of Allyship
Ideal reader: Jordan — mid-30s/40s, has done the work, fears "I'm doing more
  harm than I know," craves showing up without self-erasure. Skims theory,
  never skips a story, stops for a named move with a practice.
Reader's starting problem: knows something is broken in how they show up;
  unsure what to do about it.
Reader's end-state / promise: can play all six Faces, knows which one the
  moment needs, and runs their own game — an ally who changes the field.
Central argument: to master the game of allyship you must master all six
  developmental levels; the shadow of a skipped level is what blocks you.
Voice in five adjectives: embodied, direct, playful, testimonial, unsparing.
What the prose is allowed to do: game frame; seven in-world voices with ruled
  genres; marginalia; humor; fragments and staccato inside Sections 1–3 where
  a Head's genre requires them; direct second person in Part 2.
What would betray its voice: generic self-help smoothness; hedging; moralizing
  without self-deprecation; explaining instead of testifying; the short-
  declarative drift (ruled: drift, not voice); narrating the reader's unnamed
  history back to her as fact.
Non-negotiable boundaries: canon files only; the banned-word list; every
  source credited (Carolyn Elliott, PhD — not "Bob"); permissions live on the
  copyright page; no invented citations; no Head names a channel, feeling-word,
  or operation — Chapter 3 owns that vocabulary.
```

## 5 · The integrated loop

For any editorial work from today forward:

1. **Choose from the log.** Work not in `specs/DECISION_LOG.md` does not start.
2. **Diagnose with the right role** — Architect for structure, Auditor for
   consistency/claims, instruments first in both cases.
3. **Wendell rules.** Cold read remains a first-class input either side of the
   machine (SPEC v3 stands). Human wins on meaning and voice; machine on
   mechanics.
4. **Edit one bounded unit** through `spec_edit.py`, new prose through
   `dupes.py`, rewrites through `/no-ai-slop` edit mode with the governing
   voice named.
5. **Gate + guard**: `gate.py` (must pass), `review.py --mode voice`, compare
   against the governing voice anchor.
6. **Show the work** — before/after in the console, ≤10 flags per ask.
7. **Commit one decision**, update the log, stop when the stop rules say stop.

### The ship-window subset (next 24 hours)

The gate is green on four surfaces and the spine assembles at 115,887 words.
Between now and delivery, only the following applies: the final Book Architect
scan (§2, capped at five findings, console only), the two back-matter gaps
(DL-16 Kickstarter backers, DL-17 enrollment page) which are the only items
`build_book.py` still reports, `gate.py` on anything touched, and nothing else.
Every heavier item in this spec is standing machinery for post-ship editions,
not a reason to open the manuscript tonight.

**Recorded, because it is the point of the log.** Three items were entered here
from `MANIFEST.md` and were already ruled — Appendix C, the Five Channels
letter, and Sura. The instruments closed all three in one command. A ledger
seeded from a planning document inherits that document's errors; seed it from
instrument output.

---

## Rulings needed (also entered in the log)

1. **DL-13** — Confirm or amend the book brief in §4.
2. **DL-14** — Select the 3–5 voice-anchor passages for Part 2.
3. **DL-15** — Adopt `DECISION_LOG.md` as the single ledger going forward
   (new spec rulings sections then feed the log rather than replacing it).
