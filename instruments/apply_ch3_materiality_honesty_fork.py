# -*- coding: utf-8 -*-
"""Apply the approved Ch3 materiality-and-honesty fork via exact unique anchor."""
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(HERE, os.pardir, "manuscript", "ch3.md")

OLD = """Before you make it a quest, locate yourself in the situation. What is yours to name, offer, or change? Who can tell you no, redirect you, or correct the read? If you have standing to move, make the smallest action that changes what you control. If you do not have that relationship yet, do not seize the decision: make the quest to ask permission, offer one bounded contribution, prepare with the right support, or step back cleanly."""

NEW = """Before you make it a quest, locate yourself in the situation. What is yours to name, offer, or change? Who can tell you no, redirect you, or correct the read? If you have standing to move, make the smallest action that changes what you control. When your move changes other people’s conditions, name the decision that shapes those conditions and whether it is still open. If it is, say what affected people can change and give them the means to do it. If it is closed, say that plainly and do not call advice shared power. If you do not have that relationship yet, do not seize the decision: make the quest to ask permission, offer one bounded contribution, prepare with the right support, or step back cleanly."""


def main():
    text = io.open(PATH, encoding="utf-8").read()
    count = text.count(OLD)
    if count != 1:
        print("ABORTED: anchor matched %d times" % count)
        return 1
    if "When your move changes other people’s conditions" in text:
        print("ABORTED: proposed insertion already present")
        return 1
    io.open(PATH, "w", encoding="utf-8").write(text.replace(OLD, NEW, 1))
    print("applied 1 Ch3 materiality-and-honesty fork")
    return 0


if __name__ == "__main__":
    sys.exit(main())
