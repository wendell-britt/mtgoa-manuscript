# -*- coding: utf-8 -*-
"""markpatterns.py -- the counts behind specs/MARK_PATTERN_TABLE_2026-09-09.md.

**FR-M4: every count in that table is produced here, never written in prose.** On 2026-09-09 I
made four wrong scope claims in one day -- five sites when there were ten, nineteen licensed when
there were eighteen, eleven lines when there were ten, thirty PRO sites when there were
twenty-four. Three were caught by a script's own closing recount and one by Wendell. **A number in
a cell that no script produces is a number I remembered.**

    python3 instruments/markpatterns.py          # every row's current count
    python3 instruments/markpatterns.py P3       # one row, with its sites
    python3 instruments/markpatterns.py -v       # every row, with sites

The seven rows are the patterns at the foot of `specs/PROOF_MARKS_CH2_CH3_2026-09-09.md`, written
from Wendell's marks on ch2 pp.25-52 and ch3 pp.53-95.

**Ruled scope: everything that ships.** The panel ruled ch1-ch9 only, on the argument that the
appendices are apparatus rather than reading voice. **Wendell overruled it, 2026-09-10: "The
checklists should cover the appendices."** Six Faces agreed with each other and were wrong about
whose book it is.

The shipping set comes from `profile.corpus`, not from a raw glob. The first version globbed
`appendices/*.md` and counted `PHASE2_HOSTILE_EDITORIAL_REVIEW.md` -- an editorial review that
lives in that directory and is not in the book.

**UNSEARCHABLE is a legal result.** P1 and P2 are judgements about what a clause is doing, and no
regex reaches them at usable precision. Recording that is the row's finding. A fabricated count is
worse than an empty cell.
"""
import io, os, re, sys, glob, collections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)
MARKED = ("ch2", "ch3")          # the chapters Wendell has read on paper


def chapters():
    return sorted(glob.glob(os.path.join(ROOT, "manuscript", "ch*.md")))


def apparatus():
    """Appendices, front matter and back matter -- ruled since 2026-09-10, on Wendell's overrule.

    The appendix list is profile.corpus's, so an editorial review that happens to sit in
    appendices/ is not mistaken for a shipping appendix."""
    out = []
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("profile",
                                                      os.path.join(HERE, "profile.py"))
        prof = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(prof)
        globs = [g for g in prof.corpus(["appendices/*.md"]) if "manuscript" not in g]
    except Exception:
        globs = ["appendices/APPENDIX_*.md"]
    for g in globs + ["front_matter/*.md", "back_matter/*.md"]:
        out += sorted(glob.glob(os.path.join(ROOT, g)))
    return [p for p in out if p.endswith(".md")]


def body(path):
    """Chapter text with the framed blocks removed: the marks were made on the reading voice."""
    return re.sub(r"<!--.*?-->", "", io.open(path, encoding="utf-8").read(), flags=re.S)


def name(path):
    return os.path.basename(path)[:-3]


# --------------------------------------------------------------------------- the searches

P3 = re.compile("|".join("(%s)" % p for p in [
    r"[Tt]his chapter (?:is|gives|does|will|hands|trains)",
    r"[Cc]hapter \d+ (?:gives|tells|is|will|does|hands)",
    r"Appendix [A-I] (?:says|has|lays|gives|tells)",
    r"[Hh]old (?:these|this) (?:three |two )?\w+, because",
    r"[Tt]he deeper truth is", r"[Ww]hat follows is",
    r"[Ii]n this chapter you will", r"[Bb]y the end of this chapter",
    r"[Ww]e will come back to", r"[Mm]ore on (?:this|that) in"]))

P4 = re.compile("|".join("(%s)" % p for p in [
    r"I could be wrong", r"I have guessed wrong", r"I have not solved", r"I may be wrong",
    r"I might be wrong", r"more than is useful", r"I am not sure", r"I don't know if",
    r"I do not know if", r"for what it(?:'s| is) worth", r"take (?:this|that) or leave it",
    r"I have no idea", r"perhaps I", r"maybe I(?:'m| am)", r"who am I to", r"I could well be",
    r"if I(?:'m| am) honest", r"or so I(?:'ve| have) told myself", r"I have been wrong",
    r"I was wrong about"]), re.I)

# P5's six marked phrases, plus the inflections. light_verb.py's coverage is reported per phrase
# rather than assumed, because it catches one of the six.
P5_PHRASES = [
    (r"\blands? \w+\b|\blanding\b", "lands/landing", True),
    (r"\bruns clean\b", "runs clean", False),
    (r"\btrades? \w+ for \w+\b", "trades X for Y", False),
    (r"\bbuys \w+\b", "buys X", False),
    (r"\bmetabolis?[zs]e[sd]?\b", "metabolize", False),
    (r"\bhow you are landing\b", "how you are landing", True),
]
P5 = re.compile("|".join("(%s)" % p for p, _, _ in P5_PHRASES), re.I)

P7 = re.compile(r"^#{2,3} Section \d+:|^#{2,3} Recap and Transition\s*$", re.M)

# Exercise apparatus, deliberately identical in every chapter. A form the reader learns to
# recognise is not a refrain losing weight, and marking one would be vandalism (panel, Q1).
STOP_APPARATUS = re.compile(r"^(?:\d+ ·|RECEIPT|Ten to fifteen|Two minutes|Did |A paragraph"
                            r"|Sit thirty seconds|Speak as|Greet it|Both are information)")


def refrain_sites(text):
    """A sentence repeated 3+ times inside one chapter. P6's shape: a line, not a word."""
    seen = collections.defaultdict(list)
    for m in re.finditer(r"[^.!?\n]{16,70}[.!?]", text):
        s = " ".join(m.group(0).replace("*", "").split())
        seen[s].append(m.start())
    return [(s, o) for s, o in seen.items()
            if len(o) >= 3 and not STOP_APPARATUS.match(s)]


ROWS = [
    ("P1", "interprets the observation — the ', and [what it means]' tack-on", None,
     "UNSEARCHABLE"),
    ("P2", "concludes for the reader — the verdict stamp", None, "UNSEARCHABLE"),
    ("P3", "manages the reader's path — the signposts", P3, None),
    ("P4", "undercuts itself — the hedges", P4, None),
    ("P5", "gestures with a nothing-word — the vague verb", P5, None),
    ("P6", "repeats a line as a refrain until it stops carrying weight", "refrain", None),
    ("P7", "construction scaffolding left in the reader's text", P7, None),
]


def count(row_re, paths):
    hits = []
    for p in paths:
        t = body(p)
        if row_re == "refrain":
            for s, offs in refrain_sites(t):
                hits.append((name(p), t.count("\n", 0, offs[0]) + 1, "%d× %s" % (len(offs), s)))
        else:
            for m in row_re.finditer(t):
                hits.append((name(p), t.count("\n", 0, m.start()) + 1,
                             " ".join(t[max(0, m.start() - 30):m.end() + 40].split())))
    return hits


def main():
    verbose = "-v" in sys.argv
    only = [a for a in sys.argv[1:] if not a.startswith("-")]

    print("mark patterns — counts for specs/MARK_PATTERN_TABLE_2026-09-09.md\n")
    print("%-4s %-48s %7s %10s %9s" % ("row", "shape", "ch1-9", "apparatus", "unmarked"))
    print("-" * 82)
    detail = []
    for rid, shape, rx, fixed in ROWS:
        if only and rid not in only:
            continue
        if rx is None:
            print("%-4s %-48s %7s %10s %9s" % (rid, shape[:48], "—", "—", "UNSEARCHABLE"))
            continue
        inside = count(rx, chapters())
        out = count(rx, apparatus()) if rx != "refrain" else []
        unmarked = sum(1 for f, _, _ in inside if f not in MARKED)
        print("%-4s %-48s %7d %10d %9d" % (rid, shape[:48], len(inside), len(out), unmarked))
        detail.append((rid, inside + out))
    print("-" * 82)
    print("both columns are ruled since 2026-09-10. apparatus = shipping appendices,")
    print("front matter and back matter, on Wendell's overrule of the panel.")
    print("unmarked = sites in chapters nobody has read on paper (everything but ch2, ch3).")

    if verbose or only:
        for rid, hits in detail:
            print("\n%s — %d site(s)" % (rid, len(hits)))
            for f, ln, ctx in hits[:40]:
                print("   %-5s:%-5d %s" % (f, ln, ctx[:92]))
            if len(hits) > 40:
                print("   … %d more" % (len(hits) - 40))

    # P5's row carries a coverage claim, so it is measured rather than asserted.
    if not only or "P5" in only:
        sys.path.insert(0, HERE)
        import importlib.util
        spec = importlib.util.spec_from_file_location("lv", os.path.join(HERE, "light_verb.py"))
        lv = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(lv)
        probes = [("Praise lands warm and leaves you smaller.", "lands/landing"),
                  ("The feeling runs clean through you.", "runs clean"),
                  ("It trades contact for control.", "trades X for Y"),
                  ("Vigilance buys aim.", "buys X"),
                  ("You metabolize the charge.", "metabolize")]
        print("\nP5 against light_verb.py, probe by probe:")
        seen = 0
        for sent, label in probes:
            hit = bool(lv.sites(sent)[0])
            seen += hit
            print("   %-16s %s" % (label, "flagged" if hit else "INVISIBLE"))
        print("   %d of %d marked phrase shapes are visible to the counter that was built "
              "from this pattern." % (seen, len(probes)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
