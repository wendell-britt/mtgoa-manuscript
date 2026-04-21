# MTGOA Schema Update Plan — Phase 1 Deliverable

**Purpose:** Define Prisma schema changes to support inherited vs. customized property separation in MTGOA campaigns.

**Status:** Phase 1 Deliverable (Schema Design)
**Created:** 2026-04-20

---

## Overview

Current state: Campaign model has domain-specific fields scattered across multiple JSON columns and text fields.

Goal: Separate `inherited_world` (read-only, inherited from parent) from `campaign_flavor_layers` (customizable by GM).

---

## Key Changes to Campaign Model

### 1. Add `inheritedWorld` JSON Field

**Purpose:** Store read-only inherited properties from parent chain (Instance → Campaign).

```prisma
model Campaign {
  // ... existing fields ...

  /// Inherited world properties (read-only, inherited from Instance)
  /// Contains: magic_system, political_system, spatial_structure, personal_throughput
  inheritedWorld Json?

  /// Customizable flavor layers for this campaign
  /// Contains: allyship_domains, spatial_flavor, nation_flavor, real_world_context, game_world_flavor
  campaignFlavorLayers Json?
}
```

**Shape of `inheritedWorld`:**
```json
{
  "magic_system": {
    "channels": ["fear", "anger", "sadness", "neutrality", "joy"],
    "element_mapping": {
      "fear": "metal",
      "anger": "fire",
      "sadness": "water",
      "neutrality": "earth",
      "joy": "wood"
    }
  },
  "political_system": {
    "nations": ["Argyra", "Pyrakanth", "Lamenth", "Meridia", "Virelune"],
    "nation_profiles": {
      "Argyra": {
        "element": "metal",
        "emotion_channel": "fear",
        "developmental_emphasis": ["wake_up", "grow_up"],
        "move_style_modifiers": ["precision", "strategic_awareness", "calm_observation"]
      }
      // ... other nations
    }
  },
  "spatial_structure": {
    "instance_id": "MTGOA-BG-001",
    "instance_name": "Mastering the Game of Allyship — Book/Game",
    "parent_path": ["bruised-banana", "mastering-allyship"]
  },
  "personal_throughput": {
    "moves": [
      { "move": "wake_up", "season": "spring" },
      { "move": "clean_up", "season": "winter" },
      { "move": "grow_up", "season": "summer" },
      { "move": "show_up", "season": "fall" }
    ]
  }
}
```

---

### 2. Add `campaignFlavorLayers` JSON Field

**Purpose:** Store GM-customizable flavor properties specific to this campaign.

**Shape of `campaignFlavorLayers`:**
```json
{
  "scope": {
    "campaign_name": "Coastal Island: Gathering Resources",
    "chapter_reference": "ch1",
    "allyship_domains": ["GATHERING_RESOURCES"],
    "year_focus": "year_1_surface"
  },
  "spatial_flavor": {
    "description": "Rocky coastal shores with tide pools and ancient stone formations",
    "tone": "contemplative, grounded, water-connected",
    "nation_choice": "Lamenth",
    "npc_present": ["Elder Kai", "Tide Keeper"],
    "sensory_details": {
      "sight": "grey-blue rocks, mist",
      "sound": "waves, seabirds",
      "feel": "salt spray, cool wind"
    }
  },
  "real_world_context": {
    "actual_allyship_work": "Building resource networks for coastal communities affected by climate change",
    "real_world_outcome": "Players identify 3 resources their community already has",
    "intended_action": "Form a resource-sharing circle with 5-10 people"
  },
  "game_world_flavor": {
    "special_rules": "Players can dive into tide pools as a metaphor for resource discovery",
    "resource_limitations": "Only coastal resources available (no mountains or forests)",
    "success_definition": "A functioning resource map that guides real-world sharing"
  },
  "additional_metadata": {
    "created_by": "player_id_123",
    "created_at": "2026-04-20",
    "last_customized_at": "2026-04-20"
  }
}
```

---

### 3. Deprecate Old Fields (Phase 1 Migration)

Old text/JSON fields are deprecated in Phase 1 schema. During this migration:

- `allyshipDomain` — **DEPRECATE.** Use `campaignFlavorLayers.scope.allyship_domains` instead
- `wakeUpContent` — **DEPRECATE.** Use `campaignFlavorLayers.real_world_context.wake_up_message`
- `showUpContent` — **DEPRECATE.** Use `campaignFlavorLayers.real_world_context.show_up_message`
- `questTemplateConfig` — **DEPRECATE.** Move to `campaignFlavorLayers.quest_generation`
- `inviteConfig` — **DEPRECATE.** Move to `campaignFlavorLayers.invite_config`

**Why now, not Phase 2?** Keeping old + new fields in sync is error-prone. Better to migrate existing campaigns to JSON during Phase 1 schema migration (data migration script), then clean up the schema. Avoids "field of truth" ambiguity that caused bugs in similar systems.

**Phase 1 migration checklist:**
- [ ] Write Prisma migration to add JSON fields
- [ ] Write data migration script to populate JSON from old fields
- [ ] Backfill Phase 1 campaigns with JSON data
- [ ] Run queries to verify sync (old ≈ new)
- [ ] Drop old fields from schema (or add deprecation comment + planned removal date)

---

## 4. Update Instance Model (Optional for Phase 1)

Add fields to Instance model to make inherited properties explicit:

```prisma
model Instance {
  // ... existing fields ...

  /// Magic system definition (Emotional Alchemy)
  magicSystemConfig Json? // Inherited by all campaigns

  /// Political system definition (5 Nations)
  politicalSystemConfig Json? // Inherited by all campaigns

  /// Spatial structure definition
  spatialStructureConfig Json? // Inherited by all campaigns

  /// Personal throughput definition (4 Moves, seasons)
  personalThroughputConfig Json? // Inherited by all campaigns

  /// Allyship domains available in this instance
  allyshipDomainsConfig Json? // Inherited by all campaigns
}
```

**Note:** For MTGOA, these are defined in Bruised Banana instance and inherited down. Phase 1 focuses on Campaign model; Instance model updates are secondary.

---

## 5. Inherited World Source (Phase 1 → Phase 2 Decision)

**Decision needed:** Where does `inheritedWorld` data come from?

**Option A: Stored in DB (Recommend)**
- Store `magic_system`, `political_system`, etc. in Instance model during Phase 1
- When campaign is created, copy Instance data to Campaign.inheritedWorld
- Pros: Campaign has complete snapshot, doesn't break if Instance changes
- Cons: Some duplication, but justified for immutability

**Option B: Computed at Request Time**
- Don't store inheritedWorld; compute it from parent Instance + 52-card metadata on each request
- Pros: Single source of truth
- Cons: Slower, doesn't capture "what was the world when this campaign was made"

**Phase 1 Recommendation:** Go with Option A (stored). Phase 2 implementation should populate Instance model with inherited world config, then snapshot it to campaigns.

---

## 6. Add Helper Functions (Schema Documentation)

Document expected behaviors:

### 6.1 Campaign Creation

When campaign is created:
```
1. Fetch parent Instance
2. Extract inherited_world from Instance (magic_system, political_system, etc.)
3. Set Campaign.inheritedWorld = inherited_world (locked snapshot)
4. Set Campaign.campaignFlavorLayers = GmCustomization (unlocked, initially empty)
```

### 6.2 Campaign Retrieval

When campaign is retrieved for GM editing:
```
1. Load Campaign.inheritedWorld (read-only)
2. Load Campaign.campaignFlavorLayers (editable)
3. Merge for contextualization API response
```

### 6.3 Quest Generation

When quest is generated:
```
1. Load prompt from 52-card deck
2. Load inherited_world (magic system, political system) — Phase 2 will design merge logic
3. Load campaignFlavorLayers (spatial flavor, nation choice, domain)
4. Apply contextualization (inherited + flavor)
5. Generate quest with full inheritance metadata
```

**Note:** Contextualization API design (how inherited + flavor combine at render time) is Phase 2 work. See MTGOA_IMPLEMENTATION_ROADMAP.md § 3.2 for preview.

---

## 7. Validation Rules

### For `inheritedWorld` (Read-Only)
- ✅ Auto-populated on campaign creation
- ✅ Cannot be manually edited via API
- ✅ Updated only if parent Instance changes (rare)
- ✅ All required fields must be non-null

### For `campaignFlavorLayers` (Customizable)
- ✅ Can be partially filled (sparse JSON allowed)
- ✅ Can be updated multiple times before campaign goes live
- ✅ Required for live campaign: scope.campaign_name, spatial_flavor.nation_choice
- ✅ Validated against inherited options (e.g., nation_choice must be one of inherited nations)

---

## 8. Migration Strategy (Phase 1 → Phase 2)

### Phase 1 (Current)
- Add new JSON fields to Campaign
- Keep old fields for backward compatibility
- New campaigns populate JSON fields; old campaigns still use text fields

### Phase 2 (Implementation)
- Migrate old fields to JSON fields (data migration)
- Update all API endpoints to read from JSON fields
- Deprecate old text fields

---

## 9. Database Schema Diff

### Add to Campaign model:

```prisma
  /// Inherited world properties (read-only, locked at campaign creation)
  inheritedWorld Json?

  /// Customizable flavor layers (editable by GM before campaign goes live)
  campaignFlavorLayers Json?
```

### Optional add to Instance model:

```prisma
  /// Magic system definition (inherited by all campaigns under this instance)
  magicSystemConfig Json?

  /// Political system definition (inherited by all campaigns under this instance)
  politicalSystemConfig Json?

  /// Spatial structure definition (inherited by all campaigns under this instance)
  spatialStructureConfig Json?

  /// Personal throughput definition: 4 Moves + seasons (inherited by all campaigns)
  personalThroughputConfig Json?

  /// Allyship domains configuration (inherited by all campaigns)
  allyshipDomainsConfig Json?
```

---

## 10. Implementation Checklist

### Phase 1 (Current)
- [x] Document inherited world properties (MTGOA_WORLD_INHERITANCE_REFERENCE.md)
- [x] Design schema structure (this document)
- [x] Decide on backward compatibility (deprecate old fields now)
- [x] Decide on inheritedWorld source (store in DB, not computed)
- [ ] **NEXT:** Update prisma/schema.prisma with Campaign JSON fields
- [ ] **NEXT:** Create Prisma migration: `npx prisma migrate dev --name add_campaign_inheritance_fields`
- [ ] **NEXT:** Write data migration script (old fields → JSON fields)
- [ ] **NEXT:** Generate Prisma Client: `npx prisma generate`
- [ ] **NEXT:** Add unit tests for JSON structure validation

### Phase 2
- [ ] Populate Instance model with inherited world config (magic_system, political_system, etc.)
- [ ] Update campaign creation logic to snapshot inheritedWorld from Instance
- [ ] Update API endpoints to read from JSON fields (not old text fields)
- [ ] Design and implement contextualization logic (inherited + flavor merge)
- [ ] Update campaign creation UI to populate JSON fields
- [ ] Build nation selection component with preview
- [ ] Test with 3-5 sample campaigns (end-to-end)

---

## 11. References

- **MTGOA_WORLD_INHERITANCE_REFERENCE.md** — What's inherited and customizable
- **MTGOA_CAMPAIGN_INHERITANCE_MODEL.md** — Architecture decision
- **bars-engine/prisma/schema.prisma** — Current schema
- **MTGOA_IMPLEMENTATION_ROADMAP.md** — Full 5-phase plan

---

**Next Step:** Apply schema changes and run migration.
