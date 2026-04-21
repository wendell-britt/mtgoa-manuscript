# PLAN.md — MTGOA 52-Card Prompt Design
## *Strategy for Designing 52 Cyclical, Deepening, Allyship Prompts*

**Created:** 2026-04-20
**Status:** PLAN DRAFT
**Scope:** Design approach, templates, sequencing logic, integration strategy

---

## Overview: The Design Approach

We are designing **52 prompts organized in a 4-domain × 13-card structure**, sequenced by temporal phase (Spring → Summer → Fall → Winter) and designed to deepen across multiple years.

**Core constraint:** The same 52 prompts must work for Year 1, Year 2, and Year 3+ with different versions (surface → shadow → gift).

**This PLAN defines:**
1. How each domain's 13 prompts build sequence
2. Templates for prompts in each season
3. How GM worldbuilding enhances each prompt
4. Gate distribution strategy
5. Quality checkpoints during design

---

## Part 1: Domain Sequencing Strategy

### SPRING / GATHERING RESOURCES (Hearts 1-13)
**Phase:** Wake Up | **Tone:** Establishing, recognizing, grounding

**Purpose:** Player recognizes what exists (resources, allies, capacities, knowledge).

**Emotional arc within domain:**
- Cards 1-4: Recognition (what exists?)
- Cards 5-9: Grounding (how do I know this matters?)
- Cards 10-13: Action commitment (what will I do with this?)

**Prompt types in this domain:**
1. Abundance recognition (what do you have?)
2. Scarcity naming (what's missing?)
3. Ally identification (who supports you?)
4. Resource mapping (what can you access?)
5. Knowledge claiming (what do you know?)
6. Capacity recognition (what are you capable of?)
7. Story centering (whose story needs to be centered?)
8. Power mapping (where is power?)
9. Hidden asset discovery (what haven't you counted?)
10. Teaching relationships (who taught you?)
11. Material base (what's your foundation?)
12. Gathering week (what can you gather?)
13. Emergence (what springs forth when you rest?)

**Gate activation pattern:** Protector (resource anxiety), Skeptic (doubt about worth)

---

### SUMMER / SKILLFUL ORGANIZING (Diamonds 14-26)
**Phase:** Grow Up | **Tone:** Connective, collaborative, emerging

**Purpose:** Player builds systems, repairs relationships, processes tensions.

**Emotional arc within domain:**
- Cards 14-17: System recognition (what's in place?)
- Cards 18-22: Tension surfacing (what's stuck?)
- Cards 23-26: Coordination deepening (how do we move together?)

**Prompt types in this domain:**
1. Communication breakdown (where is it happening?)
2. System need (what structure would help?)
3. Relationship repair (what needs care?)
4. Power sharing (how do we share power?)
5. Tension naming (what's beneath the surface?)
6. Conversation needed (who needs to talk?)
7. Structure enabling (what enables movement?)
8. Decision-making (how do we decide together?)
9. Relational cost (what has this cost?)
10. Emergence observation (what's growing?)
11. Progress celebration (what's working?)
12. Coordination next (what's the next level?)
13. Sustaining (how do we stay together?)

**Gate activation pattern:** Controller (managing complexity), Victim (feeling powerless in systems)

---

### FALL / DIRECT ACTION (Clubs 27-39)
**Phase:** Show Up | **Tone:** Honest, courageous, necessary discomfort

**Purpose:** Player confronts barriers, moves despite fear, witnesses failure.

**Emotional arc within domain:**
- Cards 27-31: Barrier naming (what are we avoiding?)
- Cards 32-36: Fear surfacing (what would it take?)
- Cards 37-39: Action integration (how do we move?)

**Prompt types in this domain:**
1. Avoidance naming (what barrier are you avoiding?)
2. Change possibility (what would shift?)
3. Grief naming (what are you grieving?)
4. Anger direction (where is your anger pointing?)
5. Real cost (what's the cost of inaction?)
6. Dependency (who's depending on you?)
7. Small action (what can you do?)
8. Shadow work (what's the shadow here?)
9. Body wisdom (what does your body want?)
10. Stakes clarity (what's at stake?)
11. Bravery question (what would it take?)
12. Resistance meeting (what are you facing?)
13. Broken honoring (how do you honor what's broken?)

**Gate activation pattern:** Fear, Victim, Damaged Self (all shadow gates activated)

---

### WINTER / RAISING AWARENESS (Spades 40-52)
**Phase:** Clean Up | **Tone:** Generous, teaching, integrated wisdom

**Purpose:** Player reflects, teaches, integrates, prepares for renewal.

**Emotional arc within domain:**
- Cards 40-44: Learning reflection (what did you discover?)
- Cards 45-48: Teaching preparation (who needs to know?)
- Cards 49-52: Integration & renewal (what now?)

**Prompt types in this domain:**
1. Season teaching (what did this teach?)
2. Teaching recipient (who needs to hear?)
3. Compost work (what are you composting?)
4. Forward passing (how will you pass this on?)
5. Surprise discovery (what surprised you?)
6. Strength finding (where did you find strength?)
7. Grief honoring (what do you grieve?)
8. Gratitude (what are you grateful for?)
9. World impact (how did the world change because you moved?)
10. Next cycle planning (what will you do differently?)
11. Mentoring (who will you mentor?)
12. Legacy (what's your legacy?)
13. Rest (how do you rest now?)

**Gate activation pattern:** Vulnerable Child (telling truth), Fixer (learning from failure)

---

## Part 2: Prompt Template Structure

### Universal Prompt Template

Every prompt follows this JSON structure:

```json
{
  "card_id": "[suit]_[number]",
  "metadata": {
    "suit": "[Clubs|Hearts|Spades|Diamonds]",
    "season": "[Spring|Summer|Fall|Winter]",
    "domain": "[Gathering|Organizing|Action|Awareness]",
    "card_number": [1-13],
    "position_in_sequence": [1-52],
    "phase": "[Wake Up|Grow Up|Show Up|Clean Up]"
  },
  "prompt": {
    "title": "[1-3 words, evocative]",
    "primary_question": "[1-2 sentences, clear action]",
    "secondary_question": "[1-2 sentences, deepening]",
    "guide_lens": "[Which guide illuminates this?]",
    "gate_risk": "[1-2 gates that might activate]",
    "word_count": [number]
  },
  "design_properties": {
    "emotional_intensity": [1-5],
    "bar_phases": ["Breakthrough", "Action", "Reflection", "Sustain"],
    "cyclical_depth_layers": 3,
    "replayability_index": [1-3],
    "tone_category": "[matching domain + season]"
  },
  "gm_worldbuilding_hooks": {
    "geography": "[How geography context enhances this]",
    "social": "[How social context enhances this]",
    "history": "[How historical context enhances this]",
    "magic": "[How mystery/possibility enhances this]"
  },
  "prompt_variations": {
    "year_1_surface": { ... },
    "year_2_shadow": { ... },
    "year_3_gift": { ... }
  }
}
```

### Tone Categories by Domain

**GATHERING (Spring / Hearts):** curious, establishing, grounded, clear
**ORGANIZING (Summer / Diamonds):** connective, collaborative, collaborative, emerging
**ACTION (Fall / Clubs):** honest, courageous, discomfort-embracing, direct
**AWARENESS (Winter / Spades):** generous, teaching, reflective, integrated

---

## Part 3: Sequencing Logic Within Each Domain

### How 13 Cards Build in Each Domain

**Pattern A: Recognition → Deepening → Commitment**

1-4: **Recognition** (notice/establish/name)
5-9: **Deepening** (process/understand/integrate)
10-13: **Commitment** (action/teaching/next step)

**Applied to GATHERING (Hearts 1-13):**
```
1-4 RECOGNITION:
  1. What abundance are you carrying?
  2. Name one scarcity you face
  3. Who are your 3 key allies?
  4. What resources do you have access to?

5-9 DEEPENING:
  5. What's your energy level right now?
  6. What knowledge do you bring?
  7. What story needs centering?
  8. Where is power concentrated?
  9. What's available that you haven't noticed?

10-13 COMMITMENT:
  10. Who are the hidden allies?
  11. What's your material base?
  12. What can you gather this week?
  13. What springs forth when you rest?
```

**Applied to ORGANIZING (Diamonds 14-26):**
```
14-17 RECOGNITION:
  14. Where are communication breakdowns?
  15. What system would help coordinate this?
  16. Name one relationship that needs repair
  17. How do you share power?

18-22 DEEPENING:
  18. What tensions are beneath the surface?
  19. Who needs to be in conversation?
  20. What structure enables this work?
  21. How do you make decisions together?
  22. What's the relational cost so far?

23-26 COMMITMENT:
  23. Where is emergence happening?
  24. What's growing that wasn't planned?
  25. How do you celebrate progress?
  26. What's the next level of coordination?
```

**Applied to ACTION (Clubs 27-39):**
```
27-31 BARRIER NAMING:
  27. What barrier are you avoiding?
  28. What would change if you moved anyway?
  29. What failure are you grieving?
  30. Where is your anger pointing?
  31. What's the real cost of inaction?

32-36 FEAR SURFACING:
  32. Who's depending on you to move?
  33. What small action can you take?
  34. What's the shadow in this action?
  35. How does your body want to move?
  36. What's at stake?

37-39 ACTION INTEGRATION:
  37. What would it take to be brave?
  38. What resistance are you meeting?
  39. How do you honor what's broken?
```

**Applied to AWARENESS (Spades 40-52):**
```
40-44 LEARNING REFLECTION:
  40. What did this season teach you?
  41. Who needs to hear what you've learned?
  42. What are you composting?
  43. How will you pass this forward?
  44. What surprised you?

45-48 TEACHING PREPARATION:
  45. Where did you find unexpected strength?
  46. What do you grieve?
  47. What are you grateful for?
  48. How has the world changed because you moved?

49-52 INTEGRATION & RENEWAL:
  49. What will you do differently next cycle?
  50. Who will you mentor?
  51. What's your legacy from this work?
  52. How do you rest now?
```

---

## Part 4: Gate Distribution Strategy

### 8 Gates Across 52 Prompts

Target: Each gate represented 4-6 times, balanced across domains.

```
Protector:        5 times (primarily Spring/Gathering)
Skeptic:          5 times (primarily Spring/Gathering)
Controller:       5 times (primarily Summer/Organizing)
Victim:           8 times (distributed: Summer, Fall, Winter)
Fear:             5 times (primarily Fall/Action)
Damaged Self:     5 times (primarily Fall/Action)
Fixer:            5 times (primarily Winter/Awareness)
Vulnerable Child: 4 times (primarily Winter/Awareness)

TOTAL: 52
```

**Distribution logic:**
- **Spring (Hearts 1-13):** Protector (4x), Skeptic (5x), Controller (2x), Victim (2x)
- **Summer (Diamonds 14-26):** Controller (4x), Victim (3x), Skeptic (2x), Fixer (2x), Protector (1x)
- **Fall (Clubs 27-39):** Victim (3x), Fear (5x), Damaged Self (5x)
- **Winter (Spades 40-52):** Vulnerable Child (4x), Fixer (3x), Victim (2x), Protector (2x), Controller (1x)

---

## Part 5: GM Contextualization Strategy

### Four Worldbuilding Hooks Per Prompt

Every prompt has 4 enhancement options using Foundations' worldbuilding domains:

**Template for GM Contextual Hooks:**

For a prompt like "What barrier are you avoiding confronting?":

```
IF GM EMPHASIZES GEOGRAPHY:
  "What does the physical landscape make difficult?"
  "How far do people have to travel to take action?"
  (GM is highlighting: terrain, logistics, resources, scale)

IF GM EMPHASIZES SOCIAL:
  "Who could be retaliated against if you moved?"
  "What does the power structure make dangerous?"
  (GM is highlighting: power, relationships, risk, culture)

IF GM EMPHASIZES HISTORY:
  "What failure are you protecting against from what happened before?"
  "What precedent are you breaking?"
  (GM is highlighting: patterns, trauma, learning, precedent)

IF GM EMPHASIZES MAGIC:
  "What threshold are you standing in front of?"
  "What's waiting on the other side of this fear?"
  (GM is highlighting: possibility, transcendence, hidden resources, transformation)
```

Each hook should:
- Reference the base prompt (not replace it)
- Add 1-2 sentences of context
- Point to a specific worldbuilding domain
- Invite deeper inquiry specific to that world

---

## Part 6: Prompt Variations by Cycle

### Year 1, Year 2, Year 3+ Strategy

Each prompt has 3 variations to support deepening across cycles.

**Variation depths:**

```
YEAR 1 (Surface):
- External focus (what's happening out there?)
- Recognition task (name it, notice it)
- Gentle intensity (foundational)
- Expected answer type: observable, concrete

YEAR 2 (Shadow):
- Internal focus (what's happening in you?)
- Pattern recognition (what's your protective move?)
- Medium intensity (inviting deeper self-knowledge)
- Expected answer type: self-awareness, pattern naming

YEAR 3+ (Gift):
- Integration focus (how is this a strength?)
- Wisdom extraction (what did this teach you?)
- Higher intensity (transformation, responsibility)
- Expected answer type: integrated understanding, resource creation
```

**Example progression:**

```
BASE PROMPT: "What barrier are you avoiding confronting?"

YEAR 1 (Surface):
  Question: "What are you avoiding confronting?"
  Context: "Name the external barrier. What's in the way?"
  Answer type: External obstacle (racism, policy, logistics)

YEAR 2 (Shadow):
  Question: "What part of you feels powerless here? What's it protecting?"
  Context: "Go inward. What pattern does this activate? What's the protective strategy?"
  Answer type: Internal pattern (Victim gate, helplessness, self-doubt)

YEAR 3+ (Gift):
  Question: "What has your avoidance taught you? What wisdom is in that protection?"
  Context: "Integration. What has this pattern given you? What's the gift?"
  Answer type: Integrated resource (care, listening, discernment)
```

---

## Part 7: Quality Assurance Checkpoints

### Per-Prompt Design Checklist

As each prompt is designed, verify:

```
□ CLARITY: Can a first reader understand this on first read?
  (If no: revise for simplicity)

□ ACTIONABILITY: Does this invite observable action/naming?
  (If no: add "What would you do/say?")

□ INTENSITY MATCH: Does emotional intensity match season?
  (If no: adjust language or move prompt)

□ GATE ACTIVATION: Does this activate the target gate(s)?
  (If no: reframe to reveal the protective pattern)

□ CONTEXTUALITY: Can GM enhance with worldbuilding?
  (If no: add "what would __ context change about this?")

□ CYCLICAL DEPTH: Have you designed year_1/year_2/year_3 versions?
  (If no: work backwards from gift to shadow to surface)

□ BAR ALIGNMENT: Does prompt naturally generate B→A→R→S?
  (If no: revise to invite observable action)

□ REPLAYABILITY: Can this be answered 3+ different ways?
  (If no: make it more open-ended)

□ TONE CONSISTENCY: Does prompt match domain + season voice?
  (If no: align with domain voice guide)
```

### Full-Deck Verification (After all 52 written)

```
□ DISTRIBUTION: Each gate 4-6x? All domains 13 cards? All seasons 13?
□ INTENSITY CURVE: Spring < Summer < Fall > Winter pattern?
□ VOICE: Do all 52 prompts sound like they're from the same book?
□ SEQUENCE: Do cards within each domain build logically?
□ GATE COVERAGE: All 8 gates represented and balanced?
□ DEPTH SUPPORT: Every prompt has year_1/year_2/year_3 versions?
□ BAR STRUCTURE: Do prompts invite all 4 phases?
```

---

## Part 8: Design Workflow

### Step-by-Step Process

**Phase 1: Domain Planning**
1. Review domain sequence strategy (Part 1)
2. Sketch the 13-card arc for each domain (Recognition → Deepening → Commitment)
3. Identify gate activation targets for each prompt
4. Plan intensity curve (intensity 1-5 across 13 cards)

**Phase 2: Prompt Writing**
1. Write primary question (1-2 sentences, clear action)
2. Write secondary question (1-2 sentences, deepening)
3. Identify guide lens (which guide illuminates this?)
4. Name gate risks (which gates might activate?)
5. Design 3 variations (year_1_surface, year_2_shadow, year_3_gift)
6. Write 4 GM contextual hooks (geography, social, history, magic)

**Phase 3: Quality Review**
1. Per-prompt checklist (verify 9 criteria)
2. Per-domain review (do 13 cards build well?)
3. Full-deck review (distribution, intensity, voice, gate coverage)

**Phase 4: Finalization**
1. Compile all 52 into JSON structure
2. Run automated verification (structural, distribution, intensity checks)
3. Final human review (clarity, tone, replayability)
4. Approval and lock (ready for TASKS phase)

---

## Part 9: Success Criteria

By the end of PLAN phase, we should have:

✅ Clear design approach for each domain (Recognition → Deepening → Commitment)
✅ Prompt templates in JSON structure (reusable format)
✅ Gate distribution strategy (balanced across 52 cards)
✅ GM contextualization patterns (how each prompt enhances with worldbuilding)
✅ Cyclical variation strategy (year_1/year_2/year_3 patterns defined)
✅ Quality checkpoints defined (verification at per-prompt and full-deck level)
✅ Workflow documented (steps from design to finalization)

---

## Part 10: Open Design Questions

Before proceeding to TASKS, we should clarify:

1. **Guide Lens Attribution:** For each prompt, which of the 6 guides illuminates it? Should this vary across the domain, or should each domain have a primary guide?
   - Example: Should all Gathering prompts use Sage's lens, or mix all 6 guides?

2. **Emotional Channels:** Should prompts explicitly reference the 5 emotional channels (Fear, Sadness, Anger, Joy, Shame)? Should each prompt activate one primary channel?
   - Example: Fall/Action prompts might primarily activate Anger channel

3. **Player Context Integration:** When a player replays a card in Year 2, should they see their Year 1 answer? Should GM have access to it?
   - Example: GM shows "Last year you said ___, what's different now?"

4. **Facilitation Guidance:** How detailed should the "Facilitation Notes" be for GMs? Should we include:
   - What to watch for (shutdown, overwhelm, intellectualizing)?
   - What to offer if stuck ("What would it take to...?")?
   - Group facilitation options ("Who in this room has faced...?")?

---

**Status:** PLAN DRAFT — Ready for user input on open questions
**Next:** Clarify design questions, then proceed to TASKS phase

