# BOOK_WORKFLOW_SYSTEM.md — Token-Safe Writing Workflow

**Created:** 2026-04-23  
**Source:** Consolidated from workspace `AGENTS.md` — WAVE and Three-Context extracted to enable scannable AGENTS.md  
**Canonical location:** `manuscripts/BOOK_WORKFLOW_SYSTEM.md`  
**Referenced by:** workspace `AGENTS.md` (File Verification + Context Switching rules)

---

## Process WAVE — Token-Safe Workflow (Non-Negotiable)

**Created:** 2026-04-16  
**Source:** 6-face WAVE after repeated token-limit failures during chapter drafting

### The core problem

Token limits kill generation mid-output. When that happens:
- The tool returns "written" with no error
- The file exists but content is silently truncated
- The "written" confirmation is indistinguishable from a successful write
- Downstream merge scripts fail because anchor text doesn't exist where expected

### The WAVE discipline

| Phase | Action | Token budget |
|---|---|---|
| **W**rite | Generate section, write to file | ~30% of limit |
| **A**ssess | Read back, verify anchor text, assess completeness | ~10% of limit |
| **V**erify | Run wc -c via separate tool, confirm non-zero | ~5% of limit |
| **E**mit | Proceed or regenerate | ~5% of limit |

Stop at each phase. Don't batch W→A→V→E across multiple sections in one response.

### What "verified" means

Never write "confirmed" or "verified" without the level qualifier:
- ✓ `[L1 exists]` — file exists, size > 0
- ✓ `[L2 readback=match]` — read back, content matches
- ✓ `[L3 hash=match]` — SHA256 confirmed
- ✗ `[L2 mismatch]` — content didn't match, red flag

---

## Three-Context Protocol

**Source:** 6-face WAVE after repeated token-limit failures during chapter drafting

### The three contexts

| Context | Trigger | Rule |
|---|---|---|
| **A — Generate** | User asks to write or draft | Write file → append → confirm path only. No explanation. |
| **B — Review** | User asks to assess, gap-analyze, or audit | Read file → assess → update tracker → confirm path only. No generation. |
| **C — Plan** | User asks what's next or where to start | Read tracker → decide one action → confirm path only. No generation. |

### The rule

**Never combine A+B or C+A in the same response.**

Reason: Context switching mid-response causes token overhead and diffuses both tasks. The agent produces shallower generation and less precise review. Separating contexts prevents this.

### Recovery

If you're mid-generation and need to switch context: STOP → write the partial to a file → confirm path only → wait for next turn.

### Artifact reference

This document (`BOOK_WORKFLOW_SYSTEM.md`) is the canonical reference for WAVE + Three-Context. AGENTS.md holds the rule layer; this document holds the full system.

---

## File Write Verification — Full System

### The three levels

| Level | Checks | Use when |
|-------|---------|---------|
| L1 | File exists, size > 0 | Corpus drafts during batch write |
| L2 | L1 + readback + byte-exact content match | Ops files, specs, configs |
| L3 | L2 + SHA256 hash match | Anything with credentials, tokens, or PII |

### The six rules

1. **Per-file verification between writes.** Never: write → write → write → verify. Always: write → verify → write → verify.
2. **Readback on every L2 operation.** After writing an ops file, immediately read it back and confirm content matches.
3. **Hash check for L3.** For anything sensitive, compute SHA256 of sent vs. what was read back.
4. **Batch completion requires count + L1 check per file.** Report X of Y files confirmed before declaring batch done.
5. **Be explicit about what "verified" means.** Say "[L2 readback=match]" not just "confirmed."
6. **When in doubt, upgrade to L2.** L2 on a 5KB file costs ~same as the write. Silent failure costs a redo.

### The safe_write tool

Use `COUNCIL/scripts/safe_write.py` for all ops and critical work:

```bash
# L2 write (readback confirmed)
python3 COUNCIL/scripts/safe_write.py write /path/to/file.md "content" L2

# L1 batch write (fast)
python3 COUNCIL/scripts/safe_write.py batch /path/to/dir md "file1=content1" "file2=content2" L1

# L2 verify existing file
python3 COUNCIL/scripts/safe_write.py verify /path/to/file.md "$(cat /path/to/file.md)"

# L3 hash verify
python3 COUNCIL/scripts/safe_write.py verify-hash /path/to/file.md "<sha256_hex>"
```

### When to use safe_write.py vs. create_or_rewrite_file

| Situation | Method |
|-----------|--------|
| PERSONAL_OPS.md, COUNCIL files | `safe_write.py L2` |
| Multi-file corpus batch | `safe_write.py batch L1`, then L2 review |
| Spec or planning doc | `safe_write.py L2` |
| Large creative corpus drafts | `create_or_rewrite_file` → L1 count check after |
| Anything with credentials/tokens | `safe_write.py L3` |

---

## ITD Audit Protocol

**When to use:** Any time ITD (Integral Teal Design) is cited in a session.

**The sequence:**
1. Cast hexagram FIRST — active faces set which questions matter
2. Run all 6 ITD questions against the spec
3. Identify which of the 4 key concepts applies
4. Write the gap list
5. THEN write spec additions

**Never parallel** — audit first, writing second.

**Why this order:** ITD is an audit framework, not a writing framework. Trying to apply ITD while simultaneously writing spec additions causes working memory overflow and spec drift. The gap list is the output of the audit. Spec additions are the output of the gap list.

**The ITD reference card** (`docs/ITD_reference_card.md`) has all 6 questions, 4 concepts, audit protocol, and designer shadow checklist on one page. Use it — don't re-read the master doc.

**ITD + Hexagram rule:** Cast BEFORE audit. Active faces tell you which questions to deepen. See `docs/ITD_reference_card.md` face-to-question map.

**Pre-fail indicator:** If you feel like you need to "apply the framework" while also doing the work — stop. Audit first.