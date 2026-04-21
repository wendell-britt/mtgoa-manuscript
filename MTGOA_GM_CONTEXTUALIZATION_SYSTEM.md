# MTGOA GM Contextualization System
## Regent & Architect: Campaign Flavor Layers on the Inherited BARs-Engine World

**Status**: Design (ready for implementation)
**Created**: 2026-04-20
**Revised**: 2026-04-20 (Inheritance Model)
**Leadership**: Regent (campaign structure) + Architect (system integration)
**Purpose**: Enable deft campaign creation by adding flavor layers to the inherited BARs-engine world

---

## Core Principle

The BARs-engine world is already complete. It has:
- **Magic**: Emotional Alchemy (5 channels, nations, vibeulons) — LOCKED
- **Politics**: 5 Nations (Argyra, Pyrakanth, Lamenth, Meridia, Virelune) — LOCKED
- **Geography**: Spatial instances (Bruised Banana → MTGOA Org → Chapters) — LOCKED
- **Personal Throughput**: 4 Moves (Wake Up, Clean Up, Grow Up, Show Up) — LOCKED

GMs don't define worlds from scratch. They **add flavor layers** to this inherited world:
- Which allyship domains does this campaign emphasize?
- What's the spatial tone and appearance?
- Which nation's culture is strongest here?
- (Optional) What real-world context flavors the game experience?

**Guiding Philosophy** (from Lazy Dungeon Master's Guide): *"Prepare only what most benefits your game."*

Setup is **15–20 minutes** (not 30):
- 2 required questions: scope + spatial flavor
- 2 optional questions: nation choice + real-world context

**Result**: Identical prompts feel grounded in each campaign, with shared world properties flowing down from Bruised Banana through MTGOA through Chapter, creating coherent nested campaigns.

```
Prompt: "What resources do you have?"

Inherited Properties (from world):
  Magic: Water channel (sadness/depth)
  Politics: Can involve any nation (Lamenth, Meridia, etc.)
  Moves: Wake Up → Clean Up → Grow Up → Show Up
  Geography: Chapter 1 clearing (spatial instance)

Coastal Campaign adds:
  Spatial tone: "Three springs by the shore"
  Nation flavor: Lamenth (water, depth, memory)
  Domain focus: Gathering Resources + Raising Awareness
  Real context: Players are community dealing with water scarcity
  Game tone: Springs are sacred, spirits guard wells, merchants control trade

  → Quest: "Inventory your coastal survival resources"
    - Inherits emotional alchemy + 4 moves
    - Customized with spatial flavor + real context
    - Players navigate both inherited world's politics AND campaign's specific tone

Mountain Campaign adds:
  Spatial tone: "Deep forests and mineral slopes"
  Nation flavor: Argyra (metal, discernment, clarity)
  Domain focus: Skillful Organizing + Direct Action
  Real context: Players are organizing land stewardship
  Game tone: Elders carry knowledge, boundaries are clear, strategy matters

  → Quest: "Inventory your mountain legacy resources"
    - Inherits emotional alchemy + 4 moves (same as coastal)
    - Customized with different spatial flavor + different real context
    - Players navigate inherited world's 5 nations + campaign's specific focus

Same prompt. Same emotional channel. Same 4 moves. INHERITED WORLD.
Different flavor layers. Different felt experiences.
Player can translate discoveries back: "If I can claim the brackish springs (coastal) or mineral rights (mountain) in this campaign, what do I actually claim in our work?"
```

---

## 1. Campaign Configuration Layer

### 1.1 What GMs Define (Campaign Onboarding — 15–20 Minutes)

When a GM creates a new Allyship Campaign, they answer **4 questions**: 2 required + 2 optional.

GMs inherit the world's magic system, politics, moves, and spatial structure. They customize flavor layers on top.

**Time investment**: Required questions (10 min) + optional questions (5–10 min). GMs should define only the minimum needed to feel grounded. Additional detail emerges through play.

```
REQUIRED (10 minutes)

1. Campaign Scope (3 min)
   - Campaign name
   - Chapter (1-12 of MTGOA book)
   - Allyship domain focus (1-4 domains: Gathering Resources, Skillful Organizing, Direct Action, Raising Awareness)
   - Year focus (Year 1 surface-level or Year 2+ shadow work)

2. Spatial Flavor (7 min)
   - How does this chapter's clearing LOOK and FEEL?
     Example: "Coastal island with three springs—one fresh, two brackish. Tidal flats. Weathered fishing huts."
   - Which NPCs are present? (Choose 1-3 of 6 Game Master faces: Sage, Diplomat, Challenger, Shaman, Regent, Architect)
   - Which nation's culture is strongest here? (Argyra/Metal, Pyrakanth/Fire, Lamenth/Water, Meridia/Earth, or Virelune/Wood)
   - Tone: (urgent / celebratory / quiet / confrontational / exploratory)

OPTIONAL (5-10 minutes)

3. Real-World Context (5 min)
   - What actual allyship work are players doing in their real community?
     Example: "We're dealing with water access scarcity and community resilience."
   - How does this frame the campaign's urgency?

4. Game-World Flavor (5 min)
   - How does the real-world work TRANSLATE to game-world mythology?
     Example: "Springs are sacred. Spirits guard the wells. Getting water requires asking rightly, which means naming what we lack."
   - What metaphor bridges real → imagined?

CAMPAIGN PACING (Derived)
- Inherited: 4 Moves (Wake Up → Clean Up → Grow Up → Show Up)
- Inherited: Emotional Alchemy (5 channels, WAVE progression)
- Inherited: 5 Nations (political ecosystem)
- Inherited: 13-card sequences for selected domains
- Customized: Which year's arc (Year 1 surface / Year 2 shadow / Year 3 gift)
- Customized: Cycling (do players return to same prompts?)
```

### 1.2 Storage Structure

```json
{
  "campaign_id": "mtgoa-chapter-1-coastal",
  "campaign_name": "The Gathering at the Shore",
  "chapter": 1,

  "inherited_world": {
    "magic_system": "emotional_alchemy",
    "magic_description": "5 channels (Metal/Argyra, Fire/Pyrakanth, Water/Lamenth, Earth/Meridia, Wood/Virelune), WAVE progression (Wake→Clean→Grow→Show), vibeulons economy",
    "political_system": "5_nations",
    "nations_available": ["Argyra", "Pyrakanth", "Lamenth", "Meridia", "Virelune"],
    "personal_throughput": "4_moves",
    "moves": ["Wake Up", "Clean Up", "Grow Up", "Show Up"],
    "spatial_structure": "bruised_banana → mtgoa_org → chapter_instances"
  },

  "campaign_flavor_layers": {
    "allyship_domains": ["Gathering Resources", "Raising Awareness"],
    "domain_guides": {
      "Gathering Resources": "Sage",
      "Raising Awareness": "Shaman"
    },
    "nation_flavor": "Lamenth",
    "nation_description": "Water channel (sadness/depth/memory). Movement style: grief_dialogue, emotional_witnessing, story_excavation.",

    "spatial_flavor": {
      "appearance": "Coastal island with three springs (one fresh, two brackish). Tidal flats. Weathered fishing huts.",
      "tone": "quiet, reflective, resilience-focused",
      "npcs_present": ["Sage (elder who remembers ceremony)", "Diplomat (young merchant questioning traditions)", "Shaman (storyteller)"]
    },

    "real_world_context": {
      "allyship_work": "Community water access and resilience",
      "actual_players": "real community members dealing with scarcity and self-sufficiency",
      "urgency": "Water disruption 5 years ago; old knowledge being revived"
    },

    "game_world_flavor": {
      "metaphor": "Springs as sacred, unreliable, requiring honesty to access",
      "spirits_and_forces": "Water spirits guard deep wells. Drought spirits taunt salt flats. Asking requires naming what we lack.",
      "ceremony": "Old water ritual being revived; new workers learning from elders"
    }
  },

  "campaign_pacing": {
    "prompts_used": {
      "gr": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
      "ra": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    },
    "year_focus": 1,
    "cycling": true
  },

  "nesting": {
    "chapter_ref": "mtgoa-chapter-1",
    "book_ref": "mtgoa-book",
    "org_ref": "mtgoa-org",
    "parent_campaign_ref": "bruised-banana"
  }
}
```

---

## 2. Contextualization API

### 2.1 POST `/api/mtgoa/campaigns`

GM creates a new campaign with worldbuilding context.

**Request**:
```json
{
  "campaign_name": "The Gathering at the Shore",
  "chapter": 1,
  "allyship_domains": ["Gathering Resources", "Raising Awareness"],
  "worldbuilding_context": {
    "geography": "Coastal island...",
    "social": "Merchant families...",
    "history": "Trade disruption...",
    "magic": "Water spirits..."
  },
  "campaign_pacing": {
    "prompts_used": { "gr": [1,2,3,4,5,6,7,8,9,10,11,12,13], "ra": [1,2,3,4,5,6,7,8,9,10,11,12,13] },
    "year_focus": 1,
    "cycling": true
  }
}
```

**Response** (201):
```json
{
  "status": "success",
  "campaign": {
    "campaign_id": "mtgoa-chapter-1-coastal",
    "campaign_name": "The Gathering at the Shore",
    "worldbuilding_context": { /* ...as provided... */ },
    "nesting": { /* campaign wiring */ }
  },
  "meta": {
    "prompts_available": 26,
    "alchemy_channels_covered": ["Metal", "Water", "Wood", "Fire", "Earth"],
    "guide_lenses": ["Sage", "Diplomat"]
  }
}
```

---

### 2.2 GET `/api/mtgoa/campaigns/:campaign_id/contextualized-prompts`

Get all prompts for a campaign with inherited world properties + flavor layer contextualization.

**Query Parameters**:
```
?domain=Gathering+Resources (optional, filter by domain)
?intensity=mild|medium|high (optional)
?sort_by=sequence|channel
```

**Example Request**:
```
GET /api/mtgoa/campaigns/mtgoa-chapter-1-coastal/contextualized-prompts?domain=Gathering+Resources
```

**Response** (200):
```json
{
  "status": "success",
  "campaign_id": "mtgoa-chapter-1-coastal",
  "inherited_world": {
    "magic_system": "emotional_alchemy",
    "nation": "Lamenth (Water/sadness/depth)",
    "moves": ["Wake Up", "Clean Up", "Grow Up", "Show Up"],
    "spatial_context": "Chapter 1 clearing in MTGOA Organization in Bruised Banana"
  },
  "campaign_flavor_layers": {
    "spatial_appearance": "Coastal island with three springs (one fresh, two brackish). Tidal flats.",
    "domain_focus": ["Gathering Resources", "Raising Awareness"],
    "tone": "quiet, reflective, resilience-focused",
    "real_world_context": "Community water access and resilience",
    "game_world_flavor": "Springs are sacred and unreliable. Water spirits reward honesty."
  },
  "prompts": [
    {
      "card_id": "gr_01",
      "base_prompt": {
        "title": "Inventory",
        "primary_question": "What resources do you already have?",
        "clarification": "(What do you claim? What have you dismissed as 'not enough'?)"
      },
      "inherited_alchemy": {
        "channel": "Water",
        "altitude": "dissatisfied",
        "wave_stage": "Wake",
        "move_type": "Acknowledge",
        "nation": "Lamenth (sadness/depth/memory)"
      },
      "flavor_contextualization": {
        "spatial_detail": "The three springs are your island's primary resource. One flows clear; two taste of salt.",
        "tone_adjustment": "In this quiet, reflective campaign, the asking requires naming what you lack.",
        "guide_lens": "Sage",
        "guide_voice": "An elder who remembers the old water ceremony and knows the springs."
      },
      "contextualized_version": {
        "title": "Inventory at the Shore",
        "primary_question": "What resources already exist at the shore—in your body, in your island, in your community—that you can gather?",
        "clarification": "Think about: the three springs (which flows are yours?), the tidal flats (what gifts the tide?), your trading contacts (who do you hold close?), the Keeper elders (what did they teach you?), your hands (what skill do you carry?).",
        "campaign_color": {
          "spatial": "The springs are your island's primary resource. Before the trade disruption, mainland goods arrived by merchant ships. Now, the springs are your renewal.",
          "emotional": "Water spirits guard the deep wells. They will answer honesty with abundance.",
          "real_world_bridge": "In real work: Which actual resources (water access, trade contacts, elder knowledge) do you claim despite limitations?"
        }
      }
    }
  ]
}
```

**What's happening**:
1. Inherited world properties flow down (magic system, nation, moves, spatial context)
2. Campaign flavor layers are applied (spatial appearance, tone, real-world context, game-world flavor)
3. Base prompt contextualized with both inherited + flavor layers
4. Guide lens prepared with campaign-appropriate voice

---

## 2.3 Worldbuilding Evolution vs. Destruction

The critical friction mechanism preventing mid-campaign whipsawing:

### Evolution Through Play (Preferred)

Worldbuilding context changes **only through the consequences of play**. When players complete quests and create BARs, the world responds organically:

**Example**:
- Foundations initial state: "Merchant families control trade; young workers are leaving"
- Player's Year 1 BAR: "I claimed the elder's knowledge about water ceremony"
- GM's play-driven evolution: "The young workers see the ceremony being revived. Some are returning to learn."
- Foundations adjustment: Still merchant-controlled market, BUT now young workers have a reason to stay (ceremony revival)
- Result: Context evolved through player action, not GM whim

**Rule**: Context can evolve, but only if the evolution responds to **specific player BARs** from that campaign. GM cannot casually rewrite the world.

### Destruction and Restart (High Friction)

If the GM decides the world no longer serves the campaign, they may invoke **World Destruction**:

**Prerequisites**:
- Campaign has been running for at least one cycle (all players have completed at least one BAR each, or 4+ weeks have passed, whichever is first)
- GM has attempted evolution-through-play for at least two player decisions
- GM prepares a new Foundations context for the same campaign (or creates a new campaign)

**Operationally**:
1. GM writes a clear **destruction narrative** (1–2 paragraphs): "What happened to this world? Why can't it continue?"
   - Example: "The trade disruption worsened. The island was evacuated. A new settlement must rebuild."
2. All **existing BARs remain in the campaign history** but are marked with a `campaign_phase` tag: `original_world` vs. `new_world_v2`
3. **Milestone roll-up continues across both phases** — BARs from the original world still count toward Chapter 1 milestone, but they're visibly distinct
4. **Players are explicitly informed**: "The world has changed. Your old discoveries still matter, but the context is new."
5. GM defines new Foundations context (another 30 minutes) and resumes with new prompts

**Why this friction exists**: Destroying a world is a big decision that affects all players. High friction prevents casual rewrites while allowing GMs to make bold pivots when necessary.

### Summary: The Two Paths

| Path | Trigger | Friction | Duration | BAR Impact |
|------|---------|----------|----------|-----------|
| **Evolution** | Player BAR creates logical consequence | Low | Emerges through play | Continuous, organic development |
| **Destruction** | GM decides world can't continue | High | Requires narrative + cooldown | BARs preserved but phase-tagged |

**Lazy Dungeon Master principle**: "Prepare only what benefits the game." The same principle applies to worldbuilding change: if the change benefits the game, the GM pays the friction cost. If it's just indecision, they don't.

---

### 2.4 POST `/api/mtgoa/campaigns/:campaign_id/generate-quest`

Generate a quest from a contextualized prompt.

**Request**:
```json
{
  "prompt_id": "gr_01",
  "player_context": {
    "player_id": "player_123",
    "current_channel": "Water",
    "altitude_state": "dissatisfied",
    "year_in_cycle": 1
  },
  "apply_worldbuilding": true
}
```

**Response** (200):
```json
{
  "status": "success",
  "quest": {
    "flow_id": "gr_01_mtgoa-chapter-1-coastal_water_dissatisfied_v1",
    "campaign_id": "mtgoa-chapter-1-coastal",
    "nodes": [
      {
        "id": "intro_gr_01",
        "type": "introduction",
        "copy": "You stand by the three springs. One flows clear. Two taste of salt. What resources do you see here?",
        "worldbuilding_detail": "The springs are your island's primary resource. Before the trade disruption, mainland goods arrived by merchant ships. Now, the springs are your renewal.",
        "actions": [{ "type": "choose", "next_node_id": "prompt_gr_01" }]
      },
      {
        "id": "prompt_gr_01",
        "type": "prompt",
        "copy": "Inventory your resources: What already exists at the shore—in your body, in your island, in your community? What do you claim? What have you dismissed as 'not enough'?",
        "worldbuilding_detail": "Think about: the springs (which flows are yours?), the tidal flats (what gifts the tide?), your trading contacts (who do you hold close?), the Keeper elders (what did they teach you?), your hands (what skill do you carry?).",
        "actions": [{ "type": "submit", "next_node_id": "bar_gr_01" }]
      },
      {
        "id": "bar_gr_01",
        "type": "BAR_capture",
        "copy": "Write down: I claim these resources. Speak to the springs that you speak to them: your fresh water, your salt, your elders' voice, your own hands.",
        "actions": [{ "type": "create_BAR", "next_node_id": "completion_gr_01" }]
      },
      {
        "id": "completion_gr_01",
        "type": "completion",
        "copy": "Your inventory is visible. The springs know what you claim. The spirits know that you know.",
        "actions": []
      }
    ],
    "alchemy_metadata": {
      "source_prompt": "gr_01",
      "channel": "Water",
      "altitude": "dissatisfied",
      "wave_stage": "Wake",
      "move_type": "Acknowledge"
    }
  }
}
```

---

## 3. GM UI Patterns (Regent-Led)

### 3.1 Campaign Creation Wizard

**Step 1**: Basic Info
- Campaign name, chapter, allyship domain(s)

**Step 2**: Worldbuilding Context (4 Foundations domains)
- Geography: "Describe the physical world"
- Social: "Describe power & relationships"
- History: "What happened before?"
- Magic: "What is threshold/gift/shadow?"

**Step 3**: Campaign Pacing
- Select which prompts to use (all 52 or a subset)
- Year focus (surface work vs. shadow work)
- Will players cycle through prompts?

**Step 4**: Review & Launch
- See all prompts as they'll appear in this campaign
- See sample quests with worldbuilding applied
- Launch campaign

### 3.2 Campaign Dashboard

After launch, GM sees:
- Campaign context (Foundations domains) + **version history** (when context changed and why)
- Prompts available for this campaign
- Player progress (who has completed which prompts)
- BAR library (all BARs created in this campaign, tagged with campaign/chapter and world phase)
- **Worldbuilding evolution log** — shows BARs that triggered context changes + the GM's narrative explanation
- **World Destruction status** — if applicable, shows old-world BARs and new-world start date

### 3.3 Worldbuilding Context Editing (Constrained)

GMs can refine Foundations context, but only under specific conditions:

**Evolution-through-play edits** (low friction):
- A player BAR created a logical consequence that changes one Foundations domain
- GM explains: "Player's BAR about X led to Y, so I'm adjusting [domain] to reflect this"
- Example: Player BAR claimed elder's knowledge → GM adjusts History domain to note ceremony revival
- Approval: Automatic (change is tied to a specific BAR)

**Full worldbuilding rewrite** (high friction):
- Use the World Destruction process (see Section 2.3)
- Not a quick edit; requires narrative and cooldown period
- Prevents casual mid-campaign changes

**Anti-pattern (forbidden)**:
- GM casually refining prompts without a tied BAR or destruction narrative
- "I just want to make this prompt better" without play consequence
- Result: Players experience whipsawing; trust breaks

**Lazy Dungeon Master principle applied**: GMs can edit, but only if the edit benefits the game (is tied to play). Otherwise, they live with the initial worldbuilding choice until destruction/restart.

```
IF GM wants to refine context:
  - Check: Did a player BAR create a logical consequence?
    - YES → Evolution edit (tie it to the specific BAR)
    - NO → Either play more, or invoke World Destruction
```

---

## 4. Verification Quest (Diplomat-Led)

How does a GM know their contextualization is working?

**The Diplomat Test**: Playtest one prompt in the campaign with real players.

**Checklist**:
- [ ] Player reads the opening quest node
- [ ] Player says (or implies): "I know where I am"
- [ ] Player feels the worldbuilding details matter to their choices
- [ ] Player's BAR references something specific about the world
- [ ] Player wants to return to this world

If all 5 checks pass, the contextualization is deft.

---

## 5. Example: Full Campaign Lifecycle

### GM's Journey

**Week 1**:
- GM reads MTGOA Chapter 1
- GM imagines their world (coastal island with water scarcity)
- GM creates campaign: "The Gathering at the Shore"
- GM defines Foundations context
- System shows all 26 prompts (Gathering Resources + Raising Awareness)

**Week 2**:
- GM reads the contextualized prompts
- GM previews sample quests for gr_01, gr_02, ra_01
- GM adjusts worldbuilding context slightly (adds detail about Keeper ceremony)
- GM launches campaign to players

**Week 3–4**:
- Players engage with prompts (contextualized with coastal world details)
- Each prompt feels grounded in the island
- BARs created in this campaign carry the water/island/merchant/Keeper context

### Player's Experience

When a player selects "Inventory" (gr_01):

They don't see: "What resources do you already have?"
They see: "What resources already exist at the shore—in your body, in your island, in your community?"

The quest unfolds:
- Opening: "You stand by the three springs..."
- Prompt: "Inventory your resources: what already exists... What do you claim?"
- BAR capture: "Write down: I claim these resources. Speak to the springs..."

**Result**: Player's BAR is now about *their* resources in *this* world, not generic resources.

---

## 6. Regent's Role (Campaign Structure)

Regent ensures:
- Campaign nesting is correct (Chapter → Book → Org → BB)
- Worldbuilding context is complete (all 4 Foundations domains filled)
- Prompt selection is coherent (why this domain? why this year focus?)
- Player BARs are correctly tagged (campaign_id, chapter_ref, domain)
- Milestone roll-up works (Chapter 1 BAR → MTGOA Book milestone)

**Regent's Verification**: After GM launches a campaign, Regent checks:
```
✓ Campaign metadata complete
✓ All prompts contextualized
✓ BAR tagging structure in place
✓ Milestone roll-up working
✓ Chapter 1 BAR contributes to MTGOA Book milestone
```

---

## 7. Architect's Role (System Integration)

Architect ensures:
- Contextualization API is performant
- Worldbuilding context is stored & versioned
- Quest generation preserves alchemy metadata
- Guide lens voice is customizable per world
- Fallback to base prompts if worldbuilding unavailable

**Architect's Build Checklist**:
```
✓ Campaign CRUD endpoints
✓ Contextualized prompt query (fast)
✓ Quest generation with worldbuilding injection
✓ Campaign context caching
✓ Version history (if GM adjusts worldbuilding)
✓ Error handling (missing context, invalid domains)
```

---

## 8. Design Decision: Why This Approach?

### Problem Solved
GMs want to create campaigns that feel **deft** (coherent, grounded, intentional). Generic prompts feel flat.

### Solution
Bake worldbuilding into prompts at the campaign level, not the global level.

### Why Not Other Approaches?

**Approach A**: Pre-generated prompts for each world
- ❌ Doesn't scale (need 52 × 100 campaigns)
- ❌ Loses the power of a universal deck

**Approach B**: Let GMs write entirely new prompts
- ❌ Requires authoring skill, not just curation
- ❌ Loses the emotional alchemy alignment

**Approach C**: Template-based contextualization (chosen)
- ✅ Universal deck + campaign-specific application
- ✅ GMs curate their world, not author new prompts
- ✅ Emotional alchemy is preserved
- ✅ Scales to unlimited campaigns

---

## 9. Future Enhancements

1. **Template library**: Pre-written campaign flavor layers for common scenarios (coastal island + Lamenth flavor, urban organizing + Argyra flavor, etc.) — jump-start GMs
2. **Spatial geography documentation**: Formal inventory of what inherited BARs-engine world offers (room types, NPC availability, nation movement mechanics)
3. **Nation flavor profiles**: Detailed "move style" for each nation in campaign context (how does Argyra's precision show up in prompt tone? Pyrakanth's courage?)
4. **Guide lens customization**: GM defines how each guide lens speaks in their specific campaign (e.g., "Sage speaks as a coastal elder who remembers ceremony")
5. **Forking wizard**: When a GM intentionally creates a parallel world, a 2-hour guided workflow to design new Foundations (magic system, nations, geography, history)
6. **Multi-campaign inheritance**: GMs can create campaign variants that inherit from a "parent" campaign's flavor layers, enabling rapid iteration
7. **BAR context inheritance tracker**: Show which inherited properties (nation, channel, domain) are represented in each player's BAR collection

---

## 10. Critical Success Factors

The system works **if and only if all three are true**:

### Factor 1: 15-Minute Setup Window (Additive Layer Model)
> A GM can spend 15 minutes defining campaign flavor layers (scope + spatial flavor) and have the system produce 26 contextualized prompts that feel grounded and unique to the campaign, while inheriting the stable 5-nation world.

**Lazy Dungeon Master principle**: "Prepare only what most benefits your game." GMs inherit magic, politics, moves, and geography. They customize flavor layers on top.

**Setup time breakdown**:
- Required: Campaign scope + spatial flavor (10 min)
- Optional: Real-world context + game-world flavor (5 min)
- Result: Prompts automatically contextualized with both inherited + flavor layers

### Factor 2: Inheritance Chain Clarity
> The inheritance chain is transparent: Bruised Banana → MTGOA Org → Chapter 1 → Campaign Flavor. Players see what's inherited and what's customized.

Example inheritance check:
- Inherited: 5 nations, emotional alchemy, 4 moves
- Inherited: Spatial instances (Bruised Banana, MTGOA Organization, Chapter spaces)
- Customized: Coastal island flavor, Lamenth nation prominence, Gathering Resources domain focus
- Customized: Real context (water scarcity), game flavor (spirits, springs, ceremony)
- Result: Players navigate inherited political/emotional system grounded in campaign's specific context

### Factor 3: Forking Path (Advanced: Full Worldbuilding)
> When a GM intentionally creates a parallel world (not using inherited nations/magic/geography), they have a clear path to full Foundations design.

**Normal campaigns** (additive layer): 15 min, inherit world
**Forking campaigns** (parallel world): 2+ hours, define new Foundations
**Signal**: GM decides "This campaign needs a completely different magic system" or "These nations don't fit"

Success metrics:
- "Most GMs finish setup in 15 minutes with inherited world feeling grounded"
- "Advanced GMs who fork understand they're building parallel worlds, not exceptions"
- "Campaign BAR tagging preserves inheritance chain for all roll-up mechanics"

Everything above is in service of these three metrics.

---

## References

- [MTGOA_52CARDS_PROMPTS.json](MTGOA_52CARDS_PROMPTS.json) — Live prompts with hooks
- [MTGOA_52CARDS_API_CONTRACTS.md](MTGOA_52CARDS_API_CONTRACTS.md) — API spec
- [bars-engine/FOUNDATIONS.md](../bars-engine/FOUNDATIONS.md) — Foundations ontology
- [MTGOA Chapter 1 Demo Contract](../bars-engine/.specify/contracts/mtgoa-chapter-1-demo-contract.md) — Campaign nesting pattern

