# -*- coding: utf-8 -*-
"""
Appendix B — The Ask, a solo quest for getting the partner the campaigns require.

Ruled by Wendell 2026-08-01: *"there should be a small raise awareness quest that is
about finding an accountability partner."*

**The gap it closes.** Appendix B's loop ends Quest 8 with *"Which daemon grew? Which
domain is calling next? That answer is your next quest."* Measured, that loop cannot
close: the eight quests cover three of four domains (Direct Action has none) and five of
eight figures. The complete map is the **campaigns**, which are a clean 2-2-2-2 across
every domain and every daemon and match Appendix A's affinity table exactly. But every
campaign requires another person, and `SPEC_WORKBOOK_SCOPE.md:53` requires that *"a
reader without a coach can complete every exercise alone."* So the one route that closes
the loop is the one route ICA forbids her to take by herself.

Wendell's fix is better than the one I proposed. I recommended writing a solo Direct
Action quest, which patches one domain. A partner quest unblocks **all four campaigns**,
because the missing precondition was never the domain -- it was the person.

**Why Raise Awareness is the right domain**, and not a convenience. Asking someone to
witness your practice is making the practice visible, which is what the domain is. The
domain's daemons in Appendix A are Skeptic and Victim, and those are exactly the two
voices that stop the ask: the Skeptic supplies *why would they say yes*, the Victim
supplies *I do not have anybody*. **Victim** is assigned here because it is the shadow
that actually runs this move, and because it was one of three daemons carrying no quest
at all.

**Placement.** Not Quest 9. The frame promises *"Eight quests, one for each chapter of
the walk"* and a ninth would break the count and have no chapter. It sits at the head of
The Four Campaigns, which is where the blocker is and where she reads it at the moment
she needs it.

Measured: be 0.73 · copula 0.86 · waste 0.75 · zombie 0.00 · expletive 0.00 · passive
0.00 · empty 1.13.

**Two things this does NOT fix, held for a ruling.** Direct Action still carries no solo
quest, and Fixer/Healer and Damaged Self still carry none. And Quest 8's sentence still
routes to *your next quest* where the answer it computes is a campaign.
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)
PATH = "appendices/APPENDIX_B_QUESTS_CAMPAIGNS.md"

ANCHOR = (
    "A quest is solo. A campaign is the same kind of practice, run longer and out loud "
    "— 21 days, built to share with a partner, a team, or a community. Allyship is "
    "relational; the campaigns make it so. Each names what it builds, the milestone "
    "captures along the way, and how to run it with other people."
)

ASK = """

Every campaign needs one other person, and the book has been solo until now. So the first rep is finding them, and it is a quest in its own right.

---

### Before Any Campaign — The Ask
*Daemon: Victim · Domain: Raise Awareness · One conversation*

***The shadow running:*** You already know who you would ask, and you have the reason ready for why they would say no. The Victim carries that reason, and it always arrives sounding like realism.

***The gift:*** You ask, and find out instead of deciding. Asking is the first public rep of this practice, which makes it Raise Awareness before it is anything else.

1. Name one person who has watched you try at something and not laughed. Not necessarily your closest friend. The one who would take it seriously.
2. Tell them what you are practicing and what you want from them: hear one capture a week for three weeks, and ask you one question about it. Give them the end date when you ask, so they are agreeing to something finite.
3. Capture what you predicted they would say, next to what they said."""


def main():
    p = os.path.join(ROOT, PATH)
    t = io.open(p, encoding="utf-8").read()
    n = t.count(ANCHOR)
    if n != 1:
        print("ABORTED, nothing written:")
        print("  %s: matched %d times" % (PATH, n))
        return 1
    t = t.replace(ANCHOR, ANCHOR + ASK, 1)
    if "--dry" not in sys.argv:
        io.open(p, "w", encoding="utf-8").write(t)
    print("1 edit %s" % ("checked" if "--dry" in sys.argv else "applied"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
