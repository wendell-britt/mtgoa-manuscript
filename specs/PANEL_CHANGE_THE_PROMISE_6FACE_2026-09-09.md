---
type: panel
title: "Six-Face panel — changing the promise to fit the text, and what it must not spend"
aliases:
  - change the promise
  - signature into the admissions box
  - should the margin sign
tags:
  - mtgoa
  - editorial
  - architecture
  - voice
created: 2026-09-09
source:
  - specs/SPEC_WHOSE_VOICE_CH2_CH3_2026-09-09.md
  - specs/PROOF_MARKS_CH2_CH3_2026-09-09.md
  - marginalia/specs/MARGIN_ARC.md
  - specs/DECISION_LOG.md
---

# Changing the promise

**Wendell, 2026-09-09:** *"I think we should change the promise. Do a 6 game master analysis on
changing the promise to fit how the text is already set up. I believe this means that the
signature will end up going below or within the admission box and need signatures for each of the
following marginalia."*

Option B is ruled. The panel takes the three consequences he names and one he does not.

## What is on the board before anybody speaks

- **The promise, `ch2:577`,** commits the Heads to 2,800 words each and ends *"Everything past
  that signature is me."*
- **That paragraph is already marked.** `PROOF_MARKS_CH2_CH3_2026-09-09.md` p.50 flags two of its
  sentences, both for the *", and X"* tack-on: *"…on the record about what the teaching did to
  them, **and a margin in a hand that never signs**"* and *"Six people each solved one part of
  this, **and I would rather hand you the argument than the summary**."* **It was being rewritten
  anyway.**
- **The admissions page is already a filed document.** *"Admissions. Filed as required."* Six
  numbered sections in the Head's first person, closing on *"6. A word from the Head."*
- **The margin is the Headmaster.** `MARGIN_ARC.md` and DL-19: the annotator is an in-world
  character revealed as the Headmaster, and ch8 collapses three identities on one beat —
  *"annotator, Headmaster, Sage"* — at the moment the reader is inside the Sage's chapter. Five
  Heads and Bram Tull sign notes in **his** margin there: *"Five of them and Bram, all in my
  margin, and not one of them asked."*

---

## SHAMAN · the Body — *the reader was promised a person and met a narrator*

What went wrong is not a category error, it is a disappointment. The promise offers *their bias
and their quarrel with the other five*, which is an offer of company. What arrives is the fable,
in the voice that narrates every chapter. Nobody is confused; they are let down, and the signature
is where the letdown gets a name on it.

So the new promise must not over-correct into an apology. It should say what the boxes really are
and stop there.

On the marginalia: **signing them changes what the margin feels like.** A margin is overheard.
The reader is reading somebody else's book over their shoulder, which is why it lands. Put a name
under each note and it becomes testimony addressed to the reader, and the intimacy that makes it
work is gone.

**Votes:** rewrite the promise, signature into the box, no names in the margin.

## CHALLENGER · the Line — *the unwelcome sentence about the marginalia*

Signing the ch3–ch7 marginalia **spends the biggest structural payoff in the book to solve a
problem one sentence already solves.**

The margin's anonymity is not an accident. It is the setup for ch8, where the annotator, the
Headmaster and the Sage turn out to be one person, and the reveal only works because the reader
has been reading an unsigned hand for five chapters. Sign them in ch3 and ch8 has nothing left to
reveal. Worse: the ch8 signatures currently mean *the other Heads wrote in his margin* — a
specific, unusual event — and if every margin is signed, that event becomes ordinary and the line
*"not one of them asked"* stops landing.

The problem the proposal is aimed at is real: once the Head signs off inside the admissions box,
the reader could take the margin for the Head's continuing voice. **But the margin has never been
the Head, and `ch2:577` already says so** — *"a margin in a hand that never signs."* That sentence
is being rewritten this week for cadence. Do the work there, in one place, for free.

**Votes:** rewrite the promise; signature into the box; **no** to signing the marginalia, and this
is the one item on which the panel should be immovable.

## REGENT · the Inheritance — *what the change costs, said plainly*

Option B is right and it is not free, and Wendell should hear the invoice before it is paid.

**The Heads get smaller.** The promise gave each of them roughly 2,800 words of running text. The
admissions page is about 600. Under B, the Heads shrink to a boxed document, an epigraph of other
people talking about them, and whatever the margin says. Six characters lose three quarters of
their surface. That is the actual cost of B and no wording fixes it.

**What survives is the convention, and it is worth keeping.** A submitted document that signs
itself is a good device; it only ever needed to point at a document that exists. The admissions
page is filed, numbered, first person, and already ends on *"A word from the Head."* A signature
closing it is not a new invention. It is the convention finally landing on the right page.

On Q6: **the word *treatise* should leave the book.** It names 2,800 words that will not exist.
What remains is a filing, and the book should call it what it is.

**Votes:** rewrite; signature inside the box; no margin signatures; retire the word.

## ARCHITECT · the Design — *inside the box, not below it*

Wendell's phrasing allows two placements and they are not equivalent.

**Below the box** re-creates the exact defect the spec just measured: a signature block that sits
outside the document it attributes, reaching across a boundary to claim text it does not contain.
That is what the old signature did at the close of Section 3, one chapter earlier.

**Inside the box** is the only placement consistent with FR-1. A filed document signs itself
*inside itself*, the way the Headmaster's letter already does — the letter's *"— the Headmaster"*
sits inside `<!-- LETTER -->`, not after it. **The book has already solved this once and the
answer is one line further up.**

Mechanically it is the cheapest option in the repo: `SIGNATURE` stops being a separate insertion
at `seam_point()` and becomes the last line of `HANDBOOK[ch]` in `insertions.py`. One dictionary,
six entries, and `compile.py` loses a branch rather than gaining one.

On the leverage question: **one paragraph in ch2 carries the entire claim.** Rewrite it and six
signatures move. Nothing else in ch3–ch8 has to change except three nouns in the margin.

**Votes:** inside the box. Rewrite `ch2:577`. No margin signatures.

## DIPLOMAT · the Table — *three attributions per chapter is a tax*

Count what the reader is asked to track under the proposal: a Head who signs a box, an author who
owns the running text, and a margin that now signs too. Three attributions, per chapter, six
times. Readers do not hold that, and the ones who try are doing bookkeeping instead of reading.

The current design asks for two and gives the third away free, because an unsigned margin needs no
tracking — it is simply *not the other two*.

On Q4, the three marginal references to *"this treatise"* at `ch6:77`, `ch6:557` and `ch7:159`:
**these are the Headmaster's own words and they must be handled gently.** They are in the voice
the ch8 reveal depends on. Change the noun, keep the sentence rhythm, and do not take the
opportunity to improve them.

**Votes:** no margin signatures. Minimal, surgical noun change in the three marginal lines.

## SAGE · the Board — *name what the proposal is really solving*

The proposal to sign the marginalia is solving a fear: *if the Head signs off early, the reader
will not know who is talking in the margin.* That fear is reasonable and it is answered by the
book already, in the sentence being rewritten anyway.

**The game to refuse is fixing a local confusion by spending a global payoff.** Three identities
collapse in ch8 — annotator, Headmaster, Sage — and the currency that buys it is five chapters of
an unsigned hand. Signing the margin in ch3 pays that price in the first Face chapter for a
benefit the promise sentence delivers for nothing.

The Sage's addition, which nobody else has raised: **the new promise should say less than the old
one.** The old promise failed because it described the chapters in detail and the details were
wrong. A promise that names the boxes and stops cannot be broken by prose that changes later.

**Votes:** rewrite short; inside the box; no margin signatures.

---

## Consensus, six of six

**1 · The signature goes INSIDE the admissions box**, as its closing line, not below it. Below the
box reproduces the reaching defect the spec measured. The Headmaster's letter is the precedent:
its *"— the Headmaster"* sits inside the frame. Mechanically, `SIGNATURE[ch]` merges into
`HANDBOOK[ch]` and `compile.py` loses its seam-point branch.

**2 · The ch3–ch7 marginalia do NOT get signatures.** Unanimous, and the panel asks Wendell to
treat this as the one item to argue with rather than accept quietly. The margin's anonymity is the
currency that buys the ch8 reveal, where annotator, Headmaster and Sage turn out to be one person.
ch8's six signed notes stay exactly as they are and keep their meaning — *the others wrote in his
margin, and not one of them asked.*

**3 · The promise at `ch2:577` is rewritten, short.** It was already marked twice on the proof for
the tack-on construction, so it is being rewritten this week regardless. The new version names the
boxes, says the running text is the author's, and says the margin is a hand that does not sign. It
does not describe what the sections contain, because that is the sentence that broke.

**4 · The word *treatise* leaves the book.** Six signature lines, `ch2:577`, and three marginal
references. The marginal three are the Headmaster's voice and get a noun swap and nothing else.

**5 · The invoice, recorded so it is not a surprise.** The Heads lose about three quarters of
their surface: from ~2,800 running words each to a ~600-word filing plus an epigraph and the
margin. That is what option B costs. It is the honest price of a book that stops promising what it
does not deliver.

## What the panel leaves open

**Voss's session log, `ch3:169–173`.** Once *"above the signature, only the Head"* is retired, this
passage is the Head's voice sitting in the author's running text, and the panel split on whether
it moves into the box, gets its own frame, or is licensed where it stands. **It is the only item
here the panel could not resolve**, and it wants Wendell.

## What the panel refuses

It does not sign the marginalia. It does not place the signature below the box. It does not
improve the three marginal sentences while changing their noun. And it does not write the new
promise inside this document, because that is manuscript prose and goes in front of Wendell as a
draft before it goes anywhere near the file.
