# -*- coding: utf-8 -*-
"""
Split ch8's author Note: the memoir goes to ch9, the thesis stays with Orr.

`## A Note Before the Exile` was doing three jobs at once, and only one of them could
leave. The memoir -- the course built out of spite, George Floyd, the ten percent
completion rate, the depression well -- is Wendell's and sits above Orr's signature. The
last two paragraphs are the chapter's thesis and its scope statement, and Orr can say both.

Wendell ruled 2026-07-30: the memoir goes to ch9, and "The book in your hands came from
the bottom of that well" travels with it.

**Why ch9 and not below ch8's own seam.** ch9 is *The Return -- From Playing the Game to
Designing It*, and it already carries this story's second half: bars-engine, the sessions
that failed, the token economy rebuilt three times. The memoir is the origin of the thing
ch9 hands over. It has been told across two chapters and now it is told once.

**What stays, recast.** *"The Sage isn't the person who sees furthest. It's the person who
looked at himself long enough to stop performing the view"* is already third person about
the Face, which is exactly what `HEAD_REGISTERS` asks a Head to do. It needs no change. The
scope sentence after it needs one School swap and is then his as well. Both become ch8's
Section 1 opening, since Section 1 is The Exile and the thesis is what the exile is about.

Checked before writing: none of `NOTES[8]`'s six marginalia anchors falls inside the moved
block, so no margin note is orphaned.

    python3 instruments/ch8_note_split.py --dry
    python3 instruments/ch8_note_split.py
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

NOTE_HEAD = "## A Note Before the Exile\n"
MEMOIR_START = "The first course I built for this work, I built out of spite."
MEMOIR_END = "A game can fail to be fun, and fun on its own can fail to make a great game."
KEEPER_START = "The ones who finished changed their relationship"
THESIS = "The Sage isn't the person who sees furthest."

# ch9: the memoir lands immediately before the bars-engine paragraph, so the story runs
# origin then consequence in one place.
CH9_ANCHOR = "When I started building bars-engine, I didn't have it figured out."


def main():
    dry = "--dry" in sys.argv
    p8 = os.path.join(MS, "ch8.md")
    p9 = os.path.join(MS, "ch9.md")
    t8 = io.open(p8, encoding="utf-8").read()
    t9 = io.open(p9, encoding="utf-8").read()

    for name, s, t in (("NOTE_HEAD", NOTE_HEAD, t8), ("MEMOIR_START", MEMOIR_START, t8),
                       ("MEMOIR_END", MEMOIR_END, t8), ("KEEPER_START", KEEPER_START, t8),
                       ("THESIS", THESIS, t8), ("CH9_ANCHOR", CH9_ANCHOR, t9)):
        if t.count(s) != 1:
            raise SystemExit("%s matched %d times, expected 1" % (name, t.count(s)))

    i = t8.find(MEMOIR_START)
    j = t8.find(KEEPER_START)
    memoir = t8[i:j].strip()

    # The keeper block runs from KEEPER_START to the end of the Note (the --- rule).
    k = t8.find("\n---\n", j)
    if k < 0:
        raise SystemExit("could not find the rule closing the Note")
    keeper = t8[j:k].strip()

    for kind in ("<!-- MARGINALIA", "<!-- SIGNATURE", "<!-- EPIGRAPH", "<!-- POSTCARD"):
        if kind in memoir or kind in keeper:
            raise SystemExit("a frame block sits inside the Note; strip first")

    # "The ones who finished..." and "The book in your hands..." travel with the memoir --
    # Wendell ruled the well line goes to ch9. What stays is the thesis and the scope.
    ti = keeper.find(THESIS)
    if ti < 0:
        raise SystemExit("thesis not found inside the keeper block")
    memoir = memoir + "\n\n" + keeper[:ti].strip()
    keeper = keeper[ti:].strip().replace(
        "This chapter applies when", "The School of the Horizon applies when", 1)

    if dry:
        print("MOVES TO CH9  %d words" % len(memoir.split()))
        print("  first: %s" % memoir.split("\n")[0][:88])
        print("  last:  ...%s" % memoir.strip().split("\n")[-1][-88:])
        print("\nSTAYS IN CH8  %d words, recast as Orr" % len(keeper.split()))
        for line in keeper.split("\n"):
            if line.strip():
                print("  %s" % line[:150])
        return 0

    # ch8: the Note heading and the memoir go; the keeper opens Section 1.
    start = t8.find(NOTE_HEAD)
    t8 = t8[:start] + t8[k + len("\n---\n"):]
    s1 = t8.find("## Section 1: The Exile\n")
    if s1 < 0:
        raise SystemExit("ch8 Section 1 heading not found")
    eol = t8.find("\n", t8.find("\n", s1) + 1)      # past heading and its italic subtitle
    t8 = t8[:eol + 1] + "\n" + keeper + "\n" + t8[eol + 1:]

    m = t9.find(CH9_ANCHOR)
    t9 = t9[:m] + memoir + "\n\n" + t9[m:]

    io.open(p8, "w", encoding="utf-8").write(t8)
    io.open(p9, "w", encoding="utf-8").write(t9)
    print("ch8: Note removed, %d words of thesis kept as Orr's Section 1 opening" % len(keeper.split()))
    print("ch9: %d words of memoir landed above the bars-engine passage" % len(memoir.split()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
