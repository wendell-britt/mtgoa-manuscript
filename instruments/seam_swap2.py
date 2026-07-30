# -*- coding: utf-8 -*-
"""
Second seam pass — the five swaps the widened detector found.

`seam_sweep.py`'s BOOK pattern originally keyed on `this chapter` and missed every
other determiner. Widened 2026-07-30 to catch `the chapter`, `the whole chapter`,
`the reader` and `the ideal reader`, the remaining count went from 8 to 17. These are
the five that take the same School-of-the-X swap Wendell already approved.

The other twelve need his call and are not touched here:

  · seven italic apparatus lines -- three `*Back to the chapter.*` and four Appendix F
    pointers -- which have no in-world equivalent and move below the seam once the seam
    has a marked location.
  · ch3:155a, a forward pointer that duplicates ch3:578's fuller one below the seam.
  · ch3:169, held for the margin-versus-swap call.
  · ch8:167, the Big Mind lineage paragraph -- sourcing, same shape and same ruling as
    the wu xing paragraph.
  · ch8:191 and ch8:193, Wilber and Laloux. Laloux has no entry in Appendix G at all.

    python3 instruments/seam_swap2.py --dry
    python3 instruments/seam_swap2.py
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

SWAPS = [
    (3, "You need the pair itself here, because the chapter stands on it and the back half will hand you the other end.",
        "You need the pair itself here, because the School of the Body stands on it, and you get the other end once you can hold the first.",
        "'the back half will hand you' was Wendell describing this book's own seam, inside Voss's treatise. The most authorial sentence left above a signature."),

    (7, "The reader stays",
        "The student stays",
        "third ICA leak, after ch6:131 and ch7:73."),

    (8, "You'll know which one belongs to you. The chapter keeps going either way.",
        "You'll know which one belongs to you. The work keeps going either way.",
        "'the work' rather than the School, because the sentence is about the reader continuing, not about the School doing anything."),

    (8, "The Sage runs two questions at all times, and the whole chapter turns on keeping them apart.",
        "The Sage runs two questions at all times, and everything the School of the Horizon teaches turns on keeping them apart.",
        "noun only; 'the whole School of the Horizon turns' does not read, so the teaching takes the verb."),

    (8, "You don't have to convert to any of them to use the chapter.",
        "You don't have to convert to any of them to use the work.",
        "the second half of ch8:167. Held with the paragraph if Wendell moves it; harmless either way."),
]


def main():
    dry = "--dry" in sys.argv
    texts, plan = {}, []
    for n, old, new, note in SWAPS:
        if n not in texts:
            texts[n] = io.open(os.path.join(MS, "ch%d.md" % n), encoding="utf-8").read()
        c = texts[n].count(old)
        if c != 1:
            raise SystemExit("ch%d: %r matched %d times, expected 1" % (n, old[:60], c))
        texts[n] = texts[n].replace(old, new, 1)
        plan.append((n, old, new, note))

    if dry:
        for n, old, new, note in plan:
            print("ch%d\n  -  %s\n  +  %s\n  ~  %s\n" % (n, old[:140], new[:140], note))
        print("%d swaps, all anchors matched exactly once" % len(plan))
        return 0

    for n, t in texts.items():
        io.open(os.path.join(MS, "ch%d.md" % n), "w", encoding="utf-8").write(t)
    print("%d swaps applied across %d chapters" % (len(plan), len(texts)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
