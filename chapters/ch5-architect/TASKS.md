# TASKS.md — Chapter 5: The Architect
## *Orange — Strategic Design*

**Created:** 2026-04-16
**Based on:** PLAN.md

---

## Gap: Sections 5-7

S1-S4 already written and verified (149 lines, 4 sections confirmed).
Target: add S5-S7, verify all 7 sections present, total ~10,700 words.

---

## Section 5: Journey to the Center (~4,500 words)

**Task:** Write full immersive 8-gate walk for Orange altitude.

**Map (700 words):**
- All 8 gates with Says/Job
- Through-line: capacity to design clearly without losing sight of what it's for

**Walk (~3,800 words):**
- Gate 1 Protector: "Not safe to commit to this blueprint. You don't have enough data."
- Gate 2 Controller: "If you ship this, you can't take it back."
- Gate 3 Skeptic: "Is this even a problem worth solving?"
- Gate 4 Fixer: "Don't think — execute."
- Gate 5 Fear: Naming move. Author names their own design fear. (Use jeppi-style named part)
- Gate 6 Victim: Disowned voice. "I can't design at scale because I wasn't given the resources."
- Gate 7 Damaged Self: Witness without fixing. "I'm not actually smart enough."
- Gate 8 Vulnerable Child: "I love the elegant solution. Design is a form of love."

**Superpower at center:** Structural generosity — the blueprint as act of love

**Must include:** Gradient (thank → ask → name → listen → witness → hold) + "When you're ready, keep walking" after Gates 1-7
**Must include:** Closing coda after Gate 8 (~100-150 words)

---

## Section 6: The Game (~1,000 words)

**Task:** Write 5 concrete ally moves for Architect altitude.

**Structure:**
- Opener: "You've learned strategic design. Now—what does it look like in practice?"
- 5 named moves, each with: title, 1-2 sentence description, "Why?", "In practice:"

**5 Moves:**
1. **Find the Leverage Point** — Where does the smallest push create the largest movement?
2. **Name the Unstated Assumption** — What is everyone treating as given that isn't?
3. **Design for Handoff** — Build it so someone else can run it without you.
4. **Ship the Minimum** — Get the design into contact with reality before it's perfect.
5. **Refactor Kindly** — Change the design without shaming the version that got you here.

**Subsections required:** Split into 2-3 Python script files per template design rule.

---

## Section 7: Recap and Transition (~500 words)

**Task:** Close with what Architect contributes + bridge to Diplomat.

**Must include:**
- One-sentence thesis: "The Architect's contribution is: structural generosity."
- 2-3 carry-forward bullets
- Bridge: "The Architect can design the system but cannot hold the relational field the design lives inside."
- Closing: "Now you're ready for the Diplomat."

---

## Verification Checkpoints

After writing each section:

```
grep -c "^## Section" CHAPTER5_ARCHITECT_FULL_DRAFT.md
# Expected: 7

wc -w CHAPTER5_ARCHITECT_FULL_DRAFT.md
# Expected: ~10,000-11,000

grep "^## Section" CHAPTER5_ARCHITECT_FULL_DRAFT.md
# Expected: Exile, Distortion, Concept, Practice, Journey, Game, Recap
```

---

## Execution

- Write via Python script (content as string literals, no JSON payload)
- One section per script
- Verify after each write
- Confirm path only after all 7 sections verified
