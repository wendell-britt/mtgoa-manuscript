# SPEC — MTGOA Editorial Agent Design
**Type:** Editorial AI Agent
**Status:** Draft
**Date:** 2026-04-21

---

## What This Is

A multi-pass AI editorial agent for the MTGOA manuscript. Not a single LLM reviewing the whole book — a pipeline of specialized passes, each with a specific framework grounding, a defined job, and a structured output that feeds into the next pass.

Modeled on: PAT (Paper Analysis Tool)[^1] + bars-engine EDITORIAL_PASS_1[^2] + editorial best practices[^3]

---

## Why Not One Big Pass

A single LLM reviewing 60,000 words of manuscript produces:
- Inconsistent standards across chapters
- No framework grounding (judgments without stated criteria)
- No audit trail (you can't trace *why* a suggestion was made)
- LLM Hallucination risk increases with context length
- Impossible to iterate systematically

The multi-pass approach solves all of these. Each pass is shallow enough to be reliable, grounded enough to be consistent, and structured enough to produce a changelog.

---

## The Four Passes

### Phase 0 — Deterministic Metrics (no LLM)

**Purpose:** Establish objective baseline before editorial passes begin.

Computed via regex + heuristics — zero LLM involvement, fully deterministic.

| Metric | What it measures |
|--------|----------------|
| Passive voice ratio | % of sentences with passive construction |
| Average sentence length | Words per sentence |
| Flesch-Kincaid grade | Reading level equivalent |
| Long-sentence fraction | % of sentences >25 words |
| Hedge-word density | "perhaps", "might", "may", "somewhat" per 1000 words |
| Section word count vs spec target | Per-chapter deviation from word targets |

**Output:** `metrics_phase0.yaml` — structured per chapter, versioned, diffable against prior run.

**This is what PAT got right:** Deterministic metrics give you a before/after comparison that doesn't depend on LLM judgment. After every editorial pass, re-run Phase 0 and diff. If passive voice didn't decrease, the pass didn't work.

---

### Pass 1 — Structural Integrity (LLM)

**Framework grounding:** Chapter spec (each chapter's SPEC.md)

**Agent role:** Does this chapter do what its spec says it should do?

**Checklist:**
- [ ] Core thesis appears in first 10% of chapter
- [ ] All 7 sections present (Exile, Distortion, Concept, Practice, Journey, Game, Recap)
- [ ] Arc-bridge from previous chapter present
- [ ] Bridge to next chapter present
- [ ] Vulnerable Child superpower named and embodied
- [ ] Through-line stated explicitly
- [ ] Reflection prompts present (5)
- [ ] Word count within ±15% of spec target

**Structured output:**
```yaml
chapter: ch7-sage
pass: structural_integrity
version: 1
checks:
  - id: thesis_presence
    status: PASS | FAIL | PARTIAL
    evidence: "Found at line X: 'Mastery is knowing...'"
    severity: BLOCKER | WARNING
  - id: section_completeness
    status: PASS
    sections_found: [Exile, Distortion, Concept, Practice, Journey, Game, Recap]
    sections_missing: []
  - id: word_count_deviation
    status: PASS | FAIL
    actual: 13188
    spec_target: 12000
    deviation_pct: 9.9
suggestions:
  - type: ADD
    location: Section 2
    suggestion: "Shadow game 'The Trauma Olympics' could be expanded with one concrete example"
    effort: LOW | MED | HIGH
    impact: LOW | MED | HIGH
```

---

### Pass 2 — Voice Calibration (LLM)

**Framework grounding:** `voice-calibration-notes.md` (10 annotated passages with mechanical markers)

**Agent role:** Does this chapter sound like Wendell?

**Method:** 
1. Extract 3 random 200-word passages from chapter
2. Score each against the 10 calibration passages
3. Flag specific deviations from voice markers:
   - Discovery idioms: "Here's what I've noticed," "Here's what's true"
   - Labor metaphors: the work, the practice, the path
   - Self-deprecation via named parts
   - Permission-granters: "You can," "You don't have to"
   - Direct second-person address
   - "Weird. But literally." as acknowledgment
   - Short sentences when arriving at truth

**Structured output:**
```yaml
chapter: ch7-sage
pass: voice_calibration
version: 1
calibration_score: 0.82  # 0-1
deviations:
  - type: MISSING_DISCOVERY_IDIOM
    location: Section 3, para 2
    suggestion: "Consider adding 'Here's what I've noticed' before the altitude description"
  - type: EXCESSIVE_HEDGING
    location: Section 5, para 7
    evidence: "perhaps, might, could, somewhat"
    suggestion: "Remove hedges — the Sage doesn't hedge"
```

---

### Pass 3 — Developmental / Face Review (LLM)

**Framework grounding:** Each face's chapter spec + MTGOA AQAL framework

**Agent role (3-face approach):**[^2]

**Challenger review:**
- Does the chapter demand something uncomfortable?
- Is there genuine edge, or is it playing safe?
- Shadow named but not dwelt in

**Regent review:**
- Does the move type match the structural slot?
- Is the stage sequence (where applicable) correctly sequenced?
- Is this chapter earning the next one structurally?

**Shaman review:**
- Does the language carry this altitude's specific mythic energy?
- Does the chapter feel like it belongs to this face, or could the language belong to any chapter?
- EA labels present and correctly mapped (for ch7: Metal/Fear, Fire/Anger, Earth/Neutral, Wood/Joy, Water/Sadness)

**Each face produces:** Flag list with severity (🔴 BLOCKER / 🟡 WARNING / 🟢 NOTED)

**Example (from bars-engine EDITORIAL_PASS_1):**
```yaml
face: shaman
chapter: ch7-sage
review:
  - card: "Section 4 — Panoramic Seer"
    severity: 🟡
    issue: "The practice section uses 'notice' where 'name' would be more precise for Teal altitude"
    rule: "Teal practice should use declarative naming, not soft observation"
  - card: "Section 2 — Shadow Games"
    severity: 🟢
    note: "'The Trauma Olympics' is exemplary Shadow Sage language — model for other shadow sections"
```

---

### Pass 4 — Mechanical Polish (Deterministic + LLM hybrid)

**Deterministic (no LLM):**
- Remove double spaces
- Fix three-dot sequences (should be ellipsis: … not ...)
- Ensure em-dashes are consistent (`—` vs ` -- `)
- Check for orphaned section headers
- Verify last line matches chapter spec

**LLM-assisted (light):**
- Passive voice flagging (feed Phase 0 results + targeted rewrite suggestions)
- Long sentence breakdown (flag sentences >30 words, suggest splits)
- Repeated word clusters (same adjective used 3+ times in 50-word window)

**Structured output:**
```yaml
chapter: ch7-sage
pass: mechanical_polish
version: 1
deterministic_fixes_applied: 12
llm_suggestions:
  - type: SPLIT_SENTENCE
    location: Section 4, line 47
    original: "The Sage who has gone up and come back is more valuable than the Sage who stays above."
    suggestions:
      - "The Sage who has gone up and come back is more valuable than the one who stays above."
      - "The Sage who returns is more valuable than the Sage who stays above."
passive_voice_instances: 3
passive_voice_locations: [Section 2, line 12, Section 5, line 31, Section 7, line 8]
```

---

## Pipeline Architecture

```
Chapter draft
    │
    ├─► Phase 0: Deterministic Metrics ──────┐
    │                                        │
    │   metrics_phase0.yaml                 │
    │   (word count, passive voice,          │
    │    sentence length, Flesch-Kincaid)   │
    │                                        │
    ├─► Pass 1: Structural Integrity         │
    │       (vs chapter SPEC.md)            ├─► Combined Report
    │                                        │   per chapter
    ├─► Pass 2: Voice Calibration          │   (all passes)
    │       (vs voice-calibration-notes.md)  │
    │                                        │
    ├─► Pass 3: Developmental / 3-Face      │
    │       (vs AQAL + face specs)          │
    │                                        │
    ├─► Pass 4: Mechanical Polish            │
    │       (deterministic + light LLM)      │
    │                                        │
    └────────────────────────────────────────┘
              │
              ▼
    Combined Editorial Report (per chapter)
    │
    ├─► Actionable suggestions (sorted by effort/impact)
    ├─► BLOCKER issues (must fix before next draft)
    ├─► Phase 0 diff vs prior run (passive voice delta, etc.)
    └─► Approval: READY FOR REVISION / NEEDS DISCUSSION
```

---

## Decision Layer: What Gets Applied Automatically

| Pass | Auto-apply | Requires human decision |
|------|-----------|----------------------|
| Phase 0 metrics | Always | None — it's deterministic |
| Pass 1 structural: missing sections | Flag only | Human adds missing sections |
| Pass 1 structural: word count | Flag only | Human expands/contracts |
| Pass 2 voice deviations | Flag only | Human rewrites |
| Pass 3 Challenger: missing edge | Flag only | Human decides |
| Pass 3 Regent: structural mismatch | Flag only | Human reviews |
| Pass 3 Shaman: wrong register | Flag only | Human rewrites |
| Pass 4 deterministic fixes | **YES** | Auto-applied with diff shown |
| Pass 4 passive voice rewrite | Flag only | Human approves rewrite |

**Rationale:** Mechanical fixes (Phase 0, Pass 4 deterministic) are low-risk and high-value — apply automatically. Everything that touches meaning, voice, or structure requires human judgment because the author's voice and intent must be preserved.

---

## Output: The Editorial Report

Each chapter generates a report:

```
# EDITORIAL REPORT — Ch7 Sage
**Pipeline version:** 1.0
**Generated:** 2026-04-21
**Manuscript state:** FIRST DRAFT

## Phase 0: Metrics

| Metric | Value | Status |
|--------|-------|--------|
| Word count | 13,188 | ✅ Within spec |
| Passive voice % | 8.2% | ✅ < 15% target |
| Avg sentence length | 18.4 words | ⚠️ 3 sentences >30 words |
| Flesch-Kincaid | Grade 11 | ✅ Target 10-12 |

**Prior run delta:** +0.3% passive voice (regression — check Pass 4)

---

## BLOCKERS (must fix before next draft)

- [ ] **Pass 3 / Challenger:** Section 3 lacks genuine edge — "The Sage sees all altitudes" is stated but not demonstrated through discomfort. Need one concrete moment where seeing was costly.

---

## RECOMMENDATIONS (sorted by effort/impact)

### High Impact / Low Effort
1. **Pass 2 / Voice:** Add "Here's what I've noticed" in Section 3 before altitude description (~30 sec fix)
2. **Pass 4:** Split 3 long sentences in Section 5 (~2 min fix)

### Medium Effort
3. **Pass 3 / Shaman:** Section 2 shadow games language is strong — use as model for Section 4 practice language
4. **Pass 1:** Arc-bridge from Ch6 (Diplomat) is implicit but not explicit — add one sentence at S7 opening

---

## Decisions Needed

1. **S3 / Challenger edge:** Does the Sage need to draw a line in the Concept section, or is the altitude-switching sufficient edge?
2. **Q2 from spec:** Any specific altitude-naming moments to include? (Wendell input needed)

---

## Approval

- [ ] **READY FOR REVISION** — Fix blockers, apply mechanical auto-fixes, revise based on recommendations
- [ ] **NEEDS DISCUSSION** — blockers require Wendell input before proceeding
```

---

## Wake-Up Phase Research

Before building this agent, research these open questions during the morning session:

1. **PAT's 72.4% usefulness accuracy** — Can we validate our editorial pass framework against an external standard?
2. **NovelCrafter's pipeline mode** — How do they chain prompts sequentially? What's the token management strategy?
3. **ProseEngine's quality-gated chapters** — Do they have a published architecture for chapter-level quality gates?
4. **BubbleCow's "no new facts" rule** — Does our editorial agent ever introduce new claims, or only surface existing ones?

---

## What Makes This Approach Different

| Typical AI editing | This approach |
|-------------------|--------------|
| Single LLM, whole manuscript | Shallow specialized passes |
| No framework grounding | Each pass anchored to a named spec |
| Unexplained suggestions | Structured output with severity + evidence |
| No audit trail | Versioned reports, diffable |
| Human reviews everything | Deterministic auto-applied, only meaning choices escalated |
| LLM hallucination risk high | Short context per pass = lower hallucination |

---

## What Still Needs Design Decisions

1. **Chapter ordering:** Does the pipeline run on chapters sequentially (Ch0→Ch8) or in parallel? Sequential allows arc-bridge checks; parallel is faster.
2. **Prioritization:** If BLOCKER issues are found, does the pipeline halt or continue to remaining chapters?
3. **Change logging:** When a suggestion is accepted/rejected, should we log that decision to train future passes?
4. **Voice calibration threshold:** At what calibration score do we escalate to human review? (Suggested: <0.7)
5. **Integration with tracker:** Does the editorial report update MTGOA_BOOK_WORK_TRACKER.md automatically?

---

## Companion Files

- `voice-calibration-notes.md` — 10 annotated passages with mechanical markers (already exist)
- `MTGOA_6FACE_CHAPTER_STRUCTURE.md` — template and full chapter outline
- `SPEC.md` per chapter — each face's chapter spec
- `bars-engine/.specify/specs/deck-card-move-grammar/EDITORIAL_PASS_1.md` — three-face reviewer model

---

## References

[^1]: Bhansali et al., "A Local, Multi-Agent LLM Framework for Objective Manuscript Editing," medRxiv 2026.04.13.26350761. Pipeline: 4 phases, 31 agents, framework-grounded evaluation, 72.4% validated usefulness accuracy.
[^2]: bars-engine EDITORIAL_PASS_1.md — Three-face approach (Challenger, Regent, Shaman), structured output with severity markers (🔴/🟡/🟢).
[^3]: BubbleCow editorial ethics: "track changes" protocol, no new facts rule, source log for AI-assisted edits.
