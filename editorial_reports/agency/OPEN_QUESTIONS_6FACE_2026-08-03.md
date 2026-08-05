# 6 Game Master Analysis — the open questions

**Wendell 2026-08-03:** *"let me get a 6 game master analysis of the open questions."*

No prose changed.

---

## The measurement first

Three questions are open. They are not the same size and two of them are not the
questions they appear to be.

| | question | status | real footprint |
|---|---|---|---:|
| **Q1** | W-4 — placement of the confrontation beat | UNRULED | 0 sites; asks for new prose |
| **Q2** | `somatic` — Grade 2 names an undefined verb class | flagged DL-41 | 0 sites governed |
| **Q3** | ch8:164's triple anaphora | held by R8_VERDICT — **and already converted** | 1 site, decided without a ruling |

**The agency audit itself is at 29 findings**, from 230 raw candidates. Every named
entity block has been read. What remains is false positives and recorded keeps.

**Q1's vehicle does not exist.** W-4 proposes *"a Game So Far beat."*
`SPEC_REPETITION_AND_CUTS.md:140`: *"`The Game So Far` does not exist in the
manuscript. Zero hits across all nine chapters, despite the project glossary
describing it as a recurring element with seven instances Ch2–Ch8."*

**Q1's demonstration does exist**, at `ch6:122`, unnamed:

> They learned to have the vocabulary of structural thinking without the
> practice. **They could then dismiss structural insight with the vocabulary
> itself:** *we already looked at the incentives, we're addressing the leverage
> points, we understand the systemic issues*, while continuing to do the same
> thing that had always produced the same failure.

**The slot is empty and pre-assigned.** The same spec's callback table gives
**Ch6 → Ch7: the leverage point, Structure↔Agency.** ch7 contains `leverage
point` **0 times** and `Structure ↔ Agency` **0 times**.

**Q2 governs nothing.** Verbs actually taken by the embodied three across the
manuscript: `decides` 8 · `does` 4 · `has` 4 · `takes` 3 · `showed` 3 ·
`developed` 2 · `prefers` · `holds` · `spends` · `runs` · `works` · `goes`.
Not one is somatic. No tightening, bracing, flooding, dropping.

**Q3 was decided by a pass that was not looking at it.** R8_VERDICT held it:
*"'It learned… It learned… It learned…' reads as one organism quietly acquiring
bad habits. 'They learned' dilutes it to crowd narration. It may be doing the
same work anchor 3 protects."* My `ch578_village.py` converted all three
instances. Its docstring discusses an anaphora — ch5's — and never mentions this
one.

---

## The six reads

### SHAMAN · the Body

Ask what is alive, and where the charge actually sits.

**Q1 is alive and has no name.** A reader meets *"we're addressing the leverage
points"* and feels the recognition land — that is the charge arriving. Then
nothing catches it. The book demonstrates the move three times (ch6's distortion,
ch3's council parable, ch7's letting agent) and never once stops to say *this is
a thing, here is what it is called*. **The signal fires and has nowhere to go.**

**Q2 is not alive at all.** Nothing in the prose reaches for a somatic verb on
the Protector, the Emotional Body or the Damaged Self. They decide and prefer.
The rule was written from an idea of how those daemons should sound, not from
listening to how they do.

**Q3 is the one the body can actually settle.** *"It learned… It learned… It
learned…"* is one creature acquiring a habit. *"They learned…"* is a crowd. The
Shaman's instruction is to read both aloud and notice which one has menace in
it. **I did not do that before converting.**

### CHALLENGER · the Line

What does each cost, and who pays?

**Q1: Jordan pays, and the cost is a move.** She has the diagnosis and no handle
for it. Unnamed, she cannot catch herself mid-sentence saying *the culture here
is toxic* instead of *Dave, you interrupted her three times.* The demonstration
without the label teaches recognition in other people and nothing about herself.

**Q2: the registry pays, in credibility.** A constraint that cannot be checked is
not a constraint, and this one has been unenforceable since the file was built.
`somatic` sits in Grade 2's licence list looking exactly like the other seven.

**Q3: I paid it, on Wendell's behalf, without asking.** A keep-candidate was
converted by a pass with a different remit. That is the line: **a hold means the
next pass stops, and this one did not.**

### REGENT · the Oath

What was inherited, and what did the book actually swear to?

Two of the three are the same inheritance defect. **W-4 swore to a structure that
was never built** — The Game So Far, described in a project glossary as recurring
seven times, present zero times. **`somatic` came in from the spec's C2 alongside
`DAEMON_CANON.md`**, and both name things that are not in the repo. DL-41 already
retired the second. The first is still standing.

The pattern worth recording: **this registry inherited three names for things
that did not exist** — a canon file, a verb class, a structural beat — and each
was carried for weeks because a name in a spec reads exactly like a name for
something real.

**Q3 is a governance question, not a prose one.** R8_VERDICT held four items.
Three closed by ruling. The fourth closed by accident. The Regent's question is
not whether the conversion was right. It is: *what is a hold worth if it lives
somewhere no instrument reads?*

### ARCHITECT · the Pattern

Do not adjudicate three cases. Find the one condition.

**All three are the same defect: a decision recorded where nothing enforces it.**

- W-2's navigation licence lived as prose in `open_rulings` and every navigation
  site kept flagging as a violation of the ruling that permitted it. Fixed
  2026-08-03 by encoding it as `entity_partial`.
- `somatic` lives as a name in a licence list with no lemma set behind it.
- R8_VERDICT's holds live in a markdown report that `agency_grep.py` has never
  opened.

**The fix is structural and it is one fix: a hold, a licence and a class are all
data, and all three belong in the registry where the instrument reads them.**
The registry already has `sense_exceptions`, `entity_partial` and `registers`,
all added this week for exactly this reason. A `holds:` block is the same move a
fourth time.

Do that and Q3 cannot recur. Leave it and it recurs on the next pass by the next
agent who has not read the verdict file.

### DIPLOMAT · the Bridge

Whose is it, and who can contest it?

**Q1's real question is ownership, and the note has it wrong.** W-4 assigns the
beat to the Diplomat's shadow. The evidence says the **Architect supplies the
vocabulary** and the **Diplomat reaches for it**. That is not a contradiction to
resolve — *it is the finding.* The Architect's language becomes the Diplomat's
hiding place, which is precisely why the beat belongs at the seam between their
chapters rather than inside either one. **The Ch6→Ch7 callback is that seam, and
it is empty.**

**Q3 needs a contest and has not had one.** R8_VERDICT's claim — *"it may be
doing the same work anchor 3 protects"* — is a claim about voice. It can only be
settled by someone reading both versions aloud. I converted it instead, which
closed the contest by default rather than by argument.

### SAGE · the Horizon

Which game is each of these, actually?

**Q1 is not a placement question.** It is a naming question wearing placement's
clothes. Once the demonstration is found at ch6:122 and the empty pre-assigned
slot is found at the Ch6→Ch7 seam, placement answers itself. The live question
is the one W-4 never asks: **does the move get a name, and does it join *Name the
Field* and *Say the Thing Under the Thing* on the roster?**

**Q2 is not a lemma question.** It is asking whether the constraint is
descriptive or aspirational. The prose has already answered: the embodied three
decide and prefer. So either the prose changes to match the rule, or the rule
changes to match the prose. **Writing a lemma list first would settle it in the
wrong direction and pretend the question was technical.**

**Q3 is closed, and the only live question is whether to reopen it.** The
conversion shipped, it reads clean, and the plural is arguably truer. The Sage's
discipline is to say plainly: **the cost of re-litigating usually exceeds the
cost of the loss — unless reading it aloud says otherwise, and nobody has.**

---

## Synthesis

**Three questions. One is real, one is mis-framed, and one is mine to answer for.**

**Q1 — W-4.** Rule the placement: **the Ch6→Ch7 backward callback.** The
demonstration is written, the slot is empty and pre-assigned the exact vocabulary
the dodge uses, and the ownership split (Architect supplies, Diplomat reaches)
is the reason the seam is right. Then answer the question W-4 does not ask:
**does it get a name?**

**Q2 — `somatic`.** Do not write a lemma list. **Decide first whether the
embodied three should sound somatic**, because the prose currently says they do
not. If yes, that is a prose pass and the class follows it. If no, delete
`somatic` from Grade 2's licence list and the constraint sentence with it. Either
way the dangling name goes, because a name for nothing is what DL-41 was about.

**Q3 — ch8:164.** Read both aloud. Keep whichever has menace. If the singular
wins, it is one revert.

## The move that gets all three

**Add a `holds:` block to the registry**, and put R8_VERDICT's remaining items
into it as data rather than prose. That is the fourth time this week the same fix
has been the answer — `registers`, `sense_exceptions`, `entity_partial`, and now
this — and it is the only one of the three questions whose answer prevents its
own recurrence.

## What it costs, stated plainly

The `holds:` block costs an hour and stops nothing else.

Q1 costs new prose, which needs before/after approval per site under both Jordan
specs, and it is ship-phase work rather than audit work.

Q2 costs a decision that has been deferred since the registry was built, and
deferring it again is free — nothing in the prose is waiting on it.

## The one thing I would not do

**I would not write the `somatic` lemma list.** It is the most tractable-looking
of the three and the only one where doing the obvious work first would lock in
the wrong answer. The list would look like progress and would quietly rule that
the constraint is right and the prose is wrong — a ruling nobody made, arriving
as a technical artifact. That is the same shape as the three inherited names the
Regent's read is about, and it is how the fourth one would get created.
