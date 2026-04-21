# Phase 2a.0: Six Game Master Analysis

**Question:** How should we implement the campaign data backfill script? What language? What's the best approach?

**Context:**
- bars-engine is TypeScript/Next.js/Prisma
- 2 test campaigns ready to transform
- 100% data quality (no issues)
- Need to preserve old fields for rollback
- Must handle sparse JSON fields
- Need replica testing before production

---

## 1. THE REGENT (Authority, Discipline, Structure)

**Perspective:** *"This is infrastructure work. We need clear governance and repeatable patterns."*

**Analysis:**

The Regent sees this clearly: **we already have a pattern for this in bars-engine**. Look at `apply-migration-direct.ts` — Prisma Client + TypeScript + try/catch + idempotent operations. That's the **house style**.

**Recommendation: Write in TypeScript (tsx script)**

**Why:**
1. **Consistency** — Matches all existing migration scripts in the codebase (100+ scripts)
2. **Governance** — Single language, single runtime, single pattern
3. **Reproducibility** — Can be run via `npm run` — documented, versioned, auditable
4. **Rollback** — Error handling baked in; easy to add dry-run, verify-only flags
5. **Team knowledge** — Your team knows TypeScript/Prisma; no context switching

**Implementation pattern:**
```typescript
// scripts/migrate-campaign-flavor-layers.ts
import { PrismaClient } from '@prisma/client'

const db = new PrismaClient()

async function transformCampaign(campaign: any) {
  // Field transformation logic (from PHASE2A_BACKFILL_LOGIC_DESIGN.md)
  const result = await db.campaign.update({
    where: { id: campaign.id },
    data: { campaignFlavorLayers: transformedJSON }
  })
}

db.$executeRaw` ... ` // for bulk operations if needed
```

**Governance requirements:**
- [x] Logging: every campaign processed, every field transformed, every error
- [x] Dry-run flag: `--dry-run` shows what WOULD happen
- [x] Verify flag: `--verify-only` checks JSON validity without writing
- [x] Exit code: 0 for success, 1 for any errors

**Gate:** Script must pass code review before execution on replica.

---

## 2. THE ARCHITECT (Design, Systems, Patterns)

**Perspective:** *"Let's think about the whole system. What's the shape of this problem?"*

**Analysis:**

The Architect sees a **data transformation pipeline** with clear stages:

1. **Stage 1 (Complete):** Audit — we understand the data
2. **Stage 2 (Design phase):** Backfill logic — we have the specs
3. **Stage 3 (Today):** Implementation — write the transformer
4. **Stage 4 (Next):** Replica test — validate output
5. **Stage 5 (Later):** Production run — with monitoring

**Recommendation: Use a modular TypeScript architecture**

**Why this design:**
```
campaigns-flavor-backfill/
  ├── transform.ts (pure functions, no side effects)
  ├── validator.ts (JSON schema validation)
  ├── logger.ts (structured logging)
  ├── db.ts (database operations)
  └── main.ts (orchestration)
```

**Benefits:**
- **Testability** — Transform functions can be unit-tested against audit data
- **Reusability** — If other models need similar transforms, functions compose
- **Debuggability** — Each layer can be tested in isolation
- **Auditability** — Clear separation between logic/data/validation

**Implementation sequence:**
1. Write `transform.ts` with all 5 field transformations (pure functions)
2. Write `validator.ts` with JSON schema validation
3. Write unit tests with audit data
4. Write `main.ts` with Prisma integration
5. Test on replica
6. Run on production

---

## 3. THE SAGE (Knowledge, Gathering, Insight)

**Perspective:** *"What does the existing codebase teach us? What patterns already exist?"*

**Analysis:**

The Sage looked at the bars-engine repo and found **rich patterns you can learn from**:

**Pattern 1: Prisma migrations** (`scripts/apply-migration-direct.ts`)
- Uses `PrismaClient.$executeRawUnsafe()` for complex SQL
- Wraps operations in try/catch with idempotent error handling
- Returns clear status (✅/❌/⏭️)

**Pattern 2: Data transformation scripts** (`scripts/migrate-user-progress.ts`, `scripts/bootstrap-creation-quests.ts`)
- Query data with Prisma
- Transform in TypeScript (functions)
- Write back with Prisma Client
- Log progress

**Pattern 3: Dry-run & verification** (common pattern)
- `--dry-run` flag skips writes, logs what would happen
- `--verify-only` flag validates without executing
- `process.argv` parsing for flags

**Recommendation: Study and follow existing script patterns**

Code examples to reference:
- `scripts/apply-migration-direct.ts` — SQL + error handling
- `scripts/db-reset-guard.ts` — safety gates & confirmation
- `scripts/migrate-starters.ts` — Prisma transformations
- `scripts/deep-db-audit.ts` — detailed logging

**Key insights from codebase:**
1. **Safety first** — Always include rollback logic, error handling
2. **Logging matters** — Structured logging helps with debugging later
3. **Idempotency** — Scripts should be re-runnable without side effects
4. **Flags are essential** — Dry-run, verify, production flags

---

## 4. THE DIPLOMAT (Connection, Relationship, Organizing)

**Perspective:** *"Who needs to work together on this? What communication is needed?"*

**Analysis:**

The Diplomat sees this as **collaborative work** with clear handoffs:

**Who's involved:**
1. **You (Dev)** — Write the script
2. **QA/Reviewer** — Code review before replica test
3. **DBA** — Monitor replica test, validate output
4. **Team** — Approval before production

**Communication needs:**
- Clear documentation in the script itself (comments)
- Progress logging so watchers can follow along
- Error reporting that's actionable (not just "failed")
- Success metrics so we know when we're done

**Recommendation: Build communication into the script**

**How:**
```typescript
// Clear startup message
console.log('🚀 Starting campaign flavor layers backfill...\n')
console.log(`  Environment: ${process.env.NODE_ENV}`)
console.log(`  Database: ${process.env.DATABASE_URL?.split('@')[1]}`)
console.log(`  Mode: ${flags.dryRun ? 'DRY-RUN' : 'PRODUCTION'}`)
console.log()

// Progress updates every N campaigns
console.log(`[${i}/${total}] Processing ${campaign.slug}...`)

// Summary at the end
console.log(`\n✅ Summary:`)
console.log(`  Total processed: ${stats.total}`)
console.log(`  Successful: ${stats.success} (${percent}%)`)
console.log(`  Failed: ${stats.failed}`)
console.log(`  Match rate (old ≈ new): ${matchRate}%`)
```

**Pre-replica checklist:**
- [ ] Script reviewed by team
- [ ] Dry-run output reviewed
- [ ] Logging looks clear
- [ ] Error messages are actionable
- [ ] Success metrics are measurable

---

## 5. THE CHALLENGER (Disruption, Movement, Action)

**Perspective:** *"Are we overthinking this? What's the fastest way to validate?"*

**Analysis:**

The Challenger sees **analysis paralysis risk**. You have:
- ✅ Audit complete (2 campaigns, perfect data)
- ✅ Logic reviewed (APPROVED)
- ✅ Repo patterns (known and existing)

**Why not move faster?**

**Recommendation: Implement and replica-test THIS WEEK**

**Timeline:**
- **Today/Tomorrow:** Write TypeScript script (2-3 hours)
- **Wednesday:** Code review + dry-run test (1 hour)
- **Thursday:** Replica test with real data (2 hours)
- **Friday:** Ready for production gates

**Why speed matters:**
1. **Small dataset** — Only 2 test campaigns, super fast to transform
2. **Simple logic** — No complex branching, mostly field mappings
3. **Known patterns** — Copy from existing scripts, not inventing
4. **Learning loop** — Each test iteration teaches what's missing

**Recommendation: Start implementing NOW**

Don't wait for perfect planning. The audit is complete, the logic is reviewed. Write the script, test it, learn what breaks. This is how you discover edge cases.

**Action items:**
1. Create `scripts/migrate-campaign-flavor-layers.ts`
2. Implement all 5 transform functions
3. Add logging/flags
4. Test locally with mock data from audit
5. Run on replica Wednesday

---

## 6. THE SHAMAN (Mystery, Awareness, Hidden Patterns)

**Perspective:** *"What are we not seeing? What could go wrong? What's the shadow side?"*

**Analysis:**

The Shaman asks the dangerous questions:

**Hidden risks:**
1. **questTemplateConfig complexity** — Audit shows valid JSON arrays, but are there edge cases we haven't seen?
2. **Sparse JSON interpretation** — We skip empty fields, but what if the app expects certain fields to always exist?
3. **Backward compatibility** — Old code still reads old fields. What happens when new code reads new fields? Do they conflict?
4. **Data drift** — What if new campaigns are created DURING the backfill? Do they get transformed twice?

**Recommendation: Build in extensive validation**

**What to watch for:**
1. **Before transformation:**
   - Parse all JSON to verify it's valid
   - Check for unexpected field combinations
   - Log campaigns that break assumptions

2. **After transformation:**
   - Validate against JSON schema strictly
   - Spot-check 10-20 campaigns by hand
   - Compare old field ↔ new field for match rate
   - Look for NULL mismatches

3. **During replica test:**
   - Run transformation with `--verify-only` first
   - Check error logs for anything unexpected
   - Look for patterns in what gets skipped/failed
   - Verify instance relationships are preserved

**Safety gates:**
```typescript
// Before backfill starts
if (matchRate < 99%) {
  console.error('❌ Match rate too low. Investigate before proceeding.')
  process.exit(1)
}

// During backfill
if (errorCount > (total * 0.01)) { // >1% errors
  console.error('❌ Error rate exceeded threshold. Pausing.')
  process.exit(1)
}

// After backfill
if (!validateAllTransformations()) {
  console.error('❌ Post-backfill validation failed.')
  process.exit(1)
}
```

**The shadow question:**
*"What assumption are we making that could be wrong?"*

Answer: We assume sparse JSON is fine, but what if the application code breaks when fields are missing? Test this explicitly on replica.

---

## Consensus Recommendation

**The 6 Faces align on:**

1. ✅ **Write in TypeScript** (Regent, Architect, Sage, Diplomat agree)
   - Matches bars-engine patterns
   - Governance clear
   - Reproducible

2. ✅ **Use modular architecture** (Architect recommends)
   - Separate transform/validate/db logic
   - Testable functions
   - Debuggable stages

3. ✅ **Build in extensive logging & flags** (Diplomat, Shaman recommend)
   - Dry-run before production
   - Clear error handling
   - Structured output for analysis

4. ✅ **Implement THIS WEEK** (Challenger recommends)
   - Audit complete
   - Logic reviewed
   - Don't wait for perfection

5. ✅ **Validate heavily on replica** (Shaman insists)
   - Spot-check transformations
   - Verify match rate ≥99%
   - Check edge cases

---

## Implementation Checklist (From 6 Faces)

### Regent's Governance
- [ ] Script follows bars-engine naming convention
- [ ] Error handling with try/catch
- [ ] Idempotent (safe to re-run)
- [ ] Exit codes (0=success, 1=error)

### Architect's Design
- [ ] Separate files: transform.ts, validator.ts, logger.ts, db.ts
- [ ] Pure functions for transformations
- [ ] Comprehensive logging at each stage
- [ ] Clear separation of concerns

### Sage's Patterns
- [ ] Study existing migration scripts first
- [ ] Copy error handling from apply-migration-direct.ts
- [ ] Use Prisma Client pattern from migrate-*.ts scripts
- [ ] Reference similar scripts for structure

### Diplomat's Communication
- [ ] Clear startup/summary logging
- [ ] Progress updates every N campaigns
- [ ] Error messages are actionable
- [ ] Pre-test checklist documented

### Challenger's Speed
- [ ] Start coding today
- [ ] Test locally with mock data
- [ ] Replica test by Thursday
- [ ] Ready for production by Friday

### Shaman's Safety
- [ ] Validate all input JSON before transform
- [ ] Check match rate old ≈ new (goal ≥99%)
- [ ] Spot-check 10-20 campaigns manually
- [ ] Error thresholds: pause if >1% fail

---

## Next Step

**Proceed to Phase 2a.0 Step 3:**

1. Create `scripts/migrate-campaign-flavor-layers.ts`
2. Implement transformation functions
3. Add dry-run + verify-only flags
4. Test with mock data from audit
5. Prepare for replica test Wednesday

**Goal:** Have a working, tested script ready for replica validation by end of week.

---

**Document:** PHASE2A_SIX_FACES_BACKFILL_ANALYSIS.md
**Status:** Recommendations compiled, ready for implementation
