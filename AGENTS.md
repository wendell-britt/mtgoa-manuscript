# manuscripts/ AGENTS.md — MTGOA Book Editing

## Primary Identity

MTGOA manuscript — lives in `/home/workspace/manuscripts/`
Syncs to Obsidian via `The-Library/The Library/` (workspace) → Mac

## Canonicality

**As of 2026-07-28 this changed. Read this section before trusting any older doc.**

**Rule:** `manuscript/ch1.md` – `ch9.md` **in this git repository** are the canonical book. Edit these. Nothing supersedes them.
**Rule:** Obsidian and the Claude project are no longer canonical for chapter content. They are upstream history.
**Rule:** No canonical write happens without Wendell's conscious approval.
**Rule:** If an agent drafts or rewrites text without approval, that text is a proposal, not canon.
**Rule:** Anything outside `manuscript/` — including everything in `chapters/`, `compiled/`, and the root-level specs — is process history, a verification surface, or a derived artifact.

## Showing the work (standing rule, 2026-07-29)

**Paste every prose change into the console, before and after, in the reply that
makes it.** Wendell reviews in the conversation, not by opening files or reading
diffs. A change he cannot see in the console has not been shown to him.

- Quote the **old text and the new text**, in full, for every line touched. Not
  a summary of the change, not a file path and line number, not "updated ch5's
  opener."
- For a batch, use a table or a per-site before/after block. Group by chapter.
- Drafts for review go in the console **and nowhere else** — do not write them
  into `manuscript/` and ask him to look. Apply only what he has approved.
- Counters and test output still get reported, but they do not replace the
  prose. `BLOCK 39 -> 38` says nothing about whether the sentence is any good.

## Pushback carries a remedy (standing rule, 2026-08-27)

**Never raise a risk without a specific fix for that specific risk.** Wendell, 2026-08-27, on a
note that told him not to start a book: *"If you are going to do pushback you need to have a
remediation for the specific problem you are solving for otherwise you will come off as a neurotic
nag pretending that they are being wise."*

**He is describing a real failure and it has a shape.** An objection with no remedy attached
sounds like judgement, costs him a decision he had already made, and returns nothing he can act
on. Caution is cheap to produce and expensive to read.

**The test, before any objection ships:**

1. **Name the specific problem**, not a category of problem. *"This competes with four open
   obligations"* rather than *"this seems premature."*
2. **Attach a remedy that solves that problem**, at a cost he would actually pay.
3. **If no remedy exists, the objection is information rather than advice** — say it once, plainly,
   and do not repeat it or dress it as a recommendation.
4. **Check the objection's own premises first.** The note that produced this rule assumed
   *announcing*, when the plan was pre-production; assumed the new book competed for money, when
   it might fund the old debts; and assumed drafting meant writing a manuscript, when podcasting
   and blogging are how this author drafts. **Three premises, none of them checked, all of them
   his to know and mine to ask about.**

**The related error, worth naming separately.** Offering a "cheaper test" that is a substitute for
the thing he wants to do, rather than a mode of doing it. *Write an article instead of a book* is
an objection wearing a suggestion's clothes. *Draft it as episodes and posts, which is drafting*
is a remedy.

## Complete sentences, and every noun points at something (standing rule, 2026-08-29)

**Two rules he gave in one sitting, on marketing copy that had passed the whole review clean.**

**1 · No fragments.** Wendell, 2026-08-29: *"fragments are bad. I speak in complete sentences."*
This retires the earlier defence that a fragment triplet earns its place by being the most concrete
moment on the page. **It is not a density question, it is a voice question**, and a voice rule
outranks a texture argument. `REVISION_INSTRUMENT.md` Part 1 already restricts fragments to beats
in landing position; **treat that as the ceiling, not the licence**, and in anything customer-facing
write the sentence out with a subject doing something.

**The usual repair is to give the images a doer.** *"The meeting where somebody gets talked over.
The decision that lands on whoever can least afford it."* becomes *"You catch the meeting where
somebody gets talked over, the decision that lands on whoever can least afford to absorb it."*
**Nothing is lost but the drum.**

**2 · Every noun and pronoun has to point at something a reader could name.** Wendell, mid-draft,
on *"the meeting where the same person absorbs it again"*: ***"what person? what is it? We're
handwaving again."*** And on *"the noise of doing the work"*: ***"'this work' — what is 'this
work'? how will a reader recognize it?"***

**The test is his, and it is stricter than the counters.** `waste` measures how often *it/this/that*
appear; **he is asking whether each one has an arrow**, which is a different question and the one
that matters. Before shipping a sentence with a definite article or a pronoun in it: **state the
noun out loud.** If the answer is a category rather than a thing — *the work*, *the process*, *the
same person* — rewrite until the reader could point at it. *"The meeting that ends with the person
who named the problem owning it"* passes because the person is identified by what they did.

**Why this is a standing rule and not a note.** Four instruments exist for these exact patterns and
none of them runs on drafts — see `specs/GAP_DRAFT_REVIEW_INSTRUMENTS_2026-08-29.md`. **Until that
is fixed, these two are checks to run by hand on every customer-facing draft**, because the pass
will report `clean` on prose that fails both.

## Reporting to Wendell — ELI5 first (standing rule, 2026-08-09)

**Every reply opens with a plain-language section, before any detail.** Wendell, 2026-08-09:
*"explain it to me like I'm 5 what the above means… Your explanations are hard for me to
understand."*

**The rule already existed and was being applied to the wrong thing.** `mtgoa-review` step 0
requires an ELI5 of every passage before the register version, and says *"if you cannot write
the ELI5, you do not have the passage yet."* That was being applied to the book's prose and not
to the reports about it. Same test, same reason.

**The shape of a reply:**

1. **Plain version, at the top, always.** Short sentences. Everyday words. What happened, what
   it means for the book, and what is needed from Wendell. **No instrument names, no file paths,
   no line numbers, no trade terms** — no `waste 1.37`, no `xref 7e`, no *widow*, *recto*,
   *prodtag*, *sticky*. If a thing has a plain name, use the plain name.
2. **A rule line**, then the detail, for the record.
3. **The ask, if there is one, stated as a question** rather than buried in a paragraph.

**Two traps this rule exists to catch:**

- **Precision is not the same as clarity, and the log needs precision.** The commit message and
  `LOG_FINAL_PROOF` keep every site, count and instrument name. **The reply does not.** Writing
  the reply as a second copy of the log is what made them unreadable.
- **An ELI5 header on top of dense prose is not an ELI5.** If the plain section still needs a
  glossary, it has not been written yet. Rewrite it, do not annotate it.

**What stays in the plain section even though it is uncomfortable:** anything applied that was
not asked for, anything that turned out wrong, and anything still undecided. **Simplifying is
never a licence to leave out the bad news** — it is the reason the bad news gets read.

## Editing Protocol

When asked to edit, run the WAVE Editing Spiral:
**Full spec:** `The-Library/The Library/07 Book OS/SPEC_BOOK_EDITING_PROCESS.md`

**Practice:** The 321 somatic practice is author-led and optional. Do not access
or require the Zo surface as an automated precondition for analysis, planning,
drafting, review, or canonical edits. It never blocks editorial work. Wendell may
choose to do a somatic practice independently or request one explicitly.
**Rule:** ALWAYS git commit before and after editing
**Rule:** ALWAYS update tracker after session

## Git (CRITICAL)

```bash
# WRONG — workspace git ignores manuscripts/
cd /home/workspace && git add manuscripts/...

# RIGHT
cd /home/workspace/manuscripts && git add chapters/... && git commit -m "edit: [description]"
```

## Canonical Chapter Files

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

Numbering is 1-indexed. The retired `chapters/ch[N]-[FACE]/` drafts were
0-indexed, so every reference in an older doc is off by one. Conversion table in
`chapters/README.md`.

**Rule:** Every number quoted about this manuscript comes from running an
instrument in `instruments/` against these files. Planning documents have been
wrong.
**Rule:** Edits go through `instruments/spec_edit.py`, which aborts and writes
nothing on a missed or duplicated anchor.
**Rule:** Run `instruments/dupes.py` on new prose before insertion. Sentences
have been accidentally duplicated across five chapters before.

## Companion Files

- `specs/MANUSCRIPT_FILE_CANON.md` — canon, standing editorial rules, the voice gate
- `specs/MTGOA_INSTRUMENTS_TOOLKIT.md` — the reviewer gate and measurement tools
- `chapters/README.md` — what survives in `chapters/`, and the renumbering
- `MANIFEST.md` — export index and per-chapter word counts
- `MTGOA_BOOK_WORK_TRACKER.md` — updated after every session

## EA Standards

Every move in the book:
**Alchemy N — Emotion Name → Alchemical Outcome**

**DEPRECATED — do not write the bracketed tag.** This line used to read
`**[DISSATISFACTION → SATISFACTION] Transcend [X] — …**` and that bracket is a
production tag, not a chapter voice. It was deprecated 2026-06-03, and it has
come back into the book twice since, because **this instruction is where it is
generated from.** The verb also changed: the book says *Alchemy 1* / *Alchemy 2*
and the word *Transcend* appears nowhere in the body.

`instruments/gate.py` now hard-fails on any `[ALLCAPS]` tag in `manuscript/`, so
a move written to the old pattern cannot ship. See
`specs/SPEC_BRACKET_TAGS_2026-07-29.md` for the full history.

Energy economy (+2/+1/-1) — context for writer only, NOT in book content.
