# -*- coding: utf-8 -*-
"""ch3_true.py — the `true thing` family, swept. Option b.

Ruled by Wendell 2026-08-03: *"b then sweep the rest."* Option b was: **keep the move name,
sweep the rest — accepting that the title then uses a word the prose doesn't.**

So `Say the Thing Under the Thing` survives at all five of its sites, and the thirty
surrounding instances of the construction come out.

## The replacement system, and why nothing is imported

One substitution across the whole family, so the chapter keeps one vocabulary. Every word
used here is already ch3's:

| | count in ch3 | takes |
|---|---:|---|
| `sentence` | 23 | `the true thing` → **the true sentence** |
| `right words` | 5 | `the right thing` in the true/right pairing → **the right words** |
| `the surface` | 3 | `the beautiful thing` → **the beautiful surface** |

The `right words` swap is the one that pays twice. `ch3:754` already reads *"the council had
the right words, and the right words were the wall,"* and `ch3:895` *"it cost you the cover
of the right words."* The Raise Awareness heading was pairing `true thing` against `right
thing` while the chapter's actual pairing, three lines away, was **true against right
words**. The placeholder was standing on top of the real antithesis.

`the beautiful surface` links the parable's verdict to `ch3:891`'s *"the one who never
breaks the surface"* and `ch3:903`'s *"the comfort of the polite surface"* — a connection
the chapter had already built and the placeholder was hiding.

## Two sites where `sentence` reads wrong and `what` is used instead

`ch3:895` — *the group met the real thing* → *the group met what was true*. A group meets a
truth, not a sentence.

`ch3:903` — *you named the unsaid thing the whole coalition feels* → *you named what the
whole coalition feels*. A coalition does not feel a sentence.

## The cost of option b, on the record

The chapter now teaches **the true sentence** in its prose and names the move **Say the
Thing Under the Thing**. That gap is what Wendell accepted when he chose b over a. It is
visible at `ch3:850`, `ch3:962` and `ch3:981`, where the move title sits within a few lines
of the new vocabulary.

Anchors are exact and unique. A missed or duplicated anchor aborts with nothing written.
"""
import io, sys

P = "manuscript/ch3.md"

E = [
    ("You say the thing that needed saying",
     "You say the sentence that needed saying"),

    ("Here is the true thing anyway.",
     "Here is the true sentence anyway."),

    ("without having said the one true thing.",
     "without having said the one true sentence."),

    ("to say the true thing was to cross the man at the head of the circle",
     "to say the true sentence was to cross the man at the head of the circle"),

    ("said the true thing, to his face, in front of everyone",
     "said the true sentence, to his face, in front of everyone"),

    # links to "the one who never breaks the surface" and "the polite surface"
    ("the one who broke the beautiful thing.",
     "the one who broke the beautiful surface."),

    ("Then the true thing sat in the circle",
     "Then the true sentence sat in the circle"),

    ("Allyship is saying the true one, the thing a part of you has already felt",
     "Allyship is saying the true one, the sentence a part of you has already felt"),

    ("when the true thing sits in her chest",
     "when the true sentence sits in her chest"),

    ("A true thing said an hour late is a different move.",
     "A true sentence said an hour late is a different move."),

    ("Direct Action, the true thing said to a face.",
     "Direct Action, the true sentence said to a face."),

    # Five instances in one sentence; replaced whole.
    ("Both keep the true thing unsaid. The four domains are where it finally leaves: the "
     "true thing said to a face, the true thing said out loud in place of the right thing, "
     "the honest need named and asked for, the unsaid thing put on the table so a group "
     "can work.",
     "Both keep the true sentence unsaid. The four domains are where it finally leaves: "
     "the true sentence said to a face, the true sentence said out loud in place of the "
     "right words, the honest need named and asked for, the unsaid sentence put on the "
     "table so a group can work."),

    ("When you say the true thing, what you do next decides",
     "When you say the true sentence, what you do next decides"),

    ("You name the real thing and the read tells you it landed",
     "You say the true sentence and the read tells you it landed"),

    ("**Direct Action — the true thing said to the face**",
     "**Direct Action — the true sentence said to the face**"),

    ("you said the one true thing you had been feeling",
     "you said the one true sentence you had been feeling"),

    ("The proof is that the true thing existed between you",
     "The proof is that the true sentence existed between you"),

    # The chapter's own antithesis, three lines away, was true against RIGHT WORDS.
    ("**Raise Awareness — the true thing over the right thing**",
     "**Raise Awareness — the true sentence over the right words**"),

    ("the group met the real thing and not the performance of it",
     "the group met what was true and not the performance of it"),

    ("**Skillful Organizing — the thing the group won't say**",
     "**Skillful Organizing — the sentence the group won't say**"),

    ("you named the unsaid thing the whole coalition feels",
     "you named what the whole coalition feels"),

    ("The proof is that the unsaid thing got onto the table",
     "The proof is that the unsaid sentence got onto the table"),

    ("Did you say the true thing to change the moment",
     "Did you say the true sentence to change the moment"),

    ("Did you name the unsaid thing to free the work",
     "Did you name the unsaid sentence to free the work"),

    ("say the true thing, the doubt speaks up first",
     "say the true sentence, the doubt speaks up first"),
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
    print("ch3.md — %d edits applied" % len(E))
    return 0


if __name__ == "__main__":
    sys.exit(main())
