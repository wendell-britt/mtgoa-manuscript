# Tracker Fix — Spec
**Created:** 2026-04-21
**Problem:** Tracker updates happen in conversations separate from where work gets done. Sections complete in one chat; tracker gets updated in another. The tracker lags reality and loses accuracy.

---

## Diagnosis

**Three failure modes:**

1. **Separate-conversation drift** — Work happens in Convo A. Tracker updates happen in Convo B (planning session). If Convo B never happens, or if a different agent runs it, the tracker never reflects reality.

2. **Chapter-hierarchy blindness** — The tracker shows "Ch7 COMPLETE" but doesn't track S1 vs S7. If someone opens Ch7 to check what's actually there, they have no per-section signal.

3. **No handoff mechanism** — When a new conversation opens to work on a chapter, it has no way to know what the previous conversation already completed. It either asks the user (break flow) or starts fresh (duplicates work).

**What the tracker IS for:**
- A high-level status table at the project level
- Quick answer: "which chapters are SPEC, which are IN PROGRESS, which are COMPLETE"
- A place to record what's been updated and when

**What the tracker IS NOT for:**
- Per-section tracking (that's the chapter file's job)
- Real-time accuracy (it's a summary, not a live dashboard)

---

## Design

### Architecture: Two-Level System

**Level 1 — Chapter Status File** (source of truth, per chapter)
`chapters/chN-FACE/STATUS.md` — updated immediately when work completes, in the same conversation

**Level 2 — Project Tracker** (summary view, generated from Level 1 files)
`manuscripts/MTGOA_BOOK_WORK_TRACKER.md` — regenerated periodically or on demand

This way: work completes → STATUS.md updated immediately (same turn, same chat) → no drift.

---

### STATUS.md Template

```
# [Chapter] Status
**Face:** [Face name]
**Color/Altitude:** [color] — [altitude]
**Created:** [YYYY-MM-DD]
**Updated:** [YYYY-MM-DD]
**Current status:** [SPEC ONLY | IN PROGRESS | COMPLETE]

## Section Status

| Section | Status | Notes |
|---------|--------|-------|
| S1 Exile | ✅ DONE | 2026-04-21 |
| S2 Distortion | 🔄 IN PROGRESS | — |
| S3 Concept | ⏳ AWAIT | — |
| S4 Practice | ⏳ AWAIT | — |
| S5 Journey | ⏳ AWAIT | — |
| S6 Game | ⏳ AWAIT | — |
| S7 Recap | ⏳ AWAIT | — |

## Last Updated By
**Conversation:** [con_xxxxx]
**What changed:** [brief description]

## Pending
- [ ] S3 Concept draft
- [ ] S5 gates EA labeling

## Metabolized Learnings
- [learned X about EA mode mapping, 2026-04-21]
```

---

### Update Protocol (The Rule)

**WHEN a section draft is completed in any conversation:**
1. Update the chapter's `STATUS.md` immediately (same turn that confirms the draft)
2. Include: section name, status (DONE/IN PROGRESS/AWAIT), date
3. Do NOT wait for a planning session to update the tracker

**WHEN a chapter reaches COMPLETE:**
1. Update `STATUS.md` — all 7 sections DONE
2. Update `MTGOA_BOOK_WORK_TRACKER.md` — status column → COMPLETE, notes column → timestamp
3. Update happens in the SAME conversation where the final section was completed

**BEFORE starting work on any chapter in any conversation:**
1. Read the chapter's `STATUS.md` first
2. Note what's already done, what's in progress, what's pending
3. Do not start a section from scratch if a draft already exists

---

### Tracker Generation

A script that reads all `STATUS.md` files and generates a tracker table summary:

```bash
# Reads all chapters/*/STATUS.md → outputs a markdown table
python3 manuscripts/generate_tracker.py
```

This is a convenience — the STATUS.md files are the source of truth. The tracker is derived.

---

## Implementation Steps

1. **Create STATUS.md for all chapters that don't have one**
   - Ch1–Ch4: COMPLETE status, all sections DONE
   - Ch5: COMPLETE (done today)
   - Ch6: COMPLETE
   - Ch7: COMPLETE (done today)
   - Ch8: IN PROGRESS (drafts exist; needs section-level breakdown)

2. **Create the tracker generation script**
   - `manuscripts/generate_tracker.py` — reads STATUS.md files, outputs markdown table

3. **Create the rule**
   - "WHEN section draft completed → update STATUS.md immediately"
   - "WHEN chapter COMPLETE → update MTGOA_BOOK_WORK_TRACKER.md in same turn"

4. **Archive old tracker entries**
   - Bulk-rewrite the tracker table to match what's actually true

5. **Handoff protocol in AGENTS.md**
   - Add: "Before working on a chapter, read chapters/chN-FACE/STATUS.md first"

---

## What Gets Built

| Artifact | Purpose | Tool |
|----------|---------|------|
| `STATUS.md` template | Per-chapter source of truth | `create_or_rewrite_file` |
| `generate_tracker.py` | Derive tracker from status files | Python script |
| Rule (new) | Update STATUS on section completion | `create_rule` |
| AGENTS.md update | Handoff protocol | `edit_file_llm` |
| Tracker rewrite | Match reality | `edit_file_llm` |

**What does NOT get built:** A database, a dashboard, or any multi-file orchestration system. Keep it flat and file-based.

---

## Files to Update

- `manuscripts/chapters/ch1-FACE/STATUS.md` (×4 for complete chapters)
- `manuscripts/chapters/ch5-ARCHITECT/STATUS.md` (new)
- `manuscripts/chapters/ch6-diplomat/STATUS.md` (new)
- `manuscripts/chapters/ch7-sage/STATUS.md` (new)
- `manuscripts/chapters/ch8-player/STATUS.md` (new — IN PROGRESS)
- `manuscripts/generate_tracker.py` (new script)
- `manuscripts/MTGOA_BOOK_WORK_TRACKER.md` (rewrite from STATUS data)
- `/home/workspace/AGENTS.md` (add handoff protocol)
- Rules (new: STATUS update rule)

---

## Verification

After implementation:
- [ ] Every chapter has a current `STATUS.md`
- [ ] `generate_tracker.py` outputs a table that matches all STATUS.md files
- [ ] The rule fires on section completion (tested in next draft session)
- [ ] AGENTS.md contains the handoff protocol
