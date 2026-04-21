# MTGOA 52-Card Prompt Deck — API Contracts
## Data Integration with BARs Engine & Quest Generation

**Status**: Draft (awaiting implementation review)
**Created**: 2026-04-20
**Audience**: bars-engine backend team, quest generation system, GM toolkit

---

## Purpose

Define strict contracts for how the 52-card prompt deck integrates with:
- Quest generation pipeline
- Campaign wiring (Chapter 1 → Book → Org → Bruised Banana)
- Emotional alchemy query engine
- Player state & progression systems

All API responses must be machine-parseable and suitable for both:
- **Player-facing**: prompts, quests, next-prompt recommendations
- **GM-facing**: worldbuilding hooks, campaign configuration, guide lens selection

---

## 1. Core Data Model (Prompt)

### Prompt Object Schema

```json
{
  "card_id": "gr_01",
  "suit": "Clubs",
  "season": "Spring",
  "domain": "Gathering Resources",
  "domain_guide_lens": "Sage",
  "card_number": 1,
  "position_in_sequence": 1,
  "phase": "Wake Up",
  "depth_level": "Recognition",

  "prompt": {
    "title": "Inventory",
    "primary_question": "What resources do you already have?",
    "clarification": "(What do you claim? What have you dismissed as 'not enough'?)",
    "guide_lens": "Sage",
    "gate_risk": ["Victim", "Scarcity"],
    "word_count": 28
  },

  "emotional_alchemy": [
    {
      "emotion": "Victim",
      "channel": "Water",
      "altitude": "dissatisfied",
      "intensity": "mild",
      "wave_stage": "Wake",
      "move_type": "Acknowledge"
    }
  ],

  "design_properties": {
    "emotional_intensity": "mild",
    "bar_phases": ["Breakthrough", "Action", "Reflection", "Sustain"],
    "cyclical_depth_layers": 3,
    "replayability_index": 3,
    "tone_category": "gentle_awakening"
  },

  "gm_worldbuilding_hooks": {
    "geography": "What resources does your land/body have?",
    "social": "What resources does your community structure give you?",
    "history": "What resources survived from before?",
    "magic": "What invisible resources are already present?"
  },

  "shadow_work": {
    "year_1_surface": "What do you see? What have you normalized as 'scarcity'?",
    "year_2_shadow": "What part of you has learned not to claim what's yours?",
    "year_3_gift": "How has your inventory taught you what's truly valuable?"
  },

  "deepening_arc": {
    "replayability": true,
    "deepens_to": "gr_05"
  }
}
```

---

## 2. Endpoints

### 2.1 GET `/api/mtgoa/prompts/:card_id`

**Purpose**: Fetch a single prompt with full alchemy & worldbuilding data.

**Example Request**:
```
GET /api/mtgoa/prompts/gr_01
```

**Response** (200):
```json
{
  "status": "success",
  "data": { /* full prompt object */ },
  "meta": {
    "source": "MTGOA 52-Card Deck",
    "version": "1.0.0",
    "available_for_quest_generation": true
  }
}
```

**Response** (404):
```json
{
  "status": "error",
  "error": "Prompt not found",
  "card_id": "xx_00"
}
```

**Usage in bars-engine**:
- Player selects a prompt from Allyship Campaign hub
- Backend fetches full prompt data for display & quest generation

---

### 2.2 GET `/api/mtgoa/prompts/query`

**Purpose**: Query prompts by emotional channel, domain, altitude, WAVE stage.

**Query Parameters**:
```
?channel=Metal|Water|Wood|Fire|Earth
?domain=Gathering+Resources|Skillful+Organizing|Direct+Action|Raising+Awareness
?altitude=dissatisfied|neutral|satisfied
?wave_stage=Wake|Clean|Grow|Show
?depth_level=Recognition|Deepening|Commitment
?intensity=mild|medium|high
?sort_by=position|season|intensity
&limit=10
&offset=0
```

**Example Request**:
```
GET /api/mtgoa/prompts/query?channel=Water&altitude=dissatisfied&wave_stage=Wake&limit=5
```

**Response** (200):
```json
{
  "status": "success",
  "data": [
    { /* prompt object */ },
    { /* prompt object */ }
  ],
  "meta": {
    "total": 52,
    "returned": 5,
    "filters_applied": {
      "channel": "Water",
      "altitude": "dissatisfied",
      "wave_stage": "Wake"
    }
  }
}
```

**Usage in bars-engine**:
- GM selecting next prompt for player based on emotional channel
- Auto-routing player to next prompt after BAR completion
- Building Allyship Campaign next-move suggestions
- Worldbuilding context selection (Foundations integration)

---

### 2.3 GET `/api/mtgoa/channels/:channel`

**Purpose**: Get all prompts for an emotional channel in WAVE progression order.

**Example Request**:
```
GET /api/mtgoa/channels/Water
```

**Response** (200):
```json
{
  "status": "success",
  "channel": "Water",
  "channel_name": "Sadness",
  "channel_description": "Something I care about is distant or misaligned",
  "data": {
    "Wake": [ /* 13 prompts ordered by sequence */ ],
    "Clean": [ /* 13 prompts ordered by sequence */ ],
    "Grow": [ /* 13 prompts ordered by sequence */ ],
    "Show": [ /* 13 prompts ordered by sequence */ ]
  },
  "meta": {
    "total_prompts_in_channel": 52,
    "domains_represented": ["Gathering Resources", "Skillful Organizing", "Direct Action", "Raising Awareness"],
    "wave_progression_complete": true
  }
}
```

**Usage in bars-engine**:
- Quest generation engine selects prompts by emotional channel
- Player journeys that follow a single emotional channel thread
- Channel-specific difficulty curves (mild → medium → high → reflective)

---

### 2.4 POST `/api/mtgoa/generate-quest`

**Purpose**: Generate a quest from a prompt + player state.

**Request**:
```json
{
  "prompt_id": "gr_01",
  "player_context": {
    "player_id": "user_123",
    "current_emotional_channel": "Water",
    "altitude_state": "dissatisfied",
    "wave_stage": "Wake",
    "year_in_cycle": 1
  },
  "campaign_context": {
    "campaign_id": "mtgoa-chapter-1",
    "book_id": "mtgoa-book",
    "org_id": "mtgoa-org",
    "parent_campaign_id": "bruised-banana"
  },
  "quest_config": {
    "include_worldbuilding_hooks": true,
    "foundations_domains": ["geography", "social"],
    "guide_lens": "Sage",
    "max_nodes": 6,
    "tone": "exploratory"
  }
}
```

**Response** (200):
```json
{
  "status": "success",
  "quest": {
    "flow_id": "gr_01_water_dissatisfied_wake_v1",
    "campaign_id": "mtgoa-chapter-1",
    "start_node_id": "intro_gr_01",
    "nodes": [
      {
        "id": "intro_gr_01",
        "type": "introduction",
        "copy": "You stand in a quiet place. What do you see around you that you can use?",
        "actions": [{ "type": "choose", "next_node_id": "prompt_gr_01" }],
        "emits": ["quest_started", "prompt_viewed"]
      },
      {
        "id": "prompt_gr_01",
        "type": "prompt",
        "copy": "What resources do you already have? (Think about what you claim. What have you dismissed as 'not enough'?)",
        "actions": [{ "type": "submit", "next_node_id": "bar_gr_01" }],
        "emits": ["prompt_answered"]
      },
      {
        "id": "bar_gr_01",
        "type": "BAR_capture",
        "copy": "Write down what you discovered.",
        "actions": [{ "type": "create_BAR", "next_node_id": "reflection_gr_01" }],
        "emits": ["bar_created"]
      },
      {
        "id": "reflection_gr_01",
        "type": "reflection",
        "copy": "This is what you're claiming. This is the inventory you're working with.",
        "actions": [{ "type": "confirm", "next_node_id": "completion_gr_01" }],
        "emits": ["reflection_acknowledged"]
      },
      {
        "id": "completion_gr_01",
        "type": "completion",
        "copy": "Your inventory is now visible. You can work with what you see.",
        "actions": [],
        "emits": ["quest_completed"]
      }
    ],
    "completion_conditions": [
      { "type": "node_reached", "node_id": "completion_gr_01" }
    ],
    "expected_events": [
      "quest_started",
      "prompt_viewed",
      "prompt_answered",
      "bar_created",
      "reflection_acknowledged",
      "quest_completed"
    ]
  },
  "alchemy_metadata": {
    "source_prompt_id": "gr_01",
    "emotional_channel": "Water",
    "altitude": "dissatisfied",
    "wave_stage": "Wake",
    "move_type": "Acknowledge",
    "intensity": "mild"
  },
  "campaign_metadata": {
    "campaign_id": "mtgoa-chapter-1",
    "agent_metadata": {
      "chapterRef": "mtgoa-chapter-1",
      "bookRef": "mtgoa-book",
      "orgRef": "mtgoa-org",
      "parentCampaignRef": "bruised-banana"
    }
  }
}
```

**Response** (400 - Invalid):
```json
{
  "status": "error",
  "error": "Quest generation failed",
  "reason": "Prompt not suitable for single-player mode",
  "suggestions": ["Try a different prompt", "Adjust quest_config"]
}
```

**Usage in bars-engine**:
- Convert selected prompt → playable quest
- Respect campaign nesting (Chapter 1 → Book → Org → BB)
- Embed worldbuilding context from Foundations
- Generate guide lens-appropriate dialogue

---

### 2.5 GET `/api/mtgoa/library`

**Purpose**: Get full 52-card library with filtering options.

**Query Parameters**:
```
?include_metadata=true|false (include alchemy, worldbuilding, shadow work)
?filter_by=domain|channel|depth
?domain=Gathering+Resources
?sort_by=sequence|intensity|replayability
```

**Example Request**:
```
GET /api/mtgoa/library?include_metadata=true&domain=Direct+Action&sort_by=intensity
```

**Response** (200):
```json
{
  "status": "success",
  "library": {
    "title": "Mastering the Game of Allyship: 52-Card Prompt Deck",
    "version": "1.0.0",
    "total_prompts": 52,
    "created_date": "2026-04-20",
    "prompts": [
      { /* card_id, title, domain, emotional_alchemy */ }
    ]
  },
  "meta": {
    "domains": ["Gathering Resources", "Skillful Organizing", "Direct Action", "Raising Awareness"],
    "channels": ["Metal", "Water", "Wood", "Fire", "Earth"],
    "depth_levels": ["Recognition", "Deepening", "Commitment"],
    "all_available_for_quest_generation": true
  }
}
```

**Usage in bars-engine**:
- GM Toolkit: browse available prompts by domain/channel
- Campaign configuration: select prompt subset for a chapter
- Allyship Campaign hub: display all available prompts

---

## 3. Campaign Integration (MTGOA Nesting)

All quest generation responses include full campaign metadata to support the 4-level nesting:

```
Bruised Banana
  └── MTGOA Organization
        └── MTGOA Book/Game
              └── Chapter 1–12 (each via prompt deck)
```

When a BAR is created from a prompt:

```json
{
  "bar": {
    "campaignRef": "mtgoa-chapter-1",
    "agentMetadata": {
      "chapterRef": "mtgoa-chapter-1",
      "bookRef": "mtgoa-book",
      "orgRef": "mtgoa-org",
      "parentCampaignRef": "bruised-banana"
    }
  }
}
```

This enables:
- Milestone roll-up: Chapter 1 BAR → MTGOA Book/Game milestone
- Traversable campaign structure for BAR UI
- Proper tag inheritance (book, org, parent campaign)

---

## 4. GM Toolkit Integration (Foundations Worldbuilding)

The `gm_worldbuilding_hooks` in each prompt enable GM contextualization via Foundations domains:

**Request** (GM selecting worldbuilding context):
```json
{
  "prompt_id": "gr_01",
  "worldbuilding_context": {
    "geography": "A coastal village with limited fresh water",
    "social": "Power held by a merchant family",
    "history": "Recent trade disruption",
    "magic": "Water spirits guard the deep wells"
  }
}
```

**Usage**:
- GM Toolkit feeds Foundations data into prompt contextualization
- Quests generated with deepened worldbuilding detail
- Player experiences same emotional prompt in their unique world

---

## 5. Validation & Quality Gates

### Pre-Quest-Generation Checks

Before quest generation, validate:

- **Prompt health**: Card exists, all fields present, emotional_alchemy complete
- **Player state alignment**: Player's current channel matches prompt channel (or is neutral)
- **Campaign wiring**: All campaign refs are valid
- **WAVE progression**: Player hasn't already completed this card at this intensity

### Post-Quest-Generation Checks

After quest generation, validate:

- **Flow validity**: All nodes reachable, no cycles in onboarding quests
- **BAR lifecycle**: Prompt → capture → validate sequence intact
- **Completion condition**: At least one terminal node reachable
- **Copy clarity**: No system jargon, all <30 words per node

---

## 6. Error Handling

### Common Errors

| Error | Cause | Recovery |
|-------|-------|----------|
| `PROMPT_NOT_FOUND` | Card ID doesn't exist | Fallback to prompt library UI |
| `CHANNEL_MISMATCH` | Player channel incompatible | Suggest next available prompt |
| `CAMPAIGN_WIRING_INVALID` | Campaign refs missing/invalid | Return 400; log for admin review |
| `QUEST_GENERATION_FAILED` | LLM output invalid JSON | Retry once; if fails again, use template quest |
| `PLAYER_STATE_MISSING` | No emotional channel data | Return 400; prompt player to complete onboarding |

---

## 7. Rate Limiting & Caching

- **Prompt fetch** (`GET /api/mtgoa/prompts/:card_id`): Cache 24h (static data)
- **Library endpoint** (`GET /api/mtgoa/library`): Cache 24h
- **Query endpoint** (`GET /api/mtgoa/prompts/query`): Cache 1h (filtered results)
- **Quest generation** (`POST /api/mtgoa/generate-quest`): No cache (user-specific)

---

## 8. Future Enhancements

1. **Prompt recommendation engine**: `POST /api/mtgoa/recommend-next-prompt` using player BAR history + alchemy state
2. **Cyclical deepening tracking**: `GET /api/mtgoa/prompts/:card_id/year/:year` returns Year 1/2/3 variants
3. **Multi-channel journeys**: Support players who transition between channels mid-campaign
4. **GM contextualization API**: `POST /api/mtgoa/contextualize-prompt` with Foundations worldbuilding data

---

## 9. Response Format Standard

All responses follow this pattern:

```json
{
  "status": "success|error",
  "data": { /* ... */ },
  "meta": {
    "timestamp": "2026-04-20T19:25:00Z",
    "version": "1.0.0",
    "request_id": "uuid"
  },
  "error": "error message (if status=error)"
}
```

---

## 10. Authentication & Authorization

- **Player endpoints**: Require session auth (player viewing their own prompts/quests)
- **GM endpoints**: Require campaign admin role or Regent role
- **Admin endpoints**: Require developer role (prompt library management)

---

## References

- [MTGOA_52CARDS_PROMPTS.json](MTGOA_52CARDS_PROMPTS.json) — Live prompt data
- [EMOTIONAL_ALCHEMY_TRANSLATOR.md](EMOTIONAL_ALCHEMY_TRANSLATOR.md) — Channel mapping reference
- [bars-engine quest-generation-prompt-contract.md](../bars-engine/docs/architecture/quest-generation-prompt-contract.md)
- [MTGOA Chapter 1 Demo Contract](../bars-engine/.specify/contracts/mtgoa-chapter-1-demo-contract.md)

