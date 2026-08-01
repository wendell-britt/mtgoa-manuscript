# -*- coding: utf-8 -*-
"""
line_scan.py — the Lean OS Line Editor's own categories, as a candidate finder.

Pass 3 of `specs/EDITORIAL_OPERATING_SYSTEM.md` is the Line Editor: readability only,
after structure settles, at most ten flags per unit. Its brief names six defects —
ambiguity, vague reference, accidental repetition, a needlessly difficult sentence, a
weak logical transition, a grammar or style error — and until now this repo had an
instrument for none of them.

What existed measured neighbouring things. `gate.py` scores the standing canon list.
`prose_diet.py` scores register drift against *Igniting Joy*. `marginalia/review.py`
adjudicates voice. `dupes.py` catches an exactly repeated sentence in ch2-ch9.
`rescan.py` re-checks findings already written down. None of them answers the Line
Editor's question, which is narrower than all of these: **where does a reader have to
work, or double back, for something the sentence should have handed her.**

Six rules, each one derived from a defect the 2026-07-31 pass found by eye. That is
the whole design principle: mechanise what a reader already caught, so the second
reader does not have to catch it again.

  orphan-ref  a paragraph opening on It/This/That/These/Those/They with a heading or a
              marginalia block between the pronoun and its antecedent. From CH2 L2 —
              "That sentence" with thirteen lines and a margin block in the way.
  repeat      the same 8-word shingle twice in one chapter, far enough apart that it
              reads as an accident rather than a refrain. From CH2 L4, CH7 L1/L2/L3.
  doubled     a word printed twice in a row. From CH6 L1 — "the The Emotional Body",
              which survived every pass and the gate.
  hard        a sentence over 45 words, or over 35 carrying four or more commas.
  notbut      a not/but construction spanning 35 words or more: the reader holds a
              negation open across a clause and a half. From CH7 L6.
  banned-kin  words the canon bans, in forms the gate's regex does not reach. The gate
              closed `quiet(er|est)` on 2026-07-31 after two got through; this keeps
              the question open for the rest of the family.

**Every hit is a candidate, not a defect.** A refrain is a repeat until a reader says
it is a refrain; a 50-word sentence can be the best line on the page. The rules find
sites, and the Line Editor's seven-field flag — original, diagnosis, minimal edit,
reader problem, voice risk, leave-as-is rationale — is written by a reader who went
and looked. Nothing here modifies prose, and exit is always 0: a readability candidate
is not a build failure. That is `EDITORIAL_OPERATING_SYSTEM.md` rule 1, diagnosis
before revision.

    python3 instruments/line_scan.py              # per chapter, counts by rule
    python3 instruments/line_scan.py --margin -v  # the frame as its own surface (DL-6)
    python3 instruments/line_scan.py -v           # every hit with its line and quote
    python3 instruments/line_scan.py ch7          # one chapter, verbose
    python3 instruments/line_scan.py FILE.md      # any file, verbose
"""
import re, io, os, sys, glob
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)
MS = os.path.join(ROOT, "manuscript")

# The margin is a different hand and gets its own surface everywhere else in the
# toolkit; the Line Editor reads the body. Blocks are kept as boundary markers,
# because a block between a pronoun and its antecedent is the orphan-ref defect.
BLOCK_OPEN = re.compile(r"<!-- (MARGINALIA|EPIGRAPH-BYLINE|POSTCARD|HANDBOOK|SIGNATURE) -->")
BLOCK_CLOSE = re.compile(r"<!-- /(MARGINALIA|EPIGRAPH-BYLINE|POSTCARD|HANDBOOK|SIGNATURE) -->")
HEADING = re.compile(r"^\s{0,3}#{1,6}\s")
# A table row and a bullet are not sentences. Joining them into a paragraph and then
# counting words produced a 115-word "sentence" that is the channel table's header row,
# which is a measurement bug of exactly the kind prose_diet.py's own comments warn about.
TABLE = re.compile(r"^\s*\|")
BULLET = re.compile(r"^\s*(?:[-*+]\s|\d+[.)]\s)")

# The italic opener is deliberately NOT accepted. Found by this rule firing on its own
# fix: LE-3 repaired a cross-block pointer by quoting the line it pointed at
# (*This isn't working* is a verdict on the work), and the rule then flagged the repair
# as the defect. A demonstrative inside an italic quotation carries its antecedent with
# it. Bold is still accepted, because bold marks emphasis on the book's own sentence.
PRONOUN_OPEN = re.compile(r"^\s*(?:\*\*|>\s*)?(It|This|That|These|Those|They)\b"
                          r"(?!\s+(?:is|was|are|were)\s+(?:the\s+)?\w+ing\b)")
DOUBLED = re.compile(r"\b(the|a|an|and|of|to|in|is|that|you|it|for|with|but|on)\s+\1\b", re.I)
# "the The Emotional Body" — the second word capitalised, which is why a case-sensitive
# rule walked past it for three passes.
DOUBLED_CASED = re.compile(r"\b(the|a|an|and|of|to|in|that)\s+(The|A|An|And|Of|To|In|That)\b")
NOTBUT = re.compile(r"\bnot\b[^.!?]{60,}?\bbut\b[^.!?]*", re.I)
# The gate bans rooms?, quiet(ly|er|est)? and genuinely. These are the same words in
# forms the gate's pattern cannot see. Kept separate from the gate on purpose: the gate's
# zeros are not negotiable and these are candidates for Wendell.
BANNED_KIN = re.compile(r"\bgenuine\b|\bgenuineness\b|\bquietude\b|\broomy\b|\broominess\b", re.I)

SENT_SPLIT = re.compile(r"(?<=[.!?])\s+")
WORD = re.compile(r"[A-Za-z][A-Za-z'’-]*")
SHINGLE_N = 8
SHINGLE_GAP = 15          # lines apart before a repeat stops reading as a refrain
HARD_LONG = 45
HARD_COMMA_LEN, HARD_COMMAS = 35, 4

RULES = ["orphan-ref", "repeat", "doubled", "hard", "notbut", "banned-kin"]


def lines_of(path):
    return io.open(path, encoding="utf-8").read().split("\n")


def body_map(lines):
    """Return [(lineno, text, in_block)] — the margin marked, never dropped."""
    out, depth = [], 0
    for i, l in enumerate(lines, 1):
        if BLOCK_OPEN.search(l):
            depth += 1
            out.append((i, l, True)); continue
        if BLOCK_CLOSE.search(l):
            depth = max(0, depth - 1)
            out.append((i, l, True)); continue
        out.append((i, l, depth > 0))
    return out


def paragraphs(mapped):
    """Body paragraphs, with what separated each from the one before it."""
    paras, cur, sep = [], [], None
    for i, l, in_block in mapped:
        if in_block:
            if cur:
                paras.append((cur[0][0], " ".join(t for _, t in cur), sep)); cur = []
            sep = "block"
            continue
        if HEADING.match(l):
            if cur:
                paras.append((cur[0][0], " ".join(t for _, t in cur), sep)); cur = []
            sep = "heading"
            continue
        if TABLE.match(l):
            if cur:
                paras.append((cur[0][0], " ".join(t for _, t in cur), sep)); cur = []
            sep = "table"
            continue
        if BULLET.match(l):
            if cur:
                paras.append((cur[0][0], " ".join(t for _, t in cur), sep)); cur = []
            paras.append((i, l, "bullet")); sep = "bullet"
            continue
        if not l.strip():
            if cur:
                paras.append((cur[0][0], " ".join(t for _, t in cur), sep)); cur = []
                sep = "blank"
            continue
        cur.append((i, l))
    if cur:
        paras.append((cur[0][0], " ".join(t for _, t in cur), sep))
    return paras


def margin_map(lines):
    """The frame only, blockquote and emphasis markup stripped, one entry per line.

    Added 2026-08-01 for the margin's own pass. `--mode body` cannot double as this:
    the annotator is a different hand in a different genre, and DL-6 already rules the
    margin a separately scored surface. Returned in the same (lineno, text, in_block)
    shape as body_map so every rule downstream works unchanged, with in_block inverted —
    body lines become the thing that is skipped.

    Also returns {lineno: block type}, so a flag can say whether it landed in an unsigned
    annotation, an epigraph byline, the postcard, a handbook page or a signature. Those
    are five genres and the adjudication is different in each.
    """
    out, kinds, kind = [], {}, None
    for i, l in enumerate(lines, 1):
        m = BLOCK_OPEN.search(l)
        if m:
            kind = m.group(1)
            out.append((i, "", False)); continue
        if BLOCK_CLOSE.search(l):
            kind = None
            out.append((i, "", False)); continue
        if kind is None:
            out.append((i, "", False)); continue
        t = re.sub(r"^\s*>\s?", "", l)          # blockquote marker
        t = re.sub(r"^\s*\*(.*?)\*\s*$", r"\1", t.strip())  # the note's wrapping italics
        out.append((i, t, True)); kinds[i] = kind
    return out, kinds


def quote(s, n=100):
    s = re.sub(r"\s+", " ", s).strip()
    return s if len(s) <= n else s[:n - 1] + "…"


def scan(path, margin=False):
    lines = lines_of(path)
    kinds = {}
    if margin:
        mapped, kinds = margin_map(lines)
    else:
        mapped = body_map(lines)
    if margin:
        # Invert: the rules skip `in_block`, and in margin mode the body is what gets
        # skipped. Blank entries stand in for it, so line numbers stay true to the file.
        mapped = [(i, t, not inb) for i, t, inb in mapped]
    paras = paragraphs(mapped)
    hits = []

    # 1 · orphan-ref — the antecedent is on the far side of something the eye left.
    for start, text, sep in paras:
        if sep in ("block", "heading") and PRONOUN_OPEN.match(text):
            hits.append(("orphan-ref", start, quote(text),
                         "antecedent across a %s" % sep))

    # 2 · repeat — one 8-word shingle, twice, far apart.
    seen = defaultdict(list)
    for i, l, in_block in mapped:
        if in_block or HEADING.match(l) or not l.strip():
            continue
        w = [x.lower() for x in WORD.findall(l)]
        for j in range(len(w) - SHINGLE_N + 1):
            seen[" ".join(w[j:j + SHINGLE_N])].append(i)
    reported = set()
    for sh, where in sorted(seen.items(), key=lambda kv: kv[1][0]):
        if len(where) < 2 or max(where) - min(where) < SHINGLE_GAP:
            continue
        key = (min(where), max(where))
        if key in reported:
            continue
        reported.add(key)
        hits.append(("repeat", min(where), quote(sh),
                     "also at line %d" % max(where)))

    # 3 · doubled — a word printed twice.
    for i, l, in_block in mapped:
        if in_block:
            continue
        for m in (DOUBLED.search(l), DOUBLED_CASED.search(l)):
            if m:
                hits.append(("doubled", i, quote(l), m.group(0)))
                break

    # 4 · hard, 5 · notbut — sentence level, body only.
    for start, text, _ in paras:
        for s in SENT_SPLIT.split(text):
            n = len(WORD.findall(s))
            if n >= HARD_LONG:
                hits.append(("hard", start, quote(s, 120), "%d words" % n))
            elif n >= HARD_COMMA_LEN and s.count(",") >= HARD_COMMAS:
                hits.append(("hard", start, quote(s, 120),
                             "%d words, %d commas" % (n, s.count(","))))
            m = NOTBUT.search(s)
            if m and len(WORD.findall(m.group(0))) >= 35:
                hits.append(("notbut", start, quote(m.group(0), 120),
                             "%d words held open" % len(WORD.findall(m.group(0)))))

    # 6 · banned-kin — the family, in forms the gate cannot reach.
    for i, l, in_block in mapped:
        if in_block:
            continue
        m = BANNED_KIN.search(l)
        if m:
            hits.append(("banned-kin", i, quote(l), m.group(0)))

    if kinds:
        hits = [(r, l, t, "%s · in %s" % (w, kinds.get(l, "?"))) for r, l, t, w in hits]
    hits.sort(key=lambda h: (h[1], RULES.index(h[0])))
    return hits


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    margin = "--margin" in sys.argv
    verbose = "-v" in sys.argv or bool(args)
    if args:
        a = args[0]
        files = [a if os.path.exists(a) else os.path.join(MS, a.rstrip(".md") + ".md")]
    else:
        files = sorted(glob.glob(os.path.join(MS, "ch[1-9].md")))

    print("candidates, not defects — every hit needs a reader before it becomes a flag")
    print("surface: %s\n" % ("marginalia — the frame only" if margin else "body — the frame stripped"))
    head = "%-10s" % "file" + "".join("%12s" % r for r in RULES) + "%8s" % "total"
    print(head); print("-" * len(head))
    grand = Counter()
    for f in files:
        hits = scan(f, margin=margin)
        c = Counter(h[0] for h in hits)
        grand.update(c)
        print("%-10s" % os.path.basename(f)
              + "".join("%12d" % c[r] for r in RULES)
              + "%8d" % sum(c.values()))
        if verbose:
            for rule, line, text, why in hits:
                print("    %-11s %s:%-4d %s" % (rule, os.path.basename(f)[:-3], line, text))
                print("    %-11s %s└─ %s" % ("", " " * len(os.path.basename(f)[:-3]), why))
    print("-" * len(head))
    print("%-10s" % "TOTAL" + "".join("%12d" % grand[r] for r in RULES)
          + "%8d" % sum(grand.values()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
