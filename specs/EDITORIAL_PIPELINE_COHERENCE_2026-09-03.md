---
type: spec
title: "The editorial pipeline — how it checks itself, and how it travels to other projects"
aliases:
  - pipeline coherence
  - editorial pipeline portability
  - use on multiple projects
  - project profile
tags:
  - editorial
  - mtgoa
  - process
  - portability
created: 2026-09-03
review: 2026-09-20
source:
  - instruments/coherence.py
  - instruments/review.py
  - specs/EDITORIAL_AUTHORITIES_2026-09-01.md
---

# The editorial pipeline — checked against itself, and made to travel

**Wendell, 2026-09-03:** *"how do we check that the editorial pipeline is coherent and
consistent. I'm wanting to use this on multiple projects. Basically anything that I'm writing
must follow these rules."*

**Two questions, and they share one answer.** The way you keep a pipeline coherent is the way you
keep prose coherent: a check with a call site, run every time. What makes a
pipeline portable is what makes it checkable — **a clean line between the rules,
which are universal, and the profile, which is one project's own.** Draw that line once and both
questions are answered.

---

## 1 · How it checks itself — `coherence.py`

**The pass checked the prose. Nothing checked the pass.** It was coherent by luck: every step in
`review.py` happened to point at a real file, every baseline constant happened to match what its
instrument measured, every instrument a spec named happened to exist. On 2026-09-03 one of those
had already drifted — `telling.py` said *749 absolutes across the book* and measured
*302* — and nothing was watching.

**`coherence.py` is the watch.** Five checks, run as book step 9, so it has a call site and
cannot become the orphan it warns about:

| check | what it proves | hard? |
|---|---|---|
| **wiring** | every instrument `review.py` names, draft loop and book steps, exists on disk | fails the board |
| **drift** | every instrument that declares a `BOOK_BASELINE` still measures within 0.4 pt of it | fails the board |
| **register** | every ``instrument.py`` named in `EDITORIAL_AUTHORITIES` exists | fails the board |
| **orphan** | every baseline-declaring instrument is wired into `review.py` | fails the board |
| **doc-figure** | a book-wide count in a docstring still matches the measured count | reports only |

**It found the drift the moment it existed** — the 749/302 gap, propagated into the docstring and
two spec lines, corrected in the same session. The divergence was invisible to every other check and
obvious to this one — the whole argument for the checker in one line.

**What it does not yet check, honestly:** the many prose scanners that carry no `BOOK_BASELINE`
(`fragment`, `antecedent`, `slop_shapes`, `empty_head`, `ranking`) are outside the drift and
orphan checks. Extending those comes first, and it wants the manifest below.

## 2 · The line: universal rules vs project profile

**Everything in the pipeline is one of two kinds.** A rule that is true of any prose Wendell
writes, or a fact about this one book. They are tangled together in the files today; naming which
is which is the whole portability job.

### Universal — the rules (these travel unchanged)

- **The defect logic** — the regexes and counters in `telling.py`, `trailing_and.py`,
  `light_verb.py`, `fragment.py`, `antecedent.py`, `slop_shapes.py`, `prose_diet.py`,
  `empty_head.py`. Show-don't-tell, the loose *and*, the buried verb, the sentence fragment, the
  orphan pronoun, the AI shapes. None of these knows the book's name.
- **The structural gate** — sentence-initial *And*/*But*, glued em-dashes, negative stacks, live
  placeholder tokens, production tags. AI-slop mechanics, true everywhere.
- **`draft_lines.py`** — already reads any file into the record shape. The draft path is *already*
  project-agnostic; it proves the split is real.
- **`review.py`'s orchestration** and **`coherence.py`** — the sequence and the self-check.

### Profile — this project's own (these are declared per project)

- **The baselines** — `3.0%` telling, `13.9%` trailing-and, `0.7%` light-verb, the `prose_diet`
  ratios. Every one was *measured on MTGOA*. A different book has different numbers, and a
  baseline copied rather than measured is a lie the drift check would immediately catch.
- **The banned-word list in `gate.py`** — the handful of voice-specific words Wendell has ruled
  out for this book, plus the banned move-names. These are *this book's voice decisions*, made
  one at a time. Another project bans other words, or none.
- **The corpus** — `find_line.py` reads `build_book.SPINE`, the printed book. Another project's
  corpus is a different set of files.
- **The ontology instruments** — `agency_grep.py` and `agency_registry.yaml`, the six-role
  grades. Wholly MTGOA. A project without that ontology does not run them.

## 3 · The seam that makes it travel — the manifest (built 2026-09-03)

**The profile is now one file: `editorial.yaml`.** The baselines that lived in three Python
constants and the banned list that lived inside `gate.py` were pulled into it; `profile.py` loads
it, and `gate.py`, `telling.py`, `trailing_and.py` and `light_verb.py` read their profile from it,
each with its old hardcoded value as a fallback so a missing manifest changes nothing.

```yaml
# editorial.yaml — one per project
corpus:  ["manuscript/ch*.md", "appendices/APPENDIX_*.md", ...]   # what "the book" means here
baselines:
  telling: 3.0
  trailing_and: 13.9
  light_verb: 0.7
banned:  ["synergy", "leverage", "utilize"]                       # THIS project's voice words (illustrative)
pass:    [gate, prose_diet, fragment, antecedent, slop_shapes, trailing_and, telling, light_verb]
project_only: [agency_grep]                                       # instruments that do not port
```

**`coherence.py` validates the manifest against reality** — every named instrument exists
(`manifest`), every declared scanner is actually wired (`pass-wire`), every baseline matches a
fresh measurement (`drift`). A negative test confirmed all three bite: a baseline set to a wrong
value, and an instrument named that does not exist, both fail the board. **One manifest, one
self-check, any project.** A new project copies `instruments/`, writes its own `editorial.yaml`,
and the same checker validates it.

**What is not yet manifest-driven, honestly:** `review.py`'s step *sequence* is still declared in
Python — the manifest lists the universal `pass` and `coherence.py` checks it is wired, but the
book-only steps (voice, seam, citations, round-trip) and the draft-loop's per-tool counts still
live in the orchestration. That is the right place for control flow; the manifest carries the
data that varies, which is the part that had to move for the pipeline to travel.

## 4 · The open decision — how the core is shared

**The manifest settles what varies per project. It does not settle how the shared core reaches a
new project**, and that is a real fork with different costs:

1. **A copied template** — `cp -r instruments/ newproject/` and write a new `editorial.yaml`.
   Simplest; drifts over time as fixes land in one copy and not the others.
2. **A shared repo as a git submodule** — the instruments live once, each project pins a version.
   No drift; adds submodule mechanics to every project.
3. **A pip-installable package** — `pip install mtgoa-editorial`; the pass is a dependency, the
   manifest is the project's own. Cleanest for many projects; the most up-front work to build.

**Recommendation: start with the copied template plus the manifest** — it makes the split real
today with no packaging work — and promote to the submodule or package once a second project is
actually running and the drift becomes a cost worth paying to remove. **The manifest is worth
building first either way**, because all three distribution models need it and none of them is
clean without it.

## The standing rule

**A pipeline with no self-check silently diverges, exactly as a rule with no call site does.**
`coherence.py` runs as book step 9. When the pipeline moves to a manifest, the manifest becomes
the single source both `review.py` and `coherence.py` read, and the split between universal and
profile stops being a paragraph in this spec and becomes a file the machine enforces.
