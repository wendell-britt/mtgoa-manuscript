# -*- coding: utf-8 -*-
"""
The standing voice gate from specs/MANUSCRIPT_FILE_CANON.md, as an instrument.

Scores body text and marginalia separately, because they are different registers
by different hands and a combined number hides which one regressed. Every counter
must read 0. Exits non-zero on any hit, so it can gate a commit.

    python3 instruments/gate.py            # both surfaces, summary
    python3 instruments/gate.py -v         # quote every hit with context
"""
import re, io, os, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")
BLOCK = re.compile(
    r"<!-- (MARGINALIA|EPIGRAPH-BYLINE|POSTCARD) -->\n(.*?)\n<!-- /\1 -->", re.S)

# (name, pattern, flags) — flags matter: andbut and stacks are case-sensitive,
# and treating them otherwise invents violations that are not there.
COUNTERS = [
    ("andbut", r'(^|[.?!]["“”\'’]? |\*|\*\*|— |; )(And|But) ', re.M),
    ("banned", r'\broom\b|\bquiet(ly)?\b|\bgenuinely\b', re.I),
    ("emdash", r'[a-zA-Z0-9,]—[a-zA-Z0-9]', 0),
    ("A0", r'you (were|was) (taught|told|raised|trained)|somewhere along the way'
           r'|the village taught you', re.I),
    ("stacks", r'\bNot [^.!?]{1,60}[.!?]\s+(Not|Never|No)\b', 0),
    # Unfilled HEAD_REGISTERS biography placeholders. Deliberately introduced by
    # W6 and must not survive to print — see R9. This counter is the only thing
    # standing between a token and the typesetter.
    ("tokens", r'⟦[^⟧]*⟧', 0),
]


def split_surfaces(text):
    """Return (body, marginalia) for one chapter."""
    marg = "\n".join(m.group(2) for m in BLOCK.finditer(text))
    return BLOCK.sub("", text), marg


def score(text):
    return [(n, [m for m in re.finditer(p, text, f)]) for n, p, f in COUNTERS]


def main():
    verbose = "-v" in sys.argv
    files = sorted(glob.glob(os.path.join(MS, "ch*.md")),
                   key=lambda f: int(re.search(r"ch(\d+)", os.path.basename(f)).group(1)))
    surfaces = {"body": "", "marginalia": ""}
    for f in files:
        b, m = split_surfaces(io.open(f, encoding="utf-8").read())
        surfaces["body"] += "\n" + b
        surfaces["marginalia"] += "\n" + m

    names = [n for n, _, _ in COUNTERS]
    print("%-12s %s" % ("surface", " ".join("%8s" % n for n in names)))
    print("-" * 62)
    total = 0
    for label, text in surfaces.items():
        s = score(text)
        total += sum(len(ms) for _, ms in s)
        print("%-12s %s" % (label, " ".join("%8d" % len(ms) for _, ms in s)))
    print("-" * 62)

    if verbose:
        for label, text in surfaces.items():
            for name, ms in score(text):
                for m in ms:
                    ctx = text[max(0, m.start() - 70):m.end() + 70].replace("\n", " ")
                    print("\n%s [%s] %r\n    …%s…" % (label, name, m.group(0).strip(), ctx.strip()))
        print()

    print("GATE PASS — every counter reads 0" if total == 0
          else "GATE FAIL — %d hit(s). Re-run with -v to see them." % total)
    return 0 if total == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
