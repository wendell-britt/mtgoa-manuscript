# -*- coding: utf-8 -*-
"""sweep_p5_land_2 -- DL-99, tranche 2. `land` in the reception sense leaves the book.

Wendell, 2026-09-10, on being shown that the P5 row is 59 sites while the word is 103: *"all of
it."*

Tranche 1 (DL-98) took the 29 sites where `land` carried a manner word. This takes the rest of
the reception sense across chapters, appendices, back matter: **41 spans.** What is left is the
locative, and it is left deliberately.

**26 SITES ARE KEPT AND THEY ARE THE POINT OF THE DISTINCTION.** `land` is a real verb when
something falls somewhere and the somewhere matters:

  - *"a decision lands on the person with the least power to absorb it"* -- the image is the
    argument, and it recurs on purpose at ch1:127.
  - *"The cost lands on the people the design is for"*, and its two siblings in ch7 and ch8.
  - *"name where a feeling landed in the body"*, *"locate where it landed"*, *"You noticed where
    it landed in your body"* -- the Shaman's whole method is locating a charge somewhere.
  - *"the machine reads where the ball landed"* -- skeeball, literally.
  - *"the shape of a term is the same wherever you land"* -- a traveller's letter.
  - *"a hey, I hope that landed okay sent three hours later"* -- the book quoting the hedge it is
    criticising. Rewriting it would fix the person the book is describing.

**Three identical sentences needed context to declare.** *"The message landed."* stands three
times in ch3 -- the taught line a reader says to their own nervous system, and the last surviving
site on the P6 refrain row. All three become *"You got through."*, which is what the sentence
meant: the feeling delivered something and it arrived.

    python3 instruments/sweep_p5_land_2.py
"""
import io, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ruling import guard
from _p5_edits2 import E, APPX

CLAIM = "DL-99"
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)
EDITS = ([(os.path.join(ROOT, "manuscript", f), o, n) for f, o, n in E]
         + [(os.path.join(ROOT, f), o, n) for f, o, n in APPX])


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
    print("P5 tranche 2 applied: %d span(s) across %d file(s)" % (len(EDITS), len(staged)))

    import re, glob
    V = re.compile(r"\b(lands?|landed|landing)\b")
    files = [p for p in sorted(glob.glob(os.path.join(ROOT, "manuscript", "ch*.md")))
             + sorted(glob.glob(os.path.join(ROOT, "appendices", "APPENDIX_[A-I]*.md")))
             + sorted(glob.glob(os.path.join(ROOT, "front_matter", "*.md")))
             + sorted(glob.glob(os.path.join(ROOT, "back_matter", "*.md")))
             if "backup" not in p]
    left = sum(len(V.findall(io.open(p, encoding="utf-8").read())) for p in files)
    print("'land' remaining in the shipping set: %d (want 26, all locative and named in the "
          "docstring)" % left)


if __name__ == "__main__":
    main()
