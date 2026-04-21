# Phase 2a.0: Execution Checklist

**Status:** Ready to execute
**Duration:** 1 week (preparation before schema migration)
**Risk:** Zero — read-only audit phase

---

## What Phase 2a.0 Delivers

Three documents that define exactly how to migrate data safely:

1. **`PHASE2A_DATA_AUDIT_QUERIES.sql`** — 10 SQL queries to run on production replica
   - Campaign count and distribution
   - Field population rates
   - Data quality issues (malformed JSON, empty strings, inconsistencies)
   - Edge cases and exceptions
   - Sample campaigns for manual review

2. **`PHASE2A_BACKFILL_LOGIC_DESIGN.md`** — Transformation specification
   - How each old field maps to new JSON structure
   - Validation rules and error handling
   - Complete transformation example (before → after)
   - JSON schema for validation

3. **`PHASE2A_SAFE_MIGRATION_PLAN.md`** — Full migration strategy
   - Non-destructive approach (old fields untouched)
   - Replica testing before production
   - Rollback plan (can restore at any stage)
   - Safety gates and verification

---

## Immediate Next Steps (This Week)

### Step 1: Run Data Audit (Day 1-2)

```bash
# Connect to production replica (read-only)
psql -h prod-replica.db -U postgres -d bars_engine -f manuscripts/PHASE2A_DATA_AUDIT_QUERIES.sql > audit_results.txt

# Review results and answer:
# - How many campaigns total?
# - How many campaigns have each field populated?
# - Are there data quality issues?
# - What are the actual allyshipDomain values?
# - Any malformed JSON?
```

**Output:** `CAMPAIGN_DATA_AUDIT.md` (your findings)

### Step 2: Document Audit Findings (Day 2-3)

Write a summary of what you discovered:
```markdown
# Campaign Data Audit Results (2026-04-20)

## Statistics
- Total campaigns: X
- With allyshipDomain: Y%
- With wakeUpContent: Z%
- ...etc

## Data Quality Issues
- Malformed JSON found: count
- Empty strings (should be NULL): count
- Invalid allyshipDomain values: list

## Edge Cases Discovered
- Campaigns with missing fields
- Inconsistent data patterns
- ...etc

## Impact on Backfill
- Expected success rate: X%
- Expected manual review needed: Y campaigns
- Data transformation complexity: simple/moderate/complex
```

### Step 3: Review Backfill Logic (Day 3-4)

Read `PHASE2A_BACKFILL_LOGIC_DESIGN.md` and:
- [ ] Confirm field mappings make sense
- [ ] Identify any adjustments needed based on audit findings
- [ ] Plan for edge cases discovered in audit

### Step 4: Plan Replica Test (Day 5)

Prepare for replica testing:
- [ ] Confirm production replica is accessible (read-only)
- [ ] Plan: will you write backfill script in TypeScript, Python, or SQL?
- [ ] Plan: who reviews the replica test results?

---

## Deliverables This Week

| Item | Status | Owner |
|------|--------|-------|
| Audit SQL queries run | Pending | DBA |
| Audit results captured | Pending | DBA |
| Audit findings documented | Pending | Dev + DBA |
| Backfill logic reviewed | Pending | Dev |
| Edge cases identified | Pending | Dev |
| Replica test plan drafted | Pending | Dev |

---

## Gate: Ready for Phase 2a.1?

**Before moving to schema migration, confirm:**

- [ ] **Audit complete** — We understand the data
- [ ] **Backfill logic confirmed** — Mappings are correct for actual data
- [ ] **Edge cases documented** — We know what could go wrong
- [ ] **Replica test planned** — We know how to test safely
- [ ] **Risk assessment passed** — We're confident in the approach

**If ANY gate fails:** Loop back to Phase 2a.0 and refine.

---

## Key Principle

**Phase 2a.0 is all about avoiding surprises.** The minute we know what the data looks like, what transformations are needed, and how to test safely—we move forward with confidence.

---

## You Are Here

```
Phase 1: Architecture ✅
  └── Phase 2a.0: Preparation 🟡 (IN PROGRESS)
       ├── Audit queries designed ✅
       ├── Backfill logic designed ✅
       ├── Migration plan written ✅
       ├── Data audit (pending) 🟡
       ├── Audit review (pending) 🟡
       └── Replica test plan (pending) 🟡
        └── Phase 2a.1: Schema migration (pending)
            ├── Prisma migration
            ├── Backfill script
            └── Production migration
```

---

## Questions to Answer This Week

1. **How much data are we moving?** (total campaigns, avg field sizes)
2. **Are there data quality issues?** (corrupt JSON, invalid values)
3. **What edge cases exist?** (campaigns with inconsistent data)
4. **Will backfill be 100% successful?** (or do we need manual review?)
5. **How long will backfill take?** (estimate based on campaign count)

---

## Reference Files

- `file 'manuscripts/PHASE2A_DATA_AUDIT_QUERIES.sql'` — Run these SQL queries
- `file 'manuscripts/PHASE2A_BACKFILL_LOGIC_DESIGN.md'` — Transformation specification
- `file 'manuscripts/PHASE2A_SAFE_MIGRATION_PLAN.md'` — Full migration strategy
- `file 'manuscripts/MTGOA_SCHEMA_UPDATE_PLAN.md'` — Schema design (for reference)

---

**Status:** Ready to execute Phase 2a.0

**Owner:** DBA + Backend Dev

**Timeline:** 1 week

**Success metric:** Audit complete, backfill plan validated, ready for Phase 2a.1

---

**Next:** Run the data audit queries and document findings.
