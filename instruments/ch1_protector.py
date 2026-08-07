# -*- coding: utf-8 -*-
"""ch1_protector.py — ch1:50, the passage rewritten in Wendell's words, out of the
Controller's vocabulary, with Seligman credited.

Ruled by Wendell 2026-08-03, in three turns. First the replacement prose, in his hand:

> *"Even though they are close enough to touch, that doesn't mean you can control them. Not
> the friends who votes the wrong way, the parents and their casually racist comments. The
> coworker constantly transacting in micro-agressions: Trying to fix these people will be a
> painful lesson in learned helplessness."*

Then the canon collision: *"We're colliding into controller territory. The protector
protects and the controller controls. 'control' protect you from what you can, including
those nearest to you."* Then: *"go ahead and cite selligman and remove the mascot image."*

## The collision, and why it is a real one

`ch3:689` draws the line: *"The Protector decides whether you live. The Controller decides
how. It sets the standard."* The old sentence called this drive **control**, which assigns
it to the wrong daemon. Nothing here sets a standard. The drive is defensive.

And **ch2 already runs this exact mechanism** four hundred lines later — `ch2:318`: *"the
reason you end up walking on eggshells with everyone, including the people who have never
once been a threat."* Wendell's *"including those nearest to you"* is that sentence
arriving early. So ch1:50 was not merely using a loose verb; it was foreshadowing the wrong
part, and the right one was already written.

## The mascot

*"each one becomes a mascot for the helplessness you never worked through"* is cut on his
instruction. Worth recording what the trade was, because it is not free: the mascot was the
only one in the chapter and it was a good picture. It named a **category** — these people
stand in for a feeling. Wendell's version names a **consequence**: trying to fix them
teaches you the helplessness. A consequence carries the burnout thesis; a category does
not.

## Seligman

`learned helplessness` is Seligman's coined term and was new to the manuscript. The book's
convention is an in-text parenthetical plus an Appendix G entry — `ch1:103` credits Chou
that way, and `citation_audit.py` looks for an owner within 400 characters. Both land here:
the parenthetical, the appendix entry beside Chou (Chou explains what pulls a person back;
Seligman explains what makes them stop trying), and the `BORROWED` row so the audit can
see it from now on.

## Mechanical fixes to his text, all flagged to him before applying

`who votes` → `who vote`; `micro-agressions` → `microaggressions`; `Trying` → `trying`,
since ch1's only capital after a colon is a proper noun. His `doesn't` is kept: contractions
run 12 to 35 in ch1, so it is in-bounds.

One restatement survives and he can trim it: *the people nearest to you* is followed by his
*close enough to touch*. Left in because his sentence needs an antecedent for `they` and his
concessive needs its own phrase to turn on.

Anchors are exact and unique. A missed or duplicated anchor aborts with nothing written.
"""
import io, sys

EDITS = [
    ("manuscript/ch1.md", [
        ("Left unmetabolized, it turns into a drive to control what you can, and what you "
         "can control is the people close enough to touch. The friend who votes wrong, the "
         "parent whose politics make you wince, the coworker who says the outdated thing "
         "in the meeting: each one becomes a mascot for the helplessness you never worked "
         "through.",

         "Left unmetabolized, it turns into a drive to protect you from what it can, "
         "including the people nearest to you. Even though they are close enough to touch, "
         "that doesn't mean you can control them. Not the friends who vote the wrong way, "
         "the parents and their casually racist comments. The coworker constantly "
         "transacting in microaggressions: trying to fix these people will be a painful "
         "lesson in learned helplessness. (Martin Seligman named it: what sets in after "
         "enough tries that changed nothing.)"),
    ]),
    ("appendices/ON_THE_SHOULDERS_OF.md", [
        ("**C. Thi Nguyen**",
         "**Martin Seligman** is where *learned helplessness* comes from: the state that "
         "sets in after enough attempts that changed nothing, at which point trying stops "
         "even once trying would work. Chapter 1 uses it for what happens when the "
         "suffering that moves you is out of reach and the people in reach are the ones "
         "you try to fix instead. Chou explains what pulls a person back to a game; "
         "Seligman explains what makes them stop playing.\n\n**C. Thi Nguyen**"),
    ]),
    ("instruments/citation_audit.py", [
        ('    (r"polarity map|both/and", "Johnson"),',
         '    (r"polarity map|both/and", "Johnson"),\n'
         '    # Added 2026-08-03 with ch1:50. Wendell: "go ahead and cite selligman."\n'
         '    (r"learned helplessness", "Seligman"),'),
    ]),
]


def main():
    for path, edits in EDITS:
        t = io.open(path, encoding="utf-8").read()
        for i, (a, _b) in enumerate(edits, 1):
            n = t.count(a)
            if n != 1:
                sys.exit("%s E%d anchor matched %d times, expected 1: %r"
                         % (path, i, n, a[:60]))
    for path, edits in EDITS:
        t = io.open(path, encoding="utf-8").read()
        for a, b in edits:
            t = t.replace(a, b)
        io.open(path, "w", encoding="utf-8").write(t)
        print("%s — %d edit(s) applied" % (path, len(edits)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
