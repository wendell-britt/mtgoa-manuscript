# -*- coding: utf-8 -*-
"""
Appendix B — two solo Direct Action quests. Ruled by Wendell 2026-08-01.

**What it closes.** Before this, the eight chapter quests reached three of four domains
and five of eight figures. Direct Action had no solo quest at all, and Fixer/Healer and
Damaged Self had none either -- which is to say the domain nearest to what most readers
picked the book up to do was reachable only through a 21-day campaign requiring another
person, against ICA. With these two plus *The Ask*, every domain and every figure carries
a solo quest.

**The consequence is that Quest 8's loop now works.** *"Which daemon grew? Which domain is
calling next? That answer is your next quest."* Both questions previously resolved to
quests that did not exist for a third of the possible answers. Coverage was the bug; the
sentence was right all along and needed no edit.

**Indexing.** These two are not chapter quests and are not numbered into the eight. The
eight follow the walk; these follow the domain, so they sit between the eight and the
campaigns and can be run from anywhere in the book. Same precedent as *The Ask*.

**B, the Fixer/Healer.** Scope discipline. It mirrors the Direct Action campaign's Week 1
-- *"if you can't name the object, you don't have permission"* -- and its third task
routes a failed fix to the condition underneath, which is ch6's whole teaching about an
intervention queue that never empties. Measured: be 0.57, copula 0.38, waste 0.68, zombie
1.27, expletive 0.00, passive 0.00, empty 0.00.

**C, the Damaged Self.** Wendell's brief was *"what kind of damage are you good at taking
and how can you use that to take it for someone else."* The answer was already written at
`ch2:344`, in the daemon's own ally line: *"it turns what it survives into strength,
sorting the damage that builds you from the damage that only breaks you."* Its demon line
supplies the shadow: *"it absorbs every hit going, without a word, until it's soaking up
harm that was never yours to carry."* This quest spends standing rather than examining it,
which makes it the most directly allyship-shaped rep in the appendix. Measured: be 0.36,
copula 0.00, waste 1.13, zombie 0.61, expletive 0.00, passive 0.00, empty 0.65. A first
draft ran passive 2.91 on *"what your standing is made of"*.
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)
PATH = "appendices/APPENDIX_B_QUESTS_CAMPAIGNS.md"

FRAME_OLD = ("These are the reps. Eight **quests**, one for each chapter of the walk, "
             "that you run alone.")
FRAME_NEW = ("These are the reps. Eight **quests**, one for each chapter of the walk, "
             "and three more indexed on a domain rather than a chapter. All of them you "
             "run alone.")

ANCHOR = "## The Four Campaigns"

BLOCK = """## Two More, for Direct Action

The eight above follow the chapters, and between them they reach three of the four domains. Direct Action is the fourth, and it is the one most people came here for. These two are indexed on the domain instead, so you can run either from wherever you are in the book.

---

### Direct Action Quest — The One That's Yours
*Daemon: Fixer/Healer · Domain: Direct Action · 7 days*

***The shadow running:*** You lunge at the nearest breakage because lunging feels like helping, and the reach makes the repair yours forever.

***The gift:*** The surgical move inside your actual scope. One cut, in the place where you have standing to cut.

1. Name three problems in a situation you are close to. Cross out the two that are not yours to touch.
2. Make one clean intervention on the one left. Small enough to finish inside the week.
3. Capture whether it still needs you a week later. If it does, you treated a symptom, and the condition underneath it is your next quest.

---

### Direct Action Quest — Going First
*Daemon: Damaged Self · Domain: Direct Action · 7 days*

***The shadow running:*** You wait for somebody with less protection than you to say the costly true one, and you call the waiting politeness.

***The gift:*** You take the first hit on purpose, in the one place where your standing is worth more to somebody else than your comfort is to you.

1. Name one group where you have standing that somebody else there does not. Say where that standing comes from.
2. This week, say the costly true one first, before the person with less cover has to.
3. Capture what it cost you and what it saved them. If it cost you nothing, you did not go first.

---

"""


def main():
    p = os.path.join(ROOT, PATH)
    t = io.open(p, encoding="utf-8").read()
    bad = []
    for s in (FRAME_OLD, ANCHOR):
        if t.count(s) != 1:
            bad.append("%r matched %d times" % (s[:50], t.count(s)))
    if bad:
        print("ABORTED, nothing written:")
        for b in bad:
            print("  " + b)
        return 1
    t = t.replace(FRAME_OLD, FRAME_NEW, 1).replace(ANCHOR, BLOCK + ANCHOR, 1)
    if "--dry" not in sys.argv:
        io.open(p, "w", encoding="utf-8").write(t)
    print("2 quest(s) + 1 frame edit %s"
          % ("checked" if "--dry" in sys.argv else "applied"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
