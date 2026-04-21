# EDITORIAL PIPELINE — Version Control Protocol
**Type:** Workflow safeguard
**Status:** LIVE
**Date:** 2026-04-21

---

## The Worst Thing

An editorial pass silently overwrites a chapter draft. No backup. No recovery path. All expansions, revisions, and additions gone.

This has almost happened twice today. We caught it. The pipeline must prevent it.

---

## The Rule

**Every editorial pass that modifies a chapter draft MUST:**

1. **Copy the current state** to `DRAFT_{chapter}_{YYYY-MM-DD}.md` before any modification
2. **Timestamp the backup** — the date in the filename is the creation date, not the modification date
3. **Verify the backup exists** before modifying the original
4. **Log the backup in the editorial report** — which chapter, backup file, timestamp

---

## Pipeline Backup Enforcement

### Phase 0 / Pass 1-4 scripts

Add this at the top of any script that modifies a chapter file:

```python
def backup_chapter(chapter_path: Path) -> Path:
    """Create timestamped backup before any modification."""
    date_str = datetime.now().strftime("%Y-%m-%d")
    backup_path = chapter_path.parent / f"DRAFT_{chapter_path.stem}_{date_str}.md"
    if backup_path.exists():
        # Already backed up today — don't duplicate
        return backup_path
    shutil.copy2(chapter_path, backup_path)
    return backup_path
```

### Before any automated fix

```python
# BEFORE applying any fix:
backup = backup_chapter(chapter_path)
report["backups"].append({
    "chapter": chapter_path.name,
    "backup": str(backup),
    "timestamp": datetime.now().isoformat()
})
# THEN apply the fix
```

---

## Naming Convention

| File type | Convention | Example |
|-----------|-----------|---------|
| Active draft | `{CHAPTER}_{FACE}_{FULL_DRAFT}.md` | `CHAPTER7_SAGE_FULL_DRAFT.md` |
| Pre-edit backup | `DRAFT_{CHAPTER}_{YYYY-MM-DD}.md` | `DRAFT_CHAPTER7_SAGE_2026-04-21.md` |
| Expansion work | `G{N}_{section}.md` | `G1_TRANSCEND_MOVES.md` |
| Gap spec | `{CHAPTER}_GAP_SPEC.md` | `CHAPTER7_GAP_SPEC.md` |
| Editorial report | `editorial_reports/pass{N}_{YYYY-MM-DD}.yaml` | `editorial_reports/pass1_structural.yaml` |

---

## What Exists Now

### Ch7 Sage — Full backup chain
```
CHAPTER7_SAGE_FULL_DRAFT.md          ← current active draft (13,188 words)
CHAPTER7_SAGE_DRAFT_PREEXPANSION.md ← pre-expansion backup (4,956 words)
DRAFT_CH7_FULL_2026-04-21.md          ← day-of backup before any expansion
DRAFT_S1-S3_2026-04-21.md             ← section-level backup
G1_G5_G3_G6_backup.md                ← intermediate work artifacts
```

### Ch6 Diplomat — Orphaned draft rescued
```
CHAPTER6_DIPLOMAT_FULL_DRAFT_MASTER.md ← final 10,204-word version
CHAPTER6_DIPLOMAT_SKELETON_BACKUP.md  ← original 741-word skeleton (preserved)
DRAFT_Q1-Q2_2026-04-20.md              ← intermediate backup
```

### Ch8 Player — Versioned drafts
```
CHAPTER8_PLAYER_FULL_DRAFT.md   ← current (8,209 words)
DRAFT_CH8_V4_2026-04-21.md      ← backup before additions
DRAFT_CH8_V3_2026-04-21.md      ← prior version
DRAFT_CH8_V2ATTEMPT_2026-04-21.md
DRAFT_CH8_FULL_2026-04-21.md
```

### Ch0 — Needs backup
```
CHAPTER0_DRAFT.md   ← current (3,041 words)
CH0_EXPANSIONS.md   ← expansion notes
```
No timestamp backup exists. **Must be fixed before any editorial modification.**

---

## What Needs to Be Fixed

1. **Ch0** — Create timestamp backup before rewrite
2. **Pass 1 script** — Add backup-before-modify to any fix applied
3. **Pass 2 script** — Same
4. **Tracker update** — Add "Last backed up" column to editorial revision table

---

## Decision: Who Creates the Backup?

For automated passes: The script creates the backup.
For human edits: **The human creates the backup first.** The script cannot protect against human edits that skip the script.

**The rule:** If you are about to edit a chapter draft and there is no `DRAFT_*` file with today's date, create one first. No exceptions.

---

## Editorial Report Entry Format

Each editorial report must include a backups section:

```yaml
backups:
  - chapter: CHAPTER7_SAGE_FULL_DRAFT.md
    backup: DRAFT_CHAPTER7_SAGE_2026-04-21.md
    timestamp: "2026-04-21T20:15:00Z"
  - chapter: CHAPTER6_DIPLOMAT_FULL_DRAFT_MASTER.md
    backup: DRAFT_CHAPTER6_DIPLOMAT_2026-04-21.md
    timestamp: "2026-04-21T14:30:00Z"
```
