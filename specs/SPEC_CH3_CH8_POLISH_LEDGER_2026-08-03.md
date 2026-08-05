# SPEC — Chapters 3–8 polish ledger

**Status:** Planning and candidate adjudication only. No canonical prose changes
are authorized by this ledger.

**Source of truth:** `manuscript/ch3.md` through `manuscript/ch8.md` on `master`
after `3d441f2` (2026-08-03).

**Purpose:** Turn the book's accumulated grammar and line-editing rules into one
repeatable finishing pass across the six Face chapters. The aim is compression,
clearer reference, and more varied explanation—not uniformity or a mechanical
sentence-shortening campaign.

---

## 1 · Current state

The shipping surfaces are mechanically sound:

- `gate.py`: pass, all counters zero.
- `dupes.py`: no duplicated prose.
- `marginalia/compile.py --verify`: byte-identical body round-trip.
- `prose_diet.py`: no new heavy chapter measure except Ch7 passive voice at 1.43.

This is therefore a polish pass, not a repair pass. `line_scan.py` findings are
candidates, not defects; no count warrants an automatic replacement.

| Chapter | Candidates | High-value reading target |
|---|---:|---|
| Ch3 — Shaman | 33 | Long conceptual sentences; repeated process recap; cross-block references. |
| Ch4 — Challenger | 19 | Compressed conflict teaching; repeated boundary formulation. |
| Ch5 — Regent | 24 | Inheritance sequence repeated as explanation after explanation. |
| Ch6 — Architect | 21 | System-language abstraction; dense process summaries. |
| Ch7 — Diplomat | 33 | Repeated field/absence/distortion formulas; passive density. |
| Ch8 — Sage | 20 | Whole-board explanations and return/meta recaps. |

## 2 · Rules to apply consistently

### P1 · One full explanation per teaching unit

Keep the strongest first explanation of a model. At later appearances, add a new
consequence, example, choice, or test; do not restate the model's entire logic.

**Candidate clusters:** Ch3 `:322`, `:816–:822`; Ch5 `:456–:464`; Ch6
`:462–:485`, `:628–:630`; Ch7 `:236–:238`, `:286–:393`; Ch8 `:77`, `:156`.

### P2 · Let named sequences carry their own weight

When the reader can see a named five-stage sequence, cut prose that merely lists
the same stages again. Keep a recap only when it changes the reader's use of the
sequence or gives it an ethical limit.

**Candidate clusters:** Ch3 `:981`; Ch4 `:771`; Ch5 `:458–:464`; Ch6 `:256`,
`:630`; Ch7 `:800–:812`; Ch8 `:826`.

### P3 · Repair broad references at real seams

Replace a pronoun or demonstrative only where a reader must cross a heading or
paragraph boundary to recover its antecedent. Do not remove ordinary cohesion.

**Candidate sites:** Ch3 `:64`, `:723`; Ch5 `:236`, `:542`.

### P4 · Split only sentences that carry competing jobs

The target is not short sentences. A long sentence earns its length when it
maintains a single escalating movement. Split where it introduces an example,
qualification, definition, and instruction in one unit.

**First reading sites:** Ch3 `:179`, `:268`, `:433`, `:981`; Ch4 `:536`, `:556`,
`:771`; Ch5 `:458`, `:464`, `:513`; Ch6 `:256`, `:403`, `:423`; Ch7 `:138`,
`:719`, `:800`; Ch8 `:75`, `:178`, `:527`, `:723`.

### P5 · Restore actors where abstraction hides the move

Favor a person, decision, record, or practice over an abstract system, field,
pattern, or framework when the sentence explains what someone can actually do.
This extends the agency findings without mechanically purging the book's native
metaphors.

**First reading sites:** Ch6 `:118`, `:240`, `:246`; Ch7 `:138`, `:441`, `:719`;
Ch8 `:270`, `:431`, `:709–:711`.

### P6 · Treat fixed practice refrains as intentional

Do not “solve” repetition that supports the book's practice architecture:

- 3-2-1 / Be It / Speak as I passages;
- BAR capture instructions;
- card-to-quest drills;
- a chapter's final named commitment.

These patterns should be reviewed for accuracy and local clarity, but not varied
for variation's sake.

### P7 · Do not misclassify named vocabulary as banned language

The instrument's `banned-kin` result for **Genuine** is informational only;
`genuine` is allowed. The banned word is *genuinely*. Retain a use unless its
meaning, rather than the string match, requires revision.

---

## 3 · Approval packets

Draft and review in three small packets, each containing only 6–10 exact
before/after sites:

1. **Ch3–4:** process clarity and boundary compression.
2. **Ch5–6:** stewardship and systems clarity.
3. **Ch7–8:** relational and whole-board clarity; include a focused passive read
   of Ch7.

For every proposed edit:

1. Show full old and new prose in conversation.
2. State which P-rule the edit satisfies.
3. Preserve the chapter's native metaphor and any protected Village-fable voice.
4. Apply only after Wendell approves the exact replacement.

## 4 · Completion criteria

- No repeated explanation remains unless it adds a new reader decision or use.
- Named sequences are taught once and subsequently used rather than re-listed.
- Real orphan references have named antecedents.
- Long sentences retain their pressure and cadence while carrying one primary job.
- Ch7 passive voice is reduced where a human actor can take the verb, without
  altering deliberate treatise or fable register.
- Gate, duplicates, prose-diet, marginalia round-trip, and the relevant
  voice/agency checks pass after each approved packet.

## 5 · Print-spine follow-up

Wendell has ruled that dedication and acknowledgements are not part of this
edition. Before the final print build, leave dedication absent and remove the
acknowledgements component from `instruments/build_book.py`'s spine. That is a
production configuration change, not a prose-cut request.
