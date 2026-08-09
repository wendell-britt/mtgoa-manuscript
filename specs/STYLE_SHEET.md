# Style sheet — *Mastering the Game of Allyship*

**Opened 2026-08-07** for the final proof, per `SPEC_FINAL_PROOF_2026-08-07.md` §3. The book
reached its last pass without one, which is why the four defects in that spec's §2 all
shipped past every instrument.

**This records what the book already does, measured, and flags where it does two things.**
A style sheet is the book's memory: it goes to the designer and the proofreader so everyone
applies the same conventions through production. **Four of the six open items were ruled by Wendell on 2026-08-07; two trivial ones remain.**

---

## 1 · Spelling — **American**

Measured: `-ize` **108** against `-ise` 3 · `honor` **26** / `honour` 0 · `behavior` **22** /
`behaviour` 3.

**RULED:** US throughout the body.

**Six open sites at the time of writing**, split into two questions rather than one:

| site | word | note |
|---|---|---|
| `ch4:721`, `ch4:810` | *behaviour* | **body prose — fixed 2026-08-07** |
| `ch4:28`, `ch6:29` | *behaviour*, *apologising* | inside `>` marginalia — **another hand** |
| `ch8:663`, `ch9:701` | *organised* | inside `>` marginalia — the same hand, twice |

**RULED 2026-08-07 — the marginalia hands may spell British.** *"marginalia hands can spell
British."* So the `>` blocks are voice, not error, and the sheet says so. The two body sites
at `ch4:721` and `ch4:810` were `behaviour` and are now `behavior`. **Body reads 24 / 1, and
the 1 is a marginalia block.**

`ch4:370`'s *Apologising* was mine, written 2026-08-07 and fixed the same day. It passed
`gate`, all eight diet counters, the voice linter, `dupes` and `shipcheck` on the way in,
which is the whole argument for this document.

## 2 · Punctuation

**Apostrophes — straight.** 724 straight, **0 curly**, enforced as of 2026-08-07.

**Em-dashes — budgeted, and the budget only ratchets down.** `instruments/emdash.py` owns it.
Glued em-dashes (`word—word`) are a `gate.py` hard fail.

**Ellipses — UNRULED.** `...` twice against `…` four times. Trivial and wants deciding once.

**Serial comma — RULED 2026-08-07: take it.** Measured 27 with against 22 without before the
ruling. **Of the 22, only 7 were genuine three-or-more-item lists** — the pattern was 68%
false positive on pairs (*refined and unsaid*, *again and again*, *pause and ask*), which is
why the sweep was read before it was run. All 7 fixed. Two of them were sentences written
the same morning.

**Quotation marks.** Double for speech and quoted material; single nested. Quoted self-talk
uses *italics*, not quotation marks — see §5.

## 3 · Numbers

**RULED 2026-08-07: the observed practice is the rule.**

**The practice:** running prose spells out (*three years*, *five moves*, *four domains*,
*six Faces*); numerals appear in durations and counts inside instructions (*30 seconds*,
*21 days*, *7 days*), in the deck's card counts, and in tables.

**So: spell out in running prose; numerals for durations, quantities in exercises, and
anything in a table.** Chicago's general-prose rule (spell out under 100) is close enough
that the book was already near-conformant, which is why nothing needed sweeping.

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

**The same rule governs the four domains**, found 2026-08-07 by `copyedit.py` reporting three
false positives. *Direct Action* names the domain; *taking direct action* describes the
activity and is correctly lowercase. The book renders the set as gerunds at `ch2:567`,
`ch3:940` and `ch9:680` — *gathering resources, raising awareness, direct action, skillful
organizing* — and all three are right.

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

## Ruled 2026-08-07

1. **Serial comma — take it.** 7 real sites fixed.
2. **Marginalia hands may spell British.** Voice, not error. 2 body sites fixed.
3. **Number policy — the observed practice is the rule.** Nothing to sweep.
4. **Appendix B and D — they get on-ramps.** Wendell: *"we can find points in the text that
   pushes people to the appendix B & D."* **A task, not a ruling**, and it is the one item on
   this sheet that adds prose rather than regularising it. Appendix B is the quests-and-
   campaigns workbook and Appendix D is the emotional alchemy practices; each needs a pointer
   from the chapter whose work it continues.

## Still unruled

5. **Ellipses** — `...` twice against `…` four times.
6. **first-year** — 3 hyphenated, 2 open, and the compound-modifier rule does not explain it.

Both are trivial and neither blocks the deep read.
