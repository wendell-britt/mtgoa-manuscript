# -*- coding: utf-8 -*-
"""cut_cards_residue -- the six card references the section cut did not reach (2026-09-09).

ch4-ch8 each close their Tell with the same instruction ch3 did: log the answer "on the
card". ch7's chapter recap lists "the Diplomat's twenty cards". Companion to
cut_cards_ch3.py / cut_cards_ch4_9.py. Every edit is asserted to match exactly once.
    python3 instruments/cut_cards_residue.py
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

EDITS = {
4: [("goes on the card in writing", "goes in your log in writing")],
5: [("goes on the card in writing", "goes in your log in writing")],
6: [("goes on the card in writing", "goes in your log in writing")],
7: [("goes on the card in writing", "goes in your log in writing"),
    ("- The Diplomat's twenty cards, and the superpower they are for: Connector, connection that has survived being told the truth",
     "- The Diplomat's superpower: Connector, connection that has survived being told the truth")],
8: [("goes on the card in writing", "goes in your log in writing")],
}

def main():
    for ch, edits in EDITS.items():
        p = os.path.join(MS, "ch%d.md" % ch)
        t = io.open(p, encoding="utf-8").read()
        for old, new in edits:
            c = t.count(old)
            if c != 1:
                sys.stderr.write("ch%d: EDIT matched %d times (need 1): %r\n" % (ch, c, old[:70]))
                sys.exit(2)
            t = t.replace(old, new)
        io.open(p, "w", encoding="utf-8").write(t)
        print("ch%d: %d edits applied" % (ch, len(edits)))

if __name__ == "__main__":
    main()
