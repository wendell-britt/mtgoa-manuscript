---
type: panel
title: "Hostile review — the Chapter 8 reinclusion recommendations"
tags:
  - mtgoa
  - ch8
  - hostile-review
created: 2026-09-23
source:
  - specs/CH8_REINCLUSION_BRIEF_2026-09-23.md
  - specs/CH8_CUT_VS_REWRITE_2026-09-23.md
status: run, six of six, one cast (seed 20260923). Three claims in the brief broke. The plan narrows from "restore what siblings have" to "restore what something cites."
---

# Hostile review of the Chapter 8 reinclusion recommendations

**Wendell, 2026-09-23:** *"let's do a hostile review of these recommendations."*

**Bias, stated.** The brief was written by the reviewer ninety minutes earlier. Every claim that could be run was run before a Face spoke. Each of the six Faces read the brief and the files alone.

## Measured before anybody argues

| the brief claimed | measured | holds? |
|---|---|---|
| Ch3–7 each have a Section 5 daemon chapter; the rewrite has none | headings and `<!-- SECTION n -->` markers | **yes** |
| siblings' Take Out sections name the Appendix I superpower | ch7: *"the Connector's foundation"*; superpower names occur in ch3–7 | **yes** |
| every sibling has *From Read to Quest*; Ch9:161 needs a Sage quest | ch3–7: 1 each; rewrite 0 | **yes** |
| the rewrite has "no EA vocabulary at all" | no channel names, no alchemy; *angry* appears twice | **half** |
| "five BAR captures" lost | `grep -w BAR`: cut **4**, rewrite 0 | **BROKE** |
| the scene can stay as written | *"the Safe Self"* (ch8:347, 369, 373) appears in no other chapter and is defined nowhere. The daemon roster has seven names and it is not one | **BROKE** |
| the scene performs the five Moves (§4 table) | Faces read it row by row: V3 declines to switch games (ch8:353); V2 leaves a *table*, Move 4 puts down an *identity*; the team's correction is Move 1's test, and Move 5 has no beat | **BROKE** (rows 2, 4, 5, 6) |
| "the card grid" depends on Ch8's Moves | app grid = 60 cards, WAVE move × six Face levels × inner/outer (`grid.ts`); "twenty cards" is in no current chapter; no app code names Ch8's Moves | **false** |
| Ch9:76 and Ch9:441 depend on Ch8's Moves and daemon chapter | Ch9:76 names three capacities. Ch9:441 needs the *developed* Damaged Self as an asset (*"what you know because of what you survived"*) | **narrower** |
| the index depends on Ch8 | `instruments/index_build.py` derives it | **stale by derivation** |
| Chou needs an in-text credit | Chou is named in-text in no sibling (ch3–7, ch9: 0) | **sunk cost** |
| the brief is consistent | §7 R2 says restore EA whole; §8 and the chat summary say compress | **BROKE** |
| "+400 net" for the rewrite's Section 6 | it absorbs about 1,470 words of the rewrite | **hidden assumption** |
| restoring "verbatim from `3b37e4d`" gives clean text | `b89c60c` (trailing_and 799 → 0) is not an ancestor of `3b37e4d`. Ch8 exists in two lineages that differ by 309 lines | **BROKE** as a purity claim |
| the rewrite is body-anchored like its siblings | body words: 0.55 per 1,000 w against 1.43 in the cut region | **thinner** |

## The cast (one cast; seed 20260923)

*"Should Chapter 8 keep the altitude rewrite as its spine and bring the cut Section 5, the five Moves, the domain section, the exercises and Emotional Alchemy back around it, or is another shape right?"*

- **Hexagram 53, Steadfast** (Wind over Mountain). Patience, growth. *"Building a strong foundation is more important than endeavoring for high branches. Do not try to change your nature; instead, embrace your nature. Play to your own strengths."*
- **Changing line 4**, in the upper trigram: the pressure is in execution and the foundation is sound.
- **Hexagram 33, Withdraw.** Strategic retreat. Value turn: Patience, Growth → Strategic Retreat.
- Mountain (Clarity lives in what you refuse) is what the decision stands on. Wind (the strongest change is the one nobody noticed) is what it presents as.

The relating hexagram asked what the plan should withdraw from. The Faces answered.

## The six

**Shaman.** *What is this about underneath?* The grief of being right and unseen. The cut version held that grief once, in Alchemy Move 5 (Sadness → Poignance, cut:409–415). The rewrite's *What It Costs* states the loss as an epistemic fact and consoles with a payoff. The compressed EA path returns channel names and drops the felt paragraphs. The body thread closes only in the Walk Back (cut:513, 525), which P4 retires. **One finding:** "Safe Self" carries the scene's emotional center on a term with no owner.

**Challenger.** *What is the decisive move avoided?* Choosing what not to restore. The Tier-1 need is small: a quest, the Escape Artist and Coach naming, the credits. Restoring Section 5 whole answers sibling symmetry and no named dependency. Re-ran the brief's claims and failed four. **One finding:** the brief never cites CN-4 (the Walk Back is the only four-step sequence left), the strongest ground for retiring it, and never mentions the August list that argues against.

**Regent.** *What does this commit the season to?* Sorted the dependencies into load-bearing (Appendix I:17, Ch9:161, Ch9:575, the 08-03 domain ruling, Big Mind and Laloux credits), stale (card grid, index, Chou) and already met (Ch9:76, Ch9:441 by the untouched first half). Amending Ch9:575 costs the book's turn, so the rewrite is what bends. **One finding:** the text to restore predates the zero-target cleanup, so every restored word needs a scanner pass.

**Architect.** *What load does each element carry alone?* The second map has seven carriers. Two 3-2-1s run the same part. Two Tells check the same motive. Stand in Your Own Ground steps 1–3 compress Moves 1, 3 and 4, so restoring the Moves is a third pass. But/therefore: S4→S5 and S5→S6 are *and then*. **One finding:** rewrite:455 lists the retired Stage Sequence verbs as "moves at table altitude" and says the Sage's altitude has "nothing to do." Restoring the Moves collides with that sentence, and the brief never met it. *Who the Fight Makes You* and *Leave the Game Playable Without You* are defined nowhere.

**Diplomat.** *Whose standing changes?* Wendell called the rewrite's changes successful. The brief says "these stay," then dissolves the rewrite's Section 6. It also re-splits the merged Sections 4–5, which the tracker records as approved. E1 edits the rewrite's core reframing. **One finding:** ch9:441 frames the Damaged Self as an asset. The rewrite's Section 4 frames it as an ego seeking vindication, and the untouched first half frames it as difference converted to defect. Three definitions, one daemon.

**Sage.** *Is this the right question?* "Fit the Ch3–7 template" merges two tests: *promised elsewhere* and *sibling symmetry*. Rank by breakage, not resemblance. R5 and R2 were voids posed as branches. Withdraw Tier-2 symmetry, the 14,300 target, and any edit to Section 3's close. **The reconciling fact:** altitude is what she sees from, and the seat is where she sits. In the scene she stays seated (ch8:355–357), so "does not belong" describes the view and Section 3's close and Ch9:575 stand.

## Where the panel agrees, and where it splits

**Agreement.**
- D1 upheld: 5 of 6. Shaman amended it to add that the scene works partly because it is felt.
- D5 upheld: 6 of 6.
- D2 amended: 5 of 6. The "fits the book" frame splits into owed and symmetry. The packet did not suggest the split.
- The "+400 net" line hides the rewrite's loss: unanimous among those who checked.
- The 14,300 target has no method: 5 of 6.
- "Safe Self" is undefined: 4 of 6 carried it into their findings. The packet listed it, so this is confirmation and no independent discovery.

**Splits, kept as splits.**
- **EA.** Shaman: restore whole, because the compressed path returns only vocabulary. Regent and Diplomat: compress, keyed after the Moves. Sage: a ruling, because it was a void. The alchemy is keyed to five Modes and re-keying to Moves is not 1:1.
- **Walk Back.** Regent, Architect, Diplomat retire it. Shaman keeps the two embodiment lines.
- **The stance conflict.** Regent and Challenger amend the rewrite. Sage qualifies it by one fact. Diplomat asks Wendell to weigh the alternative of amending Section 3's close.

## Verdict on each recommendation

| item | verdict | decision |
|---|---|---|
| D1 the rewrite's working change | **upheld** | add: the scene works partly because it is felt |
| D2 fit = the Ch3–7 template | **amended** | split into *owed* and *symmetry* |
| D3 Tier-1 dependencies | **amended** | strike card grid, index, Chou, Ch9:76 as Moves-dependency; keep Ch9:161, 615, 575, Appendix I:17, credits, 08-03 domain ruling; Ch9:441 needs the developed Damaged Self |
| D4 scene performs the Moves | **reversed** | table withdrawn. The scene shows Move 1 (working vs performed), Move 3, and half of Move 4 |
| D5 Modes + Moves is convention | **upheld** | |
| P1 Section 5 whole | **amended** | restore as a section but compact: marginalia, the author's load-bearing-wall passage, the one-map limit, the mechanism, the Take Out, the 3-2-1 on the Damaged Self. Do not restage the single-beat scene (it repeats V1) |
| P2 Moves as beats | **amended** | five short named Moves, each with its own vignette. A beat locator for Moves 1 and 3 only. Trims quoted before and after, since compression is editing |
| P3 EA | **withdrawn** | not restored by default. Ruling R-A |
| P4 retire Walk Back | **upheld, amended** | retire the four-step form, record the override of the August list, keep Egan and the two embodiment lines |
| P5 3-2-1s verbatim | **amended** | restore the 3-2-1 on Your Damaged Self. *Reclaim* stays out: nothing in V3 supports the pairing |
| P6 E1 and R5 | **narrowed** | qualify ch8:365 and 397 with the one-line fact. Leave 359, 367, 371 and Section 3's close alone. "Forest" is a mechanical rename, flagged |
| P7 merge Section 6 | **reversed** | the rewrite's Section 6 stays the frame. One Tell (the rewrite's). The cut's four check-questions become proof lines under the four markers |
| P8 domain section | **upheld** | it is Wendell's 08-03 ruling, and it needs the Moves as antecedent |
| P9 credits | **amended** | Big Mind, Laloux, Egan. Chou dropped |
| P10 length 14,300 | **withdrawn** | length follows the owed list |
| P11 canon items | **amended** | add *Safe Self* and the Damaged Self definition drift |

## The revised plan

1. Restore what something cites: the quest, the Escape Artist and Coach Take Out, the credits, the domain section, the two named Moves Ch9:615 cites, the marginalia that Orr's *"Five of them and Bram"* counts.
2. Restore the five Moves compressed, with Ch9:76's three capacities carried by Moves 1, 2 and 3.
3. Keep the rewrite's Sections 4 and 6 as the frame.
4. Reconcile ch8:455 with one sentence: at the table there are moves, and the Sage makes them while standing on her own ground.
5. Every restored passage goes through the review pass, with each hit rewritten or ledgered.

**Length** follows from the list. Owed path: about 13,300 words (12,600–14,000, depending on how far the Moves compress). This is an outcome and no target.

**What this review cost the brief.** Six recommendations withdrawn or reversed, four amended, five upheld. The brief's biggest error was scope: it treated resemblance to Chapters 3–7 as a debt.

## Rulings for Wendell (world and author calls; no rewrite can settle them)

- **R-A · Emotional Alchemy in the Sage chapter.** Whole (Shaman), one move (Sadness → Poignance) plus the table, or none. Default: none.
- **R-B · Two names to fix.** *Safe Self*: which of the seven is it? And *Escape Artist*: Appendix I says it quits a game whole, the app says it sorts wise retreat from flight. Which one does the chapter teach?
- **R-C · The stance.** Qualify "does not belong" at 365 and 397 (default), or keep it and amend Section 3's close. And whether a restored Section 5 un-merges Sections 4–5, which the tracker records as approved.
- **R-D · Symmetry items** (Draw the Axis, Ecology, *Reclaim* 3-2-1, EA table, Modes). Default: off.

**Lineage.** Chapter 8 exists as `3b37e4d` (Sept-22 early daemon, no zero pass) and on `editorial/trailing-and-zero-2026-09-10` (zero pass, older structure). Choosing the source is Wendell's call, and merging the lineages is a separate decision.
