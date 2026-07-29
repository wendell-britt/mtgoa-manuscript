# -*- coding: utf-8 -*-
"""
W9 — ch3 em-dash pass, batch D. The sixteen the first three batches left.

All sixteen are single tails, so the choice is comma or colon by one test: does
the tail *list* what came before, or does it *continue the sentence*. Lists take
the colon (Feeling means the charge arriving: the heat in the chest, the drop in
the stomach). Continuations take the comma.

    python3 instruments/w9_ch3_d.py --dry
    python3 instruments/w9_ch3_d.py
"""
import io, os, sys

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "manuscript", "ch3.md")

EDITS = [
("being allowed to arrive — the heat in the chest,", "being allowed to arrive: the heat in the chest,"),
("no instrument running underneath — competent, useful in a narrow band,",
 "no instrument running underneath, competent, useful in a narrow band,"),
("Feeling in its collective form — named in a circle, processed together, honored aloud.",
 "Feeling in its collective form: named in a circle, processed together, honored aloud."),
("altitude issues them loudest — outcomes over people, results as the metric,",
 "altitude issues them loudest: outcomes over people, results as the metric,"),
("*pause* and notice what you feel — the thing actually here in your body right now,",
 "*pause* and notice what you feel, the thing actually here in your body right now,"),
("honors that moment — not immediately trying to fix it,", "honors that moment, without immediately trying to fix it,"),
("five seconds or can run throughout — you keep noticing the feeling",
 "five seconds or can run throughout, and you keep noticing the feeling"),
("sensitivity to everything actually present — in your own body first,",
 "sensitivity to everything actually present, in your own body first,"),
("turned the dial all the way back down — the only relief anyone had shown you.",
 "turned the dial all the way back down, the only relief anyone had shown you."),
("and something else surfaces — something a part of you has kept down there too.",
 "and something else surfaces, something a part of you has kept down there too."),
("the very dynamic you say you want to end — the charge of being the good one,",
 "the very dynamic you say you want to end: the charge of being the good one,"),
("stop refusing to feel it — because what stays hidden runs the moment,",
 "stop refusing to feel it, because what stays hidden runs the moment,"),
("Opening makes the fear available — fully felt instead of managed",
 "Opening makes the fear available, fully felt instead of managed"),
("is detachment and perspective — the view that lets you see the whole.",
 "is detachment and perspective, the view that lets you see the whole."),
("The Grow stage is the integration — the moment when the feeling stops",
 "The Grow stage is the integration, the moment when the feeling stops"),
("- A feeling of being met — like the feeling has been witnessed",
 "- A feeling of being met, like the feeling has been witnessed"),
]


def main():
    dry = "--dry" in sys.argv
    t = io.open(P, encoding="utf-8").read()
    bad = []
    for a, b in EDITS:
        n = t.count(a)
        if n != 1:
            bad.append((n, a[:70]))
        else:
            t = t.replace(a, b, 1)
    if bad:
        print("ABORT — anchors not unique, nothing written:")
        for n, a in bad:
            print("  %d matches: %r" % (n, a))
        return 1
    if not dry:
        io.open(P, "w", encoding="utf-8").write(t)
    print("%s %d edits" % ("would apply" if dry else "applied", len(EDITS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
