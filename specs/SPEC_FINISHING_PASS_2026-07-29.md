# SPEC — The Finishing Pass

## STATUS BLOCK — measured 2026-07-29, end of session

**Read this before the plan below. The plan's baselines predate a full working
session and its §3 numbers are no longer current.**

| Item | Plan said | Measured now |
|---|---|---|
| Body BLOCK | 40 | **16** |
| Body WARN / INFO | 88 / 177 | **75 / 167** |
| Denying negations, book-wide | 52 remaining | **9**, every one an adjudicated keep |
| Say-the-noun | 27 candidates | **6** |
| Voice BLOCK | 3 | **1** — ch4's hedge particles |
| Gate — body / marginalia | 6 body hits | **0 / 0** |
| Gate — appendices | not measured | **0** (read 27 on first run; the gate had never looked at it) |
| Gate — front/back matter | not measured | **10 tokens**, all Wendell's |
| `which is` tails | 50 | **64** measured, swept to 64 from 91 |
| Body words | 97,738 | **98,332** |

**W1, W2, W4, W6, W7 are complete.** W3 is untouched and waits on R3. W5 is
partly done: the `which is` sweep ran, and `rather than` was measured and
withdrawn as a defect.

**R4 is closed.** Appendix G is `ON_THE_SHOULDERS_OF.md`, a source-lineage
bibliography rather than a belief-to-superpower map, so the six daemon-alliance
byline lines have nothing to be diffed against.

**The plan's premise about the appendices was wrong.** §5 lists both appendices as
"still unwritten … hard print blockers." Both were committed in `appendices/`. The
full A–G set exists, and A, B, F, and G were revised against current canon this
session. See `specs/SPEC_PRINT_READINESS_2026-07-29.md`, which is now the live
worklist.

### What W7 taught, worth carrying forward

- **The bare cut is not the fix.** Cutting the negated clause deletes the
  caricature the negation was guarding against. Batches 3, 4 and 5 all shipped bare
  cuts and all had to be redone. Check whether the surrounding paragraph already
  handles the caricature before assuming a cut is enough — three times out of
  seventeen it did.
- **Move 3 is not a positive contrast.** Replacing *"not X, it's Y"* with *"looks
  like X and works as Y"* keeps the opposition and only changes its clothes. Put
  the caricature in a subject or subordinate position instead.
- **Watch for the replacement formula.** Six separate times this session a batch of
  fixes converged on one sentence shape without the author noticing. `review.py`
  and `gate.py` cannot see a formula; `/no-ai-slop` can, and it must actually be
  invoked.
- **The two rules can pull against each other.** Fixing a `which is` tail by
  splitting the sentence created a denying negation, twice. Re-measure after every
  sweep.
- **Refrains are real and must be checked before editing.** Four deliberate
  cross-chapter refrains surfaced: the quest tell (ch3–ch8), the polarity
  definition (ch4/ch5/ch7), the Alchemy Move closers (ch8), and *"The distortion is
  not that it X"* (ch5–ch8). The last is licensed ranking and stays.

### Rulings added this session

**R10** — the Five Channels appendix: **closed.** It took letter C.
**R11** — appendix reference style: **closed.** Every reference names letter and title.
**R12** — Appendix C glossary: **closed.** Retired from this edition.
**R13** — ch6:295 and ch6:455 are near-duplicate passages closing on the same
sentence. Which loses its ending is authorial.
**R14** — *"It is not enough for the other one"* appears near-verbatim in ch4 and ch6.
**R15** — ch5 states a "first move" twice, at 253 (acknowledge) and 406 (witnessing).
**R16 — WITHDRAWN 2026-07-29, my error.** I read ch6:434's *"six of which"* as
pointing at the five moves listed above it, called the sentence broken, and replaced
it. The antecedent is **seconds**, not moves: the same block contains *"Open Up: six
seconds, channel and location, before anything gets modeled,"* so *"ninety seconds —
six of which are the only ones your Emotional Body will fight you for"* is exact.
It is also the chapter's thesis in one clause — the whole pass is easy except the six
seconds you have to spend feeling something before converting it. Reverted. Nothing
for Wendell to rule on.

The lesson is the ruling: I flagged prose as broken on a misreading and then asked
for confirmation of my own inference, which is the shape of an error that gets
ratified. Find the antecedent before calling a sentence incoherent.
**R17** — Appendix A's affinity table treats the Vulnerable Child as a peer gate in
a "2-2-2-2 balanced" set. Chapter 2 seats seven daemons with the VC at the centre.
**R18** — Move 3's canonical heading is *Say the Thing Under the Thing*. Renaming it
is a book-wide change; the say-the-noun pass left it alone.

---

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

Four tools plus one editorial agent (§2b), one loop. They are complementary, not alternatives.

| Tool | Kind | Zero required? |
|---|---|---|
| `instruments/gate.py` | **Hard canon gate** — banned words, And/But openers, A0, negation stacks, em-dash joins. Scores body and margin separately. | **Yes.** Both surfaces. Margin passes clean today; body carries 6 pre-existing hits (see §4·W1). |
| `marginalia/review.py` | **Candidate finder** — AI shapes, say-the-noun, hedges, voice/genre markers, moves-without-test. | No. Every finding is adjudicated by a human or a review agent. BLOCK means *adjudicate before Wendell sees it*, not *auto-fix*. |
| `marginalia/compile.py` | Frame build. `--check` / `--apply` / `--strip` / `--verify`. | `--verify` must stay byte-identical. Body words were 97,738 when this line was written and are **98,332** as of 2026-07-29 — the test is byte-identity, not the number. |
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

### 2b · The editorial agent: `/no-ai-slop`

`.claude/skills/no-ai-slop/` (vendored 2026-07-29) is the fourth kind of tool:
the detectors above are batch regex; this is judgment applied to one draft at a
time. It has two modes and each has exactly one job in this plan:

- **Edit mode is the rewrite protocol for W1–W3.** Any new or rewritten prose —
  a stopping condition, a fixed negation, a genre-marker sentence — goes
  through an edit pass *before* the mechanical gates. Its workflow step 2
  (identify 3–5 voice signals to preserve) must be answered explicitly with
  *whose* voice: Wendell's Part-2 register, the named Head (use that Head's
  SEVEN_VOICES flavor markers as the signals), or the unsigned margin. Never
  run it on a treatise without naming the Head.
- **Detect mode is the adjudication protocol for W4–W5.** Paste the paragraph
  around each `review.py` candidate; the output is named patterns with quoted
  lines and short fixes, no rewrite. A human rules on each. This is the "review
  agent" the handoff's adjudication doctrine calls for.

**Precedence, where the skill and house doctrine disagree.** Canon and the
marginalia rules govern; the skill yields on exactly three points:

1. *Binary contrasts / negative listing*: the skill cuts them all.
   RULE_COLLISIONS is finer — ranking negation licensed, denying banned — and
   RULE_COLLISIONS governs. Use the skill to find candidates, the
   still-true-when-the-sentence-ends test to rule.
2. *Fragments and rhythm*: the skill's dramatic-fragmentation and
   robotic-rhythm rules do not apply inside Sections 1–3 where SEVEN_VOICES
   *requires* the pattern (Corin's staccato variance, Maera's unconcluded
   entries). They apply fully to Wendell's Part-2 register.
3. *Em dashes*: house style uses spaced em dashes freely; the canon gate bans
   only unspaced joins. The skill's 1–2-per-draft budget is advisory here, not
   binding.

Everything else in the skill — minimum effective edit, voice preservation,
concrete-over-abstract, and its patterns the house rules don't cover
(faux-insight setups, colon reveals, weasel attribution, synonym cycling,
importance puffery, summary-recap endings) — applies as written, to both
surfaces.

**Measured against canon, 2026-07-29.** The skill's banned-word and
empty-phrase lists were scanned over both surfaces. Margin: fully clean. Body:
27 word hits, of which **22 are `leverage point(s)` — Donella-Meadows-register
term of art central to the Architect chapter, licensed, do not re-flag** — and
3 are *facilitator/facilitated* as the real noun, also licensed. Four true
candidates, added to W5:

| Site | Pattern | Sketch of fix |
|---|---|---|
| ch8:443 | faux-insight setup | *"Here's the thing nobody says about panoramic vision: it is lonely."* → *"Panoramic vision is lonely."* |
| ch9:408 | faux-insight setup | *"Here's the thing the culture doesn't tell you:"* → cut the setup, keep the claim |
| ch2:313 | empty opener | *"At its core, it's the body's…"* → *"It is the body's…"* |
| ch7:296 | empty phrase | *"in terms of sheer presence"* — adjudicate; may be spoken register |

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

**Register layer.** `marginalia/specs/HEAD_REGISTERS.md` (2026-07-29) sits under
SEVEN_VOICES and supplies what each Head is doing with feeling while teaching —
Ash Fire→Triumph, Voss Water→Poignance, Quill compound, Vale Metal→Wonder, Cross
Metal→Water, Orr Fire→Wood. Every move is canon from ch3's channel table. The
Heads run the alchemy and never name it. Its ~60–120 words per chapter ride the
same edits as the genre markers, so W3 carries both; touching these paragraphs
twice risks the voice. Six placeholder facts are open and nothing ships with a
`⟦` token in it.

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

### W6 — Retire the "village version" formula *(ruled 2026-07-29; supersedes part of W1)*

**The defect is repetition plus abstraction, and the second one matters more.**
*The village version* appears exactly five times, once per Section 3, in ch3,
ch4, ch5, ch6, and ch7 — the same slot in five consecutive chapters. A reader
who notices it once notices it every time after.

| Ch | Current |
|---|---|
| 3 | *It's not emotional processing. That's the village version —* |
| 4 | *It's not aggression. That's the village version —* |
| 5 | *It's not nostalgia. That's the village version —* |
| 6 | *The village version of structural design is organizational design —* |
| 7 | *The village version is the ultimatum.* |

**The fix is not a synonym for "village version."** Rotating the phrase leaves
the real problem in place: it is a noun phrase that names a *thing* where the
sentence should be naming an *act*. It reports that a wrong version exists
without saying what the village actually does to the teaching.

**Required form: an active verb naming how the village mis-reads the Face's
healthy lesson.** Flattens, hears-as, mistakes-for, reduces-to, hardens-into.
The verb has to carry the specific failure of interpretation, and it should
differ per Face, because each Face is misread differently — that difference is
content the formula was throwing away.

Sketches only, to fix the shape — the real verbs come out of each chapter:

- ch3 — *The village flattens alchemy into processing:* the neat, linear model
  where you identify, understand, release, and move on.
- ch4 — *The village hears the clean no as aggression:* the Challenger as the
  angry one, the difficult one…
- ch5 — *The village mistakes the practice for nostalgia:* we do it this way
  because we have always done it this way.
- ch6 — *The village reduces structural design to the org chart:* the RACI
  matrix, the role description, the meeting cadence.
- ch7 — *The village hardens terms into ultimatums:* what someone says when
  they have decided to leave and want you to know it is your fault.

**This supersedes the W1 treatment of ch3/ch4/ch5.** Those three denying
negations were held pending a ruling and should now be resolved by W6 rather
than by the ch6 pattern proposed on 2026-07-29 — that proposal preserved the
formula and is withdrawn. **The ch6 edit already committed (`22c711d`) is
provisional for the same reason:** it removed the denying negation and the D1
opener correctly, but rebuilt the sentence as *"The village version of X is
Y,"* which is the formula this item retires. Redo it here.

Scope: five sentences, one per chapter. Each runs the §2b loop with the Head
named (Voss, Ash, Quill, Vale, Cross), then gate + review.

### W7 — The denying-negation shape, properly measured *(opened 2026-07-29)*

**The rule was written down and nothing enforced it.** Every detector keyed on
the literal strings `it's not` and `isn't the`. The identical shape in other
words — *"The test is not whether they stopped. The test is whether…"* — matched
nothing. `review.py` now carries `DENYING_GENERAL`, which tests the shape:
a negated predicate followed by the same subject restated positively,
excluding *not just/only/merely*, which is ranking and licensed.

**Book-wide count went 2 → 107.** Per chapter: ch1 2 · ch2 4 · ch3 16 · ch4 9 ·
ch5 14 · ch6 12 · ch7 15 · ch8 17 · ch9 18. The margin is clean at 0.

Two consequences that are not bookkeeping:

- **Ch7's five live stopping conditions are built on the banned shape**, and so
  is the form `EXERCISE_AUDIT`, `GAME_LOOP_GAP_ANALYSIS`, and the handoff all
  prescribe for reuse: *"the test is not [outcome you cannot control], the test
  is [the thing you did]."* The specs prescribe what the house rule bans. W2's
  first draft inherited it unexamined; the replacement form states the act and
  defers the outcome positively.
- **It is a candidate count, not a defect count.** Every one needs the
  RULE_COLLISIONS test applied by hand; the detector cannot tell ranking from
  denying, and it cannot see a subject change.

**Batch 1 complete, and the schedule claim is withdrawn.** This spec first said
W7 "cannot be cleared before August 1." That was asserted without measurement
and it was wrong. The 25 treatise-half candidates were adjudicated and cleared
in a single working pass: **22 rewrites, 3 kept.** Treatise halves 25 → 3, book
total 103 → 81, and all three survivors are adjudicated keeps.

| Kept | Why |
|---|---|
| ch2:136 | *"The problem is not that you wanted to be good."* Ranking — she did want to be good, it stays true, and it is ranked under the real problem. Adams' cave ladder. |
| ch8:81 | *"That much is not in question."* Idiomatic, not definitional. False positive. |
| ch8:144 | *"These three are not obviously wrong. The Sage in distortion is…"* The detector spans a **subject change**, not a restatement. False positive, exposed by batch 1's own edit. |

**Measured rate: ~25 candidates per pass**, most resolving to a mechanical
"delete the negated clause, keep the positive." The expensive ones are the few
carrying a distinction worth preserving — ch5's three-way *conservatism /
rigidity / always done it*, ch7's *niceness / conflict-avoidance / absence of
judgment*, both rewritten as positive lists of what the thing is mistaken for.

**Batch 2 — ch9 and ch3, 30 sites, one pass.** First batch to run the four-move
method rather than arrive at it. ch9 clear, ch3 clear. Book total **82 → 52**.

Two things it taught:

- **The detector misses cross-paragraph pairs on a line-by-line scan.** ch3's
  *"That is not the promise."* / *"The promise is discernment."* sits either
  side of a paragraph break and only surfaced on a whole-file scan. Scan whole
  files, not lines.
- **Three sites took a bare cut and nothing else.** Where the surviving positive
  already runs long, appending a synthesis line pads it. Move 2 and 3 are
  mandatory to *consider*, not to perform.

**Remaining: 52** — ch8 14 · ch5 10 · ch6 10 · ch7 8 · ch2 3 · ch1 2, plus
strays. Order largest first.

**The method is now fixed and lives in `MANUSCRIPT_FILE_CANON.md`** under
*Fixing a denying negation — the four moves, in one pass*: cut, essence,
synthesize, voice. Batch 1 took four passes to arrive at it (cut → essence →
synthesize → voice, each correcting the last). Later batches run it as one, so
the rate estimate above holds even with the extra moves.

Two things the four-move sequence proved, worth keeping:

- **Move 3 is the one that matters.** A positive two-clause contrast still
  stages an opposition. Chapter 3's polarity doctrine — *one action containing
  both* — is the test, and most of these sites sit on a named pair.
- **Move 4 pays twice.** Voicing the synthesis lines to each Head cleared ch8's
  genre-absent BLOCK and raised markers in ch5 and ch6, so W7 and W3 are the
  same edit on these paragraphs. Voice BLOCK 3 → 1; only ch4's hedge particles
  remain.

**`/no-ai-slop` must actually be invoked.** Batch 1, the essence pass and the
synthesis pass were all checked with a hand-rolled regex panel standing in for
the skill, which is the same substitution that let the original 25 tests through
in the banned shape. The skill's robotic-rhythm rule is what caught the copula
formula; no pattern in `review.py` or `gate.py` can see it.

Sequencing: W7 supersedes the denying-negation portion of W1, which reported 7
because the detector could only see 7.

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
4. **R4 — CLOSED 2026-07-29.** Appendix G is `ON_THE_SHOULDERS_OF.md`, a
   source-lineage bibliography rather than a belief-to-superpower map, so the six
   daemon-alliance byline lines have nothing to be diffed against. It asked
   whether the appendix was "in any package"; it was in this repository the whole
   time.
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
9. **R9 — the six Head biography facts** (`marginalia/specs/HEAD_REGISTERS.md`).
   Deferred by ruling on 2026-07-29: the placeholders ship in the working tree
   and get filled later. **Two are live in canon right now** — `⟦ASH-AGE⟧` and
   `⟦ASH-SPAN⟧` in ch4's Section 3 — and four more (`⟦VOSS-SPAN⟧`,
   `⟦QUILL-CLAUSE⟧`, `⟦VALE-SYSTEM⟧`, `⟦ORR-DEFLECTION⟧`) arrive as W3 reaches
   those chapters. `instruments/gate.py` now carries a `tokens` counter that
   fails on any surviving `⟦`; it is the only thing between a placeholder and
   the typesetter, so **the gate cannot be declared green until R9 is closed.**

8. **R8 — ch3:740 A0 hit** (*"a time you were told something true"*): license
   as recall-prompt or rewrite.

---

*Changelog: created 2026-07-29 from the files_2 handoff. Baselines in §3 are
reproducible: `gate.py`, `review.py` (each mode), `compile.py --verify`.*
