# Publishing Base v0.1 — Plan

## Plain version

Do not rip MTGOA apart first.

Use MTGOA as the reference implementation, write down the portable contract, then prove that contract by creating Emotional First Aid from it. Only after EFA works should shared production code be extracted into its own repository or package.

That order prevents us from generalizing MTGOA-only accidents into house law.

## Technical strategy

### Phase 1 — Define the portable contract

Create a small, readable base that can be copied into a new book repository:

- canonicality and approval rules;
- house editorial principles;
- draft/review/plan mode separation;
- repository layout contract;
- review-gate sequence;
- production-layer contract;
- branch and release hygiene.

Do not port MTGOA-specific chapter conventions, Calrunia frame devices, current banned words, or statistical thresholds as house defaults.

### Phase 2 — Instantiate Emotional First Aid

Create `wendell-britt/emotional-first-aid` and seed it with:

```text
AGENTS.md
README.md
manuscript/
drafts/
canon/
research/
specs/
editorial/
production/
build/        # ignored
MANIFEST.md
```

Initial manuscript files:

```text
manuscript/00-introduction.md
manuscript/01-where-is-your-oz.md
manuscript/02-meet-the-expedition-team.md
manuscript/03-signal-is-not-strategy.md
manuscript/04-emotions-are-narrative-truth.md
manuscript/05-first-aid-for-yourself.md
manuscript/06-first-aid-for-others.md
manuscript/07-survive-contact-with-emotion.md
```

The chapter list is a working spine, not permanent canon. EFA's scope rule overrides it: first aid ends when CONTACT and orientation produce a next aligned Challenger action; Regent through Sage belong to deeper Emotional Alchemy.

### Phase 3 — Port editorial tooling, not MTGOA conclusions

Reuse the architecture of MTGOA's review pass:

1. plain-language truth test;
2. hard gate;
3. prose-drift measurement;
4. no-AI-slop reading/eval;
5. rerun measurement after edits;
6. manuscript-wide checks after insertion.

But make configuration local:

```text
editorial/
  HOUSE_STYLE.md
  REVIEW_GATE.md
  book_rules.yaml
  voice_reference.md
```

The tool should read configuration rather than embedding EFA or MTGOA vocabulary in code.

### Phase 4 — Port production as a second implementation

Copy/adapt the MTGOA production interfaces into EFA without changing MTGOA first:

```text
production/
  build_book.py
  typeset.py
  build_pdf.py
  build_epub.py
  book/
```

Required invariant: the production layer may read and transform manuscript content but never write editorial changes back into `manuscript/`.

Do not extract a shared package yet. Two working implementations are the evidence needed to know what is truly generic.

### Phase 5 — Extract the shared package

After EFA ships a reproducible PDF and EPUB, compare the two implementations.

Move only genuinely shared code/rules into a dedicated publishing repository. Candidate shared surfaces:

- repo template;
- editorial review runner;
- generic manuscript completeness checks;
- shared intermediate representation;
- PDF/EPUB builder shell;
- release scripts;
- documentation.

Book-specific format choices remain local: trim, fonts, frame devices, chapter styling, workbook rails, marginalia, etc.

## Branch model

For book repos:

- default branch = current canonical manuscript;
- `draft/*` = prose generation or chapter work;
- `editorial/*` = review/remediation passes;
- `production/*` = format/build work that should not touch prose;
- release tags = named editions.

Short-lived branches are preferred. The MTGOA history already demonstrates that two long-lived prose branches touching the same chapters create expensive reconciliation.

## Multi-surface contract

Every surface can read canon and propose work. Only Git commits update durable canon.

- ChatGPT: research, interviewing, drafting, review, GitHub writes.
- Codex/Claude Code: repository-local implementation, review tools, production work.
- Obsidian: reading, notes, optional editing when the vault is backed by the repo.
- local editor: direct manuscript work.
- GitHub: durable history, branches, review, releases.

No surface gets a private canonical copy.

## Build model

Use one ordered manuscript spine and one shared transform before format-specific rendering.

```text
manuscript
   ↓
completeness check
   ↓
shared typeset/intermediate transform
   ├──→ PDF renderer/checks
   ├──→ EPUB renderer/checks
   └──→ future HTML renderer/checks
```

Build artifacts stay out of Git unless intentionally attached to a tagged release.

## Voice model

Do not use a universal numerical "Wendell voice score."

Use two reference layers:

1. **Author baseline** — selected passages/books known to represent Wendell's natural prose.
2. **Book register** — approved passages from the current book.

Measurements are diagnostic, not sovereign. Human review wins when a metric encourages a new defect.

## Migration rule

Publishing Base is initially **vendored** into each book repo as readable local files with an `upstream_version` marker.

Do not begin with Git submodules. They increase synchronization complexity before there is enough shared code to justify it.

When the shared production layer stabilizes, package or template distribution can replace manual vendoring.

## Decision gates

### Gate A — Ready to instantiate EFA
Pass when the portable spec, repo contract, and editorial gate are readable without MTGOA context.

### Gate B — Ready to call EFA multi-surface
Pass when a prose proposal can originate on one surface, be reviewed/approved, land in Git, and be read correctly from another.

### Gate C — Ready to extract shared production code
Pass only after MTGOA and EFA both build from the proposed common interface.

### Gate D — Publishing Base v1.0
Pass when a third book can be created without copying MTGOA-specific code or rediscovering editorial rules.
