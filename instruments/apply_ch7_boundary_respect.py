# -*- coding: utf-8 -*-
"""Apply the approved Ch7 boundary-respect clarification via exact unique anchor."""
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(HERE, os.pardir, "manuscript", "ch7.md")
OLD = """**4. Stay.** After you offer the repair, the instinct is to leave: to give them space, to give the moment space. Don't. Stay present through the discomfort of having said it. The staying is the actual repair work.

**Why it matters:** Ruptures named and repaired build more trust than ruptures that never happened. The repair does not undo the break. It proves that the relationship can survive the break, the only proof that builds confidence in a relationship."""
NEW = """**4. Stay.** After you offer the repair, the instinct is to leave: to give them space, to give the moment space. Don't. Stay present through the discomfort of having said it. The staying is the actual repair work.

Staying does not mean insisting on access after someone has set a boundary. Respect the boundary. Keep changing your part, remain reachable on terms they choose, and let the relationship be as close or as distant as they decide.

**Why it matters:** Ruptures named and repaired build more trust than ruptures that never happened. The repair does not undo the break. It proves that the relationship can survive the break, the only proof that builds confidence in a relationship."""

def main():
    text = io.open(PATH, encoding="utf-8").read()
    count = text.count(OLD)
    if count != 1:
        print("ABORTED: anchor matched %d times" % count)
        return 1
    if "Staying does not mean insisting on access" in text:
        print("ABORTED: proposed insertion already present")
        return 1
    io.open(PATH, "w", encoding="utf-8").write(text.replace(OLD, NEW, 1))
    print("applied 1 Ch7 boundary-respect clarification")
    return 0

if __name__ == "__main__":
    sys.exit(main())
