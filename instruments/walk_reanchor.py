# -*- coding: utf-8 -*-
"""
The Walk — three re-anchors, two cuts, two clauses. The last bars-engine sites.

Wendell 2026-08-01: *"the founder's move is writing the book."* The handoff scoped The
Walk for wholesale replacement by `SPEC_CH9_REWRITE_V1` §9's ~260-word page. Measured,
that is the wrong operation, and the measurement is why:

    teaching Jordan can use   2,785 words   75%
    memoir, the 2020 course     573 words   16%
    pure product routing        331 words    9%

The spec's premise -- *"5,144 words of Wendell building bars-engine"* -- does not survive
contact with the text. Only 331 words are product. Deleting the rest would take **What If
You Don't Have a Game Yet?** (the passage that catches a reader who finishes without a
Founder move), **What If You're Not a Founder?** (which finds the move in her own
history, and is what makes the chapter reachable for a parent or a teacher), the
eight-gate scan (The Walk's only exercise), and the rehearsal-versus-doing teaching. None
of those mention the app. The ruling asks for the references to go, not for the chapter
to.

**The 573-word memoir is untouched.** It carries no bars-engine reference at all -- it is
about the 2020 course -- and it is the chapter's only worked example of a Founder move
failing, where last night's shame testimony and `ch1:119`'s applause counter both land.

**Re-anchors, sourced.** `ch9:360` takes `ch1:109`, *"sitting in front of a chapter I
could not write with no way to tell tired from done."* `ch9:368`'s last clause points
back at 360, exactly as the original pointed back at its own *sessions that failed*.
`ch9:396` needs almost nothing: the problem it states -- people who understand the theory
and still have no practice -- is the book's problem in the book's words.

**Cuts.** `ch9:402` and `ch9:468` are the same paragraph twice: the common ground, the
campaigns, the non-profit, join the structure. Jordan gets nothing either time. The first
leaves the section ending on *"What's yours?"*; the second leaves `ch9:466`, *"The
village doesn't need your perfection. It needs your willingness to go first,"* which is
the teaching without the product.
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

CUT1 = (
    "When you're ready, a place waits for you. Bars-engine is the village's common "
    "ground: the playground where players arrive after finishing the book, where the "
    "allyship work becomes real. Campaigns. Quests. Allyship programs run through the "
    "non-profit. A structure people already started building before you got here, with "
    "space for what you're going to add. You don't have to build bars-engine from "
    "scratch. You don't have to build the infrastructure alone. You bring your specific "
    "gift. The structure plugs in around it. The village already stands there, doing "
    "the work, and what you make fits into what they're doing.\n\nWalking into the "
    "specific problem looks like this when you're ready: not figuring out how to start "
    "from nothing, but finding where you fit in something that's already alive. The "
    "game is bigger than any one person. That's the point. That's the gift.\n\n---\n\n"
)

CUT2 = (
    "**You don't have to build alone.**\n\nHere's what I want you to know before you "
    "go.\n\nThe village is not just the people who will receive what you build. The "
    "village is the people already building. Bars-engine works as more than a solo "
    "project: a structure already alive before you finished this book. Campaigns run. "
    "Quests stay active. Players show up. Space remains for what you're going to "
    "add.\n\nYou don't have to figure out how to start from nothing. You don't have to "
    "build the whole thing yourself. You bring your specific gift: the thing this book "
    "helped you name, the thing you figured out how to do by walking your own terrain. "
    "Other people bring theirs. The game is bigger than any one person.\n\nThe "
    "non-profit holds all of this, built so that individual Founder moves plug into a "
    "larger architecture. So that one person's practice connects to everyone else's. So "
    "that when you make something, it lives somewhere the people who need it can find "
    "it.\n\nThe village already stands out there, and you walk into it rather than "
    "found it. The question comes down to where you fit in, and that's something you'll "
    "only discover by walking into it.\n\n---\n\n"
)

E = [
    # ---- re-anchor 1 · ch9:360 -----------------------------------------------
    ("ch9.md",
     "When I started building bars-engine, I didn't have it figured out. I had a felt "
     "sense of what was missing (a game that actually taught the WAVE, that made the "
     "emotional alchemy something you could practice instead of just understand), and I "
     "had enough of the six Faces to know what I was trying to do. The game itself "
     "refused to come clear, and the mechanics kept changing. I ran sessions that "
     "failed. I redesigned the token economy three times. I threw out entire systems "
     "and rebuilt them.",
     "When I started writing this book, I didn't have it figured out. I had a felt "
     "sense of what was missing (a practice that actually taught the WAVE, that turned "
     "the emotional alchemy into moves you could run instead of only understand), and I "
     "had enough of the six Faces to know what I was trying to do. The book refused to "
     "come clear. The shape kept changing. I sat in front of chapters I could not write "
     "with no way to tell tired from done, and I started them again anyway."),

    # ---- re-anchor 2 · ch9:368 -----------------------------------------------
    ("ch9.md",
     "Every version of bars-engine was the walk, not a step toward it. The first design "
     "was the walk. The third redesign was the walk. The version that failed in front "
     "of people was the walk.",
     "Every draft of this book was the walk, not a step toward it. The first draft was "
     "the walk. The third rewrite was the walk. The chapter I could not write was the "
     "walk."),

    # ---- re-anchor 3 · ch9:396 -----------------------------------------------
    ("ch9.md",
     "My specific problem, the one I designed bars-engine to solve:",
     "My specific problem, the one I wrote this book to solve:"),

    ("ch9.md",
     "Everything I build (this book, bars-engine, the next thing) walks me further into "
     "that specific problem.",
     "Everything I make walks me further into it."),

    # ---- the two routing cuts -------------------------------------------------
    ("ch9.md", CUT1, ""),
    ("ch9.md", CUT2, ""),

    # ---- two clauses ----------------------------------------------------------
    ("ch9.md",
     "You don't have to build bars-engine. You don't have to start a nonprofit.",
     "You don't have to write a book. You don't have to start a nonprofit."),

    ("ch9.md", " Find it. Capture it. Bring it into the app.", " Find it. Capture it."),
]


def main():
    files, bad = {}, []
    for name, old, new in E:
        files.setdefault(name, io.open(os.path.join(MS, name), encoding="utf-8").read())
        n = files[name].count(old)
        if n != 1:
            bad.append("%s: matched %d times — %r" % (name, n, old[:58]))
            continue
        files[name] = files[name].replace(old, new, 1)
    if bad:
        print("ABORTED, nothing written:")
        for b in bad:
            print("  " + b)
        return 1
    if "--dry" not in sys.argv:
        for name, t in files.items():
            io.open(os.path.join(MS, name), "w", encoding="utf-8").write(t)
    print("%d edit(s) %s" % (len(E), "checked" if "--dry" in sys.argv else "applied"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
