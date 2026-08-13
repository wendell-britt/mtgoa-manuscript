# Deep read — the brief every reader works from

**The final proof of *Mastering the Game of Allyship*.** Nine chapters, one reader each,
**every chapter read against all eight others.** Wendell, 2026-08-11: *"Make sure our deep
read of each chapter includes reading it against all other chapters."*

**Every mechanical check is already clean.** `review.py` passes all twelve steps, `shipcheck`
is SHIPPABLE on six blockers, `xref` reads 0 broken and 0 unreferenced, `dupes` and
`copyedit` read 0. **So this pass is not for anything a regex can find.** Per
`SPEC_FINAL_PROOF_2026-08-07.md` §4, steps 1–7 exist so that step 8 — this — is spent on
what only a reader catches.

**The record is unambiguous about where the value has come from.** Every high-value finding
in the last two weeks came from a person reading, not an instrument: *"Not x but y is
sneaking in"* · *"the faces ARE altitudes"* · *"this should've already been ruled on and
changed"* · *"the issue I'm running into is the use of 'the WAVE'."* **Read like that.**

---

## 1 · Report, do not edit

**Change nothing.** No `Edit`, no `Write` to any file under `manuscript/`, `appendices/`,
`front_matter/` or `back_matter/`. **You are producing findings, not fixes.**

**The rule that governs everything here: never show unreviewed prose.** If you propose
replacement wording, mark it clearly as a draft for review. It goes through the
`mtgoa-review` pass before it lands, and that is not your job.

**Every finding needs three things or it is not a finding:**

1. **`file:line`** — the exact site
2. **The claim**, in one sentence
3. **The evidence** — the quoted text, and for a cross-chapter finding, the quoted text
   from the *other* chapter that it collides with

**Rank by severity and say which tier each is:**

| tier | means |
|---|---|
| **BLOCKING** | a reader is misled, a promise is broken, or two shipping sentences contradict |
| **REAL** | a genuine defect that does not mislead — a dropped payoff, a form break, a flat passage in a load-bearing spot |
| **THIN** | you noticed it and a reasonable editor might not act |

**A board that is mostly noise trains a person to skim it.** That lesson cost three rounds
of narrowing on 2026-08-07 — `ranking.py` 26→9, `copyedit.py` 47→8→0, `dupes.py` 34→0.
**Ten real findings beat sixty candidates.** If a section is genuinely sound, say so and move
on; do not manufacture findings to fill a report.

## 2 · What you are reading against — the cross-chapter job

**This is the half that has never been done.** Every previous pass read chapters one at a
time. Eight specific collisions are worth hunting, and they are ordered by how much damage
each does:

**a · Promise and payoff.** ch1 and ch2 make forward promises by name — *"you will meet that
one with the Diplomat in Chapter 7"*, *"a superpower you will only spot in motion"*, *"a line
added in every chapter ahead."* **Does the named chapter deliver the named thing, under the
same name?** A promise paid off under a different name is a broken promise. Track every
forward reference out of your chapter and every backward reference into it.

**b · One concept, two names — and one name, two concepts.** **This is the defect class that
has cost the most.** `WAVE` named two different practices across four chapters, an appendix,
the glossary and the index, and no instrument could see it because `xref.py` only asks
whether pointers resolve. **Nothing in `instruments/` asks whether a concept has one name.**
So you ask. Check anything your chapter coins or borrows against how the other eight say it.

**c · Form parity across the six Faces.** ch3–ch8 share a form and it is load-bearing:

> **Seven sections** — 1 The Exile · 2 The Distortion · 3 The Concept · 4 The Practice ·
> 5 Journey to the Center · 6 The Game · 7 Recap and Transition

Each Face also carries: **five game moves** · **twenty cards** (five movements × four
domains) · **a polarity pair** with an Appendix F pointer · **a school** · **a distortion the
village is left with** · **a native material** · **a daemon it works with** · **the
`*You're winning when:*` frame** in its domain blocks · **`The X means:`** in its opening.
**A part missing, or present in a different shape, is a finding.** On 2026-08-03 a rename
made ch9 the only one of four chapters out of form and it took measurement to catch;
on 2026-08-07 a sweep broke the six-Face `The X means:` pattern the same way.

**d · The native-material ladder.** emotion (ch3) · will (ch4) · loyalty (ch5) · logic (ch6)
· relationship (ch7) · perspective (ch8). **Does your chapter's native material stay its own,
and do the neighbouring chapters respect the boundary?**

**e · Contradiction between shipping sentences.** Two chapters asserting incompatible things
about the same object. **A known live one, deliberately untouched and still unruled:** ch3
calls the Form's units **stages**, ch5 and Appendix C call them **movements**, ch9 calls them
**moves**. Report what your chapter does and where it collides; do not fix it.

**f · Assumed prior knowledge, in both directions.** Does your chapter use a term, a move or
a Face as though already taught, when it is taught later? Does it re-teach at full length
something an earlier chapter already did — the reader's time spent twice on one idea?

**g · Cast continuity.** Ines · Ravi · Nadia · Tomas · Dara · Yusuf · Ana · Meera · Dele ·
Alan · Ellis · Ade · Femi · Tess · Bea · Ruth · Jo · Imani · Dana · Corin · Irix · Maera Voss
· Kit. **Does a named person's situation stay consistent across chapters?** Same job, same
history, same pronouns, same outcome.

**h · The apparatus voices.** Marginalia (`> ` blocks), admissions pages, the treatises that
open each Face chapter and sign off at the close of Section 3, the Headmaster's letter
between ch2 and ch3. **These are characters, not the author.** Does a margin hand say
something the body later contradicts without meaning to? Do the six treatise voices stay
distinct from each other and from Wendell's?

## 3 · What you are reading *for*, within your own chapter

**The five always-on constraints** (`REVISION_INSTRUMENT` Part 1), which no counter can
fully see:

1. **Hero and guide.** The reader is the hero; the book is the guide. A passage that makes
   the author the hero is a defect.
2. **Ranking, not denying.** **A negation is legal only if the negated thing is still true at
   the end of the sentence.** *"Not just A, but B"* ranks and is legal. *"Not A, but B"*
   denies and is not. `ranking.py` catches only the fragment forms; **the sentence-level and
   paragraph-level versions are yours.** This is the single highest-yield thing to read for —
   it was caught by eye and it caused an instrument.
3. **Mechanism visible.** A claim about what a move does must show how it does it. An
   assertion with the mechanism removed reads as authority.
4. **No Orange substrate.** No optimisation/efficiency/leverage framing as the book's own
   ground, outside ch6 where the Architect owns it and it is that Face's material.
5. **Beat placement.** A joke, an admission or a turn landing where it undercuts the work
   rather than paying for it.

**Then the ordinary line-edit questions.** Does the chapter open where it should. Does any
section outstay itself. Is there a paragraph doing no work. Does an example actually
demonstrate the claim above it. Does the reader know, at every point, what they are being
asked to do.

## 4 · What is already ruled — do not re-report these

**This list exists because a settled ruling re-reported as a finding costs the same to read
as a real one.**

- **The six Faces ARE the integral altitudes** — Shaman/Magenta, Challenger/Red, Regent/Amber,
  Architect/Orange, Diplomat/Green, Sage/Teal, in chapter order. **The concealment is
  deliberate.** The ideal reader is Green and allergic to hierarchical language; a savvy
  reader is meant to find it, and a regular reader has overcome the allergy by the time she
  does. **Do not name the ladder in the body, and do not propose naming it.** The reveal
  already exists in `ON_THE_SHOULDERS_OF`, sourcing ch8's Teal language to Laloux. **If you
  find a place where the ladder leaks into the body, that IS a finding — the opposite one.**
- **`WAVE` and the `Five-Move Form` are two different practices** and the split was finished
  on 2026-08-11. WAVE = Welcome · Acknowledge · Validate · Exhale, four breath actions, at
  home in Open Up. The Five-Move Form = Wake Up · Open Up · Clean Up · Grow Up · Show Up.
  Short form **"the Form"** is canon. **Any surviving `WAVE-Spiral` is a finding.**
- **The Form is a martial artist's form**, ruled 2026-08-11 in
  `AMENDMENT_FORM_METAPHOR_2026-08-11.md`, explained once at `ch3:284` and glossed at
  `ch1:260`. The earlier jazz ruling is superseded. **A third metaphor for the same noun is a
  finding.**
- **ch9's humor cells are Play · Fondness · Handoff**, not Clown/Jerk/Cult Leader. *"Ch9 has
  no butt and does not need one… Ch3–Ch8 humor metabolizes charge. Ch9 humor is charge-free."*
  **`ch9:348` and `ch9:352` trip `humor.py` and must stay** — the depression-well passage and
  the Captain Save-a-Kid admission are testimony, not jokes.
- **Marginalia hands may spell British.** Voice, not error.
- **Capitalisation:** a move name is capitalised when the sentence *names* it and lowercase
  when the sentence *tells you to do it*. **Both spellings are canon** and the same rule
  governs the four domains — *Direct Action* names the domain, *taking direct action*
  describes the activity.
- **`ch9:200`'s `### The Stage Sequence:` is in form** — ch4:297, ch5:384 and ch8:463 use the
  same shape. A rename here was reverted on 2026-08-03.
- **`Kit` is deliberately excluded from `agency.py`'s `ANIMATE` set** — `ch8:598` uses it as
  an object.
- **Two trivial items are unruled and known:** ellipses (`...` ×2 against `…` ×4) and
  `first-year` hyphenation (3 hyphenated, 2 open).

## 5 · Where things are

```
manuscript/ch1.md … ch9.md          the nine chapters
front_matter/headmasters_letter.md  sits between ch2 and ch3
appendices/                         A domains · B quests · C channels · D alchemy
                                    E 3-2-1 · F polarity · G shoulders · H sheet
back_matter/glossary.md             spine label "Key Terms"
back_matter/index.md                generated — instruments/index_build.py
specs/STYLE_SHEET.md                the book's memory: spelling, punctuation,
                                    numbers, hyphens, italics, caps, cast, xrefs
specs/SPEC_FINAL_PROOF_2026-08-07.md  what this pass is
instruments/                        run any of them; none of them will find
                                    what you are looking for
```

**Reading order for you:** this brief · `specs/STYLE_SHEET.md` · **your chapter, whole, twice**
· then the other eight against it. The second read of your own chapter is where the findings
are; the first one is orientation.

## 6 · The shape of your report

```
# ch<N> — deep read

## Verdict
Two or three sentences. Is this chapter sound? What is the one thing
most worth doing to it?

## BLOCKING
## REAL
## THIN
   each: file:line · the claim · the evidence · (cross-chapter: the collision, quoted)

## Read against the other eight
   What you checked and what held. Name the promises in and out of this
   chapter and whether each one is paid. Say plainly what you verified
   and found sound -- a checked-and-clean is worth reporting, an
   unchecked dimension is worth admitting.

## What I could not check
```
