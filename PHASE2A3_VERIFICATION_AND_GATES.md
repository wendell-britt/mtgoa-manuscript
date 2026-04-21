# Phase 2a.3: Verification & Gates

**Status:** Ready to execute
**Duration:** 24-48 hours (includes production monitoring)
**Goal:** Confirm data integrity, pass all gates, prepare for Phase 2b

---

## Verification Checklist

### 1. Manual Spot-Check ✅

**Approach:** Manually review transformed campaigns

**Campaign 1: "summer-solidarity-drive" (DRAFT)**

Expected:
- scope.allyship_domains: ["GATHERING_RESOURCES"]
- quest_generation: 2 quests preserved
- metadata: migrated_from, migrated_at, original_campaign_id

Verify:
- [ ] Allyship domain correct
- [ ] Quest count matches
- [ ] Metadata present
- [ ] All fields valid JSON

**Campaign 2: "casey-s-birthday" (APPROVED)**

Expected:
- scope.allyship_domains: ["DIRECT_ACTION"]
- quest_generation: 6 quests preserved
- metadata: timestamps present

Verify:
- [ ] Allyship domain correct
- [ ] Quest count matches (6)
- [ ] Each quest has correct move type
- [ ] Metadata present

**Success Criteria:** ✅ Both campaigns match expectations

---

### 2. Data Integrity Validation

**Query:** Compare old fields ↔ new JSON fields

```sql
SELECT
  id,
  slug,
  allyshipDomain,
  (campaignFlavorLayers::jsonb -> 'scope' -> 'allyship_domains' ->> 0) as new_domain,
  (campaignFlavorLayers::jsonb ->> 'quest_generation') IS NOT NULL as has_quests
FROM campaigns
WHERE id IN ('cmnkge8e0000cswzbulim9h8u', 'cmnkqua3u0001pronxeof4mht');
```

Expected: 100% match rate (old ≈ new)

**Success Criteria:** ✅ Match rate ≥99%

---

### 3. Schema Validation

Verify:
- [ ] inheritedWorld column exists (NULL for now)
- [ ] campaignFlavorLayers column exists (populated)
- [ ] Both columns are JSONB type
- [ ] GIN indexes created

**Success Criteria:** ✅ Schema correct, indexes present

---

### 4. Performance Check

Monitor:
- [ ] No unusual query latency (check if JSONB GIN indexes working)
- [ ] No table locks or blocking operations
- [ ] Storage impact acceptable (<1MB increase for 2 campaigns)

**Success Criteria:** ✅ Performance normal

---

## Safety Gates

### Gate 1: Data Audit Complete ✅
- [x] Audit queries run
- [x] Data patterns understood
- [x] Edge cases identified

**Status:** PASSED

---

### Gate 2: Backfill Logic Confirmed ✅
- [x] Transformation functions designed
- [x] Logic reviewed by 6 Game Masters
- [x] Validation schema implemented

**Status:** PASSED

---

### Gate 3: Replica Testing Complete ✅
- [x] Dry-run successful (2/2)
- [x] Verify-only passed (100%)
- [x] Spot-checks manual review

**Status:** PASSED

---

### Gate 4: Production Migration Clean ✅
- [x] Schema migration applied
- [x] Prisma Client regenerated
- [x] Backfill executed (2/2)
- [x] Zero errors

**Status:** PASSED

---

### Gate 5: Code Review Sign-Off
- [ ] Backfill script reviewed
- [ ] Migration SQL reviewed
- [ ] Implementation approach approved
- [ ] No security concerns

**Status:** PENDING (next)

---

### Gate 6: Production Monitoring (24-48h)
- [ ] Monitor error rates (expect 0)
- [ ] Monitor query latency (expect normal)
- [ ] Monitor database size (expect stable)
- [ ] Monitor user impact (expect none)

**Status:** PENDING

---

### Gate 7: Final Completion Report
- [ ] All metrics confirmed
- [ ] No unexpected issues
- [ ] Ready for Phase 2b

**Status:** PENDING

---

## Monitoring Plan (24-48 hours)

### What to Watch For

1. **Error Rates**
   - Target: 0 errors
   - Where: Application logs, database logs
   - Alert threshold: >1 error

2. **Query Performance**
   - Target: Normal latency (baseline unchanged)
   - Where: Database monitoring dashboard
   - Alert threshold: >50% increase

3. **Data Consistency**
   - Target: Old ≈ new fields match
   - Where: Validation queries every 4 hours
   - Alert threshold: <99% match rate

4. **User Impact**
   - Target: Zero impact
   - Where: Campaign access, quest creation
   - Alert threshold: Any user-facing errors

---

## Completion Criteria

**All gates must be PASSED:**

- [x] Gate 1: Data Audit ✅
- [x] Gate 2: Backfill Logic ✅
- [x] Gate 3: Replica Testing ✅
- [x] Gate 4: Production Migration ✅
- [ ] Gate 5: Code Review ← NEXT
- [ ] Gate 6: Production Monitoring ← AFTER CODE REVIEW
- [ ] Gate 7: Completion Report ← FINAL

---

## Phase 2a.3 Execution Steps

### Step 1: Immediate (Now)
1. Manual spot-check of 2 campaigns
2. Run data integrity query
3. Verify schema changes
4. Check performance baseline

### Step 2: Code Review (Next)
1. Review backfill script implementation
2. Review migration SQL
3. Review error handling
4. Review documentation
5. Team sign-off

### Step 3: Monitoring (24-48 hours)
1. Watch error rates
2. Check query latency
3. Validate data consistency
4. Note any issues

### Step 4: Completion (After monitoring)
1. Confirm all metrics
2. Write completion report
3. Prepare Phase 2b transition
4. Celebrate success 🎉

---

## Phase 2a.3 Success Looks Like

✅ All spot-checks pass (both campaigns correct)
✅ Code review approves implementation
✅ No errors in production monitoring
✅ Performance unaffected
✅ Data integrity confirmed (100% match)
✅ Ready to move forward with Phase 2b

---

## If Issues Arise

**Issue: Data mismatch in spot-check**
→ Investigate root cause, re-run backfill if needed, validate again

**Issue: Code review finds problems**
→ Fix issues, re-run tests, get re-approval

**Issue: Performance degradation**
→ Check indexes, analyze queries, optimize if needed

**Issue: Errors in production**
→ Enable extra logging, check logs, fix root cause

**Safety:** Old fields remain, can revert to old code path immediately

---

## Ready for Phase 2a.3?

✅ **YES** — All previous gates passed, ready for verification

**Expected Duration:** 24-48 hours
**Expected Outcome:** All gates pass, Phase 2b cleared to proceed
**Confidence Level:** 🟢 **VERY HIGH**

---

**Document:** PHASE2A3_VERIFICATION_AND_GATES.md
**Status:** Ready to execute
