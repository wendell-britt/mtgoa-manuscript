---
type: panel
title: "Six-Face panel — what gets worked on next"
aliases:
  - what next
  - the order after the treatise
tags:
  - mtgoa
  - editorial
  - planning
created: 2026-09-09
source:
  - instruments/claims.yaml
  - instruments/shipcheck.py
  - specs/SPEC_WHOSE_VOICE_CH2_CH3_2026-09-09.md
  - specs/PROOF_MARKS_CH2_CH3_2026-09-09.md
---

# What next

The book is **SHIPPABLE** — seven blocker categories, all clear. So this ranks quality and risk,
not the press. The original proof-mark order is finished: all seven items are applied.

## What is actually outstanding

| | item | who can do it | size |
|---|---|---|---|
| **A** | **Orphaned Head-voice passages.** Today's ruling retired *"above the signature, only the Head."* `ch3:170` is Voss's session log — *"Thirty-first session… three years of nothing, in my own handwriting"* — sitting in unboxed prose with nothing left to license it. A reader now takes it for the author's own log. `ch5` and `ch7` show the same shape and need a read to size. | me, then Wendell rules | 1 chapter confirmed, 2 likely |
| **B** | **DL-89, the compile footgun.** `insertions.py` and the manuscript disagree by fourteen lines in ch3. One `compile.py --apply` silently reverts proof-mark reworks Wendell approved. `--verify` passes over it because it compares the body and the divergence is inside the boxes. | me | small |
| **C** | **Proof ch4–ch9.** The photo set runs ch2 p.25 → ch3 p.95. **Everything this session learned came from 30% of the book.** The seven patterns, the cadence molds, the promise defect — all derived from two chapters. Six chapters have never been read this way. | Wendell only | large |
| **D** | **DL-87**, the handwritten *"Rework"* on *What You Take Out of the Forest* — a scope instruction applied sentence by sentence and never carried out. | Wendell rules, then me | medium |
| **E** | **DL-86**, one sentence rebuilt: 41 words of subject before the verb, pronoun reaching past a sentence boundary. | me | one sentence |
| **F** | **DL-88**, the `[?]` mark. Needs a sentence from Wendell, not work. | Wendell only | trivial |
| **G** | **The Polarity Map marker.** Open question 4 of the whose-voice spec, same region as A. | folds into A | — |
| **H** | **Registry coverage**, 81 of 89 rulings unguarded. | me, on contact | background |

---

## SHAMAN · the Body — *the one a reader trips on*

Read `ch3` from the top as it stands now. The admissions box closes, signed. The chapter runs in
Wendell's voice. Then, with no warning and no frame, somebody starts counting sessions and says
*three years of nothing, in my own handwriting.*

A reader takes that as Wendell's. It is Voss's — its last sentence is the admissions page's *"A
word from the Head"*, near verbatim. **This is the only item on the board that changes what a
reader believes about a real person**, and it is in the first Face chapter, the one everybody
reaches.

It also has the quality this session has taught us to fear: **it was made by a correct decision.**
Nothing is broken in the paragraph. The rule that licensed it was retired this morning, and the
license went with it, and no instrument can see that.

**Ranks:** A first, and not close.

## CHALLENGER · the Line — *do not start new work carrying a debt you made today*

The unwelcome sentence: **A is ours.** It did not arrive from the proof or from a reader. It was
created six hours ago by a change this panel's predecessor recommended and Wendell ruled. Leaving
it to start C would mean the session's own damage is the oldest outstanding item in the book.

On B, the Challenger's line is sharper than its size suggests. **A check that passes over a
fourteen-line divergence is worse than no check**, because `--verify` is the sentence people quote
when they say the marginalia are safe. It has been quoted that way in three commit messages today,
mine included.

**Ranks:** A, then B. C does not start until both are closed.

## REGENT · the Inheritance — *thirty percent*

Everything this session produced — the seven patterns, `cadence.py`, `headings.py`, the claims
registry, the promise rewrite — descends from Wendell reading two chapters on paper and marking
351 lines. **Six chapters have never had that.**

That is the largest unexamined surface in the book and no instrument substitutes for it, because
the whole lesson of today is that the instruments do not read arguments and do not hear voice. The
proof is the generator. Everything else on this board is a consequence of the last one.

But the Regent votes against going there first, for a reason the Challenger did not raise:
**A and G both live in Sections 1–3 of every Face chapter**, which is precisely what a ch4–ch9
proof would put in front of Wendell. Proof before they are settled and he marks the same structure
twice, once in the state we are about to change.

**Ranks:** A and G together, then C. B whenever, it costs an hour.

## ARCHITECT · the Design — *the split nobody has said out loud*

The board has been argued as one queue and it is two. **A, B, D, E and H are mine. C and F are
Wendell's, and F is one sentence.** Those run in parallel and the panel should say so rather than
producing a single ordering that idles one of us.

The parallel plan:

| Wendell | me |
|---|---|
| rule F, one sentence, unblocks a held mark | A: read ch3, ch5, ch7 §1–3 and census the Head-voice passages |
| begin proofing ch4–ch9 once A's structure is ruled | B: disarm the compile footgun |
| rule A and D when the census lands | E: the one-sentence rebuild |

On sequencing A against C: the Architect agrees with the Regent, and adds the mechanical reason.
**The census for A is the same read a proof of §1–3 would drive.** Doing it first means the proof
arrives at a settled structure and marks prose defects instead of architecture.

**Ranks:** A first, B in parallel, C once A is ruled. Never one queue.

## DIPLOMAT · the Table — *what today has cost the person doing it*

Wendell has spent this session in editorial machinery: registries, censuses, panels, specs. The
manuscript changed, but most of what he read was apparatus. **C is the item that puts him back in
his own book**, and that matters beyond scheduling.

So the Diplomat's caution about ranking A first: it is correct and it must be fast. If the census
for A takes a day, the ranking is wrong regardless of the argument. **Timebox it to one read of
three chapters and a list.** If it comes back larger than that, it becomes its own spec and does
not hold up the proof.

On D, the *"Rework"* section: it has been outstanding since the marks arrived and it is the only
instruction from Wendell's own hand that has not been carried out. That is worth something. It
should not slip again.

**Ranks:** A, timeboxed. Then C. D before E, because D is his handwriting.

## SAGE · the Board — *name what has been driving this*

Every item on this board except C is downstream of C. The session has been reactive in the
healthiest sense: Wendell read, Wendell marked, and the work followed. **The generator of value
here is the proof, and we have run it on 30% of the book.**

So the question to ask of today's work is not how much of it there was. It is whether each piece
was **authored** — metabolized out of a blocker Wendell named — or **accumulated**, meaning
plausible, adjacent and coherent without being the thing. Run it item by item and today holds up.
The claims registry came from *"no confidence that the editorial system I built was used."* The
boundary line came from *"I don't know what all pass means."* The whose-voice spec came from
*"you're about to mess up my manuscript."* Every one of them is a charge of his, spent.

**The failure mode is drift, not volume.** A count of instruments cannot tell the two apart, and
reaching for one is how a judgment gets dressed as a measurement.

The Sage's addition: **A and G should be ruled in one sitting, not two.** They are the same
question — what marks a voice that is not the author's inside Sections 1–3 — and answering them
separately is how a book grows two conventions for one problem.

**Ranks:** A and G as one item, then C. Judge what follows by whether it answers something Wendell
named, not by what kind of artefact it is.

---

## Consensus, six of six

**1 · A, with G folded into it, and timeboxed.** Read Sections 1–3 of ch3, ch5 and ch7, census
every passage that is not the author's voice, and put the list in front of Wendell with the
Polarity Map question attached. **One read, one list, one ruling.** It is first because today's
ruling created it, because it is in the first Face chapter, because no instrument can see it, and
because it is the same read a ch4–ch9 proof would otherwise duplicate.

**2 · B in parallel, and it is an hour.** Disarm the divergence between `insertions.py` and the
manuscript so that `compile.py --apply` cannot revert approved work, and make `--verify` compare
frame content so the check stops passing over it.

**3 · C is the big one and it is Wendell's.** Proof ch4–ch9. It waits only on A being ruled, so
that he marks prose rather than a structure about to change. Everything else on this board is a
consequence of the last proof.

**4 · F is one sentence from Wendell** and can be answered any time; **D before E**, because D is
his own handwriting and has been outstanding longest.

**5 · H is background.** It accrues on contact and is never a priority on its own.

## What the panel refuses

It does not produce a single queue, because two people are working and one ordering idles one of
them. It does not start C before A is ruled, which would put the same structure in front of
Wendell twice. And it does not rank work by artefact type.

## Correction, 2026-09-09, after Wendell read this

**The first version of this panel ended by counting today's output** — four instruments, a
registry, three specs, four panels — and ruling that *"none of it is the book"* and the ratio
should not repeat. Wendell: *"I disagree with them. This is productivity for productivity's sake…
This is an assumption of productivity that I haven't made or asked for in this session."*

He is right and the error has a name in his own draft spec for the Governor. **A volume ceiling is
not alignment**: *"Restricting throughput does not produce alignment; it produces slower drift."*
And the panel self-certified, which that spec's agent contract forbids outright — *"an agent that
self-certifies alignment is the failure mode this system exists to correct."*

The Governor spec also predicts the shape exactly. Its ontology audit records that a spec about
drift drifted into a second kingdom, and calls that *"the failure mode, reproduced at
spec-authoring altitude… plausible, adjacent, internally coherent, and not the thing that already
existed."* **This panel did the same at panel-authoring altitude**, and the giveaway is the same
one: nobody asked the question it answered.

What the Sage's section says now is what it should have said first. The test is authored against
accumulated, and it is applied per item rather than to a count.
