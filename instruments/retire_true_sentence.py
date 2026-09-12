# -*- coding: utf-8 -*-
"""retire_true_sentence -- DL-92. The book stops selling a true sentence.

Wendell, 2026-09-09, on the line the previous ruling produced: *"'one true sentence:' this is the
main problem. We're suggesting that allyship is a function of truth and not presence. there is no
such thing as one true sentence. In the words of the tao te ching the name that can be named is
not the true and unchanging name. It's this statement that makes the sentence nonsense."*

WHY THE PREVIOUS FIX WAS THE WRONG FIX. DL-91 treated *"the true one"* as a grammar defect and
supplied the noun the pro-form was reaching for. **The noun was the defect.** Swapping *the right
words* for *one true sentence* keeps the council's own game and changes the winning script: there
is still a correct utterance out there and the reader's job is still to locate it. That is what
the council was doing for three years.

THE PARABLE ALREADY REFUTES IT, twice, in the book's own words. The council's words are true --
*"It named the suffering of the lower families with real feeling"* -- and they move nothing. And
four paragraphs on, the text says **"She brought them four sentences."** Not one. The count was
never the point and the book knew it in one paragraph and forgot it in the next.

WHAT THE MOVE ACTUALLY IS, and all three parts are already in the sentence that carried the
wrong noun: *what a part of you has already felt* (you were present to it), *to the face it
concerns* (you are present to them), *at the cost of being the person who said it* (you are
present after). **Presence and address, at cost.** The truth-object was never doing work; it was
sitting where the work is.

WHAT IS NOT TOUCHED. `the true read` in the Raise Awareness handbook stays. The objection lands
on naming, not on seeing, and a read that matches the room is the Shaman's whole faculty. The
book may say a perception is accurate. It may not sell a sentence as true.

THE CENSUS WAS WRONG THE FIRST TIME AND THE FIRST RUN WENT OUT ON IT. I read a truncated grep,
counted five sites, declared the scope complete, and the script wrote. The remaining five were in
that same grep output, cut off past column 220, and I classified them from the visible half. **The
completeness check passed, because completeness only asks whether the declared work happened.** It
was `retire_true_sentence.py`'s own closing count -- the phrase, re-counted in the corpus after
writing -- that said 5 where it should have said 0. Reverted, re-censused with a script instead of
an eye, and re-run at ten. Every ruling that asserts a scope should end by counting the thing it
claims to have removed.

    python3 instruments/retire_true_sentence.py
"""
import io, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ruling import guard                     # FR-E1

CLAIM = "DL-92"

HERE = os.path.dirname(os.path.abspath(__file__))
CH3 = os.path.join(HERE, os.pardir, "manuscript", "ch3.md")
CH7 = os.path.join(HERE, os.pardir, "manuscript", "ch7.md")

# 1 -- the parable's close. What moved the water was not a sentence's truth value. It was said to
# the one who could act, in front of people, so it could not be absorbed. And the correct words
# did reach his ears for three years; what they never did was ask him for anything.
OLD_1 = ("It moved because one true sentence reached the face that could change it. Three years "
         "of correct words never reached that face.")
NEW_1 = ("It moved because she said it to the man who could change it, out loud, with everyone "
         "watching. Three years of correct words had never asked him for anything.")

# 2 -- the chapter's landing. The object goes and nothing replaces it: the appositive was always
# the definition, and it names an act with an address and a cost rather than a thing to find.
OLD_2 = ("Allyship is saying one true sentence: what a part of you has already felt, what "
         "everyone already half-knows,")
NEW_2 = ("Allyship is saying what a part of you has already felt, what everyone already "
         "half-knows,")

# 3 -- the Alchemist handoff. The outcome is the read leaving the body, not a sentence scoring.
OLD_3 = ("all aimed at one outcome: one true sentence, out of your body and into the world, "
         "where it can move the water.")
NEW_3 = ("all aimed at one outcome: what you sensed, out of your body and into the world, where "
         "it can move the water.")

# 4 -- the win condition. Three sentences later the same paragraph already defines the win as
# the sentence that left your body and changed what was possible, which is this without the noun.
OLD_4 = ("The whole win at the Shaman's altitude is one true sentence, said to a person who can "
         "hear it, while it is still live.")
NEW_4 = ("The whole win at the Shaman's altitude is what you sensed, said out loud to a person "
         "who can act on it, while it is still live.")

# 5 -- the Controller worked example, three hundred lines earlier. The read is already the
# subject of the clause; the object was the same noun arriving to take credit for it.
OLD_5 = ("and you say the one true sentence, *\"Something here doesn't sit right with me. Can we "
         "slow down?\"*,")
NEW_5 = ("and you say what you clocked, *\"Something here doesn't sit right with me. Can we slow "
         "down?\"*,")

# 6 -- the inner voice at the moment of the move. It does not need a noun; it needs a verb.
OLD_6 = "*there it is, \"not ready.\" Noted. Here is the true sentence anyway.*"
NEW_6 = "*there it is, \"not ready.\" Noted. Saying it anyway.*"

# 7 -- the chapter's last paragraph, where the Shaman hands off to the other five faces. The
# paragraph says "the read" and "the reading" five times and then swaps in the object at the end.
OLD_7 = "and why one true sentence, said and not only felt, is the move everything else will"
NEW_7 = "and why the read, said and not only felt, is the move everything else will"

# 8 -- ch7's Refuse False Equivalence handbook.
OLD_8 = "you've said the hard true sentence and nothing has broken"
NEW_8 = "you've said the hard part out loud and nothing has broken"

# 9, 10 -- ch7's two statements of the Impact-without-Care failure state. "read" is ch3's
# vocabulary and appears nowhere in ch7 as a noun, so accuracy carries it instead. The book keeps
# accuracy: what it stops selling is a sentence that owns the truth.
OLD_9 = ("the true sentence said in a way that ends the possibility of saying the next one.")
NEW_9 = ("accurate, and said in a way that ends the possibility of saying anything after it.")

OLD_10 = "and the true sentence said in a way that ends the conversation."
NEW_10 = "and the accuracy that ends the conversation."

EDITS = [(CH3, OLD_1, NEW_1), (CH3, OLD_2, NEW_2), (CH3, OLD_3, NEW_3), (CH3, OLD_4, NEW_4),
         (CH3, OLD_5, NEW_5), (CH3, OLD_6, NEW_6), (CH3, OLD_7, NEW_7),
         (CH7, OLD_8, NEW_8), (CH7, OLD_9, NEW_9), (CH7, OLD_10, NEW_10)]


def norm(s):
    return " ".join(s.replace("*", "").split())


def main():
    guard(CLAIM, EDITS)                      # FR-E3

    staged = {}                              # keyed by path -- the retire_treatise bug
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
        before = io.open(path, encoding="utf-8").read()
        b, a = before, text
        for p, old, new in EDITS:
            if p != path:
                continue
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

    print("true sentence retired: %d span(s) across %d file(s), %d words in, %d out"
          % (len(EDITS), len(staged),
             sum(len(o.split()) for _, o, _ in EDITS),
             sum(len(n.split()) for _, _, n in EDITS)))
    print("remaining occurrences of the phrase in the corpus: %d"
          % sum(io.open(p, encoding="utf-8").read().lower().count("true sentence")
                for p in staged))


if __name__ == "__main__":
    main()
