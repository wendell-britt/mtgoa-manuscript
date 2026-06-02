# SPEC: Reader-Facing Tools — Introduction Principles

**Purpose:** Define how the book introduces, scaffolds, and reinforces tools and practices that live inside the reader's allyship life — not just in their head.

**Why this matters:** The book teaches transformation, not information. A reader who knows about 3-2-1 but has never done it doesn't have a practice. A reader who has done it three times does. The book's job is to move readers from knowing to practicing. This spec defines the architectural rules that make that happen.

**Status:** APPROVED — 2026-04-22

---

## The Two Modes

Every moment in the book is in one of two modes. The transition between them must be signaled clearly.

| Mode | What it is | Reader posture | Text signal |
|------|------------|----------------|-------------|
| **Concept mode** | Explains, explores, narrates | Reading/reflecting | No explicit signal needed |
| **Practice mode** | Guided action, step-by-step | Doing | "Try this:" or explicit-entry transition |

**Explicit-entry rule:** When entering practice mode, the transition must be unmissable — a signal clear enough that a skimming reader knows to slow down. When exiting practice mode, signal the return to concept with a brief re-entry phrase ("Back to the chapter." or similar).

---

## The Three Introduction Phases

Every tool gets three phases of introduction across the book.

### Phase 1 — The Encounter

**Where:** First mention in a chapter. Never a full practice.

**What happens:** The reader encounters the tool as a concept — what it is, why it matters, when you'd use it. The encounter names the tool and gives the reader a reason to care, but does not teach the practice.

**Format:** Prose paragraph or a descriptive narrative that shows the tool in use (not a how-to). Can appear in any section (Exile, Distortion, Concept, Journey).

**Phase 1 rules:**
1. Never ask the reader to do the tool during Phase 1
2. Name the tool specifically — don't just describe it
3. Show the reader why they'd want it, not how to do it
4. Phase 1 encounter in one chapter means Phase 2 can appear in any later chapter

### Phase 2 — First Practice

**Where:** The chapter where the reader is first asked to do the tool.

**What happens:** A boxed exercise (bordered, indented, distinct typography from body prose) guides the reader through the tool for the first time. The exercise must be completable without re-reading surrounding prose.

**Format:** Boxed exercise with clear step numbers. Each step is a single action.

**Phase 2 rules:**
1. One new tool per chapter maximum — to prevent practice fatigue
2. The boxed exercise must be skimmable — a reader who skips it should still get the insight
3. After the boxed exercise, always include a "Now you know what it feels like" re-entry paragraph before returning to concept prose
4. Phase 2 first practice requires the tool's full EA channel to be confirmed (verified against canonical EA system)

### Phase 3 — The Reference

**Where:** Any section after Phase 2 is complete.

**What happens:** The tool is referenced as known — a brief acknowledgment that connects the tool to the current content, without re-teaching it. Use the "Now you've done this" shorthand when connecting to prior practice.

**Format:** Prose reference with one-line reminder of what the tool does. Never re-box the full exercise.

**Phase 3 rules:**
1. Reference assumes Phase 1 + Phase 2 complete
2. If connecting Phase 3 reference to a tool whose Phase 2 is in the same chapter, include a brief "you practiced this on page X" cross-reference

---

## Boxed Exercise Standards

A boxed exercise is valid only if:

1. **Skimmable:** The boxed text has a clear step structure — a reader who skips it still gets the insight
2. **Self-contained:** A reader who's never done the tool can complete it by following the boxed instructions alone
3. **Body-first:** The exercise asks the reader to do something, not just think about something
4. **Exit-reentry:** After the exercise, a re-entry paragraph returns the reader to concept mode

---

## Tool Inventory

**Hybrid Technique Academy inventory (authoritative 2026-05-24):** `TOOL_INVENTORY_HYBRID_2026-05-24.md` — supersedes table below until full sync.

| Tool | Type | First encounter chapter | Phase 1 status | Phase 2 status | Phase 3 status |
|------|------|------------------------|----------------|----------------|----------------|
| Token System (Bars-engine) | B | Ch0 | ✅ Complete | ❌ Missing | ❌ Missing Phase 3 refs |
| Ticket System | B | Ch0 | ✅ Complete | ❌ Missing | ❌ Missing Phase 3 refs |
| 3-2-1 Shadow Work | B | Ch2 catalog | 🔄 Compress per split spec | ❌ Ch3 pending | ❌ Missing |
| 8 Gates | B | Ch2 | ✅ Complete | ✅ Complete | 🔄 Needs Phase 3 refs |
| BARs | B | Ch1 | 🔄 Brief mention | ❌ No first practice format | ❌ Missing |
| Polarity Map | B | Ch2 catalog | 🔄 Compress per split spec | ❌ Ch4 encounter + Ch6 merge | ❌ Missing |
| Dojo Architecture | C | Ch3 | ❌ Missing | N/A | ❌ Missing |

---

## L1 / L2 Co-Dependent Model

**Decided 2026-04-22:** Writing and teaching-scaffold design are co-dependent tracks, not sequential phases.

| Level | What it is | Audience | Example |
|-------|-----------|----------|---------|
| **L1 — Draft production** | Writing chapters, hitting word counts, structural completeness | ICA reader | Editorial pipeline, word gap tracker |
| **L2 — Teaching scaffold** | Practice entry/exit signals, Phase 1/2/3 tool introductions, boxed exercises | ICA reader | This spec |
| **L3 — Author/editor workflow** | Reference tools used during drafting (EA Translator) | Author, editor | EA Translator spec |

**Core rule:** A chapter is only "complete" when both L1 and L2 are confirmed green. Word count is not a completion signal. L2 scaffold requirements must be defined in the chapter SPEC before L1 drafting begins.

---

## Companion Documents

- `SPEC_MANUSCRIPT_INTEGRATION.md` — Unit 2 (3-2-1), Unit 6 (Polarity Map), Unit 7 (Character Sheet) — where integration targets live
- `CHAPTER2_SHAMAN_FULL_DRAFT.md` — canonical Ch2, Section 5 (Journey to the Center), where 8 Gates live
- `GM_SECTION_DRAFT.md` — canonical Ch0, GM section draft

---

*Spec status: APPROVED — 2026-04-22*