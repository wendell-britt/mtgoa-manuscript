# -*- coding: utf-8 -*-
"""controller_bite_para -- the C1 fix, done to the paragraph instead of one sentence (2026-09-09).

`controller_bite.py` changed one sentence inside a paragraph whose other three sentences argue
the opposite. Wendell, on the result: *"'at the second move, by ruling that a feeling you have
already had may not show' -- nonsense sentence."* He is right, and the reason is structural: the
paragraph's engine was the entry metaphor (allowed onto the field / called out of bounds at the
whistle / made it into play), so a corrected sentence about a feeling you have already had sat in
a paragraph insisting the feeling never arrived.

This replaces the whole paragraph on the ruling the panel already reached (Round 5, six of six):
the Controller lets the feeling in and bites at Open Up. Three further things fall out.

  - The stage arithmetic was wrong in my draft. Open Up is the second move, so three moves come
    after it, not four. The paragraph now names them.
  - "This hand keeps the Shaman's instrument, sensitivity, in its case" was a proof mark (p.78)
    and is also the second telling of ch3:317's "an instrument kept behind glass reads nothing."
    A marked line that repeats an unmarked one four hundred lines earlier gets cut, not reworded.
  - "You cannot alchemize a charge you never let yourself have" would have been ch3:230 verbatim.
    Written as "cut off halfway" instead.

    python3 instruments/controller_bite_para.py
"""
import io, os, sys

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "manuscript", "ch3.md")

OLD = ("Here is why this daemon stands second, right behind the one that keeps you alive, in a book "
       "about allyship. Everything you learned in the first half of this chapter runs on a feeling "
       "being allowed onto the field. You cannot alchemize a charge that got called out of bounds at "
       "the whistle. Wake, Open, Clean, Grow, Show: every stage assumes the feeling made it into "
       "play. The shadow Controller is the part that can end the whole practice at the second move, "
       "by ruling that a feeling you have already had may not show. This hand keeps the Shaman's "
       "instrument, sensitivity, in its case. You pay twice:")

NEW = ("Here is why this daemon stands second, right behind the one that keeps you alive, in a book "
       "about allyship. Everything you learned in the first half of this chapter runs on a feeling "
       "being allowed to finish. You cannot alchemize a charge you cut off halfway. The shadow "
       "Controller lets the feeling in and stops it at Open Up. It rules on your conduct rather than "
       "on the charge: *not where anyone can see you.* So you manage the feeling instead of "
       "undergoing it. Clean Up, Grow Up and Show Up get nothing to work with. You pay twice:")


def main():
    t = io.open(P, encoding="utf-8").read()
    c = t.count(OLD)
    if c != 1:
        sys.stderr.write("anchor matched %d times (need 1)\n" % c); sys.exit(2)
    io.open(P, "w", encoding="utf-8").write(t.replace(OLD, NEW))
    print("C1 paragraph rebuilt on the Open Up bite point")


if __name__ == "__main__":
    main()
