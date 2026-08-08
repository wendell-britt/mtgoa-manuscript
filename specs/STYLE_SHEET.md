# Style sheet — *Mastering the Game of Allyship*

**Opened 2026-08-07** for the final proof, per `SPEC_FINAL_PROOF_2026-08-07.md` §3. The book
reached its last pass without one, which is why the four defects in that spec's §2 all
shipped past every instrument.

**This records what the book already does, measured, and flags where it does two things.**
A style sheet is the book's memory: it goes to the designer and the proofreader so everyone
applies the same conventions through production. **Every UNRULED item below needs Wendell.**

---

## 1 · Spelling — **American**

Measured: `-ize` **108** against `-ise` 3 · `honor` **26** / `honour` 0 · `behavior` **22** /
`behaviour` 3.

**RULED:** US throughout the body.

**Six open sites**, and they split into two questions rather than one:

| site | word | note |
|---|---|---|
| `ch4:721`, `ch4:810` | *-ise* forms | **body prose. Fix.** |
| `ch4:28`, `ch6:29` | *behaviour*, *apologising* | inside `>` marginalia — **another hand** |
| `ch8:663`, `ch9:701` | *organised* | inside `>` marginalia — the same hand, twice |

**UNRULED: do the marginalia voices spell British?** Four of six sit in blocks written by
other characters. If those hands are British, this is voice and the sheet should say so; if
not, they are errors. **One ruling settles four sites.**

`ch4:370`'s *Apologising* was mine, written 2026-08-07 and fixed the same day. It passed
`gate`, all eight diet counters, the voice linter, `dupes` and `shipcheck` on the way in,
which is the whole argument for this document.

## 2 · Punctuation

**Apostrophes — straight.** 724 straight, **0 curly**, enforced as of 2026-08-07.

**Em-dashes — budgeted, and the budget only ratchets down.** `instruments/emdash.py` owns it.
Glued em-dashes (`word—word`) are a `gate.py` hard fail.

**Ellipses — UNRULED.** `...` twice against `…` four times. Trivial and wants deciding once.

**Serial comma — UNRULED, and this is the real one.** Measured **27 with against 22 without.**
The book is genuinely split down the middle, so there is no majority to defer to and no
recovering an intent from the text. **Chicago takes the serial comma; recommend it, and it is
a ruling either way.**

**Quotation marks.** Double for speech and quoted material; single nested. Quoted self-talk
uses *italics*, not quotation marks — see §5.

## 3 · Numbers

**UNRULED.** `three` runs 77 times against numerals in 14 places, and nothing has ever
decided it.

**Observed practice:** running prose spells out (*three years*, *five moves*, *four domains*,
*six Faces*); numerals appear in durations and counts inside instructions (*30 seconds*,
*21 days*, *7 days*), in the deck's card counts, and in tables.

**Recommend ruling the observed practice as the rule**: spell out in running prose, numerals
for durations, quantities in exercises, and anything in a table. Chicago's general-prose rule
(spell out under 100) is close enough that the book is already near-conformant.

## 4 · Hyphenation

**The rule the book already follows**, and it is standard: **hyphenate a compound modifier
before a noun, leave it open elsewhere.** *the whole board* / *the whole-board view*. That
accounts for the splits below, which are correct rather than inconsistent:

| | hyphenated | open |
|---|---|---|
| whole-board | 16 | 16 |
| power-game | 3 | 16 |
| hand-over / hand over | 3 | 7 |
| walk-away | 8 | 4 |

**Always hyphenated, in every position** — the book's own compounds: *load-bearing* ·
*first-tier* · *non-renewable* · *body-read* · *self-account* · *Bridge-Builder* ·
*Field-Holder* · *Game-Switcher* · *Panoramic Seer* (open) · *Fixer/Healer* (slash, not
hyphen).

**UNRULED:** *first-year* (3 hyphenated, 2 open) does not follow the modifier rule cleanly
and wants a decision.

## 5 · Italics — what gets them

- **Quoted self-talk and interior speech** — *I know exactly what's happening here*
- **Named moves when the sentence is naming them** — *Say the Unsaid Charge*
- **Book titles** — *Igniting Joy*, *Existential Kink*, *Reinventing Organizations*
- **Single-word emphasis**, sparingly
- **The `*You're winning when:*` frame**, in all twenty-four domain blocks

## 6 · Capitalisation of the book's canon

**A rule already exists and lives in `gate.py`'s comments rather than anywhere a copyeditor
would look. It belongs here.** A move name is **capitalised when the sentence names it** and
**lowercase when the sentence tells you to do it**:

> `ch3:864` the heading — **Say the Unsaid Charge**
> `ch3:876` the imperative — *say the unsaid charge:*

**Both spellings are canon.** ch3 obeys this at all five of its sites and it was nearly
"corrected" into inconsistency on 2026-08-03.

**Always capitalised:** the six Faces (Shaman, Challenger, Regent, Architect, Diplomat, Sage)
· the Player · the eight daemons (Protector, Controller, Skeptic, Fixer/Healer, Emotional
Body, Victim, Damaged Self, Vulnerable Child) · the Forest · the Arcade · the WAVE · the four
domains (Direct Action, Raise Awareness, Gather Resources, Skillful Organizing) · the five
channels' element names (Metal, Water, Wood, Fire, Earth).

**Lowercase:** *altitude*, *native material*, *daemon* as a common noun, *the read*, *the
charge*, *tokens*, *tickets*, *the prize counter*.

## 7 · Names — the cast, spelled once

**Authoritative list**, from `instruments/agency.py`'s `ANIMATE` set, which is what the
agency board scores against:

> Ines · Ravi · Nadia · Tomas · Dara · Yusuf · Ana · Meera · Dele · Alan · Ellis · Ade ·
> Femi · Tess · Bea · Ruth · Jo

**Also named in the book:** Imani · Dana · Corin · Irix · Maera Voss · Kit.

**`Kit` is deliberately excluded from `ANIMATE`**, ruled 2026-08-05, because `ch8:598` uses it
as an object — *"The kit does have a logic"* — and admitting it would flip an agentless
finding to animate rather than suppress it. **Recorded here so nobody adds it later.**

**Real people are credited in `ON_THE_SHOULDERS_OF`** and their spellings are load-bearing:
Genpo Roshi (Dennis Genpo Merzel) · Robin Rice · Carolyn Elliott · Frederic Laloux · Eugene
Gendlin.

## 8 · Cross-reference format

**Consistent already, and worth locking:** *Chapter 7* (49 uses, never *Ch 7* or *ch7* in the
body) · *Section 4* (77) · *Appendix F* (13).

**Two open items from the spec:** **Appendix B and Appendix D are never referenced from the
manuscript.** Both ship. Appendix B is the quests-and-campaigns workbook, which is the part
the reader is meant to run.

**Back matter uses the short form** — the index reads *Ch 3 §6*. That is fine as an index
convention and should not spread into the body.

---

## What is still UNRULED

1. **Serial comma** — 27 / 22, no majority. *(recommend: take it)*
2. **Do the marginalia hands spell British?** — settles four sites at once
3. **Number policy** — *(recommend: rule the observed practice)*
4. **Ellipses** — `...` or `…`
5. **first-year** hyphenation
6. **Appendix B and D** — do they get on-ramps from the body, or ship unreferenced?
