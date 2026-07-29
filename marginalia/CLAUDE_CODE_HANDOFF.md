# Claude Code Handoff
### *MTGOA — marginalia frame conversion. 2026-07-28. Delivery Aug 1.*

Read `HANDOFF.md` first for what the frame is and why. This file is the operational half.

---

## The reason this is moving to Claude Code

Drafts were reaching Wendell without a review pass. In a chat turn, producing the artifact and
adversarially reviewing it compete for the same space, and production wins because it is the
visible output. **The fix is to make review a separate step that cannot be skipped.**

**Chat keeps the generative work** — councils, voice discovery, the calls only Wendell can make.
**Claude Code takes the mechanical work** — lint, compile, verify, apply.

---

## Setup

```
repo/
  manuscript/            # the chapters
  build/
    insertions.py        # every note as data — EDIT HERE, never hand-edit chapters
    compile.py           # applies insertions to manuscript/ -> compiled/
    review.py            # the linter
  specs/                 # 03_specs/ from this package
  compiled/              # generated, gitignore or commit, your call
```

**Everything is already in this package.** `insertions.py`, `compile.py` and `review.py` run as-is;
`compile.py` needs its `SRC` and `OUT` paths pointed at the repo.

---

## The loop

```bash
# 1. edit a note
$EDITOR build/insertions.py

# 2. rebuild
python3 build/compile.py

# 3. lint before anyone reads it
python3 build/review.py compiled/ --mode marginalia

# 3b. check each treatise still sounds like its Head
python3 build/review.py compiled/ --mode voice

# 4. verify anchors still resolve
python3 build/review.py --anchors build/insertions.py compiled/
```

**Never hand-edit a compiled chapter.** The next compile overwrites it.

---

## review.py

Implements the four standing rules plus the mechanical checks.

| Severity | Meaning |
|---|---|
| **BLOCK** | fix before Wendell sees it. Exit code 1. |
| **WARN** | look at it. May be correct. |
| **INFO** | pattern data, not a defect. |

**What it checks:** denying negations · say-the-noun (withheld nouns) · hedge density ·
minimizers · three consecutive sentences over 25 words · abstraction noun in subject slot ·
paragraph ending on its longest sentence · sentence-length variance · em-dash density ·
`not just X but Y` · appositive `which is` tails · note length (marginalia mode) · moves without
a stated test · anchor uniqueness.

**Nothing here is automatic.** A denying negation passes if the negated thing is **still true**
when the sentence ends (ranking) and fails if it was set up to be knocked down (denying). A vague
noun passes if the noun is named within two sentences. The linter finds candidates; a human or a
review agent adjudicates.

### Current baseline on the compiled chapters

```
BLOCK  35    WARN  90    INFO 167
```

Broken down:

| Count | Sev | Rule | Note |
|---|---|---|---|
| 28 | BLOCK | say the noun | expect ~half to be legitimate. **Needs calibration on real corrections.** |
| 7 | BLOCK | denying negations | mostly the template-mandated *It's not X. It's Y* — this is D2 in the work order |
| 55 | WARN | appositive `which is` tails | a real tic; worth a pass |
| 24 | WARN | abstraction noun in subject slot | overlaps D4 |
| 161 | INFO | paragraph ends on its longest sentence | **the punchline-last rule at scale** — the single most useful signal in the file |

---

## `--mode voice` — genre and flavor per Head

The check that would have caught the flavor problem. Reads Sections 1–3 only (the treatise half;
Section 4 onward is Wendell) and tests each chapter against its Head's profile from
`claude_SEVEN_VOICES.md`.

Each voice has **require** markers (absence is the finding) and **forbid** markers.

| Ch | Head | Genre | Requires | Forbids |
|---|---|---|---|---|
| 3 | Maera Voss | practitioner's casebook | numbered observations · a recorded wrong reading · sensation nouns · one refusal to name | *you should* |
| 4 | Corin Ash | drill manual | imperative openers · one self-interruption · one stated cost | hedge particles |
| 5 | Sera Quill | annotated charter | numbered clauses · citation of prior practice · written-vs-kept | contemporary vocabulary |
| 6 | Irix Vale | engineering monograph | figure reference · *in practice* ×2 · one stated tolerance | — |
| 7 | Elian Cross | negotiation casebook | case marker · direct quotation ×2 · both protections named | — |
| 8 | Thalen Orr | commentary on the other five | cites another school ×2 · one courteous disagreement | — |

Ch2 (Caretaker) and Ch9 (student) have no profile and return INFO.

### It discriminates — validated

```
current Ch4       BLOCK: genre absent · hedge particles
                  WARN:  no imperative openers, no self-interruption, no stated cost

flavored sample   clean — no findings
```

**This is the specific failure mode it catches.** A draft can have the *style* right — imperatives,
short sentences, no hedging — and still read as *a manual somebody wrote about Corin* rather than
as Corin. The flavor markers (**stated cost**, **self-interruption**, an absent interlocutor) are
what separate the two, and they are the thing that kept getting missed by eye.

### Current state: all six fail

That is correct and expected. Use the output as the re-voicing worklist — it names exactly which
markers each chapter is missing.

---

**The `say the noun` rule was tuned once already** (139 → 28 by requiring the phrase to *end* a
clause). It will still over-fire. Tune it against corrections Wendell actually makes rather than
against intuition.

---

## Suggested first session — one hour, time-boxed

1. **Wire the paths and get the loop running.** If it is not running in an hour, abandon and go
   back to chat. Nothing here is worth the setup cost this close to delivery.
2. **Run the linter on the seven treatise sections (Sections 1–3 only)** and fix the 7 denying
   negations. That is D2 in the work order and the linter already located them.
3. **Run `--mode voice` on the treatise halves.** It is already written. Currently every chapter
   fails, which is correct — the genre re-voicing has not happened. Use it as the worklist.

---

## What is NOT decided and should not be guessed

These are open in `HANDOFF.md` and Wendell rules on them:

1. **The school's name.** Blocks the half-title and enrollment page only.
2. **Part 1 / Part 2 chapter split** at Section 4 — testimony clusters there cleanly, but ~20 of
   38 marginalia notes sit in Sections 4–7 and would need rewriting from *argue with the treatise*
   to *update the teaching*.
3. **Genre re-voicing scope.** Full re-voicing vs. the 150-words-per-chapter marker version.
4. **Appendix G** is not in this package. If it maps beliefs to superpowers per Face, the six
   daemon-alliance lines in the bylines must be diffed against it. Canon governs.

---

## Do not

- Add a line under Ch8's byline. **The gap is the reveal.**
- Soften *"which is not a recommendation"* in Ch2 note 6.
- Add anything after the postcard.
- Let the fiction grow — no ship history, no founding. See the do-not-build list in
  `claude_PRODUCTION_PLAN.md`.
- Hand-edit compiled chapters.
