# NOTE — The bracketed move tags are a deprecated mechanic still in the book

**2026-07-29. Opened because Wendell read `**[TRANSLATE] Translate 1 — Anxiety →
Interest**` in a commit message and asked whether Jordan would know what to do
with it.**

Short answer: **no, and the mechanic was already deprecated fourteen months of
work ago.** It was signed off as shipped. It never reached the canonical text.

---

## 1 · What is still in the manuscript

**28 bracketed labels, in two chapters, and nowhere else in the book.**

| tag | ch7 (Diplomat) | ch8 (Sage) |
|---|---|---|
| `[DISSATISFACTION → SATISFACTION]` | 10 | 5 |
| `[TRANSLATE]` | 6 | 0 |
| `[CONTROL]` | 7 | 0 |
| | **23** | **5** |

ch1–ch6 and ch9 carry none. A reader arrives at Chapter 7 having seen six
chapters of ordinary bold headers and meets a production tag.

## 2 · It was deprecated on 2026-06-03 and marked complete

`SPEC_WB8_ARTIFACT_SWEEP_2026-06-03.md` §B1 and §B2 ordered exactly this fix, on
exactly these instances, with the reasoning already correct:

> *"The bracket reads as a **production tag**, not a chapter voice. A reader who
> has read 10 of them by Chapter 6 is being told '**you are in a Transcend
> move**' each time, which the move itself already conveys… Removing the bracket
> returns the move to prose, where it belongs."*

Its acceptance gate is signed off:

> - [x] All 10 Ch6 brackets … are stripped
> - [x] All 5 Ch7 brackets … are stripped
> - [x] `grep -nE "\[DISSATISFACTION" chapters/ch*/CHAPTER*.md …` returns zero matches

**Every one of those checkmarks is true, and the book still has the brackets.**
Here is how both can hold at once.

The old numbering had `ch6-diplomat` and `ch7-sage`, which are the current ch7
and ch8. The fix was applied to `chapters/ch6-diplomat/CHAPTER6_DIPLOMAT_FULL_DRAFT_MASTER.md`,
and the acceptance grep was scoped to `chapters/`. Verified today at `4172d7a`,
the commit that retired that tree:

| | `[DISSATISFACTION` count |
|---|---|
| `chapters/ch6-diplomat/…MASTER.md` at `4172d7a` | **0** — the fix is there |
| `manuscript/ch7.md` today | **10** |
| `manuscript/ch8.md` today | **5** |

The fix landed in one tree and never propagated to the other. Then `chapters/`
was retired as superseded and `manuscript/` became canonical, so **the repository
threw away the corrected copy and kept the uncorrected one.** The grep that was
supposed to catch this could not, because it only looked where the fix was.

**The lesson is about the check, not the fix.** An acceptance grep scoped to one
of two parallel trees proves nothing about the book. Any future gate greps
`manuscript/`, which is why `instruments/gate.py` reads that directory and only
that directory.

## 3 · Why it keeps coming back

`AGENTS.md`, under **EA Standards**, still says:

> Every move in the book:
> `**[DISSATISFACTION → SATISFACTION] Transcend [X] — Emotion Name → Alchemical Outcome**`

The deprecation never reached the instructions. Anything generating a move from
`AGENTS.md` will produce the tag, correctly, because that document still calls it
canon. **Fixing the 28 labels without fixing `AGENTS.md` guarantees they come
back.**

## 4 · Two half-finished migrations inside the mechanic

Evidence that this was already being abandoned and stalled mid-way.

**The verb changed and the tag did not.** WB-8 documents the label as
`Transcend N`. The manuscript now reads `Alchemy 1` and `Alchemy 2`, ten times,
and the word *Transcend* appears **zero** times in the body. So the migration
from *Transcend* to *Alchemy* completed and the bracket it sat inside survived
it. The tag now names a move type the book no longer uses that word for.

**The first channel is formatted differently from the other four.** Inside ch7:

| form | count | where |
|---|---|---|
| `**[TRANSLATE] Translate 1 — Anxiety → Interest**` | 2 | Bridge-Builder only |
| `**[TRANSLATE] — From Understanding to Transmission**` | 4 | the other four channels |
| `**[CONTROL] Control 1 — Untracked Depletion Pattern**` | 2 | Bridge-Builder only |
| `**[CONTROL] — Neutral Channel: Presence Collapse Pattern**` | 5 | the other four channels |

Somebody converted the first channel and stopped. Whichever form was the target,
the book currently ships both.

## 5 · The ICA answer — no, and here is the specific reason

Jordan's profile in `EDITING_PLAN.md` names her top drop-off trigger:

> **What triggers drop-off:** Jargon without translation, claims without
> practice, moralizing without self-deprecation

`SPEC_STRUCTURAL_DELIVERY.md` restates it: *"she drops the book at jargon without
translation."* That spec already logged the same failure in Chapter 8 — five
terms defined by each other with no gloss on any.

**Measured against the book itself, every term in the tag is untranslated:**

| term in the tag | times defined for the reader anywhere in the manuscript |
|---|---|
| `TRANSLATE` as a named move type | **0** |
| `CONTROL` as a named move type | **0** |
| `DISSATISFACTION → SATISFACTION` as a labelled pair | **0** |
| `Transcend` | **0** — the word is not in the book |
| `Neutral Channel` | **0 definitions, 11 uses**, all in ch7 |

*Neutral Channel* is the sharpest one. Eleven appearances, one chapter, never
introduced. `LEARNING_METABOLISM_CH6_2026-04-20.md` §14 records that the term
confused the **writing process** — *"Confusion between structural patterns and
emotional categories leads to mislabeling moves"* — and the fix was to clarify it
for the author. Nobody then asked whether the reader had ever been told.

So the honest answer to Wendell's question: **Jordan cannot make sense of it,
because there is nothing in the book to make sense of it with.** The bracket is
not hard, it is empty. It reads as a system she has not been shown, which is the
worst version of jargon — it implies she missed something.

And she did not miss anything. The prose underneath already does the work, which
is exactly what WB-8 said in June: *"the first sentence of each block"* teaches
the concept, and *"the bracket is just the label."*

## 6 · What to do

**D1 — strip all 28 brackets.** WB-8's decision stands and needs no relitigating.
`**[DISSATISFACTION → SATISFACTION] Alchemy 1 — Anxiety → Curiosity**` becomes
`**Alchemy 1 — Anxiety → Curiosity**`. Mechanical, and it takes one script.

**D2 — settle the ch7 format split in the same pass**, or the strip leaves
`**Translate 1 — Anxiety → Interest**` next to `**From Presence to Structure**`
and the inconsistency simply loses its wrapper. Recommend the Bridge-Builder
form (`Translate 1`, `Control 1`) for all five channels: it is numbered like
`Alchemy 1` and `Alchemy 2` beside it, so the four move types read as one
system.

**D3 — fix `AGENTS.md` EA Standards** to the stripped form, with a line saying
the bracket is deprecated and why. Without this, D1 is temporary.

**D4 — RULED 2026-07-29: keep *Neutral Channel*.** Wendell: *"We should keep the
neutral channel because it's one of the emotional alchemy channels."* The
cut-the-term option in the first draft of this note is withdrawn. It was wrong,
and it was wrong in the way this whole note is about: it read a term as
decoration because the term was undefined in the book, when the term names a real
part of the system.

**But the ruling collides with how ch7 actually uses the words, and the collision
has to be settled before anything is edited.** Two different referents currently
share one name.

**Referent A — Earth/Neutrality, an emotional channel.** Taught in ch3 and real:

> ch3:868 · The five channels — Metal/Fear, Water/Sadness, Wood/Joy, Fire/Anger,
> **Earth/Neutrality** — tell you which teaching a given charge carries
>
> ch3:394 · | **Earth** | Neutrality | Whole-system perspective; detachment | …
>
> ch3:428 · **Neutrality completes into peace.** Numbed, neutrality is checking
> out; opened to the whole, it completes into peace

**Referent B — what ch7 labels *Neutral Channel*, 11 times.** Every instance
labels a **Control** move, and the content of all six is behavioral:
*performative presence*, *intellectual superiority*, *presence collapse*,
*premature closure*, *endless process*, *false closure*. None is
neutrality-as-perspective. And `LEARNING_METABOLISM_CH6_2026-04-20.md` §14 rules
the opposite of the ruling above, in as many words:

> **Rule:** The Neutral Channel refers to behavioral/structural patterns (e.g.
> untracked depletion, vague threat-pattern, collapse) **NOT an emotion type.**
> **Why it matters:** Confusion between structural patterns and emotional
> categories leads to mislabeling moves and incorrect frames.

So the April ruling says *not an emotion type* and the July ruling says *one of
the emotional alchemy channels*. **Both cannot describe the same eleven lines.**
That §14 note also records that this exact ambiguity already caused mislabelled
moves once, during drafting — which is the argument for settling it rather than
patching around it.

**The open question, and it is Wendell's:** does the name *Neutral Channel* belong
to Earth/Neutrality, or to the structural Control move type?

- **If Earth/Neutrality** (which is what the July ruling says on its face), then
  ch7's 11 uses are the misnomer. They need a different label for the Control
  move type — the prose beside them already supplies one, *"the Bridge-Builder's
  Control challenge runs on depletion"* — and Earth/Neutrality needs a definition
  on first use in ch7, which it does not currently have.
- **If the Control move type**, then ch7 is correct as written, §14 stands, and
  what is missing is only the definition: one sentence on first use in ch7 saying
  what a Neutral Channel move is and why *neutral* means channel-neutral rather
  than the Earth channel. That is the smaller fix, and it needs the disambiguating
  sentence precisely **because** ch3 has already taught Neutrality as a channel
  eighty pages earlier.

Either way the term stays, per the ruling. What the answer changes is whether
this is a one-sentence gloss in ch7 or a relabelling of eleven headers.

**D5 — the deprecated-mechanic sweep this implies.** WB-8 was one artifact sweep
that was verified in the wrong tree. Nothing has re-run it against `manuscript/`.
Anything WB-8 and its siblings claim to have fixed should be re-checked where the
book actually lives, because this one was signed off and false for two months.

**Sequencing:** D1–D4 are small and independent of the em-dash pass. D5 is a real
audit and needs its own scope. None of it is a print blocker except D1, which is,
because a production tag in shipped prose is a typesetting artifact with a reader
in front of it.

## 7 · How this gets checked

```
grep -c "\[DISSATISFACTION\|\[TRANSLATE\]\|\[CONTROL\]" manuscript/ch*.md   # must be 0
grep -c "Neutral Channel" manuscript/ch*.md                                # 0, or defined
grep -n "DISSATISFACTION" AGENTS.md                                        # must be 0
```

Against `manuscript/`. Never against a parallel tree.
