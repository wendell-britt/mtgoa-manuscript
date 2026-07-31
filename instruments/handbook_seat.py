# -*- coding: utf-8 -*-
"""
Seat the six School handbooks in `marginalia/insertions.py` as a HANDBOOK dict.

The prose was approved 2026-07-30 and has been sitting in
`marginalia/new_prose/HANDBOOKS_draft2.md` with no way to reach a page:
`HANDBOOK` had zero occurrences in `compile.py`, `insertions.py`, and every chapter.

`SPEC_SCHOOL_HANDBOOKS_2026-07-30.md` §8 fixes the mechanism as the signature's, now
proven: a dict here, a fourth entry in `compile.py`'s `KINDS`, and an anchor at the end of
the `EPIGRAPH-BYLINE` block. §2 fixes the position -- **above the marginalia**, because the
annotator is commenting on the Head and that reads better once the Head has spoken.

**Why a generator rather than typing the dict.** Same reason `head_facts_apply.py` reads its
passages back out of the drafts file: the draft is the source and this is the applicator, so
the two cannot drift. Run it again after any edit to draft 2 and the dict is rebuilt.

**Two format changes, both forced by the blockquote.** `block()` prefixes every line with
`> `, and an `##` inside a blockquote renders as a full heading in the middle of a chapter
opening. So the school name becomes bold and the filing line italic. Nothing else is touched:
the clause text is byte-identical to the approved draft.

    python3 instruments/handbook_seat.py --dry
    python3 instruments/handbook_seat.py
"""
import io, os, re, sys, textwrap

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)
DRAFT = os.path.join(ROOT, "marginalia", "new_prose", "HANDBOOKS_draft2.md")
INSERTIONS = os.path.join(ROOT, "marginalia", "insertions.py")

# The chapter each school's treatise occupies, from SIGNATURE in insertions.py.
CHAPTER = {"BODY": 3, "LINE": 4, "OATH": 5, "PATTERN": 6, "BRIDGE": 7, "HORIZON": 8}

HEADER = '''

HANDBOOK = {
    # 2026-07-30. Six schools, one mandated form. The institution requires every school to
    # file the same admissions page; six temperaments comply; the form is identical and what
    # leaks through is personality. Prose approved from
    # `marginalia/new_prose/HANDBOOKS_draft2.md`, rebuilt by
    # `instruments/handbook_seat.py` -- edit the draft, not this dict.
    #
    # Position is SPEC_SCHOOL_HANDBOOKS §2: below the epigraph testimonials, above the
    # marginalia, because the annotator is commenting on a Head who should have spoken first.
'''


def parse():
    """Split draft 2 into (school, body) at its `## THE SCHOOL OF THE X` headings."""
    text = io.open(DRAFT, encoding="utf-8").read()
    out, name, buf = {}, None, []
    for line in text.split("\n"):
        m = re.match(r"^## THE SCHOOL OF THE (\w+)\s*$", line)
        if m:
            if name:
                out[name] = buf
            name, buf = m.group(1), []
        elif name is not None:
            buf.append(line)
    if name:
        out[name] = buf
    return dict((k, render(k, v)) for k, v in out.items())


def render(school, lines):
    """Bold the school name, italicise the filing line, drop the trailing rule, and reflow
    each paragraph so the dict stays readable at the file's width."""
    filing = ""
    body = []
    for line in lines:
        m = re.match(r"^### (\*.*\*)\s*$", line)
        if m:
            filing = m.group(1)
            continue
        if line.strip() == "---":
            continue
        body.append(line)

    paras, cur = [], []
    for line in body:
        if line.strip():
            cur.append(line.strip())
        elif cur:
            paras.append(" ".join(cur))
            cur = []
    if cur:
        paras.append(" ".join(cur))

    head = "**THE SCHOOL OF THE %s**\n%s" % (school, filing)
    wrapped = [textwrap.fill(p, width=92, break_long_words=False,
                             break_on_hyphens=False) for p in paras]
    return head + "\n\n" + "\n\n".join(wrapped)


def main():
    dry = "--dry" in sys.argv
    books = parse()
    missing = [s for s in CHAPTER if s not in books]
    if missing:
        raise SystemExit("draft 2 has no handbook for: %s" % ", ".join(missing))

    src = io.open(INSERTIONS, encoding="utf-8").read()
    if "HANDBOOK = {" in src:
        raise SystemExit("insertions.py already carries a HANDBOOK dict")

    chunks = [HEADER]
    for school, ch in sorted(CHAPTER.items(), key=lambda kv: kv[1]):
        chunks.append('    %d: """%s""",\n' % (ch, books[school]))
    chunks.append("}\n")
    out = src.rstrip("\n") + "\n" + "".join(chunks)

    if dry:
        print("%-8s %-3s %5s %5s  %s" % ("school", "ch", "words", "paras", "opening clause"))
        print("-" * 78)
        for school, ch in sorted(CHAPTER.items(), key=lambda kv: kv[1]):
            b = books[school]
            first = [p for p in b.split("\n\n") if p.startswith("**1.")
                     or p.startswith("**Clause one")]
            print("%-8s %-3d %5d %5d  %s"
                  % (school, ch, len(b.split()), b.count("\n\n") + 1,
                     (first[0][:44] if first else "")))
        print("-" * 78)
        joined = "\n".join(books.values())
        print("em-dashes %d, banned words %d, second person %d"
              % (joined.count("—"),
                 len(re.findall(r"\brooms?\b|\bquiet(?:ly)?\b|\bgenuinely\b", joined, re.I)),
                 len(re.findall(r"\byou(?:r|rs|rself)?\b", joined, re.I))))
        print("\nfirst 6 lines of the ch3 entry as it will render:")
        for l in books["BODY"].split("\n")[:6]:
            print("  > %s" % l)
        return 0

    io.open(INSERTIONS, "w", encoding="utf-8").write(out)
    print("seated %d handbooks: %s"
          % (len(CHAPTER), ", ".join("ch%d %s" % (c, s.title())
                                     for s, c in sorted(CHAPTER.items(),
                                                        key=lambda kv: kv[1]))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
