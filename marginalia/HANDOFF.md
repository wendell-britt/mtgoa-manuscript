# HANDOFF — Marginalia Frame Conversion
### *2026-07-28. Digital delivery August 1.*

---

## What happened

The manuscript was structurally complete and reading flat. The fix was not a rewrite. **Every
chapter is now a document written by a named character, annotated in the margin by somebody
else.**

**No body text was changed.** All eight compiled chapters are the original prose with 44
insertions layered on top.

---

## The frame, in six lines

- The book is the core text of a school aboard a lost ship called the **Calrunia**.
- Six **Heads** write the six treatises. Each has a daemon, a blind spot, and a signature question.
- **Bram Tull**, Caretaker, writes Ch2. Not faculty. His daemon is the ship.
- The **unsigned margin** belongs to the Headmaster — who is **Thalen Orr**, revealed in Ch8 by
  absence, because he cannot annotate his own chapter.
- **Earth is one of the worlds the ship visits.** That is why the treatises describe her workplace
  like an excavation site — defamiliarisation, doing the work no treatise could.
- Students are recruited from the worlds. **Not the ones who won — the ones who stayed.**

---

## Package contents

| Folder | What it is |
|---|---|
| `01_compiled_chapters/` | **The deliverable.** 8 chapters, insertions applied, ready to diff against the repo. |
| `02_new_prose/` | Author's note, bylines, epigraphs, postcard — the only genuinely new writing. |
| `03_specs/` | Voice synthesis, humour grid, margin arc, Baldwin spec, work order, audits. |
| `04_source_notes/` | Per-chapter note sets with rationale, plus the influence corpus. |
| `insertions.py` / `compile.py` | **Re-runnable.** Edit a note in `insertions.py`, run `compile.py`, get fresh chapters. |

**Insertions are wrapped in HTML comments** — `<!-- MARGINALIA -->`, `<!-- EPIGRAPH-BYLINE -->`,
`<!-- POSTCARD -->` — so they are greppable, strippable, and safe to hand a typesetter.

---

## Status

| Item | State |
|---|---|
| 44 insertions across 8 chapters | **done**, anchors machine-verified unique |
| 7 bylines + 6 byline notes | **done** |
| 16 epigraphs (student + beneficiary paired) | **done** |
| Author's note | **drafted**, needs your real dates/spans |
| Postcard (last page) | **done** |
| Ch8 reveal by absence | **done** |
| 3 defective AMEND notes | **fixed and recompiled** |
| Body-text editing pass (D1–D4) | **not started** |
| 25 move stopping conditions | **not started** — largest remaining task |
| Enrollment back matter | **not started** |
| School name | **not decided** |

---

## Pick up here — in order

**1. Name the school.** Blocks the half-title and the enrollment page. Blocks nothing else — the
Heads are identified by *School of the Body*, *School of the Line*, etc., so all bylines are
already valid.

**2. Diff `01_compiled_chapters/` against the repo and merge.** Body text is byte-identical apart
from the insertions.

**3. The 25 stopping conditions** (`claude_EXERCISE_AUDIT.md`, Finding 1). ~1,000 words. Ch7 and
Ch8 have them; Ch3/4/5/6/9 do not. Use Ch7's form: *the test is not [outcome you cannot control].
The test is [the thing you did].* **This also makes 25 moves loop-addressable**, per the game-loop
analysis — one job, two purposes.

**4. Body-text pass D1–D4** (`claude_WORK_ORDER.md`). Fix the **template** as well as Ch6, or the
next section built from it reintroduces both defects.

**5. Author's note revision**, then enrollment back matter, then postcard placement.

---

## Decisions locked today

- **Wilber and Rao are the thinking layer.** Allowed to make the idea harder, never the sentence.
  As dials they are **parody, not imitation**.
- **Ch7 carries no Jerk.** Jordan's home chapter; the withdrawal is the move, and it is what earns
  Ch4–Ch6.
- **Ch8's Jerk points at the author**, delivered by his own staff.
- **Ch9 has no marginalia** — not because the illusion fades, but because he is not aboard.
- **Beige enters as Level 0**, no Face, a Caretaker. Three table rows, no renumbering.
- **Daemons are met through the schools**, not possessed by default. The Protector comes with the
  body.
- **The book is the move library's source text; the game loop is the runtime.** The book does not
  need to be its own runtime.

---

## Rules the marginalia was written against

Four, all found by failing them first:

1. **Describe before naming.** Shklovsky — the label collapses the estrangement.
2. **Every note grabs a phrase** in the prose beside it, in its first sentence.
3. **Clear, not clever.** No figure the reader has to unpack.
4. **Say the noun.** *A world, the floor, the honest word, there was a committee* — all the same
   failure. Name it.

Plus: **the arc-beat exception** — in a note carrying an arc instalment, the beat lands last and
the joke sits earlier.

---

## Open questions

1. **School name.** See above.
2. **Appendix G is not in the project.** If it maps beliefs to superpowers per Face, the six
   daemon-alliance lines in the bylines must agree with it. Canon governs; check before print.
3. **Nima Vale / Irix Vale** share a surname. Free lore or drafting artefact. Cheapest answer is to
   say nothing.
4. **Postcard placement** — before the enrollment matter, most likely. Commerce between the
   postcard and the cover would spend it.
5. **Ch9's student author stays unnamed.** Recommended, not yet ruled.

---

## Do not

- Add a line under Ch8's byline. **The gap is the reveal.**
- Add anything after *"literature by the door"* — that note was cut, but the principle holds for
  the postcard: **the book ends because he left.**
- Soften *"which is not a recommendation"* in Ch2 note 6. It is the Ch9 invitation's only setup and
  it must stay throwaway.
- Let the fiction grow. No ship history, no founding, no politics of the Six Schools. See the
  do-not-build list in `claude_PRODUCTION_PLAN.md`.
