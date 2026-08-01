# -*- coding: utf-8 -*-
"""
DL-19 Move 4's second half, and the ruled P0 cut.

**The ch9 shame insert.** v6 of `drafts/DRAFT_S2_ch7_shame_testimony_2026-07-31.md`,
seated immediately after `ch9:342` and before *"I was right and it cost me nothing and
everything at the same time."* The first half of M4, cutting the ch7 testimony slot, was
done on this branch last night.

The relocation is the point. Wendell ruled DL-4 enforced, which leaves no legal seat for
his first person in ch7, and the marginalia cannot take it because the annotator is an
in-world character. ch9 is his frame, the confession already lives at ch9:332-358, and the
beat this passage is built from is standing three lines above the insertion point:
*"Got feedback mid-course that it wasn't fun."*

**Measurement, recorded rather than acted on.** The passage reads `waste 1.41` against the
1.30 line. It is 85 words, well under the ~300 the review skill names as the point below
which ratios are noise, and the waste counter matches `it / this / that / there`, which is
what spoken first person is made of. ch9's register is contraction-heavy confession, and
the skill gained a note last night that waste has a floor as well as a ceiling: the draft
that scored 0.06 on that counter was the unreadable one. Every other counter is clean and
the gate passes. This is approved prose in Wendell's own voice, and editing it to move a
number would be the counter governing the register rather than the other way round.

**P0.** `ch1:181`'s production marker, ruled cut. `ch1:269`'s `[ URL / QR ]` stays;
Wendell deferred it pending links, and it is not to be allowlisted.
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

INSERT = (
    "What I said back, when that feedback came, was *you don't think deep introspection "
    "and shadow work and uncovering all your hidden motivations isn't fun?* I meant it. "
    "That's what made it useful. I was having a wonderful time in there. I'd built the "
    "whole thing out of what I found fun and it hadn't occurred to me to check whether "
    "my fun was anybody else's. Four years on that sentence still gets a laugh out of "
    "me, and what arrives a second behind the laugh is shame."
)

ANCHOR = ("I was right and it cost me nothing and everything at the same time.")

E = [
    ("ch9.md", ANCHOR, INSERT + "\n\n" + ANCHOR),
    ("ch1.md", " *[visual: the six Game Masters]*", ""),
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
