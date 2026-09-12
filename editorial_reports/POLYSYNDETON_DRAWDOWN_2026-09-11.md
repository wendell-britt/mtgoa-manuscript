# Polysyndeton drawn to zero

**2026-09-11**, first chunk of the zero-target drawdown, measured with editorial-core v32 on a
clean copy of `origin/master`. Branch `editorial/drawdown-2026-09-11`.

**polysyndeton 7 → 0 unresolved** (6 rewritten, 1 ledgered). No other scanner rose at any
location — trailing_and, telling, light_verb, slop_shapes and fragment are unchanged per
`file:line`, ledger set aside for the comparison.

## The seven, each named

| site | call | what changed |
|---|---|---|
| copyright.md:48 | rewrite | `…8 and 9 and in Appendix A` → `…8, 9 and in Appendix A` — a serial list; the comma is the honest join for like items |
| ch4.md:648 | rewrite | `hard to hear and easy to answer, because` → `hard to hear, easy to answer, because` — two distinct facts (hard to *receive*, easy to *counter*); asyndeton keeps both, drops the loose *and* |
| ch4.md:690 | rewrite | `One sentence of line and one of offer` → `One sentence of line, one of offer` — a parallel pair; asyndeton |
| ch5.md:156 | rewrite | `beautiful and empty and slowly falling apart` → `beautiful but empty, and slowly falling apart` — the relation is concession then consequence, now named |
| ch7.md:766 | rewrite | `Put the other side first and put it well:` → `Put the other side first, put it well:`, and the refusal `I can state both and I do not weigh them the same` → `…both but I do not weigh them the same` — the refusal's real relation is concession |
| ch8.md:824 | rewrite | `what everyone can feel and nobody says` → `what everyone can feel but nobody says` — concession (felt yet unsaid) |
| ch7.md:654 | **ledger (my call)** | `The move either works and the conversation opens, or the other person corrects you and you update` — a symmetric either/or: each branch pairs a move with its immediate result; the two *and*s are the branches' parallelism, not a loose chain. Wendell to ratify. |

Ledger now: polysyndeton 9 accepted (8 prior + this 1), 0 stale.

## Claims carrier re-pointed

The ch4:648 rewrite moved DL-98's ch4 carrier phrase `is hard to hear and easy to answer` →
`is hard to hear, easy to answer`. DL-98's fact (the verb *land* replaced by what occurs) is
intact — the sentence still says what happens and carries no *land*. `claims.yaml`'s watched
phrase was updated to the new wording; `claims` PASSES.

## A core finding, deferred: the sentence splitter under-segments at emphasis

`ch7:766` at first would not clear because `density.sentences` does **not** break a sentence that
ends inside emphasis — `…is closing.* Then refuse: *…` reads as one sentence, bundling two
separate quoted sentences (each with a single, legitimate *and*) into an apparent chain. The
`SENT` regex splits on end-punctuation directly followed by whitespace and ignores a closing
`*`/`_`/quote/paren in between (the closer set `resolve3.py` already handles).

I cleared ch7:766 on its own merits (the refusal *and* → *but* is a real concession, not a dodge)
and **left the splitter alone**, because fixing it is a **validity change (v33), not a side
effect**. Measured in isolation on the untouched book, the fix:
- moves **no** telling / trailing_and / light_verb / slop count;
- surfaces **19 hidden fragments** (fragment 54 → 72) — sentences the bug had glued to a
  neighbour. Read: 11 are boxed HANDBOOK labels (Clause N, *A word from the Head* — these become
  boxed notes under the existing ruling) and 8 are run-in bold labels (*Stage 5: Exit.*, *The
  Trauma Olympics.*, *Protector × Gather Resources.*) that the fragment instrument would need
  taught about, the way `is_label` handles wholly-emphasised runs.

So the splitter fix is correct and worth doing, but it grows the fragment debt and wants its own
pass. Flagged here rather than folded in.

## Remaining debt (target 0)

telling 198, light_verb 52, slop_shapes 40, fragment 38 — **328**, down from 335.
