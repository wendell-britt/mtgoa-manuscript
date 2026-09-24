# Publishing Base v0.1 — Specification

## Purpose

Extract the reusable publishing system proven inside `mtgoa-manuscript` into a portable base for Wendell Britt's future book repositories.

The base must let a book move across ChatGPT, Codex, Claude Code, Obsidian, local Git, and GitHub without ambiguity about which text is canonical, who may change it, or how a shipping artifact was produced.

The first consumer will be **Emotional First Aid**.

## Problem

MTGOA now contains a working editorial and production system, but its reusable rules are mixed with book-specific canon, Calrunia frame logic, old project history, and instrumentation tuned to one manuscript.

Copying the repository wholesale would copy both the useful machinery and the scar tissue.

We need a clean house layer that says what every Wendell book repo must guarantee, while allowing each book to define its own voice, canon, vocabulary, structure, and production exceptions.

## User stories

### US1 — One canonical manuscript
As the author, I can work from multiple tools and surfaces while knowing exactly which files constitute the book.

**Acceptance criteria**
- Each book repo declares a canonical manuscript path.
- Chat histories, Obsidian notes, scratch files, generated drafts, and compiled artifacts are non-canonical unless explicitly promoted.
- A canonical prose change requires Wendell's conscious approval.

### US2 — AI drafts cannot silently become canon
As the author, I can use AI heavily without losing authorship or discovering invented prose in the manuscript later.

**Acceptance criteria**
- Generated or rewritten prose is a proposal until approved.
- Review occurs before canonical insertion.
- Edits may not invent lived history, somatic experience, facts, examples, quotes, statistics, or opinions.
- The writer's distinctive vocabulary, cadence, bluntness, humor, uncertainty, and useful roughness are preserved.

### US3 — Draft, review, and plan are distinct modes
As the author, I can ask an agent to generate, review, or plan without the tool silently switching jobs midway through a turn.

**Acceptance criteria**
- Generate creates proposal text.
- Review evaluates existing text and does not silently rewrite canon.
- Plan chooses work and does not silently execute prose changes.
- A mode switch requires an explicit transition.

### US4 — One source produces many editions
As the author, I can build print, ebook, and later web outputs from one manuscript source.

**Acceptance criteria**
- Production code never edits canonical manuscript files.
- Shared transforms happen once before format-specific rendering.
- PDF and EPUB derive from the same ordered manuscript spine.
- Build outputs are derived and reproducible, not canonical source.

### US5 — The repo is safe for concurrent agents
As the author, I can use different agents or machines without cheaply creating irreconcilable prose forks.

**Acceptance criteria**
- Concurrent canonical prose work happens on separate branches or is explicitly sequenced.
- Pull requests expose proposed changes before merge.
- The canonical branch is the durable source of truth.
- Canonical changes are committed; uncommitted container edits do not count as completed work.

### US6 — House rules and book rules are separable
As the author, I can improve my publishing system once without forcing every book to share the same vocabulary or stylistic exceptions.

**Acceptance criteria**
- House rules live in a portable publishing layer.
- Each book can add local rules without editing the shared base.
- MTGOA-only rules such as Calrunia marginalia, its banned-word list, chapter naming, and EA production syntax are not inherited automatically.
- Voice measurement can select an author-level reference corpus plus book-local reference passages.

## Editorial contract

Every book instantiated from the Publishing Base inherits these principles:

1. **Git is the durable manuscript store.**
2. **Approval creates canon.** AI output is proposal text until Wendell approves it.
3. **Show prose before applying it.** When a canonical change is proposed conversationally, Wendell must be able to read the changed prose without opening a diff.
4. **Preserve voice before polish.** Make the minimum effective edit.
5. **Never fabricate specificity.** Do not invent reader history, author history, body states, examples, facts, quotes, statistics, or source claims.
6. **Plain-language truth test.** If a passage cannot be explained plainly, its idea is not ready for stylistic treatment.
7. **Review generated prose before canon.** Mechanical gates, prose-drift checks, and human/slop review happen before merge.
8. **Production is downstream.** Typesetting and export may transform representation, not editorial meaning.
9. **Derived artifacts remain derived.** PDF, EPUB, intermediate files, caches, and local build output are rebuildable.
10. **Parallel prose work requires branch isolation or sequencing.**

## Repository contract

A conforming book repository SHOULD contain:

```text
AGENTS.md
README.md
manuscript/
drafts/
canon/
research/
specs/
editorial/
instruments/
production/
build/          # ignored
assets/
MANIFEST.md
```

A small book may omit empty optional directories, but it MUST identify:
- canonical manuscript files and order;
- proposal/draft location;
- author approval rule;
- local editorial rules;
- build entry points;
- derived output location;
- release/version convention.

## Branch and release policy

- The default branch contains the current canonical book, even while the book is unfinished.
- Canonical prose changes normally arrive through short-lived branches and pull requests.
- Two agents should not edit the same canonical chapter on separate long-lived branches unless the conflict is intentional.
- Releases/tags identify exported editions; generated deliverables may attach to releases but are not manuscript canon.

## Review gate

A proposal is eligible for canon only when:

1. Its meaning can be stated in plain language.
2. It preserves the author's actual claim and does not add unsupported particulars.
3. It passes hard local bans/placeholders/syntax checks.
4. It is checked for recurring generated-prose drift.
5. It is checked for AI-slop patterns and robotic cadence.
6. The edit has not created a new defect while fixing an old one.
7. The author has seen and approved the prose when approval is required.

The base defines the sequence. Each book defines its own thresholds, banned words, reference corpus, terminology, and exceptions.

## Production contract

The house production model inherits the MTGOA four-layer separation:

1. **Completeness:** Is every required component present?
2. **Typeset transform:** Can the manuscript be represented consistently for downstream formats? Ambiguity is flagged, not silently ruled.
3. **Print renderer:** Produce and validate PDF.
4. **Reflow renderer:** Produce and validate EPUB.

Future HTML/web output joins layer 3 as another renderer from the shared transformed source.

## Repository hygiene

- Track source, configuration, tests, and small required assets.
- Ignore generated build output and caches.
- Keep setup and build commands documented and scriptable.
- Prefer deterministic builds: pinned dependencies, explicit source paths, no "newest matching file" guessing, and build-time verification that the expected intermediate was created by the current run.
- Automated checks should fail loudly when a required component or invariant is missing.
- Do not auto-fix editorial findings unless the rule is purely mechanical and explicitly safe.

## Out of scope for v0.1

- A universal cover generator.
- Distribution to KDP, IngramSpark, Gumroad, or other stores.
- Automated ISBN acquisition.
- Automatic promotion of AI prose into canon.
- A universal voice score shared by every book.
- Moving MTGOA's existing production code out of its repository before EFA proves the abstraction.

## First proving ground: Emotional First Aid

EFA should instantiate this contract with:
- its own `AGENTS.md`;
- its own canon and terminology;
- the 4-Hour Book AUTHOR workflow captured as local process, not house law;
- manuscript files for the introduction and chapters;
- a local review configuration based on Wendell's voice plus EFA's field-manual register;
- a production layer initially copied/adapted from MTGOA, then extracted once the second implementation proves which parts are genuinely shared.

## Success condition for v0.1

Publishing Base v0.1 is successful when EFA can be drafted from multiple surfaces, reviewed and approved without losing authorship, and built to at least PDF and EPUB from the same canonical manuscript without relying on MTGOA-specific canon or file paths.
