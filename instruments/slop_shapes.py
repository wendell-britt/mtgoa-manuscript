# -*- coding: utf-8 -*-
"""
slop_shapes.py — the part of `/no-ai-slop` a regex can do, so step 3 stops being honour-system.

    python3 instruments/slop_shapes.py DRAFT.md [...]   # draft mode, one row per file
    python3 instruments/slop_shapes.py                  # the book
    python3 instruments/slop_shapes.py -v               # every site

## Why this exists

Wendell, 2026-08-29, on marketing copy the review had reported clean: *"how are our skills
not catching this?"*

`review.py` runs code for every step but one. Step 3 prints **"run /no-ai-slop by hand,
then re-run this"** — and step 3 is the step that keeps failing. It failed by omission on
2026-08-29, when I ran one check out of one file and recorded it as the whole step, and it
fails by degree every time it is done properly, because a human reading is not repeatable.

**Roughly half of `no-ai-slop/SKILL.md` is a vocabulary list or a fixed sentence shape.**
That half is mechanical, and this file runs it. The other half — is this fragment a beat or
a claim, is this contrast real or manufactured — stays a reading, and nothing here pretends
otherwise.

## The two files this consolidates rather than duplicates

**`notstack.py`** scans for sentences opening on a negation, which is the skill's *negative
listing*. It had no argv handling at all and globbed `manuscript/ch[1-9].md` at import, so
it could never see a draft. Its pattern is imported here rather than retyped, so there is
one definition and `notstack.py` stays runnable as the sweep it was written as.

**`faux_insight.py`** cannot be wired into anything, and that is worth stating plainly
rather than filing as done. **It is not a detector.** It is a spent one-shot edit script:
four hardcoded before/after strings from 2026-08-03, already applied, that rewrite the
manuscript when run. Wiring it into a review would edit the book during a check. The
pattern it was built for — *the step most people skip* — is a rule here instead, and the
original file stays as the record of what was changed and why.

## The rules, and what each one is worth

| rule | from the skill | confidence |
|---|---|---|
| `BANNED` | *delve, foster, leverage, tapestry, paradigm shift…* | high — a vocabulary list |
| `PUFFERY` | *stands as a testament, marks a pivotal moment, plays a vital role* | high |
| `WEASEL` | *experts agree, studies show, widely regarded as* | high |
| `THROAT` | *Here's the thing, Let me be clear, The uncomfortable truth is* | high |
| `FAUXINSIGHT` | *the part most people skip, what nobody tells you* | high |
| `RECAP` | *In conclusion, Ultimately, Overall* as a paragraph opener | high |
| `SUPERFICIAL` | a trailing `, highlighting/underscoring/reflecting` clause | high |
| `BINARY` | *It's not X, it's Y* / *The question isn't X, it's Y* | medium — the shape is also how you rank two real things |
| `NEGLIST` | two or more sentences in a row opening on a negation | medium — `notstack.py`'s target |
| `EMPTYPHRASE` | *it's worth noting, at the end of the day, in order to* | medium — the skill says keep some |

**Medium means a candidate, not a finding.** `BINARY` in particular fires on the book's own
always-on constraint: *ranking rather than denying* produces a two-part contrast on purpose,
and `ANALYSIS_SALES_PAGE` §2 rated one of them the sharpest line in the description. It is
printed so the decision is recorded rather than skipped.

## What it deliberately does not check

**Colon reveals** and **em dashes**, both of which the skill names. Colons are how this book
introduces every list and every gloss, so the rule would fire hundreds of times on correct
prose. Em dashes already have `emdash.py` and a ratcheting budget.
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

# notstack.py's pattern, imported rather than retyped, so there is one definition of what
# counts as a negative opener and `notstack.py` stays runnable as the sweep it was written
# as. It scans the manuscript and prints a board at import -- it is a script, not a module
# -- so the import runs with stdout swallowed. A first attempt scraped the pattern out of
# the source with a regex and broke on the apostrophe in `Don\'t`, which is what scraping
# source instead of importing it earns.
class _Quiet(object):
    def write(self, *_a): pass
    def flush(self): pass


_so, sys.stdout = sys.stdout, _Quiet()
try:
    _ns = _load("notstack", os.path.join(HERE, "notstack.py"))
finally:
    sys.stdout = _so
NEG_START = _ns.NEG_START

SENT = re.compile(r"(?<=[.!?])\s+")

# EXEMPTIONS, in gate.py's shape: (rule, phrase, reason). A hit inside one of these spans
# is dropped. Kept as a list rather than woven into the patterns so the reason travels with
# the exemption, which is the thing that stops a later pass "fixing" prose already ruled on.
EXEMPT = [
    ("BANNED", "leverage point",
     "Donella Meadows' term of art, used throughout ch6 and credited on the copyright "
     "page: *Thinking in Systems* and \"Leverage Points: Places to Intervene in a System.\" "
     "Twenty of the twenty-two book-wide BANNED hits on the first run were this term, "
     "and the copyright page's own citation of the paper was another."),
]


def exempt_spans(text, rule):
    """gate.py's mechanism, same shape, so an exemption reads the same in both files.

    Matched case-insensitively, unlike gate.py's, because the exempted phrase here is a
    cited title and appears in three cases -- `leverage points`, `Leverage points` in the
    copyright page's italicised gloss, `Leverage Points` in the paper's title.
    """
    spans, low = [], text.lower()
    for name, phrase, _reason in EXEMPT:
        if name != rule:
            continue
        p = phrase.lower()
        i = low.find(p)
        while i >= 0:
            spans.append((i, i + len(p)))
            i = low.find(p, i + 1)
    return spans


RULES = [
    ("BANNED", re.compile(
        r"\b(delve[sd]?|delving|foster(s|ed|ing)?|leverag(e|es|ed|ing)|utiliz(e|es|ed|ing)"
        r"|facilitat(e|es|ed|ing)|empower(s|ed|ing)?|streamlin(e|es|ed|ing)|robust"
        r"|cutting-edge|paradigm shift|game changer|tapestry|realm|beacon|multifaceted"
        r"|meticulous|intricate|paramount|transformative|elevat(e|es|ed|ing)|embark(s|ed|ing)?"
        r"|supercharge|harness(es|ed|ing)?|ever-evolving)\b", re.I)),
    ("PUFFERY", re.compile(
        r"\b(stands? as a testament|marks? a pivotal|plays? a vital role"
        r"|solidif(y|ies|ied) its position|underscor(e|es|ing) its significance"
        r"|this is huge|this changes everything)\b", re.I)),
    ("WEASEL", re.compile(
        r"\b(experts agree|industry reports suggest|many argue|widely regarded as"
        r"|studies show|research shows|it is widely)\b", re.I)),
    ("THROAT", re.compile(
        r"(?:^|(?<=[.!?]\s))\s*(Here's the thing|Here's what I mean|Let me be clear"
        r"|I'll be honest|The uncomfortable truth is|Let's dive in|Think about it)", re.I)),
    ("FAUXINSIGHT", re.compile(
        r"\b(most people skip|nobody tells you|what most people get wrong"
        r"|the part everyone misses|nobody gets|the training nobody|what nobody)\b", re.I)),
    ("RECAP", re.compile(
        r"(?:^|(?<=[.!?]\s))\s*(In conclusion|Ultimately|Overall|At the end of the day)\b")),
    ("SUPERFICIAL", re.compile(
        r",\s+(highlighting|underscoring|reflecting|showcasing|demonstrating|signaling)\b",
        re.I)),
    ("BINARY", re.compile(
        r"\b(it'?s not (?:just )?[^.,;]{1,40}[,.] it'?s|the question isn'?t [^.,;]{1,40}[,.] it'?s"
        r"|not (?:just )?[^.,;]{1,40}, but(?: rather)? )", re.I)),
    ("EMPTYPHRASE", re.compile(
        r"\b(it'?s worth noting|it'?s important to note|when it comes to|at its core"
        r"|in today'?s world|in the age of|in the world of|the reality is|the truth is"
        r"|in terms of|with regard to|going forward|in this article)\b", re.I)),
]

# The skill's own words for each rule, printed beside a hit so the fix is on screen.
FIX = {
    "BANNED": "banned vocabulary — say the plain word",
    "PUFFERY": "state the fact, let the reader judge whether it matters",
    "WEASEL": "name the source or cut the claim",
    "THROAT": "cut the opener and state the point",
    "FAUXINSIGHT": "flatters the writer as the lone expert — make the claim stand alone",
    "RECAP": "the reader was just there — end on the last concrete point",
    "SUPERFICIAL": "an -ing clause pretending to explain meaning — say the consequence",
    "BINARY": "state Y directly, unless this is ranking rather than denying",
    "NEGLIST": "negative listing — just say the thing it is",
    "EMPTYPHRASE": "delays the point — cut unless it is his spoken rhythm",
}


def sites(text):
    """(rule, matched text) for one line, plus the multi-sentence NEGLIST rule."""
    out = []
    for name, pat in RULES:
        skip = exempt_spans(text, name)
        for m in pat.finditer(text):
            if any(a <= m.start() < b for a, b in skip):
                continue
            out.append((name, " ".join(m.group(0).split())[:70]))
    # NEGLIST needs sentence boundaries, so it cannot be one of the RULES patterns.
    # gate.py's `stacks` counter already catches `Not X. Not Y.` where the FIRST sentence
    # opens on `Not`; this catches the family where it opens on any negation.
    clean = [re.sub(r"[*_`]", "", s).strip() for s in SENT.split(text)]
    run = []
    for s in clean:
        if NEG_START.match(s):
            run.append(s)
        else:
            if len(run) >= 2:
                out.append(("NEGLIST", " ".join(run)[:70]))
            run = []
    if len(run) >= 2:
        out.append(("NEGLIST", " ".join(run)[:70]))
    return out


def main():
    verbose = "-v" in sys.argv
    paths = dl.paths_from(sys.argv[1:])
    lines = dl.prose(dl.surfaces(paths)) if paths else [
        l for l in fl.surfaces() if l["surface"] == "body"]

    rows = []
    for l in lines:
        for name, s in sites(l["text"]):
            rows.append((l, name, s))

    print("slop shapes — the mechanical half of /no-ai-slop. See the module docstring")
    print("%-22s %6s   %s" % ("file", "hits", "rules"))
    print("-" * 62)
    per = defaultdict(lambda: defaultdict(int))
    for l, name, _s in rows:
        per[os.path.basename(l["rel"])][name] += 1
    keys = [os.path.basename(p) for p in paths] if paths else sorted(per)
    for k in keys:
        r = per[k]
        n = sum(r.values())
        print("%-22s %6d   %s" % (k[:22], n,
                                  " ".join("%s:%d" % (a, b) for a, b in sorted(r.items()))))
    if rows:
        print("")
        for l, name, s in (rows if verbose else rows[:15]):
            print("  %-12s %s:%d — %s" % (name, os.path.basename(l["rel"]), l["line"], FIX[name]))
            print("      > %s" % s)
        if not verbose and len(rows) > 15:
            print("  … %d more, run with -v" % (len(rows) - 15))
    # Book-wide this is a board to work, so it prints a total and exits 0, the same
    # contract `empty_head.py` and `ranking.py` have. On a draft the exit code is the
    # signal `review.py` uses to decide whether to print the sites, so it is 1 on any hit.
    print("")
    print("TOTAL %d site(s) across %d file(s) — %s"
          % (len(rows), len({os.path.basename(l["rel"]) for l, _n, _s in rows}),
             "fix before it lands" if paths else "reporting only"))
    return (1 if rows else 0) if paths else 0


if __name__ == "__main__":
    sys.exit(main())
