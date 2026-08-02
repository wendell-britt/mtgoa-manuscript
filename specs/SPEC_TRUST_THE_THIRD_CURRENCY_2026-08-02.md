# SPEC — Trust, the third currency

**2026-08-02. Wendell:**

> *"Another token emerged that I'd been avoiding until now. Trust is also a token, and
> the hallucinated line that's making this feel the most clunky is revealing that.
> Somewhere in between your own motivational energy is the fact that you're literally
> not allowed to practice allyship without consent, and you can't get consent without
> trust. This is a BIGGER change and I'm running out of gas, but I do want to make an
> editorial spec that will get us to the right place."*

This spec makes no prose. It records the finding, the evidence, the model, the rulings
needed, and the smallest version that fixes the defect.

---

## 1 · The finding

**The economy as built is a closed loop inside one person.**

`ch1:99`–`125` builds it: tokens are what you spend, tickets are what the play pays
back, the prize converts back into tokens. Every term in that circuit belongs to the
player. **The person being helped never enters the economy at all.**

And the book's own standing rule says the loop cannot close that way. Author's note,
`front_matter/authors_note.md:35`:

> *"You can make your move. You cannot make another person satisfied, and reaching for
> that is the exact place where helping curdles into something else."*

So the apparatus describes a solo optimisation problem, and the rule that governs the
practice says allyship is not one. **That contradiction is load-bearing and nobody has
named it.**

### Which line revealed it

The drafted Passion paragraph:

> *"Pay yourself in enthusiasm and you can spend it on the people you came here for."*

**You cannot spend it on them.** You can offer. Whether the offer lands is not yours,
and the sentence reads clunky because it is trying to complete a transaction with a
party the economy never named. The clunk is the model failing, not the wording.

---

## 2 · What canon already contains

| | count | where |
|---|---|---|
| *trust* | **43** | ch7 **13**, ch3 6, ch4 5, ch6 4, ch5 4, ch8 3, ch1 2, ch2 1, **authors_note 0, ch9 0** |
| *consent* | **1** | `ch5:37`, and it is about naming people in a ledger, not about the practice |
| *permission* | 9 | none of them about the other person's permission |

**Trust is already being used as a currency in Chapter 7 and is not recognised as
one.** Three sentences do the whole job:

- `ch7:638` — *"Prerequisite: some real trust has been built. This move requires a
  history."* — **a balance you must have before a move is available.**
- `ch7:652` — *"Ruptures named and repaired build more trust than ruptures that never
  happened."* — **it accrues, and it accrues through cost.**
- `ch7:181` — *"Care means protecting the connection itself: the trust, the willingness
  of people to stay in contact."* — **an asset with a maintenance cost.**

Prerequisite, accrual, maintenance. That is a currency, described three times in one
chapter, in a book whose economy chapter has never heard of it.

**Chapter 1 has two uses of *trust* and neither is mechanical.** The economy is built
in a chapter that does not have the word.

---

## 3 · The model

Three currencies, and the third is categorically unlike the first two.

| | Who holds it | What it does |
|---|---|---|
| **Tokens** | you | what you spend to make a move. Renewable or not. `ch1:99`–`113` |
| **Tickets** | you | what the play pays back, redeemable at one of two counters. `ch1:115`–`125` |
| **Trust** | **the other person** | whether your move is permitted to land at all |

**Consent is the gate; trust is what the gate runs on.** A move you are not permitted
to make is not a move, however well funded and however skilfully played. That is the
sentence the current economy cannot say.

### The asymmetry is the point, and it is also the safeguard

**Tokens and tickets are yours to manage. Trust is not yours at all.**

You can be trustworthy. You cannot make somebody trust you — which is the author's
note rule, restated in the economy's own vocabulary, and the reason the rule exists.

**This asymmetry must be built in from the first sentence, because the failure mode is
severe.** If trust reads as a currency you can farm, the book rebuilds the counter
marked applause one level down: a score you optimise, extracted from the people you
came to serve. That is a more sophisticated version of the exact defect Chapter 1
diagnoses, and it would be this book's worst possible outcome.

**Design rule: trust is never counted, never a target, and never something the reader
is told to build.** It is the thing that decides whether the rest of the economy can
do anything, and the only lever the reader has on it is being the kind of person it
accrues to.

---

## 4 · What this fixes, beyond the clunky line

1. **The three-games section stops doing too much.** It is currently carrying an
   economy argument it also has to explain. With the third currency built in ch1, the
   section calls back instead of teaching, which is the fix Wendell asked for and is
   worth several hundred words on its own.
2. **The Diplomat gets a spine that reaches back.** `ch7`'s thirteen trust sentences
   become the chapter that pays off a currency introduced in Chapter 1 rather than
   thirteen local observations.
3. **The book's central rule gets a mechanism.** *You cannot make another person
   satisfied* currently arrives as an ethical instruction. With trust as the third
   currency it becomes a fact about how the game is built.
4. **It answers a question Chapter 1 raises and drops** — `ch1:46`, the vocabulary
   screening. A screen exists because trust is expensive and strangers are unknown.

---

## 5 · The rulings this needs

**R-T1 · Where does the third currency get built?** Recommended: a third section in
Chapter 1 immediately after *The Ticket System*, roughly 300–400 words. It cannot go
later than ch1 because ch2 onward assume the economy is complete.

**R-T2 · What is it called?** *Trust* is the honest word and it is not a game noun.
The arcade frame has no object for "permission from another person" because arcades do
not need one — **the machine never has to agree to be played.** That is either the
metaphor breaking or the most interesting thing in the chapter. Options: name it
plainly as the place the arcade frame stops; or find the object (a member's card, a
door somebody else holds); or let it be the one thing in the Arcade that is not a
machine.

**R-T3 · Does consent appear as a word?** It currently appears once in the book and
not about the practice. Naming it explicitly is a real decision with a register cost.

**R-T4 · Does trust get retrofitted into ch7, or does ch7 stay as it is and ch1 point
forward to it?** Cheaper: ch1 builds it, ch7 unchanged, and the connection is made in
one sentence at `ch7:638`.

**R-T5 · Does ch9 need it?** Zero uses of *trust*, and it is the closing chapter.

---

## 6 · The minimum version

If the full build is too much right now, the smallest change that removes the defect:

1. **One section in ch1** after the Ticket System, ~300 words, establishing that a
   third currency exists, that somebody else holds it, and that no amount of the other
   two substitutes for it.
2. **One sentence changed in the Which Game draft** — *spend it on* becomes *offer it
   to* — which is correct only once §1 exists.
3. **One sentence at `ch7:638`** connecting the prerequisite to the currency.

Everything else in this spec can wait. The three items above are what stop the book
from describing allyship as a solo optimisation problem.

---

## 7 · What not to do

- **Do not add a trust counter to `prose_diet.py` or any instrument.** This is a
  content model, not a measurable defect.
- **Do not sweep the 43 existing *trust* mentions.** Most are ordinary English usage.
  The ones that matter are the three in ch7 named above.
- **Do not write the section before R-T2 is ruled.** The naming decision determines
  whether the arcade metaphor extends or is deliberately broken, and that changes every
  sentence in it.
