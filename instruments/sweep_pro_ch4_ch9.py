# -*- coding: utf-8 -*-
"""sweep_pro_ch4_ch9 -- DL-93. The PRO sweep of ch4 to ch9.

Wendell, 2026-09-09: *"sweep the remaining 30 PRO sites in ch4-ch9."*

There were 24, not 30. The 30 came off a count taken before DL-91 and DL-92 dropped ch3 from
eleven to nine and before the instrument stopped reporting two things that were never phrases.

**Twenty-four matches read in context. Two were the instrument's fault, leaving twenty-two real
sites. Eighteen are licensed and stay. Four changed.** The eighteen are worth naming, because a
sweep that changes everything it finds is not a sweep, it is a rewrite: *the angry one*, *the
difficult one* ×2, *the reasonable one* ×3 are social roles the book is quoting, exactly like ch3's
*the good one*; *the smallest one*, *the stated one*, *the weak ones*, *the withdrawn one*, *the
obvious one*, *the bad ones*, *the horizontal one*, *the actual one*, *the harder one*, *the cold
ones*, *the hard ones*, *the gracious one* all have their noun in the same clause or the sentence
before.

THE FOUR:

  - **ch4 ×2, `the truer one`.** Grammatically licensed -- two sentences are on the page and the
    comparative picks one. **It fails on DL-92 instead**, ruled ninety minutes earlier: the book
    does not sell one sentence as truer than another. And the passage refutes it itself three
    lines down -- *"a defense answers an accusation and Water made a report"*. The criterion is
    which channel is actually running, not which sentence is more true.
  - **ch7, `leaving out the wrong one`.** Genuinely two-ways ambiguous: the wrong account, or the
    party who was wrong. Elian's casebook means the second.
  - **ch8, `when the real one costs more than you have`.** The referent is the game you would
    play if you could afford it, and **it is nowhere in the sentence**. The only game named is the
    fallback. The reader is told *you know which one I mean* about the one thing not on the page.

    python3 instruments/sweep_pro_ch4_ch9.py
"""
import io, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ruling import guard                     # FR-E1

CLAIM = "DL-93"

HERE = os.path.dirname(os.path.abspath(__file__))
M = lambda n: os.path.join(HERE, os.pardir, "manuscript", n)

# 1, 2 -- ch4's Fire/Water channel check. DL-92 consequence, not a pro-form defect.
OLD_1 = "Say the truer one when you get there, whichever it is."
NEW_1 = "Say whichever is actually running when you get there."

OLD_2 = "Fire. The truer one runs:"
NEW_2 = "Fire. The one underneath runs:"

# 3 -- ch7, Elian Cross's casebook. The pro-form leaves the reader choosing between two readings.
OLD_3 = "leaving out the wrong one is how a case stops being a case"
NEW_3 = "leaving out whoever was wrong is how a case stops being a case"

# 4 -- ch8's last instruction before the reader builds. The game you want is the only thing the
# sentence does not name, and it is the thing the sentence points at.
OLD_4 = "the altitude you drop to when the real one costs more than you have"
NEW_4 = "the altitude you drop to when the game you want costs more than you have"

EDITS = [(M("ch4.md"), OLD_1, NEW_1), (M("ch4.md"), OLD_2, NEW_2),
         (M("ch7.md"), OLD_3, NEW_3), (M("ch8.md"), OLD_4, NEW_4)]


def norm(s):
    return " ".join(s.replace("*", "").split())


def main():
    guard(CLAIM, EDITS)                      # FR-E1/E3

    staged = {}
    for path in dict.fromkeys(p for p, _, _ in EDITS):
        staged[path] = io.open(path, encoding="utf-8").read()

    for path, old, new in EDITS:
        if staged[path].count(old) != 1:
            sys.stderr.write("REFUSED: a declared span matched %d times (need 1) in %s. Nothing "
                             "written.\n  %s\n"
                             % (staged[path].count(old), os.path.basename(path), old[:70]))
            sys.exit(2)
        staged[path] = staged[path].replace(old, new, 1)

    for path, text in staged.items():
        b, a = io.open(path, encoding="utf-8").read(), text
        for p, old, new in EDITS:
            if p == path:
                b = b.replace(old, "", 1)
                a = a.replace(new, "", 1)
        if norm(b) != norm(a):
            sys.stderr.write("REFUSED: prose changed outside the declared spans in %s. Nothing "
                             "written.\n" % os.path.basename(path))
            sys.exit(3)

    for path, old, new in EDITS:
        if old in staged[path] or new not in staged[path]:
            sys.stderr.write("REFUSED: a declared edit did not take. Nothing written.\n  %s\n"
                             % old[:70])
            sys.exit(4)

    for path, text in staged.items():
        io.open(path, "w", encoding="utf-8").write(text)

    print("PRO sweep applied: %d span(s) across %d file(s)" % (len(EDITS), len(staged)))

    # The standing rule from DL-92: a ruling that asserts a scope ends by counting the thing it
    # claims to have removed. Here that is the four phrases, and the instrument's own PRO count.
    sys.path.insert(0, HERE)
    import article
    left = sum(1 for n in ("ch4.md", "ch5.md", "ch6.md", "ch7.md", "ch8.md", "ch9.md")
               for r in article.sites(io.open(M(n), encoding="utf-8").read()) if r[0] == "PRO")
    gone = sum(io.open(p, encoding="utf-8").read().count(o) for p, o, _ in EDITS)
    print("declared phrases still present: %d (want 0)" % gone)
    print("PRO sites remaining in ch4-ch9: %d (want 18, all licensed)" % left)


if __name__ == "__main__":
    main()
