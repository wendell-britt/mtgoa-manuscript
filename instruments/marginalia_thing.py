# -*- coding: utf-8 -*-
"""marginalia_thing.py — `thing` out of the marginalia. 26 of 27 sites.

Ruled by Wendell 2026-08-03: *"sweep the marginalia and promote thing to the gate."*

## Where the edits go, and why not into the chapters

The marginalia are **not stored in `manuscript/`**. `marginalia/insertions.py` holds
`(anchor, note)` pairs and `marginalia/compile.py` writes them into the chapter files
inside `<!-- MARGINALIA -->` comments. Editing the rendered `>` lines in a chapter would be
overwritten by the next `--apply` and would break `--verify`, which proves apply+strip
returns byte-identical body text.

So this script edits `insertions.py`, and the caller recompiles.

## The register argument, which cuts toward sweeping rather than away

The marginalia are in-world documents — admissions filings for the School of the Body and
the School of the Line, clause-numbered prospectuses, signed notes from named students and
Heads. **These are the most formal registers in the book**, and a formal register is where
a placeholder reads worst. An admissions filing that says *"I look for two things"* is
weaker than one that says *"I look for two qualities."*

## The answer was in the next clause four times, again

The pattern that has run all day held here too:

- `"If it needs the shape of the thing changed … that is the School of the **Pattern**"` →
  **the pattern changed**. The word was the next four syllables.
- `"a thing that is right every time"`, preceded by *"It has been a good **call** every time
  since"* → **a call that is right every time**.
- `"other people failing to tell me things"`, followed by *"Every set of **terms** I have not
  stated"* → **failing to tell me their terms**.
- `"four separate things on this ship still function"` … *"the four things kept working"* →
  **four separate systems**, both.

## One left, and one trap

Site 15 is a Python comment about `MARGIN_ARC`, not book content. `gate.py` does not scan
`.py` files and a code comment is not prose.

**The trap:** `insertions.py` is hand-wrapped at about ninety columns, so half the anchors
straddle a line break in the source even though they read as one sentence. The first run
aborted on E1 for exactly that reason. Every anchor here is either inside a single source
line or carries its newline explicitly.

Anchors are exact and unique. A missed or duplicated anchor aborts with nothing written.
"""
import io, sys

P = "marginalia/insertions.py"

E = [
    ("the first useful thing I said",
     "the first useful sentence I said"),

    ("it is the hardest thing I have watched anyone on this staff do.",
     "I have not watched anyone on this staff do anything harder."),

    ("will feel like a thing accomplished. It is not one.",
     "will feel like an accomplishment. It is not one."),

    ("you can do one thing, so make it the same thing every time:",
     "you can say one sentence, so make it the same one every time:"),

    # "It has been a good call every time since" is the clause before it.
    ("thing that is right every time is not being tested",
     "call that is right every time is not being tested"),

    ("She will hold a thing",
     "She will hold a practice"),

    ("It is the best-attended thing we do.",
     "It is the best-attended ceremony we have."),

    ("She is the reason four separate things on",
     "She is the reason four separate systems on"),

    ("because the four things kept working",
     "because the four systems kept working"),

    # The next sentence is about terms.
    ("failing to tell me things.",
     "failing to tell me their terms."),

    ("walk-away terms are the hardest thing they teach because they are the thing they "
     "are worst at,",
     "walk-away terms are the hardest lesson they teach because they are the one they "
     "are worst at,"),

    ("*A partial list of things this school runs on that exist nowhere in writing:",
     "*A partial list of what this school runs on that exists nowhere in writing:"),

    ("That is the one thing I have that none of them can teach you",
     "That is the one lesson I have that none of them can teach you"),

    ("I look for two things and will not take one without the other.",
     "I look for two qualities and will not take one without the other."),

    ("I teach one thing. A student learns to",
     "I teach one skill. A student learns to"),

    ("begin saying things earlier",
     "begin speaking earlier"),

    # The one anchor that has to carry its own line break.
    ("Two things can be\ndone and neither of them is mine.",
     "Two responses are possible and\nneither of them is mine."),

    # "that is the School of the Pattern" is the next clause.
    ("If it needs the shape of the thing changed so the feeling stops",
     "If it needs the pattern changed so the feeling stops"),

    ("and the thing went ahead;",
     "and it went ahead anyway;"),

    ("The specific thing stops. Then the second thing,",
     "The specific behaviour stops. Then the second effect,"),

    ("has kept a thing",
     "has kept a practice"),

    ("able to refuse a thing before one can be trusted to keep it.",
     "able to refuse before one can be trusted to keep."),

    ("stop apologising for things that were never theirs,",
     "stop apologising for what was never theirs,"),
]


def main():
    t = io.open(P, encoding="utf-8").read()
    for i, (a, _b) in enumerate(E, 1):
        n = t.count(a)
        if n != 1:
            sys.exit("E%d anchor matched %d times, expected 1: %r" % (i, n, a[:70]))
    for a, b in E:
        t = t.replace(a, b)
    io.open(P, "w", encoding="utf-8").write(t)
    print("insertions.py — %d edits applied" % len(E))
    print("now: compile.py --strip && compile.py --apply && compile.py --verify")
    return 0


if __name__ == "__main__":
    sys.exit(main())
