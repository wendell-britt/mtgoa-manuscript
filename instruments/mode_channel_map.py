# -*- coding: utf-8 -*-
"""
The mode-to-channel mapping, assessed against the Lean OS priority ladder.

Wendell's question: *"Does this improve Jordan's life? Does this make it easier for her
to show up as an effective ally? Or is it something she has to memorize that she's not
going to be able to keep up?"*

That question splits what looked like one problem into two kinds, and they score
oppositely:

**A table she looks things up in is not a thing she memorizes.** It can be large and
cost her nothing, as long as it is right. A wrong lookup is worse than no lookup. So
ch5's table -- which promises "a specific EA signal" per mode and then returns the same
answer for two of them, while Metal/Fear never appears in the chapter at all -- is a
concrete reader problem. She arrives at the Regent carrying fear, which is the likeliest
thing to be carrying about an inheritance, and the chapter has nothing for her. Fixed.

**A claim about the architecture is recall with nothing attached.** "Five modes, five
channels, no overlap" is that, and ch4 says the quiet part: it "explains why the modes
number five rather than three." That answers a question the author had, not one Jordan
has. It is also false in two of five chapters. Cut, rather than made true by forcing two
chapters to fit -- three deletions instead of five forced edits, and the system ends up
honest instead of tidy.

The surrounding sentences in all three sites do real reader-facing work and are kept.
Only the boast goes.

**Not done here: ch7's Field-Holder row.** See the report.
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

E = [
    # -- ch5: the broken lookup. Keeper of Vows takes the unused channel. -------
    # Custodian is locked to Earth by its own prose ("the Neutral channel's heaviness"),
    # so by elimination the Keeper of Vows is the Metal/Fear mode -- and it fits rather
    # than merely filling a hole. Dogma is what fear does to a vow: hold the form and you
    # cannot lose the thing. Faithfulness is the discernment that survives the fear.
    ("ch5.md",
     "| **The Keeper of Vows** | Earth/Neutrality | Dogma → Faithfulness |",
     "| **The Keeper of Vows** | Metal/Fear | Dogma → Faithfulness |"),

    ("ch5.md",
     "**The Keeper of Vows** (Earth/Neutrality): Honoring commitment across time, when "
     "no one watches, becomes the silent practice. Dogma (the rote performance of "
     "loyalty) alchemizes into faithfulness (the lived commitment). The Keeper does not "
     "need to be seen. The Keeper needs to be steady. The Neutral channel's stillness "
     "becomes the foundation for everything else the Regent builds.",
     "**The Keeper of Vows** (Metal/Fear): Honoring commitment across time, when "
     "no one watches, becomes the silent practice. Dogma (the rote performance of "
     "loyalty, and what fear does to a vow: hold the form and you cannot lose the "
     "thing) alchemizes into faithfulness (the lived commitment). The Keeper does not "
     "need to be seen. The Keeper needs to be steady. The Metal channel's discernment "
     "becomes the foundation for everything else the Regent builds."),

    # -- ch4, ch6, ch8: the boast goes, the working sentences stay. --------------
    ("ch4.md",
     "Five modes, five channels, no overlap. That tidiness is no coincidence: it "
     "explains why the modes number five rather than three. Each one names a different "
     "signal in the body asking to be spent a different way.",
     "Each mode names a different signal in the body asking to be spent a different way."),

    ("ch6.md",
     "Five modes, five channels, no overlap. That accounts for five modes rather than "
     "three, and it answers the question this chapter gets asked most often: how a Face "
     "whose native material is logic belongs in a book built on emotional alchemy.",
     "The mapping answers the question this chapter gets asked most often: how a Face "
     "whose native material is logic belongs in a book built on emotional alchemy."),

    ("ch8.md",
     "Five modes, five channels, no overlap. The Sage's practice runs the full spectrum",
     "The Sage's practice runs the full spectrum"),
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
