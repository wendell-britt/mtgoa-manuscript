# -*- coding: utf-8 -*-
"""
Arc completion for ch5 and ch7 — and what the derivation actually said.

The diagnosis: ch4, ch6 and ch8 land every mode on one of the five canonical satisfied
states (Triumph, Poignance, Wonder, Peace, Bliss), so their channel column is *derived*
and cannot be wrong. ch5 and ch7 stop at a practice outcome instead, so their channel
column had nothing to derive from and was filled in by hand. Both were wrong.

Completing the arcs means giving each one its canonical terminus, so the channel is read
off the destination rather than chosen. Run on both chapters, here is what fell out.

**ch5 derives cleanly, five for five.** Every hand-assignment is confirmed, including
tonight's Keeper of Vows change, which is now provable rather than merely plausible:

    Obedience -> True allegiance -> Peace        compliance gone numb is Earth stuck;
                                                 ch4 uses that exact phrase for Earth
    Inheritance-shame -> gift -> Poignance       letting go while honouring: Water
    Duty -> Service -> Bliss                     the prose says "requires vitality"
    Rigidity -> Integrity -> Triumph             the prose says "the fire of conviction"
    Dogma -> Faithfulness -> Wonder              the prose says "what fear does to a vow"

**ch7 derives four for five, and the fifth is forced.** Bridge-Builder to Metal,
Translator to Earth, Repairer to Water, Integrative Negotiator to Fire. That leaves Wood
unclaimed and Field-Holder unassigned, so **Field-Holder is Wood by elimination and the
table was right all along.**

That is the opposite of what I recommended before running it. I had proposed changing
the table to Metal/Fear because Section 4 says Field-Holder's Dissatisfaction is anxiety.
The derivation says the section is what is out of step: **both** of Field-Holder's stated
alchemies run channels another mode already owns. Anxiety is Bridge-Builder's, and
Collapsed Calm to Active Containment is a clean Earth arc, which is Translator's. The
Wood work is the arc the table names and the section never runs.

**A second thing fell out, and it retires a theory rather than a sentence.** ch7:254 read
*"runs channel-wide, from Metal (fear/anxiety) to Wood (joy/interest)"*, and it was the
only evidence for the Diplomat being a cross-channel Face. It is a mislabel: the canon
puts Fear's satisfied state at **Wonder**, and curiosity is Wonder's own territory, not
Wood's. Corrected, the Bridge-Builder completes one channel like every other mode in the
book, and the Diplomat needs no special case.

Not done here: Field-Holder's Section 4 alchemies. The derivation now settles what they
have to say, but rewriting them is authorship rather than arithmetic.
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

# (mode, canonical terminus) in table order, per chapter.
CH5 = [("The Custodian", "Peace"), ("The Inheritor", "Poignance"),
       ("The Teacher", "Bliss"), ("The Reformer", "Triumph"),
       ("The Keeper of Vows", "Wonder")]
CH7 = [("Bridge-Builder", "Wonder"), ("Translator", "Peace"),
       ("Field-Holder", "Bliss"), ("Repairer", "Poignance"),
       ("Integrative Negotiator", "Triumph")]

E = []
for name, end in CH5 + CH7:
    E.append(("ch5.md" if (name, end) in CH5 else "ch7.md", name, end))

FIX = [
    # Bridge-Builder is the one row with two arcs. The generic rule appends the terminus
    # to the end of the cell, which puts Wonder on the secondary arc; it belongs on the
    # primary one.
    ("ch7.md",
     "| **Bridge-Builder** | Metal/Fear | Anxiety → Curiosity (primary) / Stage-Fright "
     "→ Authentic Presence → **Wonder** |",
     "| **Bridge-Builder** | Metal/Fear | Anxiety → Curiosity → **Wonder** (primary) / "
     "Stage-Fright → Authentic Presence |"),

    # The sentence that seeded the cross-channel theory.
    ("ch7.md",
     "The Bridge-Builder's primary Translate move runs channel-wide, from Metal "
     "(fear/anxiety) to Wood (joy/interest).",
     "The Bridge-Builder's primary Translate move runs the length of one channel, from "
     "the fear end of Metal to the curiosity at its far end."),
]


def main():
    files = {}
    bad = []

    for fname, mode, end in E:
        p = os.path.join(MS, fname)
        files.setdefault(fname, io.open(p, encoding="utf-8").read())
        rows = [l for l in files[fname].split("\n")
                if l.startswith("| **%s**" % mode)]
        if len(rows) != 1:
            bad.append("%s: %d rows for %r" % (fname, len(rows), mode))
            continue
        old = rows[0]
        cells = old.split("|")
        cells[3] = " %s → **%s** " % (cells[3].strip(), end)
        files[fname] = files[fname].replace(old, "|".join(cells), 1)

    for fname, old, new in FIX:
        files.setdefault(fname, io.open(os.path.join(MS, fname), encoding="utf-8").read())
        if files[fname].count(old) != 1:
            bad.append("%s: FIX anchor matched %d times" % (fname, files[fname].count(old)))
            continue
        files[fname] = files[fname].replace(old, new, 1)

    if bad:
        print("ABORTED, nothing written:")
        for b in bad:
            print("  " + b)
        return 1

    if "--dry" not in sys.argv:
        for fname, t in files.items():
            io.open(os.path.join(MS, fname), "w", encoding="utf-8").write(t)
    print("%d arc(s) + %d correction(s) %s"
          % (len(E), len(FIX), "checked" if "--dry" in sys.argv else "applied"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
