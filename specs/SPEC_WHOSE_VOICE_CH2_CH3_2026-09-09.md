---
type: spec
title: "The promise ch2 makes and ch3 does not keep — whose voice runs Sections 1 to 3"
aliases:
  - whose voice
  - the treatise promise
  - two hands corrected
  - signature attaches to what
tags:
  - editorial
  - mtgoa
  - architecture
  - voice
created: 2026-09-09
review: 2026-09-16
source:
  - manuscript/ch2.md
  - manuscript/ch3.md
  - specs/SPEC_TWO_HANDS_2026-07-30.md
  - specs/SPEC_CH2_FRAME_2026-08-01.md
  - instruments/ch3_memoir_move.py
status: measured and specified; the ruling is Wendell's, nothing applied
---

# The promise, and what arrives

**Wendell, 2026-09-09**, stopping an applied change: *"I think we aren't understanding what the
treatise is and you're about to mess up my manuscript. As of right now the boxes front matter and
the marginalia are doing most of the worldbuilding work. The signatures at the end are coming off
weird because the text after the admissions form is really just all in my voice."*

He scoped this to ch2 and ch3, and the scope turns out to be exact. **ch2 is where the book
promises the reader a treatise. ch3 is the first chapter that does not deliver one.**

---

## 1 · The promise, verbatim

`ch2:577`, in the author's own voice, to the reader:

> Turn the page and a letter is waiting, from the Headmaster. After it, six chapters, **each
> opening with a treatise by the person who runs one of the six schools: their method, in their
> voice, carrying their bias and their quarrel with the other five. It runs as ordinary text
> until you reach a signature at the close of its third section.** That is where a submitted
> document signs itself. […] The boxed inserts belong to the school as well: an admissions page
> saying who they take and what it costs, students and citizens on the record about what the
> teaching did to them. The margin is a hand that never signs.

**This is a complete and deliberate design, and it is not the error.** It commits to five things:

1. Each Face chapter **opens with a treatise** by that school's Head.
2. It is **their method, in their voice**.
3. It carries **their bias and their quarrel with the other five**.
4. It runs as **ordinary text**, not boxed.
5. A **signature at the close of Section 3** is a submitted document signing itself.

The claim has three carriers in the book. This promise; the six signatures; and the margin, which
refers to *"this treatise"* at `ch6:77`, `ch6:557` and `ch7:159` — so **the fiction asserts it
too.**

## 2 · What arrives

Measured 2026-09-09, every framed block stripped, Sections 1–3 only:

| ch | words | *you* | *I* |
|---|---|---|---|
| **3** | 2,810 | **81** | 12 |
| 4 | 2,275 | 20 | 14 |
| 5 | 3,105 | 54 | 5 |
| 6 | 2,784 | 40 | 12 |
| 7 | 2,790 | 14 | 16 |
| 8 | 4,141 | 116 | 19 |

**ch3 is the extreme case** — 81 second-person addresses in 2,810 words, the same rate as the
back half, which is why it is the chapter where the mismatch is loudest.

Against the promise, item by item:

| promised | delivered |
|---|---|
| **opens with a treatise** | opens with **the fable**. ch3: *"There was a time when the Shaman lived in the village."* ch7: *"You recognize a woman in the village."* The book's narrator, in the same voice, in all six. |
| **in their voice** | mostly the book's teaching voice. The Head does appear, in patches — ch3:169–173 is Voss's session log, *"Thirty-first session… three years of nothing, in my own handwriting"* — and it closes on a sentence that also sits inside the handbook. |
| **their bias, their quarrel** | not located. The Faces are named throughout, but as the fable's cast rather than as a Head arguing with five rivals. |
| **ordinary text** | true. This is the one term kept. |
| **signature at the close of §3** | true, and it is the problem. The last thing above every signature is the **Polarity Map** — the book's own recurring apparatus, in the book's framework vocabulary. ch4 ends *"Here is what is specific to this reader."* ch7: *"One part of this belongs specifically to this reader."* ch5 opens it with *"You met the Polarity Map at the School of the Body."* **No Head filing a document about her own school writes a sentence tracking the reader's progress through this book.** |

**So the signature is not the defect. It is where the defect becomes visible**, because it is the
moment the book asserts a name for prose the reader has just spent 2,800 words with.

## 3 · What the earlier specs got right and wrong

`SPEC_TWO_HANDS_2026-07-30` states the architecture as *"Head in the front half, Wendell in the
back half"* and moves the signature to the close of Section 3 on that basis.
`ch3_memoir_move.py` hardens it: ***"Above the signature, only the Head. Below it, only
Wendell."***

**Right, and not reopened here:** the membrane argument. The author may not step into the fiction,
the fiction may not narrate the teaching, and the marker must be apparatus rather than anybody's
voice. Wendell's 2026-07-30 rejection of a hand-off line in his own voice stands.

**Wrong:** the premise that Sections 1–3 are the Head's. They are mostly the book's. Both specs,
and the promise at `ch2:577`, describe a document the manuscript does not contain.

**ch2 itself needs no correction.** `SPEC_CH2_FRAME_2026-08-01` ruled that ch2 leaves the fiction,
and the frame inventory confirms it: ch1 and ch2 carry no epigraph, no handbook, no marginalia and
no signature. ch2's only stake in this is the sentence at 577.

## 4 · The two real options

| | option | what it costs | what it settles |
|---|---|---|---|
| **A · Keep the promise.** Write Sections 1–3 as the treatise ch2 describes: the Head's method, in the Head's voice, with the quarrel. | Six chapters of new writing at ~2,800 words each. The fable and the Polarity Map have to move or be re-voiced. | The book delivers what it told the reader it would, and the signature signs a real document. |
| **B · Change the promise.** Rewrite `ch2:577` to describe what the chapters actually do, move or retire the six signatures, and adjust the three marginal references to *"this treatise"*. | ~4 edits plus six signature decisions. The submitted-document convention goes or narrows. | The book stops asserting something the prose does not do. Cheap, and it loses a device. |

**A is the expensive one and it is not obviously wrong.** The design in `ch2:577` is good — a Head
with a bias and a quarrel is a better read than a neutral fable, and the handbooks prove the voices
exist and work. **B is honest and fast and gives up something the book wanted.**

There is no third option that keeps the promise and changes nothing, which is what the reverted
header tried to be.

## 5 · Requirements

Ruling-independent. These hold under A or B.

- **FR-1** No apparatus may attribute prose outside its own box **unless the prose delivers what
  the attribution claims.** Four of the five box kinds are self-contained today; the signature is
  the one that reaches out.
- **FR-2** The three carriers of the treatise claim — `ch2:577`, the six signatures, and the three
  marginal references — MUST agree with each other and with the prose. **Today all three agree
  with each other and none agrees with the prose**, which is why this reads as a voice problem
  rather than an error.
- **FR-3** Voss's session log at `ch3:169–173` is the Head's voice in ordinary text. Any ruling
  MUST say what happens to it. Under A it is a model for the rest; under B it is the one passage
  that still needs a home.
- **FR-4** `ch3_memoir_move.py`'s rule — *"above the signature, only the Head"* — MUST be restated
  or retired. Nothing enforces it and it describes a boundary the text does not have.
- **FR-5** ch2 changes in exactly one place under B, `ch2:577`, and in no place under A.
- **FR-6** No front-matter note may be written that restates the current promise. `SPEC_TWO_HANDS`
  designed one and left it unsigned-off since July. **The book already makes this promise at
  `ch2:577`; a second statement of it would double a claim that is the thing in question.**

## 6 · Acceptance

| # | test | expected |
|---|---|---|
| **A1** | strip boxes from ch3, list first-person-singular sentences | under A, the Head throughout; under B, only the session log, and it is ruled |
| **A2** | same on ch2 | every hit the author; ch2 has no Head voice and gains none |
| **A3** | `grep -rn treatise` across the corpus | every use names a document that exists |
| **A4** | read the paragraph above each of the six signatures | under A it is the Head closing a document; today it is the Polarity Map in all six |
| **A5** | ch2:577 read against ch3 §1–3 | the promise and the delivery match |

## 7 · The worked example, run

Per the standing rule: a spec proposing a mechanism is not specified until its worked example has
been run against it, in writing. Running these is what produced §1 and §2, and **two of the runs
refuted earlier drafts of this spec.**

- **A1 and A2 were run.** ch2 returned 52 first-person sentences, every one the author. ch3
  returned 68, of which the session log is the Head, sitting in ordinary text above the signature.
  **The first draft of §2 had not noticed that passage**, and FR-3 exists because of it.
- **A3 was run and refuted this spec's own FR-2.** The draft asserted that *treatise* appears only
  in the six signatures. It appears four more times: once at `ch2:577`, where the promise is made,
  and three times in the margin. **That finding moved the whole spec: the defect is not a
  mis-signed document, it is an unkept promise with three carriers.**
- **A4 was run on all six chapters.** The Polarity Map is the last thing above every signature.

## 8 · Open questions — all for Wendell

- **Q1 · A or B?** Keep the promise or change it. No recommendation offered: this is six chapters
  of your voice against a device you designed, and it is not a call anybody else should make.
- **Q2 · If B, what happens to the signature?** Move it to close the handbook, which is a document
  Voss actually wrote, or retire it. The handbook is already self-attributing.
- **Q3 · The session log at `ch3:169–173`.** Boxed, moved, or licensed as the one place a Head
  speaks in ordinary text.
- **Q4 · Does the Polarity Map want a marker?** It is the book's apparatus repeating across six
  chapters, and it currently sits under a signature that names a Head as its author.

## 9 · What this spec refuses

It does not rule §8; the architecture and the voice are yours. It does not touch ch2 beyond
naming the one sentence in scope. It does not reopen the membrane argument, which is correct. And
it does not use *treatise* as though its meaning were settled, which is the error that put a
header into six chapters this morning before you stopped it.
