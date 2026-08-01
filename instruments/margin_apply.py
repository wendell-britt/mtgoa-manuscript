# -*- coding: utf-8 -*-
"""
margin_apply.py — the approved marginalia line edits, applied to both copies.

Wendell 2026-08-01, on `editorial_reports/2026-08-01/PASS3_MARGIN_LINE_EDITOR.md`:
"apply them both places." MG-1 through MG-5.

**Both places is the whole point of this file.** The margin exists twice — the source in
`marginalia/insertions.py`, the compiled result in `manuscript/ch2.md`–`ch9.md` — and an
edit to one copy is silently lost (DL-26). Edit only the manuscript and the next
`compile.py --strip`/`--apply` cycle reverts it. Edit only the source and it never
reaches the book. So every anchor here is required to be present **exactly once in
`insertions.py` and exactly once across the nine chapter files**, and a miss on either
side aborts the run with nothing written.

Anchors are deliberately mid-line substrings. The compiled copy prefixes every margin
line with `> `, so an anchor that starts at a line boundary matches in one file and not
the other; an anchor that crosses a line break has to be split into two, which is why
MG-3 is two entries.

    python3 instruments/margin_apply.py --check    # verify both copies, write nothing
    python3 instruments/margin_apply.py            # apply

Run `marginalia/compile.py --check` and `instruments/gate.py` after.
"""
import io, os, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)
SOURCE = os.path.join(ROOT, "marginalia", "insertions.py")
CHAPTERS = sorted(glob.glob(os.path.join(ROOT, "manuscript", "ch[1-9].md")))

# (flag, anchor, replacement)
EDITS = [
    # MG-1 · the only exclamation mark in 66 blocks, on the formula five other
    # handbooks close with a period.
    ("MG-1", "have suffered as a result!",
             "have suffered as a result."),

    # MG-2 · "used to" does not survive the auxiliary.
    ("MG-2", "but they ask, which they did not used to,",
             "but they ask, which they did not do before,"),

    # MG-3 · three "found"s in 24 words, across a line break, so two entries.
    ("MG-3a", "found the omission — and then found",
              "found the omission — and then learned"),
    ("MG-3b", "that Sera had found it in the spring",
              "that Sera had seen it in the spring"),

    # MG-4 · a decade and a fourth year for the same span, 40 words apart.
    ("MG-4", "somebody who spent a decade marking her own homework.",
             "somebody who spent years marking her own homework."),

    # MG-5 · the eleven motif stays; the third tenure goes. Bram's is the one to move,
    # because Elian's eleven years is tied to a curriculum and Bram's to a person.
    ("MG-5", "I have known this for eleven years.",
             "I have known this since he came aboard."),
]


def main():
    check = "--check" in sys.argv
    src = io.open(SOURCE, encoding="utf-8").read()
    ms = {p: io.open(p, encoding="utf-8").read() for p in CHAPTERS}

    problems, where = [], {}
    for flag, anchor, _ in EDITS:
        n_src = src.count(anchor)
        hits = [(p, t.count(anchor)) for p, t in ms.items() if anchor in t]
        n_ms = sum(c for _, c in hits)
        if n_src != 1:
            problems.append("%s: %d hits in insertions.py" % (flag, n_src))
        if n_ms != 1:
            problems.append("%s: %d hits across manuscript/" % (flag, n_ms))
        if hits:
            where[flag] = os.path.basename(hits[0][0])
    if problems:
        print("ABORT — nothing written")
        for p in problems:
            print("  " + p)
        return 1

    for flag, anchor, new in EDITS:
        src = src.replace(anchor, new, 1)
        for p in ms:
            if anchor in ms[p]:
                ms[p] = ms[p].replace(anchor, new, 1)
                break

    for flag, anchor, new in EDITS:
        print("%-6s %-9s %s" % (flag, where[flag], anchor[:64]))
        print("%-6s %-9s -> %s" % ("", "", new[:64]))
    if check:
        print("\n--check: %d edits verified present in both copies, nothing written"
              % len(EDITS))
        return 0
    io.open(SOURCE, "w", encoding="utf-8").write(src)
    for p, t in ms.items():
        io.open(p, "w", encoding="utf-8").write(t)
    print("\n%d edits applied to insertions.py and to manuscript/" % len(EDITS))
    return 0


if __name__ == "__main__":
    sys.exit(main())
