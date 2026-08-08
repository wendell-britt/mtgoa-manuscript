# -*- coding: utf-8 -*-
"""Denying negations that the sentence-level counters cannot see.

Written 2026-08-07. `marginalia/specs/REVISION_INSTRUMENT.md` Part 1 carries the
constraint: **ranking, not denying — a negation is legal only if the negated
thing is still true at the end of the sentence.** Two instruments already look
for it and both need sentence boundaries:

    marginalia/review.py   "denying negation (X is not A. X is B)"
    gate.py `stacks`       r'\\bNot [^.!?]{1,60}[.!?]\\s+(Not|Never|No)\\b'

**Both walk straight past the fragment form**, because a fragment has no finite
verb and often no terminal punctuation before the replacement arrives:

    Not willpower, not determination: the raw energy of pushing back.

That shipped at `ch4:226` and `ch4:234` and neither instrument has ever flagged
it. It was found by Wendell reading three sentences I had just written — *"Not x
but y is sneaking in"* — after they scored BLOCK 0 on the linter and PASS on the
gate. Measured on that draft: **four denying negations against two** in the three
sentences they were written to join.

## Why this reports rather than gates

`empty_head.py`'s note applies unchanged: promote to `gate.py` after the sweep,
not before. **HARD is 2 sites and SOFT is ~26**, and several of the SOFT ones are
legitimate — a reason swap (*not because it's perfect, but because removing it
would break something*) denies one reason and supplies another, which is how
reasons work. A hard gate on that would be wrong.

## The tiers

**HARD** — the doubled fragment, `Not A, not B:`. No finite verb, two things
denied, a colon, a replacement. There is no reading of this that ranks.

**SOFT** — bare `, not A, but B`. The classic denial-and-replace. Rules as a
candidate rather than a defect, because the form has legal uses.

**EXEMPT and counted separately** — `not just / not only / not merely / not
simply A, but B`. This is the ranking form and it is what the constraint asks
for: A stays true and B is added on top. Reported so the ratio of ranking to
denying is visible, which is the number that actually matters.

    python3 instruments/ranking.py          # the board
    python3 instruments/ranking.py -v       # every site with context
"""
import re, io, os, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

RANKERS = ("just", "only", "merely", "simply")

HARD = re.compile(r"Not\s+\w[^.!?:]{0,40},\s*not\s+\w[^.!?:]{0,40}:")
SOFT = re.compile(r",\s*not\s+(\w+)[^.!?]{0,45},\s*but\s")


def scan(paths):
    hard, soft, rank = [], [], []
    for p in paths:
        name = os.path.basename(p)
        for i, line in enumerate(io.open(p, encoding="utf-8"), 1):
            for m in HARD.finditer(line):
                hard.append((name, i, m.group(0).strip()))
            for m in SOFT.finditer(line):
                bucket = rank if m.group(1) in RANKERS else soft
                bucket.append((name, i, m.group(0).strip()))
    return hard, soft, rank


def main():
    verbose = "-v" in sys.argv
    named = [a for a in sys.argv[1:] if not a.startswith("-") and os.path.isfile(a)]
    paths = named or sorted(glob.glob(os.path.join(MS, "ch*.md")),
                            key=lambda f: int(re.search(r"ch(\d+)", os.path.basename(f)).group(1)))
    hard, soft, rank = scan(paths)

    print("denying negations — a negation is legal only if the negated thing")
    print("is still true at the end of the sentence\n")
    print("  HARD  %3d   doubled fragment + colon, 'Not A, not B:'" % len(hard))
    print("  SOFT  %3d   bare ', not A, but B' — candidates, not verdicts" % len(soft))
    print("  RANK  %3d   'not just/only/merely A, but B' — the legal form" % len(rank))
    total = len(soft) + len(rank)
    if total:
        print("\n  ranking : denying = %d : %d" % (len(rank), len(soft)))

    if verbose:
        for label, rows in (("HARD", hard), ("SOFT", soft), ("RANK", rank)):
            for name, i, txt in rows:
                print("  [%s] %s:%d  %s" % (label, name, i, txt))

    # SOFT has legal uses -- a reason swap denies one reason and supplies another,
    # which is how reasons work -- so each one is a ruling, not a defect. The last
    # line is the one review.py quotes, so it carries the numbers.
    print("\nHARD %d · SOFT %d · ranking:denying = %d:%d — reporting only, "
          "promote HARD after the sweep" % (len(hard), len(soft), len(rank), len(soft)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
