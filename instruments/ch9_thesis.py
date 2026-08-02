# -*- coding: utf-8 -*-
"""
ch9_thesis.py — ch9's thesis-contradiction sites, plus three W-2 escapees.

A thesis-contradiction site is one where the closing chapter hands agency to an
abstraction inside a sentence whose whole point is that the reader acts. They
cost more than their tier suggests, because the grammar contradicts the
argument in the same breath.

LEDGER_CH9.md ranks FIVE of them, not the three I had been reporting. This
instrument does three, and defers two with reason.

  #3  line 370  "Grow up: ask what the failure is actually telling you."
  #4  line 384  "Grow up: ask what this moment asks you to become."
  #5  line 640  the Last Rep's scenario Five

  DEFERRED
  #1  line 43   "The village taught that the six Faces named a destination."
  #2  line 51   "The village forgot that the Faces were a map, not a menu."

#1 and #2 are the fable's refrain -- "The village taught", "The village heard
the six Faces and thought", "The village forgot" -- three beats of a deliberate
pattern inside ~23 village instances in this chapter alone. R8 (village ->
villagers, the population reading) is the right conversion and is already in
the registry at Grade 1, but converting two beats of a refrain while the other
twenty-one instances still read "the village" makes the fable inconsistent with
itself. They move with the ch9 village set or not at all.

--------------------------------------------------------------------- the three

370 and 384 are the same defect fourteen lines apart: both restatements of the
WAVE put the reader in every stage as the actor -- notice, let, name, ask, do --
and then, in the Grow up stage only, hand the verb to an abstraction. The WAVE
is presented everywhere else as something the reader runs, not something that
runs on the reader.

The ledger proposed "ask yourself what you can learn from the failure" for 370.
That does not survive contact with the line, which already closes on "Then come
back: notice what shifted. What you learned." -- so `learn` is taken. It is
also flabbier than the four stages around it, none of which use "yourself".

`what you were wrong about` instead. Terse enough to sit beside "notice what
happened" and "name what didn't work", the reader is the actor, and it is a
genuine Grow-up question rather than a restatement of Clean up: Clean up names
what failed out in the world, Grow up asks what that says about you. It also
leaves the closing "What you learned" its own work to do.

384 has a second problem the ledger did not name: "ask what this moment asks
you" repeats the verb inside six words. Dropping the trailing prepositional
phrase entirely fixes the repetition and the agency in one move.

Scenario Five is the only one of the Last Rep's six moments with no person in
it. The other five open on "A director says", "A friend is telling you", "the
six people who joined most recently" -- and the drill's instruction is to read a
moment and name the Face it needs. You cannot name a Face for an organization.
The ledger proposed converting the single `watched`, which leaves `says`,
`will talk`, and two `want`s standing -- four more instances in five sentences.
Fixing one verb in a vignette that runs on five is a token, not a repair, so
this rewrites the vignette to put people in it.

--------------------------------------------------------- the three W-2 escapees

W-2 was ruled and reported closed at 22 sites. Its ch9 coverage was four, all of
the "this book has been teaching you" shape. These three survived:

  328  "the book would fail you"
  360  "The book refused to come clear."
  408  "the book would cheat you if it pretended"

360 was visible to the recall net and simply not included. 328 and 408 were
structurally invisible to it: `fail`, `cheat` and `pretend` are in no lemma list
in the registry, so the net cannot see them at any grade. The ledger caught all
three by reading, filing `fail`/`cheat` under "nearest lemma: abandon/betray".

328 and 408 are the exact shape W-2 ruled on -- the sentence opens the author's
chair ("Let me tell you honestly", "I want to name that directly") and then
hands the verb to the book one clause later. They take R4, to `I`.

360 is different and does not want `I`. The paragraph is already saturated with
it ("I didn't have it figured out", "I had a felt sense", "I sat in front of
chapters I could not write"), so another `I` flattens the rhythm and a second
"could not" lands two sentences from the first. `would not come clear` keeps the
book as subject while removing the will: a door that will not open is not a door
that refuses.

    python3 instruments/ch9_thesis.py --dry
    python3 instruments/ch9_thesis.py
"""
import io, os, sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))

EDITS = [
    # ---- thesis-contradiction #3 -------------------------------------------
    ("manuscript/ch9.md",
     "Grow up: ask what the failure is actually telling you.",
     "Grow up: ask what you were wrong about."),

    # ---- thesis-contradiction #4 -------------------------------------------
    ("manuscript/ch9.md",
     "Grow up: ask what this moment asks you to become.",
     "Grow up: ask who you are willing to become."),

    # ---- thesis-contradiction #5 -------------------------------------------
    ("manuscript/ch9.md",
     "One did most of the work on a campaign and watched the other take the press. "
     "The other says it was offered the interview, stole nothing, and is now under attack. "
     "Both will still talk to you. Both want you to say the other one is the problem.",
     "The organizers who did most of the work on a campaign watched the other group take "
     "the press. The other group's director says they were offered the interview, stole "
     "nothing, and are now under attack. Both sides will still talk to you. Each wants you "
     "to say the other one is the problem."),

    # ---- W-2 escapees ------------------------------------------------------
    ("manuscript/ch9.md",
     "because the book would fail you if it ended with a rousing speech about your "
     "potential and left you to figure out the rest alone.",
     "because I would be failing you if I ended this with a rousing speech about your "
     "potential and left you to figure out the rest alone."),

    ("manuscript/ch9.md",
     "The book refused to come clear.",
     "The book would not come clear."),

    ("manuscript/ch9.md",
     "because the book would cheat you if it pretended everyone leaves Chapter 9 with a "
     "fully-formed game.",
     "because I would be cheating you if I pretended everyone leaves Chapter 9 with a "
     "fully-formed game."),
]


def main():
    dry = "--dry" in sys.argv
    loaded = {}
    for path, before, _a in EDITS:
        full = os.path.join(ROOT, path)
        loaded.setdefault(full, io.open(full, encoding="utf-8").read())

    for path, before, _a in EDITS:
        full = os.path.join(ROOT, path)
        n = loaded[full].count(before)
        if n != 1:
            sys.exit("ABORT: %s anchor matched %d times, expected 1.\n  %s\nNothing written."
                     % (path, n, before[:88]))

    for path, before, after in EDITS:
        full = os.path.join(ROOT, path)
        loaded[full] = loaded[full].replace(before, after, 1)
        print("\n%s" % path)
        print("  --  %s" % before)
        print("  ++  %s" % after)

    if dry:
        print("\n--dry: %d edits verified, nothing written." % len(EDITS))
        return 0
    for full, text in loaded.items():
        io.open(full, "w", encoding="utf-8").write(text)
    print("\nwrote %d files, %d edits." % (len(loaded), len(EDITS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
