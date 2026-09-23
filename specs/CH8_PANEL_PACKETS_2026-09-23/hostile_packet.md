# Hostile review packet — Chapter 8 reinclusion recommendations

**Bias, stated:** the recommendations under review were written by the reviewer ninety minutes ago.
Every claim below that could be run has been run. The ones that broke are marked BROKE.

## The situation in one paragraph
*Mastering the Game of Allyship* (Wendell Britt). Chapter 8, The Sage. A web session rewrote sections 4–6
around an "altitude" idea; Wendell calls that rewrite's developmental changes successful. The rewrite cut the
chapter from 15,143 to 9,670 words. Wendell asked: identify what was cut that makes the chapter not fit the
rest of the book, and reinclude it in a way that keeps the chapter aligned with the book AND with the
developmental changes that made the rewrite work. The recommendations are in
`/Users/wendellbritt/The Library/mtgoa-manuscript/specs/CH8_REINCLUSION_BRIEF_2026-09-23.md` (read it first).
Companion counts: `.../specs/CH8_CUT_VS_REWRITE_2026-09-23.md`.

## Files (read what you need; do not edit anything)
Scratchpad `/private/tmp/claude-501/-Users-wendellbritt-The-Library-/2d7b107f-03df-4ed1-adb9-8e5b5c34869b/scratchpad/`:
- `ch8_cut.md` = the pre-rewrite chapter (15,143 w). Lines 1–306 identical in both. Cut sections 4–6 = lines 307–828.
- `ch8_rewrite.md` = the rewrite (9,670 w), sections 4–6 = lines 307–507.
- `b_ch3.md … b_ch9.md` = current Chapters 3–9 (sibling chapters). `b_ch7.md` is the closest sibling.
- Other book files via `git -C "/Users/wendellbritt/The Library/mtgoa-manuscript" show origin/claude/allyship-book-download-xh85rs:<path>`:
  `appendices/APPENDIX_I_SUPERPOWERS.md`, `appendices/ON_THE_SHOULDERS_OF.md`, `back_matter/index.md`,
  `specs/SPEC_DOMAIN_SECTIONS_2026-08-03.md`, `specs/PROPOSAL_CUTS_2026-08-09.md`,
  `specs/CUTS_ARCHIVE_2026-08-09.md`, `editorial_reports/2026-07-31/CH8.md`, `MTGOA_BOOK_WORK_TRACKER.md`.
- App: `/Users/wendellbritt/bars-engine/src/lib/technique-library/superpowers/` (read-only; never run anything there).
- Reader persona: `editorial.yaml` (`reader:` block) in the mtgoa-manuscript working tree.

## The recommendations under attack (vote on each: UPHOLD / AMEND / REVERSE / ABSTAIN)
**Diagnosis**
- **D1.** The rewrite's working change is replacing a five-modes taxonomy with ONE lived situation (the hiring-meeting scene) and one
  question; the cut Section 4 taught vocabulary, the very distortion ch8:197 names.
- **D2.** "Fits the book" is defined by the Ch3–Ch7 template: a Section 5 daemon chapter, a Section 6 with five Moves + domain section +
  Tell + "Where the daemon bites" + "From Read to Quest," and Section 4 apparatus (Draw the Axis, EA alignment, Ecology, 3-2-1).
- **D3.** Tier-1 dependencies (something outside Ch8 breaks): Ch9:76/161/441/615, Appendix I (Escape Artist + Coach), back_matter/index,
  ON_THE_SHOULDERS/copyright attributions, Wendell's 2026-08-03 domain-section ruling, "the card grid."
- **D4.** The hiring-meeting scene already performs the five Moves (brief §4 table): noticing = Name the Game; V3 speaking the table's
  language = Switch; "beside, not above" = Return; V2 leaving from ground or wound = Put a Game Down / Escape Artist; V3 serving = Coach;
  the team correcting the Sage = Hold the Meta / Move 1's test.
- **D5.** Two five-item sets (Modes in S4, Moves in S6) is book convention (ch9:454), so retire the July flag ST-3.

**Plan**
- **P1.** Restore Section 5 whole (875 + 667 w incl. marginalia Irix + Corin, 3-2-1 on the Damaged Self, mechanism, Take Out).
- **P2 (R1).** Restore the five Moves (2,202 w), each opened by a line locating its beat in the scene, vignettes kept (Ellis, Sam, Kit, nine
  years, Ade), "Working vs performed" kept, the five per-mode distortion paragraphs (467 w) retired.
- **P3 (R2).** EA alchemy block (1,030 w): brief §7 says restore whole re-keyed to the Moves; brief §8 and the chat summary recommend the
  compressed path (~450 w). **BROKE — the brief contradicts itself.** Also: the 2026-08-09 length-cuts pass listed "the EA table and every
  alchemy move" as untouched.
- **P4 (R3).** Retire the Walk Back (703 w) and keep only the Egan passage (95 w). The same Aug-9 list also protected "the four Walk Back
  moves, in count and in order" and called the Walk Back "the section she stays for."
- **P5 (R4).** Restore both 3-2-1s and the BAR prompts verbatim; write no new prose.
- **P6 (R5 + E1).** Retire "the forest" as the Sage's image; reword five rewrite lines (ch8:359, 365, 367, 371, 397: "does not belong at the
  table," "invisible to them," "cannot explain it to them") so they agree with Section 3's close (ch8:297) and ch9:575 ("Sage a seat you take
  and leave"). Alternative not weighed in the brief: keep the rewrite's stance and change Section 3's close and ch9:575 instead.
- **P7.** Merge the rewrite's Section 6 (Tell, What Winning Looks Like, Stand in Your Own Ground, Building the Capacity, What You Carry Forward;
  ~1,870 w) into the restored structure; net roughly +400 w survives.
- **P8.** Restore the domain section (1,108 w) with four markers, merged with the rewrite's Tell/Winning.
- **P9.** Relocate the Sources note (169 w) into scattered in-text credits (Big Mind, Laloux, Egan, Chou).
- **P10.** Target length ≈14,300 w (the compressed path); the full-restoration path ≈15,700. Wendell said on 2026-08-09 the book "is coming in a
  bit long." Siblings: Ch3 15,724 · Ch4 12,592 · Ch5 12,228 · Ch6 13,466 · Ch7 15,057.
- **P11.** Leave canon items in Sections 1–3 to Wendell (Vulnerable Child at ch8:251 and ch9:441; daemon roster omitting the Emotional Body).

## Measured before anybody argues
| claim in the brief | measured | holds? |
|---|---|---|
| Ch3–7 each have a Section 5 daemon chapter; Ch8 rewrite has no Section 5 marker | headings + `<!-- SECTION n -->` markers: ch3–7 have S5 (Controller, Skeptic, Fixer/Healer, Emotional Body, Victim); rewrite has S1,2,3,4,6,7 | **yes** |
| siblings' "What You Take Out of the Forest" name the superpower Appendix I lists | ch7's Take Out names "the Connector's foundation"; superpower names occur in ch3–ch7 | **yes** |
| every sibling has From Read to Quest; Ch9:161 needs a Sage quest | ch3–7: 1 each; rewrite: 0; cut: 1 | **yes** |
| the rewrite has "no EA vocabulary at all (0 vs 15)" | rewrite region: no channel names, no alchemy; the word "angry" appears twice | **half** — overstated |
| "five BAR captures" cut → 0 | `grep -w BAR`: cut 4, rewrite 0 | **BROKE** (4, not 5; the earlier note said 5) |
| brief keeps the rewrite scene as-is | "the Safe Self" (rewrite ch8:347, 369, 373) appears in NO other chapter, ch1–ch9, and is defined nowhere; the book's daemons are Protector, Controller, Skeptic, Fixer/Healer, Emotional Body, Victim, Damaged Self | **BROKE** — an undefined capitalized term the brief never flagged |
| the rewrite is body-anchored like its siblings | body/breath/chest/feet/embodied/somatic: rewrite 0.55 per 1,000 w (2 hits), cut region 1.43 per 1,000 w (13) | **thinner**; the brief never flagged it |
| the app depends on the Sage Moves / card grid | bars-engine has no "Name the Game" / "Switch Games"; the July "twenty cards" section is gone from ch3–5 and ch8 and `APPENDIX_H_THE_DECK` is retired | **unverified / probably false** — the brief's "card grid" dependency has no evidence |
| the app depends on Escape Artist | `superpowers/overrides/escape-artist.ts`, `profiles.ts`, `types.ts`. The app's Escape Artist is authored separately: inner = "honoring your OWN wisdom of fear (staying for the ask, sorting wise retreat from flight)", outer = "helping others find a dignified exit," shadow = "Perpetual Vanisher (leaving… before it's time)". Appendix I's version: "quits a game whole: puts down a fight, a role, an identity." | **two definitions exist**; the brief cites only Appendix I |
| length arithmetic | full ≈15,700 and compressed ≈14,300 recompute from the components; the "+400 net from the rewrite's Section 6" line quietly absorbs ~1,470 w of the rewrite | **holds, with a hidden assumption** |
| the August "protected" list was Wendell's ruling | `PROPOSAL_CUTS_2026-08-09.md` title: "the length cuts, ruled by the six Faces"; Wendell's own line that day: "The book is coming in a bit long so if there's anything that can be cut…" | **partly** — Faces ruled, at Wendell's request for cuts |
| ST-3 (two five-item sets) is convention | ch4–7 all carry Modes + Moves; ch9:454 states it | **yes** |

## The cast (recorded; one cast per decision; seed 20260923)
Question: "Should Chapter 8 keep the altitude rewrite as its spine and bring the cut Section 5, the five Moves, the domain section, the exercises and Emotional Alchemy back around it, or is another shape right?"
- Primary **Hexagram 53 Steadfast** (Wind over Mountain). Tone: Patience, Growth. "Do not seek overnight success or instant gratification… Building a strong foundation is more important than endeavoring for high branches. Do not try to change your nature; instead, embrace your nature. Play to your own strengths."
- Changing line: **4** (old yin), in the upper trigram = what the decision *shows*, so the pressure is in execution and the foundation is sound.
- Relating **Hexagram 33 Withdraw** (Heaven over Mountain). Tone: Strategic Retreat. "Retreat does not mean surrender… a strategic withdrawal… self-reflection… personal growth."
- Value turn: Patience, Growth → Strategic Retreat.
- Lower trigram ☶ **Mountain** (The Still Point: "Clarity lives in what you refuse"): what the decision stands on.
- Upper trigram ☴ **Wind** (The Subtle Influence: "The strongest change is the one nobody noticed"): what it presents as.

## Your mandate
You are one of the six Faces. Read your Face's question below. Rules of the pass:
1. Express BOTH trigrams (Mountain and Wind) in your Face's register in two or three sentences, as they bear on THIS decision.
2. Answer your Face's one question about the recommendations, from evidence you pulled from the files. Cite file:line. Do not assert.
3. Be hostile. Find what breaks. A review that only agrees is one voice in a costume. If you have nothing new, say "no new note" for that item.
4. Vote on each D/P item: UPHOLD / AMEND (say exactly how) / REVERSE / ABSTAIN, one line each with the evidence.
5. Give one finding nobody else on the panel is likely to find.
6. Do not rank sentences; do not say any sentence is the best; do not write replacement prose. Do not edit or create any files.
7. Return at most 700 words. Plain prose and short lists. No "not X, but Y" constructions; say the half that carries the meaning.
