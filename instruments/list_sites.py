# -*- coding: utf-8 -*-
"""
Dump every denying-negation and 'which is' site with file, line, and the whole
sentence around it, so the fixes can be drafted against real context instead of
the 60-character window review.py prints.

    python3 instruments/list_sites.py denying
    python3 instruments/list_sites.py which
"""
import io, os, re, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")
sys.path.insert(0, os.path.join(HERE, os.pardir, "marginalia"))
import review as R


def sites(pat, label):
    out = []
    for f in sorted(glob.glob(os.path.join(MS, "ch*.md")),
                    key=lambda p: int(re.search(r"ch(\d+)", p).group(1))):
        t = io.open(f, encoding="utf-8").read()
        for m in re.finditer(pat, t):
            line = t.count("\n", 0, m.start()) + 1
            a = t.rfind("\n", 0, max(0, m.start() - 200))
            b = t.find("\n", m.end())
            out.append((os.path.basename(f), line, t[a + 1:b if b > 0 else len(t)].strip()))
    return out


def main():
    which = sys.argv[1] if len(sys.argv) > 1 else "denying"
    pat = (R.DENYING_GENERAL if which == "denying"
           else r"(?i)(?:,\s*|(?<=[.!?])\s+)which\s+(?:is|was|are|were)\b")
    for i, (f, ln, ctx) in enumerate(sites(pat, which), 1):
        print("\n--- %02d  %s:%d" % (i, f, ln))
        print(ctx)
    return 0


if __name__ == "__main__":
    sys.exit(main())
