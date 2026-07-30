# MANUSCRIPT FILE CANON — read this before editing any chapter

**Last synced: 2026-07-29. Book ships 2026-08-01.**

## Where the book actually is

The nine chapter files below are the manuscript. Edit these, and write edits back to the same path.

| Ch | File | Title |
|---|---|---|
| 1 | `manuscript/ch1.md` | The Infinite Arcade |
| 2 | `manuscript/ch2.md` | The Forest |
| 3 | `manuscript/ch3.md` | The Shaman |
| 4 | `manuscript/ch4.md` | The Challenger |
| 5 | `manuscript/ch5.md` | The Regent |
| 6 | `manuscript/ch6.md` | The Architect |
| 7 | `manuscript/ch7.md` | The Diplomat |
| 8 | `manuscript/ch8.md` | The Sage |
| 9 | `manuscript/ch9.md` | Creating Your Own Allyship Game |

**Canon moved to git on 2026-07-28.** This repository is now the durable store,
and these nine files are the book. The Claude project docs that used to hold
canon (`claude/CHAPTER*.md`) and the Obsidian vault are upstream history — do
not sync a chapter back to them and do not treat them as authoritative.

Commit chapter edits. A chapter edited in a session container and never
committed is a chapter that was not edited.

Word counts are deliberately not repeated here. Earlier copies of this table
drifted from the files. Measure instead — and use one measure consistently:

```
python3 -c "import glob;print(sum(len(open(f).read().split()) for f in glob.glob('manuscript/ch*.md')))"
```

As of 2026-07-29 that counts the marginalia too, and reports **103,464**. Strip
first for the body-text figure:

```
python3 marginalia/compile.py --strip     # -> 98,332 body text
python3 marginalia/compile.py --apply     # put the frame back
```

**98,332** is the body text and the figure in `MANIFEST.md`. The frame adds
**5,132** across 53 blocks. Note that `wc -w` splits differently around em dashes
and markdown punctuation and will disagree; both are correct and answer different
questions. Quote the whitespace-split figure, because that is what the manifest
uses.

These figures move with every editing session. Re-run the command rather than
quoting this paragraph — an earlier copy of it drifted and misled a session.

## The marginalia frame

As of 2026-07-28 the chapters carry the Calrunia frame: each is a document by a
named character, annotated in the margin by somebody else. It lives inside the
canonical files, wrapped in HTML comments, in `manuscript/ch2.md` – `ch9.md`.
Chapter 1 carries none.

Do not hand-edit a marginalia block in a chapter file. Edit `marginalia/insertions.py`,
then `python3 marginalia/compile.py --strip && python3 marginalia/compile.py --apply`.
Strip before measuring — an instrument run over a chapter with marginalia in it is
counting two voices at once.

```
python3 marginalia/compile.py --strip    # before running instruments
python3 marginalia/compile.py --apply    # put it back
```

See `marginalia/README.md` and `marginalia/HANDOFF.md`.

## The rest of the durable set

- `instruments/` — the measurement tools, now committed as runnable files rather than pasted from a toolkit doc. `spec_edit.py` is the safe-edit pattern every manuscript edit goes through; it aborts and writes nothing on a missed or duplicated anchor. `dupes.py` is the cross-chapter duplicate scanner. Also: practice surfaces, chain check, stylometry, term debt, negation stacks, repetition sweep, construction sites. Run them against `manuscript/ch1.md`–`ch9.md`. Every claim about this manuscript should come from one of these, not from a planning document.
- `instruments/build_book.py` — assembles the print deliverable from canon, generates the contents, and exits non-zero while a required component is missing. Added 2026-07-29; nothing built a whole book before it. `compiled/` is a stale 2026-05-29 artifact whose builder reads the retired `chapters/` tree.
- `instruments/gate.py` reads **four** printed surfaces as of 2026-07-29 — body, marginalia, appendices, and front/back matter. Before that it read only `manuscript/`, so roughly 10,000 words of shipping prose had never been held to the standing list.
- `specs/MTGOA_INSTRUMENTS_TOOLKIT.md` — documents the reviewer gate and what each instrument measures.
- `visuals/` — the built HTML visuals, self-contained with no external assets: `chapter_engine`, `ch2_seven_daemons`, `ch3_process_shape`, `structural_delivery`, `register_remediation`, `structure_comparison`, `voice_comparison`.
- The open specs: `specs/SPEC_FINISHING_PASS_2026-07-29.md` — **the active work
  plan for the August 1 delivery** — plus `specs/SPEC_STRUCTURAL_DELIVERY.md`,
  `specs/SPEC_REGISTER_REMEDIATION.md`, `specs/SPEC_REPETITION_AND_CUTS.md`.
  Each ends in a rulings section that is still awaiting Wendell.
- `marginalia/review.py` — the candidate-finding voice linter (AI shapes,
  say-the-noun, hedge density, per-Head genre markers). Findings are
  adjudicated, never auto-fixed. It complements `instruments/gate.py`; it does
  not replace it. Voice doctrine in `marginalia/specs/SEVEN_VOICES.md`.
- `drafts/` — working prose. `ch3_rebuild.md`, `ch4_section5_rebuild.md`, `newsec5.md`, and `CH2_LINE_LEDGER.md` are partial and unmerged. Two files here are **already in the book** and the directory name misleads: `ch9_transfer_drill.md` is `ch9`'s *The Last Rep* (50 of its 52 sentences appear verbatim in canon), and `appendix_channels.md` left on 2026-07-29 to become `appendices/APPENDIX_C_FIVE_CHANNELS.md`. Check canon before treating anything in `drafts/` as unbuilt.
- `chapters/ch0-infinite-arcade/` — kept out of the 2026-07-28 retirement because the Chapter 0 → Chapter 1 rewrite dropped material rather than revising it. `MONOPOLY_ORIGIN_STORY.md`, `BRIDGE_1_DRAFT.md`, and the `GM_SECTION` drafts are the only surviving copies of that prose; none of it is in the current manuscript.

## Docs that are stale and will mislead you

These describe the book as it was, not as it is. Do not plan from them without checking the claim against the chapter files above.

- `EDITING_PLAN.md` — its ICA Journey Map uses obsolete 8-chapter numbering, off by one against the current nine.
- `CHAPTER_TEMPLATE_GUIDE.md`, `claude/DAEMON_CANON.md`, `claude/ArgumentMap.md`, `claude/MTGOA_OUTLINE.md`, `DAEMON_ARCHITECT_CONSISTENCY_CHECK_2026-07-15.md` — carry the retired 8-gate walk, the retired four-stage sequences, and the retired "jeppi" naming.
- `claude/MTGOA_CROSS_BOOK_SYNTHESIS_CH3_9.md`, `CHAPTER_COMPLETION_AUDIT.md`, `claude/CH8_PRINT_READINESS_PLAN.md`, `claude/SPEC_PRINT_SPRINT_2026-07-26.md` — superseded by later work.
- `SPEC_BOOK_TOOL_PLACEMENT.md` — its appendix lettering is desynced from current appendix naming, and more so since letter C changed hands on 2026-07-29.
- `specs/SPEC_STRUCTURAL_DELIVERY.md` — a persuasive audit whose headline finding is false. It says the book has no transfer test; `ch9`'s *The Last Rep* is one. It was measured against a snapshot 3,200 words smaller than canon. It now carries a correction header listing which of its findings survive; read that before acting on any of it.
- Anything calling Chapter 9 "The Player." Canon's heading is `CHAPTER 9: CREATING YOUR OWN ALLYSHIP GAME`. Chapters 3–8 are named for their Face and ch9 for its action, which under the ICA rule is the better heading — so the docs were corrected to match canon rather than the reverse.
- The source-analysis stubs credit "Bob Elliott" for *Existential Kink*. The author is **Carolyn Elliott, PhD**.

## Structural facts that are current

The gate walk is removed from Chapters 4 through 8. Chapters 2 and 9 keep theirs. Chapter 2's daemon roster carries seven, not eight — the Vulnerable Child left with the gate walk.

Every stage sequence is five beats. There are no four-stage models left in the book.

The Reflection Prompts convention is retired. It appears in zero chapters as of 2026-07-28.

Chapter 2's sections renumber 1 through 10. The old Section 9 (Reflection Prompts) was cut and Sections 10 and 11 moved up.

## The move-section conventions — S6 ruled 2026-07-30

**The `**Example:**` label is optional.** Three conventions exist across the seven
move chapters, each doing the same job differently, and standardising them would
flatten a real difference:

| ch | words/move | `Example:` | scripted line | working-vs-performed |
|---|---|---|---|---|
| 3 | 621 | ✓ | ✗ | ✗ |
| 4 | 210 | ✗ | ✓ | ✗ |
| 5 | **119** | ✗ | ✗ | ✗ |
| 6 | 250 | ✓ | ✗ | ✗ |
| 7 | 450 | ✗ | ✓ | **✓** |
| 8 | 301 | ✗ | ✓ | ✗ |
| 9 | 399 | ✓ | ✓ | ✗ |

What the reader needs is a concrete instance she can act on, and every chapter
supplies one — as a labelled Example in ch3/ch6/ch9, as a scripted line in
ch4/ch7/ch8, as both in ch9. **The label is a navigation aid, not the substance.**
Stop flagging its absence.

**Two things this measurement overturned.** `SPEC_STRUCTURAL_DELIVERY.md` S6 says
the label is used by "Chapters 3, 4, 5, 6, and 9" — it is in ch3, ch6, ch9 only.
And its Break 3 says the Diplomat is the chapter *without* a perform layer: ch7 is
the only chapter that **has** one, an explicit `**Working vs. performed:**` block on
four of five moves, which no other chapter carries.

**The real gap is ch5, and it is not about labels.** At 119 words per move it is
half the next thinnest and a fifth of ch3. More to the point, its moves are all
internal — *make a list, identify, ask yourself* — so the Regent is the one Face
that never hands the reader a sentence to say out loud. Move 3 is the sole
exception. Open as a ruling; drafts exist in the session record.

## Still missing from the book

**Corrected 2026-07-29. The previous version of this section was wrong**, and it
cost a session. It said neither appendix existed "not in the project, not on any
disk." Both were committed in `appendices/` and had already been through a
lettering pass. The full A–G set is written, revised against current canon, and
gate-clean at 10,538 words.

What is actually still open:

- **Ten front-matter facts.** Half title, title page, copyright, and
  about-the-author are drafted in `front_matter/` and `back_matter/`; every fact
  that could not be sourced is a `⟦TOKEN⟧`, and `gate.py` fails on all of them.
- **The table of contents is generated**, not authored —
  `instruments/build_book.py --toc`.
- **Optional and unwritten:** dedication, author's note, acknowledgements,
  enrollment page. The enrollment page waits on R1.

Appendix cross-references in canon all resolve and all name a letter as of
2026-07-29. Line numbers quoted in older planning docs are stale by roughly 40
lines, because they were taken with the frame stripped.

## Standing editorial rules

### The decision rule — does this help the ICA move forward?

**Ruled 2026-07-29, and it governs every other rule on this page.** Every
editorial decision is made against one question: *does this help the ICA keep
moving?* Not whether it is consistent, not whether it is clever, not whether it
satisfies a linter. Whether the reader this book was written for gets further
because of it.

The rule exists because consistency is the cheaper thing to optimize and it
reads like rigor. Chapter 1's subtitle is the worked example: three candidates
were offered, two of them accurate descriptions of the chapter — the confession
of a late book — and the chosen one names the reader's problem instead.
*The Game You Didn't Know You Were Playing* does not describe Chapter 1. It
tells the ICA why she should keep reading.

Applied to the open questions on this page: a formatting inconsistency the
reader never sees is not worth a canon edit; a cross-reference pointing at the
wrong chapter is, because it stops her. When a rule and the ICA disagree, the
ICA wins and the exception gets recorded here.

### Voice and shape

Banned words: *room*, *quiet*, *quietly*, *genuinely*. (*Genuine* is not banned.) No sentence opens with *And* or *But*. The "Not X. Not Y." negation stack is banned. "Make room" becomes "make space." Never narrate the reader's unnamed history back to her as fact.

### The three grammar moves — run `instruments/prose_diet.py` on new prose

Named 2026-07-29. These are the structures a generated draft reaches for when it
wants to sound like a finished sentence without committing to one. They are
nearly invisible line by line and obvious in aggregate, which is the only reason
they were caught: the W7 rewrites put ~1,300 words of new prose side by side.

**Measured, against the book's own baseline:**

| | book | the W7 rewrites | |
|---|---|---|---|
| be-verbs /1k | 50.3 | 84.9 | **+69%** |
| copula as main verb | 29.1% | 53.8% | **+85%** |
| *it* /1k | 30.0 | 41.3 | **+38%** |
| article + nominalization /1k | 16.5 | 28.3 | **+71%** |

The finding stands. Generated replacement prose leans on all three markedly
harder than the prose it was inserted into, and it does so *while passing every
other gate in this repo*.

**1 · "is" — unless you are defining a term.** A be-verb is where the action went
missing. Lanham's Paramedic Method: box every be-verb, circle the prepositions,
then ask *who is kicking whom* and put the doer in the subject. Williams: the
subject should name a character and the verb should name what that character
does. Defining a new term is the licensed case — *"Force means spending yourself
on a crossing"* — and this book defines a great many terms, so the copula is not
banned. It is rationed.

**2 · "it" — only where you can point at the noun.** Sword's rule is literal:
use *it* and *this* only when you can state exactly which noun each refers to.
The standard editorial drill is to circle every *it / this / that / which* and
draw an arrow to its antecedent; anything with no arrow gets rewritten. Watch
especially for **broad reference**, where *it* stands in for a whole preceding
clause. That is the shape that reads fluently and means nothing, and it is the
one to cut first. *It is / There is* openers are the worst case — a subject
slot filled by a placeholder.

**3 · Articles fronting nominalizations.** Sword calls these zombie nouns:
verbs turned into nouns, which then need a be-verb to prop them up and an
article to introduce them. *The maintenance of*, *a recognition that*. The
article is the tell, which is what makes them findable. Turn the noun back into
a verb and the be-verb usually disappears with it — the three moves are one
problem.

Williams licenses nominalization when it refers back to a previous sentence,
replaces an awkward *the fact that*, names what would be the object of a verb,
or names a concept already familiar to the reader. So this is a candidate
finder, never a gate. **`the thing` appears 132 times in this manuscript** and
is the same defect `review.py` reports as say-the-noun.

Sources: Richard Lanham, *Revising Prose*; Joseph M. Williams, *Style: Lessons
in Clarity and Grace*; Helen Sword, *The Writer's Diet* and "Zombie Nouns"
(NYT, 2012).

### Fixing a denying negation — the four moves, in one pass

Established 2026-07-29 by doing it wrong three times in a row. A denying
negation is never fixed by deletion alone. Run all four before showing anything:

1. **Cut.** Remove the negated clause, keep the positive. Correct against the
   rule and insufficient on its own — *"That is not anger. That is will."*
   becomes *"That is will,"* which floats with nothing to push against. The
   negation was carrying a beat and a distinction; both leave with it.
2. **Essence.** Name what the negation was protecting the term against. Every
   one of them is guarding against a specific caricature — sentiment for care,
   aggression for force, cowardice for restraint. Say that thing.
3. **Synthesize.** Collapse it into **one sentence holding the axis**, not two
   staging it. *"Aggression spends someone else. Force spends you"* is still an
   opposition in positive clothing; the reader hears the negation the syntax is
   avoiding. Chapter 3 already rules on this: *two legitimate poles, your
   position on the axis, one action containing both.* Most of these sites sit
   on a named pair — Feeling ↔ Function, Force ↔ Restraint, Care ↔ Impact,
   honor ↔ reform — so hold the axis.
4. **Voice.** Shape the result to whoever is speaking. Twelve synthesis
   sentences in a row produced their own formula: nine opened *[NOUN] is
   [NOUN-phrase]*, and the two polarity pairs got near-identical syntax in the
   same chapter. Give it the Head's genre from `marginalia/specs/SEVEN_VOICES.md`
   — Ash takes an imperative and a cost, Quill a periodic clause citing prior
   keepers, Vale *in practice* and a tolerance, Cross both protections named,
   Orr a courteous disagreement with another school.

**Move 4 pays for itself.** Voicing these lines cleared ch8's genre-absent BLOCK
and supplied markers `--mode voice` had been demanding, so the negation fix and
the W3 genre pass are the same edit. Do not run them as separate passes.

**Run `/no-ai-slop` on the result, not a regex approximation of it.** Its
robotic-rhythm and fake-profound-kicker rules catch what the linters cannot:
repeated sentence shapes, and a clarifier that has turned into an appended
aphorism. Both appeared in this work and neither is detectable by pattern.

Do not attribute generated prose to Wendell as his established voice. Do not invent a frame and present it as a finding. When a voice rule is violated, write around it — do not argue for an exemption and do not build a taxonomy of acceptable variants.

**The gate applies to the marginalia as well as the body text** (ruled 2026-07-29).
The margin is a different register in another character's voice, and it is held to
the same list. Run it as an instrument, which scores the two surfaces separately so
you can see which one regressed:

```
python3 instruments/gate.py        # both surfaces
python3 instruments/gate.py -v     # quote every hit with context
```

Note the flags when reading the gate below: `andbut` and `stacks` are
case-sensitive. Running them case-insensitively invents violations that are not
there — lowercase *and*/*but* mid-sentence and a lowercase *not* opening a pair
are all legal.

Run this gate on any new prose before it goes in front of Wendell. Every counter must read 0.

```python
print('andbut',len(re.findall(r'(^|[.?!]["""\'’]? |\*|\*\*|— |; )(And|But) ',t,re.M)),
      'banned',len(re.findall(r'\broom\b|\bquiet(ly)?\b|\bgenuinely\b',t,re.I)),
      'emdash',len(re.findall(r'[a-zA-Z0-9,]—[a-zA-Z0-9]',t)),
      'A0',len(re.findall(r'you (were|was) (taught|told|raised|trained)|somewhere along the way|the village taught you',t,re.I)),
      'stacks',len(re.findall(r'\bNot [^.!?]{1,60}[.!?]\s+(Not|Never|No)\b',t)))
```

Also check new prose for duplicate sentences against all nine chapters before inserting it. Sentences have been accidentally duplicated across five chapters before. The scanner is `instruments/dupes.py`.
