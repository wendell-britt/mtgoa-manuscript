# SPEC — MTGOA Editorial Pipeline
**Type:** Multi-Pass Editorial System + Maturity Model
**Status:** Updated from 6-Face Consult + User Additions
**Date:** 2026-04-21
**Version:** 2.0

---

## What This Is

A seven-pass AI editorial pipeline for the MTGOA manuscript, organized around a **section-level maturity model**. Not a single LLM reviewing the whole book — a pipeline of specialized passes, each with a specific framework grounding, a defined job, and a structured output. Plus a human felt-sense gate that runs before any LLM pass, and a version control system that makes every change auditable.

Modeled on: PAT (Paper Analysis Tool)[^1] + bars-engine EDITORIAL_PASS_1[^2] + editorial best practices[^3]

---

## The Maturity Model

**Core insight:** The book isn't a monolith. Each of the 9 chapters has 7 sections. That's 63 atomic units, each with its own maturity level. We raise the maturity of each section independently, then verify that the raised quality connects into a coherent whole.

### Maturity Levels

| Level | Label | Definition | Gate |
|-------|-------|-----------|------|
| 0 | **SEED** | Section exists, first words written | None — authors can see raw output |
| 1 | **DRAFT** | Full section, all structural elements present | Pass 1 (Structural Integrity) |
| 2 | **REVISED** | Voice calibrated, developmental issues resolved | Pass 2 + Pass 3 |
| 3 | **POLISHED** | Mechanical issues resolved, EA impact verified | Pass 4 + Pass 5 (EA) |
| 4 | **SOURCE-ALIGNED** | Source citations verified, ICA voice checked | Pass 6 (Sources) + Pass 7 (ICA) |
| 5 | **PUBLICATION** | Passed felt-sense gate, version-locked | Human + Felt-Sense Tracker |

### State Machine

```
SEED → DRAFT → REVISED → POLISHED → SOURCE-ALIGNED → PUBLICATION
                  ↓
              [regression]
```

A section can regress if a later pass introduces new blockers. The pipeline tracks state per section per chapter.

### Tracking Format

```yaml
manuscript:
  version: "2.0.0"
  chapters:
    ch7-sage:
      version: "ch7-sage.v3"
      sections:
        s1_exile:
          maturity: POLISHED
          passes: [P0✓, P1✓, P2✓, P3✓, P4✓, P5✓]
          blockers: 0
          last_updated: "2026-04-21"
        s4_practice:
          maturity: REVISED
          passes: [P0✓, P1✓, P2✓, P3⚠️]
          blockers: 1
          blocker_detail: "Pass 3/Shaman: register mismatch in Returner section"
```

---


## Mode A: Cold Read First

You cold-read the chapter before any automated passes run. Your reading is uninfluenced by machine flags. Then automated passes run. Then convergence.

**Use when:** You want to trust your own eye before delegating to tools.

```
1. Read chapter → write human_notes_chX.yaml
2. Run automated passes
3. Convergence engine produces converged report
```

## Mode B: Automated First

Automated passes run first. Machine flags are surfaced. Then you cold-read. Your reading is informed by what the machine noticed.

**Use when:** You want your reading guided by systematic checks.

```
1. Run automated passes → machine_flags_chX.yaml
2. Read chapter + machine flags → write human_notes_chX.yaml
3. Convergence engine produces converged report
```

## Convergence Engine

When both human and machine tracks have run, the convergence engine produces a unified report.

**Rule:** Human wins on meaning, voice, intent. Machine wins on mechanical consistency.

| Issue type | Who decides | Log entry |
|------------|------------|-----------|
| Passive voice, sentence length, typo | Machine | `source: auto` |
| Voice calibration, emotional register | Human | `source: human` |
| Structural gap, missing section | Human | `source: human` |
| EA label incorrect | Machine | `source: auto` |
| Meaning unclear, intent wrong | Human | `source: human` |

**Conflict rule:** If human and machine flag the same sentence with different conclusions, escalate to "NEEDS DISCUSSION" in the converged report with both positions logged.

---

## The Seven Passes

### Phase 0 — Deterministic Metrics (no LLM)

**Purpose:** Establish objective baseline. Runs once per section, outputs to maturity tracker.

| Metric | What it measures |
|--------|----------------|
| Word count vs section target | Deviation % |
| Passive voice ratio | % of sentences with passive construction |
| Average sentence length | Words per sentence |
| Long-sentence fraction | % of sentences >25 words |
| Hedge-word density | "perhaps", "might", "may", "somewhere" per 1000 words |
| Section structural markers | Presence of Exile/Distortion/Concept/etc. headers |

**Output:** `metrics_phase0.yaml` — structured per section, versioned, diffable.

---

### Pass 1 — Structural Integrity

**Maturity gate:** SEED → DRAFT
**Framework grounding:** Chapter spec (each chapter's SPEC.md)

Does this section do what its spec says it should do?

**Checklist:**
- [ ] Core thesis or face-specific thesis appears in first 10% of section
- [ ] Required subsections present (specific to each section type)
- [ ] Arc-bridge from previous section present (for non-S1 sections)
- [ ] Face-specific structural elements present (e.g., 5 modes in S4, 5 game moves in S6)
- [ ] EA emotion labels present and correctly mapped (for face chapters)
- [ ] Word count within ±20% of section target

**Structured output:**
```yaml
section: ch7-sage.s4_practice
pass: structural_integrity
version: 1
checks:
  - id: ea_labels_present
    status: PASS
    evidence: "Metal/Fear→Excitement, Fire/Anger→Triumph, Earth/Neutral→Peace..."
  - id: five_modes_present
    status: PASS
    modes_found: [Panoramic Seer, Altitude-Switcher, Diagnostician, Liberator, Returner]
  - id: word_count_deviation
    status: WARNING
    actual: 1840
    spec_target_section: 2200
    deviation_pct: -16.4
suggestions:
  - type: EXPAND
    location: "Returner — practice section"
    suggestion: "Returner practice section is underdeveloped relative to other modes (~200 words vs ~350 for others)"
    effort: MED
    impact: HIGH
```

---

### Pass 2 — Voice Calibration

**Maturity gate:** DRAFT → REVISED
**Framework grounding:** `voice-calibration-notes.md`

Does this section sound like Wendell?

**Method:**
1. Extract 2 random 150-word passages from section
2. Score each against calibration markers
3. Flag deviations

**Calibration markers (from voice-calibration-notes.md):**
- Discovery idioms: "Here's what I've noticed," "Here's what's true"
- Labor metaphors: the work, the practice, the path
- Self-deprecation via named parts
- Permission-granters: "You can," "You don't have to"
- Direct second-person address throughout
- "Weird. But literally." as acknowledgment
- Short sentences when arriving at truth

**Structured output:**
```yaml
section: ch7-sage.s4_practice
pass: voice_calibration
version: 1
calibration_score: 0.79  # 0-1
deviations:
  - type: MISSING_DISCOVERY_IDIOM
    location: "Returner — paragraph 3"
    suggestion: "Consider 'Here's what I've noticed' before the descent framing"
  - type: EXCESSIVE_HEDGING
    location: "Altitude-Switcher — paragraph 2"
    evidence: "perhaps, might, could"
    suggestion: "Sage voice uses declarative naming, not soft observation"
```

---

### Pass 3 — Developmental / 3-Face Review

**Maturity gate:** DRAFT → REVISED
**Framework grounding:** Chapter spec + MTGOA AQAL + 6-face mechanics

**Challenger review:**
- Does the section demand something uncomfortable?
- Is there genuine edge, or is it playing safe?
- Shadow named but not dwelt in

**Regent review:**
- Does the move type match the structural slot?
- Is the stage sequence correctly sequenced?
- Does this section earn the next one structurally?

**Shaman review:**
- Does the language carry this altitude's specific mythic energy?
- Does the section feel like it belongs to this face?
- EA labels present and correctly mapped?

**Structured output:**
```yaml
section: ch7-sage.s4_practice
pass: developmental_3face
version: 1
challenger:
  - card: "Returner — shadow version"
    severity: 🟡
    issue: "Returning becomes retreating — this shadow is stated but not felt. Reader can't distinguish it from the practice without more somatic description."
    rule: "Shadow must cost something to the person experiencing it"
regent:
  - card: "Mode sequencing"
    severity: 🟢
    note: "See→Switch→Serve→Release→Return sequence is correctly ordered. Earns the loop."
shaman:
  - card: "Altitude-Switcher register"
    severity: 🟡
    issue: "Uses 'notice' where Teal practice should use 'name' — soft observation vs declarative declaration"
    rule: "Teal practice language is declarative, not observational"
```

---

### Pass 4 — Mechanical Polish

**Maturity gate:** REVISED → POLISHED
**Deterministic (no LLM, auto-applied):**
- Remove double spaces
- Fix three-dot sequences (ellipsis: … not ...)
- Ensure em-dashes consistent (`—` not ` -- `)
- Check for orphaned section headers
- Verify last line matches spec

**LLM-assisted (flag only, human approves):**
- Passive voice flagging (from Phase 0 results)
- Long sentence breakdown (sentences >30 words)
- Repeated word clusters (same adjective 3+ times in 50-word window)

**Auto-apply rule:** All deterministic fixes are auto-applied with diff shown. LLM suggestions require human approval.

---

### Pass 5 — Emotional Alchemy Impact

**Maturity gate:** REVISED → POLISHED
**Framework grounding:** EA ontology + WAVE-Spiral

**Purpose:** Does this section move the reader from one emotional state to another?

This is new — it asks whether the section actually does what the EA labels claim. A section can have correctly labeled modes (Panoramic Seer → Metal/Fear → Excitement) and still fail to move the reader from Fear to Excitement. This pass checks for the actual transport.

**Method:**
1. Identify the section's declared EA signal (e.g., "Panoramic Seer — Metal/Fear → Excitement")
2. Read the section and ask: does the writing actually make the reader feel the Fear-to-Excitement arc, or does it just describe it?
3. Identify any emotional flat spots — sections where the declared transformation doesn't actually occur in the prose

**Checklist:**
- [ ] Opening emotional state established (what does the reader feel on arrival?)
- [ ] The dissatisfaction/signal is felt before the transform
- [ ] The transform is embodied, not just stated
- [ ] The reader is brought to a new emotional state by the end
- [ ] No emotional flat spots (passages that describe transformation without producing it)

**Example flags:**
- "The anxiety, fully felt and recognized as history rather than prophecy, converts into the clean attention" — states the transform but doesn't produce it. The reader is told what happens, not made to feel it.
- "The Panoramic Seer sees all altitudes" — describes the mode but doesn't make the reader feel what it would be like to see all altitudes. No awe, no vertigo, no expansion.

**Structured output:**
```yaml
section: ch7-sage.s4_practice
pass: ea_impact
version: 1
transforms:
  - mode: Panoramic Seer
    declared_signal: Metal/Fear → Excitement
    impact_score: 0.65  # 0-1 — does the prose actually produce excitement?
    flat_spots:
      - location: "Panoramic Seer — paragraph 2"
        issue: "States 'takes in the whole field' but doesn't produce the felt sense of expansion"
        fix: "Add one sentence that makes the reader feel the difference between contracted and expanded perception"
  - mode: Returner
    declared_signal: Water/Sadness → Poignancy
    impact_score: 0.81
    flat_spots: []
```

---

### Pass 6 — Source Alignment

**Maturity gate:** POLISHED → SOURCE-ALIGNED
**Framework grounding:** Source spec (per chapter) + MTGOA source corpus

**Purpose:** Does this section accurately represent and cite the sources it draws on?

**Source spec per chapter:**

Each chapter has a `SOURCES.md` file that specifies:
- Which sources are used in this chapter
- Where in the chapter each source is cited
- What type of citation (direct quote, paraphrase, concept alignment, counter-example)
- What cannot be misrepresented about this source

**Method:**
1. Read the section's source spec
2. Verify each cited source appears correctly
3. Check for misrepresented concepts (e.g., Laloux's Teal is organizational, not individual)
4. Verify Wilber's AQAL is cited accurately (not conflated with Graves or Wade)
5. Check Chou's octalysis framework citations for accuracy

**No new facts rule (BubbleCow):** The agent surfaces what the text already contains about sources. It does not introduce new claims about source material. If the agent finds a claim about a source that seems wrong, it flags it as a potential error, not a correction to apply.

**Structured output:**
```yaml
section: ch7-sage.s5_journey
pass: source_alignment
version: 1
source_citations:
  - source: laloux-reinventing
    citations_found:
      - location: "The Walk — paragraph 4"
        type: concept_alignment
        accurate: true
        note: "'evolutionary purpose' is correctly attributed to Laloux"
      - location: "The Map — paragraph 3"
        type: concept_alignment
        accurate: false  # ⚠️
        issue: "Laloux's concept of 'evolutionary purpose' is attributed to an organizational context, not individual practice. The framing in this paragraph conflates Teal organization-level purpose with Teal individual practice."
        correction: "Either add qualifier: 'In organizational context, Laloux calls this evolutionary purpose — in personal practice, we call it...' OR use a different citation from Wilber's Integral Life Practice for individual-level purpose"
    misrepresented_concepts: []
  - source: wilber-integral-life
    citations_found:
      - location: "The Map — paragraph 2"
        type: paraphrase
        accurate: true
        note: "AQAL quadrants referenced accurately"
```

---

### Pass 7 — ICA Reader Review

**Maturity gate:** POLISHED → SOURCE-ALIGNED
**Framework grounding:** ICA (Imagined Audience Community)

**Purpose:** Does this section work for the intended reader?

**ICA definition:** Before writing, Wendell specifies an ICA — the community of readers this section is designed for. The ICA is not a demographic summary. It is a specific set of reading needs and friction points:

```
ICA for Ch7 Sage:
- Has read Ch1-6 and understands the six faces
- Is a facilitator or coach who uses allyship language with clients
- Has encountered the "sage" archetype before but is skeptical of spiritual bypassing
- Needs to see embodied practice, not just conceptual frame
- Friction point: they've met people who claim to "see all altitudes" and use it to avoid commitment
```

**Method:**
1. Read section with ICA as lens
2. Answer: Does this section serve the ICA's specific needs?
3. Flag: Where will the ICA push back, zone out, or not follow?

**ICA review checklist:**
- [ ] Opens with the ICA's actual problem (not the face's conceptual frame)
- [ ] Respects the ICA's skepticism — doesn't preach
- [ ] Uses language the ICA actually uses (not jargon)
- [ ] Gives the ICA something concrete to practice, not just understand
- [ ] Doesn't assume the ICA knows things they don't (no unexplained references)

**Example flags:**
- "The Sage can see all six altitudes" — ICA reads this as spiritual bypassing. Need more embodied context for what that actually looks like in practice.
- "This is what the Sage knows that nobody else can see" — ICA wants to know *how* they know, not just what they know. The ICA needs method, not just content.

**Structured output:**
```yaml
section: ch7-sage.s3_concept
pass: ica_reader_review
version: 1
ica: ch7-sage-ica-v1
score: 0.71
friction_points:
  - location: "Concept — paragraph 2"
    ica_objection: "Spiritual bypassing"
    cause: "States Sage 'sees all altitudes' without immediately grounding it in bodily practice"
    fix: "Add one sentence: 'This is not about having special vision — it's about having been in enough rooms that you can feel which altitude the conversation is actually happening at.'"
  - location: "Concept — paragraph 5"
    ica_objection: "Intellectual framing"
    cause: "'A meta-view of all the altitudes' is conceptual. ICA needs sensory anchor."
    fix: "Add one sensory moment: what it feels like to be in a meeting and suddenly see that two people are playing Red while the rest of the room is playing Green."
```

---

## The Felt-Sense Tracker

**The gate that makes everything else trustworthy.**

The Shaman face raised this in the consult: the spec is written from the head. Phase 0 metrics are necessary but not sufficient. A section can pass every automated check and still fail to feel like a book.

The Felt-Sense Tracker is the human readability check that runs **before** any automated pass. It is not a pass itself. It is a gate.

### When It Runs

Before the pipeline starts on any chapter, one human reads the chapter cold (no notes, no spec, no tracker) and answers three questions:

1. **Does this chapter feel like itself?** (Could this chapter be mistaken for another chapter? Does the Diplomat sound like the Sage?)
2. **Does this chapter earn its place?** (Having read ch1-6, does ch7 feel like the natural next step?)
3. **Would the ICA keep reading?** (Does something in this chapter make you want to turn the page?)

### The Felt-Sense Tracker Format

```yaml
felt_sense:
  chapter: ch7-sage
  reader: wendell
  date: "2026-04-21"
  reads:
    read_1:
      feel_like_itself: true
      notes: "Sage voice is distinct from Diplomat. The altitude-switching language is native to Teal. Good."
    read_2:
      feel_like_itself: true
      notes: "Shadow games are strong — especially Captain Save-a-Kid. That naming is going to land for facilitators."
  blockers:
    - section: s4_practice
      issue: "Returner section reads thin next to the other four modes. Needs more somatic weight."
      severity: 🟡
  earn_its_place: true
  ica_keeps_reading:
    - section: s6_game
      line: "You can hold Teal inside while your body is in the Red"
      moment: "This is the sentence the reader has been waiting for. It lands."
    - section: s2_distortion
      moment: "The Trauma Olympics is the best shadow writing in the chapter. People will recognize themselves."
```

### Integration with Pipeline

The Felt-Sense Tracker output becomes the **primary editorial input** for Passes 1-3. The pipeline doesn't start from the spec alone — it starts from the reader's felt sense of what needs fixing. The automated passes confirm, deny, or refine the human diagnosis.

**Flow:**
```
Human reads chapter → Felt-Sense Tracker
        ↓
    Pipeline input (human diagnosis)
        ↓
    Pass 1-7 (automated verification/confirmation)
        ↓
    Combined report (human + machine)
        ↓
    Human makes final approval decisions
```

---

## Version Control

**Core principle:** Every pipeline run is versioned. Every change is tracked. No whack-a-mole.

### The Version Model

The manuscript uses semantic versioning at two levels:

**Chapter level:** `ch7-sage.v3` — incremented each time a chapter moves to a new maturity level
**Section level:** `ch7-sage.s4_practice.v2` — incremented each time a section changes

### Change Log Format

```yaml
change_log:
  - chapter: ch7-sage
    timestamp: "2026-04-21T19:45:00Z"
    pipeline_version: "2.0"
    passes_run: [P0, P1, P2, P3, P4, P5]
    changes:
      - section: s4_practice
        change_type: EXPAND
        before_version: "s4_practice.v1"
        after_version: "s4_practice.v2"
        trigger: "Pass 3/Shaman — insufficient somatic weight in Returner"
        before_words: 1240
        after_words: 1480
        delta: +240
      - section: s5_journey
        change_type: SOURCE_CORRECT
        before_version: "s5_journey.v1"
        after_version: "s5_journey.v2"
        trigger: "Pass 6/Source — Laloux organizational framing conflated with individual practice"
        before: "Laloux calls this evolutionary purpose"
        after: "Laloux, in organizational context, calls this evolutionary purpose — in personal practice, Wilber's integral map serves better"
    accepted_suggestions: 7
    rejected_suggestions: 3
    net_quality_delta: POSITIVE
```

### Anti-Whack-A-Mole Rules

1. **No section change without prior run baseline.** Before any edit, document the state you're changing from. If the change breaks something, you need to be able to go back.
2. **Regressions are always visible.** If a later pass causes a regression in a section (maturity drops), it surfaces immediately in the combined report.
3. **Suggestion decisions are logged.** Every flagged issue has one of three outcomes: accepted, rejected, deferred. Deferred items get a trigger condition and a deadline.
4. **Version-locked sections don't change.** Once a section reaches PUBLICATION maturity (level 5), it is version-locked. Any further change requires a new version with explicit reason.

### Branch Model

For significant revisions (re-writing a section, changing the arc-bridge), create a branch:
```
main/
  ch7-sage.v3/  ← current publication-ready state
  ch7-sage.v3-shaman-rewrite/  ← active revision branch
```

Merge only after the revision passes the full pipeline and the felt-sense gate.

---

## Epiphany Bridge Scripting

**Purpose:** Collect transformational stories that demonstrate what the book teaches.

An epiphany bridge is a first-person narrative of a moment when someone moved from one altitude to another — from Red to Orange, from Orange to Green, from Green to Teal. Not a case study. Not a therapeutic disclosure. A *scripted story* — written for maximum clarity, with the emotional arc of the transformation rendered in precise language.

**Why this matters for MTGOA:** The book teaches through narrative, not abstraction. Every chapter has an Exile story, a Distortion story, and Practice sections. The epiphany bridges are the raw material that gets turned into those narratives. They are also the validation mechanism — if an epiphany bridge can't be written for a face, the face's teaching may not be grounded in real transformation.

**Script format:**

```yaml
epiphany_bridge:
  id: eb-ch7-sage-01
  face: sage
  altitude_shift: "Green → Teal"
  duration: "3 minutes"
  
  setup:
    - anchor: "A meeting where the room was playing the wrong game"
    - ica_objection: "We've been talking about this for two hours and getting nowhere"
    - felt_state_before: "Exhausted from trying to solve a Green relational problem with Orange systems thinking"
    
  recognition_moment:
    - trigger: "Someone says 'let's design a process' and I suddenly see — we're treating a Red boundary problem like an Orange design problem"
    - somatic: "The moment of seeing is physical — like stepping back from a painting to see the whole canvas"
    - what_shifts: "I'm in the meeting AND I'm watching myself in the meeting"
    
  altitude_switch:
    - from: Green (pluralistic, relational)
    - to: Teal (integral, meta-view)
    - what_enables: "I name the altitude out loud: 'we're arguing about strategy but this is actually about a line that got crossed'"
    - what_it_costs: "The naming creates a silence. For a moment I worry I've ruined the meeting."
    
  return_moment:
    - what_happens: "The silence breaks. Someone says 'yes.' The conversation shifts. We draw the line."
    - somatic: "Coming back down from Teal to actually do Red work — like landing after a flight"
    
  what_teaches:
    - core_insight: "The Sage's gift is not the seeing. It's the coming back."
    - why_it_matters_for_allyship: "You can't help people from above them. You have to come back to where they are."

  permission_to_share: true
  use_context: "facilitator, public, with attribution"
```

**Integration with pipeline:**
- Pass 1 (Structural) checks: Does the section have an embedded epiphany bridge or a clear invitation to practice?
- Pass 5 (EA Impact) uses: Epiphany bridges as the test case for whether the section produces genuine emotional transport
- Felt-Sense Tracker: If the section lacks any moment of genuine transformation (no bridge, no story, no somatic anchor), flag it

**Collection protocol:**
1. When Wendell has an epiphany moment, he scripts it in the format above
2. The bridge gets stored in `manuscripts/epiphany-bridges/{face}/{id}.yaml`
3. During drafting, bridges are mapped to sections
4. During editing, the section is checked against the bridge it was built from — does the section actually deliver what the bridge promises?

---

## Pipeline Architecture (v2)

```
Chapter draft
    │
    ├─► Human reads cold → Felt-Sense Tracker (gate input)
    │         ↓
    │  felt_sense.yaml (human diagnosis)
    │         ↓
    ├─► Phase 0: Deterministic Metrics
    │         ↓
    ├─► Pass 1: Structural Integrity
    ├─► Pass 2: Voice Calibration
    ├─► Pass 3: Developmental / 3-Face
    ├─► Pass 4: Mechanical Polish
    ├─► Pass 5: EA Impact
    ├─► Pass 6: Source Alignment
    ├─► Pass 7: ICA Reader Review
    │         ↓
    ├─► Combined Editorial Report
    │         ↓
    ├─► Human approves / rejects
    │         ↓
    └─► Change log + version bump
              │
              ▼
        [If mature enough]
              ↓
        PUBLICATION (version-locked)
```

---

## What Still Needs Design Decisions

### Resolved from 6-face consult:
1. ✅ **Felt-sense gate** — Added as primary input before automated passes
2. ✅ **Architecture diagram** — Corrected to show sequential with felt-sense input
3. ✅ **"No new facts" rule** — Incorporated into Pass 6
4. ✅ **Tracker data model** — Defined in maturity model section

### Still open:

1. **Chapter ordering:** Sequential (Ch0→Ch8) allows arc-bridge checks. Parallel allows faster runs. **Recommendation:** Sequential within a chapter's passes; parallel across chapters if running full manuscript.

2. **BLOCKER halt rule:** If a BLOCKER is found, does the pipeline halt for that chapter or continue? **Recommendation:** Continue but flag prominently. Don't halt — sometimes later passes surface information that reframes the BLOCKER.

3. **Felt-Sense Tracker reader:** Who does the cold read? Wendell does all chapters (Ch0-Ch8). The cold read is a first-class editorial input that runs before or after automated passes — order is user preference, both tracks converge.

4. **Epiphany bridge ownership:** Does Wendell write all bridges, or does the pipeline generate candidate bridges from the text? **Recommendation:** Wendell writes his own bridges (authenticity requirement). The pipeline can flag when a section lacks a bridge and needs one, but cannot generate the bridge content.

5. **Source spec ownership:** Who writes the SOURCES.md per chapter? **Recommendation:** This is a new document type — needs a spec template and Wendell authorship, as it requires his judgment about how each source is being used.

6. **Integration with tracker:** When the editorial report is complete, does it auto-update MTGOA_BOOK_WORK_TRACKER.md? **Recommendation:** Yes, but only the maturity level field per section. Full report is a separate file.

---

## Companion Files Required

| File | Status | Purpose |
|------|--------|---------|
| `voice-calibration-notes.md` | ✅ Exists | Voice calibration anchoring |
| `MTGOA_6FACE_CHAPTER_STRUCTURE.md` | ✅ Exists | Template + chapter outline |
| `SPEC.md` per chapter | ✅ Exists | Chapter-specific grounding |
| `chapters/{n}/SOURCES.md` | ⚠️ Needs creation | Source usage spec per chapter |
| `chapters/{n}/ICA.md` | ⚠️ Needs creation | ICA definition per chapter |
| `epiphany-bridges/{face}/{id}.yaml` | ⚠️ Needs creation | Epiphany bridge collection |
| `manuscripts/VERSION_LOG.yaml` | ⚠️ Needs creation | Change log for entire manuscript |
| `manuscripts/MANIFEST.yaml` | ⚠️ Needs creation | Current state of all sections/maturities |

---

## References

[^1]: Bhansali et al., "A Local, Multi-Agent LLM Framework for Objective Manuscript Editing," medRxiv 2026.04.13.26350761. Pipeline: 4 phases, 31 agents, framework-grounded evaluation, 72.4% validated usefulness accuracy.
[^2]: bars-engine EDITORIAL_PASS_1.md — Three-face approach (Challenger, Regent, Shaman), structured output with severity markers (🔴/🟡/🟢).
[^3]: BubbleCow editorial ethics: "track changes" protocol, no new facts rule, source log for AI-assisted edits.---
