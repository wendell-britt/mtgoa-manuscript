# -*- coding: utf-8 -*-
"""alchemist_scaffold -- give the Alchemist its category, after the parable's payoff (2026-09-09).

Wendell: "The alchemist as a superpower intro just needs scaffolding and probably an appendix
to breakdown all the superpowers." The first scaffold (scratch, never applied) put a taxonomy
in front of the payoff and said "seven"; the hostile review rejected both. This one goes after
"where it can move the water", names the category without a count, ties every superpower to
the same alchemy, and points at Appendix I.
    python3 instruments/alchemist_scaffold.py
"""
import io, os, sys

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "manuscript", "ch3.md")

OLD = "all aimed at one outcome: one true sentence, out of your body and into the world, where it can move the water.\n"
NEW = ("all aimed at one outcome: one true sentence, out of your body and into the world, where it can move the water.\n"
       "\n"
       "The Alchemist is a superpower, the one this chapter trains, and that is a different kind of name from the Faces. A Face is a role at the table. A superpower is the capacity you built to survive, made usable for somebody else, and every one of them runs on the same alchemy: a live charge, spent. The Alchemist is the one who leads with it. Appendix I lays them all out.\n")

def main():
    t = io.open(P, encoding="utf-8").read()
    c = t.count(OLD)
    if c != 1:
        sys.stderr.write("anchor matched %d times (need 1)\n" % c); sys.exit(2)
    io.open(P, "w", encoding="utf-8").write(t.replace(OLD, NEW))
    print("Alchemist scaffold placed after the parable's payoff")

if __name__ == "__main__":
    main()
