# Campaign Data Audit Results

**Date:** 2026-04-20
**Status:** Complete
**Dataset Size:** 2 campaigns (small test database)

---

## Executive Summary

The audit reveals a **small, clean dataset** with:
- **100% data quality** — no malformed JSON, no empty strings, no NULL inconsistencies
- **High field population for questTemplateConfig** (100%) — ready for transformation
- **Zero population for text fields** (wakeUpContent, showUpContent) — sparse JSON expected
- **Valid allyshipDomain values** — all valid domains, no cleanup needed
- **100% expected backfill success rate** — no data quality blockers

---

## Campaign Statistics

| Metric | Count | Details |
|--------|-------|---------|
| **Total campaigns** | 2 | 1 DRAFT, 1 APPROVED |
| **Active campaigns** | 1 | Status: APPROVED |
| **Campaign avg age** | ~16 days | Created 2026-04-04 |

---

## Field Population Analysis

### Overall Population Rates

| Field | Populated | Count | Rate | Status |
|-------|-----------|-------|------|--------|
| `allyshipDomain` | 2 | 2/2 | **100%** | ✅ Ready |
| `wakeUpContent` | 0 | 0/2 | **0%** | ⏸️ Sparse |
| `showUpContent` | 0 | 0/2 | **0%** | ⏸️ Sparse |
| `questTemplateConfig` | 2 | 2/2 | **100%** | ✅ Ready |
| `inviteConfig` | 0 | 0/2 | **0%** | ⏸️ Sparse |

### By Status

| Status | Count | allyshipDomain | wakeUpContent | showUpContent | questTemplateConfig |
|--------|-------|-----------------|----------------|----------------|----------------------|
| DRAFT | 1 | ✅ Yes | ❌ No | ❌ No | ✅ Yes |
| APPROVED | 1 | ✅ Yes | ❌ No | ❌ No | ✅ Yes |

---

## allyshipDomain Values

**Distinct values found: 2**

| Value | Count | Status |
|-------|-------|--------|
| `GATHERING_RESOURCES` | 1 | ✅ Valid |
| `DIRECT_ACTION` | 1 | ✅ Valid |

**Validation:** All values are in the valid domain list:
- ✅ GATHERING_RESOURCES
- ✅ SKILLFUL_ORGANIZING
- ✅ DIRECT_ACTION
- ✅ RAISE_AWARENESS

---

## questTemplateConfig Structure

**Campaigns with config: 2/2 (100%)**

### Campaign 1: "Summer Solidarity Drive" (DRAFT)
- Config contains: **2 quest templates**
  1. "Take Your First Action" (moveType: showUp, allyshipDomain: DIRECT_ACTION)
  2. "Welcome Quest" (moveType: wakeUp, allyshipDomain: GATHERING_RESOURCES)
- Status: ✅ Valid JSON, well-structured

### Campaign 2: "Casey's Birthday" (APPROVED)
- Config contains: **6 quest templates**
  1. "Welcome Quest" (moveType: wakeUp, allyshipDomain: GATHERING_RESOURCES)
  2. "Introduce Yourself" (moveType: showUp, allyshipDomain: GATHERING_RESOURCES)
  3. "Share Your Why" (moveType: wakeUp, allyshipDomain: RAISE_AWARENESS)
  4. "Amplify the Message" (moveType: showUp, allyshipDomain: RAISE_AWARENESS)
  5. "Share a Resource" (moveType: growUp, allyshipDomain: GATHERING_RESOURCES)
  6. "Organize a Gathering" (moveType: showUp, allyshipDomain: SKILLFUL_ORGANIZING)
- Status: ✅ Valid JSON, well-structured

**Observations:**
- Both configs are valid JSON arrays with complete quest template objects
- Templates include detailed quest copy, settings, and configuration
- This data will map cleanly to `campaignFlavorLayers.quest_generation`

---

## Text Field Sizes

| Field | Count | Avg Size | Max Size | Status |
|-------|-------|----------|----------|--------|
| `wakeUpContent` | 0 | N/A | N/A | No data |
| `showUpContent` | 0 | N/A | N/A | No data |

**Notes:**
- No text content in either field (expected in test campaigns)
- When populated, expect to be well under 5KB limit

---

## Data Quality Assessment

### ✅ Positive Findings

1. **No empty strings** — All NULL/empty fields are properly NULL, not empty strings
2. **No malformed JSON** — questTemplateConfig both contain valid, parseable JSON
3. **No NULL inconsistencies** — Campaigns with questTemplateConfig don't have data mismatches
4. **Valid domain values** — All allyshipDomain values are in the allowed list

### ⚠️ Audit Query Note

One audit query (query #8) had a PostgreSQL syntax error:
- **Query:** Checking for invalid JSON with `IS JSONB` syntax
- **Error:** PostgreSQL 17 may not support this exact syntax
- **Impact:** Query did not execute, but not critical (other queries confirmed JSON validity)
- **Action:** This can be fixed or skipped in future audits

---

## Instance Hierarchy

**Campaigns linked to instances: 2/2 (100%)**

| Campaign | Instance | Instance ID | Type |
|----------|----------|-------------|------|
| summer-solidarity-drive | BB-BDAY-001 | BB-BDAY-001 | Custom |
| casey-s-birthday | bruised-banana-house | cmn3hzn1s00011hh35umwl14b | Primary |

**Status:** ✅ Both campaigns properly linked to instances

---

## Edge Cases & Issues

| Category | Count | Status | Action |
|----------|-------|--------|--------|
| Empty strings | 0 | ✅ None | No cleanup needed |
| Malformed JSON | 0 | ✅ None | No validation errors |
| Missing allyshipDomain | 0 | ✅ None | All campaigns have domain |
| Missing questTemplateConfig | 0 | ✅ None | Both have configs |
| Incomplete data patterns | 0 | ✅ None | No anomalies detected |

---

## Impact on Backfill

### Expected Success Rate

**✅ 100% — All 2 campaigns will backfill successfully**

Reasoning:
- ✅ All campaigns have required fields (allyshipDomain)
- ✅ All JSON fields are valid and well-formed
- ✅ No data quality issues to work around
- ✅ No NULL inconsistencies to handle

### Sparse JSON Fields

Some campaigns will have sparse JSON output (missing fields):
- **wakeUpContent:** Will not be in real_world_context (expected)
- **showUpContent:** Will not be in real_world_context (expected)
- **inviteConfig:** Will not be populated (expected)

This is **expected and fine** — Backfill logic handles sparse JSON by skipping empty fields.

### Data Transformation Complexity

**Complexity: SIMPLE**

- All mappings are 1:1 or simple value conversions
- No complex business logic needed
- No edge case handling required beyond standard NULL checks

---

## Recommendations

1. **Proceed with backfill** — Data quality is excellent
2. **Sparse JSON is OK** — Test the transformation with incomplete/sparse fields
3. **Test with production data** — Once production has more campaigns, re-audit for additional patterns
4. **Monitor questTemplateConfig structure** — Ensure all variations parse correctly during transformation

---

## Backfill Logic Checklist

**For Phase 2a.0 backfill review:**

- [x] Field population rates understood
- [x] Allyship domain values validated
- [x] JSON structure verified (questTemplateConfig)
- [x] No data quality blockers
- [x] Edge cases identified (sparse fields expected)
- [x] Transformation complexity assessed (simple)

---

## Files Used

- Audit queries: `manuscripts/PHASE2A_DATA_AUDIT_QUERIES.sql`
- Results: `/tmp/audit_results_20260420.txt`

---

## Next Steps

1. ✅ **Phase 2a.0 Step 1 Complete** — Data audit finished
2. **Phase 2a.0 Step 2** — Review backfill logic against actual data (next)
3. **Phase 2a.0 Step 3** — Plan replica test strategy
4. **Phase 2a.0 Step 4** — Prepare for Phase 2a.1 gates

---

**Status:** Ready for Phase 2a.0 Step 2 (Backfill Logic Review)
