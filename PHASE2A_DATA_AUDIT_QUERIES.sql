-- PHASE 2a.0: Campaign Data Audit Queries
-- Purpose: Understand current state of Campaign table before migration
-- Run on: PRODUCTION REPLICA (read-only)
-- Date: 2026-04-20

-- ============================================================================
-- 1. CAMPAIGN COUNT & STATUS
-- ============================================================================

-- Total campaigns in system
SELECT
  COUNT(*) as total_campaigns,
  COUNT(CASE WHEN status = 'DRAFT' THEN 1 END) as draft,
  COUNT(CASE WHEN status = 'PENDING_REVIEW' THEN 1 END) as pending_review,
  COUNT(CASE WHEN status = 'APPROVED' THEN 1 END) as approved,
  COUNT(CASE WHEN status = 'LIVE' THEN 1 END) as live,
  COUNT(CASE WHEN status = 'ARCHIVED' THEN 1 END) as archived
FROM campaigns;

-- ============================================================================
-- 2. FIELD POPULATION ANALYSIS
-- ============================================================================

-- How many campaigns have each field populated?
SELECT
  COUNT(*) as total,
  COUNT(CASE WHEN "allyshipDomain" IS NOT NULL AND "allyshipDomain" != '' THEN 1 END) as with_allyshipDomain,
  COUNT(CASE WHEN "wakeUpContent" IS NOT NULL AND "wakeUpContent" != '' THEN 1 END) as with_wakeUpContent,
  COUNT(CASE WHEN "showUpContent" IS NOT NULL AND "showUpContent" != '' THEN 1 END) as with_showUpContent,
  COUNT(CASE WHEN "questTemplateConfig" IS NOT NULL THEN 1 END) as with_questTemplateConfig,
  COUNT(CASE WHEN "inviteConfig" IS NOT NULL THEN 1 END) as with_inviteConfig
FROM campaigns;

-- Breakdown by status
SELECT
  status,
  COUNT(*) as count,
  COUNT(CASE WHEN "allyshipDomain" IS NOT NULL AND "allyshipDomain" != '' THEN 1 END) as with_allyshipDomain,
  COUNT(CASE WHEN "wakeUpContent" IS NOT NULL AND "wakeUpContent" != '' THEN 1 END) as with_wakeUpContent,
  COUNT(CASE WHEN "showUpContent" IS NOT NULL AND "showUpContent" != '' THEN 1 END) as with_showUpContent
FROM campaigns
GROUP BY status
ORDER BY count DESC;

-- ============================================================================
-- 3. ALLYSHIP DOMAIN VALUES
-- ============================================================================

-- What values exist in allyshipDomain?
SELECT DISTINCT
  "allyshipDomain",
  COUNT(*) as count
FROM campaigns
WHERE "allyshipDomain" IS NOT NULL
GROUP BY "allyshipDomain"
ORDER BY count DESC;

-- ============================================================================
-- 4. QUEST TEMPLATE CONFIG ANALYSIS
-- ============================================================================

-- How many campaigns have questTemplateConfig? What's the data?
SELECT
  COUNT(*) as total_with_config,
  COUNT(CASE WHEN "questTemplateConfig"::TEXT ~ 'templateType' THEN 1 END) as has_templateType,
  COUNT(CASE WHEN "questTemplateConfig"::TEXT ~ 'overrides' THEN 1 END) as has_overrides
FROM campaigns
WHERE "questTemplateConfig" IS NOT NULL;

-- Sample 5 questTemplateConfig values to understand structure
SELECT
  id,
  slug,
  "questTemplateConfig"
FROM campaigns
WHERE "questTemplateConfig" IS NOT NULL
LIMIT 5;

-- ============================================================================
-- 5. INVITE CONFIG ANALYSIS
-- ============================================================================

-- How many campaigns have inviteConfig?
SELECT
  COUNT(*) as total_with_config,
  COUNT(CASE WHEN "inviteConfig"::TEXT ~ 'method' THEN 1 END) as has_method,
  COUNT(CASE WHEN "inviteConfig"::TEXT ~ 'capacity' THEN 1 END) as has_capacity,
  COUNT(CASE WHEN "inviteConfig"::TEXT ~ 'messaging' THEN 1 END) as has_messaging
FROM campaigns
WHERE "inviteConfig" IS NOT NULL;

-- Sample 5 inviteConfig values to understand structure
SELECT
  id,
  slug,
  "inviteConfig"
FROM campaigns
WHERE "inviteConfig" IS NOT NULL
LIMIT 5;

-- ============================================================================
-- 6. TEXT FIELD SIZES
-- ============================================================================

-- How big are wakeUpContent and showUpContent?
SELECT
  COUNT(*) as total,
  COUNT(CASE WHEN "wakeUpContent" IS NOT NULL THEN 1 END) as with_wake,
  AVG(CASE WHEN "wakeUpContent" IS NOT NULL THEN LENGTH("wakeUpContent") ELSE NULL END) as avg_wake_len,
  MAX(CASE WHEN "wakeUpContent" IS NOT NULL THEN LENGTH("wakeUpContent") ELSE NULL END) as max_wake_len,
  COUNT(CASE WHEN "showUpContent" IS NOT NULL THEN 1 END) as with_show,
  AVG(CASE WHEN "showUpContent" IS NOT NULL THEN LENGTH("showUpContent") ELSE NULL END) as avg_show_len,
  MAX(CASE WHEN "showUpContent" IS NOT NULL THEN LENGTH("showUpContent") ELSE NULL END) as max_show_len
FROM campaigns;

-- ============================================================================
-- 7. EDGE CASES & DATA QUALITY
-- ============================================================================

-- Campaigns with inconsistent data (e.g., has questTemplateConfig but no allyshipDomain)
SELECT
  COUNT(*) as potential_issues,
  COUNT(CASE WHEN "questTemplateConfig" IS NOT NULL AND "allyshipDomain" IS NULL THEN 1 END) as config_no_domain,
  COUNT(CASE WHEN "inviteConfig" IS NOT NULL AND ("wakeUpContent" IS NULL OR "showUpContent" IS NULL) THEN 1 END) as invite_missing_content
FROM campaigns;

-- Campaigns with empty strings (should be NULL)
SELECT
  COUNT(CASE WHEN "allyshipDomain" = '' THEN 1 END) as empty_allyshipDomain,
  COUNT(CASE WHEN "wakeUpContent" = '' THEN 1 END) as empty_wakeUpContent,
  COUNT(CASE WHEN "showUpContent" = '' THEN 1 END) as empty_showUpContent
FROM campaigns;

-- ============================================================================
-- 8. MALFORMED JSON CHECK
-- ============================================================================

-- Check for campaigns with invalid JSON in questTemplateConfig or inviteConfig
-- (This is PostgreSQL-specific; adjust for your DB)
SELECT
  id,
  slug,
  'questTemplateConfig' as field
FROM campaigns
WHERE "questTemplateConfig" IS NOT NULL
  AND NOT ("questTemplateConfig" IS JSONB)
LIMIT 10
UNION ALL
SELECT
  id,
  slug,
  'inviteConfig' as field
FROM campaigns
WHERE "inviteConfig" IS NOT NULL
  AND NOT ("inviteConfig" IS JSONB)
LIMIT 10;

-- ============================================================================
-- 9. SAMPLE CAMPAIGNS FOR MANUAL REVIEW
-- ============================================================================

-- 10 diverse campaigns for spot-checking during backfill
SELECT
  id,
  slug,
  name,
  status,
  "allyshipDomain",
  "wakeUpContent",
  "showUpContent",
  "questTemplateConfig",
  "inviteConfig",
  "createdAt"
FROM campaigns
ORDER BY RANDOM()
LIMIT 10;

-- ============================================================================
-- 10. INSTANCE HIERARCHY CHECK
-- ============================================================================

-- Verify campaign → chapter → instance relationships
SELECT
  c.id as campaign_id,
  c.slug as campaign_slug,
  c."instanceId" as instance_id,
  i.slug as instance_slug,
  i.name as instance_name
FROM campaigns c
LEFT JOIN instances i ON c."instanceId" = i.id
LIMIT 20;

-- ============================================================================
-- Output checklist:
-- [ ] Total campaign count and distribution by status
-- [ ] Field population rates (%) for each old field
-- [ ] Unique values in allyshipDomain
-- [ ] Sample JSON structures for questTemplateConfig and inviteConfig
-- [ ] Text field sizes (min/avg/max)
-- [ ] Data quality issues (empty strings, malformed JSON, inconsistent data)
-- [ ] Edge cases and exceptions
-- [ ] Instance relationship validation
-- ============================================================================
