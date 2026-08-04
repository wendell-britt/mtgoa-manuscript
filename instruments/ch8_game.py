# -*- coding: utf-8 -*-
"""
ch8_game.py — the two sites where the game does the teaching.

`The Game` is Grade 6, which licenses pattern verbs only. `teach` is
social-causal, severity 4. But the reason these two matter is not the grade --
it is that each one argues against the paragraph it sits in, and the book has
already written the corrected sentence elsewhere.

    ch8:387   The game taught you what it had to teach.      <- defect
    ch8:725   You learned what it had to teach.              <- same sentence, correct

Two passages about the same move, one chapter apart: the Liberator's alchemy at
387 and Put a Game Down at 725. One hands the capacity to the game, the other
keeps it with the reader.

------------------------------------------------------------------ 387, Liberator

The move is Joy -> Bliss, joy fused to the game, and its whole argument is
unfusing: "you notice that the joy has fused to this particular game rather than
to playing ... the aliveness was never the game's property. It was yours, it
travels." The defect sat one sentence before that turn and re-fused to the
object, handing the game a capacity the next line spends its energy taking back.

Wendell chose the completion beat over the plain mirror:

    Nothing is left in it you did not already get.

Harder than "You learned what it had to teach", and it does more work in
position -- it closes the account before the turn names where the aliveness
lived, so "was never the game's property" lands as confirmation rather than as
the first time the idea appears.

--------------------------------------------------------------- 731, the test

The test has to answer to the move's own body eight lines above it:
"Completion. The game ran its course. You learned what it had to teach."

    Can you name what you learned from it before you put it down?

Keeps the game present as the thing put down without making it the teacher, and
the two `it`s now point at the same referent, which the original already did in
its second half.

--------------------------------------------------------------------- NOT DONE

The Example at ch8:729 still reads "Say what it taught you before you set it
down." Under these two changes the move's body and test both say `you learned`
and the Example alone says `it taught you`, sandwiched between them. Flagged in
conversation, not among the two chosen, so not applied. The fix is ready:

    -> Say what you learned before you set it down.

Also left, and recorded so nobody re-flags them:

  "Do the work the game requires before you leave it." -- `require` is classed
  social-causal, but the sense here is structural entailment, the same as "the
  recipe requires flour". No mind, no counterparty. Third instance of the
  verb-sense problem after `meant` = signified and `asks for` = calls for.

  "The game read tells you what to do." -- the subject is the read YOU
  produced, and it is deliberately parallel with "The altitude read tells you
  how to say it." Not B6, which is clean across the whole book.

  "the fuel the game runs on" and "The game ran its course" -- mind-free
  directional verbs on a Grade 6 pattern. The shape that earned the field its
  six-verb license, but the game has no bodies generating it and does not
  inherit that argument. They flag until somebody rules otherwise.

    python3 instruments/ch8_game.py --dry
    python3 instruments/ch8_game.py
"""
import io, os, sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))
CH8 = "manuscript/ch8.md"

EDITS = [
    ("the ending is not the same as the failure. The game taught you what it had to teach.",
     "the ending is not the same as the failure. Nothing is left in it you did not already get."),

    ("Can you name what the game taught you before you put it down?",
     "Can you name what you learned from it before you put it down?"),
]


def main():
    dry = "--dry" in sys.argv
    full = os.path.join(ROOT, CH8)
    text = io.open(full, encoding="utf-8").read()

    for before, _a in EDITS:
        n = text.count(before)
        if n != 1:
            sys.exit("ABORT: anchor matched %d times, expected 1.\n  %s\nNothing written."
                     % (n, before[:96]))

    for before, after in EDITS:
        text = text.replace(before, after, 1)
        print("  --  %s" % before)
        print("  ++  %s" % after)

    if dry:
        print("\n--dry: %d edits verified, nothing written." % len(EDITS))
        return 0
    io.open(full, "w", encoding="utf-8").write(text)
    print("\nwrote %s, %d edits." % (CH8, len(EDITS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
