# MTGOA Campaign Inheritance Model

**Status**: Design (addressing user feedback on campaign architecture)
**Created**: 2026-04-20
**Purpose**: Position MTGOA campaigns as additive layers on the existing BARs-engine world, not standalone worldbuilding efforts

---

## The Insight

The BARs-engine world was not consciously designed through Foundations, but it IS already a complete Foundations implementation:

- **Magic system** = Emotional Alchemy (intrinsic, not added)
- **Geography** = Spatial rooms/instances (existing)
- **Politics** = Movement through Nations (Argyra, Pyrakanth, Lamenth, Meridia, Virelune)
- **Social structures** = Nation cultures of practice

**Implication**: GMs don't need to define a complete new world. They inherit the base world and add campaign-specific context layers.

---

## Existing Foundations in BARs-Engine

### 1. MAGIC (Emotional Alchemy)
The magic system IS emotional alchemy:
- 5 channels/elements: Metal (Fear), Fire (Anger), Water (Sadness), Earth (Neutrality), Wood (Joy)
- Nations mapped to channels: Argyra (Metal), Pyrakanth (Fire), Lamenth (Water), Meridia (Earth), Virelune (Wood)
- Movement through emotions IS the power system
- Vibeulons (inspiration currency) flow from emotional transformation

**Locked for nested campaigns**: GMs cannot redefine the magic system. Emotional alchemy is universal to the world.

### 2. POLITICS (Nations & Movement)
5 distinct nations represent "cultures of practice":

| Nation | Element | Channel | Core Theme |
|--------|---------|---------|------------|
| **Argyra** | Metal | Fear → Clarity | Discernment, boundaries, truth |
| **Pyrakanth** | Fire | Anger → Power | Will, courage, decisive action |
| **Lamenth** | Water | Sadness → Depth | Grief, memory, emotional integration |
| **Meridia** | Earth | Neutrality | Whole-system perspective |
| **Virelune** | Wood | Joy | Vitality, growth, generative action |

Nations are NOT isolated; players move BETWEEN them. Politics = the pattern of how characters/factions distribute influence across nations.

**Customizable for nested campaigns**: GMs can add faction relationships, power dynamics within nations, but not redefine the nations themselves.

### 3. GEOGRAPHY (Spatial Instances)
Rooms, clearings, and traversable spaces:
- Bruised Banana (residency world)
- MTGOA Organization (spatial clearing)
- Chapter 1-12 spaces (nested within MTGOA)
- Future: player-created home spaces

Rooms have:
- Twee passages (flavor text)
- NPC presences (6 Game Master faces + others)
- Quest anchors (where prompts manifest)
- State persistence (World State Provider tracks carrying/selected state)

**Customizable for nested campaigns**: GMs define what a chapter space LOOKS and FEELS like, which NPCs are present, what's available there. But they don't invent new spatial layers—they use the existing instance/room structure.

### 4. PERSONAL THROUGHPUT (4 Moves)
The system for how players get things done:

- **Wake Up** (Spring): See more; orientation; recognition phase
- **Clean Up** (Winter): Unblock; clarify emotional energy; deepening phase
- **Grow Up** (Summer): Increase capacity; develop skills; growth phase
- **Show Up** (Fall): Do the work; take action; commitment phase

**Locked for nested campaigns**: These moves are universal. MTGOA campaigns use them; they don't redefine them.

### 5. ALLYSHIP DOMAINS (WHERE)
Implicit in the world but not yet formally named:

- Gathering Resources (primary for Recognition phase)
- Skillful Organizing (primary for Deepening phase)
- Direct Action (primary for Commitment phase)
- Raising Awareness (secondary/cross-cutting)

**Explicit in MTGOA 52-card deck**: Each prompt has a domain. GMs select which domains their campaign emphasizes.

---

## What GMs DO Define (Campaign Additive Layers)

When a GM creates an MTGOA campaign, they inherit the 5-nation world and add:

### Layer 1: Campaign Scope
- Which allyship domains this campaign emphasizes
- Which chapter(s) from MTGOA book
- How long (cycles, year focus)

### Layer 2: Spatial Flavor
- What does Chapter 1's clearing LOOK like in this campaign?
- Which NPCs are present as guides?
- What's the tone (urgent? celebratory? quiet? confrontational?)?
- Which nation feels most present in this space?

### Layer 3: Campaign-Specific Context (Optional)
- Real-world context: What actual allyship work are players doing?
- Game-world flavor: How does that translate to this chapter's imagined space?

**Key difference from previous design**: GMs are NOT defining Geography/Social/History/Magic from scratch. They're answering: "In THIS chapter, with THIS nation's flavor, focused on THIS allyship work, what does the inherited world offer us?"

---

## Example: Coastal Campaign

### What's INHERITED (Locked)
- **Magic**: Emotional alchemy (Water channel prominent because player's emotional work involves sadness/grief)
- **Politics**: 5 nations exist; if players encounter NPCs, they come from one of these nations
- **Geography**: Chapter 1 is a spatial clearing within MTGOA Organization within Bruised Banana
- **Moves**: Wake Up → Clean Up → Grow Up → Show Up progression

### What GM ADDS (Campaign Layer)
- **Allyship Focus**: Gathering Resources + Raising Awareness domains
- **Spatial Flavor**: Chapter clearing is "three springs by the shore" — visual distinct from other chapters
- **NPCs**: Sage (elder who remembers ceremony) + Diplomat (young merchant questioning traditions)
- **Real Context**: Players are actual community members dealing with water access scarcity
- **Game-World Flavor**: Springs are sacred, spirits guard the wells, merchants control trade
- **Tone**: Grief + resilience (Water channel + recognition of enduring knowledge)

**Result**: Players play in the inherited BARs-engine world, navigating the 5 nations' emotional ecosystems, but GROUNDED in THIS campaign's specific spatial and thematic context.

---

## Nested Campaign Architecture

```
Bruised Banana (base world)
  └── Instance: bruised-banana
        └── Spatial clearing(s)
        └── Politics: Nation influence distribution
        └── Magic: Emotional Alchemy (global)

MTGOA Organization (sub-world)
  └── Instance: mtgoa-org
        └── Book/Game hub spatial clearing

Chapter 1 Campaign (nested campaign)
  └── Instance: mtgoa-chapter-1
        └── Spatial clearing(s) [GM adds flavor]
        └── Campaign context [optional: real + game layers]
        └── Prompts: gr_01-13, ra_01-13 (inherited from 52-card deck)
        └── Inheritance: All base world properties flow down
```

**BAR Continuity**: When a player creates a BAR in Chapter 1:
```json
{
  "campaignRef": "mtgoa-chapter-1",
  "agentMetadata": {
    "chapterRef": "mtgoa-chapter-1",
    "bookRef": "mtgoa-book",
    "orgRef": "mtgoa-org",
    "parentCampaignRef": "bruised-banana"
  },
  "world_inheritance": {
    "nations_available": ["Argyra", "Pyrakanth", "Lamenth", "Meridia", "Virelune"],
    "magic_system": "emotional_alchemy",
    "spatial_context": "chapter-1-clearing"
  }
}
```

---

## GM Setup Complexity

### If NOT Forking (Using Inherited World)
**Time**: 15–20 minutes
**Question Set**:
1. Which allyship domains?
2. What's the spatial flavor of this chapter?
3. (Optional) What real-world context?
4. (Optional) What game-world tone?

**Result**: Prompts are automatically contextualized with inherited world + campaign layer.

### If Forking (Creating Parallel World)
**Time**: 2+ hours
**Question Set**: Full Foundations from scratch
- New magic system? (or inherit emotional alchemy)
- New nations/cultures? (or reinterpret existing nations)
- New geography? (or use inherited spaces)
- New history? (or extend existing lore)

**This is World Destruction / Full Fork** — not common, but possible for radical departures (e.g., "What if this campaign exists in a fully different world?").

---

## Implementation Impact

### What Changes in GM Contextualization System
1. **Reframe as "Campaign Layer" not "Full World"** — GMs inherit magic, politics, geography
2. **Simplify setup** — 4 optional questions, not 4 required Foundations questions
3. **Remove worldbuilding friction complexity** — No "destroy the world" unless truly forking
4. **Add nation selection** — GMs choose which nation(s) flavor their campaign
5. **Show inheritance chain** — GMs see what they inherit from Bruised Banana → MTGOA Org → base world

### What Stays the Same
- Emotional alchemy translator (same system)
- 52-card deck prompts (same)
- 4 moves / seasonal alignment (same)
- Quest generation with worldbuilding hooks (same)
- BAR tagging and milestone roll-up (same)

### What Simplifies
- **No multi-layer translation mapping** — Base world is already real + imagined
- **No complex prompt editing** — GMs accept inherited context, add campaign flavor
- **No "world destruction" unless actually forking** — Simpler mental model for most GMs

---

## Testing Against Existing World

### Verification: Map Existing World to Foundations

**Magic**: ✅ Emotional Alchemy fully implemented
- 5 channels (Metal, Fire, Water, Earth, Wood)
- 15 canonical moves
- WAVE progression
- Vibeulons economy

**Politics**: ✅ Nations = cultures of practice fully implemented
- 5 distinct nations with move profiles
- Movement between nations is how characters transform
- Nation preference shapes quest flavor

**Geography**: ⚠️ Implicit in spatial system
- Rooms/clearings exist (Bruised Banana, MTGOA Organization, Chapters)
- Spatial state tracked (World State Provider)
- Traversal mechanics working
- *Needs formal documentation of spatial ontology*

**Personal Throughput**: ✅ 4 moves fully implemented
- Wake Up, Clean Up, Grow Up, Show Up
- Tied to seasonal progression
- Quest generation respects move development

**Allyship Domains**: ⚠️ Implied but not formally named in world
- 4 domains exist (Gathering, Organizing, Action, Awareness)
- MTGOA 52-card deck makes them explicit
- *Could document in world lore why these domains matter*

---

## Next Steps

1. **Revise GM Contextualization System** to position as "additive layer" model
2. **Document spatial geography** formally (what exists in world)
3. **Add nation selection** to campaign setup
4. **Simplify setup questions** from 4 required to optional flavor questions
5. **Test with Chapter 1 demo** — show inheritance chain working

---

## References

- [MTGOA_GM_CONTEXTUALIZATION_SYSTEM.md](MTGOA_GM_CONTEXTUALIZATION_SYSTEM.md) — Current version (to be revised)
- [bars-engine/FOUNDATIONS.md](../bars-engine/FOUNDATIONS.md) — Five dimensions
- [bars-engine/docs/architecture/nation-move-profiles.md](../bars-engine/docs/architecture/nation-move-profiles.md) — Nations & channels
- [bars-engine/docs/BRUISED_BANANA_HOUSE_INSTANCE.md](../bars-engine/docs/BRUISED_BANANA_HOUSE_INSTANCE.md) — Spatial instances
