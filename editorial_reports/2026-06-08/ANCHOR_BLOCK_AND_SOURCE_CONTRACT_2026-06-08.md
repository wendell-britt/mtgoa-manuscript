# Anchor Block + Source Contract — Reanchoring Instruments

**Date:** 2026-06-08
**Status:** PROPOSAL (workspace surface). Canon promotion happens in Obsidian with Wendell's approval.
**Purpose:** Stop the simplified chapters from drifting away from the four-source fusion (10K HP, ILP, Skilled Helper, Existential Kink) during compression passes.

The problem these instruments solve: compression keeps cutting load-bearing material as if it were excess, and rewriting keeps mutating coined/cited terms — because **nothing pins the source-intent to the page.** The protocol spec is a separate file nobody re-reads mid-edit. These two instruments make every future pass *re-anchor* instead of *re-derive*.

---

## Instrument 1 — The Anchor Block

A ~15-line block pinned at the **top of each chapter file** (and its canonical Obsidian source), written as an HTML comment so it travels with the text but never renders in the book.

Every editing or compression pass reads the Anchor Block first. The rule: **you may cut anything that is not protected by the Anchor Block; you may not cut, rename, or paraphrase anything that is.**

### Template

```
<!-- =========================== ANCHOR BLOCK ===========================
CHAPTER:    <n — Face>
ONE IDEA:   <the single allyship problem this chapter solves — one sentence>
ONE TOOL:   <named practice + LOCKED stage names, verbatim>
WELLBEING:  <the kind of well-being this Face/altitude defines — protocol's allyship addition>

SOURCE BEATS (all must survive compression; the source named owns that beat):
  Promise   [EK]   — bold claim, fast; the reader knows what the chapter is FOR
  Diagnosis [Egan] — the distortion/exile/misconception that keeps the problem alive
  Tool      [ILP]  — one module, taught at two speeds (quick version + deeper version)
  Examples  [10K]  — multiple worked real-world tests of the tool
  Practice  [Egan] — one concrete "It's Your Turn" implementation move
  Safety    [EK]   — objection-handling / "what this is NOT / when not to use it"
  Handoff   [10K]  — highlights recap → next chapter

LOCKED TERMS: <coined/cited terms that must appear verbatim — never paraphrased or "tidied">
LINEAGE:      <citations that anchor the tool — author/work; these are the credibility anchor>
DEEP-LAYER HOME: <where the demoted depth lives — appendix letter / deck card / coaching asset>
DO-NOT-DRIFT: <chapter-specific traps: an acronym that wants to "self-correct," a spine term at risk>
==================================================================== -->
```

### Rules of use

1. **Read it first, every pass.** The Anchor Block is the contract; the chapter prose is the implementation.
2. **Locked terms are pasted, not typed.** When prose must be rewritten, coined/cited terms come verbatim from `LOCKED TERMS`. (This is what would have prevented the Ch2 `WAVE → Wake/Acknowledge/Validate/Exhale` mutation.)
3. **A beat may be compressed to a sentence but never to zero.** If a source-beat would disappear, that's drift — flag it, don't ship it. (The `Safety [EK]` beat is the one most often dropped.)
4. **Demote, never delete.** Anything cut for length goes to its `DEEP-LAYER HOME`, never to nothing. That is what keeps ILP's modularity real instead of cosmetic.

---

## Instrument 2 — The Source Contract

One table, book-level. Each source owns exactly one structural job. Drift = one source's job quietly eating another's. After every compression pass, run the **presence test** column as a yes/no checklist per chapter — that *is* the drift audit.

| Source | Job it owns | Beat(s) it anchors | Presence test (Y/N per chapter) | What's lost if it drifts |
|---|---|---|---|---|
| **10K Hours of Play** | Repeatable rhythm + visible next step | Promise → … → Highlights/Handoff | Does the chapter open with a clear promise and close with a recap + named next move? | Reader stops feeling "I got one complete thing" |
| **Integral Life Practice** | Modularity / multi-speed; deep layer relocates, not deletes | Tool + Practice (quick + deep) | Is the tool taught at two speeds, AND does the deep layer have a named home? | Chapter re-bloats or over-thins; "deeper version" vanishes |
| **Skilled Helper (Egan)** | Staged process + reader agency + "what can go wrong" | Diagnosis → Tool → Practice | Is there a staged move (not a pile), and is reader kept in the driver's seat? | Reader becomes passenger; honesty about difficulty disappears |
| **Existential Kink (Elliott)** | Provocative compactness + objection-handling safety valve | Promise (bold) + Safety (Q&A / "what this is NOT") | Is there a dedicated objection/safety section? | Chapter reads as overclaim; resistance-lowering layer gone |

**Protocol overlay (the allyship-wellbeing addition):** each chapter must also *define the well-being that matters at its Face* — Shaman: felt relief/emotional truth; Challenger: clarity/protected space; Regent: continuity/stewardship; Architect: leverage/design; Diplomat: mutuality/trust; Sage: perspective with commitment; Player: ongoing play that keeps it alive. Presence test: *does the chapter name its kind of well-being?*

---

## Worked example — Ch7 (the benchmark)

Ch7 is the chapter that drifted least (it was built from a reverse outline, not rewritten). Its filled Anchor Block, which gets prepended to `CHAPTER7_SIMPLIFIED_DRAFT_2026-06-08.md`:

```
<!-- =========================== ANCHOR BLOCK ===========================
CHAPTER:    7 — The Sage
ONE IDEA:   Sage altitude helps you stop mistaking perspective for action —
            you see the whole board without turning that view into a hiding place.
ONE TOOL:   See -> Switch -> Serve -> Release -> Return   (5 moves, in this order, these names)
WELLBEING:  Perspective with commitment (not detachment; you come back down and stay present)

SOURCE BEATS (all must survive compression):
  Promise   [EK]   — "the Sage is not the one who sees farthest, but who sees the whole board
                      without making it a hiding place"
  Diagnosis [Egan] — the exile (village hears seeing as leaving) + the distortion (naming without
                      choosing; perspective as a place to stand ABOVE the room)
  Tool      [ILP]  — See/Switch/Serve/Release/Return, taught at two speeds:
                      full 9-step (S5) + the 4-question simpler version (S5)
  Examples  [10K]  — the strategy-vs-power room; the harmony-game room; the overexplain/rescue list
  Practice  [Egan] — "Try this with one real situation" (S5) + BAR-style capture
  Safety    [EK]   — *** CURRENTLY THIN. Only the half-line "if someone is in immediate danger,
                      act." NEEDS a real objection beat: "when seeing becomes stalling / when the
                      high view is avoidance / inner work is not a delay tactic." ***
  Handoff   [10K]  — recap (what Sage gives / does not give) -> Player ("what am I building now?")

LOCKED TERMS: "See -> Switch -> Serve -> Release -> Return"; "perspective with commitment";
              "Trauma Olympics"; "Captain Save-a-Kid"; "Dragging horses to water";
              "the Sage in distortion" (NOT "shadow Sage" — WB-10); "Effective Allyship Formula"
LINEAGE:      Wilber (integral/Teal stage) [^wilber]; Laloux (Teal orgs) [^laloux]
              — credit inline/footnote, Spiral COLOR labels stay submerged (WB-9)
DEEP-LAYER HOME: five-mode alchemy expansion, full forest/gate walk, Face-by-Face developmental
              map -> Appendix / deck cards (the chapter's DEMOTED list already itemizes these)
DO-NOT-DRIFT: (1) keep "altitude" submerged — generic "high view" OK, no Spiral ladder/colors.
              (2) Safety beat is the known gap — do not let the next pass "clean it up" into nothing;
                  it needs MORE, not less.
==================================================================== -->
```

### Source Contract scorecard for Ch7

| Source | Present? | Note |
|---|---|---|
| 10K HP (rhythm/handoff) | ✅ | Clean promise; strong recap + Player handoff |
| ILP (multi-speed + deep home) | ✅ | 9-step + 4-question simpler version; deep layer itemized in DEMOTED list |
| Egan (staged + agency) | ✅ | See/Switch/Serve/Release/Return is a true staged process; reader in driver's seat |
| EK (objection/safety valve) | ⚠️ **GAP** | Only a half-line. This is the one beat to add. |
| Wellbeing defined | ✅ | "perspective with commitment" stated explicitly |

**Action falling out of Ch7's own Anchor Block:** add a short Safety/objection beat — "When seeing becomes stalling" — before the Summary. Everything else holds.
