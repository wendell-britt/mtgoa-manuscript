# MTGOA Implementation Roadmap

**Status**: Ready for implementation (campaign inheritance model)
**Created**: 2026-04-20
**Focus**: Additive layer model (GMs add flavor to inherited world)

---

## Phase 1: Core Infrastructure (Weeks 1–2)

### 1.1 Document Inherited World Properties
- [ ] **Spatial geography**: Formal inventory of BARs-engine world (room types, spatial instances, instance structure)
- [ ] **Nation profiles**: How 5 nations translate to campaign context (move styles, preferred quests, flavor modifiers)
- [ ] **Magic system reference**: How emotional alchemy appears in campaign setup (channel selection, WAVE progression in quests)
- [ ] **4 Moves reference**: Wake Up → Clean Up → Grow Up → Show Up in campaign context

**Deliverable**: `MTGOA_WORLD_INHERITANCE_REFERENCE.md` (campaign designers' reference to inherited properties)

### 1.2 Revise Campaign Storage Schema
- [ ] Update `Instance` or `Campaign` model to separate `inherited_world` from `campaign_flavor_layers`
- [ ] `inherited_world`: magic_system, political_system, spatial_structure, personal_throughput (read-only, inherit from parent)
- [ ] `campaign_flavor_layers`: allyship_domains, spatial_flavor, nation_flavor, real_world_context, game_world_flavor (customizable by GM)
- [ ] Verify nesting chain (Bruised Banana → MTGOA Org → Chapter → Campaign) preserves inheritance

**Deliverable**: Updated Prisma schema with explicit inherited vs. customized properties

---

## Phase 2: GM Setup UI (Weeks 2–3)

### 2.1 Simplify Campaign Creation Wizard
- [ ] **Step 1**: Campaign scope (name, chapter, domain focus, year focus) — 3 minutes
- [ ] **Step 2**: Spatial flavor (appearance, tone, NPCs, nation choice) — 7 minutes
- [ ] **Step 3 (Optional)**: Real-world context + game-world flavor — 5–10 minutes
- [ ] **Step 4**: Review & confirm — 2 minutes
- [ ] Total time: 15 minutes for required, 20+ for advanced

**Deliverable**: Updated campaign creation UI that guides GMs through 2 required + 2 optional questions

### 2.2 Nation Selection Component
- [ ] Dropdown: Select primary nation flavor (Argyra/Metal, Pyrakanth/Fire, Lamenth/Water, Meridia/Earth, Virelune/Wood)
- [ ] Show nation description (element, emotional channel, core theme, move style)
- [ ] Show how nation flavor influences quest generation

**Deliverable**: Nation selection UI with preview/description

### 2.3 Campaign Preview
- [ ] Show inherited properties (what's locked from world)
- [ ] Show customized properties (what GM added)
- [ ] Show sample prompt contextualized with both layers
- [ ] Let GM preview 2–3 prompts before confirming

**Deliverable**: Campaign preview screen showing inheritance + flavor layers

---

## Phase 3: Contextualization API (Weeks 3–4)

### 3.1 GET `/api/mtgoa/campaigns/:campaign_id/inherited-world`
- [ ] Return inherited properties from parent chain (Bruised Banana → MTGOA Org → Chapter)
- [ ] Include: magic_system, nations_available, spatial_structure, moves, allyship_domains
- [ ] Cache 24h (static data)

**Deliverable**: API endpoint for inherited world properties

### 3.2 GET `/api/mtgoa/campaigns/:campaign_id/contextualized-prompts`
- [ ] Return prompts contextualized with inherited + flavor layers
- [ ] Include: inherited_alchemy, flavor_contextualization, contextualized_version
- [ ] Support filtering by domain, intensity, nation
- [ ] Cache 1h (inherited properties are stable; flavor can change with BAR evolution)

**Deliverable**: Revised contextualization endpoint

### 3.3 POST `/api/mtgoa/campaigns/:campaign_id/generate-quest`
- [ ] Accept prompt + player state + campaign context (inherited + flavor)
- [ ] Pass inherited_alchemy (channel, nation, moves) to quest generation
- [ ] Apply flavor_contextualization (spatial detail, tone, guide lens voice)
- [ ] Return quest with full inheritance metadata

**Deliverable**: Quest generation with inheritance chain preserved

---

## Phase 4: Template Library & Examples (Week 4)

### 4.1 Pre-Written Campaign Flavor Templates
- [ ] **Template 1**: Coastal Island (Lamenth/Water, Gathering Resources focus)
- [ ] **Template 2**: Urban Organizing (Argyra/Metal, Skillful Organizing focus)
- [ ] **Template 3**: Land Stewardship (Virelune/Wood, Direct Action focus)
- [ ] **Template 4**: Community Education (Pyrakanth/Fire, Raising Awareness focus)

Each template includes:
- Spatial flavor description
- Nation choice + why
- Sample real-world context
- Sample game-world flavor
- Estimated setup time: "15 minutes, or customize further"

**Deliverable**: Template library in GM toolkit

### 4.2 Chapter 1 Demo
- [ ] Create one end-to-end campaign (Chapter 1 Coastal)
- [ ] Verify 4-level nesting works (Bruised Banana → MTGOA Org → Chapter 1 → Campaign flavor)
- [ ] Verify inheritance chain flows through quest generation
- [ ] Verify BAR tagging preserves full inheritance metadata
- [ ] Test with 3–5 actual prompts (gr_01, gr_02, ra_01, ra_02, etc.)

**Deliverable**: Working Chapter 1 demo with inheritance visible

---

## Phase 5: Advanced Features (Post-Implementation)

### 5.1 Forking Wizard (Full Worldbuilding Path)
- [ ] Detect when GM wants to "fork" (create parallel world)
- [ ] Guided wizard for full Foundations design (2+ hours)
- [ ] Create new `Instance` with custom inherited_world properties
- [ ] Show forking as explicit, advanced path (not default)

**Deliverable**: Forking workflow for advanced GMs

### 5.2 Campaign Variants
- [ ] Enable "inherit flavor from another campaign" (rapid iteration)
- [ ] GMs can fork a campaign's flavor layers, modify for new chapter
- [ ] Share flavor templates across teams

**Deliverable**: Multi-campaign flavor inheritance

---

## Data Flow Summary

```
Campaign Creation
├── Inherit: Bruised Banana world
│   └── Magic: Emotional Alchemy
│   └── Politics: 5 Nations
│   └── Geography: Spatial instances
│   └── Moves: Wake/Clean/Grow/Show
│
├── GM Customizes (15–20 min):
│   ├── Scope: domains, chapter, year focus
│   ├── Spatial Flavor: appearance, tone, NPCs
│   ├── Optional: Real-world context
│   └── Optional: Game-world flavor
│
└── Result: Campaign with full inheritance chain
    └── Used in quest generation
    └── Preserved in BAR tagging
    └── Rolled up to Chapter/Book milestones
```

---

## Testing Checklist

### Unit Tests
- [ ] Inheritance chain resolves correctly (follow nesting 4 levels down)
- [ ] Flavor layers merge with inherited properties without conflict
- [ ] Contextualized prompts include both inherited + flavor
- [ ] Nation selection updates move style modifiers
- [ ] Domain selection filters prompts correctly

### Integration Tests
- [ ] Campaign creation flow: required (10 min) + optional (5 min)
- [ ] Quest generation: inherited alchemy + flavor context applied
- [ ] BAR creation: campaign_ref + agent_metadata includes inheritance chain
- [ ] Milestone roll-up: Chapter 1 BAR → MTGOA Book milestone works

### User Tests (Chapter 1 Demo)
- [ ] First-time GM completes setup in 15 minutes
- [ ] GM feels world is "grounded" (not generic)
- [ ] Player plays 3 prompts, all feel contextualized
- [ ] Player creates BAR, sees inheritance chain in metadata

---

## Success Metrics

**Phase 1 Complete**:
- Inherited world properties documented
- Schema supports inherited vs. customized separation

**Phase 2 Complete**:
- Campaign creation reduced to 15 min (required) + 5 min (optional)
- GM preview shows inheritance + flavor clearly
- Nation selection updates prompt tone in real-time

**Phase 3 Complete**:
- Contextualized prompts include inherited alchemy + flavor
- Quest generation preserves inheritance chain
- BAR tagging shows full heritage

**Phase 4 Complete**:
- Chapter 1 demo runs end-to-end with inheritance visible
- 3–5 GMs successfully create campaigns using templates
- First-time GMs finish in 15 minutes

---

## References

- [MTGOA_CAMPAIGN_INHERITANCE_MODEL.md](MTGOA_CAMPAIGN_INHERITANCE_MODEL.md) — Architecture specification
- [MTGOA_GM_CONTEXTUALIZATION_SYSTEM.md](MTGOA_GM_CONTEXTUALIZATION_SYSTEM.md) — Revised system (15-min setup)
- [MTGOA_52CARDS_PROMPTS.json](MTGOA_52CARDS_PROMPTS.json) — Prompt data
- [bars-engine/docs/architecture/nation-move-profiles.md](../bars-engine/docs/architecture/nation-move-profiles.md) — Nation details
