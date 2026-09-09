# -*- coding: utf-8 -*-
"""marks_ch3_t8 -- proof marks, ch3 pp.61 and 65 marginalia (wrapped blockquotes), every
entry changed (2026-09-09). Same rule and contract as marks_ch2_t1.py.
    python3 instruments/marks_ch3_t8.py
"""
import io, os, sys

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "manuscript", "ch3.md")

EDITS = [
# p.61 -- the Polarity aside
("> *Watch for the point where you get good at this and it becomes enough.*",
 "> *Watch for the point where being good at this starts to feel like enough.*"),
("That is a real skill, rarer than it sounds, and\n> each accurate read will feel like an accomplishment. It is not one. A read that never becomes\n> a move is a very sophisticated way of standing still, and I have watched people build whole\n> careers in that spot and be admired the entire time.*",
 "That is a real skill, rarer than it sounds.\n> Each accurate reading will feel like an accomplishment, and a reading that never becomes\n> a move is a very sophisticated way of standing still. People build whole careers in that\n> spot and are admired the entire time.*"),
# p.65 -- the Maera aside
("on\n> your own time, and they are where the training actually happens.",
 "on\n> your own time, where the training actually happens."),
]

def main():
    t = io.open(P, encoding="utf-8").read()
    for old, new in EDITS:
        c = t.count(old)
        if c != 1:
            sys.stderr.write("EDIT matched %d times (need 1): %r\n" % (c, old[:70]))
            sys.exit(2)
        t = t.replace(old, new)
    io.open(P, "w", encoding="utf-8").write(t)
    print("ch3 tranche 8: %d edits applied" % len(EDITS))

if __name__ == "__main__":
    main()
