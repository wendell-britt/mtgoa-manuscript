# -*- coding: utf-8 -*-
"""Apply the approved Ch3 relational-placement gate via exact unique anchor."""
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(HERE, os.pardir, "manuscript", "ch3.md")

OLD = """A quest is a commitment to act that touches somebody other than you, on a date. It is not a resolution and it is not a value. It has a verb, a name in it, and a deadline. Quests come from the Show Up cards, and every one of them ends in an artifact, and an artifact is something another person can encounter.

Write yours in one sentence: what you will do, who it reaches, by when, and what it costs you."""

NEW = """A quest is a commitment to act that touches somebody other than you, on a date. It is not a resolution and it is not a value. It has a verb, a name in it, and a deadline. Quests come from the Show Up cards, and every one of them ends in an artifact, and an artifact is something another person can encounter.

Before you make it a quest, locate yourself in the situation. What is yours to name, offer, or change? Who can tell you no, redirect you, or correct the read? If you have standing to move, make the smallest action that changes what you control. If you do not have that relationship yet, do not seize the decision: make the quest to ask permission, offer one bounded contribution, prepare with the right support, or step back cleanly.

Write yours in one sentence: what you will do, who it reaches, by when, and what it costs you."""


def main():
    text = io.open(PATH, encoding="utf-8").read()
    count = text.count(OLD)
    if count != 1:
        print("ABORTED: anchor matched %d times" % count)
        return 1
    if "Before you make it a quest, locate yourself in the situation." in text:
        print("ABORTED: proposed insertion already present")
        return 1
    io.open(PATH, "w", encoding="utf-8").write(text.replace(OLD, NEW, 1))
    print("applied 1 Ch3 relational-placement gate")
    return 0


if __name__ == "__main__":
    sys.exit(main())
