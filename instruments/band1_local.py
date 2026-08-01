# -*- coding: utf-8 -*-
"""
Band 1, the second pass: the five findings the reports marked `fix locally`.

The first pass took the ten errors the manuscript settles by itself and left fourteen.
Re-reading the reports rather than my summary of them, five of those fourteen carry the
disposition **fix locally**, not `structural decision`. They needed a correct sentence,
not a ruling, and holding them back was over-caution on my part.

The nine that remain all carry `structural decision` (or, in one case, are a false
positive) and are not touched here.
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

E = [
    # CH2 C3 -- ch2's best-taught unit ends by promising that the next chapter takes up
    # what sets the Protector off and how to steer it. ch3's up-close daemon is the
    # Controller; `Protector` appears once in ch3 and only inside the Controller's
    # definition. What ch3 does teach is reading the channels, and the Protector runs on
    # Metal/Fear -- so the promise is repointed at what is actually there rather than cut.
    ("ch2.md",
     "That speed has kept you alive, and you want to keep it. The next chapter takes up "
     "what sets it off and how you learn to steer it.",
     "That speed has kept you alive, and you want to keep it. The next chapter teaches "
     "you to read the fear channel it runs on, which is where steering it starts."),

    # CH3 C7 -- the term is defined twice, differently, 119 lines apart, and the two
    # definitions are opposite failures: silent sensing here, saying only the correct
    # words at the later site. The later one is the operative definition -- the four
    # domains and the App Layer both run on it -- so this site keeps the observation and
    # gives up the name.
    ("ch3.md",
     "Feeling without Function is the whole awareness trap worn by one person: endless "
     "sensing, nothing done.",
     "Feeling without Function is endless sensing, nothing done."),

    # CH8 CN-3 -- canon removes the gate walk from ch4-ch8, and this is the only
    # occurrence of `gate` in ch8, doing positional work in the daemon recap. A reader
    # with no gates in ch4-ch8 has nothing to count back from. The ordinal survives; the
    # gate does not.
    ("ch8.md",
     "You met the Damaged Self deep in the Forest, seventh in line, one gate before the "
     "center.",
     "You met the Damaged Self deep in the Forest, seventh in line, closest to the "
     "center."),

    # CH8 CN-5 -- the chapter names four games twice ("Power, strategy, harmony,
    # whole-board", at two sites) and counts six twice. Six is the number of Faces, and
    # the chapter insists elsewhere that a game is not a Face. The count is what is wrong.
    ("ch8.md",
     "Holding six games at once without collapsing into any of them.",
     "Holding all four games at once without collapsing into any of them."),
    ("ch8.md",
     "It requires knowing all six games well enough to move between them",
     "It requires knowing all four games well enough to move between them"),

    # CH8 CN-7 -- `diagnosis` is the chapter's own name for the Diagnostician's shadow
    # ("Diagnosis becomes lecturing", and "Say it as an offering rather than as a
    # diagnosis or a verdict"). Using it here as the healthy pole of a named test inverts
    # the instruction for any reader who took the other two seriously. The test survives;
    # the word it turns on changes to the one the chapter already uses for the healthy
    # side, at the same site: offering.
    ("ch8.md",
     "*This is a power-game table* said with the energy of a diagnosis is service.",
     "*This is a power-game table* said with the energy of an offering is service."),
]


def main():
    files, bad = {}, []
    for i, (name, old, new) in enumerate(E, 1):
        files.setdefault(name, io.open(os.path.join(MS, name), encoding="utf-8").read())
        n = files[name].count(old)
        if n != 1:
            bad.append("#%d %s matched %d times: %r" % (i, name, n, old[:56]))
            continue
        files[name] = files[name].replace(old, new, 1)
    if bad:
        print("ABORTED, nothing written:")
        for b in bad:
            print("  " + b)
        return 1
    if "--dry" not in sys.argv:
        for name, t in files.items():
            io.open(os.path.join(MS, name), "w", encoding="utf-8").write(t)
    print("%d edit(s) %s across %d file(s)"
          % (len(E), "checked" if "--dry" in sys.argv else "applied", len(files)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
