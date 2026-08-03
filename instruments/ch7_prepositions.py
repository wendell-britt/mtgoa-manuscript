# -*- coding: utf-8 -*-
"""ch7_prepositions.py — R-B, and the two agency defects it exposed.

Ruled by Wendell 2026-08-02, after the ch7:359 rewrite: "go, draft all three shapes
together", then "write the script with the abort-on-miss anchors."

`SPEC_FIELD_OF_BODIES_2026-08-02.md` §3, R-B: a field has no inside. The definition at
ch7:359 now reads *"what happens between people in relationship with each other… Everyone
there makes it"*, and every site below was written against the container reading it
replaced.

## Why the three shapes ship in one pass rather than three

The eight relocations in `ch7_field.py` were run apart from the ledger that had already
cleared some of those sites, and contradicted it. Splitting R-B the same way would repeat
the mistake at smaller scale, since all three shapes take their answer from one sentence.

**Shape 1, straight container — 6 edits.** Mechanical. Two are deletions: at 93 both
parties are already named and `in the field` carries nothing; at 77 Bridge is the one move
where arrival language is correct, because before Bridge there is no field to be inside of.

**Shape 2, motion verbs — 11 edits over 8 lines.** The shape that gains rather than
breaking even. You cannot leave a field you are generating; you stop generating it, and it
collapses. `ch7:351` said *disappear from the field entirely* and now says *withdraw until
there is no field left to hold*, which is the physics and also the Field-Holder's actual
failure. `ch7:361` loses a locative `put it there` for `said it for them`, which is truer:
the point was never placement, it was that the sentence was not yours to say.

**Shape 3, the six relocations from earlier today — 6 edits.** `at it` was the spec's
answer and it died with the table, because *at* wanted furniture. Each site takes the
nearest true noun instead. 343 takes `both camps`, which ch7 already owns at 33 instances
and which is what the Translator mediates between. The 669/673/677 refrain takes `the
people it concerns`, which is **already in the manuscript at 818** and matches the ledger's
own shipped fix at ch7:138, *"to the people who are then free to answer."* Reused rather
than varied across the three, per the original docstring's reasoning.

## Two sites that were agency defects, not prepositions

R-B only exposed these; they were already violations under the registry.

`ch7:181` — *"A field with no care in it cannot be told anything."* Speech class, Grade 6,
never licensed. The repair states the mechanism the previous sentence already set up
(*care maintains the only medium through which anything relational travels*): **Take the
care out and the field carries nothing.** `carries` is mechanical, which the trace does
license.

`ch7:379` — *"You tell the field in advance"* and *"a personal precedent that the field can
depend on."* Speech, and social-causal. Both route to the people.

## Not touched, on purpose

`ch7:236`'s *approaches every relational field as a transaction* — `approach` reads as
treating-something-as rather than walking-toward. `ch7:77`'s *sustained containment of a
whole field* is HOLD family, not a preposition. The `Hothouse Safety → Hardy Field` heading
at 363/365 stays unruled.

Anchors are exact and unique. A missed or duplicated anchor aborts with nothing written.
"""
import io, sys

P = "manuscript/ch7.md"

E = [
    # ---- Shape 3 · the six relocations from ch7_field.py -------------------
    ("let the people in the field decide what they can actually hold",
     "let everybody involved decide what they can actually hold"),

    ("is the one the people in the field can trust",
     "is the one both camps can trust"),

    ("makes it possible for the people in it to move through what they need to move "
     "through",
     "makes it possible for the people making it to move through what they need to move "
     "through"),

    # The three-part refrain. Same substitution each time, on purpose.
    ("said once and then left alone for the people in it to answer.",
     "said once and then left alone for the people it concerns to answer."),

    ("Then the people in it get to respond.",
     "Then the people it concerns get to respond."),

    ("left it alone for the people in it to answer.",
     "left it alone for the people it concerns to answer."),

    # ---- Shape 1 · straight container --------------------------------------
    ("Taking what one party in the field means",
     "Taking what one party means"),

    ("addressing harm that has occurred within the field without pretending the harm did "
     "not occur",
     "addressing harm one party did to another without pretending it did not occur"),

    # Agency, not preposition. See the docstring.
    ("A field with no care in it cannot be told anything.",
     "Take the care out and the field carries nothing."),

    ("Pick a live field with actual people in it,",
     "Pick a live field with actual people making it,"),

    ("everyone in the field becomes a means to an end",
     "everyone they make contact with becomes a means to an end"),

    ("in front of the people standing in it.",
     "in front of the people making it."),

    # ---- Shape 2 · motion verbs --------------------------------------------
    ("the act of showing up in the field with curiosity rather than judgment",
     "the act of showing up with curiosity rather than judgment"),

    ("they either escalate into the conflict or disappear from the field entirely.",
     "they either escalate into the conflict or withdraw until there is no field left to "
     "hold."),

    ("Their sentence is in the field now, and you could not have put it there.",
     "Their sentence is between all of you now, and you could not have said it for them."),

    ("From inside it looks like health.",
     "To everyone making it, it looks like health."),

    ("and the people in it learn to bring less of themselves to match.",
     "and the people making it learn to bring less of themselves to match."),

    ("the behavioral pattern of disappearing from the field the moment it becomes charged.",
     "the behavioral pattern of withdrawing the moment the field becomes charged."),

    ("a commitment to remaining in the field when it becomes charged.",
     "a commitment to staying present when the field becomes charged."),

    # Agency, not preposition.
    ("You tell the field in advance:",
     "You say so in advance:"),

    # Agency, not preposition.
    ("a personal precedent that the field can depend on.",
     "a personal precedent the people around you can depend on."),

    ("disappear into the field, or they keep perfect count and spend it",
     "disappear into the work, or they keep perfect count and spend it"),

    ("before you left the field instead of staying in it and disappearing.",
     "before you walked out instead of staying and disappearing."),
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
