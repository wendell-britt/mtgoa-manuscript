# Style sheet — *Mastering the Game of Allyship*

**Opened 2026-08-07** for the final proof, per `SPEC_FINAL_PROOF_2026-08-07.md` §3. The book
reached its last pass without one, which is why the four defects in that spec's §2 all
shipped past every instrument.

**This records what the book already does, measured, and flags where it does two things.**
A style sheet is the book's memory: it goes to the designer and the proofreader so everyone
applies the same conventions through production. **Every open item is now ruled** — four by Wendell on 2026-08-07, the rest on 2026-08-09
during the final proof, the last three by delegation. **The unruled list is empty.**

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

**RULED 2026-08-09 — the `-wards` family takes the American form.** Found in the ch1 deep
read, not by an instrument: `copyedit.py` carried `towards` from the day it was built and did
not carry `afterwards`, so **four body sites survived every pass** — `ch1:204`, `ch2:13`,
`ch7:737`, `ch8:730` — in a book that reads `afterward` 28 times. All four swept; the four
`>` sites (`ch3:296`, `ch4:384`, `ch4:385`, `ch8:623`) stay under the marginalia ruling above.
`ch1:181`'s `backwards` went with them. **The whole family was measured before the sweep so
the board would not gain noise:** forward 40/0 · toward 42/0 · inward 10/0 · outward 9/0.
`afterwards` and `backwards` are now in `copyedit.py`'s `BRITISH` map.

`ch4:370`'s *Apologising* was mine, written 2026-08-07 and fixed the same day. It passed
`gate`, all eight diet counters, the voice linter, `dupes` and `shipcheck` on the way in,
which is the whole argument for this document.

## 2 · Punctuation

**Apostrophes — straight.** 724 straight, **0 curly**, enforced as of 2026-08-07.

**Em-dashes — budgeted, and the budget only ratchets down.** `instruments/emdash.py` owns it.
Glued em-dashes (`word—word`) are a `gate.py` hard fail.

**Ellipses — RULED 2026-08-09 (delegated by Wendell): the single glyph `…`, everywhere.**
Measured 4 `…` against 2 `...`, **and the build does not normalize** — both forms reached the
typeset page and render differently. The two `...` sites (`ch4:84`, `ch4:717`) were swept.
Every site in the book is a trailing-off or a header; none is a suspension of quoted text, so
no four-dot case exists to rule.

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

**RULED 2026-08-09 — Fixer/Healer takes the slash, and the body now agrees with the sheet.**
Four independent readers flagged this in one pass. The sheet had ruled the slash and **the book
ran 16 hyphen against 10 slash**, with the hyphen owning ch5's section heading and the daemon
roll-calls in ch5, ch7 and ch8, and the slash owning ch2's introduction, ch9 and every appendix.
All 16 body sites were swept to the slash, `## Section 5: The Fixer/Healer, Up Close` included.
**`copyedit.py` could never have escalated this**: it files the pair under the read-only HYPHEN
tier, which says *compounds also appearing open — READ, do not sweep*. The tier count went 16 to
15 when the sweep landed. The bare short form *the Fixer* is untouched and remains house.

**first-year — RULED 2026-08-09 (delegated by Wendell): the observed practice is the rule,
and the rule was mis-named.** It never followed the compound-modifier rule because the
hyphenated sites are not modifiers — they are **the noun for a student**: *a first-year*,
*the oldest first-year*, *first-years every season* (`ch4:9`, `ch4:42`, `ch8:49`, `ch8:226`),
4/4 hyphenated. The open sites are **spans of time**: *your first year*, *in the first year*
(`ch3:296`, `ch5:562`), 2/2 open. Six sites, two senses, zero deviations. **Nothing swept.**

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

**RULED 2026-08-09 — `face` is lowercase for the seat, capitalised for the canon.** Lowercase
when the reader is selecting or occupying one: *your home face*, *which face the moment needs*,
*your default face*, *the face that never came up*, *which face am I being*. Capitalised when
the noun names a member of the set categorially: *a Face*, *this Face*, *every Face*, *the last
Face before the Player*, *one per Face*, and always *the six Faces*.

**The first version of this ruling, written the same day, was wrong, and the error is worth
keeping.** It claimed *"ch9's capitals are all the six Faces, the named set, and are correct."*
They were not. The count behind it was the phrase `home face` at 4:1 and nothing else —
**a generalisation from one phrase to a whole rule, never checked against ch9's actual sites.**
ch9 held fourteen slot-sense capitals, `ch8` three more, and a line-based `grep` hid every
occurrence past the first on a long line, so the site count was under-reported twice before an
occurrence-level scan got it right. **Count occurrences, not lines.**

**Swept 2026-08-09 after the deep read: 21 slot-sense occurrences** — ch9 ×18 (including six in
`ch9:670` alone) and ch8 ×3. **17 capitals stay**, all naming-sense, listed above.

**Always capitalised:** the six Faces (Shaman, Challenger, Regent, Architect, Diplomat, Sage)
· the Player · the seven daemons (Protector, Controller, Skeptic, Fixer/Healer, Emotional
Body, Victim, Damaged Self) and the Vulnerable Child at the center, who is the Player rather
than an eighth daemon (ruled 2026-08-11; `ch2:275`, `ch9:430` and the glossary all say seven) · the Forest · the Arcade · the WAVE · the four
domains (Direct Action, Raise Awareness, Gather Resources, Skillful Organizing) · the five
channels' element names (Metal, Water, Wood, Fire, Earth).

**Lowercase:** *altitude*, *native material*, *daemon* as a common noun, *the read*, *the
charge*, *tokens*, *tickets*, *the prize counter*.

## 7 · Names — the cast, spelled once

**Authoritative list**, from `instruments/agency.py`'s `ANIMATE` set, which is what the
agency board scores against:

> Ines · Ravi · Nadia · Tomas · Dara · Yusuf · Ana · Meera · Dele · Alan · Ellis · Ade ·
> Femi · Tess · Bea · Ruth · Jo

**The Examples' second cast, and it was missing from this sheet until 2026-08-09.** §7 said
the list came from `agency.py`'s `ANIMATE` set and then transcribed **only line 88**. Line 87
is also `ANIMATE` and carries a whole second group, so five names the agency board already
scores were absent from the book's memory:

> Priya (`ch5:757`, `ch4:651`) · Marcus (`ch5:668`) · Nia (`ch7:675`) · Sam (`ch2:345`) ·
> Rosa (`ch9:530`)

All five are spelled consistently at every site, so nothing in the manuscript was wrong — the
sheet was short. Found by four of the eight chapter readers independently, which is what a gap
in a shared reference looks like.

**Also named in the book:** Imani · Dana · Corin · Irix · Maera Voss · Kit · Jess (`ch6:672`).

**The six school bylines**, one per Face chapter, each a forename used nowhere else:
Ilse Marrow (`ch3:9`) · Ren Alcott (`ch4:9`) · Tomas Vey (`ch5:9`) · Sim Orrel (`ch6:9`) ·
Nell Ferran (`ch7:9`) · Veyra Sol (`ch8:9`). **`Tomas Vey` is the one exception to the
never-reused rule** — *Tomas* is in `ANIMATE` and appears as an Example person at `ch4:667`.
Recorded rather than changed: renaming a character is a decision, not a copyedit.

**Place names:** Oreve (`ch3:94`, `ch4:14`) · Sethen (`ch3:14`, `ch9:14`).

**`Kit` is deliberately excluded from `ANIMATE`**, ruled 2026-08-05, because `ch8:598` uses it
as an object — *"The kit does have a logic"* — and admitting it would flip an agentless
finding to animate rather than suppress it. **Recorded here so nobody adds it later.**

**Real people are credited in `ON_THE_SHOULDERS_OF`** and their spellings are load-bearing:
Genpo Roshi (Dennis Genpo Merzel) · Robin Rice · Carolyn Elliott · Frederic Laloux · Eugene
Gendlin.

## 8 · Cross-reference format

**Consistent already, and worth locking:** *Chapter 7* (49 uses, never *Ch 7* or *ch7* in the
body) · *Section 4* (77) · *Appendix F* (13).

**CLOSED 2026-08-09 — Appendix B and Appendix D now have on-ramps.** B is pointed at from
`ch9`, closing *"The five moves are the map. The practice is the walking."*; D from `ch3`,
closing the Somatic Markers section. Both use the house form — italic line, description,
colon, `Appendix X:` and the appendix's H1 verbatim. `xref.py` step 7e reads **0 broken · 0
unreferenced**. Any appendix cited by title also needs an entry in `build_book.py`'s
`NAMED_REFERENCES`; B and D were added there in the same commit.

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

## Ruled 2026-08-09

5. **Appendix B and D got their on-ramps.** Item 4 above is closed. See §8.
6. **The `-wards` family takes the American form.** 5 body sites swept, marginalia exempt,
   `copyedit.py` taught the pair. See §1.
7. **`face` is the seat, `Face` is the canon.** 21 occurrences swept. **The first version of
   this ruling was wrong and is kept in §6 with the error.** See §6.
8. **The serial comma reaches the domain blocks.** The 2026-08-07 sweep never touched the
   twenty-four `*You're winning when:*` frames: they held **six** three-or-more-item lists with
   a conjunction and **zero** took the mark, so the register looked exempt and was not.
   Swept: `ch4:757` · `ch5:700` · `ch5:704` · `ch5:708` · `ch6:619` · `ch7:809`.
9. **Fixer/Healer takes the slash.** 16 body sites swept. See §4.
10. **Six more British forms ruled out of the body**, all found by readers rather than by an
    instrument: *rigour* · *programme* · *instalments* · *signalled* · *relabelled* ·
    *disorganised*, plus *per cent* at `ch8:764`. `copyedit.py` now carries all but the
    two-word *per cent*, which its word-token map cannot express.

## Still unruled

8. ~~Ellipses~~ — **RULED 2026-08-09**, see §2. The glyph, everywhere; 2 sites swept.
9. ~~first-year~~ — **RULED 2026-08-09**, see §4. Noun hyphenates, time-span stays open;
   nothing swept.
10. ~~Question marks inside an italic question~~ — **RULED 2026-08-09: the italic question
    keeps its mark wherever it sits in the sentence.** The book was split 3:2 on the same
    construction — `ch3:355` *what is this showing me?*, `ch3:748` and `ch8:673` keep the
    mark mid-sentence; `ch1:117` and `ch9:260` dropped it. The 3 are also standard practice,
    and the "stranded comma" worry (`?*,`) was already house at two of them. Both bare sites
    swept; `ch9:260`'s second question, which closed on a period, took its mark with it.

**The unruled list is empty.**
