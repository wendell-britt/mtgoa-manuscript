# AGENTS.md — Book Repository

> Publishing Base version: 0.1
> Replace bracketed values when instantiating a book.

## Plain version

The book lives in Git.

AI can draft, review, and propose changes. It does not get to quietly decide what the book says. Wendell approves canonical prose.

Build tools may turn the manuscript into other formats. They may not rewrite the manuscript while doing so.

## Book identity

**Title:** [BOOK TITLE]

**Canonical manuscript:** `[MANUSCRIPT PATH OR FILE LIST]`

**Working register:** [SHORT DESCRIPTION]

## Canonicality

- The files named above are the canonical book.
- Git on the default branch is the durable source of truth.
- Chat conversations, Obsidian notes, local scratch files, `drafts/`, research notes, specs, and generated build output are not canonical chapter prose.
- No canonical prose write happens without Wendell's conscious approval.
- AI-generated or AI-rewritten prose is a proposal until approved.
- A change made in a temporary environment but not committed has not become durable canon.

## Show the work

When proposing prose changes conversationally:

- show the proposed prose in the conversation before applying it to canon;
- for edits to existing text, show enough before/after context for Wendell to judge the actual sentence rather than a summary of the edit;
- do not make Wendell open a diff merely to discover what wording changed;
- after approval, apply exactly the approved wording unless a new issue requires another proposal.

## Three work modes

### Generate
Create proposal prose. Do not silently promote it to canon.

### Review
Assess existing prose against the book's editorial rules. Findings are not automatic permission to rewrite canon.

### Plan
Choose or sequence work. Do not silently perform prose edits while planning.

If the job changes modes, state the transition.

## Editorial principles

- Preserve Wendell's actual voice before polishing it.
- Make the minimum effective edit.
- Keep distinctive vocabulary, cadence, bluntness, humor, uncertainty, useful digressions, and purposeful roughness.
- Never invent author history, reader history, somatic experience, facts, examples, quotations, statistics, or opinions.
- Never narrate an unnamed reader's pathology or body state as fact.
- If a passage cannot be explained plainly, work out the idea before styling it.
- Measurements and linters diagnose; they do not outrank meaning or voice.
- A repair that creates a new defect has failed.

## Local editorial rules

Read `[LOCAL EDITORIAL RULES PATH]` before drafting or editing.

Book-specific vocabulary, banned words, terminology, voice references, exceptions, and structural rules live there. Do not import another book's local rules unless Wendell explicitly adopts them.

## Review gate

Before proposed prose becomes canonical, run the local review sequence in `[REVIEW GATE PATH]`.

Minimum sequence:

1. Plain-language truth test.
2. Unsupported-specificity check.
3. Hard local gate.
4. Prose-drift diagnostics.
5. AI-slop / cadence review.
6. Re-run diagnostics after repair.
7. Author approval where required.
8. Manuscript-wide checks after insertion.

## Git discipline

- Commit canonical changes.
- Use short-lived branches for substantive prose, editorial passes, and production changes.
- Do not let two agents independently edit the same canonical chapter on long-lived branches unless the conflict is intentional.
- Keep production-only work separate from prose work where practical.
- Use pull requests when they improve review or when work crosses surfaces/agents.

## Production boundary

- Production reads canon; it does not editorially rewrite canon.
- Shared transforms may normalize representation for output formats but must preserve editorial meaning.
- PDF, EPUB, HTML, intermediates, caches, and local previews belong in derived output paths.
- Generated output is rebuildable and should normally be ignored by Git.
- The build must fail loudly when a required component or invariant is missing.

## Release boundary

- The default branch holds the current canonical manuscript, finished or unfinished.
- Tags/releases identify exported editions.
- A release artifact is derived from a tagged canonical state.

## Book-specific process

Read `[BOOK PROCESS PATH]` for the current authoring/editing method. A book-specific process is not automatically a house publishing rule.
