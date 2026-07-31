# -*- coding: utf-8 -*-
"""
The Vulnerable Child ruling — Wendell, 2026-07-31.

> *"The vulnerable child is the player. This means they should be in the 9th chapter
> and they are the ones who have befriended the daemons in a way that they are now
> able to use them as allies to show up for people more effectively."*

This dissolves three Band 1 findings rather than fixing them, because **the book was
never wrong -- it was unnamed**. ch2 already says all of it:

  ch2:296  "Seven daemons live in the Forest, and the player at its center is you.
            You're not here to slay these daemons but to befriend them, one by one,
            until the parts that have been running you are working for you instead."
  ch2:434  "at the center, the youngest part of you still waits: the player, the one
            who should have been holding it the whole time."
  ch2:436  "The whole walk is reaching her ... putting the joystick back in her hands."

The figure, the word *player*, and the befriending arc are all in place. What is missing
is the name, which is why ch8:230 and ch9:508 read as references to a retired term.

  CH8 CN-1  "This is the Vulnerable Child's gift, held all the way up" -- correct, and
            now has an antecedent.
  CH9 C2    "Eight gates, eight questions" -- correct. Seven daemons plus the player at
            the centre is eight, which is also what APPENDIX_C_KEY_TERMS already says:
            "Vulnerable Child -- The eighth gate -- the destination behind all seven."
  CH2 C2    "the centre is defined twice, incompatibly" (Band 3) -- it is defined once.
            "The player at its center is you" and "the youngest part of you ... the
            player" are the same claim. The Child is not an eighth daemon; she is who
            the seven were taking turns standing in for.

Two edits, both small, plus one roster consistency fix that rode along in CH9 C2.
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

E = [
    # The name, seated where the figure already is.
    ("ch2.md",
     "Underneath all of it, at the center, the youngest part of you still waits: the "
     "player, the one who should have been holding it the whole time.",
     "Underneath all of it, at the center, the youngest part of you still waits: the "
     "Vulnerable Child, the player who should have been holding it the whole time."),

    # ch9's gate scan names the Fixer where the ch2 roster names the Fixer/Healer. The
    # report logged this as riding along with the count; it is a straight roster fix.
    ("ch9.md",
     "*The Fixer showed up in your building",
     "*The Fixer/Healer showed up in your building"),
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
    print("%d edit(s) %s" % (len(E), "checked" if "--dry" in sys.argv else "applied"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
