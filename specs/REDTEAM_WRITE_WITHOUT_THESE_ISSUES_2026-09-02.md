---
type: redteam
title: "Red team — why 'a way to write without these issues' will partly fail, and what the evidence says works"
aliases:
  - red team generative discipline
  - why the solve fails
  - write without these issues
tags:
  - editorial
  - mtgoa
  - process
  - research
created: 2026-09-02
review: 2026-09-16
source:
  - specs/RESEARCH_TELLING_NOT_SHOWING_2026-09-02.md
  - specs/EDITORIAL_AUTHORITIES_2026-09-01.md
---

# Red team — the plan will partly fail

**Wendell, 2026-09-02:** *"I'd like a hostile review for why this is going to ultimately fail
mixed with external research about how such an approach has worked in the wild."*

**The proposal under review** — my two-part solve for the telling defects that keep reaching
him one layer deeper each draft:

1. **A generative discipline** — a pre-write protocol I apply to myself (scene not claim,
   concrete agent plus real verb, abstract equals unfinished).
2. **A mechanical backstop** — extend the pass to catch the light-verb class (*land, leave,
   make, give*) on abstract subjects.

**The verdict, up front:** part 1 is the plan's weakest point, and the research predicts it
underperforms. Part 2 works, at scale, in the wild — but only for the enumerable, and each new
rule buys less than the last. **What actually works is the part neither of us
proposed as the mechanism: the external signal. His eye.**

---

## Five reasons it fails, each with the evidence

### 1 · The judge is the defendant

**The generative discipline asks me to catch, before writing, the exact defect I have proven
across six drafts I cannot catch after writing.** This is not a motivation problem a protocol
fixes. It is a capability the research says the model lacks.

Huang et al., *Large Language Models Cannot Self-Correct Reasoning Yet* (ICLR 2024): **without
external feedback, self-correction does not reliably improve output and at times degrades it.**
The line that names this thread exactly: *models can repair an error once its location is
supplied, but cannot reliably find that location themselves.* The transcript above runs exactly
that way — Wendell locates, I repair, the next draft carries the same defect somewhere new.

**A protocol I self-administer is intrinsic self-correction wearing a checklist.** The evidence
says the checklist does not install the missing judgement.

### 2 · Goodhart — the defect relocates the moment a detector targets it

**Goodhart's law: when a measure becomes a target, it stops being a good measure.** Every draft
in this session passed the growing instrument set — gate, diet, empty-head, fragment,
antecedent, slop, trailing-and, telling — and every one carried a defect the instruments did
not model, one layer deeper. *praise has a shape* passed everything. *it leaves you smaller*
passed everything. *you start watching* passed everything.

**Add a light-verb detector and the defect moves to the next un-modeled layer** — a strong verb
with no real referent, a scene that shows the wrong moment, a true sentence in the wrong place.
The instrument count has gone from one to nine chasing a defect that keeps stepping sideways.
Nine will not be the number that closes it, because no finite list closes an open class.

### 3 · The defect is baked into the model, not sitting on top where a prompt can reach it

**Industry analysis, 2026:** *stylistic guidance and prompting techniques have limited
effectiveness because the underlying issue is embedded in how these models are fundamentally
trained and optimized.* The default reaches for the abstract proposition and the light verb
because the training corpus — *millions of mediocre whitepapers and press releases* — made that
the highest-probability continuation. And: **editing AI text makes it feel more personal, but
the stylistic fingerprint usually remains.**

**So the protocol fights the grain of the tool on every sentence, forever.** It does not retrain
the default. It asks the default to be overridden by will, one token at a time, by the same
system whose will is the default.

### 4 · Linters cannot model "scene or claim," and light-verb bans produce contortion

**The mechanical half has a ceiling the best tools have already hit.** `proselint`, the most
academically careful prose linter, reports a false-discovery rate of 1 in 10 — *twenty times
better than Microsoft Word* — and its own authors conclude **every software editing tool is
incomplete: none frees our knowledge of good writing from its bindings.** `write-good` flags
to-be verbs exactly as I proposed and is known for false positives, because not every *is* is
weak — *the third you are* is the point of its sentence.

**A light-verb ban has a failure mode of its own: contortion.** Forbidding *is, has, make,
leave, give* pushes the writer toward torqued strong verbs that call attention to themselves —
*praise shrinks you*, which I drafted and backed away from because it preened. The cure grows a
new tic.

### 5 · The wild successes are technical docs, not literature

**Where this approach demonstrably works, it works on the opposite of this book.** Vale, the
prose linter used in the wild by GitLab, Red Hat, Grafana and Datadog — *Datadog keeps 14
writers consistent across 35 product areas with it, and GitLab makes it a required check in
CI* — enforces **enumerable, mechanical rules**: terminology, passive voice, banned words,
house consistency. It succeeds because **documentation wants consistency and does not want
voice.** This book wants the reverse. Its defect is artistic — *telling instead of showing* —
which is precisely the class no linter in that list touches.

## What the same evidence says works

**The hostile read is not nihilism. The evidence points at a working mechanism — it is just not
the one I called the solve.**

**External feedback beats self-correction, decisively.** The Huang result has a positive half:
**models correct reliably once the error's location is supplied.** That is this session working
as designed. Wendell's eye is the external signal, and the detectors are a cheaper, faster
external signal that catches the enumerable subset before his does. **The loop is the product,
not the protocol.**

**Mechanical rules enforced in a pipeline scale.** Vale is real, adopted, and load-bearing for
teams larger than this one. The instrument set is this project's Vale, and it works for the
same reason: **it externalises the enumerable so no one has to hold it in their head.** Growing
it to catch light verbs is worth doing — as a pre-filter, not a cure.

**Goodhart has a known mitigation, and the project already uses it:** multiple orthogonal
sensors, adversarial checks, and — the important one — **auditing whether the metric still
tracks human judgement.** Nine instruments is not embarrassing; it is the orthogonal-axes
strategy. The discipline it demands is to keep asking, on each of Wendell's catches, whether a
detector could have caught it.

## What this means for the design

**Do not build part 1 as a cure, and do not sell it as one.** A pre-write protocol is worth
writing down as a reminder of what good looks like, but the research forecasts that a
self-administered checklist will not stop the defect at generation time. Claiming it will is the
same over-confidence that put five clean-scoring drafts in front of Wendell.

**Build part 2, scoped honestly.** A light-verb / weak-agency detector — the Williams test,
which `agency_grep.py` already gestures at — as a pre-filter that shrinks what reaches him.
Accept its false positives and its ceiling.

**Reframe the goal, because the current one is unreachable.** *"Write without these issues"* asks
a model to defeat its own training-baked default by will. The evidence says no. **The reachable
goal is a shrinking gap and a faster loop:** more of the defects caught mechanically before he
sees them, his eye reserved for the irreducible class that only judgement catches, and a running
count of which catches were fixable-by-instrument versus judgement-only. When the first number
stops falling, the pass has caught up to what mechanics can do, and the rest is his to hold —
permanently, not as a failure of the method but as the boundary of it.

## Sourcing

**Read as search-result extracts, not primary texts** — `arxiv.org`, `github.com` and most of
the cited hosts are blocked by this environment's egress proxy, so the Huang paper, the proselint
study, the Vale case studies and the 2026 industry analyses come through search summaries.
**The two claims worth verifying against the primaries before leaning hard on them** are the
exact Huang finding on self-correction degradation and proselint's 1-in-10 false-discovery rate.

- [Huang et al., *LLMs Cannot Self-Correct Reasoning Yet*, ICLR 2024](https://arxiv.org/abs/2310.01798)
- [*The Self-Correction Illusion: LLMs Correct Others but Not Themselves*](https://arxiv.org/pdf/2606.05976)
- [Suchow et al., proselint study](https://suchow.io/assets/docs/pacer2016proselint.pdf) · [proselint](https://github.com/amperser/proselint) · [write-good](https://github.com/btford/write-good)
- [Vale](https://vale.sh/) · [Vale in GitLab CI](https://docs.gitlab.com/development/documentation/testing/vale)
- [Goodhart's law](https://en.wikipedia.org/wiki/Goodhart's_law)
- [When AI Writes for You, Can It Still Sound Like You? — NSF TRAILS](https://www.trails.umd.edu/news/when-ai-writes-for-you-can-it-still-sound-like-you)
