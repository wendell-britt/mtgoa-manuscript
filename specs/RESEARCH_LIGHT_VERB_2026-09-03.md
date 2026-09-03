---
type: research
title: "The light verb — the buried verb and the fake-concrete verb, the lists that name them, and the tools that catch them"
aliases:
  - light verb detector
  - weak verb
  - delexical verb
  - nothing words
  - lands warm
tags:
  - editorial
  - mtgoa
  - strunk
  - williams
  - research
created: 2026-09-03
review: 2026-09-17
source:
  - instruments/light_verb.py
  - specs/REDTEAM_WRITE_WITHOUT_THESE_ISSUES_2026-09-02.md
  - specs/EDITORIAL_AUTHORITIES_2026-09-01.md
---

# The light verb — the detector, its lists, and the field it comes from

**Wendell, reading the proof, 2026-09-02:** *"'lands warm' — what the fuck does landing warm
mean? Land is another one of those nothing words that gets overused."* And on *"it leaves you
smaller"*: *"who is the it that makes you smaller and how can they leave you?"*

**The red-team named this the buildable half of the solve.** That review
(`specs/REDTEAM_WRITE_WITHOUT_THESE_ISSUES_2026-09-02.md`) split the plan in two and forecast
that the self-administered discipline fails while **the mechanical, external, enumerable half
works — at scale, in the wild.** The light verb is enumerable. This spec builds that half, and
answers the two questions Wendell asked with it: **what lists already name these verbs, and what
have the people who went down this path built.**

---

## 1 · Two shapes ride under one complaint

**"Nothing words" is one gut-name for two different defects, and each has a different fix.**

### DELEXICAL — the buried verb

**A light verb plus a nominalization that hides the real verb inside a noun.** *make a
decision* (decide), *reach a conclusion* (conclude), *conduct an investigation* (investigate),
*provide assistance* (help), *perform an analysis* (analyse). The verb slot is spent on a verb
that means almost nothing; the meaning sits in the noun, one step removed from the action.

**This is old, named, and settled doctrine.** Strunk Rule 13 — *omit needless words, make every
word tell*. Williams, *Style* — **put the main action of the sentence in its verb, not in an
abstract noun.** It is the single most-taught prose repair in English, and it is mechanical:
recover the buried verb, drop the noun, the sentence shortens 10–20% and the action returns.

### DEAD — the fake-concrete verb

**A motion or placement verb handed a subject that cannot move or be placed.** *praise lands
warm*, *the shame sits there*, *it leaves you smaller*, *a decision lands on the person*. The
verb borrows the look of a physical action — *land, leave, sit, hang, settle, run* — and spends
it on an abstraction. On a concrete subject the same verb is honest (*she left the meeting*), which
is exactly why the defect hides: the word is not wrong, the pairing is.

**Wendell's eye caught this one where no counter saw it.** It tells the same way the
copula-label in `telling.py` does: a symptom that the thought under it is unfinished. The writer
reached for *lands* because the real verb — what praise actually *does* to you — had not been
worked out.

## 2 · The lists that already name these verbs

**Someone has made the list — several someones, and they agree.** The light verb is a settled
category in linguistics before it is a style fault.

**The linguistics core (Wikipedia, *Light verb*; British Council, *Delexical verbs*).** A light
verb — also *delexical verb, thin verb, empty verb, semantically weak verb* — is one that
carries little meaning of its own and forms a predicate with a noun that carries it. The
canonical set is small and stable:

> **do, make, take, give, have, get** — the six the British Council teaches — plus **keep, set,
> put, hold, go** in the wider lists. *"She made a decision"* is delexical; the meaning is in
> *decision*.

**The craft lists (ProWritingAid, Kindlepreneur, Self-Publishing School, Fictionary).** The
writing-coach world calls the same class *weak verbs* and adds the copulas: **forms of *to be*
and *to have*, plus the light verbs *make / take / get*, plus weak verb + adverb pairs**
(*walked quickly* → *hurried*). Their remedy is one line: **replace the weak verb, or the
weak-verb-plus-adverb, with one precise verb.**

**The nominalization signature (Williams; SJSU Writing Center).** The buried verb usually wears
a suffix — **-tion, -sion, -ment, -ance, -ence, -ity** — or a gerund. *"She performed an
analysis"* → *"she analysed."* *"conducted an investigation"* → *"investigated."* The suffix is
what makes the DELEXICAL tier mechanically findable.

**The detector uses all three.** Light-verb list for the verb slot, nominalization suffix for
the noun slot, and — added for this book — the two verbs Wendell named by hand, **land and
leave**, as the head of the DEAD family.

## 3 · What the people who went down this path built

**Wendell's second question: for people who have gone through path 2, what have they been doing?
What lists and linters have developed?** The answer is a decade of prose linters, and they share
one architecture and one ceiling.

| tool | what it is | what it flags near this defect |
|---|---|---|
| **write-good** (btford) | a naive JS prose linter, the most-forked of them | passive, weasel words, adverbs, wordiness, *there is/are* openers, **and an opt-in E-Prime mode that flags every *to-be* verb** |
| **proselint** (amperser / Suchow) | 20+ modules, each following a named editor | redundancy, jargon, clichés; FDR ~1 in 10, **20× better than Word — and its authors still conclude every such tool is "incomplete"** |
| **Vale** (errata-ai) | the CI-grade linter — GitLab, Datadog, Red Hat, Grafana | YAML rules of a few types: **existence** (flag a word list), **substitution** (X→Y), **occurrence** (count per scope), readability. Weak-verb detection = an `existence` rule with a `tokens:` list |
| **matt.might shell scripts / editsaurus** | grep one-liners, the ancestor of the rest | a hard-coded weasel-word list and a *to-be* list, greped straight |
| **textlint** + `textlint-rule-write-good` | pluggable JS linter re-hosting write-good | the write-good checks, configurable |
| **alex** | inclusive-language only | (out of scope, listed for completeness) |

**Three findings from that field decide how this instrument is built:**

1. **They are all existence checks on word lists.** Vale, the most serious of them, reduces to
   *flag these tokens, substitute these, count these.* A light-verb detector is not a new idea;
   it is a `tokens:` list. **So `light_verb.py` is a word-list existence check by design**, and
   claims nothing more.

2. **The most relevant feature ships OPT-IN because it is too noisy.** write-good's E-Prime mode
   — ban every *to-be* verb, the exact rule the craft lists ask for — is off by default, because
   *not every* is *is weak.* **The false-positive floor lives exactly there**, and it is why the DELEXICAL
   tier keeps a stoplist (*reality, conscience, presence*…) and the DEAD tier is surfaced, not
   graded. The red-team predicted this ceiling; the field confirms it.

3. **Where they succeed is technical docs, not literature** — enumerable house rules, CI gates,
   consistency without voice. `light_verb.py` inherits their reach and their limit: it catches
   the enumerable subset before Wendell does, and **the irreducible class — a strong verb with no
   real referent — stays his eye's.**

## 4 · The remediation

**DELEXICAL — recover the action.** *make a decision* → *decide*. Not a better noun; the verb.
Mechanical, and the fix Strunk and Williams both give.

**DEAD — give the verb a subject that can do it.** *it leaves you smaller* → name who, and let
them do something a person can do: *when you take the grade, their read of your work outranks
your own.* The dead verb flags an unfinished thought; the fix is to finish it, not to swap in a
stronger-looking verb (*praise shrinks you* preens — a new tic, per the red-team).

## 5 · The instrument — `light_verb.py`

**Two tiers, matching the two shapes:**

- **DELEXICAL** — light verb + article + nominalization. **Gradeable, drive down.** A single
  strong verb is buried; the fix is mechanical. Reported as a rate against the book.
- **DEAD** — a motion/placement verb on an abstract or bare-demonstrative subject. **Surfaced,
  never graded** — on a concrete subject the same verb is right, and only a reader can tell.

**Wired as review step 3f (draft) and book step 7i.** Drive DELEXICAL toward the book's own
rate, not to zero — a light verb on a concrete object is often exactly right.

## Measured

| corpus | DELEXICAL rate | DEAD count | note |
|---|---|---|---|
| **the book** | **0.7%** of sentences (39) | 124 | the baseline |

**The DEAD count runs high on purpose.** Most of its 124 subjects are concrete and fine, which
is why the tier is surfaced rather than graded — the instrument does not get to decide which
*runs* or *sits* is fake-concrete, any more than it clears an absolute in `telling.py`.

## The house rule

**A buried verb is a defect; a dead verb is a candidate.** Run `light_verb.py` on every draft.
Recover the DELEXICAL verbs; read the DEAD ones and finish the thought where the subject cannot
do the verb. **This makes four instruments built from a defect Wendell caught by eye** — after
`fragment.py`, `trailing_and.py`, and `telling.py`. The pattern holds: the catch becomes a
measurement, and the measurement runs before the draft reaches him.

## Sourcing

**Read as search-result extracts, not primary texts.** `github.com` (write-good, proselint,
editsaurus), `grafana.com` and the craft-blog hosts (kindlepreneur, matt.might) are blocked by
this environment's egress proxy, so the tool inventory and the word lists come through search
summaries. **The linguistics core is the solid part** — the delexical-verb category is stable
across the Wikipedia and British Council entries, which agree on the same six verbs.

- [Wikipedia, *Light verb*](https://en.wikipedia.org/wiki/Light_verb)
- [British Council, *Delexical verbs: have, take, make, give, go, do*](https://learnenglish.britishcouncil.org/grammar/english-grammar-reference/delexical-verbs-have-take-make-give-go-do)
- [write-good](https://github.com/btford/write-good) · [proselint](https://github.com/amperser/proselint) · [proselint study (Suchow et al.)](https://suchow.io/assets/docs/pacer2016proselint.pdf)
- [Vale](https://vale.sh/) · [Vale rules, Grafana Writers' Toolkit](https://grafana.com/docs/writers-toolkit/review/lint-prose/rules/)
- [matt.might, *Shell scripts for passive voice, weasel words, duplicates*](https://matt.might.net/articles/shell-scripts-for-passive-voice-weasel-words-duplicates/)
- Williams, *Style: Lessons in Clarity and Grace* — put the action in the verb (already in `EDITORIAL_AUTHORITIES`)
