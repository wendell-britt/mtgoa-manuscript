# -*- coding: utf-8 -*-
"""article.py -- a definite article standing over a noun the reader was never given.

Wendell, 2026-09-09, on a draft that had passed every counter: *"'the true sentence.' also a
definite article failure. 'the true one'"* and then, on the rule: *"if it can be said without it
it should be rewritten unless it's doing the specific things in our rules which I notice aren't
firing for these revisions."*

He was right that nothing fired. `empty_head.py` asks whether a HEAD NOUN is empty -- `thing`,
`part`, `piece`. **Nothing asked whether a definite article was earning its place over a
perfectly good noun**, so a whole defect class was invisible and a green board reported over it.

    python3 instruments/article.py                 # the book
    python3 instruments/article.py FILE [FILE...]  # named files
    python3 instruments/article.py -v              # every site, with context

## The rule this tests

`MANUSCRIPT_FILE_CANON` and the review skill: **`the X` is a presupposition.** It tells the
reader *you already know which one I mean*, and it is legal four ways -- an antecedent, a
referent unique in the world, a clause that supplies it on the spot, or canon the book has
taught her. When none holds, the grammar asserts shared knowledge that was never established.

## Two tiers, and why not a third

**PRO** -- `the [adjective] one`. The head is a pro-form carrying nothing and the adjective is
doing all the identifying work. *"Allyship is saying the true one"*, `ch3:693`. Deictics and
ordinals are excluded, because *the next one*, *the other one*, *the third one* point at
something the sentence just counted and are ordinary English.

**ADJ** -- `the [evaluative adjective] [noun]` where the phrase does not occur in the preceding
260 characters. *"the beautiful words"*, *"the correct response"*, *"the real work"*. Lower
precision than PRO, because some are named concepts the book capitalises and some are licensed
by a context this cannot see. **It reports; it does not grade.**

**The wide version was built first and thrown away.** Flagging every `the + noun` with no
antecedent within two paragraphs, no supplying clause, and not on a canon list produced **455
hits in ch3 alone** -- *on the surface*, *in the sand*, *the way a house gets colder*. That is
noise, and a check that cries 455 times gets switched off. Recorded so nobody rebuilds it.

## What it cannot do

It cannot tell a deliberate quotation of a social phrase from a lapse. *"the certainty that you
are one of the good ones"* is the book quoting a thing people believe about themselves, and it
looks identical to a defect. **Every hit is a candidate for a reader, which is why this reports
and does not gate.**
"""
import io, os, re, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)

# Pointing at something the sentence just counted. Ordinary English, never a finding.
DEICTIC = set("""first second third fourth fifth sixth seventh last next other only same
previous latter former one another either neither""".split())

# An adjective asked to carry a noun. Evaluative, not descriptive: `the red door` identifies,
# `the right door` presupposes that the reader knows which one counts as right.
EVAL = (r"true|truer|truest|right|correct|real|honest|good|better|best|bad|worse|worst|wrong|"
        r"beautiful|palatable|reasonable|difficult|easy|proper|actual|genuine|clean|safe|kind|"
        r"hard|harder|stated|obvious|useful|cheap|expensive|gracious|conscientious|angry|cold|"
        r"warm|nice|polite|brave|smart|clever|serious|important|necessary")

PRO = re.compile(r"\bthe\s+([a-z]+)\s+(ones?)\b", re.I)
ADJ = re.compile(r"\bthe\s+(" + EVAL + r")\s+([a-z]{3,})\b", re.I)
LOOKBACK = 260          # characters; a phrase named this recently is licensed by its antecedent


def sites(text):
    """(tier, phrase, offset) for every site in one file's text."""
    out = []
    for m in PRO.finditer(text):
        if m.group(1).lower() in DEICTIC:
            continue
        out.append(("PRO", m.group(0), m.start()))
    for m in ADJ.finditer(text):
        # A capitalised head is a named concept the book owns -- the Right Thing, the Wrong Game.
        if m.group(2)[:1].isupper():
            continue
        if m.group(0).lower() in text[max(0, m.start() - LOOKBACK):m.start()].lower():
            continue
        out.append(("ADJ", m.group(0), m.start()))
    return sorted(out, key=lambda r: r[2])


def corpus():
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("profile", os.path.join(HERE, "profile.py"))
        prof = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(prof)
        globs = prof.corpus(["manuscript/ch*.md"])
    except Exception:
        globs = ["manuscript/ch*.md"]
    out = []
    for g in globs:
        out += sorted(glob.glob(os.path.join(ROOT, g)))
    return out


def line_of(text, off):
    return text.count("\n", 0, off) + 1


def main():
    verbose = "-v" in sys.argv
    paths = [a for a in sys.argv[1:] if not a.startswith("-")] or corpus()

    print("definite articles standing over a noun the reader was not given\n")
    print("%-30s %6s %6s %8s" % ("file", "PRO", "ADJ", "/1k"))
    print("-" * 54)
    tp = ta = words = 0
    detail = []
    for p in paths:
        try:
            text = io.open(p, encoding="utf-8").read()
        except IOError:
            continue
        rows = sites(text)
        pro = sum(1 for r in rows if r[0] == "PRO")
        adj = len(rows) - pro
        n = len(text.split())
        tp += pro; ta += adj; words += n
        print("%-30s %6d %6d %8.2f"
              % (os.path.basename(p), pro, adj, 1000.0 * len(rows) / n if n else 0))
        for tier, phrase, off in rows:
            detail.append((os.path.basename(p), line_of(text, off), tier, phrase,
                           " ".join(text[max(0, off - 44):off + len(phrase) + 30].split())))
    print("-" * 54)
    print("%-30s %6d %6d %8.2f"
          % ("TOTAL", tp, ta, 1000.0 * (tp + ta) / words if words else 0))

    show = detail if verbose else [d for d in detail if d[2] == "PRO"][:12]
    if show:
        print("")
        for f, ln, tier, phrase, ctx in show:
            print("  %-9s %s:%-5d %-22s …%s…" % (tier, f, ln, phrase, ctx[:88]))
    if not verbose and ta:
        print("\n  %d ADJ site(s) not shown. Re-run with -v." % ta)

    print("\nreporting only. Every hit is a candidate for a reader: the book quoting a social"
          "\nphrase looks identical to a lapse. PRO is the high-precision tier.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
