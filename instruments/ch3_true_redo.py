# -*- coding: utf-8 -*-
"""ch3_true_redo.py — undo the term, use verbs and pronouns instead.

Wendell 2026-08-03, on the substitution table from the previous commit: *"these all still
have the problem of using the definite article to get the point across. It's better than
thing, but still doesn't solve for the whole problem. Also the true sentence doesn't land
right. The issue is coming from the back we are being robotic about what spoken truth is."*

Then, on `the beautiful surface` → `the beautiful warmth`: *"what the hell is a beautiful
warmth? warmth can be comfortable or delicious but not beautiful."*

## Two errors, and the second is the one worth keeping

**One.** `the true thing` → `the true sentence` changed the head noun and kept the
construction. `the X` still asserts the reader knows which one. A more specific-sounding
placeholder is still a placeholder.

**Two, and this is the real finding.** Picking one label and stamping it across 25 sites
turned *a person saying something hard, at cost, to a face* into an object with a name.
**Consistency was the error.** The instruments reward uniformity and the prose does not
want a term at all, because spoken truth is an act and it happens differently every time.

**The rule that comes out of it:** when a repair needs a subject or an object, reach for a
pronoun with a real antecedent, or a verb. A new noun is the last resort. **And if every
site takes the same new noun, that is the signal the sentence wanted a verb.**

## The chapter was already doing it right

`ch3:752` — *"It moved because one sentence was true and said to the face that could change
it. The correct words, for all their beauty, never were."* Predicate adjective, not a
modifier on a noun, and the antithesis is `true` against `correct`, which ch3 runs at seven
sites.

`ch3:895` — *"you said what was actually happening, the read under the approved language,
to the real people who needed to hear it."* No placeholder anywhere in it.

And every move in the chapter is an imperative — *Catch It Before the Story · Turn the Dial
Up · Name the Channel Out Loud · Say What You Can Do Now* — so the four domain glosses
become verbs here rather than nouns sitting under a system of verbs.

## `the beautiful words`, and the same mistake twice

`ch3:750`'s referent is named in the parable's opening line, `ch3:742`: *"There is a council
that meets when the season turns, and it has beautiful words."* Reused at 746 — *"So she
said the beautiful words too"* — and paid off at 752 — *"The correct words, for all their
beauty, never were."*

I invented `surface`, then invented `warmth`, with the answer eight lines above. Identical
to `ch1:113`, where the word `fuel` was sitting in the sentence between the two placeholders
being replaced. **The definite article is legal here** because the antecedent is real and
established, which is the first of the four legal cases.

Anchors are exact and unique. A missed or duplicated anchor aborts with nothing written.
"""
import io, sys

P = "manuscript/ch3.md"

E = [
    ("You say the sentence that needed saying",
     "You say what needed saying"),

    ("without having said the one true sentence.",
     "without anyone saying what was true."),

    # The sentence before it is "It was not."
    ("to say the true sentence was to cross the man at the head of the circle",
     "to say so was to cross the man at the head of the circle"),

    # The words themselves follow immediately after the colon.
    ("said the true sentence, to his face, in front of everyone:",
     "said it, to his face, in front of everyone:"),

    # ch3:742 — "it has beautiful words". Named in the parable's first line.
    ("the one who broke the beautiful surface.",
     "the one who broke the beautiful words."),

    ("Then the true sentence sat in the circle",
     "Then it sat in the circle"),

    ("Allyship is saying the true one, the sentence a part of you has already felt",
     "Allyship is saying the true one, what a part of you has already felt"),

    ("when the true sentence sits in her chest",
     "when the read sits in her chest"),

    ("A true sentence said an hour late is a different move.",
     "Said an hour late, it is a different move."),

    ("Direct Action, the true sentence said to a face.",
     "Direct Action, said to a face."),

    # The antecedent is "the read", one sentence up.
    ("Both keep the true sentence unsaid. The four domains are where it finally leaves: "
     "the true sentence said to a face, the true sentence said out loud in place of the "
     "right words, the honest need named and asked for, the unsaid sentence put on the "
     "table so a group can work.",
     "Both keep it unsaid. The four domains are where it finally leaves: said to a face, "
     "said out loud instead of the correct version, named as a need and asked for, put on "
     "the table so a group can work."),

    ("When you say the true sentence, what you do next decides",
     "When you say it, what you do next decides"),

    ("You say the true sentence and the read tells you it landed",
     "You say it and the read tells you it landed"),

    # The domain glosses become verbs, matching the chapter's imperative move names.
    ("**Direct Action — the true sentence said to the face**",
     "**Direct Action — you say it to their face**"),

    ("you said the one true sentence you had been feeling",
     "you said what you had been feeling"),

    ("The proof is that the true sentence existed between you",
     "The proof is that it existed between you"),

    ("**Raise Awareness — the true sentence over the right words**",
     "**Raise Awareness — true instead of correct**"),

    ("**Skillful Organizing — the sentence the group won't say**",
     "**Skillful Organizing — you say what the group won't**"),

    ("The proof is that the unsaid sentence got onto the table",
     "The proof is that it got onto the table"),

    ("Did you say the true sentence to change the moment",
     "Did you say it to change the moment"),

    ("Did you name the unsaid sentence to free the work",
     "Did you name what nobody would say to free the work"),

    ("The moment you take it into the world and say the true sentence, the doubt speaks up "
     "first",
     "The moment you take the read into the world and say it out loud, the doubt speaks up "
     "first"),
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
