# Mastering the Game of Friendcraft — General Project Spec (v0.1)

**Date:** 2026-04-20  
**Status:** Draft for alignment  
**Project family:** MTGOA -> Friendcraft -> BARs Engine

## 1) Project Intent

Build a coherent book-to-game system that helps players practice allyship and friendship as repeatable behavior, not inspiration-only content.

The system must preserve player agency through the BAR loop:
- Signal -> Meaning -> Action -> Consequence

## 2) What This Spec Solves

- Unifies scattered docs (MTGOA manuscript, Friendcraft ontology, bars-engine integration) into one operating spec.
- Defines clear build order so chapter writing and product implementation stay synchronized.
- Prevents ontology drift (same concepts named differently across book/game/docs).

## 3) Risks This Spec Must Prevent

- **Concept drift:** MTGOA terms vs Friendcraft terms diverge.
- **Framework collision:** e.g., dual WAVE definitions used without disambiguation.
- **Over-automation:** interpretation done by system instead of player meaning-making.
- **Write-first tech bias:** engine features built before manuscript mechanics are explicit.

## 4) Scope

### In scope (v1)
- Core practice system: Wake Up, Clean Up, Grow Up, Show Up.
- Six-face pedagogy and chapter architecture.
- Friendcraft ontology and state transitions for bonds/threads.
- BAR turn as canonical runtime and writing backbone.
- Spaced repetition scheduling for relational follow-through.
- Chapter-to-quest mapping for bars-engine prototype.

### Out of scope (v1)
- Full commercial launch operations.
- Large-scale multi-tenant social graph.
- Advanced predictive/recommendation AI that interprets meaning for the player.

## 5) Primary Artifacts

- **Book layer (source of truth for pedagogy):**
  - `/home/workspace/manuscripts/MTGOA_6FACE_CHAPTER_STRUCTURE.md`
  - `/home/workspace/manuscripts/MTGOA_BOOK_WORK_TRACKER.md`
  - Chapter drafts under `/home/workspace/manuscripts/chapters/`

- **Friendcraft system layer (source of truth for ontology):**
  - `/home/workspace/manuscripts/FRIENDCRAFT_V1_ONTOLOGY_SPEC.md`

- **Implementation layer (source of truth for runtime behavior):**
  - `/home/workspace/bars-engine/data/mtgoa_quest_map.json`
  - `/home/workspace/bars-engine/scripts/seed-mtgoa-spatial-world.ts`
  - `/home/workspace/bars-engine/docs/runbooks/BOOK_CYOA_MTGOA_CHAPTER1_DEMO.md`

## 6) Canonical Model

### 6.1 Pedagogy model
- 6 Faces are the developmental arc.
- Each chapter must include:
  - thesis
  - shadow if skipped
  - 3-5 named moves
  - shadow demonstration
  - BAR prompts
  - bridge to next face

### 6.2 Runtime model
- A **BAR Turn** is the minimum unit of progress.
- A turn is invalid without concrete action.
- Consequence logging is mandatory even on miss/failure.

### 6.3 Friendcraft model
- Entity backbone: Player, Bond, Third Body (Fred), Daemon, Move, BAR Turn, Campaign.
- Bond states: Dormant, Active, Drifting, Strained, Renewing.
- Daemon severity escalates on repeated misses and unresolved friction.

## 7) Integration Contract (Book <-> Engine)

Each chapter should map to playable constructs:
- Chapter thesis -> campaign objective
- Named move -> prompt card / quest action
- Shadow scenario -> failure state / daemon trigger
- BAR prompts -> in-game reflection nodes
- Connecting quest -> spoke transition criteria

Definition of done for each chapter integration:
1. Chapter draft complete in manuscripts.
2. Minimum 3 named moves represented in quest system.
3. At least 1 shadow/failure path represented.
4. BAR loop verifiably executable in prototype flow.

## 8) Decision Log (Current)

- Keep WU/CU/GU/SU invariant across MTGOA and Friendcraft.
- Treat BAR as canonical mechanic for both text and software.
- Keep interpretation assistive, never authoritative.
- Prioritize missing manuscript mechanics before broad new feature expansion.

- [2026-04-20] Canon locked: Use nested+suffix disambiguation for WAVE.
  - `WAVE-Spiral` = Wake Up -> Clean Up -> Grow Up -> Show Up (macro practice loop).
  - `WAVE-Somatic` = Welcome -> Acknowledge -> Validate -> Exhale (micro regulation protocol).
  - Rule: `WAVE-Somatic` runs inside the Wake Up stage whenever regulation is needed before interpretation/action.
  - Naming convention in manuscript and engine docs must always include suffix on first mention per section.

## 9) Open Decisions to Resolve Next

1. Where 5 emotional channels live (standalone chapter vs per-face embedding).
2. Placement of “works-inspired quests” (appendix vs companion workbook).
3. Degree of explicit I Ching layer in core manuscript.

## 10) Execution Plan (Now)

### Phase A: Canon lock
- Freeze terminology for WAVE and emotional-channel placement.
- Publish v1 glossary in manuscripts and bars-engine.

### Phase B: Manuscript completion
- Complete remaining face chapters with mechanical parity.
- Ensure every chapter has operational moves, not concept-only prose.

### Phase C: Playable mapping
- Map each chapter to spoke quest artifacts and BAR nodes.
- Validate player can run at least one full turn per major move family.

### Phase D: QA + launch prep
- Consistency audit (terms, ontology, chapter contracts, quest contracts).
- Produce release candidate for reader-playtester loop.

## 11) Immediate Next 3 Actions

1. **Close manuscript gap:** write/add the missing 5 Emotional Channels mechanics section.
2. **Bridge proof:** create one end-to-end chapter contract doc (chapter -> moves -> quests -> BAR checks) and test it in bars-engine.
3. **Propagation pass:** apply canonical WAVE naming across active chapter drafts and runbooks.

## 12) Build Strategy Recommendation

- **Core system:** Build custom.
  - Solves: preserves your specific pedagogy and transformation model.
  - Risks breaking: speed of shipping if over-engineered early.
- **Scheduling/infrastructure:** Integrate where possible.
  - Solves: reduces rebuild cost for reminders and repeat cadence.
  - Risks breaking: coherence if external tools define core semantics.
- **Advanced personalization AI:** Defer.
  - Solves: avoids premature complexity and agency loss.
  - Risks breaking: none near-term; protects model integrity.

---

## Resume Brief (Current Snapshot)

- Documentation exists and is substantial across manuscripts + bars-engine.
- Friendcraft ontology is drafted and usable as a v1 base model.
- MTGOA chapter framework is defined; several chapters drafted, some still pending.
- Primary blockers are taxonomy alignment and missing mechanics propagation.
- The project is ready for a canonical-spec pass and then chapter-to-engine contract execution.