# -*- coding: utf-8 -*-
"""Paragraphs that ship more than once.

Written 2026-08-07, after three of them were found by accident. Renaming ch3's
Move 5 meant reading every site of a phrase, and two lines apart sat the same
paragraph twice:

    ch3:125/127  the Shaman's "means" line, two variants
    ch6:107/109  the Architect's, differing only in villagers/village
    ch7:82/84    the Diplomat's, byte-identical twins

All three arrived through merges. **All three passed `gate`, `diet`, the em-dash
budget, the seam sweep, the citation audit, round-trip and `shipcheck` while
shipping twice.** Round-trip is the check you would assume catches it and does
not: it verifies the marginalia frame does not alter the body, never that the
body says anything once.

## Why near-duplicates and not just exact ones

Only one of the three was byte-identical. ch6's pair differed by a single word
and ch3's by an opening clause, which is the signature of a merge that kept both
sides of a conflict rather than resolving it. An exact-match check would have
found one of three.

## Why there is a length floor

The book repeats deliberately and often: move names, the five-move recaps, the
`*You're winning when:*` frame, the Tell. Those are structure, not duplication.
Below `MIN_WORDS` the false-positive rate makes the board unreadable, which is
the failure `ranking.py` had on its first run and had to be narrowed out of.

    python3 instruments/dupes.py           # the board
    python3 instruments/dupes.py -v        # both copies of every pair
"""
import re, io, os, sys, glob
from difflib import SequenceMatcher

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)

MIN_WORDS = 25      # below this the recaps and frames drown the signal
NEAR = 0.90         # ch6's pair scored one word apart; ch3's an opening clause apart

SURFACES = ["manuscript/ch*.md", "appendices/APPENDIX_[A-H]*.md",
            "front_matter/*.md", "back_matter/*.md"]


def norm(p):
    """Compare what a reader hears, not what the file holds."""
    p = re.sub(r"[*_`>#]", "", p)
    return re.sub(r"\s+", " ", p).strip().lower()


def paragraphs(path):
    text = io.open(path, encoding="utf-8").read()
    line = 1
    for block in text.split("\n\n"):
        n = line
        line += block.count("\n") + 2
        s = block.strip()
        if s and not s.startswith(("|", "---", "#")) and len(s.split()) >= MIN_WORDS:
            yield n, s


def main():
    verbose = "-v" in sys.argv
    rows = []
    for pat in SURFACES:
        for path in sorted(glob.glob(os.path.join(ROOT, pat))):
            name = os.path.basename(path)
            for n, s in paragraphs(path):
                rows.append((name, n, s, norm(s)))

    # SAME FILE ONLY, both tiers. The first run reported 34 EXACT pairs and every one
    # was cross-chapter: the shared frames each Face chapter carries by design -- the
    # deck explanation, the 3-2-1 instructions, the recap forms. Those are structure.
    # All three real defects were same-file and within a few lines of each other,
    # because that is what a merge that kept both sides of a conflict leaves behind.
    exact, near = [], []
    for i, (f, n, s, k) in enumerate(rows):
        for f2, n2, s2, k2 in rows[i + 1:]:
            if f2 != f or abs(n2 - n) > 400:
                continue
            if k2 == k:
                exact.append(((f, n, s), (f2, n2, s2)))
            elif SequenceMatcher(None, k, k2).ratio() >= NEAR:
                near.append(((f, n, s), (f2, n2, s2)))

    print("paragraphs that ship more than once\n")
    print("  EXACT %3d   identical after normalising emphasis and whitespace" % len(exact))
    print("  NEAR  %3d   >=%d%% similar and within 400 lines — the merge signature"
          % (len(near), int(NEAR * 100)))

    if verbose:
        for label, pairs in (("EXACT", exact), ("NEAR", near)):
            for a, b in pairs:
                print("\n  [%s] %s:%d  and  %s:%d" % (label, a[0], a[1], b[0], b[1]))
                print("      %s…" % a[2][:110].replace("\n", " "))
                print("      %s…" % b[2][:110].replace("\n", " "))

    total = len(exact) + len(near)
    print("\n%d pair(s) — %s" % (
        total, "clean" if not total else "read both copies before cutting either"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
