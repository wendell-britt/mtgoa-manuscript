# MTGOA export — measured 2026-07-30

Book ships 2026-08-01. Every figure below came out of an instrument against **this
branch** on 2026-07-30 and is reproducible:

```bash
python3 instruments/build_book.py            # the spine and what is missing from it
python3 instruments/build_book.py --write    # emit build/MTGOA_PRINT_<date>.md
python3 instruments/gate.py                  # four printed surfaces
python3 marginalia/compile.py --verify       # frame round-trips byte-identical
```

**This branch is `master`, plus the print apparatus, plus the self-sabotage belief
work.** It deliberately carries none of the chapter-prose work from
`claude/book-print-readiness-august-ar95mo`, which collided with master's register
fan-out across 91 hunks. See §Deferred.

`claude/self-sabotage-ally-beliefs-a9lhzu` merged with **zero conflicts**, into both
master and here. It works inside named sections — ch2 §6, ch3 §4/§5 — rather than
sweeping every chapter, which is why it merges where the other branch does not.
Localized section work merges; book-wide passes collide. That is the whole lesson of
this split.

**An earlier version of this file was wrong in a way that cost a session.** It
reported 97,738 words and said both the Polarity Map and the 3-2-1 Shadow Process
existed "not in the project, not on any disk." Both were committed in
`appendices/`. Do not plan from a word count or a gap claim in a planning document
without running the instrument.

## The whole book

`instruments/build_book.py --write` assembles front matter, generated contents,
nine chapters with the frame applied, appendices A–G, and back matter into one
file. **112,776 words.** Nothing built a book before 2026-07-29; `compiled/` holds
a stale 2026-05-29 artifact whose builder reads the retired `chapters/` tree.

## manuscript/ — the nine chapters

**96,355 words of body text. 101,487 with the marginalia frame applied**, which is
what the files on disk contain. Strip before measuring anything else.

| File | With frame |
|---|---|
| ch1.md — The Infinite Arcade | 7,470 |
| ch2.md — The Forest | 7,834 |
| ch3.md — The Shaman | 16,128 |
| ch4.md — The Challenger | 11,637 |
| ch5.md — The Regent | 9,354 |
| ch6.md — The Architect | 10,290 |
| ch7.md — The Diplomat | 12,991 |
| ch8.md — The Sage | 13,577 |
| ch9.md — Creating Your Own Allyship Game | 12,206 |

Chapter 1 carries no marginalia by design. The frame is **53 blocks**;
`compile.py --verify` confirms the body round-trips byte-identical.

## appendices/ — A through G, all written

**10,468 words**, and gated for the first time on 2026-07-30.

A `APPENDIX_A_FOUR_ALLYSHIP_DOMAINS.md` · B `APPENDIX_B_QUESTS_CAMPAIGNS.md` ·
C `APPENDIX_C_KEY_TERMS.md` · D `APPENDIX_D_EMOTIONAL_ALCHEMY_PRACTICES.md` ·
E `APPENDIX_E_321_SHADOW_PROCESS.md` · F `APPENDIX_F_POLARITY_MAP.md` ·
G `ON_THE_SHOULDERS_OF.md`

A, B, D, E, F, and G were revised against current canon: B's eight quest chapter
numbers were each one short, F contradicted canon's own statement at `ch3:486`, and
G was missing two credits the book owes (Robin Rice, Donella Meadows) and described
a gate structure the book no longer runs.

**Appendix C is an open decision.** This branch keeps master's Key Terms glossary,
which master is repairing in place — its "The Face" entry now names the current six
Faces. A parallel branch retired the glossary instead and gave letter C to The Five
Channels in Practice. Measured, the glossary still carries **1 eight-gate
definition, 3 Vulnerable Child references, 4 `[Ch0]` tags, and 11 trigram
references**, so the repair is genuine but incomplete. Ruling needed.

**`ch3:400` points at an appendix that does not exist.** It sends the reader to
*"Appendix: The Five Channels in Practice"*; the prose is written, 1,176 words, and
sits in `drafts/appendix_channels.md` with no letter. `build_book.py` reports it
under UNPLACED every run until it has one or the reference comes out.

## front_matter/ and back_matter/

New on 2026-07-30. Zero placeholders.

| Component | State |
|---|---|
| `front_matter/half_title.md` | done |
| `front_matter/title_page.md` | done |
| `front_matter/copyright.md` | done — carries every source permission the book owes |
| Table of contents | generated — `build_book.py --toc` |
| `back_matter/about_the_author.md` | done |

Self-published, self-designed, and **no ISBN assigned**, so the ISBN lines are
absent rather than blank — an ebook ships without one. They go back in when a print
run needs them; nothing in the build depends on them.

Optional and unwritten: dedication, author's note, acknowledgements, enrollment
page. The enrollment page waits on R1.

## instruments/

`build_book.py` (new) assembles the book and exits non-zero while a required
component is missing. `gate.py` reads **four** surfaces — body, marginalia,
appendices, and front/back matter; until 2026-07-30 it read only `manuscript/`, so
~10,500 words of shipping prose had never been held to the standing list. It keeps
master's tightened `banned` rule, which catches the plural *rooms*.

**The first gated run of the appendices found a violation in master's own new
prose**: the repaired "The Face" entry in Appendix C read *"who they are in the
room."* That is what the extension is for.

## Editorial state, measured on this branch

| | |
|---|---|
| Gate — all four surfaces | **2 hits**, both `⟦ASH-AGE⟧` / `⟦ASH-SPAN⟧` in ch4 (**R9**) |
| `review.py --mode body` | BLOCK **28** · WARN **43** · INFO **159** |
| `review.py --mode voice` | BLOCK **1** — ch4's hedge particles |
| Denying negations | **2** |
| `which is` appositive tails | **9** |
| say-the-noun | **25** |
| Abstraction nouns in subject slots | **25** |

**R9 is the only thing between this branch and a green gate.** Two facts about
Corin Ash's biography, in ch4 Section 3, that nobody but Wendell can supply. R8 is
already ruled on master and the A0 counter reads 0.

## Deferred — the prose branch

`claude/book-print-readiness-august-ar95mo` holds 26 commits of chapter work that
conflicts with master across **91 hunks in nine chapters**. Measured against this
branch, most of it is superseded and some of it is not:

| | this branch | the prose branch |
|---|---|---|
| Denying negations | **2** | 9 |
| `which is` tails | **9** | 64 |
| say-the-noun | 25 | **6** |
| Body words | **96,355** | 98,383 |

Master's register fan-out went further on two of the three, so **the W7 and
`which is` work on that branch is superseded and should be dropped rather than
merged.** Its say-the-noun pass is the one prose item still worth re-applying, plus
ch5's three spoken lines and one heading-style question. Two items travelled with
this branch because they had to: ch4's *"kindness-deceiving-as-cruelty"*, which was
backwards, and ch1's subtitle.
