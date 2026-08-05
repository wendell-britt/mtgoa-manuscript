# -*- coding: utf-8 -*-
"""
The standing voice gate from specs/MANUSCRIPT_FILE_CANON.md, as an instrument.

Scores each surface separately, because they are different registers by
different hands and a combined number hides which one regressed. Every counter
must read 0. Exits non-zero on any hit, so it can gate a commit.

Four surfaces, because four surfaces get printed:

  body        manuscript/ch1.md-ch9.md with the marginalia frame stripped
  marginalia  the frame blocks only
  appendices  the lettered appendices A-G
  matter      front matter and back matter

The last two were added 2026-07-29. Until then the gate read only manuscript/,
so ~10,000 words of shipping prose had never been held to the standing list.
Suppress them with --no-appendices when you are measuring a chapter edit in
isolation.

The `tokens` counter earns its keep on the matter surface: the front matter
carries ⟦ISBN-PRINT⟧, ⟦IMPRINT⟧, and the author-bio blanks, and the gate is what
stands between an unfilled placeholder and the typesetter.

    python3 instruments/gate.py                  # every printed surface
    python3 instruments/gate.py -v               # quote every hit with context
    python3 instruments/gate.py --no-appendices  # chapters only, the old behavior
"""
import re, io, os, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)
MS = os.path.join(ROOT, "manuscript")
APX = os.path.join(ROOT, "appendices")

# The appendices that ship. Everything else in appendices/ is a backup, an
# architecture decision record, or a review artifact, and is not printed.
SHIPPING_APPENDICES = [
    "APPENDIX_A_FOUR_ALLYSHIP_DOMAINS.md",
    "APPENDIX_B_QUESTS_CAMPAIGNS.md",
    "APPENDIX_C_FIVE_CHANNELS.md",   # C changed hands 2026-07-30 by Wendell's
                                     # ruling; the Key Terms glossary is retired
    "APPENDIX_D_EMOTIONAL_ALCHEMY_PRACTICES.md",
    "APPENDIX_E_321_SHADOW_PROCESS.md",
    "APPENDIX_F_POLARITY_MAP.md",
    "ON_THE_SHOULDERS_OF.md",
]
BLOCK = re.compile(
    r"<!-- (MARGINALIA|EPIGRAPH-BYLINE|POSTCARD) -->\n(.*?)\n<!-- /\1 -->", re.S)

# (name, pattern, flags) — flags matter: andbut and stacks are case-sensitive,
# and treating them otherwise invents violations that are not there.
COUNTERS = [
    ("andbut", r'(^|[.?!]["“”\'’]? |\*|\*\*|— |; )(And|But) ', re.M),
    # "rooms" plural banned 2026-07-29 by Wendell. The earlier rule read
    # \broom\b, which let the plural through; ch5 carried three.
    # 2026-07-31: the comparative and superlative were invisible. `quiet(ly)?` matched
    # `quiet` and `quietly` and walked past `quieter`, which sat in ch1 and ch5. Wendell
    # on the ch5 site: "how can you claim to hear something when you don't have ears. You
    # do have eyes so harder to see makes sense." The word was wrong there as a metaphor
    # before it was wrong as a banned word.
    ("banned", r'\brooms?\b|\bquiet(ly|er|est)?\b|\bgenuinely\b', re.I),
    ("emdash", r'[a-zA-Z0-9,]—[a-zA-Z0-9]', 0),
    ("A0", r'you (were|was) (taught|told|raised|trained)|somewhere along the way'
           r'|the village taught you', re.I),
    ("stacks", r'\bNot [^.!?]{1,60}[.!?]\s+(Not|Never|No)\b', 0),
    # Unfilled HEAD_REGISTERS biography placeholders. Deliberately introduced by
    # W6 and must not survive to print — see R9. This counter is the only thing
    # standing between a token and the typesetter.
    ("tokens", r'⟦[^⟧]*⟧', 0),
]


# Sentence-level exemptions, each one ruled by Wendell on a named date. Keyed on the
# exact sentence rather than the word, so an exemption cannot silently spread: change
# the sentence and the exemption stops applying, which is the behaviour we want.
#
# The alternative was weakening a counter's pattern book-wide, which trades one
# approved site for an unbounded number of unapproved ones.
EXEMPT = [
    ("banned",
     "the Sage's question is about rooms rather than about people",
     "2026-07-30 — Laloux entry, Appendix G. Wendell: \"we can leave rooms in this "
     "example. It's not load bearing.\""),
]


def exempt_spans(text, counter):
    """Character spans in `text` that this counter must ignore."""
    spans = []
    for name, phrase, _reason in EXEMPT:
        if name != counter:
            continue
        i = text.find(phrase)
        while i >= 0:
            spans.append((i, i + len(phrase)))
            i = text.find(phrase, i + 1)
    return spans


def split_surfaces(text):
    """Return (body, marginalia) for one chapter."""
    marg = "\n".join(m.group(2) for m in BLOCK.finditer(text))
    return BLOCK.sub("", text), marg


def score(text):
    out = []
    for n, p, f in COUNTERS:
        skip = exempt_spans(text, n)
        out.append((n, [m for m in re.finditer(p, text, f)
                        if not any(a <= m.start() < b for a, b in skip)]))
    return out


def draft_surfaces(paths):
    """Score named files instead of the board.

    Added 2026-08-05. Until today `main` globbed the manuscript and silently
    discarded any path handed to it, so `gate.py somedraft.md` printed a verdict
    on the shipped book. Four domain sections were drafted against that reading
    before one of them checked. Same failure as the six board-only instruments
    `draftprobe.py` was built to wrap: an instrument that answers a question you
    did not ask is worse than one that refuses, because the answer looks fine.
    """
    surfaces = {}
    for p in paths:
        b, m = split_surfaces(io.open(p, encoding="utf-8").read())
        surfaces[os.path.basename(p)] = b
        if m.strip():
            surfaces[os.path.basename(p) + " (marginalia)"] = m
    return surfaces


def main():
    verbose = "-v" in sys.argv
    paths = [a for a in sys.argv[1:]
             if not a.startswith("-") and os.path.isfile(a)]
    if paths:
        return report(draft_surfaces(paths), verbose)

    files = sorted(glob.glob(os.path.join(MS, "ch*.md")),
                   key=lambda f: int(re.search(r"ch(\d+)", os.path.basename(f)).group(1)))
    surfaces = {"body": "", "marginalia": ""}
    for f in files:
        b, m = split_surfaces(io.open(f, encoding="utf-8").read())
        surfaces["body"] += "\n" + b
        surfaces["marginalia"] += "\n" + m

    if "--no-appendices" not in sys.argv:
        text = ""
        for name in SHIPPING_APPENDICES:
            path = os.path.join(APX, name)
            if os.path.exists(path):
                text += "\n" + io.open(path, encoding="utf-8").read()
        surfaces["appendices"] = text

        matter = ""
        for d in (os.path.join(ROOT, "front_matter"), os.path.join(ROOT, "back_matter")):
            for path in sorted(glob.glob(os.path.join(d, "*.md"))):
                matter += "\n" + io.open(path, encoding="utf-8").read()
        surfaces["matter"] = matter

    return report(surfaces, verbose)


def report(surfaces, verbose):
    width = max([12] + [len(l) for l in surfaces])
    names = [n for n, _, _ in COUNTERS]
    print("%-*s %s" % (width, "surface", " ".join("%8s" % n for n in names)))
    print("-" * (width + 50))
    total = 0
    for label, text in surfaces.items():
        s = score(text)
        total += sum(len(ms) for _, ms in s)
        print("%-*s %s" % (width, label, " ".join("%8d" % len(ms) for _, ms in s)))
    print("-" * (width + 50))

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
