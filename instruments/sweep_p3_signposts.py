# -*- coding: utf-8 -*-
"""sweep_p3_signposts -- DL-103. The book stops narrating its own structure.

Wendell, 2026-09-10: *"sweep the p3 signposts."* The marks, 2026-09-09: *"Hold these three
words, because the whole book turns on them"*, *"This chapter is the threshold map"*, *"The
deeper truth is this:"*, *"Chapter 3 gives you both"*, *"and Chapter 9 tells that part"*,
*"Appendix G says where."*

**29 spans. Three shapes, and the third is the one I would have argued about.**

  1. **The book announcing its own chapters.** *"So Chapter 3 does two jobs"*, *"what this
     chapter trains"*, *"this chapter is unusual in the book"*. The reader is inside the chapter;
     telling her which chapter she is in is the writer checking their own outline in public. **The
     ch7/ch8 duplicate goes with it** -- *"Every move in this chapter is an instrument for making
     that sentence true"* stood word-for-word in both, and now differs in both.
  2. **`What follows is`.** Five sites, including two in appendices.
  3. **The reader steered to an appendix.** *"Appendix G says where to read them / her / him /
     each one"* -- five sites, plus *"Appendix I lays them all out."* **Every one is a source
     credit with a navigation tail, and the credit survives without the tail.** The names stay in
     the sentence; only the instruction to go elsewhere goes.

**The one I nearly kept.** A cross-reference inside a reference appendix is arguably that
appendix's whole function -- a bibliography that cannot name chapters cannot work. That is the
same shape of argument that kept fifteen `read`s and 26 `land`s, and both were overruled the same
day. So `APPENDIX_B`'s pointer changes shape and keeps its content, and `APPENDIX_G`'s own
chapter-mapping is left alone because mapping chapters to sources is the text of that appendix
rather than an aside inside another one.

**xref is the constraint that decides how far this can go.** Cutting five *Appendix G* pointers
would orphan the bibliography if nothing else referenced it. `front_matter/copyright.md` names it
twice, so it survives. `xref.py` is run after this and the result is recorded.

    python3 instruments/sweep_p3_signposts.py
"""
import io, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ruling import guard
from _p3_edits import E

CLAIM = "DL-103"
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)
EDITS = [(os.path.join(ROOT, f), o, n) for f, o, n in E]


def norm(s):
    return " ".join(s.replace("*", "").split())


def main():
    guard(CLAIM, EDITS)
    staged = {}
    for path in dict.fromkeys(p for p, _, _ in EDITS):
        staged[path] = io.open(path, encoding="utf-8").read()
    for path, old, new in EDITS:
        if staged[path].count(old) != 1:
            sys.stderr.write("REFUSED: span matched %d times (need 1) in %s.\n  %r\n"
                             % (staged[path].count(old), os.path.basename(path), old[:70]))
            sys.exit(2)
        staged[path] = staged[path].replace(old, new, 1)
    for path, text in staged.items():
        b, a = io.open(path, encoding="utf-8").read(), text
        for p, old, new in EDITS:
            if p == path:
                b = b.replace(old, "", 1); a = a.replace(new, "", 1)
        if norm(b) != norm(a):
            sys.stderr.write("REFUSED: prose changed outside the declared spans in %s.\n"
                             % os.path.basename(path)); sys.exit(3)
    for path, old, new in EDITS:
        if old in staged[path] or new not in staged[path]:
            sys.stderr.write("REFUSED: a declared edit did not take.\n  %r\n" % old[:70])
            sys.exit(4)
    for path, text in staged.items():
        io.open(path, "w", encoding="utf-8").write(text)
    print("P3 signposts swept: %d span(s) across %d file(s)" % (len(EDITS), len(staged)))
    print("run instruments/xref.py next: five Appendix G pointers were removed.")


if __name__ == "__main__":
    main()
