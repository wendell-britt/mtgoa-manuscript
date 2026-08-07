# -*- coding: utf-8 -*-
"""Move the polarity draws out of the treatise and into the author's half.

Ruled by Wendell 2026-08-01, on being shown that the draws were the only reader
practice above the treatise signature: "Do the polarity relocation."

Measured before the ruling. `**Try this now.**` appears above the signature in ch4, ch5
and ch7, and ch6 carries the same thing under the label `Situational draw`. Every other
practice in the book -- every Try It Now, every 3-2-1, every BAR, card draw and quest --
is below it. Four blocks, one exception, no rule.

The likely history: the Polarity Encounters predate the seam. SPEC_TWO_HANDS is
2026-07-30 and ch3 was already routing "First draw: Chapter 4" before it, so the
signature was placed at the close of Section 3 and the draws happened to be inside it.
`compile.py`'s seam_point already reasons the same way about the trailing italics --
"these belong to the book rather than to the Head" -- and stopped one block short.

**What splits and what stays.** Section 3 keeps the doctrine: the pair, the two poles,
the failure states, and the altitude-specific squeeze. All of that is the Head's. The
draw is a practice, so it goes where the practices are. The cut is the setup sentence
that turns doctrine into instruction -- "The draw is situational", "The draw is solo",
"The draw is relational", "only a directional diagnostic works".

**Where it lands.** As the first `###` subsection of Section 4, before the chapter's own
mechanics, so the reader finishes the doctrine, sees it signed, and opens the practice
half by drawing the axis they just read about. The new heading is the only new prose in
this pass; the draws move verbatim.

Run on stripped body text: `compile.py --strip`, this, `compile.py --apply`.
"""
import io, os

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

# ch: (start of the draw, anchor it lands before, heading, inline label to drop)
JOBS = {
    4: ("The draw is situational.",
        "### The Five Modes of Confrontation",
        "### Draw the Axis — Force ↔ Restraint", None),
    5: ("The draw is solo.",
        "### The Five Modes of Loyalty",
        "### Draw the Axis — Honor ↔ Reform", None),
    6: ("Neither pole is the answer.",
        "### EA Channel Alignment — How Each Mode Moves Energy",
        "### Draw the Axis — Structure ↔ Agency",
        "**Situational draw: Structure ↔ Agency**\n\n"),
    7: ("The draw is relational.",
        "### Channel 1 — Bridge-Builder",
        "### Draw the Axis — Care ↔ Impact", None),
}

# The trailing italics that close Section 3. They belong to the book rather than to the
# Head -- compile.py's seam_point already treats them that way -- so the draw is cut at
# whichever appears first. ch6 carries only the second.
TAILS = ("*Back to the chapter.*",
         "*For the full process and additional pairs, see Appendix F: The Polarity Map.*")

import sys
ONLY = [int(a) for a in sys.argv[1:]] or sorted(JOBS)
for ch in ONLY:
    start, anchor, heading, drop = JOBS[ch]
    p = os.path.join(MS, "ch%d.md" % ch)
    t = io.open(p, encoding="utf-8").read()

    for probe in (start, anchor):
        if t.count(probe) != 1:
            raise SystemExit("ch%d: anchor %r occurs %d times" % (ch, probe[:40], t.count(probe)))

    i = t.index(start)
    ends = [t.index(x) for x in TAILS if x in t and t.index(x) > i]
    if not ends:
        raise SystemExit("ch%d: no trailing apparatus found after the draw" % ch)
    j = min(ends)
    if j <= i:
        raise SystemExit("ch%d: tail precedes the draw" % ch)

    block = t[i:j].rstrip()
    if drop:
        if block.count(drop) != 1:
            raise SystemExit("ch%d: inline label not found once" % ch)
        block = block.replace(drop, "", 1)

    t = t[:i] + t[j:]                       # lift it out of Section 3
    k = t.index(anchor)                     # drop it in at the head of Section 4
    t = t[:k] + heading + "\n\n" + block + "\n\n---\n\n" + t[k:]

    # The Section 5 back-reference now points at the wrong section.
    old = "axis in Section 3."
    if t.count(old) == 1:
        t = t.replace(old, "axis in Section 4.", 1)

    io.open(p, "w", encoding="utf-8").write(t)
    print("ch%d relocated (%d words moved)" % (ch, len(block.split())))
