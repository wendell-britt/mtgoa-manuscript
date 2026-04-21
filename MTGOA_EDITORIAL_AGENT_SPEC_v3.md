# SPEC — MTGOA Editorial Pipeline v3
**Type:** Bidirectional Editorial System
**Status:** Draft v3
**Date:** 2026-04-21
**Key change:** Human cold read is a first-class input, runnable FIRST or LAST — not a validation pass

---

## Core Insight

Two editorial tracks exist:
- **Automated track** — passes 1-6 (structural, voice, developmental, mechanical, sources, polish)
- **Human track** — Wendell's cold read

Either track can run first. The other runs second. Both produce annotated feedback. They converge into a single editorial report.

**Why this matters:** Wendell's cold read is not a validation step — it is a primary input that stands on its own. Automated passes should not gatekeep Wendell's feedback. And Wendell's feedback should not be treated as optional icing on an automated cake.

---

## Two Modes

### Mode A: Wendell Cold Read FIRST

```
Wendell cold reads chapter
    ↓
Cold read notes → Pipeline (structured as human_notes.yaml)
    ↓
Automated passes run (with human_notes as input)
    ↓
Converged report: human flags + automated flags combined
```

**Use when:** You want your reading to be undistracted by what the machine found. You want to notice confusion, boredom, energy, belief — before you know what the machine thought was wrong.

### Mode B: Automated Passes FIRST

```
Automated passes run
    ↓
Automated report → Wendell
    ↓
Wendell cold reads (with automated report in hand)
    ↓
Converged report: human flags + automated flags combined
```

**Use when:** You want your cold read to be informed by what the machine flagged. You want to notice whether the machine's concerns match your experience of the chapter.

### Either mode produces the same converged output.

---

## Human Track: Cold Read Notes

**Input:** A chapter draft (clean, no prior annotations visible)
**Process:** Wendell reads and notes:
- Where he got confused
- Where he got bored
- Where he got convinced
- Where he got skeptical
- Where he felt the author's voice (his own) and where it went missing
- Any line, paragraph, or section that needs work

**Output format:** `human_notes_ch7.yaml`
```yaml
chapter: ch7-sage
reader: wendell
date: 2026-04-21
mode: COLD_READ_FIRST  # or COLD_READ_SECOND
notes:
  - location: Section 3, para 4
    type: CONFUSION
    text: "I read this sentence three times and still wasn't sure what altitude was being described"
    severity: 🟡  # 🔴 BLOCKER / 🟡 WARNING / 🟢 NOTED
  - location: Section 4, practice section
    type: BORED
    text: "The Altitude-Switcher section feels repetitive — I wrote this move three times already in Ch5"
    severity: 🟡
  - location: Section 2, para 2
    type: CONVICTION
    text: "'The horse wasn't thirsty' — this is perfect. Don't change it."
    severity: 🟢
  - location: Section 5, Walk section
    type: SKEPTIC
    text: "The Laloux reference feels tacked on — I don't believe this is where I actually learned this"
    severity: 🟡
  - location: Section 3, mid-chapter
    type: VOICE_ABSENCE
    text: "This paragraph sounds like I'm explaining, not discovering. Missing 'Here's what I've noticed'"
    severity: 🟡
```

**When run FIRST:** This is the raw input to the pipeline. Automated passes see it and can: verify, expand, contextualize, or respectfully disagree.

**When run SECOND:** Wendell reads with automated report in mind. His notes can directly address machine-flagged issues and add the human-signal the machine couldn't detect.

---

## Pipeline Architecture (Unchanged Inputs)

```
Chapter draft
    │
    ├─► Phase 0: Deterministic Metrics (always runs — establishes baseline)
    │
    ├─► Automated passes (1-6) — OR Wendell cold read first (either order)
    │
    └─► Converged Editorial Report
            ├─ Human notes (if Wendell read first)
            ├─ Automated flags (if passes ran first)
            └─ Combined action list: BLOCKER / RECOMMENDED / NOTED
```

---

## Decision Layer: Convergence Rules

When both tracks have run, the converged report applies these rules:

| Situation | Resolution |
|-----------|-----------|
| Human flags as 🔴 BLOCKER, machine flags same as 🟡 | Human wins → stays BLOCKER |
| Machine flags as 🔴 BLOCKER, human didn't note it | Flag anyway → add "human didn't catch, verify" |
| Human flags as 🟢 NOTED, machine says 🟡 | Human wins → downgrade to NOTED (reader said don't fix) |
| Machine says PASS, human says 🔴 | Human wins → escalate to BLOCKER |
| Neither flagged → clean | Section is clean per both tracks |

**The rule:** When human and machine disagree, human wins on meaning/voice/intent. Machine wins on mechanical consistency. Both are logged.

---

## Companion File: `human_notes_TEMPLATE.yaml`

Created once, reused per chapter:
```yaml
chapter: ch[N]-[FACE]
reader: wendell
date: YYYY-MM-DD
mode: COLD_READ_FIRST | COLD_READ_SECOND
notes:
  - location: Section X, para Y
    type: CONFUSION | BORED | CONVICTION | SKEPTIC | VOICE_ABSENCE | STRUCTURAL | OTHER
    text: "exact quote or description of what you noticed"
    severity: 🔴 BLOCKER | 🟡 WARNING | 🟢 NOTED
```

**Note type definitions:**
- **CONFUSION:** You read something twice and still didn't get it
- **BORED:** You noticed your attention wandering
- **CONVICTION:** You believed what was written — this works
- **SKEPTIC:** You didn't believe the claim or the move
- **VOICE_ABSENCE:** Your voice went missing — this reads like generic self-help
- **STRUCTURAL:** Something is wrong with the shape of the section (arc, bridge, sequence)
- **OTHER:** Something that doesn't fit the above

---

## What This Changes in the Spec

1. **Pass 7 (ICA Reader Review) is no longer the "last pass"** — it is a parallel track that can run first or second
2. **Pipeline entry points are now two:** automated_track_start() or human_track_start()
3. **Convergence step is explicit** — after both tracks complete, a merge pass produces the converged report
4. **human_notes.yaml becomes a required input** for converged reports, regardless of which track ran first

---

## Still Open (unchanged from v2)

1. Chapter ordering: sequential or parallel?
2. BLOCKER halt rule: halt or continue?
3. Epiphany bridge ownership
4. Source spec (SOURCES.md) ownership
5. Tracker auto-update

---

*Timestamped copy: `MTGOA_EDITORIAL_AGENT_SPEC_v3_2026-04-21.md`*