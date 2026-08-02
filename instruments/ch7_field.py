# -*- coding: utf-8 -*-
"""ch7_field.py — the eight ch7 sites where the field takes a mind-verb.

Ruled by Wendell 2026-08-02: "do the ch7 field sites."

**R8 has no role here, and that is the finding rather than a caveat.**
`R8_TEST_CH7_GLOSSARY.md`: *"It is not a hard case of R8 — it is a category mismatch…
'The fields knew' is not a strained instance of R8, it is not English."* The village is a
population; the field is a medium. Pluralizing needs members to count and the field has
none.

## Why ~30 of the field's ~40 sites were never defects

ch7:359 defines the term on the page: *"The field is what sits between the people at it,
and it lasts only as long as they are all still there."* Under C1 that is a real trace, and
it licenses pattern, directional and mechanical verbs — *pushes, holds, gets clearer, stays
warm, costs more.* The registry amendment adding `the field` to Grade 6 is already on
master and resolves those.

**What the trace cannot bear is cognition.** A thing whose entire definition is *it exists
because you are all still there* cannot independently know, decide, need, trust, or be free
to answer, because freedom presupposes a chooser with continuity of identity and this
entity's defining trait is that it has none. That leaves the eight sites below.

## The repair, and the one place it goes flat

Relocation to participants, ranked first by the test and holding on every site it was
tested against: *the field* → *the people in the field* / *the people in it* / *they*. Cost
is one to five unstressed syllables inside sentences of twenty to forty words.

`ch7:669`, `ch7:673` and `ch7:677` are the same refrain three times over. The substitution
is **deliberately not varied** across them — the test's own reasoning: reused rather than
varied, it reads as one fix carried through a callback device rather than a drumbeat.

`ch7:140` is the one shape relocation goes flat against, and it takes R6 instead.
*"The people in the field who do not know what your staying requires"* is grammatically
legal and structurally inert — it buries the point, which is that nobody told **this
specific person**, inside a crowd noun phrase. The R6 version makes the sentence more true:
it answers *who failed to know* with a nameable absence.

## Already done, and not repeated here

`ch7:138` — *"offered as information, once, to the people who are then free to answer"* —
came through the master merge with the ledger's R1 fix already applied. It is the chapter's
own definition of its own key term and the test calls it the single highest-value repair in
the book.

## The repair that was rejected, because the reasoning is worth keeping

R2, mechanize, ranked worst: *"…offered as information, once, into a field left open to
receive it."* Grammatical, and it sounds like the register. It is also wrong. The whole
distinction the chapter draws — an ultimatum removes the other party's freedom to answer,
an honest term gives it back — depends on *answer* naming an act only a chooser can
perform. **The repair fixes the grammar and kills the concept it was checking for.**

Anchors are exact and unique. A missed or duplicated anchor aborts with nothing written.
"""
import io, sys

P = "manuscript/ch7.md"

E = [
    ("the willingness to let the field decide what it can actually hold",
     "the willingness to let the people in the field decide what they can actually hold"),

    # R6, not relocation. See the docstring.
    ("A field that does not know what your staying requires has never once had the chance "
     "to choose you.",
     "A person who was never told what your staying requires has never once had the chance "
     "to choose you."),

    ("Am I bridging because the field needs me",
     "Am I bridging because someone here actually needs me"),

    ("is the one the field can trust",
     "is the one the people in the field can trust"),

    ("makes it possible for the field to move through what it needs to move through",
     "makes it possible for the people in it to move through what they need to move "
     "through"),

    # The three-part refrain. Same substitution each time, on purpose.
    ("said once and then left alone for the field to answer",
     "said once and then left alone for the people in it to answer"),

    ("Then the field gets to respond.",
     "Then the people in it get to respond."),

    ("said it once, and left it alone for the field to answer",
     "said it once, and left it alone for the people in it to answer"),
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
