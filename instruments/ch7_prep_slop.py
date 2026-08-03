# -*- coding: utf-8 -*-
"""ch7_prep_slop.py — the five slop findings against R-B's own new strings.

Ruled by Wendell 2026-08-02: "all five", after `/no-ai-slop` was run in detect mode
against the 23 strings `ch7_prepositions.py` introduced and returned findings against
four of them plus one referent wobble.

**Every one of these is a defect the preposition pass created.** None is pre-existing. The
pattern is worth naming because it will recur on any mechanical sweep: a batch that
substitutes one correct phrase across twenty sites produces word-repetition inside
paragraphs that no single-site check can see, because each substitution is correct in
isolation and the collision only exists in the neighbourhood.

`ch7:97` — robotic rhythm. R-B put *one party did to another* two bullets away from 93's
existing *one party… another party*. Adjacent items in the Faces list, same shape, reads
as a form. Takes a named agent instead, which is also what C1 wanted.

`ch7:236` — the paragraph already ran `makes contact` and `contact-for-contact's-sake`.
R-B added a third. *everyone they meet* keeps the agent the fix was there to restore.

`ch7:351` — the following sentence is *"They can hold the good conditions; they cannot hold
the bad ones."* R-B's *no field left to hold* put a third `hold` immediately before it. Two
words come off and the physics is unchanged: the field ends because the source withdrew.

`ch7:365` — both R-B edits on that line landed on `making it`, four sentences apart. The
first one moves. *keeping it that way* echoes the paragraph's own opening (*a field you
keep so comfortable*) and assigns the agency that sentence was missing, so this is a
better sentence rather than a rotated synonym. The second stays: `making it` is the
definition's own verb and repeating the clear word is correct.

`ch7:361` — referent wobble, and the only one of the five that is not repetition. *all of
you* includes the reader; the `you` four words later means the reader alone. *everyone*
resolves it without touching the clause that carries the point.

Anchors are exact and unique. A missed or duplicated anchor aborts with nothing written.
"""
import io, sys

P = "manuscript/ch7.md"

E = [
    ("The work of addressing harm one party did to another without pretending it did not "
     "occur",
     # `actually` came out on a second read: it is an empty adverb doing nothing that
     # "without pretending it did not occur" does not already do.
     "The work of addressing harm somebody did, without pretending it did not occur"),

    ("everyone they make contact with becomes a means to an end",
     "everyone they meet becomes a means to an end"),

    ("or withdraw until there is no field left to hold.",
     "or withdraw until there is no field left."),

    ("To everyone making it, it looks like health.",
     "It looks like health to everyone keeping it that way."),

    ("Their sentence is between all of you now,",
     "Their sentence is between everyone now,"),
]


def main():
    t = io.open(P, encoding="utf-8").read()
    for i, (a, _b) in enumerate(E, 1):
        n = t.count(a)
        if n != 1:
            sys.exit("E%d anchor matched %d times, expected 1: %r" % (i, n, a[:70]))
    for a, b in E:
        t = t.replace(a, b)
    io.open(P, "w", encoding="utf-8").write(t)
    print("ch7.md — %d edits applied" % len(E))
    return 0


if __name__ == "__main__":
    sys.exit(main())
