# 6-Face Analysis: MTGOA 52-Card Prompt SPEC
## Improvements for Deftness + API-First Development

**Date:** 2026-04-20
**Scope:** Analyzing the SPEC for structural improvements

---

## 🧠 ARCHITECT — Structural Logic

### Current State Assessment
**Strength:** The 9-point verification framework is solid. Clear separation of concerns (design constraints, quality criteria, integration points).

**Gap:** The SPEC describes prompts as text, not as data structures. No machine-readable format specified.

### TAKE:
- The 9-point verification rubric (excellent — keep it)
- The quality criteria are precise and falsifiable (good basis for automation)
- The gate-activation pattern (each prompt has predictable gate associations)

### IMPROVE FOR API-FIRST:

**Current problem:** If we write prompts as prose in TASKS.md, the game engine must parse them to extract:
- Card number
- Domain/season
- Gate pattern
- GM context hooks
- BAR alignment

**API-First solution:** Structure prompts as **JSON schema** from the start.

```json
{
  "card_id": "clubs_07",
  "suit": "Clubs",
  "season": "Fall",
  "domain": "Direct Action",
  "card_number": 7,
  "position_in_sequence": 32,
  "prompt": {
    "title": "The Barrier",
    "primary_question": "What are you avoiding confronting?",
    "secondary_question": "What would change if you moved anyway?"
  },
  "guide_lens": "Challenger (call it out)",
  "gate_risk": ["Victim", "Fear"],
  "emotional_intensity": "high",
  "bar_phases": ["Breakthrough", "Action", "Reflection", "Sustain"],
  "cyclical_depth_layers": 3,
  "gm_worldbuilding_hooks": {
    "geography": "What barrier does the landscape create?",
    "social": "What barrier does power structure create?",
    "history": "What barrier comes from what happened before?",
    "magic": "What barrier is actually a threshold?"
  },
  "replayability_index": 3,
  "tone_category": "honest_courageous"
}
```

**Why this matters:**
- Game engine can fetch prompts programmatically
- GM toolkit can dynamically construct contextualized versions
- Verification can be automated (check required fields, gate distribution, intensity curve)
- Player deck UI can render with all metadata

### RECOMMENDATION:
Rewrite SPEC to define **both**:
1. **Human-readable design guidance** (what makes a good prompt)
2. **Machine-readable structure** (JSON schema for how prompts are stored)

---

## 🏛 REGENT — Elegant Preservation

### Current State Assessment
**Strength:** The verification process preserves quality through checkpoints.

**Gap:** No versioning strategy. If a prompt is revised (Year 1 → Year 2), how is the change tracked? How do we know what changed?

### TAKE:
- The 9-point verification checklist (keeps consistency)
- The integration with BAR phases (ensures practice loop works)

### IMPROVE FOR PRESERVATION:

**Current problem:** If we update a prompt after players use it, we lose the original. No audit trail.

**Solution:** Add versioning metadata to each prompt.

```json
{
  "card_id": "clubs_07",
  "current_version": "2.1",
  "versions": [
    {
      "version": "1.0",
      "created_date": "2026-04-20",
      "created_by": "claude",
      "prompt_text": "What are you avoiding confronting?",
      "status": "approved"
    },
    {
      "version": "1.1",
      "created_date": "2026-05-15",
      "created_by": "wendell",
      "change_reason": "clarified secondary question",
      "prompt_text": "What are you avoiding confronting? (What would change if you moved anyway?)",
      "status": "approved"
    }
  ],
  "stability": "stable", // stable | experimental | deprecated
  "locked": false // if true, can't be changed without special approval
}
```

**Why this matters:**
- Players using Year 1 cards see original version
- Year 2 players might use refined version
- We can track what worked and what needed revision
- Supports iterative improvement without losing history

### RECOMMENDATION:
Add "Versioning & Stability" section to SPEC. Define when prompts are locked vs editable.

---

## ⚔️ CHALLENGER — Critical Edge

### Current State Assessment
**Strength:** The 9-point verification is skeptical and falsifiable.

**Gap:** Verification is manual. No automated way to check that all 9 points pass. Humans will miss things.

### TAKE:
- The skepticism about prompt quality (force every prompt to prove itself)
- The gate-activation test (forces prompts to be psychologically sound)

### IMPROVE FOR DEFTNESS:

**Current problem:** After writing 52 prompts, running 9-point verification on each = 468 manual checks. Prone to fatigue, inconsistency.

**Solution:** Automate the parts that can be automated, require human judgment only where needed.

```
AUTOMATED CHECKS (code can verify):
✓ Card_id format is valid (clubs_07, hearts_13, etc.)
✓ All 52 cards present (no gaps)
✓ Gate distribution is balanced (each gate represented 4-6 times)
✓ BAR phases all present in prompt structure
✓ Intensity curve goes: Spring mild → Summer medium → Fall high → Winter reflective
✓ No prompts are below X word count (minimum readability)
✓ No prompts exceed Y word count (maximum clarity)
✓ All 9 metadata fields present per prompt

HUMAN JUDGMENT CHECKS (require review):
✓ Clarity (does this make sense to a first reader?)
✓ Actionability (does this invite real action?)
✓ Emotional tone (does intensity match season?)
✓ Gate resonance (does this activate the right pattern?)
✓ Contextuality (can GM enhance this with worldbuilding?)
✓ Cyclical depth (will this deepen on replay?)
✓ Replayability (3+ legitimate answers?)
```

**Why this matters:**
- Reduces verification burden by ~60%
- Catches structural errors early (before human review)
- Humans focus on the subtle stuff (emotional tone, gate resonance)
- Build the verification script once, run it on every prompt automatically

### RECOMMENDATION:
Add section: "Automated Verification Pipeline." Define which checks are code-based, which require human judgment.

---

## 🎭 DIPLOMAT — Bridge & Harmonize

### Current State Assessment
**Strength:** SPEC acknowledges GM toolkit integration. But disconnection between player experience and GM experience.

**Gap:** The prompts are designed for players. How do GMs access them? What's the UX?

### TAKE:
- The worldbuilding hooks (Geography/Social/History/Magic)
- The integration example showing how GM enhances prompts

### IMPROVE FOR BRIDGE:

**Current problem:** SPEC says "GM can contextualize," but doesn't show HOW in the game engine.

**Solution:** Define the **GM Interface Contract** — what data structure the GM needs to SEE.

```
Player Interface (sees):
- Card front: [Title] [Primary Question]
- Card back: [BAR template]

GM Interface (sees):
- Prompt metadata: [card_id, domain, season, gates]
- Contextualization templates: [Geography hook, Social hook, History hook, Magic hook]
- Player context: [Does this player struggle with this gate? Show previous year's answer]
- Facilitation guide: [How to ask this question in a group? What to watch for?]

EXAMPLE:
Player draws "7 of Clubs"
GM sees:
  - Base prompt: "What barrier are you avoiding?"
  - Geography context: "What does the landscape make difficult?"
  - Social context: "Who could be hurt if you moved?"
  - History context: "What failure are you protecting against?"
  - Magic context: "What threshold are you standing in front of?"
  - Facilitation: "This activates Fear/Victim gates. Watch for shutdown or storytelling. Offer: 'What would it take to move?'"
```

**Why this matters:**
- GMs understand how to enhance each prompt
- Bridging is intentional, not accidental
- Creates shared language between player deck and GM toolkit
- Player and GM experience is designed together, not separately

### RECOMMENDATION:
Add section: "Player Interface + GM Interface Contract." Define what each sees and how they work together.

---

## 🌊 SHAMAN — Shadow & Metaphysics

### Current State Assessment
**Strength:** SPEC recognizes that prompts activate gates. But treats gates as mechanics, not as shadow work.

**Gap:** The shadow work is implicit. The prompts should explicitly invite the shadow, not hide it.

### TAKE:
- Gate activation (each prompt has a shadow pattern)
- The replayability insight (deeper each cycle)

### IMPROVE FOR SHADOW:

**Current problem:** A prompt like "What barrier are you avoiding?" activates Victim gate, but doesn't name it. The player might not recognize the pattern.

**Solution:** Add **Shadow Prompt Variations** — multiple versions for different years/depths.

```json
{
  "card_id": "clubs_07",
  "prompt_variations": {
    "year_1_surface": {
      "title": "The Barrier",
      "primary": "What are you avoiding confronting?",
      "secondary": "What would change if you moved anyway?",
      "gate_target": ["Victim", "Fear"],
      "depth": "surface"
    },
    "year_2_shadow": {
      "title": "The Barrier",
      "primary": "What part of you feels powerless here? What's it protecting?",
      "secondary": "What would it mean to acknowledge that powerlessness instead of avoiding it?",
      "gate_target": ["Victim"],
      "depth": "shadow",
      "note": "Year 2: invite the Victim to speak"
    },
    "year_3_gift": {
      "title": "The Barrier",
      "primary": "What has your avoidance taught you? What's the wisdom in that protection?",
      "secondary": "How could that protection become a resource?",
      "gate_target": ["Victim"],
      "depth": "gift",
      "note": "Year 3: transform the shadow into strength"
    }
  }
}
```

**Why this matters:**
- Explicitly supports cyclical deepening (not just "harder questions")
- Shadow work is intentional and named
- Players understand the transformation arc
- Supports 3-2-1 shadow process (I do it → I see it → I integrate it)

### RECOMMENDATION:
Add section: "Prompt Variations by Cycle." Define year_1 (surface), year_2 (shadow), year_3+ (gift) versions of each prompt.

---

## 📖 SAGE — Timeless Principle

### Current State Assessment
**Strength:** SPEC acknowledges that prompts need to work across multiple cycles.

**Gap:** No guidance on what "deepening" actually means. How do you know if a prompt supports deepening?

### TAKE:
- Cyclical replay (same prompt, deeper understanding each year)
- The principle that practice changes you

### IMPROVE FOR WISDOM:

**Current problem:** How do we design for deepening without being prescriptive about what the player learns?

**Solution:** Define **Deepening Principles** — what makes a prompt support continued learning.

A prompt supports deepening if:

1. **It can be answered multiple ways** (Year 1: "I avoid confronting my boss." Year 2: "I avoid confronting my own compliance." Year 3: "I avoid confronting what my avoidance costs the movement.")

2. **The answer informs the next cycle** (This year's barrier becomes next year's focus)

3. **It reveals layers** (First answer: external barrier. Second answer: internal barrier. Third answer: systemic barrier.)

4. **It stays relevant** (Same question, different context each year. Player grows into the question.)

Example deepening arc for "What barrier are you avoiding?":

```
YEAR 1: External barrier recognition
"I'm avoiding confronting my workplace's culture."
→ BAR: I noticed, I spoke up, people got defensive, I'll keep trying

YEAR 2: Internal barrier exploration
"I'm avoiding confronting how my Victim gate makes me collapse when challenged."
→ BAR: I recognized the pattern, I sat with the discomfort, I found my ground, I practice standing

YEAR 3: Systemic/relational barrier
"I'm avoiding confronting how my avoidance is replicating the system I'm trying to change."
→ BAR: I named the contradiction, I changed my approach, the movement shifted, I hold this tension
```

**Why this matters:**
- Prompts don't need to change year to year (same 52 cards)
- But player's understanding deepens
- Supports long-term practice (not one-time insight)
- Aligns with "mastery through repetition" principle

### RECOMMENDATION:
Add section: "Deepening Principles." Define what makes a prompt support cyclical learning, not repetition.

---

## Summary: Improvements Across 6 Faces

| Face | Current Gap | Recommended Improvement | Effort |
|------|---|---|---|
| **Architect** | Text-only prompts, not machine-readable | Define JSON schema for prompts | Medium |
| **Regent** | No versioning/audit trail | Add versioning metadata | Low |
| **Challenger** | Manual 9-point verification (468 checks) | Automate what's automatable | High |
| **Diplomat** | Player/GM disconnection | Define interface contract | Medium |
| **Shaman** | Shadow implicit, not explicit | Add year_1/year_2/year_3 prompt variations | High |
| **Sage** | Deepening undefined | Define deepening principles | Medium |

---

## Prioritized Implementation

### Phase 1 (Essential for API-first)
1. **Architect: JSON schema** — Can't code the game engine without this
2. **Diplomat: Interface contract** — Needed for player + GM UX alignment

### Phase 2 (Essential for quality)
3. **Challenger: Automated verification** — Reduces human error, catches issues early
4. **Regent: Versioning** — Supports iteration without losing history

### Phase 3 (Essential for depth)
5. **Shaman: Prompt variations** — Supports cyclical deepening
6. **Sage: Deepening principles** — Documents what deepening looks like

---

## Revised SPEC Writing

The SPEC should be restructured to include:

**Current sections (keep):**
- Metadata
- Core design principle
- Card prompt structure
- Quality criteria (9-point)
- Design constraints
- Integration with other systems

**New sections (add):**
- **JSON Schema Definition** (machine-readable structure for all 52 prompts)
- **Versioning & Stability Strategy** (how prompts evolve, how history is preserved)
- **Automated Verification Pipeline** (what checks are code-based, what require human judgment)
- **Player + GM Interface Contract** (what each sees, how they work together)
- **Prompt Variations by Cycle** (year_1/year_2/year_3 versions of each prompt)
- **Deepening Principles** (what makes a prompt support cyclical learning)

---

**Status:** 6-Face analysis complete. Recommended revisions prioritized.
**Next step:** Revise SPEC to incorporate these improvements, or proceed to PLAN phase with current SPEC and plan these as Phase 2?

