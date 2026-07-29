# SPEC — Print readiness, measured

## STATUS — end of session, 2026-07-29

**Everything in §2 is done except the parts only Wendell can do.** The sections
below are kept as the record of what was found and why; this block is the current
state.

| Blocker | State |
|---|---|
| B1 — gate fails | **13 hits, all Wendell's.** `⟦ASH-AGE⟧` / `⟦ASH-SPAN⟧` in ch4 (R9), ch3's A0 (R8), ten front-matter facts. |
| B2 — appendices never gated | **Closed.** 27 hits on first run, now 0 across every counter. |
| B3 — front and back matter | **Drafted.** Half title, title page, copyright, about-the-author. Every unsourced fact is a `⟦TOKEN⟧` the gate fails on. |
| B4 — nothing built a book | **Closed.** `instruments/build_book.py --write` emits 114,691 words. Spine complete. |
| §3 — appendices describe the retired book | **Closed.** C retired, A/B/F/G revised, D/E gated. |
| §4 — Five Channels unlettered | **Closed.** Took letter C. |
| §5 — reference style | **Closed.** All eight sites name letter and title. |
| §6 — four heading styles | **Closed.** All nine read `CHAPTER N: THE NAME`; ch1 gained the subtitle every other chapter had. |
| §7 — editorial BLOCK 80 | **16.** W7 complete, say-the-noun done, `which is` swept 91 → 64. |

**What is left, in order:**

1. The ten front-matter facts, `⟦ASH-AGE⟧` / `⟦ASH-SPAN⟧`, and R8. Wendell only —
   the gate cannot go green without them.
2. **R13–R18**, opened while doing the work and listed in
   `SPEC_FINISHING_PASS_2026-07-29.md`. R16 matters most: ch6:434 had a broken
   sentence and my repair infers intent.
3. W3, the genre-marker pass, untouched and waiting on R3.
4. ch4's hedge particles — the last voice BLOCK.
5. 167 punchline-last INFO hits. Pattern data, not defects.

**Withdrawn as a defect:** `rather than`, 103 uses. Exactly one sentence carries
two and exactly one paragraph carries three, and that paragraph is a deliberate
teaching triad in ch3. The per-chapter rate tracks the chapters that draw the most
distinctions, which is where ranking language belongs. Recorded so nobody re-opens
it.

**Corrected in this document:** §5's line-number table was itself taken from stale
sources; the numbers moved again when the frame was reapplied. Do not quote line
numbers from any spec. Grep the file.

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

`⟦ASH-AGE⟧` and `⟦ASH-SPAN⟧` are live in ch4 Section 3. **These cannot be
resolved by anybody but Wendell** — they are two facts about Corin Ash's
biography, deferred by ruling under R9. Nothing else on this list is blocked on a
person. Everything else can proceed while they are open, and the gate stays red
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
5. **B1** — fill `⟦ASH-AGE⟧` / `⟦ASH-SPAN⟧`, rule R8. Wendell only.

## 9 · Rulings this document needs

- **R9 (live blocker)** — the two Ash biography facts. The gate cannot go green
  without them and nobody else can supply them.
- **R8** — ch3's A0 hit: license as recall-prompt, or rewrite.
- **R10 (new)** — the Five Channels appendix: give it a letter, or cut the ch3
  reference.
- **R11 (new)** — appendix reference style in canon: by letter or by title.
- **R12 (new)** — Appendix C: rewrite against current canon, or cut the glossary
  from this edition. Rewriting is ~1,100 words of definitional prose against a
  book the writer knows well; cutting is free and loses a reference surface.

**R4 closes** (§1). R1 still gates the enrollment page and half-title only.

---

*Created 2026-07-29. Instruments: `gate.py` (extended to the appendices surface
this session), `build_book.py` (new), `review.py`, `compile.py --verify`.*
