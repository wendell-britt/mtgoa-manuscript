# -*- coding: utf-8 -*-
"""
ch3's App Layer section, drafted. DL-20 blocker one, and the last real rewrite in it.

`SPEC_REMOVE_APP_V1` line 75 had already seen the shape of it: the section is *called*
the App Layer, and its content is four self-check questions the app never needed to ask.
The app appears twice in twenty-two lines, in the heading and in one framing clause. The
four Tells, which are the section's whole value, do not mention it.

**What the app was actually doing, and what replaces it.** The framing read *"So the app
holds it. When you log the rep, it asks the one thing the marker didn't."* The app's job
was to ask, so that you could not skip a question you would rather not answer — and the
sentence immediately above says why that matters: this is *"the easiest thing in the world
to lie to yourself about."*

Paper cannot ask. It can do the other half, and the book already says so at `ch1:241`:
*"putting the thought, the feeling, the experience on a page is halfway to something."*
A written answer is one a later reader can be caught by, and ch1 promises exactly that
re-encounter: *"a year from now, you draw from it and it hands you back something you
earned once already."* So the answer goes on the card, and the reason given is the one the
book already owns.

This meets the ICA standard in `SPEC_WORKBOOK_SCOPE.md:53` — a reader without a coach
completes it alone — and it keeps the four Tells untouched.

**Heading.** `### The App Layer (the Tell)` becomes `### The Tell`. The parenthetical was
already carrying the real name. Checked for inbound references first: nothing in
`manuscript/`, `appendices/`, `front_matter/` or `back_matter/` points at the old heading.

Measured against the original, 90 words, every counter better or equal:

    be 0.92 -> 0.84   waste 1.03 -> 0.75   zombie 1.55 -> 1.40
    passive 7.50 -> 6.79   empty 1.66 -> 1.50   copula and expletive unchanged

Both heavy counters are inherited from the one sentence this pass does not touch: *"It is
also the easiest thing in the world to lie to yourself about, in the moment you most want
to be seen seeing"* carries the expletive and both passives.
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

E = [
    ("### The App Layer (the Tell)", "### The Tell"),

    ("So the app holds it. When you log the rep, it asks the one thing the marker "
     "didn't:",
     "So the answer goes on the card in writing, where a later you can read it back. "
     "When you log the rep, answer the one thing the marker didn't ask:"),
]


def main():
    p = os.path.join(MS, "ch3.md")
    t = io.open(p, encoding="utf-8").read()
    bad = []
    for i, (old, new) in enumerate(E, 1):
        n = t.count(old)
        if n != 1:
            bad.append("#%d matched %d times: %r" % (i, n, old[:56]))
            continue
        t = t.replace(old, new, 1)
    if bad:
        print("ABORTED, nothing written:")
        for b in bad:
            print("  " + b)
        return 1
    if "--dry" not in sys.argv:
        io.open(p, "w", encoding="utf-8").write(t)
    print("%d edit(s) %s" % (len(E), "checked" if "--dry" in sys.argv else "applied"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
