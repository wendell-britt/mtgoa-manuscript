# Publishing Base v0.1

A portable house layer for Wendell Britt book repositories.

## What this is

MTGOA proved several useful publishing ideas in production:

- Git-backed manuscript canon;
- explicit author approval for prose changes;
- review-before-canon;
- measurable editorial gates plus human voice review;
- separation of manuscript from derived artifacts;
- one manuscript source feeding PDF and EPUB;
- build checks that fail loudly instead of guessing.

Publishing Base extracts those ideas without inheriting MTGOA-specific canon, Calrunia frame logic, chapter forms, or local vocabulary.

## What this is not

It is not yet a standalone package or repository.

For v0.1 it is staged inside `mtgoa-manuscript` as the reference implementation's extraction branch. Emotional First Aid will be the first clean instantiation. Once two books implement the same interfaces, the genuinely shared code can be moved into a dedicated publishing repo/template.

## Portable files

- `AGENTS.template.md` — canonicality, approval, mode separation, Git and production boundaries.
- `editorial/REVIEW_GATE.md` — house review sequence before prose becomes canon.
- `../specs/001-publishing-base/spec.md` — requirements and acceptance criteria.
- `../specs/001-publishing-base/plan.md` — staged implementation plan.
- `../specs/001-publishing-base/tasks.md` — rollout checklist.

## Core invariant

**Every surface may propose. Git records canon. Wendell controls prose canon. Production never silently becomes editorial.**

## Intended book-repo shape

```text
AGENTS.md
README.md
manuscript/        # canonical prose
 drafts/           # proposals and unapproved prose
canon/             # model/terminology decisions
research/          # evidence, stories, notes
specs/             # scoped changes and decisions
editorial/         # local house-style additions + review config
instruments/       # review/check tools
production/        # source → output transforms/renderers
assets/            # required source assets
build/             # ignored derived artifacts
MANIFEST.md        # ordered spine, version/build metadata
```

## Inheritance rule

Books inherit the Publishing Base principles, not another book's local rules.

A new book may deliberately adopt an MTGOA rule, but it must do so explicitly. This prevents one manuscript's workaround from becoming every manuscript's style guide.

## First consumer

`emotional-first-aid` should be instantiated from this base, then used to discover what still depends on MTGOA assumptions.
