---
type: research
title: "Telling not showing — the copula-label, what it hides, and how to finish the thought"
aliases:
  - telling not showing
  - copula label
  - that is the trade
  - show don't tell
tags:
  - editorial
  - mtgoa
  - strunk
  - v2
created: 2026-09-02
review: 2026-09-16
source:
  - manuscript/ch1.md
  - instruments/telling.py
  - specs/EDITORIAL_AUTHORITIES_2026-09-01.md
---

# Telling not showing — the copula-label

**Wendell, reading the proof, 2026-09-01:** *"That is the trade, every time. THAT IS THAT IS THAT
IS."* Then, when asked to teach it rather than have me guess again:

> *"That is the trade points to nothing the reader can hold onto. They have to move backwards to
> remember what it's referring to. Using the definite article* the *in* the trade *assumes there
> is a trade that people know about AND it's supporting something they have to reference back to
> understand… These are telling instead of showing, which is my big critique of the writing time
> and time again… but more than anything these all break Strunk's Rules of Style."*

**Four defects rode in one sentence, and I had been mashing them into a single "metaphor"
complaint.** This separates them, because each has a different fix.

---

## 1 · "That is the trade" — the reader holds nothing, and *the* lies to them

**Two moves, both backward.**

- **The demonstrative points back.** *That* sends the reader in reverse to rebuild the referent.
  The sentence hands over a label and makes the reader fetch its meaning from behind.
- **The definite article presupposes.** *the trade* claims a trade the reader already knows,
  when nothing has named one. *The* smuggles in a shared referent that does not exist, then leans on
  it.

**It breaks Strunk twice, verified against the 1918 text.** Rule 18: *"The word or group of words
entitled to this position of prominence is usually the logical predicate, that is, the new
element in the sentence."* A re-label carries no new element to the emphatic end. Rule 11: the
active voice is *"more direct and vigorous"* — and the flat copula is the least vigorous verb in
the language.

## 2 · "praise has a shape" — a metaphor the reader cannot step into

**The instinct works and the vehicle fails.** Making the abstract concrete is the right reflex,
but praise does not map to *shape* in anyone's shared vocabulary. Praise reaches for a memory or
a scene, and a reader goes there without effort; *shape* asks for a move they do not own,
mid-dense-page, and they stall.

**This one comes from Lakoff, not Strunk** — *Metaphors We Live By*, metaphor as a mapping the
culture already runs. It is rare in this manuscript — **five sentences in the whole
book** — which is exactly why one of them stopped the reader cold.

## 3 · *is* walks you into metaphor whether you meant to or not

**The copula does not only link; it asserts identity, and metaphor lives in identity claims.**
This book's ontology spends *is* on purpose — *allyship is a game*, the psyche as an arcade, the
self as a party of characters, the licensed metaphors of `Metaphors We Live By`. So a careless
*is* makes an accidental metaphor off the system and muddies it. **The copula does not cause the
defect. Using *is* without noticing it has gone metaphorical does.**

## 4 · "every time" — a separate sickness

**Not the *is* problem.** A universal that has to be proven and dies on the first exception.
Wendell: *"everytime has to be proven and is easily disproven."* It keeps a certainty the writing
never earned. Its nearest Strunk relative is Rule 13, *omit needless words*; more honestly it is
a logic defect rather than a style one.

**I do not get to decide which of them are earned, either.** The first draft of this note called the
302 absolutes *mostly fine*. Wendell: *"'mostly fine' you don't get to decide this."* He is
right, and it repeats the copula hedge from one turn earlier — me pre-clearing a defect
class to shrink the work, when the whole thread has established I lack the judgement to. The
instrument surfaces every absolute; the reader clears the earned ones.

## The umbrella, and the honest Strunk footnote

**Telling instead of showing — Wendell's recurring critique.** The show-don't-tell rule he
invokes, *"Use definite, specific, concrete language,"* is **White's, modern Rule 16, and the
1918 edition he uploaded leaves it out.** In that edition the same force comes through Rules 11
and 18. So he is right that Strunk carries most of it: **defects 1 breaks Strunk outright, and 2
and 4 lean on Lakoff and on plain honesty.**

## The remediation — finish the thought, do not tighten the label

**Wendell, on how he fixes one:**

> *"If the reader is making a trade we need to use language that puts them in a place where the
> trading is happening and they see the result of the trade they've made. And feel the
> dissatisfaction. What it's leaving out is that it's a bad trade. Most people don't talk about
> good trades. It flags that the thought is unfinished."*

**Three moves follow, and they carry the method.**

1. **A copula-label is a symptom of unfinished thinking.** The writer reached for the label
   because the scene, the mechanism, and the consequence were not worked out. So the fix is never
   a better sentence in the same slot. **The fix is to finish the thought.**
2. **Put the reader where it happens.** Show them making the trade and seeing the result, so they
   *feel* it rather than get told its name.
3. **The label hides a verdict — surface it.** *Trade* means a *bad* trade; nobody names a good
   one. The label flattened the judgment. Showing it lets the reader feel the bad deal.

**A sketch, not a ruling.** For *"That is the trade, every time,"* the remediation is not a
rewrite of that clause. The remediation lives in a moment: the small lift of being praised, then the drop when
the reader notices they have agreed to stand below the person handing it down. **The v2 rewrite
of the passage is a separate, approved pass** — this note fixes the method, not the paragraph.

## Measured

| corpus | LABEL rate | PROPERTY | note |
|---|---|---|---|
| **the book** | **3.0%** of sentences (181) | 5 | the baseline |
| **the flagged proof passage** (ch1 143–167) | **7.3%** (4) | 1 | **2.4× the book**, flagged HEAVY |

**The gut found the spike again**, exactly as it did with the trailing-and. The copula-label
concentrates where the reading felt worst, and the reader flagged it before the instrument
existed.

## The instrument — `telling.py`

**Three tiers, by how much they mean:**

- **LABEL** — demonstrative or *it* + copula + article + noun. The flagship, the one to drive
  down toward the book's 3.0%. **Guilty until justified:** a LABEL hit is a defect unless the
  thought under it is shown finished, which is rare.
- **PROPERTY** — an abstract handed a physical property. Low-noise (five book-wide), the
  off-system copula-metaphor.
- **ABSOLUTE** — an asserted universal. **302 book-wide, and the instrument surfaces every one.**
  Whether a given absolute is earned or unprovable is a reading call — not the instrument's, and
  not mine. I do not get to pre-clear 302 sentences I have not read as *mostly fine*; that was
  the exact error corrected on 2026-09-02, twice made and twice the same shape.

**It cannot tell a licensed *is* from an accidental one**, because the book's real metaphors use
the copula deliberately. It reports candidates and a rate; the reader applies the test: *does it
show or tell, is the metaphor on-system, is the thought under it finished.*

## The house rule

**A copula-label is a defect until the thought under it is shown to be finished.** Run
`telling.py` on every draft; wired as review step 3e and book step 7h. Drive LABEL toward the
book's own 3.0%, not to zero — the ontology's deliberate metaphors are the floor.

**That makes three instruments built from a defect Wendell caught by eye and no counter saw** —
after `fragment.py` and `trailing_and.py`. The pattern holds: a rule with no call site is a rule
nobody keeps, so the catch becomes a measurement.

## Sourcing

**Strunk verified against the primary text** — Rules 11 and 18 read from the 1918 PDF Wendell
uploaded, quoted verbatim. **Lakoff and Johnson, *Metaphors We Live By*, is second-hand** for
this session; the conceptual-metaphor framing is Wendell's, who reads it into the book's
ontology. The show-don't-tell rule is White's Rule 16 in the modern *Elements of Style*, absent
from the 1918 text.
