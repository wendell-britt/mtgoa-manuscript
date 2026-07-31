# -*- coding: utf-8 -*-
"""
Band 1's last two. Neither needed a new rule; both needed a parent named.

**CH9 C3 — the WAVE has six beats in ch9 and five everywhere else.**

The deck settles it before any argument does. A hundred and twenty BARs is five moves
crossed against four domains across six Faces, and ch9 states that arithmetic itself at
line 169 and line 694, eighty lines either side of the sites that count six. A sixth
stage would need a card row that does not exist.

So `Come back` is not a WAVE stage. It is what you do after a pass, and it is what makes
the pass repeat, which is a different and larger claim than being sixth in a list. The
fix marks it as following the five rather than joining them, at the three sites that
present it as a member.

`ch9:480`'s bold **Come back.** is untouched. That one opens the chapter's closing
passage on the return, which is ch9's own theme and makes no claim about the WAVE.

**CH8 CN-4 — a four-move ordered sequence, the only one left in the book.**

Canon reads: *"Every stage sequence is five beats. There are no four-stage models left in
the book."* The Walk Back is not a stage sequence. It is a drill inside the fifth stage of
See → Switch → Serve → Release → Return, and the section already calls it a drill in its
first line. What made it read as a rival was the framing sentence, which announced four
moves immediately after a five-stage sequence without saying which stage they belong to.

Naming the parent costs three words and invents no fifth move. Padding a working practice
to satisfy a numbering convention is the memorisation tax cut earlier tonight, applied to
the author instead of the reader.
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

E = [
    # CH8 CN-4 — name the parent stage.
    ("ch8.md",
     "The practice has four moves. Run them in order the first several times.",
     "Return has four moves inside it. Run them in order the first several times."),

    # CH9 C3 — three sites, all of which list Come back as a member of the five.
    ("ch9.md",
     "You now know the WAVE. Wake up. Open up. Clean up. Grow up. Show up. Come back.",
     "You now know the WAVE. Wake up. Open up. Clean up. Grow up. Show up. Then you come "
     "back, and coming back is what turns one pass into a practice."),

    ("ch9.md",
     "Show up: do the next version. Come back: notice what shifted.",
     "Show up: do the next version. Then come back: notice what shifted."),

    ("ch9.md",
     "not from the reactive place the old habit would have sent you to. Come back: "
     "notice what happened, what shifted, what you learned.",
     "not from the reactive place the old habit would have sent you to. Then come back: "
     "notice what happened, what shifted, what you learned."),
]


def main():
    files, bad = {}, []
    for name, old, new in E:
        files.setdefault(name, io.open(os.path.join(MS, name), encoding="utf-8").read())
        n = files[name].count(old)
        if n != 1:
            bad.append("%s: matched %d times — %r" % (name, n, old[:60]))
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
    print("%d edit(s) %s" % (len(E), "checked" if "--dry" in sys.argv else "applied"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
