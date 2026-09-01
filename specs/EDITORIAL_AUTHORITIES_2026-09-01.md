---
type: spec
title: "The editorial authorities — which guides this project answers to, and which rule has an instrument"
aliases:
  - editorial authorities
  - style guides
  - strunk integration
created: 2026-09-01
review: 2026-09-20
source:
  - specs/EDITORIAL_OPERATING_SYSTEM.md
  - specs/RESEARCH_TRAILING_AND_2026-09-01.md
  - .claude/skills/mtgoa-review/SKILL.md
---

# The editorial authorities

**Wendell, 2026-09-01:** *"First we need to formally integrate the strunk rules into our
editorial system, do research on any other style guides that would benefit us from not running
into this AI slop issue again."*

**Four authorities were already load-bearing here and none of them was written down as one.**
Lanham, Williams and Sword each appear in an instrument docstring as the reason a counter
exists; Strunk arrived on 2026-09-01. **This file is the register**, and its organising claim
is that **an authority earns its place here by producing a rule a machine can find.**

---

## 1 · Strunk, formally

**The 1918 *Elements of Style*, read from the PDF Wendell uploaded.** Four rules bear directly
on prose this project generates.

| rule | what it says | status here |
|---|---|---|
| **4** | *"and, is the least specific of connectives. Used between independent clauses, it indicates only that a relation exists between them without defining that relation."* | **`trailing_and.py`**, review step 3d |
| **11** | *Use the active voice* | `prose_diet.py` — `passive` |
| **13** | *Omit needless words* — *"every word tell"* | `prose_diet.py` — `waste`, `empty`; `empty_head.py` |
| **14** | *Avoid a succession of loose sentences* | **`trailing_and.py`**, both tiers |
| **15** | *Express co-ordinate ideas in similar form* | **unchecked.** See §4 |

**Rule 13's list of expressions is directly checkable and mostly is not checked.** *the question
as to whether*, *there is no doubt but that*, *he is a man who*, *this is a subject which*, and
above all **`the fact that`**, which Strunk says *"should be revised out of every sentence in
which it occurs."* `slop_shapes.py`'s `EMPTYPHRASE` rule covers a different list. **Adding
Strunk's is an afternoon and it is the cheapest unclaimed win in this document.**

**Rule 4 also supplies the two repairs to try first**, which is why the research spec lists
them ahead of the others: subordinate the clause, or reduce it to a phrase.

## 2 · The four that were already here, now written down

| authority | what it gave this project | instrument |
|---|---|---|
| **Lanham, *Revising Prose*** | the Paramedic Method — box the be-verbs, find who is kicking whom | `prose_diet.py` — `be`, `copula` |
| **Williams, *Style*** | characters as subjects, actions as verbs; nominalization as the primary defect | `prose_diet.py` — `zombie`; `agency_grep.py` |
| **Sword, *The Writer's Diet*** | be-verbs, zombie nouns, and the waste words *it / this / that / there* | `prose_diet.py` — the counter set is hers |
| **Vague-pronoun doctrine** | draw an arrow from every pronoun to its antecedent | `antecedent.py`, review step 3b |

**Williams is the one to read against the rule rather than with it.** He calls coordination
*"the foundation of a gracefully shaped sentence"* when the coordinated elements are parallel
in grammar and in sense. **That is the licence Rule 14 needs so it does not become
superstition**, and it is why `trailing_and.py` reports a rate rather than a count.

## 3 · Researched 2026-09-01 — what else earns a place

**The question was which guides prevent the specific failure, so the test applied to each was:
does it produce a rule a machine can find?**

### Orwell, *Politics and the English Language*, 1946 — the diagnosis, forty years early

**His account of ready-made phrases is a description of next-token prediction:**

> *"they will construct your sentences for you — even think your thoughts for you, to a certain
> extent — and can partially conceal your meaning even from yourself."*

**That is the mechanism behind every finding in this repo's slop record.** A generated sentence
is not wrong because a machine wrote it; it is wrong when the phrase arrived before the thought
and the writer accepted it.

**Four of his six rules are already enforced here** — never a figure of speech you are used to
seeing in print (`slop_shapes.BANNED`), never a long word where a short one will do, cut every
word you can (`waste`, `empty`), never the passive where the active will serve (`passive`).
**The sixth is the one to keep visible:** *"Break any of these rules sooner than say anything
outright barbarous."* Every counter here is a candidate finder for that reason.

### Wikipedia's *Signs of AI writing* — the live catalogue, and the most useful new source

**A ~15,000-word community-maintained list of AI prose tells**, updated as models change. It is
the only source in this section that tracks a moving target, which is what makes it worth a
standing review date rather than a single read.

**Two of its findings are already instruments here** — the *"It's not X, it's Y"* parallelism is
`slop_shapes.BINARY`, and importance puffery is `slop_shapes.PUFFERY`.

**Three are not, and each is checkable:**

- **The rule of three.** Models over-produce three-item lists and triads. **Nothing here counts
  them.** This book uses deliberate triads, so a counter would report a rate rather than a
  defect, exactly like `trailing_and.py`.
- **Punctuation migration.** The catalogue records that as em-dash overuse got trained out,
  **colons and semicolons took the load**. `emdash.py` has a ratcheting budget and watches one
  mark; the defect moved and the instrument did not follow.
- **Undue emphasis on significance** — *fascinating*, *majestic*, *captivating*, and symbolism
  asserted rather than shown. Adjacent to `PUFFERY` and wider than it.

### PNAS, *Do LLMs write like humans?* — the stylometric finding worth acting on

**Instruction-tuned models produce a distinctly noun-heavy, informationally dense style**, and
they keep producing it when asked for informal register. **That is `zombie` and `empty_head`
already**, and the research says the pull is structural rather than a matter of prompting, which
argues for a measured ceiling rather than an instruction not to do it.

**The prevalence figures are the useful part:** LLM-associated patterns measured at **15.3% of
academic prose in 2024 and 26.2% in 2025.** The drift is fast enough that a fixed word list
dates in about a year.

### Considered and not adopted, with the reasoning rather than the verdict

| source | why not | how solid the reason is |
|---|---|---|
| **Garner's *Modern English Usage*** | a usage authority rather than a style one. It settles *which word* — *comprise*, *beg the question*, *which* against *that* — and this project's defects are structural. `gate.py`'s banned list is about voice rather than correctness, so Garner would arbitrate a question nobody here is asking | **holds.** A scoping judgement, not a knock on the book |
| **Zinsser, *On Writing Well*** | the core is clutter, which is Lanham's territory and already counted. No countable rule that the register does not already have | **holds under the test, and the test is the limitation.** See below — Zinsser's actual contribution is warmth and the writer's presence, which no counter can score |
| **Pinker, *The Sense of Style*** | the curse-of-knowledge diagnosis is real and unmeasurable | **thin, and I undersold him.** See below |
| **Christensen's cumulative sentence** | the *defence* of the loose sentence, held in `RESEARCH_TRAILING_AND` as the counterweight | **holds, and it is not a dismissal.** He is the opposing brief rather than an authority to obey, which is a role the register needs |

**Correcting the Pinker line, 2026-09-01.** *"Real and unmeasurable"* is true of the curse of
knowledge and it is not the whole book. Two points I passed over:

- **The curse of knowledge is this book's central risk**, not a general caution. MTGOA explains
  a six-role framework to a reader who does not have it, while concealing the ladder underneath
  on purpose. **A writer who can see the architecture cannot feel what the page is like without
  it**, which is the exact failure mode Pinker names.
- **His syntax material is partly measurable** — heavy left-branching, long dependencies between
  a subject and its verb. Nothing off-the-shelf counts it, so it stayed out; that is a cost
  rather than a reason.

**So Pinker is out of the register and into the reading list**, which is a different verdict
from the one the table first recorded.

### The blind spot in the test itself

**The register's admission test — does it produce a rule a machine can find — is right for what
this file is, and it excludes a whole class of defect that keeps going wrong.**

**Every correction Wendell has made to generated prose this year is in that excluded class:**

| his note | what it asks for | what could count it |
|---|---|---|
| *"then write more descriptive images throughout, don't keep them out of scarcity"* | density of concrete images | nothing |
| *"We want people to laugh out loud when reading"* | a joke that lands | nothing |
| *"fragments are bad. I speak in complete sentences"* | his voice, not a style rule | `fragment.py`, after he said it |
| *"what person? what is it? We're handwaving again"* | a noun a reader can point at | partly `antecedent.py` |
| *"this trailing 'and' construction needs to go"* | a rhythm he does not want | `trailing_and.py`, after he said it |

**Two of the five got instruments, and both only after he caught the defect first.** The
counters find what is mechanically wrong with a sentence and are blind to whether it is warm,
funny, concrete, or his.

**That is the argument for keeping Zinsser and Pinker on the reading list rather than striking
them.** The register catches slop. **Neither the register nor any counter in it can tell you
the prose is bloodless**, and bloodless is the failure this project's voice is actually at risk
from.

## 4 · What this leaves open, in the order it would pay

1. **Strunk Rule 13's expression list**, `the fact that` first. Checkable today.
2. **Strunk Rule 15**, parallel construction, is unchecked and is the rule most likely to catch
   a defect nothing else here sees — a three-item list whose members are not the same shape.
3. **A triad counter**, reporting a rate against the book's own.
4. **Extend `emdash.py` to the colon and the semicolon**, since the catalogue says that is where
   the mark went.

**Every one of those is a rate rather than a gate**, which is this project's settled pattern:
`gate.py` fails a build, everything else finds candidates.

## 5 · The standing rule

**An authority enters this register only with a rule that has a call site.** The four that were
here arrived as instrument docstrings and were invisible outside them; Strunk arrived because
Wendell caught a defect by eye and asked where it was written down.

**The failure this guards against has happened three times.** `fragment.py`, `antecedent.py`
and `notstack.py` each existed for a defect Wendell kept catching, and none of them ran on a
draft until 2026-08-29. **A rule with no call site is a rule nobody keeps**, and a named
authority with no instrument is a citation rather than a practice.

**Sources.** Strunk, *The Elements of Style*, 1918 — read from the uploaded PDF ·
[Orwell, *Politics and the English Language*](https://www.orwellfoundation.com/the-orwell-foundation/orwell/essays-and-other-works/politics-and-the-english-language/) ·
[Wikipedia, *Signs of AI writing*](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) ·
[PNAS, *Do LLMs write like humans?*](https://www.pnas.org/doi/10.1073/pnas.2422455122) ·
[Williams, *Style*](https://www.clc.hcmus.edu.vn/wp-content/uploads/2015/11/Style_-_Joseph_M._Williams_Joseph_Bizup.pdf)

**Sourcing note.** Orwell, the Wikipedia catalogue and the PNAS paper were read as
search-result extracts; `orwellfoundation.com`, `en.wikipedia.org` and `pnas.org` are all
blocked by this environment's egress proxy. **Strunk is the only one verified against a primary
text**, because Wendell uploaded it.
