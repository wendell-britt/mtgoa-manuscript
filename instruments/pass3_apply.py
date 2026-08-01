# -*- coding: utf-8 -*-
"""
pass3_apply.py — the 33 Pass 3 line-editor flags, applied.

Wendell 2026-08-01, on the report: "All of these are blockers to be updated." LE-3's
proposed edit was rejected in the same breath and is rewritten here — the original
proposal nested the quoted line inside the sentence ("The subject of *this isn't
working* is the work"), which is unreadable aloud. The pointer is what was broken, so
the fix quotes the line and states what the paragraph is actually for.

Anchors are exact and the file is written once, at the end, after every anchor in it
has been found exactly once. A missed or duplicated anchor aborts the whole run and
writes nothing — `spec_edit.py`'s discipline, which exists because a partial
application is worse than none.

    python3 instruments/pass3_apply.py --check    # verify anchors, write nothing
    python3 instruments/pass3_apply.py            # apply

Flag IDs are `editorial_reports/2026-08-01/PASS3_LINE_EDITOR.md` §4. Run `gate.py`,
`dupes.py` and `line_scan.py` after.
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

# (flag, file, anchor, replacement)
EDITS = [
    # ---------------------------------------------------------------- ch1
    ("LE-1", "ch1.md",
     "Children receive care or not based on whether you actually understand something, "
     "and your theory of harm stays invisible to them.",
     "Children receive care or not based on whether you actually understand what they "
     "need, and your theory of harm is invisible to them either way."),
    ("LE-2", "ch1.md",
     "does the same thing less visibly: a set of conditions to meet before the real help arrives",
     "asks for the same conversion, less visibly: a set of conditions to meet before the "
     "real help arrives"),

    # ---------------------------------------------------------------- ch2
    # LE-3 rewritten after Wendell rejected the first proposal.
    ("LE-3", "ch2.md",
     "The subject of that sentence is the work.",
     "*This isn't working* is a verdict on the work, not on you."),
    # LE-4's first replacement inserted "often" and produced a second reading -- "the ones
    # who do not often push through" -- which is the opposite of the sentence, so the flag
    # was closed without being fixed. Caught by the Voice Guardian pass, DL-27.
    ("LE-4", "ch2.md",
     "The ones who don't push through instead of going through:",
     "Of the ones who don't, most push through instead of going through:"),
    ("LE-5", "ch2.md",
     "When the Protector holds the joystick, I walk into a conversation already armored, "
     "braced against something that has not happened, and the person across from me meets "
     "the hull before they meet me.",
     "When the Protector holds the joystick, you walk into a conversation already armored, "
     "braced against something that has not happened, and the person across from you meets "
     "the hull before they meet you."),

    # ---------------------------------------------------------------- ch3
    ("LE-6", "ch3.md",
     "and every card in it ends in an artifact",
     "and every one of them ends in an artifact"),
    ("LE-7", "ch3.md",
     "*Aim the Awareness* becomes:",
     "A Show Up card like *Aim the Awareness* becomes:"),
    ("LE-8", "ch3.md",
     "This stage can take five seconds or can run throughout, and you keep noticing the "
     "feeling across the whole experience.",
     "This stage can take five seconds or run the length of the encounter, and you keep "
     "noticing the feeling the whole way through."),
    ("LE-9", "ch3.md",
     "So take the move where it counts, out of the forest, where nothing costs you and no "
     "one is watching, and into the places allyship actually happens.",
     "So take the move out of the forest, where nothing costs you and no one is watching, "
     "and into the places allyship actually happens."),
    ("LE-10", "ch3.md",
     "that is the awareness trap, the domain that swallowed the others",
     "that is the awareness trap, the habit that swallowed the others"),

    # ---------------------------------------------------------------- ch4
    ("LE-11", "ch4.md",
     "by watching boundaries dissolve, relationships violate, and lines get crossed",
     "by watching boundaries dissolve, relationships rupture, and lines get crossed"),
    ("LE-12", "ch4.md",
     "From outside it will look like fighting. Ignore that.",
     "From outside it will look like fighting. Let it look like that."),
    ("LE-13", "ch4.md",
     "Everything stopped in a particular way. They didn't come back after that.",
     "Everything stopped. The people on the other end of it didn't come back."),
    ("LE-14", "ch4.md",
     "You let the field settle. You do not retraumatize the other person by returning to "
     "the confrontation before the moment has passed.",
     "You let the field settle. Do not go back to the confrontation before the moment has "
     "passed: returning early retraumatizes the person you were confronting."),

    # ---------------------------------------------------------------- ch5
    ("LE-15", "ch5.md",
     "Here's what it is: a question about what you built instead, and whether it lasted, "
     "and whether you can see the connection.",
     "Here's what it asks: what you built instead, whether it lasted, and whether you can "
     "see the connection."),
    ("LE-16", "ch5.md",
     "It goes on record here because from the inside it reads as weakness, and keepers "
     "before you have filed the tension under that name.",
     "It is named here because from the inside the tension reads as weakness, and keepers "
     "before you have filed it under that name."),
    ("LE-17", "ch5.md",
     "Somebody repaired every tradition still worth having, noticed it failing, and did "
     "something about it instead of calling the failure sacred.",
     # The first version of this replacement read "was repaired by someone who noticed",
     # which fixed the garden path and bought it with a passive: prose_diet moved ch5 from
     # 1.35 to 1.38 on a counter the chapter was already heavy on. Active, same subject.
     "Every tradition still worth having had someone who noticed it failing and did "
     "something about it instead of calling the failure sacred."),
    ("LE-18", "ch5.md",
     "the next person can receive (endurance and loyalty are the entry requirements): the account of",
     "the next person can receive: the account of"),
    ("LE-19", "ch5.md",
     "Nothing in it is made.",
     "Not one of them makes anything new."),
    ("LE-20", "ch5.md",
     "Whether I commit is not in your remit.",
     "Whether I commit is not yours to decide."),

    # ---------------------------------------------------------------- ch6
    ("LE-21", "ch6.md",
     "The discipline goes out with it, and the discipline alone addresses the thing above.",
     "The discipline goes out with it, and the discipline is the only thing that keeps a "
     "relational field from becoming a leverage point in the first place."),
    ("LE-22", "ch6.md",
     "It is not enough for the other one, and that shortfall is the point.",
     "It is not enough for the question underneath it, and that shortfall is the point."),
    ("LE-23", "ch6.md",
     "The reason you can walk into an organization and know, before you have seen a single "
     "number, that something has gone wrong under the third floor of the org chart, comes "
     "down to this: the Emotional Body registered it and the rest of you is still catching up.",
     "You can walk into an organization and know something has gone wrong under the third "
     "floor of the org chart before you have seen a single number. The Emotional Body "
     "registered it; the rest of you is still catching up."),

    # ---------------------------------------------------------------- ch7
    ("LE-24", "ch7.md",
     "**Hold** is the maintenance of enough safety that difficult conversation remains "
     "possible even when the field is charged, not the four seconds of Stand you learned "
     "from the Challenger, where one person declines to take back one line, but the "
     "sustained containment of a whole field over the length of a hard conversation, "
     "sometimes over months.",
     "**Hold** is the maintenance of enough safety that difficult conversation remains "
     "possible even when the field is charged. It is not the four seconds of Stand you "
     "learned from the Challenger, where one person declines to take back one line; it is "
     "the sustained containment of a whole field over the length of a hard conversation, "
     "sometimes over months."),
    ("LE-25", "ch7.md",
     "It is the altitude at which a person can hold multiple valid perspectives simultaneously.",
     "The Diplomat's altitude is the one at which a person can hold multiple valid "
     "perspectives simultaneously."),
    # The second half of the anchor is what makes it unique: the identical sentence at
    # ch7:185 is followed by "Everyone likes you", this one by "Every live relationship".
    ("LE-26", "ch7.md",
     "Care without impact is attendance: warm, dependable, and doing nothing. Impact "
     "without care is the Challenger's altitude imported into a conversation that needed "
     "this one. Every live relationship",
     "You know both failure states: attendance on one side, the Challenger's altitude "
     "imported on the other. Every live relationship"),

    # ---------------------------------------------------------------- ch8
    ("LE-27", "ch8.md",
     "It looks like delay from outside, and from inside on a bad day.",
     "It looks like delay from outside, and on a bad day it looks like delay from inside too."),
    ("LE-28", "ch8.md",
     "Holding space participates in it.",
     "Holding space participates in the competition."),
    ("LE-29", "ch8.md",
     "None of this describes the guru on the mountain who has risen above it all.",
     "The Sage described here is not the guru on the mountain who has risen above it all."),
    ("LE-30", "ch8.md",
     "That happens frequently, and at this altitude almost always, because panoramic "
     "vision is not the common configuration.",
     "It does for a lot of people, and at this altitude almost always, because panoramic "
     "vision is not the common configuration."),
    ("LE-31", "ch8.md",
     "Something in me runs differently, and that is usually accurate and sometimes the "
     "whole instrument.",
     "Something in me runs differently, and that reading is usually accurate, and "
     "sometimes it is the whole instrument."),
    ("LE-32", "ch8.md",
     "They leave with reading. On the narrow jurisdiction, the same part returns the same "
     "accurate report and the answer changes:",
     "They leave with reading. Give that same part its narrow jurisdiction and it returns "
     "the same accurate report, but the answer changes:"),

    # ---------------------------------------------------------------- ch9
    ("LE-33", "ch9.md",
     "Right now I'm essentially the only one running it in this mode.",
     "Right now I'm essentially the only one teaching it this way."),
]


def main():
    check = "--check" in sys.argv
    files, problems = {}, []
    for flag, name, anchor, _ in EDITS:
        if name not in files:
            files[name] = io.open(os.path.join(MS, name), encoding="utf-8").read()
        n = files[name].count(anchor)
        if n != 1:
            problems.append("%s %s: anchor found %d times: %r" % (flag, name, n, anchor[:70]))
    if problems:
        print("ABORT — nothing written")
        for p in problems:
            print("  " + p)
        return 1

    for flag, name, anchor, new in EDITS:
        files[name] = files[name].replace(anchor, new, 1)

    print("%-7s %-8s %s" % ("flag", "file", "change"))
    for flag, name, anchor, new in EDITS:
        print("%-7s %-8s %s" % (flag, name, anchor[:66]))
        print("%-7s %-8s %s" % ("", "", "-> " + new[:66]))
    if check:
        print("\n--check: %d anchors verified, nothing written" % len(EDITS))
        return 0
    for name, text in files.items():
        io.open(os.path.join(MS, name), "w", encoding="utf-8").write(text)
    print("\n%d edits applied across %d files" % (len(EDITS), len(files)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
