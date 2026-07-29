# SIX-FACE PANEL — the *Neutral Channel* collision

**2026-07-29. Convened by Wendell: "Can we have 6 game masters weigh in on how to
solve this collision?" One panelist per Face, each ruling from its own chapter's
doctrine, each required to verify against the files rather than accept the brief.**

Companion to `specs/SPEC_BRACKET_TAGS_2026-07-29.md` §D4, which posed the
question. That section's framing was wrong in two ways the panel corrected, and
both corrections are recorded below.

---

## 1 · The tally

| Face | verdict | who keeps the name *Neutral Channel* | where the definition lives |
|---|---|---|---|
| Shaman | A | Earth/Neutrality | ch7:175 gloss |
| Challenger | A | Earth/Neutrality | ch7:175 gloss, pointing at ch6 |
| Regent | C | Earth/Neutrality | ch7:175 gloss |
| Diplomat | A | Earth/Neutrality | ch7:175 gloss + ch7:77 |
| Sage | C | Earth/Neutrality | ch7:175 gloss |
| Architect | C | **the Control move type** | **ch3** |

**Unanimous, 6–0: ch7 has to change.** No panelist accepted option B — leave ch7
as written and add a disambiguating sentence — and the reason is §2.1.

**5–1 on the name.** Five give *Neutral Channel* to Earth/Neutrality and take the
word *channel* away from ch7's Control moves. The Architect dissents, and its
dissent is about the leverage point rather than the label. §4.

The three C verdicts are not a third position. Regent's C and Sage's C both give
the name to Earth/Neutrality and differ only in scope — Regent removes the
channel word from ch7's headers, Sage additionally renames ch7's `Channel N` to
`Mode N`. Only the Architect's C is genuine dissent.

## 2 · What the panel found that the brief had wrong

### 2.1 The term IS defined, and the definition is false

`SPEC_BRACKET_TAGS` §5 reported *"0 definitions, 11 uses."* Wrong on both counts.
**15 uses**, and there is one definition — ch7:175, found independently by all
six panelists:

> *Emotional alchemy vocabulary: every move below carries a type label.
> **Dissatisfaction moves** alchemize a negative charge into a positive one.
> **Neutral channel moves** redirect a negative pattern into a neutral structure.
> **Satisfaction moves** amplify what is already working. **If these terms are
> unfamiliar, Chapter 3 (The Shaman) has the full system.***

`manuscript/ch3.md` contains **zero** instances of *Dissatisfaction move*,
*Satisfaction move*, *Control move* or *Alchemy move*. Verified. The book ships a
cross-reference sending the reader to a chapter for a taxonomy that chapter does
not contain.

**This kills option B.** B was "the term is undefined, so define it." The term is
defined, in the wrong chapter, wrongly, with a dead pointer. As the Regent put
it: *an inheritance with a dead pointer in it.*

### 2.2 Outside ch7, the book already uses the term the other way

| | text | means |
|---|---|---|
| ch5:283 | "the **Neutral channel's** heaviness into the spaciousness of genuine stewardship" | Earth/Neutrality |
| ch5:291 | "the **Neutral channel's** stillness becomes the foundation for everything else the Regent builds" | Earth/Neutrality |
| ch8:329 | "Flat sight feels like objectivity and amounts to **the Neutral channel** stuck" | Earth/Neutrality |
| ch4:250 | "**The Refusal** (Earth/Neutrality → Peace)… Earth gone flat" | Earth/Neutrality |

3 uses meaning the emotional channel, 12 meaning the structural move type, and
all 12 of the latter are in one chapter. As the Diplomat wrote: **the book has
already voted.**

### 2.3 ch8 ran the natural experiment and ch7 never got the result

`chapters/ch7-sage/G2_CONTROL_MOVES.md`, the Sage chapter's own draft, used
*Neutral Channel* **five times.** Verified at `4172d7a^`.

The shipped `manuscript/ch8.md` **dropped it** — its Control moves read
`**Control Move 1: Panoramic Seer — *perspective as performance***`, with no
channel word — **while keeping** *"the Neutral channel stuck"* for Earth at
ch8:329.

So this exact decision was already made once, correctly, in the Sage chapter, and
never propagated to the Diplomat chapter. **The same failure this whole spec is
about.** ch4, ch5, ch6 and ch9 have no Control move type at all.

### 2.4 ch7 spent the word *channel* on its modes, which is why a sixth had to be minted

`Five modes, five channels, no overlap` appears verbatim in **ch4:242, ch6:245,
ch8:300** — *modes* are a Face's five sub-units, *channels* are ch3's five
emotional channels.

ch7 inverts it. It is the **only chapter in the book** with `### Channel N —`
mode headers (5 of them, under *The Five Channels — How the Diplomat Actually
Works*). Verified: every other chapter has zero.

Having spent *channel* on its modes, ch7 had nowhere to put a move type that
carries no emotion — so *Neutral Channel* got minted as a sixth Diplomat channel,
a slot that exists nowhere else. **Three meanings of *channel* in one chapter.**

### 2.5 The sharpest instance, which the brief missed entirely

ch7:77 assigns the **Translator** channel to `Earth/Neutrality`. ch7:282 then
places `Neutral Channel: Intellectual Superiority Pattern` **inside Channel 2 —
Translator**.

A reader following the table concludes that Earth/Neutrality means intellectual
superiority. The Diplomat's summary: *my own table refutes my own headers.*

## 3 · The etymology — how both rulings became true at once

The Challenger traced it, and it is the finding that dissolves the conflict.
`EMOTIONAL_ALCHEMY_TRANSLATOR.md:27`, verified:

```
### Altitude States (per channel)
- **Dissatisfied**: Mask + desire + fear (unaligned, carrying the charge)
- **Neutral**: In-process, moving through WAVE
- **Satisfied**: Aligned action + artifact (alchemized into gift)
```

**Neutral is an altitude state that exists inside every channel.** Never a channel.

Now read ch7:175 again. Its three move types are *Dissatisfaction moves*,
**Neutral channel moves**, *Satisfaction moves* — named after the three altitude
states, in order. The source heading reads *Altitude States **(per channel)***,
and the parenthetical got absorbed into the middle name.

That is the whole bug. And it means:

- **Wendell's July ruling is correct.** *Neutral* is real emotional-alchemy
  vocabulary, and Earth/Neutrality is genuinely one of the five channels. Both
  halves of "it's one of the emotional alchemy channels" are true of the right
  referent.
- **April's §14 is also correct.** The move type it describes is structural and
  carries no emotion of its own. That is exactly what the *in-process* altitude
  state is.
- **Neither ruling is overturned.** §14 keeps its concept and loses one word.
  Wendell keeps the word and loses nothing. The error is the two words glued
  together, and it was a transcription slip, not a doctrinal choice.

**The panel is explicit on this point because it matters for how the fix reads:**
removing *Channel* from ch7's Control headers **ratifies** the July ruling. It
does not reverse it. The Regent flagged the risk directly — *"it will read as
defiance unless the panel states plainly that the channel survives and only the
mislabel dies."*

## 4 · The dissent — the Architect, and it is worth reading

The Architect agrees ch7 must change and disagrees about where the fix belongs.
Its argument, from ch6's own doctrine:

> ch6:158 — *"what is this system actually rewarding?"* This naming system rewards
> per-chapter invention, and that is exactly what it produced: three incompatible
> schemes.

> ch6:390 — *"where are people already trying to work around the problem? That's
> usually the leverage point. The workaround is a sign."*

**ch7:175 is the workaround.** A drafter needed a move-type definition, found none
in the authority chapter, wrote a local gloss, and pointed at ch3. ch3 — declared
authoritative by the `shaman-first` rule — **defines no move types at all.**
Verified: zero.

So the Architect's position is that A fixes eleven headers, B fixes one sentence,
and neither fixes the empty authority slot that produced both. It wants the
three-move taxonomy added to ch3, and it keeps *Neutral Channel move* as the name
with *neutral* glossed as the destination rather than a sixth channel.

**Its cost, which it states:** ch3 is already the longest chapter and this adds
machinery to its most lyrical passage. **Its own flip condition:** if Wendell
says *Neutral Channel* was always meant as Earth/Neutrality applied to behavior,
then A is right and ch3 needs a bridge instead.

**The majority answer to it:** the taxonomy belongs somewhere, but ch6 already
ships the verb — ch6:486 and ch6:500 give *"transcend, translate, or neutralize"*
as a real choice with three real answers. The Challenger's gloss points there
instead of ch3, which costs ch3 nothing and makes the cross-reference true.

## 5 · The convergent fix

Where five of six agree, with the sixth agreeing on everything except the label:

**F1 — ch7's 12 instances lose the word *channel*.** Not the word *neutral* from
the book; the word *channel* from these labels.

Headers, 5 of them at ch7:282, 320, 358, 402, 410 — adopting the form ch8
already ships:

```
**[CONTROL] — Neutral Channel: Presence Collapse Pattern**
->  **Control 3 — Presence Collapse Pattern**
```

Body, 6 of them at ch7:217, 223, 284, 322, 360, 404:

```
The Neutral Channel pattern here is **presence collapse**
->  The Control pattern here is **presence collapse**
```

**F2 — ch7:175 gets a true gloss.** The current one is the load-bearing error.
Panel-merged text, using the Challenger's cross-reference because it is the one
that resolves:

> *Emotional alchemy vocabulary: every move below carries a type label.
> **Dissatisfaction moves** alchemize a negative charge into a positive one.
> **Satisfaction moves** amplify what is already working. **Control moves**
> neutralize: they take a behavioral pattern that is costing you something and
> redirect it into structure, without alchemizing any charge — which is why they
> carry no channel of their own. Chapter 6 names the choice: transcend,
> translate, or neutralize.*

**F3 — define Earth/Neutrality on first use in ch7.** ch7:77 names it in a table
with no gloss. Shaman and Diplomat both note that F1 without F3 is half a fix.

**F4 — retag the downstream files keyed to §14**, or the term regenerates exactly
as the bracket does: `LEARNING_METABOLISM_CH6_2026-04-20.md:131`
(`neutral-channel-structural`), `chapters/ch5-ARCHITECT/CH5_REWRITE_SPEC.md:25`,
`chapters/ch7-sage/G2_CONTROL_MOVES.md`. Same mechanism as `AGENTS.md` in
`SPEC_BRACKET_TAGS` §D3.

**Cost is lower than feared, and this was checked rather than assumed.**
`MTGOA_52CARDS_PROMPTS.json` carries exactly five `channel` values — Earth, Fire,
Metal, Water, Wood — and none is Neutral. Verified. No card data, no deck schema,
and no `AGENTS.md` entry keys off the string, so F1 is prose, not a data
migration.

## 6 · Open for Wendell — three decisions, in order of size

**Q1 — ratify the 5–1?** *Neutral Channel* means Earth/Neutrality; ch7's Control
moves lose the word *channel*. F1–F4 follow mechanically and I can run them.

**Q2 — the Architect's dissent: does the three-move taxonomy go into ch3?** The
majority route puts a true gloss in ch7:175 pointing at ch6's *transcend,
translate, or neutralize*, and leaves ch3 alone. The Architect's route adds the
taxonomy to ch3 as the authority chapter so this stops recurring. **The
Architect is right that ch3 currently defines zero move types**, which is the
structural hole. The question is whether ch3 should carry that weight three days
from ship.

**Q3 — the Sage's extra: rename ch7's `Channel 1–5` to `Mode 1–5`?** ch7 is the
only chapter using *channel* for a Face's sub-units, against `Five modes, five
channels, no overlap` in ch4, ch6 and ch8. This is the root cause of §2.4 rather
than a symptom, and it is six more headers. It also touches nothing else, since
no data keys off it.

Q1 is the blocking one. Q2 and Q3 are independent and can be deferred without
leaving the book inconsistent.

## 7 · How this gets checked

```
grep -rin "neutral channel" manuscript/          # only ch5:283, ch5:291, ch8:329 survive
grep -c "Chapter 3 (The Shaman) has the full system" manuscript/ch7.md   # 0
grep -n "^### Channel [0-9]" manuscript/ch7.md   # 0 if Q3 is taken, 5 if deferred
```

Against `manuscript/`. Never against a parallel tree — that scoping error is what
produced this whole file.
