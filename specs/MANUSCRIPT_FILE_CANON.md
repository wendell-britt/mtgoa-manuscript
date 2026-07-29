# MANUSCRIPT FILE CANON — read this before editing any chapter

**Last synced: 2026-07-28. Book ships 2026-08-01.**

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
| 9 | `manuscript/ch9.md` | The Player |

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

Since 2026-07-28 that counts the marginalia too, and reports **102,875**. Strip
first for the body-text figure:

```
python3 marginalia/compile.py --strip     # -> 97,738 body text
python3 marginalia/compile.py --apply     # put the frame back
```

**97,738** is the body text and the figure in `MANIFEST.md`. The frame adds
**5,137**. Note that `wc -w` reports 96,260 for the same body text — it splits
differently around em dashes and markdown punctuation. Both are correct; they
answer different questions. Quote the whitespace-split figure, because that is
what the manifest and every planning doc use.

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
- `drafts/` — working prose not merged into any chapter. `appendix_channels.md` and `ch9_transfer_drill.md` are finished pieces; `ch3_rebuild.md`, `ch4_section5_rebuild.md`, `newsec5.md`, and `CH2_LINE_LEDGER.md` are partial.
- `chapters/ch0-infinite-arcade/` — kept out of the 2026-07-28 retirement because the Chapter 0 → Chapter 1 rewrite dropped material rather than revising it. `MONOPOLY_ORIGIN_STORY.md`, `BRIDGE_1_DRAFT.md`, and the `GM_SECTION` drafts are the only surviving copies of that prose; none of it is in the current manuscript.

## Docs that are stale and will mislead you

These describe the book as it was, not as it is. Do not plan from them without checking the claim against the chapter files above.

- `EDITING_PLAN.md` — its ICA Journey Map uses obsolete 8-chapter numbering, off by one against the current nine.
- `CHAPTER_TEMPLATE_GUIDE.md`, `claude/DAEMON_CANON.md`, `claude/ArgumentMap.md`, `claude/MTGOA_OUTLINE.md`, `DAEMON_ARCHITECT_CONSISTENCY_CHECK_2026-07-15.md` — carry the retired 8-gate walk, the retired four-stage sequences, and the retired "jeppi" naming.
- `claude/MTGOA_CROSS_BOOK_SYNTHESIS_CH3_9.md`, `CHAPTER_COMPLETION_AUDIT.md`, `claude/CH8_PRINT_READINESS_PLAN.md`, `claude/SPEC_PRINT_SPRINT_2026-07-26.md` — superseded by later work.
- `SPEC_BOOK_TOOL_PLACEMENT.md` — its appendix lettering is desynced from current appendix naming.
- The source-analysis stubs credit "Bob Elliott" for *Existential Kink*. The author is **Carolyn Elliott, PhD**.

## Structural facts that are current

The gate walk is removed from Chapters 4 through 8. Chapters 2 and 9 keep theirs. Chapter 2's daemon roster carries seven, not eight — the Vulnerable Child left with the gate walk.

Every stage sequence is five beats. There are no four-stage models left in the book.

The Reflection Prompts convention is retired. It appears in zero chapters as of 2026-07-28.

Chapter 2's sections renumber 1 through 10. The old Section 9 (Reflection Prompts) was cut and Sections 10 and 11 moved up.

## Still missing from the book

Neither appendix exists as prose anywhere — not in the project, not on any disk. Both are hard print blockers.

- **Appendix — The Polarity Map** (~1,500 words). Closes open references at `ch3:623`, `ch4:148`, `ch5:188`, `ch6:151`, `ch7:121`.
- **Appendix — The 3-2-1 Shadow Process** (~1,500 words). Closes `ch3:456`, `ch3:593`, `ch4:374`. Carries the book's only Wilber credit.

Front matter, table of contents, and back matter are also unwritten.

## Standing editorial rules

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
