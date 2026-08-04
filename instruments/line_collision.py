# -*- coding: utf-8 -*-
"""line_collision.py — the worksheet sense of `line` gives the word back to ch4.

Ruled by Wendell 2026-08-03, on the collision audit: *"do the line fix, one sentence and add
a row."*

`line` means the Challenger's boundary at roughly 154 sites, 102 of them in ch4. It also
means a line of text, and that second sense lives in the two most repeated instructions in
the book — the quest formula in six chapters and the between-chapters worksheet line in
seven.

`ch4:795` is why this is a defect rather than a coincidence. Both senses, twelve words
apart, in the chapter that spends 102 instances teaching the second one:

> **Add a line to the sheet.** Under the channel you skip, **write the line you have not
> drawn**: what you owe a specific person and have been softening since before you picked
> up this book.

## Today's `thing` sweep made it worse, which is how it surfaced

`One line, four things:` was standardised to `One line:` across five chapters this morning,
on the correct reasoning that the colon already names the four elements. That fix was right
on its own terms **and it deleted the one word that was signalling *a row of text* rather
than *a boundary*.** The formula came out maximally ambiguous in exactly the chapter where
it matters. A repair that is locally correct and globally wrong is worth a name; this is the
third one today, after `the beautiful warmth` and the ch5 handoff.

## Why these two words

**`One sentence:`** is more accurate, not merely unambiguous. `ch9:508` already defines the
artifact as *"said in a sentence a stranger could repeat,"* and `ch4:712` already writes
*"One sentence of line and one of offer."* The formula was asking for a sentence and calling
it a line.

**`Add a row to the sheet`** is what the instruction physically means. The sheet is a table
built up across the book — myth, daemon, channel, line, inheritance, harm, walk-away price,
game — one entry per chapter.

## Not touched

`ch2:328` — *"it lets you name one line, 'I'm open to challenge; I'm not available for
personal attacks'"* — and `ch7:77` — *"where one person declines to take back one line"* —
are both the boundary sense and correct.

13 sites. Anchors are exact and unique; a missed or duplicated anchor aborts with nothing
written.
"""
import io, sys

SHEET = ("Add a line to the sheet", "Add a row to the sheet")
QUEST = ("One line: what you will do", "One sentence: what you will do")

EDITS = [
    ("manuscript/ch2.md", [SHEET]),
    ("manuscript/ch3.md", [("Write yours in one line: what you will do",
                            "Write yours in one sentence: what you will do"), SHEET]),
    ("manuscript/ch4.md", [QUEST, SHEET]),
    ("manuscript/ch5.md", [QUEST, SHEET]),
    ("manuscript/ch6.md", [QUEST, SHEET]),
    ("manuscript/ch7.md", [QUEST, SHEET]),
    ("manuscript/ch8.md", [QUEST, SHEET]),
]


def main():
    for path, edits in EDITS:
        t = io.open(path, encoding="utf-8").read()
        for i, (a, _b) in enumerate(edits, 1):
            n = t.count(a)
            if n != 1:
                sys.exit("%s E%d anchor matched %d times, expected 1: %r"
                         % (path, i, n, a[:60]))
    n = 0
    for path, edits in EDITS:
        t = io.open(path, encoding="utf-8").read()
        for a, b in edits:
            t = t.replace(a, b)
        io.open(path, "w", encoding="utf-8").write(t)
        n += len(edits)
    print("%d edits applied across %d files" % (n, len(EDITS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
