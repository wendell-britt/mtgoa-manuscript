# -*- coding: utf-8 -*-
"""
Seam 1 — pull the six BAR grids out of the chapters and into the deck design surface.

Wendell 2026-07-29: "seam 1. I was hoping to use the deck architecture to generate
moves that would make sense. Taking them out makes sense, but let's keep em in the
repo as things that we can design against."

What comes out: the 5x4 table only, in ch3-ch8. Six tables, 120 cards, which is the
whole deck.

What stays, deliberately:

  · The framing paragraph. In ch3 it reads "The deck runs five basic moves, and you
    already know all five, because they are the WAVE-Spiral: Wake Up, Open Up,
    Clean Up, Grow Up, Show Up." That is the book stating its own spine, and it is
    the sentence the WAVE realignment map is built on. Cutting the table with it
    would have thrown away the design statement along with the data.
  · `### Drawing Against the Shadow`, which walks the chapter's daemon through all
    five WAVE stages in prose. That is teaching, not a lookup table.

Why the table is the right thing to cut: a 5x4 grid is a lookup surface, not a
curriculum. 20 cards per chapter across six chapters is 120 named units in a book
that carried 219 — more than half the reader's naming load sitting in tables she
was never meant to memorise. The deck is where 120 cards belong.

    python3 instruments/seam1_pull_grids.py --dry
    python3 instruments/seam1_pull_grids.py
"""
import io, os, re, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")
OUT = os.path.join(HERE, os.pardir, "deck", "BAR_GRIDS.md")

FACE = {3: "Shaman", 4: "Challenger", 5: "Regent",
        6: "Architect", 7: "Diplomat", 8: "Sage"}

HEADER = """# The Six BAR Grids — deck design surface

**Pulled from the manuscript 2026-07-29 by Wendell's ruling on Seam 1.** These are
not book content any more. They are the design surface the deck generates from, kept
in the repo on purpose so moves can be designed against the architecture.

Each grid is one Face's twenty cards: the five basic moves of the WAVE-Spiral down
the side, the four allyship domains across the top. Five times four is twenty per
Face; six Faces is the hundred and twenty in the deck.

**Why they left the book.** A 5x4 table is a lookup surface, not a curriculum.
Across six chapters these six tables were 120 of the book's 219 named units — more
than half the reader's total naming load, sitting in tables nobody was ever meant
to memorise. The chapters keep the sentence that explains where the twenty come
from, and keep `Drawing Against the Shadow`, which teaches the five stages in prose.

**Design note for whoever works here next.** The row labels carry the WAVE stage
question — *notice the signal, allow experience, identify the channel, identify
emerging capacity, choose the domain*. Those questions are the generative part. The
cell names are one pass of many at answering them.

---

"""

POINTER = ("*Your twenty live in the deck rather than on this page: five basic moves "
           "against four domains, one card per crossing. You do not have to learn "
           "them. You have to find yours, and you already know the five moves that "
           "get you there.*")


def main():
    dry = "--dry" in sys.argv
    chunks, edits, cards = [], [], 0
    for p in sorted(glob.glob(os.path.join(MS, "ch*.md")),
                    key=lambda f: int(re.search(r"ch(\d+)", os.path.basename(f)).group(1))):
        n = int(re.search(r"ch(\d+)", os.path.basename(p)).group(1))
        lines = io.open(p, encoding="utf-8").read().split("\n")
        idx = next((i for i, L in enumerate(lines)
                    if "Gather Resources | Raise Awareness" in L), None)
        if idx is None:
            continue
        table = lines[idx:idx + 7]
        # A grid is exactly a header, a separator, and five WAVE rows. Anything else
        # means the shape moved and this script must not guess.
        assert table[1].startswith("|---"), "ch%d: separator missing" % n
        assert sum(1 for r in table[2:] if r.startswith("|")) == 5, \
            "ch%d: expected 5 rows, got %d" % (n, sum(1 for r in table[2:] if r.startswith("|")))
        chunks.append("## Chapter %d — the %s\n\n%s\n" % (n, FACE[n], "\n".join(table)))
        cards += 20
        lines[idx:idx + 7] = [POINTER]
        edits.append((p, "\n".join(lines), n))
        if dry:
            print("ch%d: table at line %d, 7 lines -> pointer" % (n, idx + 1))

    assert len(edits) == 6, "expected 6 grids, found %d" % len(edits)
    if dry:
        print("\nwould pull %d grids / %d cards into deck/BAR_GRIDS.md" % (len(edits), cards))
        return 0

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    io.open(OUT, "w", encoding="utf-8").write(HEADER + "\n".join(chunks))
    for p, text, n in edits:
        io.open(p, "w", encoding="utf-8").write(text)
    print("pulled %d grids / %d cards -> deck/BAR_GRIDS.md" % (len(edits), cards))
    return 0


if __name__ == "__main__":
    sys.exit(main())
