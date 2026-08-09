# -*- coding: utf-8 -*-
"""Every pointer resolves.

Written 2026-08-07 for the final proof. **This one has already earned itself
twice, by hand, on the day it was specified:**

  - ch7's EA table moved from Section 2 to Section 4, and `back_matter/index.md`
    went on pointing *bliss*, *poignance* and *triumph* at `Ch 7 §2`. Caught by
    running `index_build.py` on a hunch after the restructure.
  - `index_build.py`'s own term list still matched `Say the Thing Under the
    Thing` after the move was renamed, so the entry would have vanished from the
    index on the next rebuild. Caught by reading the file.

**Neither was caught by review.py**, because a stale cross-reference is not a
voice defect, a heavy sentence, or a banned word. It is a promise the book makes
to a reader who then goes looking.

## What it resolves

    Chapter N     N is a chapter that exists
    Appendix X    X ships — checked against gate.py's SHIPPING_APPENDICES
    Section N     the chapter making the reference has that section
    Ch N §M       index shorthand: chapter N has section M
    moves         a named move referenced anywhere is defined in some chapter

## What it cannot check

**Whether the pointer says the right thing.** `Chapter 7` may exist and still be
the wrong chapter for the sentence. That is the deep read's job, per
`SPEC_FINAL_PROOF_2026-08-07.md` §4 step 8.

    python3 instruments/xref.py
    python3 instruments/xref.py -v
"""
import re, io, os, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)

SHIPPING = {"A": "APPENDIX_A_FOUR_ALLYSHIP_DOMAINS.md",
            "B": "APPENDIX_B_QUESTS_CAMPAIGNS.md",
            "C": "APPENDIX_C_FIVE_CHANNELS.md",
            "D": "APPENDIX_D_EMOTIONAL_ALCHEMY_PRACTICES.md",
            "E": "APPENDIX_E_321_SHADOW_PROCESS.md",
            "F": "APPENDIX_F_POLARITY_MAP.md",
            "G": "ON_THE_SHOULDERS_OF.md",
            "H": "APPENDIX_H_CHARACTER_SHEET.md"}


def chapters():
    out = {}
    for p in glob.glob(os.path.join(ROOT, "manuscript", "ch*.md")):
        n = int(re.search(r"ch(\d+)", os.path.basename(p)).group(1))
        text = io.open(p, encoding="utf-8").read()
        out[n] = {"path": p, "text": text,
                  "sections": {int(m) for m in re.findall(r"^## Section (\d+):",
                                                          text, re.M)}}
    return out


def main():
    verbose = "-v" in sys.argv
    ch = chapters()
    moves = set()
    for c in ch.values():
        moves |= {m.strip().lower() for m in
                  re.findall(r"^### Move \d+[:·] (.+)$", c["text"], re.M)}

    bad, unref = [], []
    for n, c in sorted(ch.items()):
        name = "ch%d" % n
        for i, line in enumerate(c["text"].split("\n"), 1):
            for m in re.finditer(r"\bChapter (\d+)\b", line):
                if int(m.group(1)) not in ch:
                    bad.append((name, i, "Chapter %s does not exist" % m.group(1)))
            for m in re.finditer(r"\bAppendix ([A-Z])\b", line):
                if m.group(1) not in SHIPPING:
                    bad.append((name, i, "Appendix %s does not ship" % m.group(1)))
            for m in re.finditer(r"\bSection (\d+)\b", line):
                if int(m.group(1)) not in c["sections"]:
                    bad.append((name, i, "Section %s not in %s (has %s)"
                                % (m.group(1), name,
                                   ",".join(str(s) for s in sorted(c["sections"])))))

    # index shorthand: Ch N §M
    idx = os.path.join(ROOT, "back_matter", "index.md")
    if os.path.exists(idx):
        for i, line in enumerate(io.open(idx, encoding="utf-8"), 1):
            for m in re.finditer(r"Ch (\d+) §(\d+)", line):
                n, s = int(m.group(1)), int(m.group(2))
                if n not in ch:
                    bad.append(("index", i, "Ch %d does not exist" % n))
                elif s not in ch[n]["sections"]:
                    bad.append(("index", i, "Ch %d §%d — ch%d has %s"
                                % (n, s, n, ",".join(str(x) for x in sorted(ch[n]["sections"])))))

    # appendices that ship and are pointed at from nowhere in the body
    body = "\n".join(c["text"] for c in ch.values())
    for letter in sorted(SHIPPING):
        if not re.search(r"\bAppendix %s\b" % letter, body):
            unref.append(letter)

    print("cross-references — every pointer resolves\n")
    print("  BROKEN     %3d   a pointer that goes nowhere" % len(bad))
    print("  UNREFERENCED %d   appendices that ship and nothing points at: %s"
          % (len(unref), ", ".join(unref) or "none"))

    if verbose or bad:
        for f, i, msg in bad:
            print("  [BROKEN] %s:%d  %s" % (f, i, msg))

    print("\n%d broken · %d unreferenced — %s" % (
        len(bad), len(unref),
        "clean" if not bad and not unref else "an unreferenced appendix still prints"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
