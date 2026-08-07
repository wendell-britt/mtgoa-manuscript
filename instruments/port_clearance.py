# -*- coding: utf-8 -*-
"""
port_clearance.py -- the two series that finish what ch2's Second Walk starts.

Thirteen paragraphs from claude/book-pdf-epub-production-ybxa11, ported 2026-08-05
on Wendell's ruling ("port all 13") after a three-way comparison against the common
base 4f1a4e2 showed that branch had changed almost nothing else in ch3-ch9: four
lines per chapter, and every one of them belonging to one of two designed series.

SERIES A -- what each Face means by good. One per chapter, ch3 to ch8, all six
Faces. ch3 sets the frame; the rest give a definition and its cost.

SERIES B -- the same daemon, in somebody else. One per chapter, ch3 to ch8, six
daemons: Controller, Skeptic, Fixer, Emotional Body, Victim, Damaged Self. The
seventh is the Protector, and it is missing on purpose -- ch2's Second Walk works
the Protector at the door and these six are what stands behind it.

Plus one in ch9 extending clearance to the one-person move.

Porting the Second Walk (DL-56) without these left an arc started and dropped.
`clearance` is the through-line: coined in ch2 section 7, spent once per chapter
after it, and the index entry written yesterday called it a ch2-local term.

TWO COLLISIONS, both from this branch's own work:

  1. Four Series A anchors are `The village never meant for that to happen` on
     that branch and `The villagers never meant...` here, because R8 converted
     them. Anchored on the converted form.

  2. ch6's Series A paragraph arrives carrying `more often than the village
     believes` -- a perception verb on a Grade 6 entity, the exact construction
     this branch converted 40+ times. Converted on the way in. Importing it as
     found would have re-introduced the violation the whole audit removed.

ch4's Series B anchor reads `your auditor` here and `your Skeptic` there. Same
sentence, same slot; the Skeptic is called the auditor in that passage.

    python3 instruments/port_clearance.py --dry
    python3 instruments/port_clearance.py
"""
import io, os, sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))

EDITS = [
    ('manuscript/ch3.md',
     'The villagers never meant for that to happen.',
     'Each of the six Faces carries its own word for being good to somebody. **The Shaman means one thing by it: somebody said the true thing, and it landed.** People who share that definition call you kind. People who hold a different one call you cold. Neither scores you wrong. They score you in another dictionary.'),

    ('manuscript/ch3.md',
     'You know what your Controller is for now. That is what you take out.',
     "Theirs is doing the same job in a Forest you cannot see into. A stranger's Controller enforces a rulebook you have never read, so it fires when you arrive holding a better standard, and it opens when you meet the one they already keep. You earn clearance with a Controller by keeping their rule."),

    ('manuscript/ch4.md',
     'The villagers never meant for that to happen.',
     '**The Challenger means: somebody drew the line on the day it needed drawing.** A Diplomat can watch your best hour and see damage, and mean it sincerely.'),

    ('manuscript/ch4.md',
     'You know what your auditor is for now. That is what you take out.',
     "Theirs is doing the same job in a Forest you cannot see into. A stranger's Skeptic is an auditor somebody fooled once, so confidence is the one thing it will not take as evidence. What you admit you do not know is the cheapest clearance available anywhere in this book."),

    ('manuscript/ch5.md',
     'The villagers never meant for that to happen.',
     '**The Regent means: somebody carried the inheritance far enough that the next person can pick it up.** A keeper who holds a rule for fifteen years earns faithful from one person and immovable from the next, on identical evidence.'),

    ('manuscript/ch5.md',
     'You know what your Fixer is for now. That is what you take out.',
     "Theirs is doing the same job in a Forest you cannot see into. A stranger's Fixer is holding something in place on purpose, and they will not always tell you which thing, or why. Repair what they chose to keep and the door shuts, however broken it looked from outside."),

    ('manuscript/ch6.md',
     'The villagers never meant for that to happen.',
     '**The Architect means: what you built runs after you leave.** That scores a design nobody thanks you for above a conversation everybody remembers, and it is right about that more often than the villagers believe.'),

    ('manuscript/ch6.md',
     'You know what your Emotional Body is for now. That is what you take out.',
     "Theirs is doing the same job in a Forest you cannot see into. A stranger's Emotional Body is a sensor that learned not to output in front of people, so naming out loud what you can see it doing is the fastest way to close a door. Clearance opens when the feeling gets to stay theirs."),

    ('manuscript/ch7.md',
     'Each stage earns the next.',
     '**The Diplomat means: nobody left the table.** It is the most generous of the six and the easiest to overspend, because a table nobody leaves also decides nothing.'),

    ('manuscript/ch7.md',
     'You know what your Victim is for now. That is what you take out.',
     "Theirs is doing the same job in a Forest you cannot see into. A stranger's Victim guards a story and the returns on telling it, and some of those returns are real: sympathy, an exemption, a reason to stay where they are. Say that out loud and the door shuts for good. Clearance here comes from feeling it with them without confirming them in it, which is the line this chapter has been drawing for you all along."),

    ('manuscript/ch8.md',
     'Keep the terms apart so they don',
     '**The Sage means: they can do it without you.** It is the only one of the six that counts your absence as success, and the other five mistake that for indifference more often than not.'),

    ('manuscript/ch8.md',
     'You know what your Damaged Self is for now. That is what you take out.',
     "Theirs is doing the same job in a Forest you cannot see into. A stranger's Damaged Self carries weight it has already agreed to carry, and asking it to account for the weight is one more thing to carry. Take load off without requiring the account, and the door opens."),

    ('manuscript/ch9.md',
     'In practice: one person, not an audience.',
     "One person is also the smallest ask you can make of anybody's Protector. An audience needs a door opened wide on a day nobody chose; one person, asked for one thing, fits through almost any clearance you already hold."),

]


def main():
    dry = "--dry" in sys.argv
    loaded = {}
    for path, anchor, _p in EDITS:
        full = os.path.join(ROOT, path)
        loaded.setdefault(full, io.open(full, encoding="utf-8").read())

    for path, anchor, para in EDITS:
        full = os.path.join(ROOT, path)
        if loaded[full].count(anchor) != 1:
            sys.exit("ABORT: %s anchor matched %d times, expected 1.\n  %s\nNothing written."
                     % (path, loaded[full].count(anchor), anchor[:88]))
        if para[:60] in loaded[full]:
            sys.exit("ABORT: %s already carries this paragraph.\n  %s\nNothing written."
                     % (path, para[:88]))

    for path, anchor, para in EDITS:
        full = os.path.join(ROOT, path)
        i = loaded[full].index(anchor)
        j = loaded[full].index("\n\n", i)
        loaded[full] = loaded[full][:j] + "\n\n" + para + loaded[full][j:]
        print("  ++ %-18s %s" % (path.split("/")[-1], para[:88]))

    if dry:
        print("\n--dry: %d paragraphs verified, nothing written." % len(EDITS))
        return 0
    for full, text in loaded.items():
        io.open(full, "w", encoding="utf-8").write(text)
    print("\nwrote %d files, %d paragraphs." % (len(loaded), len(EDITS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
