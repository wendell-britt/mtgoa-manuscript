# -*- coding: utf-8 -*-
"""
Move Wendell's memoir out of Voss's treatise and into his own half of ch3.

Wendell ruled 2026-07-30 that a marked heading does not repair a membrane breach, because
any framing that licenses the author being inside the document makes him a character:
"we haven't really solved the note before the concept problem... It breaks the fiction for
Jordan if this is the case. Is it possible to move this below the handbook and treatise,
across the book."

So the rule is absolute. **Above the signature, only the Head. Below it, only Wendell.**

What moves: seventeen lines in ch3's Section 3, from "I used to be very good at putting
feelings away" through the allyship turn that ends "What it is." The customer service years,
the tightening in his chest, a real book, and the game he invented.

Why the lift is clean: the block sits between two sentences that already join.

    "Emotional alchemy is the practice of STAYING in relationship with..."   (before)
    "The Shaman's practice is THAT STAYING."                                 (after)

The second refers to the first, not to the memoir, so the argument closes over the gap with
its antecedent intact.

Where it lands: the head of Section 4, immediately after the question Section 4 opens with
-- "how do you actually *do it* when you're in the middle of a hard conversation" -- because
the memoir is the answer to that question. Question, then the story of learning the answer,
then the WAVE-Spiral as the technique. It reads better there than it did where it was.

    python3 instruments/ch3_memoir_move.py --dry
    python3 instruments/ch3_memoir_move.py
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CH3 = os.path.join(HERE, os.pardir, "manuscript", "ch3.md")

START = "I used to be very good at putting feelings away."
END = "That requires staying with the feeling long enough to find out what it actually is. Not what you want it to be. What it is."
AFTER = ("If emotional alchemy means learning from emotions instead of managing them, then "
         "how do you actually *do it* when you're in the middle of a hard conversation, a "
         "crisis, a moment where the feeling is rising and you have thirty seconds to respond?")


def main():
    dry = "--dry" in sys.argv
    t = io.open(CH3, encoding="utf-8").read()

    for name, s in (("START", START), ("END", END), ("AFTER", AFTER)):
        if t.count(s) != 1:
            raise SystemExit("%s anchor matched %d times, expected 1" % (name, t.count(s)))

    i = t.find(START)
    j = t.find(END) + len(END)
    block = t[i:j].strip()

    # The block must not contain a frame block: moving one would orphan its anchor.
    for kind in ("<!-- MARGINALIA", "<!-- SIGNATURE", "<!-- EPIGRAPH"):
        if kind in block:
            raise SystemExit("a frame block sits inside the memoir; strip first")

    rest = (t[:i] + t[j:]).replace("\n\n\n\n", "\n\n")
    k = rest.find(AFTER) + len(AFTER)
    out = rest[:k] + "\n\n" + block + rest[k:]

    if dry:
        print("block: %d chars, %d words" % (len(block), len(block.split())))
        print("first line: %s" % block.split("\n")[0][:90])
        print("last line:  ...%s" % block.split("\n")[-1][-90:])
        print("\nthe join the lift leaves behind:")
        n = rest.find("The Shaman's practice is that staying.")
        print("  ...%s" % " ".join(rest[max(0, n - 210):n + 40].split()))
        return 0

    io.open(CH3, "w", encoding="utf-8").write(out)
    print("moved %d words from Voss's treatise to the head of Section 4" % len(block.split()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
