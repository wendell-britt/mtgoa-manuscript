# -*- coding: utf-8 -*-
"""
DL-19 · Moves 1 and 2 — enforcing DL-4 against author collision in body text.

Spec: `specs/SPEC_DL19_AUTHOR_COLLISION_2026-07-31.md`, merged from master today.
Wendell: *"chapter 3 and 5 SHOULDN'T be breaking this pattern. Enforce DL-4."*

**Move 1, ch3.** De-personed to second person, which is the chapter's own register, so
the mechanism and the game survive and the collision goes. Customer service is a
real-world referent a Face cannot own; it becomes a voice on the phone. *The Courage to
Be Disliked* stays, because a Face may cite.

**Move 2, ch5.** Stays first person, because a Regent-Face writing about inheritance is
the correct owner. Only the real-world referents move, into Sera Quill's register:
Keeper of Continuance, School of the Oath, genre *an annotated charter*.

    Martial arts, church, academia          ->  A house, an archive, a bench
    a collective ... progressive,           ->  a body that had unwritten its own
    justice-focused, right values on            charter. The right principles, agreed
    paper, absolutely no governance             and then struck, and no governance at all

*Charter* is her genre word and *struck* is what an annotated charter does to a clause.
The archive is already hers in canon: *"four generations of designs in the archive and no
record of what any of them cost."*

**The spec says "two phrases only" and there is a third.** Sixteen lines below the first,
the passage repeats the referents: *"Martial arts and the church and watching things
dissolve for twenty years actually prepare you for that."* Converting the first and
leaving this one would put *a house, an archive, a bench* and *martial arts and the
church* in the same passage, which is worse than either state. Converted to match, and
recorded here because it extends the spec's stated scope.

**Move 3 is not here and that is the ruling.** `ch5:516` and `ch6:365` already comply:
they are the Face-author writing under the chapter's assigned daemon, which
`FACE_AUTHORS.md` names as the most important thing a Face-author does. The typo the spec
found while reading ch6:365 was fixed on this branch last night.
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

E = [
    # ---- Move 1 · ch3, first person out --------------------------------------
    ("ch3.md",
     "I used to be very good at putting feelings away.",
     "Some people are very good at putting feelings away."),

    ("ch3.md",
     "Customer service. Someone on the phone, upset. The emotion would arrive, theirs "
     "and mine, and my chest would do this particular thing: a tightening, a pulling "
     "inward, like a door closing fast. Then I'd be gone. Not literally. I stayed on the "
     "call, professional, efficient. The part of me that could feel the situation had "
     "left the building.",
     "A voice on the phone, upset. The emotion arrives, theirs and yours, and the chest "
     "does a particular thing: a tightening, a pulling inward, like a door closing fast. "
     "Then you are gone. Not literally. You stay on the call, professional, efficient. "
     "The part of you that could feel the situation has left the building."),

    ("ch3.md",
     "I'd locate the problem. Solve the problem. Move on.",
     "Locate the problem. Solve the problem. Move on."),

    ("ch3.md",
     "It didn't work. Not because I solved the wrong problem. Because the problem wasn't "
     "the problem. *The Courage to Be Disliked* has a line: all problems are relational "
     "problems. I took it further. All problems are emotional problems. The rupture "
     "exists because something has gone unfelt. Solve for the emotion and you can move "
     "to service, the thing I thought I was doing all along.",
     "It does not work. Not because the wrong problem got solved. Because the problem "
     "wasn't the problem. *The Courage to Be Disliked* has a line: all problems are "
     "relational problems. Take it further. All problems are emotional problems. The "
     "rupture exists because something has gone unfelt. Solve for the emotion and you "
     "can move to service, which you thought you were doing all along."),

    ("ch3.md",
     "I was solving for my own emotion. The tightening in my chest when someone got "
     "upset was my discomfort, not theirs. I converted it into competence and action as "
     "fast as possible. They got efficiency. They needed presence.",
     "You are solving for your own emotion. The tightening in your chest when someone "
     "gets upset is your discomfort, not theirs. You convert it into competence and "
     "action as fast as possible. They get efficiency. They needed presence."),

    ("ch3.md",
     "I eventually invented a game, Tough Conversations.",
     "A game exists for exactly this, Tough Conversations."),

    ("ch3.md",
     "The first time I played it, I had to say \"tell me more\" to something that made me "
     "want to fix it immediately. I said the words. I stayed. The person went somewhere "
     "they wouldn't have gone if I'd moved. The thing they said next was the real thing, "
     "not the complaint, not the position, the feeling underneath it.",
     "The first time you play it, you will have to say \"tell me more\" to something that "
     "makes you want to fix it immediately. You say the words. You stay. The person goes "
     "somewhere they would not have gone if you had moved. What they say next is the "
     "real one, not the complaint, not the position, the feeling underneath it."),

    ("ch3.md",
     "Most allyship has the same problem I had on those calls.",
     "Most allyship has the same problem those calls had."),

    # ---- Move 2 · ch5, re-voiced to Sera Quill --------------------------------
    ("ch5.md",
     "I came up in traditions. Martial arts, church, academia: all of them Regent "
     "organizations,",
     "I came up in traditions. A house, an archive, a bench: all of them Regent "
     "organizations,"),

    ("ch5.md",
     "I belonged to a collective for a few years. Progressive, justice-focused, the "
     "right values on paper, and absolutely no governance.",
     "I sat some years with a body that had unwritten its own charter. The right "
     "principles, agreed and then struck, and no governance at all."),

    # The third site, beyond the spec's stated scope. See the docstring.
    ("ch5.md",
     "Martial arts and the church and watching things dissolve for twenty years actually "
     "prepare you for that.",
     "The house and the bench and watching things dissolve for twenty years actually "
     "prepare you for that."),
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
