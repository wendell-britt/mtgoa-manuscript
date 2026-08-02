# SPEC — Print readiness, measured

## STATUS — 2026-07-30, on `claude/print-apparatus-off-master`

**This branch is `master` plus the print apparatus.** Everything below §1 was
measured on a different base and is kept as the record of what was found. This
block is the state here.

| Blocker | State |
|---|---|
| B1 — gate fails | **Closed. 0 hits, GATE PASS.** R9 filled 2026-07-30; R8 was ruled on master; the A0 counter reads 0. |
| B2 — appendices never gated | **Closed.** First gated run found 1 hit, in master's own new Appendix C prose. |
| B3 — front and back matter | **Closed.** Zero placeholders. ISBN lines absent by decision — none assigned, an ebook needs none. |
| B4 — nothing built a book | **Closed.** `build_book.py --write` emits 112,054 words. Spine complete. |
| §3 — appendices describe the retired book | **A, B, D, E, F, G revised.** Appendix C is an open ruling — see below. |
| §4 — Five Channels unlettered | **Still open.** `ch3:400` points at it; it has no letter and sits in `drafts/`. Reported UNPLACED every build. |
| §5 — reference style | **Master's style, not mine.** Master normalised to `Appendix: Title`. Consistent, but no letter, so the contents page cannot be matched against it. Low priority. |
| §6 — heading styles | **Closed 2026-08-01 on master.** One form, and every chapter now carries a plain clause as well: `# CHAPTER N: THE FACE — clause`, over the italic subtitle `d65ba78` ruled a feature. `6cbdf8d` drafted the eight new clauses against each chapter's own argument; `ff942d3` taught the contents page to set the pair as `The Shaman: What to Do With What You Feel`. `instruments/typeset.py` reads the form, reuses `build_book.py`'s `toc_title` so the two contents pages cannot disagree, and BLOCKs on a chapter that departs from it — the nine hand-maintained display titles are gone. **Note for anyone reading the July branches:** `claude/book-print-readiness-august-ar95mo` commit `6026b06` also normalised the form, by *deleting* Chapter 2's clause. It is superseded — master went the other way and gave the other eight one. |

**The gate is green as of 2026-07-30.** R9 is closed.

### The rulings that need Wendell

1. ~~**R9**~~ — **closed 2026-07-30.** Ash was told at **nineteen** and believed it
   for **another thirty years**. The same ruling settled Ash's pronouns as
   **they/them**, which ch4's marginalia already used and ch8:225 contradicted.
2. **Appendix C.** Master is repairing the Key Terms glossary in place; a parallel
   branch retired it and gave letter C to The Five Channels. Master's repair is real
   but partial — the glossary still carries 1 eight-gate definition, 3 Vulnerable
   Child references, 4 `[Ch0]` tags, and 11 trigram references. Repair or retire.
3. **The Five Channels appendix** — give it a letter, or cut `ch3:400`.

### Carried from the prose branch, and why only these two

`claude/book-print-readiness-august-ar95mo` conflicts with master across 91 hunks.
Two chapter edits came anyway:

- **ch4's `kindness-deceiving-as-cruelty`** was backwards. Not a style call.
- **ch1's subtitle**, purely additive, in master's heading form rather than mine.

Everything else on that branch is deferred, and measurement says most of it should
be **dropped rather than merged**: master reached 2 denying negations against that
branch's 9, and 9 `which is` tails against its 64. The exception is say-the-noun,
where that branch reached 6 and this one stands at 25. That pass is worth
re-applying; the W7 and `which is` work is superseded.

### Withdrawn

`rather than` as a defect. 103 uses on the other base, essentially no local
clustering, and the one cluster is a deliberate teaching triad in ch3.

**Do not quote line numbers from any spec.** They drift with every frame
reapplication. Grep the file.

---

**2026-07-29. Ships August 1.** Every number here came out of an instrument run
against canon on 2026-07-29. Where it contradicts `SPEC_FINISHING_PASS_2026-07-29.md`,
`MANIFEST.md`, or `specs/MANUSCRIPT_FILE_CANON.md`, this document is the measurement
and those are the claim.

Reproduce the whole thing:

```bash
python3 marginalia/compile.py --apply     # the frame is part of the printed page
python3 instruments/gate.py               # three surfaces now, not two
python3 instruments/build_book.py         # the spine, and what is missing from it
python3 instruments/build_book.py --toc   # the generated contents
```

---

## 1 · The correction that changes the schedule

**Both "hard print blockers" are written.** `MANIFEST.md` and
`MANUSCRIPT_FILE_CANON.md` both say the Polarity Map and the 3-2-1 Shadow Process
exist "not in the project, not on any disk." They are on this disk, committed, and
have been through an ordering pass that assigned them letters:

| Claimed missing | Actually at | Words |
|---|---|---|
| Appendix — The Polarity Map | `appendices/APPENDIX_F_POLARITY_MAP.md` | 951 |
| Appendix — The 3-2-1 Shadow Process | `appendices/APPENDIX_E_321_SHADOW_PROCESS.md` | 1,088 |

The full appendix set A–G is written — 10,556 words of it. `ON_THE_SHOULDERS_OF.md`
is Appendix G, and it answers **R4**: it is a source-lineage bibliography, not a
belief-to-superpower map, so the six daemon-alliance byline lines have nothing to
be diffed against. R4 closes.

**This does not mean the appendices are ready.** It means the remaining work on
them is revision and integration, not composition — a different and smaller job,
but not a finished one. See §3.

## 2 · What actually blocks the typesetter

Four things, in the order they bite.

### B1 — The gate fails, and two of the three hits are placeholders

```
surface        andbut   banned   emdash       A0   stacks   tokens
body                0        0        0        1        0        2
marginalia          0        0        0        0        0        0
appendices          4       20        0        0        3        0
```

`⟦ASH-AGE⟧` and `⟦ASH-SPAN⟧` were the last two, and Wendell filled them on
2026-07-30: **nineteen** and **another thirty years**. Nothing on this list is
blocked on a person now, and the gate reads 0 on all four surfaces. The four
dormant tokens are not in canon and do not hold it
until they are filled.

The body A0 hit is ch3's *"a time you were told something true"* — **R8**, still
open, and plausibly a licensed recall-prompt rather than a violation.

### B2 — The appendices had never been gated

The gate read `manuscript/` only. Roughly 9,000 words of shipping prose were
outside it. Extended on 2026-07-29 to a third surface; the appendices came in at
**27 hits** on their first run — 20 banned words, 4 And/But openers, 3 negation
stacks. Concentrated in A (7 banned, 3 stacks) and F (6 banned).

These are mechanical and fixable in a pass. They are only alarming because they
were invisible: the standing rule says every counter reads 0, and for the
appendices nobody had ever run the counter.

### B3 — Front and back matter, genuinely unwritten

This claim in the planning docs holds up. Confirmed absent from every directory:

| | Component | Required |
|---|---|---|
| front | Half title | **blocker** |
| front | Title page | **blocker** |
| front | Copyright page | **blocker** |
| front | Table of contents | generated — `build_book.py --toc` |
| front | Dedication, author's note | optional |
| back | About the author | **blocker** |
| back | Acknowledgements, enrollment page | optional |

The copyright page needs the Wilber credit for Appendix E and whatever the
Elliott correction implies for the source stubs. The enrollment page waits on
**R1** (school name), which is why it is marked optional rather than blocking.

### B4 — Nothing built a book

`compiled/MTGOA_COMPILED_2026-05-29.md` is two months stale and
`compiled/build_compile.py` reads the retired `chapters/` tree. Neither reflects
canon. `instruments/build_book.py` (new) assembles from canon, generates the
contents, and exits non-zero while a required component is missing — so the gap
is enforced rather than asserted.

Current spine total: **114,322 words** across 16 present components, 53
marginalia blocks applied.

## 3 · The appendices need revision, not composition

Three of the seven describe a book that no longer exists. Measured against the
retired-canon list in `MANUSCRIPT_FILE_CANON.md` §"Structural facts that are current":

| Appendix | gate-walk refs | Vulnerable Child | `[Ch0]` index | hexagram/trigram/oracle |
|---|---|---|---|---|
| A — Four Allyship Domains | 1 | 2 | 0 | 0 |
| B — Quests & Campaigns | 7 | 2 | 0 | 0 |
| **C — Key Terms** | **10** | **4** | **4** | **51** |
| D, E, F, G | 0 | 0–1 | 0 | 0–1 |

**Appendix C is the serious one.** It is the glossary, which is the one appendix a
reader consults rather than reads — and it defines a different book. It gives
*The Face* as "Protector, Controller, Skeptic, Fixer, Victim, Damaged Self"
against canon's Shaman, Challenger, Regent, Architect, Diplomat, Sage. It defines
*Gate* as "one of eight threshold moments," a walk removed from Chapters 4–8. It
defines *Vulnerable Child* as "the eighth gate," a daemon that left Chapter 2's
roster. Its chapter tags are 0-indexed throughout, so *"Upper trigram of Ch2
(Shaman)"* points at The Forest.

Appendix B's eight quests are keyed to the same removed gate walk and 0-indexed
chapter numbers. Appendix A carries the lighter version of it.

D, E, F, and G are current and need only the B2 gate pass.

## 4 · The Five Channels appendix has no letter

`manuscript/ch3.md:400` sends the reader to *"Appendix — The Five Channels in
Practice."* It is written — 1,176 words, gate-clean on first run — and it is in
`drafts/`, outside the A–G lettering, so it appears in no contents and no spine.
Either it gets a letter and the sequence after it shifts, or the ch3 reference
comes out. `build_book.py` reports it under UNPLACED until one of those happens.

## 5 · Cross-references resolve, but not by the numbers in the plan

The five Polarity Map references and the 3-2-1 references are live and correctly
worded in canon. The line numbers quoted in `MANIFEST.md` and the finishing-pass
spec are stale by roughly 40 lines because they were taken with the frame
stripped:

| Reference | Plan says | Actually at |
|---|---|---|
| Polarity Map, ch3 | 623 | 575 |
| Polarity Map, ch4 | 148 | 199 |
| Polarity Map, ch5 | 188 | 234 |
| Polarity Map, ch6 | 151 | 194 |
| Polarity Map, ch7 | 121 | 168 |

They also name the appendices by title, not letter — *"Appendix: The Polarity
Map"* — while the files are lettered. That is a defensible house style, but it has
to be one style: ch2:556 uses *"Appendix A"* and ch3:545 uses *"Appendix — 3-2-1
Shadow Process"* in the same book.

Two forward-references inside the appendices are off by one against canon.
`APPENDIX_E` says the first practice is in Ch3; `ch3.md:545` says Chapter 4.
`APPENDIX_A` says "After Ch8," which was written when the Sage was Ch8's
neighbour rather than Ch8 itself.

## 6 · Chapter headings are in four styles

A typesetter needs one. `build_book.py --headings`:

```
Chapter 1    # Chapter 1 — The Infinite Arcade          title case, em dash, no subtitle
Chapter 2    # CHAPTER 2: THE FOREST — Why Allyship…    caps, colon, subtitle inside the H1
Chapter 3    # CHAPTER 3: THE SHAMAN                    caps, colon
Chapter 7    # CHAPTER 7 — THE DIPLOMAT                 caps, em dash
Chapter 9    # CHAPTER 9: CREATING YOUR OWN ALLYSHIP…   caps, colon, no Face name
```

Chapters 2–8 carry a `## *subtitle*` line; 1 and 9 do not. Chapter 2 carries its
subtitle twice, once in each. The generated TOC normalizes all of this, so this
blocks a typeset page rather than a contents page.

## 7 · Editorial state, for scheduling only

`review.py --mode body`, frame stripped: **BLOCK 80 · WARN 89 · INFO 169.** The
BLOCK count is 25 say-the-noun and 25 abstraction-noun subjects, plus singles.
The finishing pass's W2 has landed — *moves without stopping condition* is down
to **1 chapter** from 6. W7's denying negations no longer dominate the count.

None of this blocks print. It is quality work with a deadline behind it, and §2
is quality work with a deadline in front of it.

## 8 · Sequence for the remaining days

1. **B2** — clear 27 appendix gate hits. Mechanical, no rulings needed.
2. **§3** — rewrite Appendix C against current canon; retag B's quests. The
   glossary is the highest-risk single artifact in the book.
3. **B3** — draft half title, title page, copyright, about-the-author.
4. **§4, §5, §6** — settle appendix lettering, one reference style, one heading
   style. All three are decisions, then a mechanical pass.
5. ~~**B1**~~ — done. Tokens filled 2026-07-30, R8 ruled on master.

## 9 · Rulings this document needs

- ~~**R9**~~ — **closed 2026-07-30.** nineteen / another thirty years, and Ash is
  they/them. The gate went green on the same commit.
- **R8** — ch3's A0 hit: license as recall-prompt, or rewrite.
- **R10 (new)** — the Five Channels appendix: give it a letter, or cut the ch3
  reference.
- **R11 (new)** — appendix reference style in canon: by letter or by title.
- **R12 (new)** — Appendix C: rewrite against current canon, or cut the glossary
  from this edition. Rewriting is ~1,100 words of definitional prose against a
  book the writer knows well; cutting is free and loses a reference surface.

**R4 closes** (§1). R1 still gates the enrollment page and half-title only.

---

## 10 · The assertion blocker — asserted reader experience

**Added 2026-08-01, batch nine.** Wendell, ruling on a drafted line of mine:

> *"This sentence structure needs to get banned. We don't know they've been on the
> paying end of this. We can invite them to imagine and it solves all of these
> assertions. But these types of assertions have become a blocker for the book. We
> need a plan to solve for this and add it to the readiness guide."*

### What it is

A declarative about what the reader has done, felt, seen or become, stated as fact.
Distinct from assumed prior *knowledge* (a term used before its definition), which
`assumed.py` already tracked. This is assumed prior *experience*, and it fails
differently: a reader who has not had the experience is not confused, they are
excluded, and they close the book on the sentence that told them who they are.

**It has been arriving as read-through notes since batch two and was never
consolidated.** `N12` (*You are a Game Master*), `N15` (*You have done this before*
— Wendell: *"done what before? I hate all intros like this, vague and weird"*),
`N17` (*You graduated from it years ago*), the ch1-opener note about assumed secret
competence, and now `N58`. Five notes, four batches, one defect.

### The measurement

`instruments/assumed.py` gains an `EXP:` tier and counts the licensed alternative
alongside it, because Wendell's repair is a conversion rather than a deletion.

| | ch1 | ch2 | ch3 | ch4 | ch5 | ch6 | ch7 | ch8 | ch9 |
|---|---|---|---|---|---|---|---|---|---|
| assertions | **37** | 5 | 19 | 25 | 23 | 11 | 18 | 24 | **50** |
| of those, asserted experience | 19 | 1 | 4 | 9 | 10 | 3 | 5 | 12 | **35** |
| invitations | 2 | 3 | 2 | 1 | **0** | 1 | **0** | **0** | 5 |

**212 assertions against 14 invitations, book-wide.** The count nearly doubled when
the experience tier was added, which means roughly half of this defect was invisible
to the instrument that was supposedly watching it.

**Three chapters extend no invitation at all** — ch5, ch7, ch8. Chapter 9 is the
worst on both counts and is also the chapter that closes the book.

### The plan

**The repair is a conversion, not a cut.** Every one of these sentences is trying to
create recognition, which is the right instinct; asserting it is what breaks. The
grammar of the fix is small and mechanical:

| Asserted | Invited |
|---|---|
| You've been on the paying end of this. | Picture yourself on the paying end of this. |
| You have done this before. | If you have ever done this — and most people have — |
| That was the beginner's game. You graduated from it years ago. | If the beginner's game is behind you… |

**Sequence.**

1. **Rule the 35 in ch9 first.** It is the largest block, the last thing a reader
   reads, and it has five invitations already, so the register exists in the chapter
   and does not have to be invented.
2. **Then ch1 (19) and ch8 (12).** Chapter 1 sets the contract for the whole book;
   if it asserts, every later assertion is licensed by it.
3. **The zero-invitation chapters get one invitation before any assertion is
   converted.** A chapter with no invitational register anywhere reads as instruction;
   converting sentences inside it without establishing the register produces a chapter
   that hedges instead of one that invites.
4. **Re-run `assumed.py` after each chapter.** The target is the ratio, not the raw
   count. A chapter is not fixed by deleting assertions.

**Gate condition for print.** No chapter ships with zero invitations. That is a
condition a person can check and an instrument can enforce, unlike "fewer
assertions".

### What this document should not pretend

The instrument cannot tell an earned assertion from an unearned one. A reader who
has been taught the thing by page 200 genuinely has done it before, and saying so is
correct. Every site is a candidate and needs Wendell. What the instrument removes is
the possibility of the defect being invisible, which is what it has been.


---

*Created 2026-07-29. Instruments: `gate.py` (extended to the appendices surface
this session), `build_book.py` (new), `review.py`, `compile.py --verify`.*
