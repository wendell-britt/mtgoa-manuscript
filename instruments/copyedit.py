# -*- coding: utf-8 -*-
"""
The copyedit pass: mechanics and house style, reported as patterns rather than sites.

`EDITORIAL_OPERATING_SYSTEM.md` puts this after content and line work are frozen —
"a conventional copyedit for mechanics and house-style consistency." It is the one
pass where the finding is almost never a single line. One `Face` against fourteen
`face` is not fourteen defects; it is one decision nobody has made yet, and fixing
it a line at a time is how a book ends up half-converted.

So this groups by **variant family**: every surface form of the same thing, with
its count and where it is. Wendell rules once per family, and the ruling applies
everywhere.

    python3 instruments/copyedit.py                  # the board
    python3 instruments/copyedit.py -v               # every site
    python3 instruments/copyedit.py --write FILE     # the full report

## Two things it will not do

**It never proposes which variant wins.** A house style is a decision, and the
majority form is not automatically the right one — `wu xing` is lowercase eleven
times and italicised twice on purpose, and a counter cannot see that.

**It scores the body and the margin separately, and never compares them.** The
Calrunia characters write British: `colour`, `organised`, `practising`,
`apologising`, none of which appear in Wendell's body text. That is the frame
working, and a copyedit that "corrected" it would erase the device the book is
built on. Every check below reports per surface for the same reason.
"""
import io, os, re, sys, importlib.util
from collections import defaultdict, Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    argv, sys.argv = sys.argv, [name]
    try:
        spec.loader.exec_module(mod)
    finally:
        sys.argv = argv
    return mod


fl = _load("find_line", os.path.join(HERE, "find_line.py"))


# The book's own vocabulary. Each family is a set of forms that mean one thing;
# the check reports which forms are in use and where, and rules on none of them.
# A term enters this list because the book coined it or leans on it, not because
# it looks capitalisable.
FAMILIES = [
    ("the Faces",        r"\b(Six Faces|six Faces|Six faces|six faces)\b"),
    ("a Face",           r"(?<![-\w])(Face|face)(?=[ ,.;:)]|$)"),
    ("Game Master",      r"\b(Game Master|Game master|game master|GM)\b"),
    ("the WAVE",         r"\b(WAVE|Wave)(?=[ ,.;:\-]|$)"),
    ("WAVE-Spiral",      r"\bWAVE[- ]Spiral\b|\bWave[- ]spiral\b"),
    ("BAR",              r"\b(BAR|BARs|Bar|bar)(?= deck| grid|s? \b)"),
    ("Token",            r"\b(Tokens?|tokens?)\b"),
    ("Ticket",           r"\b(Tickets?|tickets?)\b"),
    ("the schools",      r"\b(School of the [A-Z]\w+|school of the [a-z]\w+)\b"),
    ("five channels",    r"\b([Ff]ive [Cc]hannels)\b"),
    ("wu xing",          r"\b(wu xing|Wu Xing|wu-xing)\b"),
    ("Emotional Alchemy", r"\b([Ee]motional [Aa]lchemy)\b"),
    ("the Infinite Arcade", r"\b([Ii]nfinite [Aa]rcade)\b"),
    ("3-2-1",            r"\b(3-2-1|3‑2‑1|three-two-one)\b"),
    ("polarity map",     r"\b([Pp]olarity [Mm]ap)\b"),
    ("shadow work",      r"\b([Ss]hadow [Ww]ork)\b"),
]

# How the book points at its own parts. These need their own grouping rule: the
# question is whether the *shape* is consistent, and `Appendix A` against
# `Appendix G` is two appendices rather than two house styles. The number or
# letter is normalised to N before the forms are counted, so the family holds
# `Appendix N` against `appendix N` and nothing else.
XREF = [
    ("chapter reference", r"\b(Chapter \d+|chapter \d+|Ch\.? ?\d+|ch\d+)\b"),
    ("appendix reference", r"\b(Appendix [A-G]|appendix [A-G])\b"),
    ("section reference", r"\b(Section \d+|section \d+)\b"),
]
XREF_NAMES = {name for name, _ in XREF}
NORMALISE = re.compile(r"[A-G0-9]+$")

# Compounds the book uses. Discovered rather than listed: any hyphenated pair
# whose open or closed form also appears is a split the copyedit has to settle.
# Not `\b...\b`: that matched inside a longer hyphenated string, so
# `after-the-meeting` reported a `the-meeting` compound and `transcend-and-include`
# reported `transcend-and`. A compound is a compound only when nothing is attached
# to either end of it.
HYPHEN = re.compile(r"(?<![-\w])([a-z]{3,})-([a-z]{3,})(?![-\w])")

DOUBLED = re.compile(r"\b(\w+)\s+\1\b", re.I)
NUMWORD = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
           "six": "6", "seven": "7", "eight": "8", "nine": "9", "ten": "10"}

# British forms, listed rather than pattern-matched. The pattern version flagged
# `raised`, `rising`, `promised`, `disguised` and `revising` — words with no
# American variant at all — and buried the five real leaks under sixteen false
# ones. A stem list is longer to write and it only fires on words that genuinely
# have two spellings. `dialogue`, `catalogue`, `analogue` and `grey` came back out
# after the first run: all four are ordinary in American prose, and flagging them
# put eight false hits beside the eight real ones.
UK_STEMS = (
    "organis apologis practis recognis realis civilis minimis maximis summaris "
    "analys criticis memoris prioritis categoris normalis specialis standardis "
    "utilis visualis characteris sympathis patronis emphasis authoris "
    "familiaris legitimis marginalis moralis rationalis sensitis stabilis "
    "disorganis"
).split()
UK_WORDS = {
    "colour", "colours", "coloured", "behaviour", "behaviours", "favour",
    "favours", "favoured", "favourite", "honour", "honours", "honoured",
    "labour", "labours", "neighbour", "neighbours", "rigour", "vigour",
    "humour", "odour", "armour", "harbour", "harbours", "endeavour",
    "splendour", "centre", "centres", "centred", "theatre", "metre", "metres",
    "litre", "fibre", "defence",
    "offence", "licence", "travelled", "travelling", "cancelled",
    "modelling", "whilst", "amongst", "learnt", "spelt", "burnt", "sceptic",
    "sceptical", "storey", "storeys", "practise", "practises", "practised",
    "practising", "programme", "programmes", "manoeuvre", "sulphur",
}
UK_MARK = re.compile(
    r"\b(?:%s)\b|\b(?:%s)(?:e|es|ed|ing|ation|ations|er|ers)\b"
    % ("|".join(sorted(UK_WORDS)), "|".join(UK_STEMS)), re.I)
UK_FALSE = set()

TYPO_CHECKS = [
    ("curly quotes in source", r"[‘’“”]"),
    ("double space", r"[^\n] {2,}\S"),
    ("space before punctuation", r"\s+[,;.!?](?=\s|$)"),
    ("spaced en dash as a range", r"\d\s+[-–]\s+\d"),
]
# A straight-apostrophe check was here and came out backwards: 1,771 hits, which is
# every contraction in the book. The source is *meant* to be straight — the
# typesetter curls them, and Typst does. The real defect is the opposite one, and
# `curly quotes in source` above is it: four hits, all in Appendix C, where somebody
# pasted from a word processor.


# `front_matter/headmasters_letter.md` carries no marginalia markers, so the
# surface split called it body — and then reported its British spelling as a leak.
# It is a character's document, in-world, the same as the margin. Third surface.
LETTER = "front_matter/headmasters_letter.md"


def resurface(lines):
    for l in lines:
        if l["rel"] == LETTER:
            l["surface"] = "letter"
    return lines


def group_by_surface(lines):
    out = defaultdict(list)
    for l in lines:
        out[l["surface"]].append(l)
    return out


def families(lines, patterns):
    """For each family, which surface forms are in use, per surface."""
    found = defaultdict(lambda: defaultdict(lambda: {"n": 0, "sites": []}))
    for l in lines:
        for name, pat in patterns:
            for m in re.finditer(pat, l["text"]):
                form = m.group(0)
                if name in XREF_NAMES:
                    form = NORMALISE.sub("N", form)
                rec = found[(name, l["surface"])][form]
                rec["n"] += 1
                if len(rec["sites"]) < 6:
                    rec["sites"].append("%s:%d" % (l["rel"], l["line"]))
    # Only families with more than one form in use are findings.
    return {k: v for k, v in found.items() if len(v) > 1}


def hyphen_splits(lines):
    """A compound spelled two ways is a decision nobody made."""
    hyph, seen = defaultdict(lambda: {"n": 0, "sites": []}), Counter()
    text_by_surface = defaultdict(list)
    for l in lines:
        text_by_surface[l["surface"]].append(l)
        for m in HYPHEN.finditer(l["text"]):
            key = (m.group(1).lower(), m.group(2).lower(), l["surface"])
            hyph[key]["n"] += 1
            if len(hyph[key]["sites"]) < 4:
                hyph[key]["sites"].append("%s:%d" % (l["rel"], l["line"]))
    out = []
    for (a, b, surface), rec in sorted(hyph.items()):
        blob = "\n".join(l["text"] for l in text_by_surface[surface])
        openf = len(re.findall(r"\b%s %s\b" % (re.escape(a), re.escape(b)), blob, re.I))
        closed = len(re.findall(r"\b%s%s\b" % (re.escape(a), re.escape(b)), blob, re.I))
        if openf or closed:
            out.append((surface, "%s-%s" % (a, b), rec["n"], openf, closed, rec["sites"]))
    return sorted(out, key=lambda r: -(r[2] + r[3] + r[4]))


def numbers(lines):
    """A bare quantity before a noun, spelled one place and numeralled another.

    The first version counted every `one` against every `1` and reported 648
    against 99, which is the pronoun *one*, list markers, chapter numbers and
    section headings all counted as a spelling inconsistency. The only version of
    this question a copyeditor can act on is the same quantity of the same noun,
    written both ways: `three people` against `3 people`.
    """
    word_use = defaultdict(lambda: defaultdict(int))
    digit_use = defaultdict(lambda: defaultdict(lambda: {"n": 0, "sites": []}))
    for l in lines:
        s = l["surface"]
        for m in re.finditer(r"(?<![\w-])(\d{1,2})\s+([a-z]{3,})\b", l["text"]):
            digit_use[s][(m.group(1), m.group(2).lower())]["n"] += 1
            rec = digit_use[s][(m.group(1), m.group(2).lower())]
            if len(rec["sites"]) < 4:
                rec["sites"].append("%s:%d" % (l["rel"], l["line"]))
        for w in NUMWORD:
            for m in re.finditer(r"\b%s\s+([a-z]{3,})\b" % w, l["text"], re.I):
                word_use[s][(NUMWORD[w], m.group(1).lower())] += 1

    out = {}
    for s in digit_use:
        for key, rec in digit_use[s].items():
            wn = word_use[s].get(key, 0)
            if wn:
                out[(key, s)] = {"word": wn, "digit": rec["n"], "sites": rec["sites"]}
    return out


def simple(lines, pat, flags=0):
    hits = []
    for l in lines:
        for m in re.finditer(pat, l["text"], flags):
            hits.append(("%s:%d" % (l["rel"], l["line"]), l["surface"],
                         l["text"][max(0, m.start() - 35):m.end() + 35].strip()))
    return hits


def spelling(lines):
    out = defaultdict(lambda: defaultdict(int))
    sites = defaultdict(list)
    for l in lines:
        for m in UK_MARK.finditer(l["text"]):
            w = m.group(0).lower()
            out[l["surface"]][w] += 1
            if len(sites[(l["surface"], w)]) < 3:
                sites[(l["surface"], w)].append("%s:%d" % (l["rel"], l["line"]))
    return out, sites


def report(lines, verbose):
    L = []
    add = L.append
    by_surface = group_by_surface(lines)
    add("Surfaces: " + ", ".join("%s %d lines" % (k, len(v))
                                 for k, v in sorted(by_surface.items())))
    add("")

    add("## 1 · House terms with more than one form in use")
    add("")
    add("One ruling per family, applied everywhere. The instrument does not pick.")
    add("")
    fam = families(lines, FAMILIES + XREF)
    if not fam:
        add("No family splits. Nothing to rule.")
    for (name, surface), forms in sorted(fam.items()):
        total = sum(f["n"] for f in forms.values())
        add("**%s** — %s surface, %d uses across %d forms"
            % (name, surface, total, len(forms)))
        for form, rec in sorted(forms.items(), key=lambda kv: -kv[1]["n"]):
            add("  - `%s` × %d — %s" % (form, rec["n"], ", ".join(rec["sites"][:4])))
        add("")

    add("## 2 · Compounds spelled more than one way")
    add("")
    splits = hyphen_splits(lines)
    if not splits:
        add("None.")
    for surface, comp, h, o, c, sites in splits[:40 if not verbose else 400]:
        add("- `%s` (%s) — hyphenated %d, open %d, closed %d — %s"
            % (comp, surface, h, o, c, ", ".join(sites[:3])))
    add("")

    add("## 3 · Spelling convention, per surface")
    add("")
    add("The margin is written by the Calrunia characters and its British forms are")
    add("the device working. This is here to catch a British form leaking into the")
    add("body, or an American one leaking into the margin.")
    add("")
    sp, sites = spelling(lines)
    for surface in sorted(sp):
        words = sorted(sp[surface].items(), key=lambda kv: -kv[1])
        add("**%s** — %d marked form(s): %s"
            % (surface, len(words),
               ", ".join("`%s`×%d" % (w, n) for w, n in words[:14])))
    add("")

    add("## 4 · Numbers: the same value spelled and numeralled")
    add("")
    nums = numbers(lines)
    if not nums:
        add("None.")
    for ((digit, noun), surface), rec in sorted(
            nums.items(), key=lambda kv: -(kv[1]["digit"] + kv[1]["word"])):
        add("- **%s %s** (%s) — spelled %d, numeralled %d — %s"
            % (digit, noun, surface, rec["word"], rec["digit"],
               ", ".join(rec["sites"][:3])))
    add("")

    add("## 5 · Mechanics")
    add("")
    for name, pat in TYPO_CHECKS:
        hits = simple(lines, pat)
        add("**%s** — %d" % (name, len(hits)))
        for where, surface, ctx in hits[:6 if not verbose else 200]:
            add("  - %s (%s) `%s`" % (where, surface, ctx))
        add("")

    dbl = simple(lines, DOUBLED.pattern, re.I)
    add("**doubled word** — %d" % len(dbl))
    for where, surface, ctx in dbl[:20]:
        add("  - %s (%s) `%s`" % (where, surface, ctx))
    add("")
    return L


def main():
    verbose = "-v" in sys.argv
    out = None
    if "--write" in sys.argv:
        i = sys.argv.index("--write")
        out = sys.argv[i + 1] if i + 1 < len(sys.argv) else os.path.join(
            ROOT, "editorial_reports", "COPYEDIT.md")

    lines = resurface(fl.surfaces())
    body = report(lines, verbose)

    header = [
        "# Copyedit pass — mechanics and house style",
        "",
        "Generated by `instruments/copyedit.py` against the printed spine.",
        "",
        "**Findings are families, not sites.** One `Face` against fourteen `face` is",
        "one undecided question, not fourteen defects, and fixing it a line at a time",
        "is how a book ends up half-converted. Rule once per family; the ruling",
        "applies everywhere.",
        "",
        "**The instrument never picks the winner.** The majority form is not",
        "automatically right.",
        "",
        "| Status | Meaning |",
        "|---|---|",
        "| open | nobody has ruled |",
        "| ruled | Wendell picked a form; not yet applied |",
        "| applied | swept and re-measured |",
        "",
    ]
    text = "\n".join(header + body) + "\n"

    if out:
        os.makedirs(os.path.dirname(out), exist_ok=True)
        io.open(out, "w", encoding="utf-8").write(text)
        print("wrote %s (%d lines)" % (os.path.relpath(out, ROOT), len(text.split("\n"))))
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
