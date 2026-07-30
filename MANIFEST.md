# MTGOA export — measured 2026-07-29

Book ships 2026-08-01. Every figure below came out of an instrument on 2026-07-29
and is reproducible:

```bash
python3 instruments/build_book.py            # the spine and what is missing from it
python3 instruments/build_book.py --write    # emit build/MTGOA_PRINT_<date>.md
python3 instruments/gate.py                  # four printed surfaces
python3 marginalia/compile.py --verify       # frame round-trips byte-identical
```

**The previous version of this file was wrong in a way that cost a session.** It
reported 97,738 words and said both the Polarity Map and the 3-2-1 Shadow Process
existed "not in the project, not on any disk." Both were committed in
`appendices/`. Do not plan from a word count or a gap claim in a planning document
without running the instrument.

## The whole book

`instruments/build_book.py --write` assembles front matter, generated contents,
nine chapters with the frame applied, appendices A–G, and back matter into one
file. **114,691 words.** Nothing built a book before 2026-07-29; `compiled/` holds
a stale 2026-05-29 artifact whose builder reads the retired `chapters/` tree.

## manuscript/ — the nine chapters

**98,332 words of body text. 103,464 with the marginalia frame applied**, which is
what the files on disk contain. Strip before measuring anything else.

| File | Body | With frame |
|---|---|---|
| ch1.md — The Infinite Arcade | 7,527 | 7,527 |
| ch2.md — The Forest | 7,190 | 7,886 |
| ch3.md — The Shaman | 15,264 | 16,040 |
| ch4.md — The Challenger | 11,258 | 11,993 |
| ch5.md — The Regent | 8,966 | 9,586 |
| ch6.md — The Architect | 9,896 | 10,546 |
| ch7.md — The Diplomat | 12,736 | 13,575 |
| ch8.md — The Sage | 13,245 | 13,912 |
| ch9.md — The Player | 12,250 | 12,399 |

Chapter 1 carries no marginalia by design. The frame is **53 blocks** and adds
5,132 words; `compile.py --verify` confirms the body round-trips byte-identical.

**Chapter 9's heading is `CHAPTER 9: CREATING YOUR OWN ALLYSHIP GAME`**, not "The
Player." Chapters 3–8 are named for their Face and ch9 for its action. Under the
ICA decision rule that is the better heading, so the docs were corrected to match
canon rather than the reverse.

## appendices/ — A through G, all written

**10,538 words.** The full set exists and is gate-clean.

| Letter | File | Words |
|---|---|---|
| A | `APPENDIX_A_FOUR_ALLYSHIP_DOMAINS.md` | 3,051 |
| B | `APPENDIX_B_QUESTS_CAMPAIGNS.md` | 1,891 |
| C | `APPENDIX_C_FIVE_CHANNELS.md` | 1,198 |
| D | `APPENDIX_D_EMOTIONAL_ALCHEMY_PRACTICES.md` | 670 |
| E | `APPENDIX_E_321_SHADOW_PROCESS.md` | 1,077 |
| F | `APPENDIX_F_POLARITY_MAP.md` | 943 |
| G | `ON_THE_SHOULDERS_OF.md` | 1,708 |

**Letter C changed hands 2026-07-29.** The Key Terms glossary was retired — it
defined the pre-2026-07 book, with an eight-gate walk, 0-indexed chapter tags, and
51 references to a hexagram system not in the manuscript. `APPENDIX_C_KEY_TERMS.md`
stays on disk marked retired, as a second-edition starting point. The Five Channels
in Practice took the slot, which is where `ch3:332` was already sending the reader.

A, B, F, and G were revised against current canon in the same pass: the quest
chapter numbers in B were each one short, F contradicted canon's own statement at
`ch3:486`, and G was missing two credits the book owes.

## front_matter/ and back_matter/

Written 2026-07-29 as drafts on the working branch. Every fact that could not be
sourced is a `⟦TOKEN⟧` rather than a guess, and `gate.py` fails on any surviving
token — that counter is the only thing between a placeholder and the typesetter.

| Component | Words | State |
|---|---|---|
| `front_matter/half_title.md` | 6 | done |
| `front_matter/title_page.md` | 21 | done |
| `front_matter/copyright.md` | 336 | done — carries all source permissions |
| Table of contents | generated | `build_book.py --toc` |
| `back_matter/about_the_author.md` | 47 | done |

**All ten placeholders closed 2026-07-30**, on three facts: the book is
self-published, Wendell designed it, and no ISBN has been assigned. Those settle
the page rather than leaving it blank — the imprint and publisher-address blanks
were asking for things that do not exist, so `Published by Wendell Britt` replaces
both, and the designer credit is his. Author website is `masteringallyship.com`,
the domain ch9 already prints as the certification contact.

**No ISBN is assigned, so the ISBN lines are out of this edition rather than
blank.** An ebook needs none to ship on most platforms. They go back in when a
print run makes one necessary; nothing in the build depends on them.

Optional and unwritten: dedication, author's note, acknowledgements, enrollment
page. The enrollment page waits on R1.

## instruments/

`build_book.py` (new 2026-07-29) assembles the book and exits non-zero while a
required component is missing. `gate.py` reads **four** surfaces — body,
marginalia, appendices, and front/back matter; until 2026-07-29 it read only
`manuscript/`, so ~10,000 words of shipping prose had never been held to the
standing list. `spec_edit.py` is the safe-edit pattern. `dupes.py` finds exact
cross-chapter duplicates only — it misses near-duplicates, of which three were
found by hand this week. `prose_diet.py` measures the three grammar moves.

## Editorial state, measured

| | |
|---|---|
| Gate — body, marginalia, appendices | **0 across every counter** |
| Gate — front/back matter | **10 tokens**, all awaiting Wendell |
| `review.py --mode body` | BLOCK **16** · WARN **75** · INFO **167** |
| `review.py --mode voice` | BLOCK **1** — ch4's hedge particles |
| Denying negations | **9**, every one an adjudicated keep |
| `which is` appositive tails | **64**, down from 91 |
| `rather than` | 103 — measured and **withdrawn as a defect**, see the print-readiness spec |

## The 13 open gate hits, all of them Wendell's

- `⟦ASH-AGE⟧` and `⟦ASH-SPAN⟧` live in ch4 Section 3 (**R9**)
- ch3's A0 hit, *"a time you were told something true"* (**R8**)
- the ten front-matter facts: imprint, two ISBNs, designer, publisher address,
  website ×2, and three author-bio lines

Nothing else in the book is blocked on a person.

## specs/

`SPEC_PRINT_READINESS_2026-07-29.md` is the measured audit and the live worklist.
`MANUSCRIPT_FILE_CANON.md` carries canon, the standing rules, and the ICA decision
rule that governs them. `SPEC_FINISHING_PASS_2026-07-29.md` is the W-item plan;
its baselines predate this week's work and its status table has been updated.
