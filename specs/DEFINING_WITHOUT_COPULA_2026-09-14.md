# Defining a term without the copula

**Ruled 2026-09-14 (Wendell):** *"We are reverting to `is` to define things and there are more
sophisticated ways to do this."* The telling instrument (core v34) now flags every
`<subject> is/are/was/were a/an/the <noun>`, which correctly catches the lazy definition
`A daemon is a rule`. Removing the copula by swapping the subject is a dodge; the fix is to
define by what the term **does, contains, or contrasts with**. This is the remediation menu.

The frame is E-Prime (Bourland: English without *to be*) crossed with the book's own rule —
show, don't label. Sources: [E-Prime (Wikipedia)](https://en.wikipedia.org/wiki/E-Prime),
[E-Prime as a Revision Strategy](https://www.researchgate.net/publication/268375253_E-Prime_as_a_Revision_Strategy).

## The techniques, strongest first

1. **By function — what it does.** `X is a Y` → `X <verbs>`. The definition becomes the term's
   action. *"The clean no is the practice of stating a boundary without apologizing"* → *"The
   clean no states a boundary and does not apologize for it."* *"A daemon is a rule in force at
   every move"* → *"A daemon holds one rule in force at every move."*

2. **By operation — how it behaves / what it produces.** `Structural design is the practice of
   understanding why a system produces its outcomes` → `Structural design asks why a system
   produces its outcomes, then redesigns it so the right thing gets built.`

3. **By contrast — genus by what it is not paired with what it does.** Best where the term lives
   against a near neighbour. `A polarity is an ongoing tension` → `A polarity holds a tension you
   manage; a problem takes a solution and closes.` (Contrast carries the definition; neither half
   uses the labelling `is a`.)

4. **Ostensive — show one instance.** Replace the label with a concrete case the reader watches,
   and let the term attach to it. Strongest for a term the surrounding prose already dramatizes.

5. **Appositive on first use.** Introduce the term inside the sentence that already does the work:
   `…the willingness to stay when staying is hard — the Field-Holder's whole job.` rather than
   `What the Field-Holder is for is the willingness to stay.`

6. **become / remain / turn** for a transformation, never `is`: `Finished, it becomes Poignance.`

## What still earns a copula (do NOT force these)

- **Named questions used as a teaching refrain** — the Architect's *"Where is the leverage
  point?"* Ruled a KEEP 2026-09-14; ledger, do not rewrite.
- **Voice anchors** (specs/VOICE_ANCHOR.md) and **boxed HANDBOOK records** — ledger notes.
- A copula whose predicate is an **adjective**, not an article+noun (`the room went quiet`, `it
  is hard`) — the instrument does not flag these and they are not the labelling tell.

## The test after a definition rewrite

Does a verb now carry the meaning, and would the reader know the term from what the sentence
shows it doing? If the sentence still hands over a bare label, it has not been fixed — it has
been reworded. See core `telling.py` docstring and [[rewrite-names-the-relation]].
