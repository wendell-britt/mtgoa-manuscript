# MTGOA Book Production — Process Architecture
## *Spec → Plan → Tasks → Execute → Verify → Iterate*

**Created:** 2026-04-16
**Source:** RCA session + research synthesis

---

## The Problem We're Solving

We lose work when:
1. Content generation is embedded in Python (JSON payload limit)
2. Specs aren't saved before seeking approval
3. No verification step after writes
4. No intermediate planning layer between spec and execution
5. Vibe coding (react to failure) vs formal ceremony (spec → execute → verify)

---

## The 4-File Production System

Every chapter follows this sequence:

### File 1: `ch{N}-{face}/SPEC.md` — Written by AI from template + matrix, signed off by Wendell
### File 2: `ch{N}-{face}/PLAN.md` — Written by AI from SPEC, signed off by Wendell
### File 3: `ch{N}-{face}/TASKS.md` — Written by AI from PLAN, signed off by Wendell
### File 4: `ch{N}-{face}/DRAFT.md` — Written by AI from TASKS, verified by AI

**Rule: Save before seeking approval. Never block on approval to save.**

---

## Content Generation Rules

**NEVER pass chapter content through Python/JSON.** Instead:

**Generate:** Content written as plain Python string literals in scripts (≤5,000 chars per script)
**Save:** Python `with open(path, 'a') as f: f.write(content)` — pure file operation, no JSON
**Verify:** Immediate `wc -l` + `grep -c "^## Section"` + compare to TASKS.md expected count

**If script exceeds ~200 lines:** Split into two scripts. No exceptions.

---

## Verification Protocol (After Every Write)

After every file write, verify against TASKS.md:

```
Expected sections:  [from TASKS.md]
Actual sections:    [from grep -c "^## Section" draft.md]
Expected words:     [from TASKS.md]
Actual words:       [from wc -w draft.md]
Status:             PASS / FAIL
```

**If FAIL:** Stop. Diagnose. Do not continue to next section.

---

## The 4-Step Execution Pattern

For each section in TASKS.md:

1. **Read** the relevant spec/plan/tasks for this section
2. **Generate** content as plain string (≤5,000 chars)
3. **Save** via Python script (no content in JSON payload)
4. **Verify** against TASKS.md expected output

**Then only then:** Confirm path only in chat.

---

## Current Book State

| Chapter | SPEC | PLAN | TASKS | DRAFT | Verified |
|---------|------|------|-------|-------|---------|
| Ch2 Shaman | ✅ | — | — | ✅ 10,280w | — |
| Ch3 Challenger | ✅ | — | — | ✅ 8,195w | — |
| Ch4 Regent | ✅ | — | — | ✅ 6,299w | — |
| Ch5 Architect | ✅ | — | — | ⚠️ 2,695w | FAIL |
| Ch6 Diplomat | ✅ | — | — | ⏳ | — |
| Ch7 Sage | ✅ | — | — | ⏳ | — |

---

## Next Session Priority

1. Write Architect PLAN.md and TASKS.md
2. Write Architect S5-S7 using 4-step pattern
3. Write Diplomat + Sage PLAN + TASKS + DRAFT

---

## Applied to This Session

**Would have prevented:**
- Architect S5-S7 lost 3x → 4-file system + save-before-approve + verify would have caught it
- Chapter audit took 45 min → verification after each write would have caught in seconds
- Specs not saving before approval → rule is now save-first, never block

**Research sources:**
- Cursor SubAgent pattern (Zvi Schreiber, LinkedIn)
- GitHub Spec Kit (Michael Hoffmann)
- JetBrains Junie 4-file system
- Addy Osmani LLM coding workflow
- r/claudexplorers iterative prose workflow
