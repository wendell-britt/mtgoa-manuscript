# SPEC — Gate 5 Fix Across All Chapters
**Date:** 2026-05-22
**Authority:** Wendell Britt
**Based on:** `RCA_GATE5_MISS.md` (root cause analysis) + `GATE5_INTERPRETATION_SPEC.md` (interpretation audit)
**Status:** ✅ CONFIRMED — Option A

---

## Background

Gate 5 (Emotional Body / The Fear / Fear — Fear / Already Alone) is inconsistently labeled across Ch1–Ch6. The inconsistency wasn't caught for 5 weeks because:

1. No canonical structural definition existed for Gate 5's identity
2. The hostile editorial pass was chapter-scoped, not cross-chapter
3. EA channel labels (Metal/Fear) and WAVE tactical states (Fear as Charge state) were conflated with the gate's structural identity

---

## Interpretation Decision Required

**Before any chapter edits can proceed, Wendell needs to confirm one of three options:**

### Option A — Gate 5 is always the Emotional Body (Structural Identity)

Gate 5's structural identity = "The Emotional Body." This is fixed and canonical. The gate is defined by its *function* (feeling, processing, relating to emotional charge) not by any particular emotional state.

- "The Fear" becomes a descriptive phrase about *one possible state* the Emotional Body can be in — not the gate's name
- All chapters get labeled: "Gate 5: The Emotional Body"
- WAVE state language (Clean/Charge/Flood/Resolve) used separately when describing the Emotional Body's tactical condition
- EA channel language (Metal/Fear, Water/Sadness, etc.) used when describing EA-specific emotional processing modes

**Chapters to change:** Ch1 (already correct — keep), Ch2 (relabel), Ch3 (relabel), Ch4 (relabel), Ch5 (relabel), Ch6 (relabel)

### Option B — Gate 5 has face-emergent labels (Face-Specific)

Each face gets to name Gate 5 in its own voice, as long as the underlying mechanics are consistent. "The Fear" in the Challenger/Regent chapters reflects how those faces specifically encounter the Emotional Body — through fear. "Already Alone" in the Diplomat reflects how that face specifically encounters it.

- Canonical = face-emergent diversity, not structural uniformity
- Each chapter's Gate 5 label reflects the face's relationship to the Emotional Body
- No cross-chapter consistency required beyond mechanical soundness

**Chapters to change:** None — difference is intentional and valid. Validate mechanical consistency instead.

### Option C — Gate 5 is the WAVE Charge state system (Tactical)

Gate 5 is the tactical moment when the Emotional Body is in a Charge state. "The Fear" is the label for that tactical state — not the gate's identity. The gate is about *how the Emotional Body moves in Charge* — and fear is one common Charge-state expression.

- "Gate 5: The Emotional Body (Charge State — Fear)" as the canonical label form
- Each chapter describes what Charge state the Emotional Body is experiencing at Gate 5
- EA channels (Metal/Fear etc.) are separate — they describe the quality of the emotional experience, not the gate's tactical function

**Chapters to change:** All — standardize to the canonical label form

---

## Fix Protocol (for all chapters)

For each chapter, the fix involves:

**1. Relabel the gate**
- Find: `### Gate 5: [current label]` or `#### Gate 5: [current label]`
- Replace label with canonical form per chosen option
- Preserve all subsection content (trigger, reframe, moves, BAR prompt, etc.)

**2. Audit the gate body**
- Check all references to "Gate 5" in the body text — update label consistency
- Check all references to "The Fear" or "fear" as a gate identity — confirm whether it's referring to the WAVE state or the EA channel
- Add clarifying language if the WAVE/EA distinction matters in that chapter's context

**3. Check oracle card**
- Card 5 for this chapter should reference Gate 5 — verify card text is consistent with chosen interpretation
- Reference: `HEXAGRAM_CARDS_CH[N]_[FACE].md`

**4. Validate cross-chapter consistency**
- After all chapters are updated, run the gate label audit script to confirm all 8 gates in all chapters are consistently labeled

---

## Chapter-Specific Changes

| Chapter | Current Label | Required Change | Notes |
|---------|--------------|-----------------|-------|
| Ch1 Forest | "Emotional Body" | Keep — already correct | Verify gate subsections don't use "The Fear" incorrectly |
| Ch2 Shaman | "Fear" | Relabel to "Emotional Body" or chosen option | Also check oracle card text |
| Ch3 Challenger | "The Fear" | Relabel | "The Fear" becomes descriptive phrase, not gate name |
| Ch4 Regent | "The Fear" | Relabel | Same — "The Fear" becomes contextual, not structural |
| Ch5 Architect | "Fear — Fear" | Relabel | First "Fear" = gate label, second "Fear" = EA channel — clarify this distinction |
| Ch6 Diplomat | "Already Alone" | Relabel or document as face-emergent (Option B) | "Already Alone" is a valid face-specific description if Option B |
| Ch7 Sage | Not found in draft | Audit — locate or confirm Gate 5 doesn't exist in this chapter's structure | |
| Ch8 Player | Not found in draft | Audit — locate or confirm Gate 5 doesn't exist in this chapter's structure | |

---

## Validation

**Post-fix audit script** — run after all chapter edits:
```bash
python3 << 'PYEOF'
import re
chapters = {
    "Ch1": "manuscripts/chapters/ch1-SHAMAN/CHAPTER1_FULL_DRAFT.md",
    "Ch2": "manuscripts/chapters/ch2-SHAMAN/CHAPTER2_SHAMAN_FULL_DRAFT.md",
    # ... etc
}
for name, path in chapters.items():
    content = open(path).read()
    gates = re.findall(r'(?:###|####) Gate (\d+).*?: (.+)', content)
    print(f"=== {name} ===")
    for g, label in gates:
        print(f"  Gate {g}: {label}")
PYEOF
```

Expected output: All Gate 5 labels are identical across all chapters.

---

## Related Documents

- `RCA_GATE5_MISS.md` — root cause analysis of why drift wasn't caught
- `GATE5_INTERPRETATION_SPEC.md` — interpretation audit across all chapters
- `AD-2026-0522-002` — architectural decision placeholder (waiting on this spec's resolution)

---

## Next Action

**Wendell:** Choose Option A, B, or C. Once confirmed, the fix protocol can be applied to all chapters.