# -*- coding: utf-8 -*-
"""tier1_empty.py — the tier-1 sweep, which turned out to be six sites, not 136.

Ruled by Wendell 2026-08-03: *"do the tier-1 empty_head sweep."*

## The count was wrong, and the instrument is what was wrong

`empty_head.py` reported 136 HARD sites after the `thing` sweep. Broken down by head noun:

    part 88 · parts 10 · thing 11 · piece 7 · matter 6 · things 1 · bit 1 · pieces 1

**98 of 125 are `part`, and in this book `part` is canon.** The daemon system *is* parts
work — *"Those parts are daemons"* (ch2), *"a part of you has already felt"* (ch3), *"the
part that audits your charge"* (ch4), *"The Part That Turned a Difference Into a Defect"*
(ch8, a section heading). ch5 and ch6 add a second contentful sense — a part of a structure
or an inheritance: *"This part is load-bearing"*, *"whether the parts add up to a whole"*.

`piece` and `matter` are the same story. Every one sits in a fixed compound where the head
is doing real work: *a piece of evidence*, *a piece of feedback*, *a piece of institutional
memory*, *moving a piece on the board*, *allyship is a matter of following the right people*,
*any say in the matter*, *picked up the pieces*.

**So tier 1 was over-broad, and `HARD` is corrected in this commit rather than swept.** A
head noun is only empty when it is empty *in this book*. `thing` was empty everywhere.
`part` is a term of art here, which is exactly the `field` and `charge` situation from the
other direction.

## What the split actually found, which is better

Filtering the daemon and structural senses left one repeated construction, and it is not an
empty-head problem at all:

> `Here is the part…`

`.claude/skills/no-ai-slop/SKILL.md` lists this verbatim under **faux-insight setups** —
*"This is the part most people skip," "Here's what nobody tells you," "The part everyone
misses."* The note on it: *"These flatter the writer as the lone expert. Cut the setup and
make the claim stand on its own."*

`ch6:197` runs the banned phrase almost word for word: *"here comes the part most people
skip."*

## The six, and the two that are left alone

**Cut, claim stands alone:**

- `ch1:95` — *"Here is the part the game would rather you not notice: you can look straight
  at it"* — flatters, and personifies the game as withholding. The claim after the colon is
  the strongest sentence in the paragraph and it does not need an introduction.
- `ch4:504` — *"Here is the part almost nobody gets told about that voice: it is not lying
  to you"* — the purest instance of the pattern in the book.

**Named, not cut:**

- `ch6:197` — the parenthetical is making a real claim about the method, that practitioners
  omit this step, so it keeps its meaning and loses the placeholder: `part` → `step`.
- `ch3:239`, `ch4:203` — *"Here is the part specific to this reader"* is a structural
  signpost used in two chapters, not flattery. It keeps the device and names the noun.

**Left alone, and deliberately:** `ch1:243` *"Here is the part I did not plan"* and `ch2:197`
*"The part I did not say out loud."* Both are Wendell in first person about his own story.
The faux-insight rule targets claims about what other people miss; a man saying which part
of his own story he withheld is not that.

Anchors are exact and unique. A missed or duplicated anchor aborts with nothing written.
"""
import io, sys

EDITS = [
    ("manuscript/ch1.md", [
        ("rigged before you sat down. Here is the part the game would rather you not "
         "notice: you can look straight at it,",
         "rigged before you sat down. You can look straight at it,"),
    ]),
    ("manuscript/ch3.md", [
        ("Here is the part specific to this reader, and its shape is",
         "Here is what is specific to this reader, and its shape is"),
    ]),
    ("manuscript/ch4.md", [
        ("Here is the part specific to this reader. The suspicion runs one direction.",
         "Here is what is specific to this reader. The suspicion runs one direction."),
        ("Here is the part almost nobody gets told about that voice: it is not lying to "
         "you.",
         "That voice is not lying to you."),
    ]),
    ("manuscript/ch6.md", [
        ("(here comes the part most people skip)",
         "(here comes the step most people skip)"),
    ]),
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
