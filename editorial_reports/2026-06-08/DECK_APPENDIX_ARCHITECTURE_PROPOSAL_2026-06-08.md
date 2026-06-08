# Deck Appendix — Architecture Proposal (resolves the open fork)

**Date:** 2026-06-08
**Status:** PROPOSAL (workspace surface). Canon promotion happens in Obsidian with Wendell's approval.
**Resolves:** the ship-week OPEN FORK — "~40 Section-6 Face-moves → WCGS suit×rank grid" — and the long-standing suit-mapping inconsistency across the April deck artifacts.

---

## 1. The problem this resolves

The deck has never had a consistent spine. Three April artifacts disagree:

| Artifact | Suit → phase mapping | Suit axis |
|---|---|---|
| `CARD_DECK_ARCHITECTURE_ANALYSIS.md` | Hearts=Wake, Diamonds=Clean, Clubs=Grow, Spades=Show | 4 Domains |
| `MTGOA_CARD_ARCHITECTURE_FINAL.md` | Hearts=Wake, Diamonds=Grow, Clubs=Show, Spades=Clean | 4 Domains |
| `MTGOA_52CARDS_PROMPTS.json` | `gr_01` = Clubs + Spring + Wake (unaligned) | 4 Domains |

Two problems: (a) the suit↔WCGS assignment differs in every file, and one even orders the phases Wake/Grow/Show/Clean — **not** the canonical WAVE-Spiral sequence; (b) all three make **suits = the 4 Allyship Domains**, which the June pivot overrides.

There are *three* competing 4-fold systems in play — **WCGS** (the milestones), the **6–7 Faces** (the chapters), and the **4 campaign Domains** (Gathering / Organizing / Action / Awareness). They were fighting for the same axis. The fix is to give each a different job.

---

## 2. The resolution — three axes, three jobs

```
SUIT      = WCGS milestone   (the deck's structural spine)   — 4 suits
LENS      = Face             (the voice that runs the card)   — tag on each card
CONTENT   = Domain / move    (what the card actually asks)    — the card body
```

### Suits = WCGS (per the pivot, in canonical WAVE-Spiral order)

| Suit | Milestone | What the card does | Tone |
|---|---|---|---|
| ♠ Spades | **Wake** | notice the signal; name the game/feeling | recognize, establish |
| ♥ Hearts | **Clean** | strip the distortion; get to the clear read | discern, clarify |
| ♦ Diamonds | **Grow** | let it teach you; integrate the lesson | integrate, deepen |
| ♣ Clubs | **Show** | make the move; act; hand it forward | act, transmit |

This matches the Ch2 WAVE-Spiral (now fixed to Wake/Clean/Grow/Show) and the Wilber lineage. **13 ranks × 4 suits = 52.**

### Faces = the guide lens (not a suit)

Each card carries a **Face lens** — the voice that knows how to play that card (Shaman/Challenger/Regent/Architect/Diplomat/Sage; Player = the meta-host / the rules card / the "you"). This is already a field in the JSON (`domain_guide_lens`). Faces ride *on* the grid; they are not the grid. That dissolves the WCGS-vs-Faces collision.

### Domains = content, not structure

The 4 campaign Domains survive as the **Ch0 "Campaigns"** layer — *what you are working on*. Some cards are domain-campaign prompts; they live inside whichever WCGS suit their phase belongs to. Domains stop competing for the suit axis and become card content. (This keeps the reconciled Ch0 spine — tokens → tickets → **campaigns** → prize — visible in the deck.)

---

## 3. How the ~40 Section-6 moves populate the grid

The pivot's principle: **"the Section-6 Moves ARE the cards"** and the appendix is **mostly extraction, not net-new writing.** Method:

1. Each chapter's Section-6 has 5 named Moves (Move 1–5). ~7 Faces × 5 ≈ 35–40 moves.
2. **Each move is filed under the WCGS suit it enacts** (its dominant milestone) and tagged with its Face lens.
3. A move's **rank** within the suit reflects depth/sequence (Ace = the cleanest entry instance of that milestone; higher pips = more demanding instances).
4. Remaining slots (52 − the move-cards) are filled by the existing JSON's **domain-campaign prompts** (resource/organizing/action/awareness questions) — already written, re-filed by phase. Net-new writing ≈ minimal.
5. Each card's **back** = the BAR template (Breakthrough / Action / Reflection / Sustain), unchanged from the JSON.

**Judgment call this surfaces:** a Face has 5 moves but there are 4 suits, so moves don't map 1-per-suit. Some Faces will weight toward one or two milestones (e.g., the Challenger lives mostly in Show; the Shaman mostly in Wake/Clean). That distribution is a design choice — see the worked example.

---

## 4. Worked example — the Sage's 5 moves → WCGS (proof of method)

Using Ch7 (the benchmark). Sage tool = See → Switch → Serve → Release → Return; Section-6 moves = Name the Game / Switch Games Deliberately / Serve the Room / Put a Game Down / Return Without Condescension.

| Section-6 move | Enacts | Suit (WCGS) | Card title | Face lens |
|---|---|---|---|---|
| Name the Game | noticing what's really happening | ♠ Wake | *Name the Game* | Sage |
| Switch Games Deliberately | choosing the right game, clear-eyed | ♥ Clean | *Switch Deliberately* | Sage |
| Serve the Room | doing what the game requires | ♣ Show | *Serve the Room* | Sage |
| Put a Game Down / Return | releasing, then re-entering integrated | ♦ Grow | *Put It Down, Come Back* | Sage |
| Return Without Condescension | acting from the integrated place | ♣ Show | *Return Without Condescension* | Sage |

So the Sage contributes 1 Wake, 1 Clean, 1 Grow, 2 Show cards. The weighting is the data: the Sage's gift is mostly *Wake* (seeing) resolved into *Show* (moving), which is exactly the chapter's thesis ("stop mistaking perspective for action"). **The mapping is faithful when the per-Face suit-distribution mirrors that Face's actual center of gravity.** That is the test to apply across all 7 Faces.

---

## 5. Appendix letter / placement

Letters are locked A–G (A Domains / B Quests / C Key Terms / D Emotional Alchemy / E 3-2-1 Shadow / F Polarity / G On the Shoulders Of). The deck needs a new letter. Two reasonable placements:
- **Appendix H** — after the existing set, before/with the bibliography tail. Lowest disruption.
- **Featured / Appendix A-prime** — the deck is the book's practiceable centerpiece; it may deserve to lead the back matter rather than sit last. Higher disruption (renumbers cross-refs).

Recommend **Appendix H** for ship-week (zero cross-ref churn); revisit prominence post-launch.

---

## 6. The 52 → 64 relationship (one paragraph of canon, per the pivot)

The **52-card deck** is the practiceable layer (4 WCGS suits × 13, one standard playing deck, lives in this appendix). The **64-card codex** is the depth/oracle layer (8 gates × 8 = I Ching hexagrams), post-launch, routed to the app. The 52 is what you *play weekly*; the 64 is what you *consult* for shadow/gate depth. Do not cram 64 into 52 this week — they are different instruments sharing the same WCGS/Face/gate vocabulary.

---

## 7. What's genuinely Wendell's call before I generate all 52

1. **Domains as content layer** — confirm the 4 campaign Domains become card *content* (not the suit axis), keeping the Ch0 campaigns visible. (Recommended.)
2. **Per-Face suit weighting** — accept "map each move to its dominant milestone, let the distribution be uneven" (the Sage example), or impose a fixed quota per Face?
3. **Appendix letter** — H (recommended) vs featured placement.
4. **Player as meta** — treat Player (Ch8) as the deck's rules/host card(s) rather than a Face with its own pip cards? (Keeps the move count near 52 and honors Player-as-meta.)

Once these are set, the build is largely extraction: re-key the existing 52-card JSON to suits=WCGS, attach each card's Section-6 move + Face lens, and render the appendix table.
