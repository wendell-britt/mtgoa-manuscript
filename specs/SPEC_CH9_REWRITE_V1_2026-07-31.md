# SPEC — Chapter 9 rewrite for v1

**Branch:** `claude/ch9-rewrite-v1`. Diagnosis and scope. Nothing rewritten yet.

**Wendell, 2026-07-31:** *"Chapter 9 needs to get rewritten if I'm taking
bars-engine out of the v1 of the book. We need to save what we've got for now
because it might make its way back in, but now we have to actually teach people
to create their own allyship game using their moves they've been practicing and
the character sheet they've ostensibly been filling out."*

**Preserved first.** The current chapter is at
`drafts/archive/ch9_bars-engine_version_2026-07-31.md` — 12,608 words, byte-for-byte,
before anything is touched.

---

## 1 · The good news: the skeleton already does this

ch9 is **not** a bars-engine chapter with a lesson attached. Its architecture is
already *design your own game*:

| Section | Words | State |
|---|---|---|
| Front matter — *The Return* | 73 | clean |
| 1 · The Exile | 270 | clean |
| 2 · The Distortion | 432 | clean |
| 3 · The Concept — *From Map to Design* | 463 | clean |
| 4 · The Practice — **How to Design Your Own Allyship Game** | 2,220 | **1** bars-engine ref |
| 5 · Journey to the Center — *Building the Thing That Didn't Exist* | **5,144** | **7** refs — the memoir |
| 6 · The Game — the five Player moves | 2,187 | 2 refs |
| 7 · Recap and Transition | 192 | clean |
| The Last Rep — the six-moment drill | 1,302 | **clean** |
| The Village Is Already Playing | 317 | 1 ref — a product list |
| The Last Line | 98 | clean |

**Roughly 9,500 of 12,608 words are structurally clean.** Section 4 already names
the five modes of self-authorship and the stage sequence *Review → Discern →
Design → Build → Pass On*. Section 6 already carries five Player moves — *Cut the
Field to One Problem · Put It in Front of One Person Before It's Defensible ·
Take the Note That Costs You the Design · Run It Again With One Thing Changed ·
Hand Someone the Pen*. The Last Rep already runs the transfer drill.

**The rewrite is Section 5**, and one clause each in three other places.

## 2 · What Section 5 is, and what it has to become

5,144 words — 41% of the chapter — of Wendell building bars-engine, used as the
worked example of designing a game.

**The memoir is not the problem. Its exclusivity is.** The chapter currently
demonstrates *design your own game* by narrating one person designing one
specific thing the reader cannot use, and then telling her to go do her own.

Per §8 of `SPEC_HUMOR_PASS_2026-07-31.md`, the eleven references do two jobs, and
only one is app routing:

- **ROUTING** — `ch9:400` *"Bars-engine is the village's common ground"*,
  `ch9:696` the product list. **Out for v1.**
- **TESTIMONY** — `ch9:358` *"When I started building bars-engine, I didn't have
  it figured out"*, `ch9:608` *"Bars-engine has cost me all five of these."*
  **Keep.** Strip this and the chapter is a person recommending a journey he did
  not take.

**The replacement is not more memoir. It is her build**, with his as the worked
example beside it — which is what every other chapter in the book already does.

## 3 · The dependency that outranks everything else

**Wendell's brief says the reader builds from "the character sheet they've
ostensibly been filling out." She has not been filling it out.**

Finding A2, measured: `ch1:207` promises *"a line added in every chapter ahead."*
Delivered: **ch2 and ch9 only. Six consecutive chapters add nothing.**

So a rewritten ch9 that opens *"look at your character sheet"* is addressing a
reader holding four entries from ch1 and one from ch2.

**A2 is now a hard dependency of this rewrite, not an optional improvement.** The
new chapter's central input does not exist until those six lines are seated.

**They are already drafted, gated and approved** — six sheet lines for ch3–ch8 in
`drafts/APPROVED_unearned_recall_2026-07-31.md` on
`claude/edit-assumed-prior-knowledge`. Each names that chapter's own artifact:
the channel she skips, the line she has not drawn, the inheritance she carries,
the harm she keeps fixing, her walk-away price, where she goes when a situation
is larger than she can hold.

**Read as a set, those six lines are the character sheet the new ch9 needs.** They
were drafted to close a promise; they turn out to be the input for the payoff.

**Sequence: A2 lands first, then ch9 is rewritten against a sheet that is full.**
Reversing that order produces a chapter whose first instruction fails.

## 4 · The second input: her moves

The brief also says *"the moves they've been practicing."* Measured, those exist
and are plentiful — **five per chapter across ch3–ch8, thirty in total**, plus
the WAVE's five stages, plus ch9's own five Player moves.

**The risk is arithmetic, not availability.** ch9 already carries three competing
sets of five (CH9 report, finding S2), and the rewrite adds a fourth reference
class. The chapter that teaches her to build must be the clearest in the book
about which five it means at any moment, and it is currently the least clear.

## 5 · What the rewrite has to deliver

1. **An instrument she fills in**, drawing on the sheet and her thirty moves —
   the thing Section 5 currently substitutes memoir for.
2. **A worked example that is his, kept short**, standing beside her build rather
   than in place of it. The testimony survives; the 5,144 words do not.
3. **A game she can actually run this week**, which is what the five Player moves
   in Section 6 already describe and Section 5 never lets her reach.
4. **No product.** Routing out, testimony in, `masteringallyship.com` as the one
   door — per `SPEC_REMOVE_APP_V1_2026-07-31.md`.

## 6 · What is reusable, verbatim

- **The Last Rep** (1,302 words) — the six-moment transfer drill. The only place
  in the book she is given situations and asked to choose a Face and a move. It
  needs the three fixes in the CH9 report (an outcome for the middle result, the
  move half scored, a move roster) and needs no bars-engine.
- **Section 6's five Player moves** (2,187 words) — already the right teaching,
  two clauses to clean.
- **Sections 1, 2, 3, 7 and The Last Line** — clean, ~1,100 words.
- **Section 4's five modes and stage sequence** — the frame the new Section 5
  should execute against, one ref to cut at `ch9:153`.

## 7 · Rulings needed

1. **How long is the new Section 5?** It is 5,144 words. A build instrument plus a
   short worked example is plausibly 1,500–2,500, which would take ch9 from
   12,608 to roughly 9,000–10,000 and make it the shortest teaching chapter
   rather than the second longest.
2. **Does the archived version stay in the repo?** It is preserved at
   `drafts/archive/`. A second edition that restores bars-engine wants it intact.
3. **Does A2 land first?** Recommended, and near-blocking. The alternative is
   writing ch9 to a sheet the reader does not have.
4. **What is the reader's build, concretely?** A one-page game design? A single
   quest she runs on the cause she chose in ch1? The answer sets the instrument,
   and it is the one piece of this that cannot be derived from what already
   exists.
