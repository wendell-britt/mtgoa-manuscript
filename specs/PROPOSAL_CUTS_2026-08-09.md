# Proposal — the length cuts, ruled by the six Faces

**2026-08-09. Wendell:** *"The book is coming in a bit long so if there's anything that can be
solved with aggressive cuts across all chapters, we can keep it for the repo but remove from
the book, then we'll sand down any edges that emerge from those cuts."*

**Status: PROPOSAL. Nothing in this document has been applied.**

This supersedes spec §6's no-restructuring rule by the author's instruction, for the cuts
listed here and nothing else.

## The numbers

Body: **120,042 words** across ch1–ch9 (ch3 longest at 17.6k; ch7 and ch8 both over 16k).
Workbook interior: 404 pages, ≈308 body-words per page.

The eight readers' drag zones measure **9,329 words of territory**. Not all of it is cuttable
— the zones contain protected structure — and the honest deletion-only yield is:

**Tier 1 (pure deletions): ≈4,300 words ≈ 14 pages.**
**Tier 2 (compression surgery, if wanted): ≈3–5k more, at real risk.** See the Sage.

---

## The six analyses

**Shaman — cut where the charge is dead, never where it is live.** The readers marked exactly
which stretches survive on scenes: ch7's Modes 3 and 5 live because the retro and the
swallowed *no* are in them, Modes 1–2 sag because they are definition. Every cut below removes
*restatement* — the third telling, the summary of a thing just shown, the definition after
the scene already taught it. **No scene, no Example, no named person leaves the book.**

**Challenger — whole blocks, cleanly.** The temptation is a 10% trim everywhere, which leaves
every drag in place at 90% of its size and blurs a hundred paragraphs. The clean no is: the
third restatement goes entirely, the first stays entirely. Every cut below is a block with a
boundary, deletable in one motion, so the sand-down pass works on a few seams rather than
everywhere.

**Regent — the protected inheritance, named before anything moves.** Nothing on this list is
touched even where it sits inside a cut zone: the cross-chapter formulas (The Tell · How to X
So It Y · the exile closers · the axis sentences · RECEIPT lines · the 24 domain blocks · the
Ecology sentence) · everything the index locates (all of Ch 3 §4's channel and satisfied-state
content) · every `>` block and comment-fenced device (other hands; and marginalia anchors must
still resolve) · every named move · the concealed ladder structure · the WAVE stage headings.

**Architect — the mechanism that makes the cuts safe.**
1. Every removed passage is copied **verbatim** into `specs/CUTS_ARCHIVE_2026-08-09.md`
   before deletion — "keep it for the repo" as a readable file, not git archaeology.
2. Cuts land **one chapter per commit**, board re-run each time: gate, review, xref, dupes,
   `index_build --check`, marginalia round-trip.
3. The sand-down is a **separate sitting after all cuts land**, reading each seam in place —
   never written blind into the cutting commit.
4. The cuts repaginate the book, so the page-level proof re-runs **once, at the end**, not
   per chapter.

**Diplomat — Jordan keeps everything Jordan stops for.** Jordan skims theory, never skips a
story, stops for a named move with a practice, and drops off at moralizing and repetition.
Every cut below removes what Jordan skims. Two cuts actively *serve* Jordan: the first
coaching offer interrupts the Founder teaching mid-flow (selling inside teaching is a listed
drop-off trigger), and ch9's recap litany is the third telling of material Jordan has already
been tested on.

**Sage — which game is being played.** These cuts buy **~14 pages of a 404-page book**. If
"a bit long" means 390 pages, this proposal solves it. If it means 340, that is a different
game — compressing the five-mode deep-dive template across five chapters — and it is surgery
on the book's teaching spine at final proof, with a full re-review per chapter. The Sage's
counsel: **take Tier 1 now, judge the built result, and only then decide whether Tier 2's
game is worth entering.**

---

## Tier 1 — the cut list (≈4,300 words)

| # | site | what goes | ≈words |
|---|---|---|---|
| 1 | ch3 §3 (189–215) | three of the five same-template feeling paragraphs; first and strongest stay | 380 |
| 2 | ch3 §4 (302–422) | the *This might look like* bullet lists under Grow and Show, after the prose has made the point; stage headings and prose stay | 320 |
| 3 | ch4 §4 (273–295) | two of the five EA-channel expansion paragraphs (the table and three strongest stay) | 250 |
| 4 | ch4 (≈448–462) | the third untitled first-person block — the thesis restart after the reader has the practice | 250 |
| 5 | ch4:741 clause + ch4:543 restate | the duplicated mild-irritation line; the weather-image restatement trimmed to its callback | 60 |
| 6 | ch5 §3 (≈238–246) | two of the four five-stage restatements (arrows version and one prose rerun); Polarity Encounter untouched | 120 |
| 7 | ch7 Mode 2 (305–368) | the definition-only prose between Elian's marginalia blocks; both alchemies and all `>` blocks stay | 300 |
| 8 | ch7 (777–795) | the *Where You'll Actually Spend the Close* inventory; the three-move block, How to Close It and The Tell stay | 350 |
| 9 | ch8 (407–460) | the fourth telling of Panoramic Seer → Returner — the block the reader stops paying at | 600 |
| 10 | ch9 recap (234–320) | the third six-Faces litany compressed to its *you now know* spine | 600 |
| 11 | ch9 (440–460) | the sixth telling of *the walk includes failure* | 250 |
| 12 | ch9 (153–161) | the first coaching offer; a one-line pointer to the closing offer stays | 240 |
| 13 | ch9 (190–196) | the second coaching offer — the Founder branch already reappears at 684 | 150 |
| 14 | ch9 (≈141) | the duplicated memoir beat merged into its first telling | 50 |

**Held back for individual rulings, not in the batch:** ch7's repeated Elian Cross sentence
(46 ↔ 139) and ch8's handbook echo (47 ↔ 226) — both may be deliberate signatures of those
Heads, and each is one sentence either way.

## What Tier 1 does not fix

ch2's structural drags (the four-job opening run, the three-rosters overload) are *ordering*
problems, not length problems — cuts do not touch them, and they stay second-edition. The
same for ch6's mid-chapter register drop into Irix's first person.

## The order, if approved

1. `CUTS_ARCHIVE` opened; cuts land ch3 → ch9, one commit per chapter, board green each time.
2. Sand-down sitting: every seam read in place, repairs shown as diffs.
3. Full rebuild, page-level proof re-run, index rebuilt and checked.
4. The log records each cut and each seam repair.
