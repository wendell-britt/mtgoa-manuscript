# SPEC — The Finishing Pass

**2026-07-29. Digital delivery August 1. Integrates the 2026-07-28 Claude Code
handoff (`review.py`, `SEVEN_VOICES.md`, the operational loop) into this
repository and sequences the remaining work.**

Read `specs/MANUSCRIPT_FILE_CANON.md` first. Canon is `manuscript/ch1.md`–`ch9.md`
in this repo; nothing in the handoff package overrides that. Every number below
was re-measured against canon on 2026-07-29 — the handoff's own baseline was run
against the stale compiled chapters and is quoted only where it differs.

---

## 1 · What arrived and where it now lives

| Handoff file | Repo location | State |
|---|---|---|
| `review.py` — the voice linter | `marginalia/review.py` | Ported. Reads `manuscript/`, scores body and margin separately, `--anchors` strips the frame first. Rules, patterns, and thresholds untouched. |
| `claude_SEVEN_VOICES.md` — genre + flavor doctrine | `marginalia/specs/SEVEN_VOICES.md` | As delivered. |
| `CLAUDE_CODE_HANDOFF.md` — the operational loop | `marginalia/CLAUDE_CODE_HANDOFF.md` | As delivered. Its `build/` layout maps to `marginalia/`; its `compiled/` output tree does not exist here — the frame compiles into canon directly. |

Everything else in the package was already integrated on 2026-07-29
(`marginalia/`, commit `682fbde`).

### Port corrections, so nobody re-litigates them

- **`--anchors` on an applied manuscript false-positived.** Rule 2 makes every
  note grab a phrase from the prose beside it, so each anchor legitimately
  appears twice once the frame is applied. The port strips the frame before
  counting. Now clean: 0 findings.
- **The original linted both surfaces as one text.** Body mode now strips the
  margin; marginalia mode reads only the margin with `> ` prefixes removed so
  the paragraph-level rules see it.

## 2 · The tool contract

Four tools, one loop. They are complementary, not alternatives.

| Tool | Kind | Zero required? |
|---|---|---|
| `instruments/gate.py` | **Hard canon gate** — banned words, And/But openers, A0, negation stacks, em-dash joins. Scores body and margin separately. | **Yes.** Both surfaces. Margin passes clean today; body carries 6 pre-existing hits (see §4·W1). |
| `marginalia/review.py` | **Candidate finder** — AI shapes, say-the-noun, hedges, voice/genre markers, moves-without-test. | No. Every finding is adjudicated by a human or a review agent. BLOCK means *adjudicate before Wendell sees it*, not *auto-fix*. |
| `marginalia/compile.py` | Frame build. `--check` / `--apply` / `--strip` / `--verify`. | `--verify` must stay byte-identical at 97,738 body words. |
| `instruments/dupes.py` | Cross-chapter duplicate scanner. | Run on all new prose before insertion. |

**The loop, repo-native** (replaces the handoff's §The loop):

```bash
$EDITOR marginalia/insertions.py                     # 1. edit a note (never the chapter)
python3 marginalia/compile.py --strip                # 2. rebuild
python3 marginalia/compile.py --apply
python3 instruments/gate.py                          # 3. hard gate — must pass
python3 marginalia/review.py --mode marginalia       # 3b. lint the margin
python3 marginalia/review.py --mode voice            # 3c. each treatise sounds like its Head
python3 marginalia/review.py --anchors               # 4. anchors still unique
```

Body-prose edits go through `instruments/spec_edit.py` as always, then the same
gate + review steps.

## 3 · Measured baseline, 2026-07-29

Body surface = canon with the frame stripped, all nine chapters. Margin surface
= the 53 blocks only.

| Surface | BLOCK | WARN | INFO |
|---|---|---|---|
| Body | **40** | 88 | 177 |
| Margin | **1** | 8 | 8 |
| Anchors | 0 | — | — |

BLOCK breakdown, body: **27 say-the-noun** candidates · **7 denying negations**
· **6 chapters with moves missing tests**. (Handoff quoted 35/90/167 against the
stale compiled set, which excluded ch1 and predates the July line edit. Trust
these numbers, not those.)

Leading WARN/INFO signals, body: 172 paragraph-ends-on-longest-sentence (the
punchline-last rule at scale — the handoff calls this the single most useful
signal in the file) · 50 `which is` appositive tails · 25 abstraction-noun
subjects.

## 4 · The work, sequenced

Order matters: W1 and W2 are pure body-prose fixes with no dependencies. W3
depends on ruling R3 and touches the same sections as W2, so W2 lands first.
W4–W5 are adjudication passes that can interleave.

### W1 — Clear the body's hard-gate hits and the denying negations *(one session)*

The canon gate's 6 body hits and the linter's 7 denying negations are the same
kind of work and should be one pass. This is D2 from the work order; the linter
has already located every site.

Canon-gate hits (must reach 0):

| Site | Counter | Text |
|---|---|---|
| ch3:738 | stack | *Not what the situation warrants. Not what a person…* |
| ch3:740 | A0 | *a time you were told something true* — likely false positive: it asks for recall, it does not narrate her history. Adjudicate, and if licensed, record it in the spec, not as a regex exemption. |
| ch6:107 | stack | *Not the outcomes the founders intended. Not…* — RULE_COLLISIONS independently scores ch6's negations as **denying → cut** |
| ch6:399 | banned | *The Capacity in the Room* (table cell) |
| ch7:69 | stack | *Not a demand. Not a condition of continued affection.* |
| ch8:401 | stack | *Not as diagnosis. Not as verdict.* |

Denying negations (`It's not X. It's/That's Y`): ch3 ×1 (*emotional
processing*), ch4 ×1 (*aggression*), ch5 ×2 (*nostalgia*; *will*), ch6 ×1
(*organizational design*), ch8 ×1 (*sees furthest* variant), ch9 ×1 (*morning
routine*). Apply the RULE_COLLISIONS test to each: still true when the sentence
ends → ranking → keep and record; set up to be knocked down → say Y directly.

Every edit through `spec_edit.py`; gate + `--verify` after.

### W2 — The 25 stopping conditions *(~1,000 words, the largest remaining task)*

Measured: ch3, ch4, ch5, ch6, ch9 have five moves each and zero tests — **25 to
write**. Ch7 has all five in the bolded `**The test:**` form. Ch8 has its five,
but as plain `The test:` sentences embedded in its Section 5 shadow-version
paragraphs — the handoff's "Ch7 and Ch8 have them" is true in substance, not in
form. Ruling R5 decides ch8.

Form, per the handoff: **the test is not [outcome you cannot control]. The test
is [the thing you did].** Note this is ch7 *Move 3's* form; ch7's own Moves 1,
2, and 4 are outcome-based (*"both sides say yes"*) and technically fail the
prescription. Ruling R6 decides whether they are retrofitted.

This also makes the 25 moves loop-addressable per the game-loop analysis — one
job, two purposes. New prose runs `dupes.py` and the gate before insertion.

### W3 — Genre markers, the ~150-word version *(after R3 is confirmed)*

Per `SEVEN_VOICES.md` §What ships August 1: surface idiosyncrasies applied to
Sections 1–3 only, three to five per treatise, ~150 words of edits per chapter.
Full re-voicing is explicitly a second-edition project.

`--mode voice` output is the worklist, and today every Head fails, which is
expected — the re-voicing has not happened:

| Ch | Head | Missing (require) | BLOCK |
|---|---|---|---|
| 3 | Maera Voss | numbered observations · recorded wrong reading · sensation rate (4, want ≥3/1k) · refusal to name | — |
| 4 | Corin Ash | imperative openers · self-interruption · stated cost | genre absent **+ 4 hedge particles (forbidden)** |
| 5 | Sera Quill | clause rate (3, want ≥2/1k) · citation rate · written-vs-kept rate | — closest to passing |
| 6 | Irix Vale | figure-reference rate · *in practice* ×2 · stated tolerance | — |
| 7 | Elian Cross | case marker · quotation rate (1, want ≥2/1k) · both-protections-named | — |
| 8 | Thalen Orr | cites another school ×2 · courteous disagreement | genre absent |

Ch4 is the worst and also the validated case — the linter demonstrably
discriminates style-only from style-plus-flavor there. Do ch4 first and
calibrate the remaining five against what Wendell accepts.

Sequencing: the SEVEN_VOICES note says the Part 1/Part 2 split (R2) decides
where the markers stop. In canon the seam is `## Section 4` in every chapter
ch3–ch8 regardless of how R2 is ruled, so **W3 may proceed before R2** provided
the seam stays at Section 4; only the ~20 Part-2 margin notes wait on R2.

### W4 — Say-the-noun adjudication *(27 body + 1 margin candidates)*

Expect ~half to be legitimate. Recurring true-positive shapes worth a look
first: bare *"the thing"* clause-enders in ch4/ch5 move instructions (*"You said
the thing. You drew the line."* — deliberate register or withheld noun?), and
*"for a while."* paragraph-enders in ch5. The one margin BLOCK is ch7's *"I am
told this is the honest version"* — which reads as a deliberate echo of the
say-the-noun rule itself; adjudicate, don't auto-fix (R7).

Calibration rule from the handoff stands: tune against corrections Wendell
actually makes, not against intuition. Record each adjudication in this spec's
changelog so the pattern list can be tightened once.

### W5 — Tail passes *(WARN-level, time-permitting)*

50 `which is` appositive tails (a real tic; worth a sweep) · 25
abstraction-noun subjects (overlaps D4 in the work order) · 172 punchline-last
INFO hits as pattern data for wherever W1–W4 already open a file. No file is
opened solely for a W5 finding before August 1.

## 5 · Standing constraints, carried forward

From the handoff and HANDOFF.md, still binding:

- Never hand-edit a marginalia block in a chapter — `insertions.py` only.
- No line under Ch8's byline. The gap is the reveal.
- Do not soften *"which is not a recommendation"* in Ch2 note 6.
- Nothing after the postcard.
- The fiction does not grow: no ship history, no founding, no politics of the
  Six Schools (`marginalia/specs/PRODUCTION_PLAN.md` do-not-build list).
- Chat keeps the generative work; this repo keeps the mechanical loop. A draft
  that has not been through §2's loop does not go in front of Wendell.

Still unwritten and unaffected by this spec: both appendices (Polarity Map,
3-2-1 Shadow Process — hard print blockers), front matter, TOC, back matter,
enrollment page, author's-note dates.

## 6 · Rulings awaiting Wendell

1. **R1 — School name.** Blocks half-title and enrollment page only. (Carried.)
2. **R2 — Part 1 / Part 2 split at Section 4.** ~20 of 38 notes would move from
   *argue with the treatise* to *update the teaching*. (Carried.)
3. **R3 — Genre scope.** SEVEN_VOICES recommends the ~150-word marker version
   for Aug 1, full re-voicing as second edition. Confirm; W3 waits on this.
4. **R4 — Appendix G.** Not in any package. If it maps beliefs to superpowers
   per Face, the six daemon-alliance byline lines must be diffed against it
   before print. Canon governs.
5. **R5 — Ch8's five embedded tests.** Normalize to the bolded standalone form
   (typographic consistency, loop-addressability) or leave embedded in the
   shadow-version prose (the chapter's own voice). Measured fact: the linter
   counts them as missing until normalized or until the pattern learns the
   plain form.
6. **R6 — Ch7 Moves 1/2/4 tests are outcome-based**, against the prescribed
   act-based form taken from its own Move 3. Retrofit or leave.
7. **R7 — Say-the-noun calibration authority.** Which of the 28 candidates are
   corrections; the ch7 margin note's *"the honest version"* specifically —
   defect or deliberate echo.
8. **R8 — ch3:740 A0 hit** (*"a time you were told something true"*): license
   as recall-prompt or rewrite.

---

*Changelog: created 2026-07-29 from the files_2 handoff. Baselines in §3 are
reproducible: `gate.py`, `review.py` (each mode), `compile.py --verify`.*
