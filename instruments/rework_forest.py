# -*- coding: utf-8 -*-
"""rework_forest -- DL-87. Rebuild ch3's "What You Take Out of the Forest".

Wendell, 2026-09-09: *"the 'what you take out of the forest' section is almost word salad. I have
no idea what it's saying how it's supposed to help the reader. We need to fix it."*

He had written **Rework** by hand against this whole section on the printed proof. Five of its
lines were separately highlighted, the five were changed in earlier tranches, and the section note
was read as their sum. It was not: a note against a section is a scope, and applying it sentence
by sentence is DL-78 one level up.

WHY IT WAS SALAD. All six Face chapters run the same four-beat close — what the healed daemon
gives you, the handoff to the superpower, a takeaway, then other people's version. ch4 executes it
cleanly. **ch3 is the only one whose beats were individually reworded**, and each rewording broke
its beat. The takeaway is the clearest case: *"You know what your Controller is for now. That is
what you take out"* was marked, and the rewording produced *"What you take out is what your
Controller is for"*, which defines the takeaway as the thing it is the takeaway of.

FOUR ROUNDS OF WENDELL'S CORRECTIONS ARE IN THIS TEXT, each naming a defect no counter caught:

  - *"does what nothing else in this chapter can"* — falsifiable, unhelpful, and it throws away
    what everything else in the chapter did. Cut, not replaced.
  - *"is not something a feeling decides"* — a negation, and it hands a feeling agency.
  - *"What chooses is a rule you set on a clearer day"* — vague passive hiding that the chooser is
    **you**, earlier. Named.
  - *"you spend it"* — an empty phrase. The action is saying it, to the face it concerns, while
    still afraid. Named.
  - *"the true sentence"*, *"the true one"* — definite articles over nouns the reader was never
    given, lifted out of the parable forty lines up that licensed them.
  - *"the Alchemist"* stays: it is a named title.

Eleven definite articles in the draft went to four, and the four that remain are the named title,
the chapter's own canon phrase, and two with antecedents in the parable the reader just finished.

    python3 instruments/rework_forest.py
"""
import io, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ruling import guard                     # FR-E1

CLAIM = "DL-87"                              # the ruled fact in instruments/claims.yaml

HERE = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(HERE, os.pardir, "manuscript", "ch3.md")

OLD = """The Controller developed does what nothing else in this chapter can do: it admits a feeling onto the field and holds you to a line in the same motion. Those two rarely travel together. The Shaman's move needs both at once: the reading let all the way in, and something in you that will not let you leave the table with it unsaid.

That is what the Alchemist runs on. You cannot burn a charge you never let yourself have. You will not spend one while the fear is still live unless some part of you enforces a rule you set on a clearer day. The woman at the council had both. The rule won, which is a referee doing its job rather than a feeling that finally got loud enough.

What you take out is what your Controller is for.

Other people's Controllers do the same job in a Forest you cannot see into. A stranger's Controller enforces a rulebook you have never read, so it fires when you arrive holding a better standard, and it opens when you meet the one they already keep. Keeping their rule is how you earn clearance with it."""

NEW = """Your Controller, once you develop it, lets a feeling run its whole length and still holds you to your own rule. Most people manage one. They feel it clearly and say nothing, or they say correct words with nothing running underneath them.

The Alchemist needs both. Let a charge finish and you know what is actually happening. Hold your rule and you say so to the face it concerns, while you are still afraid, because you decided on a calmer day that you would. The woman on that council had both. She read that circle accurately for three seasons and said nothing. When she finally spoke, she named whose plan had moved the river, to his face, in front of everyone. She was no readier than she had been.

You came into this section with a critic. You leave with a referee. You write its rulebook.

A stranger has a Controller too, working in a Forest you cannot see into. It enforces a rulebook you have never read. It fires when you arrive holding a standard they never agreed to. It opens when you keep a standard they already hold. Meet their rule first. Your standard travels afterward, or it does not travel at all."""

# One declared edit, four paragraphs. Declared as (old, new) so the change is addressable
# rather than merely counted -- the shape SPEC_WRITE_CONTRACT_2026-09-09 asks for.
EDITS = [(OLD, NEW)]


def norm(s):
    return " ".join(s.replace("*", "").split())


def main():
    guard(CLAIM, EDITS)                      # FR-E3

    before = io.open(P, encoding="utf-8").read()
    if before.count(OLD) != 1:
        sys.stderr.write("REFUSED: the section matched %d times (need 1). Nothing written.\n"
                         % before.count(OLD))
        sys.exit(2)
    after = before.replace(OLD, NEW, 1)

    # Containment, by hand until the write contract exists: nothing outside the declared span
    # may differ. This is the check that caught two silent failures today.
    if norm(before.replace(OLD, "")) != norm(after.replace(NEW, "")):
        sys.stderr.write("REFUSED: prose changed outside the declared span. Nothing written.\n")
        sys.exit(3)
    # Completeness: the declared edit actually took.
    if OLD in after or NEW not in after:
        sys.stderr.write("REFUSED: the declared edit did not take. Nothing written.\n")
        sys.exit(4)

    io.open(P, "w", encoding="utf-8").write(after)
    print("What You Take Out of the Forest rebuilt: %d words in, %d out"
          % (len(OLD.split()), len(NEW.split())))


if __name__ == "__main__":
    main()
