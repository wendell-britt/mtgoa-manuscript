# Phase 2a: Safe Schema Migration — Non-Destructive Approach

**Purpose:** Add `inheritedWorld` + `campaignFlavorLayers` JSON fields to Campaign model without breaking existing campaigns.

**Principle:** Old fields stay untouched until we prove JSON fields work perfectly. Zero production risk.

**Status:** Pre-implementation planning
**Created:** 2026-04-20

---

## Safe Migration Strategy

### Phase 2a.0: Preparation (No DB Changes)

**Goal:** Design everything, test on replica, before touching production.

#### Step 1: Analyze Current Campaign Data
```bash
# Questions to answer (via queries on production replica):
- How many campaigns exist?
- Which campaigns have allyshipDomain populated? showUpContent? questTemplateConfig?
- Are there campaigns with partially-empty fields?
- What are the actual data patterns (not what we assume)?
```

**Deliverable:** Data audit report (`CAMPAIGN_DATA_AUDIT.md`)

#### Step 2: Design Backfill Logic
**For each old field, define the mapping:**
- `allyshipDomain` (text) → `campaignFlavorLayers.scope.allyship_domains` (array)
- `wakeUpContent` (text) → `campaignFlavorLayers.real_world_context.wake_up_message`
- `showUpContent` (text) → `campaignFlavorLayers.real_world_context.show_up_message`
- `questTemplateConfig` (JSON) → `campaignFlavorLayers.quest_generation`
- `inviteConfig` (JSON) → `campaignFlavorLayers.invite_config`

**Special handling:**
- Empty/null fields → don't include in JSON (sparse JSON allowed)
- Validate transformed data against JSON schema before writing

**Deliverable:** Backfill script (TypeScript/Python, untested against production yet)

#### Step 3: Test on Replica
- Restore production DB to a test replica
- Run backfill script on replica
- Verify: old fields ≈ new JSON fields (sample 20-30 campaigns by hand)
- Run unit tests on transformation logic
- Check for edge cases (null values, malformed JSON, missing chapters, etc.)

**Deliverable:** Test report (`REPLICA_TEST_REPORT.md`)

---

### Phase 2a.1: Schema Change (Non-Breaking)

**Goal:** Add new fields without removing old ones.

#### Step 1: Create Prisma Migration

```bash
npx prisma migrate dev --name add_campaign_inheritance_fields
```

**Migration adds:**
```prisma
model Campaign {
  // ... existing fields stay untouched ...

  /// NEW: Inherited world properties (read-only, locked at campaign creation)
  inheritedWorld Json?

  /// NEW: Customizable flavor layers (editable by GM before campaign goes live)
  campaignFlavorLayers Json?

  // OLD FIELDS REMAIN (backward compat):
  // - allyshipDomain String?
  // - wakeUpContent String? @db.Text
  // - showUpContent String? @db.Text
  // - questTemplateConfig Json?
  // - inviteConfig Json?
}
```

**Status:** Non-breaking. New fields are `?` (optional). Existing campaigns unaffected.

**Deliverable:** `.prisma/migrations/<timestamp>_add_campaign_inheritance_fields/`

#### Step 2: Generate Prisma Client

```bash
npx prisma generate
```

**Status:** Update TypeScript types to include new fields. App still works with old fields.

**Deliverable:** Updated `node_modules/@prisma/client`

---

### Phase 2a.2: Data Migration (Tested, Reversible)

**Goal:** Populate new JSON fields from old fields. Keep old fields as backup.

#### Step 1: Run Backfill Script on Production Replica (Final Validation)

```bash
# On production replica only
npm run migrate:backfill -- --dry-run
npm run migrate:backfill -- --verify-only
```

**Flags:**
- `--dry-run`: Shows what WOULD happen, doesn't write
- `--verify-only`: Checks transformed data against schema, doesn't write

**Status:** Still safe. No production writes yet.

**Deliverable:** Dry run output + verification report

#### Step 2: Create Reversible Snapshot

```bash
# Backup current production state
pg_dump -h prod.db -U postgres -d bars_engine > /backups/campaigns_before_migration_$(date +%s).sql
```

**Status:** Can restore to current state if something goes wrong.

**Deliverable:** SQL backup file (stored safely, with timestamp)

#### Step 3: Run Backfill on Production (With Monitoring)

```bash
# Run backfill with transaction (can rollback if it fails)
npm run migrate:backfill -- --production --log-to-file=/logs/backfill_$(date +%s).log

# Parallel process: monitor logs in real-time
tail -f /logs/backfill_*.log
```

**Status:** Writes JSON fields. Old fields untouched.

**Deliverable:** Backfill log with record count + timing

#### Step 4: Verify Data Integrity

```bash
# Run validation queries
npm run migrate:validate

# Check: for each campaign, does old field ≈ new JSON field?
# Expected: 100% match rate
# If match rate < 99%, STOP and investigate
```

**Status:** Proof that transformation worked.

**Deliverable:** Validation report (campaign-by-campaign comparison)

---

### Phase 2a.3: Rollback Plan (Just in Case)

**If anything goes wrong at any step:**

**Before Step 2a.2:**
- Nothing to roll back. New fields exist but are empty. Old fields untouched. Revert migration if needed.

**After Backfill:**
- If validation fails: restore from backup snapshot (SQL dump)
- If validation passes but issues appear later: old fields still exist, can revert code to read old fields

**Rollback checklist:**
```
[ ] Stop all requests to Campaign API
[ ] If backfill incomplete: restore SQL snapshot
[ ] If backfill complete but broken: revert code to read old fields, not JSON
[ ] Re-run validation after rollback
[ ] Post-incident: update backfill logic, fix root cause, retry
```

**No data is lost. We can always go back.**

---

## Implementation Checklist

### Phase 2a.0: Preparation (Week 1)
- [ ] Analyze current campaign data (queries on replica)
- [ ] Write `CAMPAIGN_DATA_AUDIT.md` (data patterns, edge cases)
- [ ] Design backfill mappings (old → new field transformations)
- [ ] Write backfill script (TypeScript/Python)
- [ ] Test script on replica
- [ ] Write `REPLICA_TEST_REPORT.md` (validation results, edge cases found, fixes applied)

### Phase 2a.1: Schema Change (Week 2, Day 1)
- [ ] Create Prisma migration (`add_campaign_inheritance_fields`)
- [ ] Review migration code (ensure old fields untouched)
- [ ] Run `npx prisma migrate dev` locally
- [ ] Generate Prisma Client (`npx prisma generate`)
- [ ] Commit migration to git (don't deploy to prod yet)

### Phase 2a.2: Data Migration (Week 2, Day 2-3)
- [ ] Deploy migration to production (adds new columns, non-breaking)
- [ ] Create SQL backup snapshot
- [ ] Run backfill script with `--dry-run`
- [ ] Run backfill script with `--verify-only`
- [ ] Run backfill script on production with `--production` flag
- [ ] Monitor logs in real-time
- [ ] Run validation queries (match rate check)
- [ ] Write final migration report

### Phase 2a.3: Verification & Gates (Week 2, Day 4)
- [ ] Manual spot-check: 10-20 campaigns (old ≈ new field)
- [ ] Code review: backfill logic + transformation edge cases
- [ ] Deploy backfilled code (API now reads from JSON fields)
- [ ] Monitor in production for 24-48 hours
- [ ] If issues: rollback plan (revert to reading old fields)
- [ ] Write `PHASE2A_COMPLETION_REPORT.md`

### Phase 2a.4: Cleanup (Week 3)
- [ ] Once new fields proven solid for 1+ week: deprecate old fields
- [ ] Add comment to schema: "Deprecated 2026-04-XX. Remove in 2026-05-XX."
- [ ] Stop backfilling into old fields
- [ ] Plan full schema cleanup for next quarter (remove old columns entirely)

---

## Testing & Validation Gates

### Mandatory Gates (Before Production)

| Gate | Check | Pass Criteria | Owner |
|------|-------|---------------|-------|
| **Data Audit** | Campaign data patterns understood | 100% of campaigns analyzed | DBA + Dev |
| **Replica Test** | Backfill script works on production copy | 100% match rate old ≈ new | Dev |
| **Migration Review** | Schema change is non-breaking | No destructive changes, old fields untouched | Code Review |
| **Dry Run** | Production transformation validated | Dry run succeeds with 0 errors | Dev + DBA |
| **Backup** | Safe rollback possible | SQL snapshot created, tested restore | DBA |

### Production Gates (After Backfill)

| Gate | Check | Pass Criteria | Owner |
|------|-------|---------------|-------|
| **Validation Query** | Data integrity confirmed | ≥99% match rate old ≈ new | DBA |
| **Spot Check** | Random campaigns manually reviewed | All spot-checked campaigns match | QA |
| **Log Review** | No errors during backfill | Backfill log has 0 errors, all campaigns processed | Dev |
| **Monitoring** | Production stable post-migration | No spike in error rates, API latency normal | Ops |

---

## Key Rules

### Never Break These Rules

1. **Read-Only Old Fields During Migration**
   - `allyshipDomain`, `wakeUpContent`, etc. are READ-ONLY during backfill
   - No new campaigns should populate old fields
   - No code should write to old fields

2. **Validate Before Writing**
   - Backfill script validates transformed JSON against schema
   - If validation fails: log error, skip campaign, continue (don't crash)
   - Human review of skipped campaigns afterward

3. **Keep Backup Until Proven**
   - SQL snapshot kept for 1 week post-migration
   - Only delete after new fields proven solid
   - Rollback plan always available

4. **Zero Production Downtime**
   - Migration runs during normal business hours (can pause/resume)
   - API stays up throughout
   - Old code path stays active until backfill complete

---

## Success Metrics

| Metric | Target | Measured |
|--------|--------|----------|
| **Data match rate** | ≥99% old ≈ new | Validation query |
| **Migration time** | <2 hours | Backfill log |
| **Error rate** | 0 errors | Backfill log |
| **API uptime** | 100% during migration | Monitoring dashboard |
| **Production issues post-migration** | 0 within 48 hours | Error logs |

---

## References

- `MTGOA_SCHEMA_UPDATE_PLAN.md` — Design details
- `MTGOA_WORLD_INHERITANCE_REFERENCE.md` — What data we're migrating
- `bars-engine/prisma/schema.prisma` — Current schema

---

**Next:** Approve Phase 2a.0 preparation plan, then begin data audit.
