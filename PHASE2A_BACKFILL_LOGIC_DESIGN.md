# Phase 2a.0: Backfill Logic Design

**Purpose:** Define how old Campaign fields map to new JSON fields during migration.

**Status:** Design phase (before implementation)
**Created:** 2026-04-20

---

## Overview

When backfill runs, for each campaign:
1. Read old fields: `allyshipDomain`, `wakeUpContent`, `showUpContent`, `questTemplateConfig`, `inviteConfig`
2. Transform into new JSON structure
3. Validate against schema
4. Write to `campaignFlavorLayers` JSON field
5. Log success/failure

**Principle:** Be conservative. If data is malformed or ambiguous, log it and skip the campaign (human review later).

---

## Field Mappings

### 1. allyshipDomain → campaignFlavorLayers.scope.allyship_domains

**Old field:** `allyshipDomain` (single text value)
```
GATHERING_RESOURCES | SKILLFUL_ORGANIZING | DIRECT_ACTION | RAISE_AWARENESS
```

**New field:** `campaignFlavorLayers.scope.allyship_domains` (array)
```json
{
  "scope": {
    "allyship_domains": ["GATHERING_RESOURCES"]  // Convert to array
  }
}
```

**Transformation logic:**
```typescript
function transformAllyshipDomain(oldValue: string | null): string[] | null {
  if (!oldValue || oldValue.trim() === '') return null;

  const valid = ['GATHERING_RESOURCES', 'SKILLFUL_ORGANIZING', 'DIRECT_ACTION', 'RAISE_AWARENESS'];
  if (!valid.includes(oldValue.trim())) {
    console.warn(`Invalid allyshipDomain: "${oldValue}". Skipping.`);
    return null;
  }

  return [oldValue.trim()];
}
```

**Validation:** Must be array of 1-4 items from the valid domains list.

---

### 2. wakeUpContent → campaignFlavorLayers.real_world_context.wake_up_message

**Old field:** `wakeUpContent` (text, up to 5KB)
```
"Players learn the story of why this movement matters..."
```

**New field:** `campaignFlavorLayers.real_world_context.wake_up_message` (text)
```json
{
  "real_world_context": {
    "wake_up_message": "Players learn the story of why this movement matters...",
    "actual_allyship_work": null,  // Populated from other source, not old field
    "real_world_outcome": null,
    "intended_action": null
  }
}
```

**Transformation logic:**
```typescript
function transformWakeUpContent(oldValue: string | null): string | null {
  if (!oldValue || oldValue.trim() === '') return null;
  return oldValue.trim();
}
```

**Validation:**
- Max 5KB (same as original)
- Must be non-empty if present

---

### 3. showUpContent → campaignFlavorLayers.real_world_context.show_up_message

**Old field:** `showUpContent` (text, up to 5KB)

**New field:** `campaignFlavorLayers.real_world_context.show_up_message` (text)

**Transformation logic:**
```typescript
function transformShowUpContent(oldValue: string | null): string | null {
  if (!oldValue || oldValue.trim() === '') return null;
  return oldValue.trim();
}
```

**Validation:** Same as wakeUpContent.

---

### 4. questTemplateConfig → campaignFlavorLayers.quest_generation

**Old field:** `questTemplateConfig` (JSON object)
```json
{
  "templateType": "starter_quest",
  "overrides": { "difficulty": "medium", "pace": "moderate" }
}
```

**New field:** `campaignFlavorLayers.quest_generation` (JSON object)
```json
{
  "quest_generation": {
    "templateType": "starter_quest",
    "overrides": { "difficulty": "medium", "pace": "moderate" },
    "createdFrom": "questTemplateConfig (old field)"  // Track origin
  }
}
```

**Transformation logic:**
```typescript
function transformQuestTemplateConfig(oldValue: any | null): object | null {
  if (!oldValue) return null;

  try {
    // Validate it's a valid object
    if (typeof oldValue !== 'object' || Array.isArray(oldValue)) {
      console.warn(`Invalid questTemplateConfig: not an object`);
      return null;
    }

    // Copy structure as-is
    return {
      ...oldValue,
      createdFrom: 'questTemplateConfig (old field)'
    };
  } catch (e) {
    console.warn(`Failed to transform questTemplateConfig: ${e.message}`);
    return null;
  }
}
```

**Validation:**
- Must be a JSON object (not array, not scalar)
- If it has `templateType`, must be a known type
- If it has `overrides`, must be a JSON object

---

### 5. inviteConfig → campaignFlavorLayers.invite_config

**Old field:** `inviteConfig` (JSON object)
```json
{
  "method": "public_link",
  "capacity": 50,
  "messaging": "Join our campaign"
}
```

**New field:** `campaignFlavorLayers.invite_config` (JSON object)
```json
{
  "invite_config": {
    "method": "public_link",
    "capacity": 50,
    "messaging": "Join our campaign"
  }
}
```

**Transformation logic:**
```typescript
function transformInviteConfig(oldValue: any | null): object | null {
  if (!oldValue) return null;

  try {
    if (typeof oldValue !== 'object' || Array.isArray(oldValue)) {
      console.warn(`Invalid inviteConfig: not an object`);
      return null;
    }

    // Validate known fields
    const validMethods = ['public_link', 'invite_only', 'custom'];
    if (oldValue.method && !validMethods.includes(oldValue.method)) {
      console.warn(`Invalid invite method: ${oldValue.method}`);
      return null;
    }

    if (oldValue.capacity && (typeof oldValue.capacity !== 'number' || oldValue.capacity < 0)) {
      console.warn(`Invalid invite capacity: ${oldValue.capacity}`);
      return null;
    }

    return oldValue;
  } catch (e) {
    console.warn(`Failed to transform inviteConfig: ${e.message}`);
    return null;
  }
}
```

**Validation:**
- Must be a JSON object (not array, not scalar)
- If it has `method`, must be one of: public_link, invite_only, custom
- If it has `capacity`, must be a positive integer

---

## Complete Campaign Transformation

**Input:** Old Campaign record
```sql
{
  id: "camp_123",
  slug: "coastal-gathering",
  allyshipDomain: "GATHERING_RESOURCES",
  wakeUpContent: "Learn about coastal communities...",
  showUpContent: "Help build resource networks...",
  questTemplateConfig: { templateType: "starter_quest" },
  inviteConfig: { method: "public_link", capacity: 100 },
  ...other fields...
}
```

**Transformation:**
```typescript
function transformCampaignToJSON(campaign: Campaign): {
  inheritedWorld?: object | null;
  campaignFlavorLayers?: object | null;
} {
  const flavorLayers: any = {};

  // Build scope
  const domains = transformAllyshipDomain(campaign.allyshipDomain);
  if (domains) {
    flavorLayers.scope = { allyship_domains: domains };
  }

  // Build real_world_context
  const wake = transformWakeUpContent(campaign.wakeUpContent);
  const show = transformShowUpContent(campaign.showUpContent);
  if (wake || show) {
    flavorLayers.real_world_context = {
      ...(wake && { wake_up_message: wake }),
      ...(show && { show_up_message: show }),
      actual_allyship_work: null,
      real_world_outcome: null,
      intended_action: null
    };
  }

  // Build quest_generation
  const questConfig = transformQuestTemplateConfig(campaign.questTemplateConfig);
  if (questConfig) {
    flavorLayers.quest_generation = questConfig;
  }

  // Build invite_config
  const inviteConfig = transformInviteConfig(campaign.inviteConfig);
  if (inviteConfig) {
    flavorLayers.invite_config = inviteConfig;
  }

  // Add metadata
  if (Object.keys(flavorLayers).length > 0) {
    flavorLayers.additional_metadata = {
      migrated_from: 'Phase 1 old fields',
      migrated_at: new Date().toISOString(),
      original_campaign_id: campaign.id
    };
  }

  return {
    inheritedWorld: null,  // Will be populated from Instance in Phase 2b
    campaignFlavorLayers: Object.keys(flavorLayers).length > 0 ? flavorLayers : null
  };
}
```

**Output:** New JSON fields
```json
{
  "inheritedWorld": null,  // Phase 2b will populate this
  "campaignFlavorLayers": {
    "scope": {
      "allyship_domains": ["GATHERING_RESOURCES"]
    },
    "real_world_context": {
      "wake_up_message": "Learn about coastal communities...",
      "show_up_message": "Help build resource networks...",
      "actual_allyship_work": null,
      "real_world_outcome": null,
      "intended_action": null
    },
    "quest_generation": {
      "templateType": "starter_quest",
      "createdFrom": "questTemplateConfig (old field)"
    },
    "invite_config": {
      "method": "public_link",
      "capacity": 100
    },
    "additional_metadata": {
      "migrated_from": "Phase 1 old fields",
      "migrated_at": "2026-04-20T20:15:00Z",
      "original_campaign_id": "camp_123"
    }
  }
}
```

---

## Error Handling

**Three categories of failures:**

### 1. Skip Campaign (Log as Warning)
- Malformed JSON in questTemplateConfig or inviteConfig
- Invalid allyshipDomain value (not in allowed list)
- Corrupted data that can't be parsed

**Action:** Log campaign ID + error message, don't write JSON field, move to next campaign.

### 2. Skip Field (Log as Info)
- Empty/null field (expected, common)
- Field exists but is empty string (edge case)

**Action:** Don't include that field in JSON, include other fields. Normal operation.

### 3. Data Quality Issue (Log as Info)
- Campaign has `questTemplateConfig` but no `allyshipDomain`
- Campaign has `inviteConfig` but missing `wakeUpContent`

**Action:** Still transform what we can, log the inconsistency for human review.

---

## Validation Schema

### campaignFlavorLayers JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "scope": {
      "type": "object",
      "properties": {
        "allyship_domains": {
          "type": "array",
          "items": { "enum": ["GATHERING_RESOURCES", "SKILLFUL_ORGANIZING", "DIRECT_ACTION", "RAISE_AWARENESS"] },
          "minItems": 1,
          "maxItems": 4
        }
      }
    },
    "real_world_context": {
      "type": "object",
      "properties": {
        "wake_up_message": { "type": "string", "maxLength": 5120 },
        "show_up_message": { "type": "string", "maxLength": 5120 },
        "actual_allyship_work": { "type": ["string", "null"] },
        "real_world_outcome": { "type": ["string", "null"] },
        "intended_action": { "type": ["string", "null"] }
      }
    },
    "quest_generation": { "type": "object" },
    "invite_config": { "type": "object" },
    "additional_metadata": { "type": "object" }
  },
  "additionalProperties": false
}
```

---

## Transformation Checklist

**For each campaign in the backfill:**
- [ ] Read old fields
- [ ] Call transformation functions
- [ ] Validate result against schema
- [ ] Write to `campaignFlavorLayers` if validation passes
- [ ] Log success (campaign ID, fields transformed)
- [ ] On error: log error (campaign ID, field, reason), skip campaign

**Post-backfill:**
- [ ] Count total campaigns processed
- [ ] Count successful transforms
- [ ] Count skipped/failed campaigns
- [ ] Count campaigns with incomplete transforms (some fields, not all)
- [ ] Report: match rate (old ≈ new) for sample of campaigns
- [ ] If match rate < 99%: investigate root cause, fix logic, retry

---

## Next Steps

1. **After data audit completes:** Use findings to refine transformation logic
2. **Before replica test:** Implement transformation functions (TypeScript or Python)
3. **Replica test phase:** Run backfill script on production copy, validate output

---

## References

- `PHASE2A_DATA_AUDIT_QUERIES.sql` — SQL queries to understand current data
- `PHASE2A_SAFE_MIGRATION_PLAN.md` — Full migration strategy
- `MTGOA_SCHEMA_UPDATE_PLAN.md` — Schema design
