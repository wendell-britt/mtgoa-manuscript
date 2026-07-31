# -*- coding: utf-8 -*-
"""
Band 6, LINE — third pass. Six more, plus the `quieter` ruling applied.

**ch5:78, and the reason it was wrong.** Wendell, on "The Regent arrived with something
quieter and harder to see": *"how can you claim to hear something when you don't have
ears. You do have eyes so harder to see makes sense."* The word was a broken metaphor
before it was a banned word, sitting next to a sight claim that works. It becomes
*slower*, which is a real property of the Regent and one the chapter states later: the
Regent's pace is generational.

That clears the gate gap left open in the last pass. `\\bquiet(ly)?\\b` matched *quiet*
and *quietly* and walked past *quieter*, which sat in ch1 and ch5. Both are now fixed, so
the pattern closes to `\\bquiet(ly|er|est)?\\b` and the gate still reads zero.

  CH7 L3  the Care/Impact failure state restated with one word swapped, "warm,
          dependable" against "warm, reliable", 336 lines apart. It reads as a draft
          artefact rather than a callback. Made identical, so the second is heard as the
          same sentence returning.
  CH7 L1  "You build a practice ... that does not skip" run twice as a formula. The
          second keeps the list and drops the formula.
  CH7 S2  the recap claimed a practice the chapter never ran: "you have now practiced all
          five". The chapter teaches the five and drills one.
  CH6 L5  a sentence that folds back on itself: "The four rows around it are that
          unauthorized selection showing up before and after itself."
  CH9 L3  "a different journey" pointed at nothing.
  CH9 L4  a sentence that closes on itself: "Every detour that feels like a detour just
          shows you what walking looks like."
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

E = [
    ("ch7.md",
     "Care without impact is attendance: warm, reliable, and doing nothing.",
     "Care without impact is attendance: warm, dependable, and doing nothing."),

    ("ch7.md",
     "You build a practice that does not skip",
     "You work the sequence without skipping"),

    ("ch7.md",
     "The five stages form the chapter's spine, and you have now practiced all five: "
     "Bridge, Translate, Hold, Repair, Negotiate.",
     "The five stages form the chapter's spine, and you have now met all five: Bridge, "
     "Translate, Hold, Repair, Negotiate."),

    ("ch6.md",
     "The four rows around it are that unauthorized selection showing up before and "
     "after itself.",
     "The four rows around it are what that early selection does to the stages on either "
     "side of it."),

    ("ch9.md",
     "Ascending belongs to a different journey, and so does perfecting.",
     "Ascending belongs to somebody else's book, and so does perfecting."),

    ("ch9.md",
     "Every detour that feels like a detour just shows you what walking looks like.",
     "Every detour that feels like a detour is another stretch of the same road."),
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
