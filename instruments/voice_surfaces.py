# -*- coding: utf-8 -*-
"""
voice_surfaces.py -- run the voice linter over the shipping surfaces it never reached.

`marginalia/review.py` owns voice: denying negations, vague nouns, the AI shapes, hedges.
Its `path` argument is `nargs="?"` and defaults to `manuscript/`, and `review.py`'s
book-wide pass called it **with no arguments**. So from the day that step was added it
read the nine chapters and nothing else.

`gate.py` covers four surfaces -- body, marginalia, appendices, matter. The voice step
covered one. Measured 2026-08-05, the gap was not empty:

    Appendix C   1 BLOCK
    Appendix E   2 BLOCK
    Appendix G   1 BLOCK   "the problem isn't the practitioner. It's the design of
                            the game" -- a denying negation, and the book's central
                            empirical claim, so it is a ruling rather than a fix

The glossary, the index and Appendix H had never been read by it at all.

Denying negations and vague nouns are exactly what a reference page accumulates, because
nobody reads an appendix aloud. This walks the shipping surfaces one at a time, because
the linter takes a single path, and reports the total.

Retired and backup files under `appendices/` are excluded -- `APPENDIX_C_KEY_TERMS.md`
is off the spine (DL-8) and auditing it reports defects in a page no reader will see.

    python3 instruments/voice_surfaces.py
    python3 instruments/voice_surfaces.py --quiet
"""
import glob, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, os.pardir))
LINTER = os.path.join(ROOT, "marginalia", "review.py")


def surfaces():
    """The shipping non-chapter surfaces, taken from the spine so the two cannot drift."""
    sys.path.insert(0, HERE)
    from build_book import SPINE
    out = []
    for _kind, _label, rel, _lvl in SPINE:
        if not rel or rel.startswith("manuscript/"):
            continue
        p = os.path.join(ROOT, rel)
        if os.path.exists(p):
            out.append(rel)
    return out


def main():
    quiet = "--quiet" in sys.argv
    rows, block, warn = [], 0, 0
    for rel in surfaces():
        out = subprocess.run([sys.executable, LINTER, os.path.join(ROOT, rel)],
                             capture_output=True, text=True).stdout
        # The linter prints "clean -- no findings" instead of a summary line when a file
        # has none, so a missing BLOCK/WARN line means clean, NOT unreadable. The first
        # draft of this file labelled six clean surfaces "unreadable", which is the same
        # mislabelling `glossary_check.py` shipped this morning: a report that hides the
        # answer is worse than a long one.
        m = re.search(r"BLOCK (\d+)\s+WARN (\d+)", out)
        if not m:
            rows.append((rel, (0, 0) if "clean" in out else None, None))
            if "clean" in out:
                rows[-1] = (rel, 0, 0)
            continue
        b, w = int(m.group(1)), int(m.group(2))
        block += b
        warn += w
        rows.append((rel, b, w))

    if quiet and not block:
        # Say the number even when it is zero. A check that prints nothing on success
        # tells a reader it did not run.
        print("voice surfaces clean -- %d file(s), 0 BLOCK, %d WARN" % (len(rows), warn))
    if not quiet or block:
        print("voice, shipping surfaces outside manuscript/ -- %d file(s)" % len(rows))
        for rel, b, w in rows:
            if b is None:
                print("  %-46s NO SUMMARY -- read it by hand" % rel)
            elif b or w:
                print("  %-46s BLOCK %d  WARN %d" % (rel, b, w))
        print("TOTAL BLOCK %d  WARN %d" % (block, warn))
    return 1 if block else 0


if __name__ == "__main__":
    sys.exit(main())
