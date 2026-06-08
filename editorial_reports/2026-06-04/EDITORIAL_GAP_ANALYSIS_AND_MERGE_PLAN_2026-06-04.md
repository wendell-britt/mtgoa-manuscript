# Editorial Gap Analysis and Merge Plan — 2026-06-04

## Purpose

This memo compares the existing MTGOA editorial system with the new style materials added on 2026-06-04, then turns the overlap into a single copy-edit plan for next week.

## What we already had

The existing system is strong on structure, placement, and chapter behavior:

- [SPEC_MANUSCRIPT_INTEGRATION.md](</Users/wendellbritt/The Library /mtgoa-manuscript/SPEC_MANUSCRIPT_INTEGRATION.md>) defines what goes where and why.
- [MTGOA_EDITORIAL_AGENT_SPEC_v3.md](</Users/wendellbritt/The Library /mtgoa-manuscript/MTGOA_EDITORIAL_AGENT_SPEC_v3.md>) defines the editorial pipeline and human cold read as a first-class input.
- [CROSSCHAPTER_SPEC.md](</Users/wendellbritt/The Library /mtgoa-manuscript/chapters/CROSSCHAPTER_SPEC.md>) defines the cross-chapter structural patterns that keep the second half of the book from flattening.
- [GATE_VOICES_CANONICAL.md](</Users/wendellbritt/The Library /The Library/07 Book OS/07 Book OS/GATE_VOICES_CANONICAL.md>) defines the gate ontology and the developmental arcs.
- [MTGOA_BOOK_WORK_TRACKER.md](</Users/wendellbritt/The Library /mtgoa-manuscript/MTGOA_BOOK_WORK_TRACKER.md>) keeps the backlog, sequencing, and editorial state visible.

In short: the old system tells us the book’s architecture, chapter function, and workflow.

## What the new materials add

The new style materials do not replace the old system. They sharpen the voice layer.

- [MTGOA_Developmental_Editorial_Specification.pdf](</Users/wendellbritt/The Library /mtgoa-manuscript/editorial_reports/2026-06-04/MTGOA_Developmental_Editorial_Specification.pdf>) gives the formal developmental style baseline for the copy-edit pass.
- [deep-research-report.md](</Users/wendellbritt/The Library /mtgoa-manuscript/editorial_reports/2026-06-04/deep-research-report.md>) gives the operational anti-AI style analysis:
  - detectors are triage, not verdict
  - style artifacts are best handled as spans, not broad “humanization”
  - the repair layer should target Wendell-specific moves: recognition, confession, game mechanics, reframing, comic escalation
  - the missing operational piece is a stable Wendell anchor corpus

This is the new layer’s core value: it tells us how to make the manuscript sound like Wendell without losing the structure already built.

## Gap analysis

### Gap 1: Structure is strong, but style repair is not yet operationalized

The old docs already govern content placement and chapter shape, but they do not yet provide a book-wide linting workflow for AI-like artifacts. The new report does.

**Merged fix:** keep the structural canon, add a style-lint layer before line-level copy edits.

### Gap 2: We have voice intent, but not yet a formal anchor corpus

The report makes this the highest-leverage missing piece. We still need a stable set of unquestionably Wendell-authored pages to serve as the voice reference.

**Merged fix:** build or confirm the anchor corpus before broad copy-editing starts.

### Gap 3: We have chapter-level editorial rules, but no single checklist for sentence-level repair

The old system tells us what each chapter should do. The new report tells us what to remove or rewrite when a sentence sounds wrong. Those need to be combined into one working checklist.

**Merged fix:** convert the deep research report into a chapter-by-chapter style-lint checklist.

### Gap 4: The tracker knows the backlog, but not yet the merged copy-edit sequence

The tracker contains the right pieces, but the next-week workflow needs to be explicit enough that copy-editing can start without re-litigating the editorial theory.

**Merged fix:** treat the new docs as the style baseline, while keeping the old spine as the authority on structure and placement.

## Merged strategy

The best synthesis is:

**Preserve structure, upgrade voice.**

That means:

1. Keep the existing editorial spine intact.
2. Use the new materials as a style-lint and voice-anchoring layer.
3. Repair locally, not by flattening the manuscript into generic “clean prose.”
4. Use detectors only to flag suspicious zones.
5. Use human voice judgment to decide the final form.

### What stays authoritative

- chapter architecture
- gate ontology
- cross-chapter structural patterns
- pipeline sequencing
- backlog and editorial state

### What the new materials govern

- anti-AI artifact detection
- style-lint categories
- Wendell anchor corpus
- voice anchoring
- local sentence repair
- the copy-edit pass for next week

## Copy-edit plan for next week

1. Confirm the Wendell anchor corpus.
2. Turn the deep research report into a short style-lint checklist.
3. Run the voice-anchoring pass chapter by chapter.
4. Preserve structure unless voice or clarity requires a change.
5. Use detector output only as triage.
6. Finish with a consistency sweep so the old spine and the new style layer still agree.

## Current backlog folded into the merged plan

The live backlog now sits inside this merged strategy instead of competing with it. The sequence below is the practical order for the remaining editorial work.

### 1. Structural cleanup that protects the spine

- **Ch6 channel reorder + format normalization**: keep this as the only must-fix structural item before any broad copy-editing.
- **Ch0 consolidation / rewrite**: keep the GM section and missing arcade material in view, but treat this as part of the opening-book stabilization rather than a new theory pass.

### 2. Voice and style repair

- **Style-lint checklist**: convert the deep research report into a working checklist before broad copy-editing.
- **Voice anchoring pass**: repair prose back toward Wendell using the anchor corpus and the five Wendell moves.
- **Terminology sweep / consistency pass**: keep the energy ecology, fuel budget, and alchemy language aligned across chapters.

### 3. Chapter-level editorial pass work

- **Ch1**: preserve the humane teaching and gates tutorial flow; use it as a primary voice calibration target.
- **Ch5–Ch8**: apply the cross-chapter pattern audit, especially the try-it-now practice, honest subsection, bars-engine proof, and come-back moment.
- **Ch6**: after normalization, use it as the main prose rhythm check.

### 4. Final pre-copy-edit readiness check

- Confirm the anchor corpus.
- Confirm the tracker reflects the merged sequence.
- Make sure detectors are only used for triage.
- Start the line-by-line copy-edit week from the merged plan, not from the older backlog alone.

## Success criteria

The merged strategy is working if:

- the manuscript still behaves like the manuscript structurally
- the prose sounds more like Wendell and less like a generic assistant
- style issues are caught as patterns, not as one-off annoyances
- next week’s copy-edit lane can start immediately without another theory pass

## Backlog principle

The backlog is no longer a separate queue floating next to the editorial plan. It is the execution order for the merged system: structure first where needed, then style repair, then chapter-level copy-editing.
