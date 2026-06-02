# SPEC: Tool Placement Rules — Book Architecture
## Where Each Tool Lives and Why

**Purpose:** Determine where every tool in MTGOA goes — book body, appendix, or workbook — so editorial passes don't make placement decisions ad hoc.
**Source:** Integration session 2026-04-22, 6 GM Face analysis
**Status:** READY TO USE — canonical reference for all chapter editorial passes
**Companion:** `SPEC_EMOTIONAL_ALCHEMY_TRANSLATOR.md`, `SPEC_WORKBOOK_SCOPE.md` (to be written)

---

## The Revenue Architecture

```
Book (front-end product)
  ↓ demonstrates tool + raises ICA level
  ↓ inspires practice hunger
  ↓ creates desire for structure
Workbook (upsell)
  ↓ provides practice infrastructure
  ↓ deepens what the book introduced
  ↓ enables real mastery
  ↓ creates desire for coaching/$$$
Coaching (backend product)
```

The book makes readers curious about practice. The workbook gives them a structure to practice in. The coaching gives them a guide who has already walked the path. The revenue flows from this sequence — not the other way around.

**Rule:** The book must be complete without the workbook. The workbook must be comprehensible without the book. They are two different products with two different jobs.

---

## The Four Placement Zones

Each tool in MTGOA goes into exactly one of four zones:

| Zone | Location | Job | What lives here |
|------|----------|-----|-----------------|
| **Alpha** | Book body | Teaches the concept and gives one example | Core framework concepts, first introductions of each tool |
| **Beta** | Book body | Gives the reader a single concrete application | Practice moments, chapter-end exercises, in-text challenges |
| **Gamma** | Appendix | Full reference + cross-reference map | Deep tools, multi-step practices, tools with sub-components |
| **Delta** | Workbook | Practice structure + repetition scaffolding | Any tool requiring repeated application over time, journaling, multi-session work |

A tool may appear in multiple zones across its lifecycle (e.g., 3-2-1: Alpha teaches it exists, Gamma has the full process, Delta has the practice log). Never repeat the full content in multiple zones — cross-reference instead.

---

## Placement Decision Rules

### Rule 1: Time Required

| Time to use | Placement |
|-------------|-----------|
| Under 2 minutes (in-conversation) | Alpha or Beta only |
| 5-20 minutes (standalone practice) | Gamma reference + Beta example |
| 20+ minutes or multi-session | Delta (workbook) |

### Rule 2: Scaffold Dependency

| If the tool needs... | Then it goes to... |
|----------------------|--------------------|
| No scaffold (self-contained) | Alpha + Beta only |
| Repeated application to work | Delta (workbook) |
| A reference sheet to use correctly | Gamma (appendix) |
| A partner, facilitator, or guide | Coaching territory (not in this product) |

**The 3-2-1 example (updated 2026-05-24):** Requires 20+ minutes for full process. **Hybrid:** Ch2 Phase 1 catalog only; Ch3 Phase 2 first practice; Gamma appendix full process; Delta workbook log. Ch2 sidebar-in-Gates pattern **superseded** by Technique Academy routing.

**Polarity Map (updated 2026-05-24):** Ch2 Phase 1 catalog; Ch4 short encounter (Honor↔Reform); Ch6 merged practice (Care↔Impact + Close with Honest Terms). Full examples in appendix. See `POLARITY_PHASE2_SPLIT_SPEC.md`.

**The WAVE-Somatic example:** 4 steps, 10 seconds, in-conversation. Decision: Alpha teaches it (Ch2 concept), Beta gives one example (10-Second WAVE scenario). No Gamma needed. No Delta needed.

### Rule 3: Depth vs. Breadth

If a tool is **needed to understand the next chapter**, it goes in Alpha (book body) at the point of first use. If a tool is **useful but not blocking**, it goes in Gamma (appendix) with a cross-reference note in the book.

**The Dojo example:** Reader needs to know what a dojo is before Ch3. Decision: One paragraph in Ch3 body (Alpha/beta placement), full dojo descriptions in Gamma (appendix reference).

### Rule 4: Revenue Logic

If the tool is the **primary reason someone would buy the workbook**, it goes in Delta (workbook) with a book-body teaser. If it belongs in the book for conceptual completeness, it goes there — not in the workbook to artificially drive sales.

**The BARs loop example:** The BARs loop is the book's practice unit — one per chapter, in the book body. The full BARs practice journal (daily logging, weekly review, 52-week cycle) goes in the Delta workbook. The book demonstrates the tool. The workbook provides the infrastructure to practice it long-term.

### Rule 5: ICA Reader Level

At ICA reader level (pre-engagement, pre-Coaching), a reader can:
- Do a 2-minute tool without supervision
- Follow written instructions for a 20-minute tool if the steps are clear
- Not reliably do complex shadow work alone without grounding

This means: Alpha + Beta are ICA-reader-safe. Gamma is ICA-reader-accessible with effort. Delta is ICA-reader-optimized (workbook guides them through the harder stuff with structure they cannot yet design themselves).

---

## The Tool Inventory

### Framing Devices (not tools — book structure)
These are structural concepts that organize the book. They are not practice tools. They live in the book body, fully explained, with no appendix or workbook presence.

| Framing Device | Zone | Reasoning |
|---------------|------|-----------|
| **Token System** | Alpha (book body) | Core metaphor — teaches resource awareness. Fully in Ch0. |
| **Ticket System** | Alpha (book body) | Core metaphor — teaches reward structure. Fully in Ch0. |
| **Three Game Types** | Alpha (book body) | Core framework — teaches game structure. Fully in Ch0. |
| **Six Faces (mentor-guides)** | Alpha (book body) | Core structure — organizes entire book. Each chapter has one. |

### Tools (practice elements)

| Tool | Zone(s) | Reasoning |
|------|---------|-----------|
| **Character Sheet** | Beta (book body) | One exercise, in Ch0 |
| **WAVE-Spiral** | Alpha + Beta (book body) | **HIGHEST PRIORITY.** Core process. Taught in Ch2. Every chapter references it. |
| **WAVE-Somatic** | Alpha + Beta (book body) | **HIGHEST PRIORITY.** In-conversation tool, 10 seconds. In Ch2. |
| **5 Emotional Channels** | Alpha (book body) | Core framework — named in Ch2 |
| **Transcend moves** | Beta (book body) | One example per channel in Ch2 |
| **8 Gates** | Alpha (book body) + Gamma (appendix) | Core concept in Ch2; full map in appendix |
| **3-2-1 Shadow Process** | Ch2 Phase 1 catalog + Ch3 Phase 2 practice + Gamma (appendix) + Delta (workbook) | **Hybrid Technique Academy (2026-05-24):** Ch2 names + routes; Ch3 first sit-down; full process in appendix |
| **BARs loop** | Beta (book body) | One per chapter, book demonstrates the cycle |
| **BARs practice journal** | Delta (workbook) | Long-term logging, weekly review, 52-week cycle |
| **Dojo Architecture** | Alpha (book body) + Gamma (appendix) | One paragraph in Ch3; full descriptions in appendix |
| **Polarity Map** | Ch2 Phase 1 catalog + Ch4 Phase 1.5 encounter + Ch6 Phase 2 practice + Gamma (appendix) | **Split (2026-05-24):** Honor↔Reform (Ch4), Care↔Impact merged with Close (Ch6). Spec: `POLARITY_PHASE2_SPLIT_SPEC.md` |
| **W.A.V.E.** | Gamma (appendix) | Reference only; fully taught in Igniting Joy. MTGOA references it by name only. |
| **Happy Apples** | Gamma (appendix) | Reference; Igniting Joy brand territory. Not MTGOA content. |
| **Comedic Archetypes** | Not in MTGOA | Igniting Joy + future comedy books only. Remove from this inventory. |

### Tools by placement zone

**Alpha + Beta (book body — highest priority):**
- **WAVE-Spiral** — taught in Ch2, referenced throughout all chapters
- **WAVE-Somatic** — taught in Ch2, used in every chapter
- 5 Emotional Channels
- Transcend moves (one per channel)
- Character Sheet
- 8 Gates (concept)
- Dojo Architecture (one paragraph)
- BARs loop (one per chapter)

**Gamma (appendix — reference layer):**
- 3-2-1 Shadow Process (full process)
- 8 Gates (full map, all 8 gates + prompts)
- W.A.V.E. (reference — Igniting Joy brand)
- Dojo Architecture (full descriptions of all 4 dojos)
- BARs Reference Sheet

**Delta (workbook — practice infrastructure):**
- 3-2-1 Shadow Process (practice log, multi-session scaffolding)
- BARs practice journal (daily log, weekly review, 52-week cycle)
- 8 Gates walk (multi-session journal for the forest walk)
- Dojo selection + commitment log
- Character Sheet (updated each quarter)
- Emotional Alchemy practice cards (52-card system, adapted from Igniting Joy)

---

## Cross-Reference Protocol

When a tool appears in the book body, include:
1. A one-line description of what it is
2. A cross-reference to where it lives in Gamma ("For the full process, see Appendix: [Tool Name]")
3. A Beta moment (the reader does something with it right now)

**Format for in-book cross-reference:**
> "You've just met the 3-2-1 — a way to find your shadow before it finds you. The full process is in the Appendix. For now, try this: [Beta example]."

**Format for appendix cross-reference:**
> "**[Tool Name]** (first introduced Ch.X)
> See Book Ch.X for the concept. The full process follows."

---

## Appendix Structure (Gamma)

```
Appendix A: Shadow Work
  - 3-2-1 Shadow Process (full)
  - 8 Gates Full Map (all 8 gates + prompts)

Appendix B: Emotional Practice
  - 5 Channels + Transcend Moves (quick reference)
  - W.A.V.E. (reference — Igniting Joy brand)

Appendix C: Structural Tools
  - Dojo Architecture (all 4 dojos, full descriptions)
  - BARs Reference Sheet

Appendix D: Game Mechanics
  - (Token, Ticket, Three Game Types are fully in Ch0 — no appendix needed)
```

**Removed from Appendix:** Comedic Archetypes, Happy Apples — these are Igniting Joy territory.

---

## What the Appendix Is NOT

- Not a second book
- Not a place to teach concepts — only to reference them
- Not where a reader goes first — they come here after the book shows them something
- Not searchable like a glossary — organized by the sequence of the book's discovery

---

## What the Workbook Is NOT

- Not a supplement to the book — a different product with a different job
- Not where concepts are first taught — ever
- Not a place to read — a place to practice

---

## Spec Dependencies

| Spec | Status | What it needs from this spec |
|------|--------|------------------------------|
| `SPEC_WORKBOOK_SCOPE.md` | TODO | Delta tool list, zone assignments |
| `SPEC_MANUSCRIPT_INTEGRATION.md` | DONE | Placement rules applied per unit |
| `SPEC_EMOTIONAL_ALCHEMY_TRANSLATOR.md` | DONE | Translator for Beta writing |
| Chapter editorial passes | TODO | Reference this spec before placing any tool |

---

**Spec status:** READY TO USE
**Created:** 2026-04-22
**Owner:** Wendell Britt
**Next action:** Write `SPEC_WORKBOOK_SCOPE.md` using Delta tool list as input