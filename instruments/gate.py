# -*- coding: utf-8 -*-
"""
The standing voice gate from specs/MANUSCRIPT_FILE_CANON.md, as an instrument.

Scores each surface separately, because they are different registers by
different hands and a combined number hides which one regressed. Every counter
must read 0. Exits non-zero on any hit, so it can gate a commit.

Three surfaces, because three surfaces get printed:

  body        manuscript/ch1.md-ch9.md with the marginalia frame stripped
  marginalia  the frame blocks only
  appendices  appendices/APPENDIX_*.md and the back matter

The appendices surface was added 2026-07-29. Until then the gate read only
manuscript/, so ~9,000 words of shipping prose had never been held to the
standing list. Suppress it with --no-appendices when you are measuring a
chapter edit in isolation.

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
    "APPENDIX_C_FIVE_CHANNELS.md",          # C changed hands 2026-07-29; the
    "APPENDIX_D_EMOTIONAL_ALCHEMY_PRACTICES.md",  # Key Terms glossary is retired
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

    if "--no-appendices" not in sys.argv:
        text = ""
        for name in SHIPPING_APPENDICES:
            path = os.path.join(APX, name)
            if os.path.exists(path):
                text += "\n" + io.open(path, encoding="utf-8").read()
        surfaces["appendices"] = text

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
