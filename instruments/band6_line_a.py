# -*- coding: utf-8 -*-
"""
Band 6, LINE — first pass. Five findings whose evidence is still on the page and whose
fix the manuscript settles by itself.

A note on the band, because the titles mislead. Seventeen of the thirty-nine LINE
findings carry `AWAITS STRUCTURAL RULING` in their titles, which suggests they belong in
Band 2. They do not: `rescan.rank()` reads the **Disposition** field, and on every one of
them it reads `fix locally`. Checked on CH1 L1 and CH6 L1 directly. The title marker is
stale annotation from an earlier pass.

  CH6 L1  a doubled article, "the The Emotional Body"
  CH7 L4  a malformed possessive, "one sentence' worth of time"
  CH9 L6  sentence-initial `bars-engine` against the chapter's own capitalisation, which
          uses `Bars-engine` in that position four times
  CH4 S5  a forward-pointer that arrives immediately. "(One of those three stops you.
          We're going to get there.)" promises distance, and the thing it promises is
          the next section
  CH3 S5  the five-move summary listed two moves the chapter never taught. Its items
          three and four, "Ask for the unreduced version" and "Spend the read inside the
          window", correspond to nothing; the chapter's Moves 2 and 4 are Turn the Dial
          Up and Say What You Can Do Now. The summary now runs the five in Move order.
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

E = [
    ("ch6.md",
     "it is the whole racket: the The Emotional Body is being *employed.*",
     "it is the whole racket: the Emotional Body is being *employed.*"),

    ("ch7.md",
     "stay there for one sentence' worth of time without answering",
     "stay there for one sentence's worth of time without answering"),

    ("ch9.md",
     "The village is the people already building. bars-engine works as more than a solo "
     "project",
     "The village is the people already building. Bars-engine works as more than a solo "
     "project"),

    # The parenthetical promises a later arrival for something that arrives in the next
    # section. Naming the one that stops people does the same work without the promise.
    ("ch4.md",
     "Very few people can do all three without flinching. (One of those three stops you. "
     "We're going to get there.)",
     "Very few people can do all three without flinching, and the third is where most "
     "people stop."),

    ("ch3.md",
     "That is the Shaman's game. Five moves. Catch it before the story rewrites it. Name "
     "the channel where people can hear it. Say the thing under the thing. Ask for the "
     "unreduced version. Spend the read inside the window.",
     "That is the Shaman's game. Five moves. Catch it before the story rewrites it. Turn "
     "the dial up instead of down. Name the channel out loud. Say what you can do now. "
     "Say the thing under the thing."),
]


def main():
    files, bad = {}, []
    for name, old, new in E:
        files.setdefault(name, io.open(os.path.join(MS, name), encoding="utf-8").read())
        n = files[name].count(old)
        if n != 1:
            bad.append("%s: matched %d times — %r" % (name, n, old[:58]))
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
