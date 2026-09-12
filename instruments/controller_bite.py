# -*- coding: utf-8 -*-
"""controller_bite -- item 7 of the proof-mark panel, the C1 Controller contradiction (2026-09-09).

ch3 Section 5 had the shadow Controller ending the Form "before Stage One, by ruling that the
feeling never had permission in the first place." The daemon section says the rule bites in a
single place, Open Up, and ch4-ch8 say five times that the Controller decides how you behave
once inside, not whether you go in (the Protector's gate). Panel Round 5, six of six: Section 5
changes; the daemon section stands.
    python3 instruments/controller_bite.py
"""
import io, os, sys

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "manuscript", "ch3.md")

OLD = ("The shadow Controller is the part that can end the whole practice before Stage One, "
       "by ruling that the feeling never had permission in the first place.")
NEW = ("The shadow Controller is the part that can end the whole practice at the second move, "
       "by ruling that a feeling you have already had may not show.")

def main():
    t = io.open(P, encoding="utf-8").read()
    c = t.count(OLD)
    if c != 1:
        sys.stderr.write("anchor matched %d times (need 1)\n" % c); sys.exit(2)
    io.open(P, "w", encoding="utf-8").write(t.replace(OLD, NEW))
    print("Controller bite point: Section 5 now agrees with Where the Daemon Bites")

if __name__ == "__main__":
    main()
