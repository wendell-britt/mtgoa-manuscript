# -*- coding: utf-8 -*-
"""treatise_open -- DL-85. Frame the treatise where the reader enters it, in all six chapters.

Wendell, 2026-09-09, ruling the candidate: *"Rule DL-85, frame the treatise entry in all six
chapters."*

The mark was on the ch3 signature (proof p.62), and the signature is not the defect. It is the
first place a reader learns whose voice they have been reading for three sections, so the line
that closes the treatise was carrying the work of the line that never opened it. Six exits
attributed; six entries did not.

**This does not undo the 2026-07-30 move.** What came off the top then was the full byline —
*"submitted by Corin Ash, Master of the Clean No"* — and it came off because a submitted document
is signed at the end of itself. That argument is untouched and the signatures stay where they are.
What goes on top now is a document header: the treatise and the school, never the person and never
"submitted by". A filed document carries both, and the name still arrives only at the signature.

**The other half of this ruling was designed on 2026-07-30 and never built.** `SPEC_TWO_HANDS`
§*"The convention gets explained once, in front matter"* specifies a short note in
`front_matter/copyright.md`, and its own open-questions list carried it as item 3, unsigned-off.
Without it the header reads as decoration; with it the reader knows what a treatise is, whose
voice it is in, and that the signature marks the turn. Both halves land together or neither works.

    python3 instruments/treatise_open.py
"""
import io, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ruling import guard                       # FR-E1: two lines and one import

CLAIM = "DL-85"                                # the ruled fact in instruments/claims.yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)
ANCHOR = "<!-- SECTION 1 -->"

# The six entry points DL-85 censused. Chapter number to header, matching
# marginalia/insertions.py TREATISE_OPEN, which is where compile.py reads them from.
EDITS = [
    (3, "THE FIRST TREATISE · THE SCHOOL OF THE BODY"),
    (4, "THE SECOND TREATISE · THE SCHOOL OF THE LINE"),
    (5, "THE THIRD TREATISE · THE SCHOOL OF THE OATH"),
    (6, "THE FOURTH TREATISE · THE SCHOOL OF THE PATTERN"),
    (7, "THE FIFTH TREATISE · THE SCHOOL OF THE BRIDGE"),
    (8, "THE SIXTH TREATISE · THE SCHOOL OF THE HORIZON"),
]


def block(text):
    body = "\n".join("> " + l if l.strip() else ">" for l in text.split("\n"))
    return "<!-- TREATISE-OPEN -->\n%s\n<!-- /TREATISE-OPEN -->\n\n" % body


def main():
    guard(CLAIM, EDITS)                        # FR-E3: refuses unless the census is covered

    # Read and check every chapter before writing any of them. Atomic, matching the tranche
    # contract: a half-applied ruling is the defect this whole apparatus exists to prevent.
    staged = []
    for ch, header in EDITS:
        path = os.path.join(ROOT, "manuscript", "ch%d.md" % ch)
        text = io.open(path, encoding="utf-8").read()
        if "<!-- TREATISE-OPEN -->" in text:
            sys.stderr.write("ch%d already carries a treatise header; nothing written\n" % ch)
            sys.exit(2)
        c = text.count(ANCHOR)
        if c != 1:
            sys.stderr.write("ch%d: anchor matched %d times (need 1); nothing written\n" % (ch, c))
            sys.exit(2)
        i = text.index(ANCHOR)
        staged.append((path, text[:i] + block(header) + text[i:]))

    for path, text in staged:
        io.open(path, "w", encoding="utf-8").write(text)
    print("treatise header placed in %d chapters" % len(staged))


if __name__ == "__main__":
    main()
