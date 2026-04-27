# Chapter Completion Audit — 2026-04-27
**Purpose:** Resolve the recurring false-loop where we treat structural inconsistencies as content gaps.

---

## Confirmed Complete Chapters

All 8 chapters have full draft content across all 7 sections.

| Chapter | Full Draft File | Lines | Sections | Status |
|---------|----------------|-------|----------|--------|
| Ch1 | `ch1-SHAMAN/CHAPTER1_FULL_DRAFT.md` | 534 | 11 (old template) | ✅ Complete |
| Ch2 | `ch2-SHAMAN/CHAPTER2_SHAMAN_FULL_DRAFT.md` | 900 | 7/7 | ✅ Complete |
| Ch3 | `ch3-CHALLENGER/CHAPTER3_CHALLENGER_FULL_DRAFT.md` | 673 | 7/7 | ✅ Complete |
| Ch4 | `ch4-REGENT/CHAPTER4_REGENT_FULL_DRAFT.md` | 542 | 7/7 | ✅ Complete |
| Ch5 | `ch5-ARCHITECT/CHAPTER5_ARCHITECT_FULL_DRAFT.md` | 482 | 7/7 | ✅ Complete |
| Ch6 | `ch6-diplomat/CHAPTER6_DIPLOMAT_FULL_DRAFT_MASTER.md` | 566 | 7/7 | ✅ Content complete |
| Ch7 | `ch7-sage/CHAPTER7_SAGE_FULL_DRAFT.md` | 668 | 7/7 | ✅ Complete |
| Ch8 | `ch8-player/CHAPTER8_PLAYER_FULL_DRAFT.md` | 540 | 7/7 | ✅ Complete |

---

## Ch6 Structural Fix (Not Content Gap)

**What needs fixing:** Channel ordering + header format. Content is complete.

**Current channel order in S3:**
1. CHANNEL 1 — BRIDGE-BUILDER ✅
2. CHANNEL 5 — PRICE-NAMER ⚠️ (out of sequence)
3. CHANNEL 2 — TRANSLATOR ✅ (in sequence now but after 5)
4. CHANNEL 3 — FIELD-HOLDER ✅
5. CHANNEL 4 — REPAIRER ✅

**Correct order per SPEC.md:** Bridge → Translate → Hold → Repair → Name Price

**Header format:** Ch6 uses `# SECTION 1 — TITLE` (H1). Other chapters use `## Section 1: Title` (H2). This is a formatting inconsistency, not a content problem.

**Fix required:** Reorder channels + normalize header format. No new content needed.

---

## Why We Keep Falling Into the False Loop

**Root Cause:** The tracking file (`MTGOA_BOOK_WORK_TRACKER.md`) has a "status" field that is never updated after content is shipped. The tracker keeps showing "🔴 IMMEDIATE" and "Gap Analysis" language that was accurate during production but is now stale. When we open the tracker, we're reading the state of the book *during* production, not the state of the book *after* production.

**Contributing causes:**

1. **Per-chapter section counts aren't in the tracker.** The tracker says "Gap Analysis — In progress" for Ch6, but doesn't note that all 7 sections exist. We'd have to open the file to know the actual state.

2. **No "shipped" signal.** Every chapter file has a different naming convention and no canonical "this is done" marker. The tracker relies on a human reading each file.

3. **Editorial pass is a different workflow from draft completion.** We treat "editorial pass" as if it's a content gap, when it's actually a post-completion cleanup task (formatting, channel ordering, hedge reduction). The tracker doesn't distinguish between "content missing" and "formatting needs cleanup."

4. **6-face template evolution.** Ch1 uses an 11-section template. Ch2-Ch8 use a 7-section template. The tracker assumes all chapters follow the same template, so Ch1 always looks "different" even though it's complete for its template.

5. **No pre-flight check before declaring a chapter "needs work."** We open the tracker → see "⚠️ Gap Analysis" → start looking for gaps → find structural formatting issues → call them content gaps → loop.

---

## Pattern: The Four-State Chapter Model

Every chapter goes through four states. The tracker needs to reflect all four:

| State | What it means | Tracker signal |
|-------|---------------|----------------|
| **DRAFTING** | Content being written | 🔴 IN PROGRESS |
| **SHIPPED** | All content present, 7/7 sections done | ✅ COMPLETE |
| **EDITORIAL** | Formatting/hedge/sequence cleanup | 🟡 EDITORIAL PASS |
| **FINAL** | Hedge reduced, format normalized, ready for copyedit | ✅ FINAL |

**Current state:**
- Ch1: EDITORIAL (old template, hedge cleanup needed)
- Ch2, Ch3, Ch4, Ch5: EDITORIAL (hedge reduction per tracker)
- Ch6: EDITORIAL (channel reorder + format normalization)
- Ch7, Ch8: EDITORIAL (hedge reduction per tracker)

**None are DRAFTING. None need new content.**

---

## Rule Going Forward

**Before declaring a chapter "needs work":**
1. Run section count check (`grep -c "^## Section\|^# SECTION" draft.md`)
2. Confirm section count matches expected template (Ch1=11, Ch2-Ch8=7)
3. If section count matches → declare "EDITORIAL PASS" not "Gap Analysis"
4. Distinguish between "content missing" vs "formatting/ordering needs cleanup"
5. Log the distinction in the tracker before starting any work

**The trigger for re-entering draft mode on any chapter:** New content request from the author. Not a tracker read.

---

*Audit run: 2026-04-27*
*Companion: MTGOA_BOOK_WORK_TRACKER.md (should be updated to match this finding)*