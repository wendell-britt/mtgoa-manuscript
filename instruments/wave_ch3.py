# -*- coding: utf-8 -*-
"""
ch3 onto the five WAVE stages — the first chapter through the realignment.

Target, per specs/SPEC_WAVE_REALIGNMENT §10:

  1 Wake Up   Catch It Before the Story      keep, was M1
  2 Open Up   Turn the Dial Up               NEW
  3 Clean Up  Name the Channel Out Loud      keep, was M2
  4 Grow Up   Say What You Can Do Now        NEW
  5 Show Up   Say the Thing Under the Thing  keep, was M3

Retired: *Ask for What It Actually Needs* and *Spend the Read, Don't Bank It*, both
Show Up in a different domain, which is what made them duplicates. Verified first
that no marginalia anchor falls inside either block.

Both new Moves are built from ch3's own Stage 2 and Stage 4 prose — the dial
passage, the payoff paragraph, and the five integration lines. Both were run through
no-ai-slop before drafting was called done: it caught a negative listing, a colon
reveal and a fake-profound kicker, and the kicker came back as an argument rather
than being deleted, because the metaphor is the mechanism.

    python3 instruments/wave_ch3.py --dry
    python3 instruments/wave_ch3.py
"""
import io, os, re, sys

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "manuscript", "ch3.md")

NEW2 = """### Move 2 · Open Up — Turn the Dial Up

**What it is:** In the second you would normally compose yourself, turn the sensitivity up instead. Six seconds is enough.

**Why it matters:** You cannot affect what you cannot feel, and the dial in your hand only ever moved one direction. A reading taken at that setting arrives a beat after the moment it was for. Turn it up and you find what the low setting was covering. A part of you is getting something out of the very dynamic you say you want to end. The charge of being the good one. The relief when the conversation stays comfortable. That part steers better in the dark, and the low setting is the dark.

In practice: the marker is the urge to sit up straight and sound reasonable. That urge is your hand on the dial, moving it down. Leave it where it is. Count six seconds and let the situation reach you at full strength, including the part of it you would rather not have found.

**Example:** Someone takes credit for your work in a meeting. The composed version arrives instantly, fully formed: measured voice, generous face, a note to yourself to raise it later. Turn the dial up instead and two things arrive together. The anger, which you expected, and underneath it the small relief that you now hold a grievance you never had to ask for.

**The test:** You can say what you were getting out of the moment, not only what it cost you. Liking some part of it is information rather than a confession. What stays hidden runs the moment, and what you can feel, you can play.
"""

NEW4 = """### Move 4 · Grow Up — Say What You Can Do Now

**What it is:** After the read lands, name the capability it left behind. One sentence, present tense.

**Why it matters:** A read you understand and then set down leaves you where you started with better vocabulary. This stage converts information into equipment. Fear that showed you what matters becomes a value you hold rather than one you argue for. Anger that showed you a line becomes a line you are allowed to have. The feeling stops being something that happened to you and becomes something you own.

In practice: say it to your own nervous system, plainly, in the seconds after the read. *I get it. The message landed.* Then finish the sentence with the equipment. *I can tell when a plan is being agreed to and not believed.* *I can hold a hard look without going away.*

**Example:** You clock that a colleague's enthusiasm in a planning meeting is performance. Two weeks later the plan stalls exactly where you felt it would. Being right cost you nothing and bought you nothing. The Grow move is the sentence you say in the seconds after the original read: *I can feel the difference between agreement and compliance, and I get to act on it before the evidence arrives.*

**The test:** You can state the capability in the present tense with no story attached. If the sentence only makes sense once you explain the meeting, it has not landed yet.
"""

# new heading for each kept Move, keyed by its old number
RETAG = {1: "### Move 1 · Wake Up — Catch It Before the Story",
         2: "### Move 3 · Clean Up — Name the Channel Out Loud",
         3: "### Move 5 · Show Up — Say the Thing Under the Thing"}


def main():
    dry = "--dry" in sys.argv
    t = io.open(P, encoding="utf-8").read()

    blocks = {}
    for n in range(1, 6):
        m = re.search(r"^### Move %d:.*?(?=^### Move %d:|^---|\Z)" % (n, n + 1), t, re.M | re.S)
        if not m:
            print("ABORT — Move %d not found" % n); return 1
        blocks[n] = m
    span = (blocks[1].start(), blocks[5].end())

    body = {n: re.sub(r"^### Move \d:[^\n]*\n", RETAG[n] + "\n", blocks[n].group(0), count=1)
            for n in (1, 2, 3)}
    rebuilt = "".join([body[1], NEW2 + "\n", body[2], NEW4 + "\n", body[3]])

    if dry:
        print("Move block span: chars %d-%d" % span)
        for n in (1, 2, 3): print("  keep old M%d -> %s" % (n, RETAG[n]))
        print("  insert NEW Move 2 (Open Up), NEW Move 4 (Grow Up)")
        print("  retire old M4 (%d chars), old M5 (%d chars)"
              % (len(blocks[4].group(0)), len(blocks[5].group(0))))
        print("\nnet change: %+d chars" % (len(rebuilt) - (span[1] - span[0])))
        return 0

    io.open(P, "w", encoding="utf-8").write(t[:span[0]] + rebuilt + t[span[1]:])
    print("ch3 restructured onto the five stages")
    return 0


if __name__ == "__main__":
    sys.exit(main())
