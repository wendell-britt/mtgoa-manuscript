# Publishing Base v0.1 — Tasks

## Phase 1 — Contract

- [x] Inspect MTGOA canonicality rules.
- [x] Inspect MTGOA review gate and no-AI-slop eval.
- [x] Inspect MTGOA source-to-PDF/EPUB production layers.
- [x] Write portable Publishing Base specification.
- [x] Write implementation plan.
- [ ] Add portable AGENTS template.
- [ ] Add portable editorial review gate.
- [ ] Add concise repo contract / README.

## Phase 2 — Emotional First Aid

Blocked on creation of `wendell-britt/emotional-first-aid`.

- [ ] Create repository.
- [ ] Seed the Publishing Base files.
- [ ] Add EFA-specific `AGENTS.md`.
- [ ] Add EFA scope/canon documents.
- [ ] Add the current research log and story database.
- [ ] Add `manuscript/00-introduction.md` from the approved Author-stage draft.
- [ ] Create chapter stubs from the current working spine.
- [ ] Add Four Hour Book AUTHOR process as EFA-local process guidance.
- [ ] Add EFA terminology/voice configuration.

## Phase 3 — Editorial tooling

- [ ] Identify which MTGOA checks are truly generic.
- [ ] Port generic checks behind book-local configuration.
- [ ] Establish EFA author baseline and approved book-register samples.
- [ ] Add review command that can run on proposal files without touching canon.
- [ ] Add manuscript-wide gate after insertion.
- [ ] Verify that fixing one metric cannot silently bypass another gate.

## Phase 4 — Production

- [ ] Port/adapt completeness check.
- [ ] Port/adapt shared typeset transform.
- [ ] Establish EFA print design and trim.
- [ ] Build PDF.
- [ ] Build EPUB.
- [ ] Add format-specific checks.
- [ ] Confirm both formats derive from the same manuscript spine.
- [ ] Confirm builders never edit `manuscript/`.

## Phase 5 — Extraction

- [ ] Compare MTGOA and EFA implementations.
- [ ] Mark code/rules shared by both.
- [ ] Create dedicated Publishing Base repository or template.
- [ ] Move only proven-generic components.
- [ ] Instantiate a third book as the v1.0 proof.

## Definition of done for v0.1

EFA can be worked on from multiple surfaces, with Git as durable canon; proposed prose cannot silently land; approved prose survives review gates; and a single manuscript source can produce reproducible PDF and EPUB outputs.
