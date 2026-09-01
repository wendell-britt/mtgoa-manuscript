# -*- coding: utf-8 -*-
"""
trailing_and.py — Strunk's loose sentence, counted, with the ranking tag broken out.

    python3 instruments/trailing_and.py DRAFT.md [...]   # draft mode, one row per file
    python3 instruments/trailing_and.py                  # the book, as the baseline
    python3 instruments/trailing_and.py -v               # every site

## Why this exists

Wendell, 2026-09-01, on a sentence of mine: *"this trailing 'and' construction needs to go. I
don't want to see it anymore in any writing that I want to have generated."*

The construction is a comma, a coordinating conjunction, and a second independent clause.
**Strunk named it in 1918** and Rule 14 bans a run of them — *"loose sentences of a particular
type, those consisting of two co-ordinate clauses, the second introduced by a conjunction or
relative."* His replacement list ends on the line that is the whole diagnosis: choose
*"whichever best represent the real relations of the thought."*

**`and` represents no relation.** Every other connective commits — `because` to cause, `once`
to sequence, `though` to concession. `and` says only *here is another one*, so reaching for it
is declining to say how two ideas relate.

See `specs/RESEARCH_TRAILING_AND_2026-09-01.md` for the styles where parataxis is craft rather
than tic, and for the eight repairs.

## Measured before it was written, which is why the thresholds are real

    documents I generated, two weeks     206 / 806 sentences    25.6%
    the manuscript, hand scan            980 / 6407 sentences   15.3%
    the manuscript, by this file         783 / 5643 sentences   13.9%
    DECISION_FUNNEL, written that day     17 / 41               41%

**The book is the baseline and it is not zero.** A single loose sentence is unexceptionable —
Strunk says so — and a corpus at 0% would be a different mechanical voice rather than a better
one. **The target is the manuscript's own rate.**

## Two tiers, because reading the hits showed two habits

**LOOSE** — the general case. A candidate, scored as a rate against the book's 13.9%.

**RANK** — the ranking tag: a set asserted, then a member ranked in a trailing clause.
*"Two errors, and the second is worse than the first."* *"There is now a third, and it is the
strongest of them."* **Twenty-three of these in two weeks of my output**, most of them the
literal string `, and it is the` plus a superlative.

**RANK is a defect rather than a candidate, and the reason is not grammatical.** It announces a
hierarchy instead of enacting one. If the second item is worse, lead with it or put it in the
stress position; saying so in a trailing clause is telling the reader about an ordering the
paragraph declined to build. **It also flatters** — the same move `/no-ai-slop` bans as
faux-insight, arriving through grammar rather than vocabulary, which is why `slop_shapes.py`
never saw it.

## What it cannot decide

Whether a given loose sentence is the right structure. Deliberate polysyndeton — the King
James cadence, Hemingway's iceberg — is this exact shape used on purpose, and the instrument
cannot tell intent from habit. **It reports a rate.** A rate at the book's baseline is a voice;
a rate at 25% is a tic.
"""
import io, os, re, sys, importlib.util
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    argv, sys.argv = sys.argv, [name]
    try:
        spec.loader.exec_module(mod)
    finally:
        sys.argv = argv
    return mod


fl = _load("find_line", os.path.join(HERE, "find_line.py"))
dl = _load("draft_lines", os.path.join(HERE, "draft_lines.py"))

SENT = re.compile(r"(?<=[.!?])\s+")

# Strunk's own list of connectives, minus the relatives. `who/which/when/where/while` are in
# Rule 14 too and are left out here on purpose: in this book they are overwhelmingly
# restrictive, and counting them would bury the coordinators under ordinary relative clauses.
JOIN = re.compile(r",\s+(and|but|or|so|yet)\s+(?=\w)", re.I)

# Does what follows the conjunction look like an independent clause? A subject within a few
# words, then a finite verb. Crude on purpose -- the alternative is a tagger, and `fragment.py`
# already records what a tagger costs on single sentences.
FINITE = re.compile(
    r"^(?:\w+[\w'-]*\s+){0,4}\b(is|are|was|were|has|have|had|does|do|did|will|would|can|could|"
    r"should|must|may|might|\w{3,}s|\w{3,}ed)\b", re.I)

# The ranking tag. A trailing coordinate clause whose whole content is where a member sits in
# an ordering. `, and it is the strongest of them.`
RANK = re.compile(
    r",\s+(?:and|but)\s+(?:the\s+|these\s+|that\s+|this\s+|it\s+|they\s+)?(?:\w+\s+){0,3}"
    r"\b(?:is|are|was|were)\s+(?:not\s+)?(?:the\s+|a\s+)?(?:\w+\s+){0,2}"
    r"(strongest|weakest|worst|best|hardest|easiest|sharpest|cheapest|biggest|smallest|"
    r"only|real|serious|better|worse|first|second|third|last|load-bearing|"
    r"useful|important|expensive|dangerous|interesting|surprising)\b"
    # `most`/`least` only in superlative position -- `the most likely one`, not `most people`.
    r"|,\s+(?:and|but)\s+(?:\w+\s+){0,4}\b(?:is|are|was|were)\s+(?:not\s+)?the\s+"
    r"(?:most|least)\b", re.I)

# Measured 2026-09-01 by this file on the book's own body prose: 770 LOOSE + 13 RANK across
# 5,643 sentences. An earlier hand scan said 15.3% because it counted headings and tables too;
# this is the number the instrument itself produces, which is the one to hold new prose to.
BOOK_BASELINE = 13.9


def sites(text):
    """[(tier, sentence)] for one block of prose, plus the sentence count."""
    out = []
    sents = [" ".join(s.split()) for s in SENT.split(text)]
    sents = [s for s in sents if len(s.split()) > 4]
    for s in sents:
        if RANK.search(s):
            out.append(("RANK", s))
            continue
        for m in JOIN.finditer(s):
            if FINITE.match(s[m.end():m.end() + 70]):
                out.append(("LOOSE", s))
                break
    return out, len(sents)


def main():
    verbose = "-v" in sys.argv
    paths = dl.paths_from(sys.argv[1:])
    if paths:
        groups = [(os.path.basename(p), dl.prose(dl.surfaces([p]))) for p in paths]
    else:
        groups = [("the book", [l for l in fl.surfaces() if l["surface"] == "body"
                                and not l["text"].lstrip().startswith(("#", "|", ">", "-", "*"))])]

    print("trailing coordination — Strunk Rule 14. RANK is a defect; LOOSE is a rate")
    print("%-24s %6s %6s %7s %8s" % ("file", "LOOSE", "RANK", "sents", "rate"))
    print("-" * 56)
    bad, rows = 0, []
    for label, lines in groups:
        hits, n = [], 0
        for l in lines:
            h, c = sites(l["text"])
            hits += [(t, s, l) for t, s in h]
            n += c
        loose = sum(1 for t, _s, _l in hits if t == "LOOSE")
        rank = sum(1 for t, _s, _l in hits if t == "RANK")
        rate = 100.0 * (loose + rank) / max(n, 1)
        flag = "" if rate <= BOOK_BASELINE + 3 else "  HEAVY"
        print("%-24s %6d %6d %7d %7.1f%%%s" % (label[:24], loose, rank, n, rate, flag))
        bad += rank + (1 if flag else 0)
        rows += hits
    print("-" * 56)
    print("book baseline %.1f%% of sentences. Zero is a different tic, not a better voice."
          % BOOK_BASELINE)

    shown = [r for r in rows if r[0] == "RANK"] + [r for r in rows if r[0] == "LOOSE"]
    if shown:
        print("")
        for tier, s, l in (shown if verbose else shown[:12]):
            print("  %-5s %s:%d" % (tier, os.path.basename(l["rel"]), l["line"]))
            print("      > %s" % s[:130])
        if not verbose and len(shown) > 12:
            print("  … %d more, run with -v" % (len(shown) - 12))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
