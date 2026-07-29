# -*- coding: utf-8 -*-
"""
W9 batch — the `**Label** — definition` family, 51 lines across ch3–ch8.

This is the one fully mechanical family in SPEC_EMDASH_AND_DENSITY. Every one of
these dashes stands between a bold term and its gloss, which is a definition
list, and a definition list takes a full stop. The house style already has the
shape elsewhere: `**Job:** To keep you alive.`

The full stop is used rather than a colon on purpose. Fifty-one new colons would
just install the colon-reveal pattern `no-ai-slop` warns about, in place of the
dash — the same trap W7 hit when the synthesis pass produced its own formula.

Run with --dry to see every conversion before anything is written.

    python3 instruments/w9_labels.py --dry
    python3 instruments/w9_labels.py
"""
import io, os, re, sys, glob

MS = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "manuscript")
PAT = re.compile(r"^(\s*)(\*\*[^*\n]{2,45}\*\*)\s+—\s+(\S)(.*)$")


def convert(line):
    m = PAT.match(line)
    if not m:
        return None
    indent, label, first, rest = m.groups()
    stem = label[:-2].rstrip()
    # Two glosses open on an italic quotation — *can I stay with this?* — where a
    # full stop would leave a lowercase word standing after it. Those take the
    # colon, which is what a colon is actually for: a label introducing a quote.
    if first == "*":
        mark, first = ":**", first
    else:
        mark, first = ".**", first.upper()
    body = label if stem.endswith((".", ":", "?", "!")) else stem + mark
    return "%s%s %s%s" % (indent, body, first, rest)


def main():
    dry = "--dry" in sys.argv
    staged, n = [], 0
    for p in sorted(glob.glob(os.path.join(MS, "ch*.md")),
                    key=lambda f: int(re.search(r"ch(\d+)", os.path.basename(f)).group(1))):
        lines = io.open(p, encoding="utf-8").read().split("\n")
        out, changed = [], 0
        for line in lines:
            new = convert(line)
            if new is None:
                out.append(line)
            else:
                if dry:
                    print("\n%s" % os.path.basename(p))
                    print("  -  %s" % line.strip()[:120])
                    print("  +  %s" % new.strip()[:120])
                out.append(new); changed += 1
        n += changed
        staged.append((p, "\n".join(out)))
    if not dry:
        for p, t in staged:
            io.open(p, "w", encoding="utf-8").write(t)
    print("\n%s %d label lines" % ("would convert" if dry else "converted", n))
    return 0


if __name__ == "__main__":
    sys.exit(main())
