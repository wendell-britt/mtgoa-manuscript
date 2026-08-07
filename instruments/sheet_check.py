# -*- coding: utf-8 -*-
"""
sheet_check.py -- keeps the character sheet's three copies saying the same thing.

Wendell 2026-08-05: *"keep the html in the repo."* The sheet now exists three times --
`instruments/character_sheet.html` (print and screen artwork), `appendices/
APPENDIX_H_CHARACTER_SHEET.md` (the page a reader holds), and the chapters that ask for
each line. **Co-locating them does not keep them honest.** DL-68's commit message claimed
keeping the HTML in the repo would stop the artwork and the appendix drifting apart, and
that was wrong on its own terms: proximity is not a check. This file is the check.

Three comparisons, and the third is the one that reaches past the pair.

  1. **Same fields, same order.** The stamped field list in the HTML and in Appendix H
     must match exactly. A field renamed in one and not the other is how a typesetter
     ends up setting a form the book describes differently.

  2. **Same stamps.** Every field carries the chapter that asks for it. If a line moves
     chapters, both copies move or the check fails.

  3. **Every stamp answers to the book.** A `CH n` stamp is a claim that chapter n asks
     the reader to add this line. Chapters 2 through 8 each say *"Add a line to the
     sheet"*; ch9 collects. If a stamp names a chapter that never asks, the sheet is
     inventing an instruction -- which is exactly what the first draft of this sheet did
     with six ability-score boxes no chapter ever asked for (DL-68).

`OPEN` is exempt from check 3 and required to stay exempt: the superpower has no chapter
by design, because `ch2:342` defines it and never says to write it down while `ch1` says
you will only spot it in motion. A stamp of `CH 2` on that line would be the defect.

    python3 instruments/sheet_check.py
    python3 instruments/sheet_check.py --quiet
"""
import io, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, os.pardir))

HTML = os.path.join(HERE, "character_sheet.html")
APPENDIX = os.path.join(ROOT, "appendices", "APPENDIX_H_CHARACTER_SHEET.md")

# What each chapter must say for a CH stamp to be honest. ch1 seats four lines in Build
# Your Allyship Character; ch2-ch8 each add one; ch9 collects the autopilot line.
#
# These are patterns, not literals, and that is the whole lesson of 2026-08-07. The first
# draft pinned the exact string "Add a line to the sheet" at seven sites. The merge with
# `claude/lakoff-integration-readability-299l3y` brought in a deliberate rename -- all
# seven now read "Add a **row** to the sheet" -- and the check reported the book broken at
# seven places when nothing was broken. A sheet is a form; a form has rows; the rename is
# better than what it replaced.
#
# This is the sixth time on this branch that a ruling frozen as a string outlived the
# wording it was copied from. The check has to test the condition -- does this chapter ask
# the reader to add to the sheet -- and not one sentence's phrasing.
ASKS = {
    "CH 1": ("manuscript/ch1.md", r"This is yours, a few lines filled in for who you are"),
    "CH 2": ("manuscript/ch2.md", r"Add a (line|row) to the sheet"),
    "CH 3": ("manuscript/ch3.md", r"Add a (line|row) to the sheet"),
    "CH 4": ("manuscript/ch4.md", r"Add a (line|row) to the sheet"),
    "CH 5": ("manuscript/ch5.md", r"Add a (line|row) to the sheet"),
    "CH 6": ("manuscript/ch6.md", r"Add a (line|row) to the sheet"),
    "CH 7": ("manuscript/ch7.md", r"Add a (line|row) to the sheet"),
    "CH 8": ("manuscript/ch8.md", r"Add a (line|row) to the sheet"),
    "CH 9": ("manuscript/ch9.md", r"left a (line|row) open on your character sheet"),
}


def from_html():
    t = io.open(HTML, encoding="utf-8").read()
    return [(re.sub(r"\s+", " ", s).strip(), re.sub(r"<[^>]+>", "", h).strip().lower())
            for s, h in re.findall(r'class="stamp[^"]*">([^<]+)</span>\s*<h2>(.*?)</h2>', t, re.S)]


def from_appendix():
    t = io.open(APPENDIX, encoding="utf-8").read()
    return [(s.strip(), h.strip().lower())
            for s, h in re.findall(r"^\*\*(CH \d+|OPEN) · ([^*]+?)\*\*", t, re.M)]


def main():
    quiet = "--quiet" in sys.argv
    html, apx = from_html(), from_appendix()
    bad = []

    if [s for s, _h in html] != [s for s, _h in apx]:
        bad.append("STAMP ORDER differs.\n    html     %s\n    appendix %s"
                   % (" ".join(s for s, _ in html), " ".join(s for s, _ in apx)))
    if len(html) != len(apx):
        bad.append("FIELD COUNT differs: html %d, appendix %d" % (len(html), len(apx)))
    else:
        for (hs, hh), (as_, ah) in zip(html, apx):
            if hh != ah:
                bad.append("FIELD differs at %s: html %r, appendix %r" % (hs, hh, ah))

    for stamp, _h in apx:
        if stamp == "OPEN":
            continue
        rel, pattern = ASKS.get(stamp, (None, None))
        if rel is None:
            bad.append("UNKNOWN STAMP %s -- no chapter recorded as asking for it" % stamp)
            continue
        text = io.open(os.path.join(ROOT, rel), encoding="utf-8").read()
        if not re.search(pattern, text):
            bad.append("STAMP %s does not answer to the book: %s matches nothing for %s"
                       % (stamp, rel, pattern))

    if not quiet or bad:
        print("character sheet -- %d fields, html and appendix" % len(apx))
        print("\n".join("  " + b for b in bad) if bad else "  in agreement, every stamp answers to its chapter")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
