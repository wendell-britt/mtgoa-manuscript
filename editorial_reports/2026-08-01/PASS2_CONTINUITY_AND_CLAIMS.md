# PASS 2 · CONTINUITY AND CLAIMS AUDITOR — whole book, 2026-08-01

**Role:** Continuity and Claims Auditor, `specs/EDITORIAL_OPERATING_SYSTEM.md` §2 —
consistency before polish. Not a proofreader, not a rewriter.
**Scope:** nine chapters, seven shipping appendices, front and back matter — 120,141
words as `build_book.py` assembles them.
**Status: RULED AND APPLIED — Wendell, 2026-08-01.** *"let's make the changes for
these."* CA-1 to CA-6 applied by `instruments/pass2_apply.py`, 30 edits across five
files. The application record is §7.

**This is the pass that had never run book-wide.** The July reports carry a continuity
section per chapter, and `citation_audit.py` mechanised the claims half on 2026-07-31,
but the role itself — one auditor, the whole book, the canonical terms in hand — had
not. The OS puts it *before* line polishing for a reason: *"Central claims need checking
before line polishing begins."* We have now run Pass 3 twice ahead of it. This closes
the gap rather than pretending the order was right.

Instruments ran first and judgment second, per `SPEC_EDITORIAL_OS_INTEGRATION` §3.2.

---

## 1 · What ran

| Instrument | Result |
|---|---|
| `termdebt.py` | 5 real debts; 1 term reported NEVER DEFINED that is defined — see §4 |
| `citation_audit.py` | 0 uncredited · 9 borrowed · 2 dead — 10 of the 11 withdrawn in §4 |
| `build_book.py` | spine assembles, 120,141 words, **2 gaps** (DL-16, DL-17) |
| `chain2.py` | 25 moves, **0 bare claims**; every move carries an example |
| `dupes.py` · `repeat.py` | 0 · concept definition events mapped |
| `rescan.py` | the July claim/continuity/verify bands, re-verified against current text |
| `placeholders.py` | 1 — `ch1:269`, unchanged, P0 |
| `gate.py` | PASS, 0 on four surfaces |

**Thirteen of the July claim-errors are closed by edits made since.** Verified by string
search, not by status column: the joystick is in ch1 (2 hits), ch3's *third stage* is
gone, ch4 now reads *the same five WAVE stages*, ch5's EA table carries five distinct
channels, *read the meter* is gone, ch7's *shortest in the book* is gone, ch8's roster
enumerates seven, *six games* is gone, ch9's WAVE lists five beats and *the altar*
returns zero hits, and ch9 now uses the word BAR. That band was doing real work and the
work landed.

What follows is what survived, plus what a whole-book pass could see that nine
per-chapter passes could not.

---

## 2 · ERROR — a stated fact is wrong

### CA-1 · `ch8:224`, `ch8:262` (+ four) · **a ruling made on 2026-07-31 was never applied**

> *Which altitude is this?* is a vertical question. **Red, Amber, Orange, Green, Teal.** It asks what a person can currently hold.
> …the capacity to take in all the altitudes **(Red, Amber, Orange, Green, Teal)** and still choose to stand somewhere.

**The decision log records this as ruled.** DL row A4: *"Wendell 2026-07-31: **CUT.**
Replacement must carry the same weight — the six Faces are the taught answer-set."*
Status: *"RULED — cut, replacement required at `ch8:223`."*

**Measured today: it is still on the page.** The five-term scale runs at two sites,
*Teal* alone at four more (`ch8:252`, `338`, `348`, `368`), and `termdebt.py` reports
*Teal* first used at `ch8:224` and not glossed until `ch8:338` — 114 lines. *Amber*,
*Orange* and *Green* are never defined anywhere in the book. Magenta, which the scale
implies, is absent book-wide.

- **Recommended action:** apply the ruling. This is not a new decision; it is an
  unexecuted one, and `ch8:262` is the site that uses the scale as the answer-set to the
  Sage's central diagnostic question.
- **Confidence: high.** The ruling is quoted in the log; the text is quoted above.
- **This is the most consequential finding in the pass.** A ruled cut that did not
  happen is worse than one never ruled, because the ledger says it is done.

### CA-2 · `ch7:89`, `ch7:755` against `ch3:431`, Appendix C · **"five channels" names two different sets**

> ch3 · These five channels did not start with me. **Metal, Water, Wood, Fire and Earth** come from **wu xing**…
> ch7 · The Diplomat operates through **five channels**: Bridge-Builder, Translator, Field-Holder, Repairer, Integrative Negotiator.

Appendix C ships under the title *The Five Channels in Practice* and means the first
set. Chapter 7 is the only chapter that reuses the phrase for its own five, and it does
so four times. The chapter also runs *five stages* (Bridge, Translate, Hold, Repair,
Negotiate) whose names shadow the channel names one-for-one, so the reader is holding
three fives at once, two of them called channels.

- **Recommended action:** rename ch7's set — *the Diplomat's five modes* is the word
  every other Face chapter uses for its own five (ch4 modes, ch5 stewardship modes, ch6
  modes, ch8 modes). ch7 is the outlier.
- **Confidence: high** on the collision, **medium** on the fix being a rename rather
  than a route.

### CA-3 · `ch9:1` · **the chapter title is not the chapter's canon name**

> `# CHAPTER 9: CREATING YOUR OWN ALLYSHIP GAME`

`AGENTS.md:64` and `specs/MANUSCRIPT_FILE_CANON.md` both record chapter 9 as **The
Player**. Every other chapter's H1 carries its Face — The Forest, The Shaman, The
Challenger, The Regent, The Architect, The Diplomat, The Sage. Chapter 9 carries a
subtitle where its name should be, and its actual subtitle line (*The Return — From
Playing the Game to Designing It*) sits underneath it doing the job twice.

- **Recommended action:** `# CHAPTER 9: THE PLAYER`, subtitle unchanged. Or amend canon.
  Either way the two must agree before the TOC is typeset.
- **Confidence: high.** This is print-visible in the TOC and in running heads.

### CA-4 · all nine H1s · **three different title formats in one book**

| format | chapters |
|---|---|
| `# Chapter 1 — The Infinite Arcade` — title case, em-dash | ch1 |
| `# CHAPTER 7 — THE DIPLOMAT` — caps, em-dash | ch7 |
| `# CHAPTER 2: THE FOREST` — caps, colon | ch2, ch3, ch4, ch5, ch6, ch8, ch9 |

- **Recommended action:** pick one and apply it to nine files. The caps-colon form is
  the majority at seven of nine.
- **Confidence: high**, and this is the cheapest fix in the report — nine lines.

### CA-5 · seven sites · **a coined term of art is used throughout and credited only in further reading**

*Felt sense* is **Eugene Gendlin's**, from *Focusing*. It appears at `ch1:121`,
`ch3:175`, `ch5:330`, `ch8:295`, `ch9:360` and twice in Appendix A. **Gendlin is named
in exactly one file in the shipping book: Appendix G**, the further-reading list.

The copyright page's sources-and-permissions block names Carolyn Elliott for
*existential kink* and Donella Meadows for *leverage points* — the same situation,
handled. Gendlin is the third case and is not there.

- **Recommended action: VERIFY, then credit.** *Felt sense* may now be common enough to
  be generic; Elliott and Meadows were treated as owed, and this book has twice had to
  correct a credit after the fact. One line on the copyright page settles it.
- **Confidence: high** on the measurement, and this is Wendell's call on the principle.

## 3 · VERIFY — a conflict that may be intentional

### CA-6 · `ch9:474` · eight gates, seven daemons

> *Before you step into the game: a gate scan. **Eight gates, eight questions.***

The scan runs Protector, Controller, Skeptic, Fixer/Healer, Victim, Emotional Body,
Damaged Self — the seven — and then an eighth block that is the **Vulnerable Child**,
whom ch2:434 places *"underneath all of it, at the center"* rather than in the roster.
So eight is defensible and the arithmetic is only visible to a reader tracking both.

- **Recommended action:** VERIFY, not ERROR. If it stays at eight, one clause in the
  opening line — *seven daemons and the child at the center* — closes it for good.

### CA-7 · five terms · prerequisite arrives after the term

`termdebt.py`, against the canonical first-use rule:

| term | first use | first definition | debt |
|---|---|---|---|
| Game Master | `ch1:16` | `ch1:193` | 177 lines |
| the joystick | `ch1:62` | `ch2:386` | one chapter |
| superpower | `ch1:209` | `ch2:394` | one chapter |
| the Forest | `ch1:263` | `ch2:125` | one chapter |
| quest | `ch1:207` | `ch3:892` | **two chapters** |

All five are ch1 opening its own vocabulary and paying it off later, which is a
deliberate move in a first chapter — the reader is meant to feel the frame before she
can define it. *Quest* is the one worth a second look: it is the thing ch1 asks her to
pick and carry into every chapter, and its definition waits until ch3.

- **Recommended action:** VERIFY. Structural, not a claim error, and it belongs to the
  Architect rather than to this pass.

### CA-8 · `back_matter/` · the two build gaps, restated

`build_book.py` reports the spine assembling with two gaps — Kickstarter backers
(DL-16), enrollment page (DL-17). Both are open and both need Wendell, not an auditor.

## 4 · Instrument findings withdrawn — recorded so they are not re-raised

**Ten of `citation_audit.py`'s eleven, and one of `termdebt.py`'s, do not survive
reading.** Recording the reason matters more than the count: both rules over-fire in a
specific, repeatable way.

- **DEAD ×2 — Peter Levine, Stephen Porges.** Credited in Appendix G, never used in the
  body. Appendix G's own header reads *"Where an idea here is load-bearing, it has a
  lineage — and you deserve to know where to read further."* **A further-reading list is
  supposed to contain books the text does not quote.** The rule is measuring the wrong
  appendix. Not findings.
- **BORROWED ×9.** The rule wants an owner within 400 characters of the term. Meadows is
  named at `ch6:251` *and* on the copyright page, and the term then recurs 19 times;
  Laloux is named at `ch8:295`; Kaptchuk and *wu xing* are on the copyright page and at
  `ch3:431`. Credit at first use plus the permissions page is the correct pattern, and
  the rule cannot see it. **Except Gendlin, which is CA-5 above** — the one real finding
  in the nine, which is exactly why the rule earns its keep even at 8 false positives.
- **`termdebt.py`: "Vulnerable Child — NO DEFINITION".** It is defined at first use,
  `ch2:434`: *"the youngest part of you still waits: **the Vulnerable Child, the player
  who should have been holding it the whole time.**"* That is an appositive, and
  `termdebt` matches copula, roster, table, heading and inline glosses but not
  appositives. **This is the same miss that withdrew finding A5 on 2026-07-31** — a
  definition the rule's shapes cannot see. Two instances now; the rule should learn the
  shape before a third.

## 5 · What this pass did not do

- **It did not re-run the Book Architect.** Structure is a separate role and its
  whole-book run is `editorial_reports/2026-07-31/ARCHITECT_WHOLE_BOOK.md`. CA-7 is
  handed to it rather than solved here.
- **It did not verify claims against sources it cannot reach** — Maslach's three
  dimensions, Gorski's mechanism, Carse's finite/infinite distinction and Chou's
  framework are all characterised in ch1 and ch8 and all read fair to me, but I have not
  opened the books. That is a real limit and it is not a finding either way.
- **It did not touch prose.** Diagnosis only.

## 6 · Rulings needed

1. **CA-1 — apply A4's ruled cut.** It is the one item here I would call print-relevant:
   the log says it is done and the page says it is not.
2. **CA-3 and CA-4** — the ch9 title and the three H1 formats. Nine lines, print-visible,
   and cheap.
3. **CA-2** — rename ch7's five channels to five modes, or route it another way.
4. **CA-5** — credit Gendlin on the copyright page, or rule *felt sense* generic.
5. **CA-6** — eight gates: leave, or add the clause.

*No file changed by this pass.*

---

## 7 · Application record — 2026-08-01

30 edits, five files, applied by `instruments/pass2_apply.py` — exact anchors, every
one verified present exactly once before anything is written.

| | |
|---|---|
| **CA-1** · the ruled cut, applied at last | 7 sites in ch8. `ch8:224` loses the colour list; `ch8:262` gets the answer-set Wendell's ruling named — *"its answer-set is the six Faces you have spent this book learning"*; `ch8:252`, `338`, `348`, `368` and `270` take the chapter's own taught vocabulary instead of a colour — the four games at `ch8:260`, or the whole-board view |
| **CA-2** · channels → modes | 18 sites in ch7. **The EA channels keep the word** — the Fire channel, the destination channel, *the length of one channel from the fear end of Metal* are untouched, because those are the wu xing five the copyright page names |
| **CA-3 · CA-4** · titles | `# CHAPTER 1: THE INFINITE ARCADE` · `# CHAPTER 7: THE DIPLOMAT` · `# CHAPTER 9: THE PLAYER` |
| **CA-5** · the credit | copyright page, above the wu xing paragraph: *"Felt sense, used in Chapters 1, 3, 5, 8 and 9 and in Appendix A, is **Eugene Gendlin's**, from Focusing."* |
| **CA-6** · the gate count | *"a gate scan. **Seven daemons and the child at the center:** eight gates, eight questions."* |

| check | before | after |
|---|---|---|
| altitude colours in `manuscript/` | 7 sites | **0 — none anywhere** |
| `termdebt.py` Red / Amber / Orange / Green / Teal | Teal used, glossed 114 lines later; three never defined | **all four rows read 0 uses** |
| `citation_audit.py` | 9 borrowed | **8** — Gendlin closed |
| `gate.py` four surfaces | 0 | **0 — PASS** |
| `compile.py --check` | green | **green** |
| `build_book.py` | 2 gaps | **2 gaps** — DL-16, DL-17, unchanged and not ours |

**Four sites the first run missed, and how they were caught.** Six anchors covered the
colour scale and fourteen covered the rename; re-running `termdebt.py` afterwards
reported **`Green`, one use, defined nowhere** at `ch8:270`, and re-reading every
surviving *channel* in ch7 found three more in the Diplomat's sense. Both are now folded
into the script. *Measure after applying, not only before* — the first run would have
left a single undefined colour in a chapter the pass exists to clear.

**Left open, deliberately:** ch2's H1 still carries a trailing clause — `# CHAPTER 2:
THE FOREST — Why Allyship Keeps Failing (and Where to Start)` — where the other eight
stop at the Face name and put the rest on the subtitle line. That is a fourth variance
and a content question rather than a format one, so it is flagged rather than changed.
