# -*- coding: utf-8 -*-
"""ch2_hum_inplay.py — the hum pair, and the *In play* slots that report sensation.

Ruled by Wendell 2026-08-02: "fix ch2:89 and the In play slots."

## The hum pair — E1 and E2

`ch2:89` is the sentence this whole session started from, still standing in Section 1's
back half because the first pass covered the front half and the `we` sweep only touched
pronouns. Wendell, on the chapter's opening: *"The world is not fine. What is the IT that
is being referred to… Hums are arriving? Who sent them?"* `ch2:89` carried both — **It
shows up as** and **just hums** — plus an invented somatic event, *a tightening that
doesn't quite release*.

`ch2:318` is its deliberate callback, which is why nothing touched either one until both
could move together. The pair now turns on the mechanism instead of the sensation: hard
conversations arriving too close together for anything to stand down, and bracing that
stops having a target. That is the same claim `:318` goes on to explain, and it sets up
`:318`'s own landing line — *blanket bracing feels identical from the inside to paying
attention* — which is kept, because that sentence describes how a state is mistaken rather
than reporting the state.

## The *In play* slots — E3, E4, E5

The convention runs 14 times across the seven daemons. Nine describe an event. Five
reported a sensation, and the rule is `SKILL.md`'s, added the same day off `ch2:276`:
**sensation is unfalsifiable and unshared, which makes it an easy subject and a bad one.
Ask what is actually being described.**

Three fixed. Each keeps its observable cost, which was always the strong half, and
replaces the invented interior with the mechanism the entry exists to teach.

**Three left, and the reasons matter more than the edits:**

- `ch2:292`, the Fixer — *"you're already three solutions deep."* Three solutions is
  countable by anyone in the conversation, and the *already* is the daemon frame, licensed
  at `ch2:264`: parts that *"act on their own, before you've decided anything."*
- `ch2:297`, the Emotional Body demon — *"an unprocessed feeling spills out of you."* The
  book's own model of the failure, in the book's own vocabulary, and the next clause proves
  it happened from the outside: the person you came to support ends up taking care of you.
- `ch2:307`, the Damaged Self — *"it leaves you steadier and more able to do it again."*
  Doing it again is observable, and *steadier* is the claim the entry exists to make.

**The line is not "never mention feeling."** This book cannot teach emotional alchemy
without describing feeling. The line is between a mechanism the book asserts in its own
voice and a specific sensation reported as though the reader had confirmed it.

Anchors are exact and unique. A missed or duplicated anchor aborts with nothing written.
"""
import io, sys

P = "manuscript/ch2.md"

E = []

# E1 — ch2:89. "It shows up as" and "just hums", plus a tightening nobody reported.
E.append((
    "Something has shifted. It shows up as a tightening that doesn't quite release between "
    "hard conversations, a vigilance that no longer has a clear target and just hums.",

    "Something has shifted. Hard conversations arrive close enough together now that "
    "nothing stands down in between, and vigilance with no particular target starts "
    "passing for ordinary alertness."))

# E2 — ch2:318, the callback. Same claim, no hum.
E.append((
    "and the reason the tightening between hard conversations stops having a target and "
    "just hums.",
    "and the reason the bracing between hard conversations stops having a target at all."))

# E3 — the Protector as demon. The armored reply and its cost were always the strong half.
E.append((
    "*In play:* a hard email lands and your whole body braces as if it were a physical "
    "threat; you answer armored, and the other person meets the armor before they reach "
    "you.",

    "*In play:* a hard email lands and the Protector runs it as a physical threat. You "
    "answer armored, and the other person meets the armor before they reach you."))

# E4 — the Emotional Body as ally. Its own line above reads "the feeling runs clean and
# becomes information you can use", so the slot should show that rather than invent a sting.
E.append((
    "*In play:* something stings in a conversation; you feel it all the way through, and "
    "it tells you something true about what just happened.",

    "*In play:* someone says something and it lands hard. The charge runs its course "
    "instead of lodging, and by the end of the conversation you can name what happened and "
    "why it mattered."))

# E5 — the Victim as ally. Resonance without collapse is the capacity; "moved by it" was
# the invented part.
E.append((
    "*In play:* someone tells you something hard and you feel it with them, moved by it, "
    "without losing yourself in it or making it yours; you stay steady enough to actually "
    "help.",

    "*In play:* someone tells you something hard and it reaches you without taking you "
    "over. You can still see them, and you stay steady enough to be useful."))


def main():
    t = io.open(P, encoding="utf-8").read()
    for i, (a, _b) in enumerate(E, 1):
        n = t.count(a)
        if n != 1:
            sys.exit("E%d anchor matched %d times, expected 1: %r" % (i, n, a[:70]))
    for a, b in E:
        t = t.replace(a, b)
    io.open(P, "w", encoding="utf-8").write(t)
    print("ch2.md — %d edits applied" % len(E))
    return 0


if __name__ == "__main__":
    sys.exit(main())
