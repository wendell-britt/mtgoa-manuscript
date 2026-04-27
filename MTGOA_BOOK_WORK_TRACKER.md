# Book Work Tracker — MTGOA
**Created:** 2026-04-14
**Last Updated:** 2026-04-27
**Status:** All 8 chapters complete — Editorial Pass Phase

---

## Chapter Completion Table

| Chapter | Face | Draft File | Lines | Sections | State |
|---------|------|-----------|-------|----------|-------|
| Ch1 | Shaman | `ch1-SHAMAN/CHAPTER1_FULL_DRAFT.md` | 534 | 11 (old template) | 🟡 EDITORIAL |
| Ch2 | Shaman | `ch2-SHAMAN/CHAPTER2_SHAMAN_FULL_DRAFT.md` | 900 | 7/7 | 🟡 EDITORIAL |
| Ch3 | Challenger | `ch3-CHALLENGER/CHAPTER3_CHALLENGER_FULL_DRAFT.md` | 673 | 7/7 | 🟡 EDITORIAL |
| Ch4 | Regent | `ch4-REGENT/CHAPTER4_REGENT_FULL_DRAFT.md` | 542 | 7/7 | 🟡 EDITORIAL |
| Ch5 | Architect | `ch5-ARCHITECT/CHAPTER5_ARCHITECT_FULL_DRAFT.md` | 482 | 7/7 | 🟡 EDITORIAL |
| Ch6 | Diplomat | `ch6-diplomat/CHAPTER6_DIPLOMAT_FULL_DRAFT_MASTER.md` | 566 | 7/7 | 🟡 EDITORIAL |
| Ch7 | Sage | `ch7-sage/CHAPTER7_SAGE_FULL_DRAFT.md` | 668 | 7/7 | 🟡 EDITORIAL |
| Ch8 | Player | `ch8-player/CHAPTER8_PLAYER_FULL_DRAFT.md` | 540 | 7/7 | 🟡 EDITORIAL |

**All chapters: ✅ SHIPPED → 🟡 EDITORIAL PASS. No chapters in DRAFTING state.**

---

## Editorial Pass Queue (Ordered by Priority)

### P0 — Must Fix Before Any Other Editorial Work

**Ch6 Channel Reorder + Format Normalization**
- File: `ch6-diplomat/CHAPTER6_DIPLOMAT_FULL_DRAFT_MASTER.md`
- Issue: Channels out of sequence (Channel 5 written before Channel 2); H1 headers instead of H2
- Fix: Reorder to Bridge→Translate→Hold→Repair→Price; normalize to `## Section N:` format
- Size: Reorder only, no new content
- Owner: Editorial pass

**Ch0 Rewrite (New)**
- File: `ch0-infinite-arcade/CHAPTER0_DRAFT.md`
- Issue: Content from drafts needs consolidation into single chapter file; GM section v3 exists
- Fix: Consolidate GM_SECTION_v3 into CHAPTER0_DRAFT, write missing sections
- Status: PARTIAL (147-line GM section exists, rest needs writing)

### P1 — Hedge Reduction (tracker metric)

| Chapter | Hedge ratio (per 1K words) | Priority |
|---------|---------------------------|----------|
| Ch8 | 2.64 | 🔴 High |
| Ch7 | 1.41 | 🟠 Medium-High |
| Ch1 | 1.0–1.2 | 🟡 Medium |
| Ch2–Ch6 | 0.5–1.0 | 🟢 Low |

### P2 — Template Normalization

Ch1 uses 11-section template (old). Ch2–Ch8 use 7-section template. Ch1 is complete for its template — not a gap, just different format. No changes needed to Ch1 structure.

---

## What "Editorial Pass" Means Here

The editorial pass is **formatting + ordering cleanup**, not new content writing. Specifically:
- Ch6: channel reorder + header format
- Ch0: consolidate drafts + write missing sections
- All chapters: hedge reduction (language, not content)

**What is NOT needed:**
- No chapters need new sections written
- No chapters need new EA moves written
- No "gap analysis" — all 7 sections exist in all 8 chapters

---

## Running the Audit Yourself

Before declaring any chapter "needs work," run:

```bash
# Check section count
grep -c "^## Section\|^# SECTION" manuscripts/chapters/<ch>/CHAPTER*FULL*.md

# Expected: Ch1=11, Ch2-Ch8=7
# If count matches → state is "EDITORIAL PASS"
# If count doesn't match → log the missing section
```

**Rule:** "Section count matches template" = "EDITORIAL PASS." Only "section missing" = "DRAFTING."

---

## Active Editorial Items

### Ch6: Channel Sequence Fix
- Current: Bridge(1) → Price-Namer(5) → Translator(2) → Field-Holder(3) → Repairer(4)
- Target: Bridge(1) → Translator(2) → Field-Holder(3) → Repairer(4) → Price-Namer(5)
- Action: Reorder the 5 channel sections within S3; change H1 `# SECTION` to H2 `## Section`
- No new content needed

### Ch0: Consolidation + Missing Sections
- GM section v3 draft exists: `GM_SECTION_v3_2026-04-22.md`
- Missing: Token System, Ticket System, Three Game Types, Why Gamify, Six Faces Ladder, Entering the Arcade
- Action: Consolidate v3 into CHAPTER0_DRAFT; write remaining sections

---

## Night Research Loop

| Status | PAUSED |
|--------|--------|
| Note | Resume when editorial pass is complete |

---

## Key Files
- `CHAPTER_COMPLETION_AUDIT.md` — root cause analysis of the false-loop pattern
- `MTGOA_6FACE_CHAPTER_STRUCTURE.md` — 7-section template (Ch2–Ch8)
- `MTGOA_BOOK_WORK_TRACKER.md` — this file

---

## ❌ Do Not Use Old Gap Analysis Language

The following tracker language is now **stale** and incorrect:
- "Gap Analysis — In progress"
- "Missing Systems"
- "Chapter-by-Chapter Coverage — Gaps"
- "Write Big Mind Voices chapter"
- "Write Fred Taxonomy chapter"

These were accurate during DRAFTING. All chapters are now in EDITORIAL state. The tracker has been updated to reflect this.

**Updated: 2026-04-27**