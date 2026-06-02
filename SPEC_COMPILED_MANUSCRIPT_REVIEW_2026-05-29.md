# SPEC — Compiled Manuscript for Whole-Book Ideal-Reader Review

**Created:** 2026-05-29
**Status:** Proposal (the compiled file is a *derived surface*; per the Canon Rule, no canonical write happens without Wendell's approval)
**Owner:** editorial
**Purpose:** Produce a single compiled file of the entire book — Ch0–Ch8 + Appendices A–E — **with pending edits applied into the compile**, so the ideal-reader developmental-editing prompt can be run across the whole book in one continuous pass (not just chapter-by-chapter).

---

## 1. Why compile

Chapter-by-chapter review (done for Ch0) catches per-chapter problems. It **cannot** catch the cross-book failures that are exactly where this reader gets stuck:

- **Framework accumulation.** Ch0 alone hands her ~13 frameworks. By Ch4 she may be drowning in a map she's mastering instead of territory she's walking. Only a whole-book read surfaces the cumulative mastery-loop load.
- **Repeated shame-loop triggers.** A phrase that's fine once may be corrosive as a recurring tic across 9 chapters. (E.g., "you will never be ready," "not enough," retroactive-indictment closes.)
- **ROI-argument trajectory.** The "bullshit prizes" reframe has to *build* — cost in early chapters, prize-hunger later. Does the payoff land by Ch8, or does the book stay all-cost?
- **Eight-gates fatigue (Issue 5).** Repetition by Ch7 is a structural read only visible in sequence.
- **Voice drift across faces** (Issues 2, 12, 15-Ch6).

The compiled file is the **input artifact** for that whole-book read.

---

## 2. Canon safety (non-negotiable)

- The compiled file is a **derived surface**. It is built FROM canonical chapter files; it is never written BACK to them.
- Applied pending edits live **only in the compile** until Wendell promotes any of them to canon in Obsidian.
- Every applied edit carries a **provenance marker** (see §6) so nothing can leak into canon unattributed.
- Output path: `manuscripts/compiled/MTGOA_COMPILED_<DATE>.md` (new `compiled/` dir; treat as build output, regenerable, never hand-edited as source).

---

## 3. Source manifest — chapters (canonical, verified 2026-05-29)

| Order | Chapter | Canonical file | Words |
|---|---|---|---|
| 1 | Ch0 — The Infinite Arcade | `chapters/ch0-infinite-arcade/CHAPTER0_DRAFT.md` | 6,086 |
| 2 | Ch1 — The Forest (Shaman threshold) | `chapters/ch1-SHAMAN/CHAPTER1_FULL_DRAFT.md` | 8,460 |
| 3 | Ch2 — The Shaman | `chapters/ch2-SHAMAN/CHAPTER2_SHAMAN_FULL_DRAFT.md` | 12,722 |
| 4 | Ch3 — The Challenger | `chapters/ch3-CHALLENGER/CHAPTER3_CHALLENGER_FULL_DRAFT.md` | 10,135 |
| 5 | Ch4 — The Regent | `chapters/ch4-REGENT/CHAPTER4_REGENT_FULL_DRAFT.md` | 8,561 |
| 6 | Ch5 — The Architect | `chapters/ch5-ARCHITECT/CHAPTER5_ARCHITECT_FULL_DRAFT.md` | 7,996 |
| 7 | Ch6 — The Diplomat | `chapters/ch6-diplomat/CHAPTER6_DIPLOMAT_FULL_DRAFT_MASTER.md` | 11,853 |
| 8 | Ch7 — The Sage | `chapters/ch7-sage/CHAPTER7_SAGE_FULL_DRAFT.md` | 15,104 |
| 9 | Ch8 — The Player | `chapters/ch8-player/CHAPTER8_PLAYER_FULL_DRAFT.md` | 8,786 |

**Total chapter prose:** ~89,700 words.

> Note: `chapters/ch5-architect/` (lowercase) holds only PLAN.md/TASKS.md — **not** manuscript. Canonical Ch5 is `ch5-ARCHITECT/` (uppercase). Do not compile the lowercase dir.

---

## 4. Source manifest — appendices (all five A–E represented)

| Section | Title | Source | Status |
|---|---|---|---|
| A | Four Allyship Domains | `appendices/APPENDIX_A_FOUR_ALLYSHIP_DOMAINS.md` (3,107w) | Prose; depth-passed 2026-05-29 (Issue 15) |
| B | Quests + Campaigns | — (per `docs/plans/2026-05-21-appendix-design.md`) | **Not written** → reserved placeholder w/ design summary (Issue 13) |
| C | Key Terms (≤20) | `appendices/APPENDIX_C_KEY_TERMS.md` (1,079w) | Prose |
| D | EA Practices (Happy Apples / Grounding / The Rose) | design spec only; draft noted in memory | **Draft pending** → reserved placeholder; pull draft if located (Issue 13) |
| E | Bibliography | source citations scattered across chapters | **Not written** → reserved placeholder; needs Wendell pass (Issue 13) |

For B, D, E: insert a labeled section header + a 2–4 line summary of the planned content (from the appendix design spec) so the reviewer can assess the *intended* structure and flag arc-level gaps. Mark unmistakably as `[NOT YET WRITTEN]`.

---

## 5. Pending-edit application model

"Apply edits into the compile" only works cleanly for edits whose prose exists. Most tracker issues are *diagnosed*, not *drafted*. So classify every pending edit into one of three readiness tiers and handle each differently:

### Tier R — Ready (apply directly)
Edited prose exists or is mechanically derivable (e.g., a locked line swap).
→ Apply into the compile verbatim. Wrap in provenance markers.

### Tier D — Draftable (draft into compile, mark provisional)
Diagnosis + spec exist; prose must be written to spec.
→ Draft the replacement/insertion into the compile, marked `PROVISIONAL — drafted to spec, not canon`. This is the bulk of the work and is itself an editorial drafting task gated by the spec it derives from.

### Tier U — Unresolved (cannot apply — insert editorial note)
Design problem with no chosen solution.
→ Do **not** fabricate a fix. Insert a labeled `[EDITORIAL NOTE — UNRESOLVED]` at the locus describing the known gap, so the ideal-reader review accounts for it rather than reviewing around a hole.

---

## 6. Pending-edit inventory (mapped to tiers)

| Source | Locus | Tier | Compile action |
|---|---|---|---|
| **Ch0 fixes** P1-1 ("not enough"→"not where the game is played"; forward-tense indictment) | Ch0 lines ~277–289, 323 | R | Apply line swaps |
| **Ch0 fixes** P0-1/P0-2 (BAR relocation + bounded first action) | Ch0 BAR + Three Games | D | Draft to `SPEC_CH0_IDEAL_READER_FIXES_2026-05-29.md` |
| **Ch0 fixes** P0-3 (company-before-frame at the blade) | Ch0 ~line 45 | D | Draft confession beat |
| **Ch0 fixes** P0-4 (give both prizes a body) | Ch0 Ticket System | D | Draft somatic prize prose |
| **Ch0 fixes** P2-1/P2-2 (de-genericize vignettes; demote citations; cut "Vibeulons") | Ch0 §GM, 167 | R/D | Apply cuts; draft race-specific vignette |
| **Issue 2** — Wendell voice not yet applied to manuscript | all chapters | U | Editorial note (infra built, no edits) |
| **Issue 3** — Ch1+Ch2 oracle-card revision pass deferred | Ch1, Ch2 | U/D | Note; BARs already embedded elsewhere |
| **Issue 5** — eight-gates repetitive by Ch7 | Ch5–Ch7 | U | Editorial note at onset of fatigue |
| **Issue 6** — Ch8 doesn't integrate Six Faces | Ch8 | U | Editorial note |
| **Issue 10** — somatic poetics / Council of Joanne's / comedic calibration | all | U | Note (specs complete, awaiting session) |
| **Issue 11** — shame-parasite ontology integration | TBD chapters | U | Editorial note |
| **Issue 12** — Ch7 confession voice pass | Ch7 "A Note Before the Exile" | D | Draft voice pass to WENDELL_VOICE guides (no in-file flag found; confirm locus) |
| **Issue 13** — Appendices B, D, E unwritten | Appendix | U | Reserved placeholders (see §4) |
| **Issue 15 (domains)** — Four Domains depth pass | Appendix A | R | Already applied in source (2026-05-29) |
| **Issue 15 (Ch6)** — Integrative Negotiator voice pass deferred | Ch6 Channel 5 | U | Editorial note |
| **Issue 16** — spec↔manuscript drift (Ch4 polarity + Ch6 Move 3 merge) | Ch4, Ch6 | U | Editorial note (architecture approved, implementation gated) |

> **Sequencing implication:** Tier-R edits can go into a compile *today*. Tier-D edits require drafting passes first (the Ch0 fixes spec is the model). A useful intermediate deliverable is a **Tier-R-only compile** (current prose + safe line fixes + unresolved notes) that's reviewable immediately, with Tier-D drafts folded in as they're written.

---

## 7. Compiled file structure

```
# MASTERING THE GAME OF ALLYSHIP — COMPILED REVIEW BUILD
<provenance header: build date, source commit, edit-tier legend, "DERIVED — NOT CANON">

<Table of Contents with word counts>

═══════════════════════════════════════
# CHAPTER 0 — The Infinite Arcade
<source: path | words | edits applied: [list]>
───────────────────────────────────────
<prose, with inline provenance markers around applied edits>

  [[EDIT R: Ch0 P1-1 — "not enough" swap ............... ]] ... [[/EDIT]]
  [[EDIT D: Ch0 P0-3 company-before-frame (PROVISIONAL) ]] ... [[/EDIT]]
  [[EDITORIAL NOTE — UNRESOLVED: Issue 2 voice not applied]]

═══════════════════════════════════════
# CHAPTER 1 ...
...
═══════════════════════════════════════
# APPENDIX A — Four Allyship Domains
...
# APPENDIX B — Quests + Campaigns   [NOT YET WRITTEN]
<planned-content summary>
...
```

**Marker conventions** (chosen so they're greppable AND visible to the reviewer):
- `[[EDIT R: <id> — <desc>]] … [[/EDIT]]` — Ready edit applied.
- `[[EDIT D: <id> — <desc> (PROVISIONAL)]] … [[/EDIT]]` — Draftable edit, drafted to spec.
- `[[EDITORIAL NOTE — UNRESOLVED: <id> — <gap>]]` — Tier-U gap flagged in place.
- Chapter separators: heavy rule `═` between chapters, light rule `─` between header and prose.

The markers do double duty: (1) the ideal-reader review reads *through* them as "this is the intended prose," and (2) any later promotion to canon can grep `[[EDIT` to find exactly what changed and where it came from.

---

## 8. Build process

1. Create `manuscripts/compiled/`.
2. Emit provenance header + tier legend + TOC.
3. For each chapter in order: emit chapter header (source path, words, edits-applied list) → emit prose → splice Tier-R edits and Tier-D drafts at their loci with markers → insert Tier-U editorial notes at their loci.
4. Append Appendices A–E (A, C prose; B, D, E placeholders w/ design summaries).
5. Emit a closing **Pending-Edit Ledger** (every marker in the doc, listed with tier + source issue) for at-a-glance audit.
6. Record build metadata (date, git commit of sources, total words) in the header.
7. **Do not** write anything back to canonical files.

A regenerate step must be cheap: the compile is rebuildable from sources + this spec at any time. If a Tier-D draft is promoted to canon in Obsidian, drop its marker on next rebuild.

---

## 9. The whole-book review pass (what the compile feeds)

Run the ideal-reader developmental-editing prompt in two layers:

**Layer 1 — Per-chapter** (the existing 5 analyses): defense-up / stay-stuck / shame-loop / loses-me / central-argument-ROI. One pass per chapter, reading the compiled (edits-applied) prose.

**Layer 2 — Cross-book synthesis** (only possible on the compile):
- **Framework-load curve** — cumulative count of new frameworks/terms introduced per chapter; where does the mastery-loop risk peak?
- **Shame-trigger recurrence** — every repeated phrase/move that feeds the loop, tracked across chapters.
- **ROI trajectory** — does cost-vs-prize balance shift from all-cost (early) to prize-hunger (late)? Where does the reader start *wanting* the renewable prize?
- **Gate-fatigue onset** (Issue 5) — the chapter where eight-gates repetition stops earning its length.
- **Voice consistency** across the six faces (Issues 2, 12).
- **The off-ramp audit** — across the whole book, how many bounded *external* actions is she actually asked to take vs. acts of self-reflection?

Output artifacts:
- `manuscripts/editorial_reports/IDEAL_READER_WHOLEBOOK_<DATE>.md` — Layer 1 + Layer 2.
- Per-chapter fixes specs in the chapter dirs (model: `SPEC_CH0_IDEAL_READER_FIXES_2026-05-29.md`).

---

## 10. Acceptance criteria

- [ ] Single compiled file exists at `manuscripts/compiled/MTGOA_COMPILED_<DATE>.md`.
- [ ] All 9 chapters present, in order, from the verified canonical files in §3.
- [ ] Appendices A–E all represented (A, C prose; B, D, E labeled placeholders w/ design summaries).
- [ ] Every applied edit carries a provenance marker (`[[EDIT R/D ...]]`); every Tier-U gap carries an `[[EDITORIAL NOTE]]`.
- [ ] Header declares **DERIVED — NOT CANON** + build date + source commit.
- [ ] Closing Pending-Edit Ledger lists every marker with tier + source issue.
- [ ] No canonical chapter or appendix file was modified by the build.
- [ ] File is regenerable from sources + this spec (no hand-editing of the compile as source).

---

## 11. Open questions / decisions to confirm

1. **Tier-D drafting scope.** Draft *all* Tier-D edits before first compile, or ship a **Tier-R-only compile now** and fold Tier-D drafts in as written? (Recommend: Tier-R-only first — reviewable immediately, avoids blocking on a large drafting backlog.)
2. **Issue 12 locus.** Memory says Ch7 confession carries a `VOICE PASS NEEDED` flag; grep of the canonical file finds none. Confirm whether the pass was already applied or the flag was removed without the pass.
3. **Appendix D draft.** Memory notes a draft exists "from IJ source." Locate it for inclusion, or treat D as placeholder.
4. **Front/back matter.** Title page, dedication, intro/foreword, TOC — in scope for the compile, or chapters+appendices only?
5. **Promotion path.** When a Tier-D draft is approved, what's the ritual for promoting it from compile → Obsidian canon? (Out of scope for this spec, but the markers are designed to support it.)
```
