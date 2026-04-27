# Plan: manuscripts/ Git — Workflow & Ownership
**Date:** 2026-04-27
**Problem:** manuscripts/ is gitignored at workspace root but has its own git repo. Every session we re-discover this and waste time. This plan fixes it permanently.

---

## Current State

Three independent versioning systems in the workspace:

| Location | VCS | Synced to Mac |
|----------|-----|---------------|
| Workspace root (`/home/workspace/`) | Git (workspace root) | ❌ No |
| `manuscripts/` | Git (standalone repo) | ❌ No |
| `The-Library/` | Obsidian Sync | ✅ Yes |

**Rule:** manuscripts/ is NOT managed by the workspace root git. It has its own `.git/` directory and must be worked with directly from within that directory.

---

## The Problem We Keep Running Into

When we try to run `git add/commit` from the workspace root on manuscripts files, the workspace root git ignores them (per `.gitignore`). We then assume git isn't being used for manuscripts at all — so we don't commit, we lose version history, and we fall back on file-based versioning (timestamps, `_v1`, `_v2`).

Then we re-discover the manuscripts/.git repo and lose time re-orienting.

---

## The Fix

### 1. Always work from within manuscripts/

When editing anything in `manuscripts/`, always cd there first:

```bash
# WRONG — runs workspace root git (ignores manuscripts/)
cd /home/workspace && git add manuscripts/chapters/ch6-diplomat/...

# RIGHT — runs manuscripts repo git
cd /home/workspace/manuscripts && git add chapters/ch6-diplomat/...
```

### 2. Commit convention for manuscripts/

Standard format:
```
[TYPE] description

TYPE: EDIT | SPEC | DRAFT | REPORT | AUDIT
```

Examples:
```
git commit -m "EDIT: ch6-diplomat channel reorder complete"
git commit -m "SPEC: ch7-sage EA mode confirmations applied"
git commit -m "DRAFT: ch5-architect full pass"
git commit -m "REPORT: chapter completion audit"
```

### 3. Remote setup

Check if manuscripts/ has a remote:
```bash
cd /home/workspace/manuscripts && git remote -v
```

**Recommendation:** Connect manuscripts/ to a GitHub repo. This gives:
- Offsite backup of all book content
- Full version history accessible from anywhere
- Ability to review diffs on GitHub

**If no remote exists yet**, the content lives only on this machine. Setting up GitHub is a one-time action.

### 4. Obsidian sync note

`The-Library/` (Obsidian vault) syncs to Mac via Obsidian Sync. This is separate from manuscripts/ git.

- manuscripts/ content that should be in Obsidian: copy to `The-Library/The Library/07 Book OS/` (manual or script)
- Obsidian vault is NOT git-tracked — use Obsidian Sync for its versioning
- Cross-reference: `The-Library/The Library/07 Book OS/INDEX.md` points to manuscripts/ files

---

## Action Items

- [ ] **Decide:** Does manuscripts/ need a GitHub remote?
  - If yes: create repo + add remote + push
  - If no: document why (e.g., private until publication)
- [ ] **Bookmark:** Always `cd /home/workspace/manuscripts` before git operations
- [ ] **Update AGENTS.md** in manuscripts/ repo with this workflow
- [ ] **Script alias** (optional): add `mgit()` function to workspace shell profile that runs git in manuscripts/ dir

---

## Quick Reference

```bash
# Check manuscripts git status
cd /home/workspace/manuscripts && git status

# Commit manuscripts work
cd /home/workspace/manuscripts && git add <file> && git commit -m "[TYPE] description"

# Check manuscripts remote
cd /home/workspace/manuscripts && git remote -v

# Check workspace root git status (manuscripts files WON'T appear here)
cd /home/workspace && git status
```
