# Tier 2 — the surgical pass, specced before a word moves

**2026-08-09. Wendell:** *"Let's get a spec for the surgical shift. Include the review
protocol in the prompt for what we should be generating. The deft moves and moves that will
help Jordan's reading experiences. We want the most bang for our buck on compute, so we want
to also holistically kick the tires on any major parts of the book that aren't earning their
keep across the chapters. The things that if you were the most hostile editor needing to get
the book to 380 for margin reasons (cost of printing goes way up after 350)."*

**Status: SPEC. Nothing here has been generated or applied.**

## 1 · The target, and the math

Body today: **118,143 words → 398 pages** (≈308 body-words/page).

| target | pages to cut | words to cut | what it takes |
|---|---|---|---|
| **380** | 18 | **≈5,500** | this spec — compression surgery, no restructuring |
| 350 (the printing cliff) | 48 | ≈14,800 | a different book: dropping a whole layer book-wide (e.g. every secondary alchemy, §2 merged into §1 across chapters). Not specced; priced so the choice is visible. |

**This spec aims at 380.** If the hostile editor is ever told 350, that is a restructure and
wants its own proposal.

## 2 · The weight map — measured, not felt

Cross-chapter section weight (words, all Face chapters):

```
Section 4  (The Practice)   26,862   ch3 5,820 · ch7 5,726 · ch4 3,971 · ch8 3,583 · ch5 3,177 · ch6 2,241
Section 6  (The Game)       23,416
Section 5  (Up Close)       18,448
Your Twenty Cards ×6         5,122
3-2-1 blocks ×11             2,426   every chapter after ch3 runs TWO
Take Out of the Forest ×6    1,655   every chapter ALSO runs Section 7 (recap) — a double recap layer
Draw the Axis ×6               733
```

**The single number that justifies the surgery: ch3's Section 4 is 2.6× ch6's, and ch6 is
the chapter the readers called tight.** ch6 proves the template can teach at 2,241 words.

## 3 · The hostile editor's list, ranked by yield

| # | candidate | mechanism | ≈yield |
|---|---|---|---|
| S1 | **§4 parity: ch3, ch7, ch4 toward the ch6 weight** | the deft moves in §5; ch6 is the proof of possibility | 3,000 |
| S2 | **the double recap layer** | *What You Take Out of the Forest* compressed to its superpower handoff; §7 keeps the transition | 800 |
| S3 | **second 3-2-1 blocks, ch4–ch8** | after ch3 and ch4 teach the form twice in full, later second instances become prompt + RECEIPT only | 500 |
| S4 | **Your Twenty Cards ×6** | ch3 teaches the deck; ch4–ch8 re-explain it before their grids. Explanation compresses to one line after ch4 | 600 |
| S5 | **ch8's double-weight opening** | §1+§2 run 2,750 against ~1,300 elsewhere; the Distortion section retells the Exile | 600 |
| S6 | **ch9 §5 (the walk), still 4,247 after Tier 1** | the Cartographer/Founder mode blocks carry offer-adjacent restatement | 500 |
| S7 | **ch2 §6 roster per-daemon repetition** | the mirror structure is protected (the readers' best-of); only within-entry repetition moves | 400 |

Sum ≈ 6,400 before protections bite; **landing estimate ≈ 5,500** — Tier 1 taught us zones
shrink when read precisely, so the ledger will report actual against estimate per chapter.

## 4 · What Jordan gets out of this

Jordan skims theory, never skips a story, stops for a named move with a practice, drops off
at jargon-without-translation and repetition. **Every candidate above is theory-restatement
or machinery re-instruction.** The surgical rule, chapter by chapter: **word count goes down,
scene count does not.** The Examples, the named moves, the fix-questions, the parables, the
marginalia, the humor beats — none is touched. A shorter Section 4 gets Jordan to the daemon
section — the part the readers kept calling the best writing — sooner in every chapter.

## 5 · The deft moves — how compression happens without rewriting the book

1. **Fold the definition into the scene.** Where a mode runs definition-then-scene, the
   scene opens and carries the definition's load. (ch7 Modes 1–2 are the type site.)
2. **Second-instance compression.** The first time machinery appears it teaches in full;
   later instances *run*, not re-teach. (S3, S4.)
3. **Merge absence into distortion.** The template's "what its absence looks like / what its
   distortion looks like" pairs often say one thing twice; where they do, one paragraph.
4. **The test-line discipline.** Template closers ("The test:", "Working vs. performed:")
   compress to their single load-bearing sentence.
5. **Keep the terminus, cut the runway.** In any arc, the last sentence usually carries it;
   compress toward closers.
6. **EA-table sync is law.** Any change inside a mode re-runs the arc-resolution check
   (5 modes · N arcs · 0 unresolved) before it ships. The table lies to nobody — the lesson
   this proof already paid for once.

## 6 · The generation protocol — carried INSIDE every generator prompt

Every agent that generates replacement prose receives, verbatim in its prompt:

> **You are compressing, in Wendell's voice, prose that already passed every reviewer. Your
> output is a set of before/after diffs, nothing else. For every diff:**
> 1. **ELI5 first.** Write the plain version of what the passage says. If you cannot, you do
>    not have the passage; report that instead of generating.
> 2. **The compression must say what the ELI5 says and nothing less.** No new claims, no new
>    examples, no invented specifics, no narrated somatic experience, no reader pathologies.
> 3. **Gate:** no *rooms/quiet/genuinely/thing(s)*, no sentence-initial And/But, no glued or
>    added em-dashes (the budget only ratchets down), no bracketed production tags, no
>    `⟦tokens⟧`.
> 4. **Diet:** run `python3 instruments/review.py DRAFT` on every batch; every counter under
>    1.30 against baseline, and `waste` has a floor as well as a ceiling — prose that never
>    says *it* has stopped pointing at things. Score the batch, not the sentence.
> 5. **Slop reading** against `no-ai-slop`'s `eval.md`: no colon reveals, no binary-contrast
>    rewrites, no fake-profound kickers — and check 1 above all: nothing added.
> 6. **Stance pass, all five:** person (no drifted *we*), doer (no get-passives), borrowed
>    move (nothing performing another chapter's named move unnamed), back-pointer (every
>    That/This opener resolves inside its paragraph), membrane (author's voice never enters
>    the fiction; the Heads' voices never teach).
> 7. **Protected, absolutely:** every Example and named person · every named move · all
>    marginalia/handbook/postcard blocks and their anchors · the cross-chapter formulas
>    (The Tell, How-to-X-So-It-Y, Where-You'll-Spend, exile closers, axis sentences,
>    RECEIPT lines, domain blocks, Ecology sentence) · everything the index locates · the
>    six-Faces-are-altitudes concealment — the ladder is never named in the body.
> 8. **Diff-only output, whole sentences quoted both sides.** A fragment is enough to find
>    an edit and not enough to judge one.

## 7 · Compute plan — most bang, least burn

The scouting is **done and inline** (§2–§3 of this spec — no agent re-derives it). Then:

1. **Six generator agents, one per chapter** (ch2, ch3, ch4, ch7, ch8, ch9 — ch5/ch6 are at
   weight), each with: this spec's target for its chapter, the §6 protocol verbatim, the
   chapter's drag notes from the deep read, and Jordan's per-chapter drop-off risk.
2. **One adversarial verifier per chapter**, prompted to *refute*: find the protected item
   touched, the claim added, the seam broken, the table desynced. A diff any verifier kills
   is dead.
3. **Diffs to Wendell per chapter, batched** — nothing applies without approval, same as
   Tier 1.
4. Per-chapter apply → board → commit, same protocol as Tier 1; **one** page-proof re-run at
   the end, then the sand sitting.

Per-chapter word targets: ch3 −1,400 · ch7 −1,400 · ch4 −700 · ch8 −900 · ch9 −500 ·
ch2 −400 · S2/S3/S4 machinery sweeps −800 (cross-chapter, one agent). **Total −5,600 ≈ 380pp.**

## 8 · Acceptance

Approved diffs land chapter-by-chapter with the Tier 1 mechanism (archive → cut → board →
commit). The pass is done when: body ≤ **112,700 words**, the built workbook ≤ **380 pages**,
arc-resolution 0 unresolved, xref 0/0, index rebuilt clean, and the sand sitting has read
every seam. The log records actual-against-estimate per chapter, including every veto.
