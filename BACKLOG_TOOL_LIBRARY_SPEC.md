# BACKLOG ITEM — Tool Library Spec
## Source: Integration Session 2026-04-22

---

**Status:** BACKLOG
**Type:** Editorial Infrastructure
**Owner:** Council / Wendell
**Priority:** P1 — needed before next editorial pass
**Estimated effort:** Medium (1–2 sessions to spec, 1 session to populate initial tools)

---

## The Ask

Create `SPEC_TOOL_LIBRARY.md` — a master reference document for every tool across the Britt publishing ecosystem (MTGOA, Igniting Joy, future books).

This spec serves three purposes:
1. **Editorial pass checklist** — when integrating tools from legacy sources into MTGOA, the library tells us which tools exist, where they live, and whether they're novel or adapted
2. **Cross-book consistency** — tools that appear in multiple books (BARs, WAVE, 3-2-1) have a single source of truth for their definition and protocol
3. **Future book foundation** — new books can draw from the library instead of inventing tools from scratch

---

## Known Tools (Incomplete List — Populate in Spec)

### From Igniting Joy (Wendell's, 2024)

| Tool | Category | Novel to IJ? | MTGOA Status |
|------|----------|-------------|--------------|
| W.A.V.E. (Welcome, Acknowledge, Validate, Engage/Exhale) | A — Somatic | Novel | ⚠️ Name collision with WAVE-Spiral. IJ version is micro (10-second regulation). MTGOA's is macro (Wake/Clean/Grow/Show). Different tools, same acronym. |
| Happy Apples | A — Somatic | Novel | Not in MTGOA |
| 3-2-1 Shadow Process | B — Reflection | Novel | ⚠️ In TEAL, not in canonical MTGOA. Integration gap identified. |
| Comedic Archetypes (Clown, Jerk, Cult Leader) | C — Conceptual | Novel | Not in MTGOA |
| Truth + Pain + Perspective (comedy model) | C — Conceptual | Novel | Not in MTGOA |
| Two-Deck System (standard 52 + blank BARs) | D — Operational | Novel | Partial — BARs in MTGOA, 52-card deck not present |
| Standard 52-Card Suit Structure | D — Operational | Novel | Not in MTGOA |
| BARs (Breakthrough, Action, Reflection, sustain) | B — Reflection | IJ origin | ⚠️ MTGOA has BARs, IJ has BARs — same acronym, different density and format |

### From MTGOA Canonical

| Tool | Category | Novel to MTGOA? | Status in MTGOA |
|------|----------|----------------|----------------|
| Token System | D — Operational | Novel | Ch0 complete |
| Ticket System | D — Operational | Novel | Ch0 complete |
| Character Sheet | B — Reflection | Novel | Ch0 draft complete |
| Three Game Types | C — Conceptual | Novel | Ch0 complete |
| GM Framing | C — Conceptual | Novel | Ch0 draft complete |
| WAVE-Spiral (Wake/Clean/Grow/Show) | C — Conceptual | Novel | Ch1–Ch2+ complete |
| WAVE-Somatic (micro regulation) | A — Somatic | Novel | Not written — distinct from WAVE-Spiral |
| 5 Emotional Channels (Metal/Water/Wood/Fire/Earth) | C — Conceptual | Novel | Ch2+ complete |
| 8 Gates | B — Reflection | Novel | Ch2 complete |
| BARs (Breakthrough/Action/Reflection/sustain) | B — Reflection | IJ-origin | Ch1+ brief mentions |
| Polarity Map | B — Reflection | TEAL-origin | Not in canonical |
| 3-2-1 Shadow Work | B — Reflection | TEAL-origin | Not in canonical |

### From TEAL (Integration Sources)

| Tool | Category | Source | MTGOA Status |
|------|----------|--------|--------------|
| 3-2-1 Shadow Work | B — Reflection | TEAL | Integration gap — Unit 2 |
| Polarity Map | B — Reflection | TEAL | Integration gap — Unit 6 |
| Dojo Architecture | C — Conceptual | Nov/Jan | Integration gap — Unit 3 |

---

## Spec Structure (Proposed)

```
SPEC_TOOL_LIBRARY.md
├── Purpose & Usage
├── Tool Taxonomy (A/B/C/D categories from SPEC_TOOL_INTRODUCTION)
├── Tool Entry Template
│   ├── Name + aliases
│   ├── Origin (book, source, date)
│   ├── Category
│   ├── Core protocol (step-by-step)
│   ├── Variants
│   ├── MTGOA status (absent / partial / complete)
│   ├── Editorial recommendation (integrate / adapt / keep separate)
│   └── Cross-references
├── Tool Entries (one per tool)
├── Name Collision Register (WAVE vs W.A.V.E., etc.)
└── Backlog: Tools Not Yet Written
```

---

## Tool Entry Template

```markdown
## [TOOL NAME]

**Aliases:** [other names it goes by]
**Origin:** [book / source / date]
**Category:** [A — Somatic | B — Reflection | C — Conceptual | D — Operational]
**MTGOA Status:** [Absent | Partial | Complete | Name Collision]
**Editorial Recommendation:** [Integrate into MTGOA | Keep separate | Adapt for MTGOA | New for MTGOA]

### What it is
[2–3 sentence description]

### Core Protocol
[Step-by-step for the tool's use]

### Variants
[Any known versions]

### Relationship to Other Tools
[Cross-references]

### Notes
[Editorial notes, name collisions, open questions]
```

---

## Key Decisions Needed Before Spec Is Written

1. **WAVE vs W.A.V.E. naming** — IJ uses W.A.V.E. (micro regulation), MTGOA uses WAVE-Spiral (macro development). The collision is real. Options: rename IJ's tool, rename MTGOA's, use suffix disambiguation throughout. Decision needed before spec is written.

2. **BARs as single framework or two variants** — IJ BARs (journaling cards) vs MTGOA BARs (validation checkpoints). Same acronym, different format and density. Decision: one framework with two formats, or two named tools that share the BARs lineage?

3. **3-2-1 Shadow Process vs 3-2-1 Shadow Work** — IJ and TEAL both have 3-2-1 but with different emphases. Spec should capture both and note the difference.

---

## Companion Documents

- `SPEC_TOOL_INTRODUCTION.md` — tool introduction protocol (Category A/B/C/D, three phases, signal language)
- `SPEC_MANUSCRIPT_INTEGRATION.md` — Unit 2 (3-2-1), Unit 6 (Polarity Map) — integration targets that depend on this library
- `IGNITING_JOY_TO_MTGOA_BAR_INTEGRATION.md` — detailed BARs comparison across IJ and MTGOA
- `manuscripts/sources/igniting-joy/CORPUS.txt` — IJ source text for tool extraction

---

**Next action:** Spec TOOL_LIBRARY.md — populate all known tools, resolve name collisions, write entry template for each tool. Estimated 1–2 sessions.

**Blocking:** WAVE/W.A.V.E. naming decision, BARs framework decision.

---

# BACKLOG ITEM — the superpowers' second names
## Source: canon collision, 2026-08-05

**Status:** BACKLOG
**Type:** Content expansion
**Owner:** Wendell
**Priority:** P3 — deliberately deferred, nothing blocked
**Trigger:** the RPG manual, or expanded School content, whichever comes first

**The ask.** `CANONICAL_ALLYSHIP_SUPERPOWERS.md` gives every superpower a second name — Connector
*the Webweaver*, Strategist *the System Seer*, Disruptor *the Sacred Spark*, Escape Artist *the
Framebreaker*, Alchemist *the Emotional Transmuter*, Storyteller *the Meaning Weaver* — plus two
named shadows each: Chaos Bringer, Caged Rebel, Ghost, Martyr, Emotional Overload, Detached
Observer, Manipulator, Lost Author, and for Coach the Taskmaster and the Empty Cheerleader.

**All of them read 0 hits in `manuscript/`.** Ruled 2026-08-05: the quiz leads with the primary
name, the book and the quiz share one vocabulary, and the second names wait for the RPG manual or
the expanded School material. They are held back from the reader rather than retired — the canon's
definitions still govern.

**Check before adopting them:** `System Seer` collides with `Panoramic Seer`, one of the Sage's
five modes at `ch8:340`. Two Seers on two different Faces, harmless while the epithet is unused and
live the moment it is not.

**Context:** `CANON_AMENDMENT_MANUSCRIPT_SEATING_2026-08-05.md`,
`CANON_COLLISION_SUPERPOWERS_2026-08-05.md`.
