# -*- coding: utf-8 -*-
"""
W8 batch A — the three defects Wendell found by reading ch5 Section 1, applied
book-wide now that the detectors can see them.

  · 3 banned plural "rooms" (gate.py now reads \\brooms?\\b)
  · 8 sentence-initial "Which is/was" fragments (review.py now reads the
    post-terminal position, not only the comma tail)
  · the two em-dash denials in the same ch5 passage Wendell quoted

Abort-before-write: nothing is written unless every anchor matches exactly once.

    python3 marginalia/compile.py --strip     # must already be stripped
    python3 instruments/w8_batch_a.py
"""
import io, os, sys

MS = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "manuscript")

EDITS = {
"ch2.md": [
    # banned: rooms
    ("the same pattern surfacing in different rooms, with different people, wearing different faces",
     "the same pattern surfacing in a different building, with different people, wearing different faces"),
],
"ch5.md": [
    # banned: rooms
    ("I've spent most of my adult life in rooms where that reads as a threat.",
     "I've spent most of my adult life in movements where that reads as a threat."),
    ("Careful things, the kind you say in rooms allergic to structure.",
     "Careful things, the kind you say to a group allergic to structure."),
    # em-dash denial — Wendell quoted this one
    ("Not because they forgot — because structure was suspect.",
     "They had decided structure was suspect."),
    # em-dash denial in the same paragraph
    ("The way you can feel a building that's going to fail — not because of the people in it but because no floor holds them up.",
     "The way you can feel a building that's going to fail. The people inside are fine. No floor holds them up."),
    # em-dash denial + "Which is" fragment, both in the line Wendell quoted
    ("The ones who wanted the crown usually sought someone to give themselves to. They weren't receiving the tradition — they were looking for a patriarch. Which is its own kind of problem.",
     "The ones who wanted the crown were looking for a patriarch to give themselves to, and a patriarch does its own kind of damage."),
],
"ch1.md": [
    ("I was staying in integrity. Which was all true, and also meant the guilt had nowhere to go.",
     "I was staying in integrity. Every word of that was true, and every word of it left the guilt nowhere to go."),
    ("Look at what the payoff really buys you: safety. Which is why fear sits at the center of the work.",
     "Look at what the payoff really buys you. It buys safety, so fear sits at the center of the work."),
],
"ch4.md": [
    ("Which is why the move is not argument.",
     "That is why the move never argues."),
    ("Which is why nobody catches the shadow in the act.",
     "So nobody catches the shadow in the act."),
],
"ch6.md": [
    ("and stops attending. Which is the only version of this that outlives the Architect's interest in it.",
     "and stops attending. Only that version outlives the Architect's interest in it."),
],
"ch7.md": [
    ("Which is why the shadow hides inside the act.",
     "So the shadow hides inside the act."),
],
"ch8.md": [
    ("To validate. To see. Which is a form of participation.",
     "To validate. To see. Holding space participates in it."),
],
}


def main():
    staged, bad = [], []
    for name, pairs in EDITS.items():
        p = os.path.join(MS, name)
        t = io.open(p, encoding="utf-8").read()
        for a, b in pairs:
            n = t.count(a)
            if n != 1:
                bad.append((name, n, a[:64]))
            else:
                t = t.replace(a, b, 1)
        staged.append((p, t))
    if bad:
        print("ABORT — anchors not unique, nothing written:")
        for name, n, a in bad:
            print("  %s  %d matches: %r" % (name, n, a))
        return 1
    for p, t in staged:
        io.open(p, "w", encoding="utf-8").write(t)
    print("applied %d edits across %d files" % (sum(len(v) for v in EDITS.values()), len(EDITS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
