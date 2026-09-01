> **Provenance:** delivered by Wendell 2026-07-31, stored verbatim. How it maps onto
> this repository's existing machinery is ruled in `specs/SPEC_EDITORIAL_OS_INTEGRATION_2026-07-31.md`.
> The decision log it requires is `specs/DECISION_LOG.md`. Read the integration spec first;
> several of this document's defaults are adapted there against measured lessons in this repo.

# Lean Editorial Operating System

## The purpose

Finish the manuscript without flattening its voice, inviting a stealth rewrite, or creating an elaborate editing ritual that replaces real decisions. AI may identify evidence-backed candidates for attention and offer tightly scoped alternatives. The author decides what is a problem and owns every final sentence.

This is built for long-form nonfiction with a reader promise, an argument or framework, stories/examples, and practical guidance.

## The four rules

1. **Diagnosis before revision.** A scan identifies problems; it never changes prose. Revision begins only after the author has chosen a problem to solve.
2. **One job at a time.** Do not combine structural diagnosis, factual verification, line editing, and copyediting in one pass.
3. **Evidence or silence.** Every finding needs a specific location and a short quotation. “No material issue found” is a valid result.
4. **No unearned change.** If you cannot say what reader problem an edit solves, do not make it.

## Before you begin: make three anchors

### 1. The book brief

```text
Working title:
Ideal reader:
Reader’s starting problem:
Reader’s end-state / promise:
Central argument or framework:
Voice in five adjectives:
What the prose is allowed to do (fragments, humor, direct address, intensity, etc.):
What would betray its voice:
Non-negotiable factual or ethical boundaries:
```

### 2. The voice anchor

Select three to five passages you consider the book at its best. Do not polish them during this process. They are a comparison set, not a style checklist: edits elsewhere should not become more generic, formal, or emotionally muted than these passages.

### 3. The decision log

Maintain a short log:

```text
ID | location | reader problem | evidence | decision | intended result | status
```

Only items in this log may become editing work. It prevents rediscovery loops and makes rejected ideas stay rejected.

## The four roles

### 1. Book Architect — structure only

Use once at the beginning and once near the end. Give it the book brief, table of contents, a paragraph summary of each chapter, and whatever manuscript text fits cleanly.

It looks only for a broken promise/payoff, argument gap, bad sequence, consequential redundancy, contradiction, missing prerequisite, or a structural dependency that cannot be fixed locally.

It does not rewrite. It produces at most five findings and may recommend: **fix locally**, **make a structural decision**, or **leave alone**.

```text
You are the Book Architect for a human-authored nonfiction manuscript. Diagnose; do not rewrite.

[PASTE BOOK BRIEF]
[PASTE TABLE OF CONTENTS, CHAPTER SUMMARIES, AND TEXT]

Find at most five high-impact structural risks: a broken reader promise, argument gap, sequencing problem, significant redundancy, contradiction, missing prerequisite, or missing payoff.

For each, provide: ID; locations and quoted evidence; reader-level consequence; why this is structural rather than a preference; recommended disposition (fix locally / make a structural decision / leave alone); and evidence that would disprove the finding.

Do not praise, summarize, invent content, or edit prose. Report “no material issue found” where appropriate. Separate confirmed findings from hypotheses.
```

### 2. Continuity and Claims Auditor — consistency before polish

Use after the initial structural scan, and again only for material added or changed later. This is not a proofreader.

It checks terminology, definitions, promises, cross-references, names, numbers, timelines, quotations, case studies, and claims that carry the argument. Central claims need checking *before* line polishing begins.

```text
You are a continuity and claims auditor. Compare only the supplied chapters, canonical terms, and source notes. You are not a rewriter.

[PASTE CANONICAL TERMS, PROMISES, FACTS, AND SOURCE NOTES]
[PASTE TEXT]

Find verifiable inconsistencies or claims that need source/permission verification: terminology drift, changed definitions, broken cross-references, incorrect sequencing, names/numbers/timelines, quotations, case studies, and argument-bearing factual claims.

Return: ID | item | locations with quotes | discrepancy or verification needed | recommended action | confidence.
If a conflict may be intentional, mark VERIFY, not ERROR. Never invent a citation, fact, or source.
```

### 3. Line Editor — readability only

Use chapter by chapter only after relevant structural decisions and claim checks are complete. It flags only a concrete readability problem: ambiguity, vague reference, accidental repetition, unnecessary reader effort, a weak transition, or a grammar/style error.

It does not make prose more formal, more corporate, or generically smooth. The author can always choose “leave as-is.”

```text
You are a precise line editor. Preserve the author’s voice and intentional texture.

[PASTE BOOK BRIEF]
[PASTE CHAPTER PURPOSE]
[PASTE TEXT WITH STABLE PARAGRAPH NUMBERS]

Flag only a concrete readability problem: ambiguity, vague reference, accidental repetition, a needlessly difficult sentence, weak logical transition, or a grammar/style error. Ignore personal preferences.

Return at most 10 flags: location | original (maximum two sentences) | diagnosis | minimal proposed edit | reader problem solved | risk to voice | leave-as-is rationale.

Do not alter facts, meaning, tone, dialect, examples, or structure. If the passage works, leave it alone.

### Reader-run pattern audit — a supplement to the Line Editor

Use this after a reader has made a first pass through a bounded chapter or sequence.
It turns demonstrated reader friction into a repeatable audit; it is not a second
rewriting role. The Chapter 2 run established these questions:

1. **Name before reference.** Has the thing been named before a pronoun, a
   placeholder such as *somewhere*, or a claim about it asks the reader to infer it?
2. **Seat the consequential verb.** Does a named person, group, or licensed interior
   part hold the action that matters? Use `agency_grep.py` as a recall net; it does
   not decide the sentence.
3. **Show before interpreting.** Does a social fact, observable behavior, or concrete
   situation arrive before the sentence explains what it means?
4. **Earn embodiment.** When prose names bracing, tightening, vigilance, or another
   body-state, does it give a concrete event and observable consequence? Do not ban
   body language; reject only a generic somatic explanation that substitutes for one.
5. **Preserve real both/ands.** Do not deny one true condition merely to make the
   contrast cleaner. If people move the goalposts *and* conditions change, let both
   facts stand.
6. **Do not stage significance.** Cut an instruction to hold, sit with, or bravely
   face a line unless the instruction itself changes the reader's next action. Make
   the content carry its importance.
7. **Teach in reader order.** Introduce a term before using it; state where a promised
   document or practice sits in the production spine before judging an apparent gap.
   Continuity reads must use `instruments/build_book.py`, not adjacent chapter files
   alone—Chapter 2's Headmaster letter is a standalone file placed between Chapters 2
   and 3 by that spine.

`instruments/reader_run_scan.py` supplies a small, high-recall candidate list for
questions 4 and 6. It is deliberately narrow and always exits successfully: a hit is
a place to read, never a defect or a required edit. Questions 1, 2, 3, 5, and 7 need
the reader's judgment and recorded evidence. Add a new mechanical pattern only after
a reader has caught it in the manuscript and can state the reader problem it caused.
```

### The named authorities — added 2026-09-01

**This system answers to five style authorities and each one has a call site.** The register is
`specs/EDITORIAL_AUTHORITIES_2026-09-01.md`; the short version is that **Lanham, Williams and
Sword** supply the counters in `prose_diet.py`, **vague-pronoun doctrine** supplies
`antecedent.py`, and **Strunk** supplies `trailing_and.py` — Rule 4 on `and` as *"the least
specific of connectives"* and Rule 14 on a succession of loose sentences.

**An authority enters that register only with a rule that has a call site.** A named source with
no instrument is a citation rather than a practice, and this project has three files that proved
it: `fragment.py`, `antecedent.py` and `notstack.py` each existed for a defect Wendell kept
catching by eye, and none ran on a draft for weeks.

**The pattern-audit rule above applies to authorities too** — add a mechanical check only after
a reader has caught the defect and can state the problem it caused. Every rule now in the
register got there that way.

### 4. Voice Guardian — final editorial gate

Use only on passages changed during a line-edit batch. Compare the original and revision to the book brief and voice anchor. This role is deliberately conservative: it guards against the most common AI failure, prose that is technically cleaner but less alive.

```text
You are the Voice Guardian. Compare each original passage and proposed revision against the book brief and voice anchor.

[PASTE BOOK BRIEF]
[PASTE VOICE ANCHOR]
[PASTE ORIGINAL / REVISION PAIRS]

For each pair, choose ACCEPT, RESTORE ORIGINAL, or REVISE MINIMALLY. In one sentence, assess specificity, rhythm, authority, emotional temperature, and natural syntax. If revision is needed, alter only the offending words.

Reject edits that are generic, over-smoothed, verbose, corporate, falsely certain, or less alive than the original.
```

## The actual loop

1. **Whole-book scan.** Run Book Architect. Choose no more than three issues worth pursuing.
2. **Make the decision.** For each chosen issue, write in the decision log what must become true for the reader. If it requires a structural decision, make that decision yourself before asking for wording.
3. **Verify dependencies.** Run the Continuity and Claims Auditor on the relevant chapters and source notes. Resolve or explicitly defer material verification questions.
4. **Edit one bounded unit.** Work on one section or chapter. Use the Line Editor only after the section is structurally settled.
5. **Test the edit yourself.** Read the changed paragraph aloud with its surrounding pages. Then answer: *What can the reader now understand, trust, feel, or do that they could not before?* If there is no clear answer, restore the original.
6. **Protect the voice.** Run Voice Guardian on accepted changes, comparing them with the voice anchor.
7. **Commit the one decision.** Review the diff. Commit only one coherent editorial decision, update the log, and proceed.

## When a “minimal edit” is the wrong tool

Do not patch a design problem sentence by sentence. Escalate to a structural decision when:

- A section is solving two different reader problems.
- The reader needs information that arrives later.
- A claim requires a different example, evidence, or qualification.
- You have made two local fixes and the passage is still unclear.
- The premise, not the wording, is what the reader is resisting.

Possible structural decisions are: move, cut, split, merge, add a bridge, replace an example, qualify the claim, or leave intentionally unresolved. Make the decision first; return to line editing afterward.

## Priority, without fake math

Ask these questions in order:

1. Does this threaten the book’s central promise or reader transformation?
2. Does it make a core claim untrustworthy, unclear, or unsafe?
3. Does it affect more than one chapter?
4. Is the evidence strong enough to justify disruption?
5. Is the likely improvement worth the words, time, and risk it introduces?

The first “yes” generally beats a dozen small readability fixes.

## Stop rules

Stop the pass when:

- You cannot name a concrete reader problem remaining in the section.
- Suggestions have become rephrasing preferences rather than corrections.
- The same issue has been checked twice with no new evidence.
- You are changing text because it is not the model’s preferred style.

After content and line work are frozen, run a conventional copyedit for mechanics and house-style consistency, then conduct a clean, human read-aloud pass. AI does not replace real readers: if possible, use a few people who resemble the intended audience to test the chapters where your structural choices matter most.

## Git cadence

Use branches for an editorial concern, not a mechanical unit:

```text
edit/reader-promise
edit/framework-continuity
edit/ch03-clarity
edit/house-style
```

Each commit should answer one editorial question, such as: `Clarify Chapter 3 bridge from diagnosis to practice`. Compare each change with the baseline and the voice anchor before you keep it.
