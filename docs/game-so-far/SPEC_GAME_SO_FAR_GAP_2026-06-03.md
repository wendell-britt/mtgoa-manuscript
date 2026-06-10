# SPEC -- "The Game So Far" Recurring Section: Gap Audit and Build Plan

**Created:** 2026-06-03
**Status:** PROVISIONAL -- gap surfaced, prompts staged, drafts not yet generated. Awaiting Wendell's call on whether to draft in this session or pause.
**Parent specs:**
- `SPEC_WHOLEBOOK_IDEAL_READER_FIXES_2026-05-29.md` (WB-1 conversion beat, WB-6 gate-walk de-densify)
- `SPEC_WHOLEBOOK_FIXES_6FACE_ANALYSIS_2026-05-29.md` (Sage classification of the fixes)
**Scope:** Ch2--Ch7 only (Ch8 already has the equivalent via "Try It Now: Sixty Seconds" at the close of Section 6).

---

## A. The problem (audited 2026-06-03)

You wrote six Claude Code prompt sequences -- one per chapter, Ch2 through Ch7 -- for a recurring section titled **"The Game So Far."** The prompts live in `chat-uploads/`. The recurring section itself, the scenario proposals, the altitude-blindness framing, and the per-Face close-register notes are not in any chapter file.

**Evidence (zero in any chapter file):**
- `grep "Game So Far" chapters/**` returns zero matches in Ch2--Ch7
- `grep "altitude blindness" chapters/**` returns zero matches
- `grep "scenario proposals" chapters/**` returns zero matches
- The 6 prompt templates total 45,481 bytes; the generated sections total zero bytes
- The Ch2 prompt references "the same book as the Ch8 'The Game So Far' draft" -- but no Ch8 "Game So Far" draft exists either; Ch8 has a related but distinct "Try It Now: Sixty Seconds" at the close of Section 6 (lines 511--524 in `ch8-player/CHAPTER8_PLAYER_FULL_DRAFT.md`)

**Stakes:** The recurring "Game So Far" section is the reader's mirror at the end of each chapter. The prompt templates are precise about register, length, and shadow specificity (Ch6: "this is the most important instance"; Ch7: "the dress rehearsal before Ch8"). If the section never lands, the book has six chapters that end in static toolkit exposition without a diagnostic moment that names what the reader is currently doing wrong. This is a structural gap, not a content gap.

**Stakes, second order:** The Ch6 prompt is explicitly framed as "the most important instance" because the ideal reader is meeting her own shadow at her home developmental level. If the section is missing here specifically, the book fails its most identified reader at the chapter where she needs it most.

---

## B. Charter of the section (what it has to do, per the prompts)

Each "Game So Far" is a recurring section that appears once per chapter. Its job, distilled from the six prompts:

1. **Open in a specific 2026 scenario** where the chapter's shadow is running. Not generic. Recognizable within the first two sentences.
2. **Show the shadow** with precision, not judgment. Name the pattern specifically (over-attunement, avoidance-then-explosion, accommodation-to-collapse, redesign-as-avoidance, field-disappearance, altitude-blindness).
3. **Run the chapter's toolkit** against the shadow. Toolkit size grows: Ch2=1 tool, Ch3=2, Ch4=3, Ch5=4, Ch6=5, Ch7=6. The cumulative structure is the point -- by Ch7 the reader has everything she needs.
4. **Close on a delta** -- one specific thing the reader can name, do, or ask, today. Not a summary. A diagnostic question or one concrete move.
5. **Length grows with the toolkit** (400--500 for Ch2, climbing to 600--700 for Ch6/Ch7). Voice stays second person, complete sentences only, no fragments, no negation stacks.
6. **Register is Face-specific** and must remain distinct across chapters: Bard (Ch2), Warm setup + clean line (Ch3), Compassionate gravity (Ch4), Mad-scientist delight (Ch5), Spock/Obama polyglot (Ch6), Uncle Iroh oblique (Ch7).

---

## C. Prompts staged (2026-06-03)

All six Claude Code prompt templates moved from `chat-uploads/` to `docs/game-so-far/`:

| Source | Target | Size |
|---|---|---|
| `chat-uploads/Ch2_Shaman_GameSoFar-c2860cc85698.md` | `docs/game-so-far/CH2-SHAMAN_GameSoFar_prompts.md` | 6,395 bytes |
| `chat-uploads/Ch3_Challenger_GameSoFar-5c8c19afe24d.md` | `docs/game-so-far/CH3-CHALLENGER_GameSoFar_prompts.md` | 7,064 bytes |
| `chat-uploads/Ch4_Regent_GameSoFar-7e410498e735.md` | `docs/game-so-far/CH4-REGENT_GameSoFar_prompts.md` | 7,134 bytes |
| `chat-uploads/Ch5_Architect_GameSoFar-c62b79a3c503.md` | `docs/game-so-far/CH5-ARCHITECT_GameSoFar_prompts.md` | 7,414 bytes |
| `chat-uploads/Ch6_Diplomat_GameSoFar-4acaceebfdaa.md` | `docs/game-so-far/CH6-DIPLOMAT_GameSoFar_prompts.md` | 9,463 bytes |
| `chat-uploads/Ch7_Sage_GameSoFar-b020dbc60a4a.md` | `docs/game-so-far/CH7-SAGE_GameSoFar_prompts.md` | 8,011 bytes |

**Why staged, not just referenced:** the prompts are detailed enough (each is 1,500--2,500 words of step-by-step Claude Code instructions including scenario-generation prompts, selection protocol, draft system prompt, fragment/negation repair pass) that they are themselves part of the build plan. Anyone running a chapter's section needs the prompt next to the draft, not buried in chat uploads.

**Backlinks from each prompt to this spec:** each prompt file's first line should be updated to reference this spec. (Pending. One-line edit per file.)

---

## D. Build order (recommended)

The six sections are not parallel work. They form a cumulative arc where each chapter's section depends on the prior ones being tonally and structurally consistent. Build in this order:

1. **Ch6 first** -- the most important instance. Gets the longest treatment. Establishes the template that the others pattern-match. ~700 words.
2. **Ch7 next** -- "dress rehearsal before Ch8." All six tools visible. Tests whether the cumulative structure lands. ~700 words.
3. **Ch5** -- the design move has to be concrete. Tests the "delight in the mechanism" register. ~600 words.
4. **Ch4** -- the thing being lost has to be concrete. Tests the "reluctant authority" register. ~550 words.
5. **Ch3** -- the avoidance-to-explosion sequence. The line must be a single sentence shown in the text. ~500 words.
6. **Ch2 last** -- the shortest. Establishes the pattern that the others build on. Must feel lean and unadorned. ~450 words.

**Why this order, not chapter order:** Ch6 and Ch7 are the hardest because they have the most tools and the most reader-identification risk. Ch2 and Ch3 are the easiest. If you start with the easy ones you lock in a register that Ch6 might not fit. Start with the hardest, then the template is set.

**Estimated word count across all six:** 3,500--3,900 words total. At 400--500 words per section, that is six sections of focused, register-distinct prose.

---

## E. Per-chapter sub-specs (not yet written)

When drafts are produced, each one needs a sub-spec that records:
- The selected scenario (from the three the prompt proposed)
- The shadow sentence (the one that names the pattern precisely)
- The load-bearing sentence (per chapter: Ch3=the line, Ch4=what is worth protecting, Ch5=the design move, Ch6=the terms of staying, Ch7=the altitude diagnosis, Ch2=the EA move)
- The author-shadow disclosure (if used; the prompts do not require one for Game So Far sections, distinguish from WB-1 First Move)
- The BAR prompt at close (if used; the prompts do not require one for Game So Far sections, distinguish from WB-1 First Move)
- The fragment/negation repair pass result (Option B: collapse negation pairs into complete sentences)

**File convention:** `docs/game-so-far/CH[N]-[FACE]_GameSoFar_draft.md` -- one per chapter. Drafts marked `PROVISIONAL` until Wendell promotes to canonical prose in the chapter file.

---

## F. Acceptance criteria (for the build to count as done)

- [ ] All six "Game So Far" sections drafted, each 400--700 words per its chapter's spec
- [ ] Each section's load-bearing sentence flagged in a sub-spec
- [ ] Each section's shadow named with precision (not judgment)
- [ ] Each section closes on a delta (one specific thing, not a summary)
- [ ] Voice-distinct across chapters (per Face register)
- [ ] No fragments, no negation stacks, second person throughout, complete sentences only
- [ ] Toolkit cumulative structure lands (Ch2=1 tool, Ch7=6 tools)
- [ ] Ch6's section is the longest and most pressure-creating (forward pressure, not just recognition)
- [ ] Ch7's altitude-blindness diagnosis names a specific altitude (Red, Orange, Amber), not just "wrong tool"
- [ ] Once promoted to canonical prose, no chapter regresses on existing WB-1 First Move upgrade (Ch1, Ch3, Ch8 already shipped 2026-06-03)

**Stop condition (Sage):** when the reader finishes a chapter and can name one specific thing she is currently doing that the chapter's shadow names, the section works. The test is recognition plus one specific move, not exhaustive coverage.

---

## G. Open question for Wendell

The prompts are detailed enough that they are runnable today via Claude Code (Step 1 scenario proposals, Step 2 selection, Step 3 draft, Step 4 fragment/negation repair, quality check). The question is whether to draft all six in this session, or to:

(a) Draft one (probably Ch6) to validate the prompt sequence works end-to-end, then decide.
(b) Draft all six in sequence per the build order above.
(c) Stage the prompts + sub-specs only (this current step) and pause for a fresh session to run the actual Claude Code sequences.

(c) is the safest. (b) is the most efficient if the prompts hold up. (a) is the middle path.
