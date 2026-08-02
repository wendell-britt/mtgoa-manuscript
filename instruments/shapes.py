# -*- coding: utf-8 -*-
"""
Syntactic shapes standing in for a plain statement.

    python3 instruments/shapes.py                  # the board
    python3 instruments/shapes.py -v               # every site
    python3 instruments/shapes.py --write FILE     # the full report

## Why this exists

Wendell's sixth read-through batch, 2026-08-01, named two shapes inside one
stretch of Chapter 1 and asked for a rule against the second of them:

> *"That model does not fail because people care too little. It fails because
> caring, run as suffering, burns down to nothing…"* — **Not X but Y. Simplify.**

> *"the campaign, the pledge, the training you complete, the bar you clear and then
> clear again."* — **definite articles creeping in in a repetitive way with no
> referent. We may need an even stricter rule around the use of "the" if this keeps
> up.**

> *"The being-needed. The safety of the line you never cross. The exhaustion you
> wear like proof."* — **more of the sentence fragments and definite articles.**

None of the three had an instrument. The first is worse than that: the repository's
own `/no-ai-slop` skill has banned it by name since it was written —

> **Binary contrasts.** *"This is not X. It's Y." / "The question isn't X, it's Y."*
> State Y directly.

— and the batch-edit scripts in this directory have repeatedly rewritten *into* the
shape rather than out of it. `w9_ch5.py:254` turns `Not because they're perfect —
because removing them would break something real.` into `Not because they're
perfect. Because removing them would break something real.` The em-dash was the
target and the em-dash is gone; the binary contrast survived the edit untouched.
`w8_batch_a.py`, `w8_batch_b.py`, `w9_ch4.py`, `w9_ch8.py` and `dl19_moves.py` all
do the same thing. That is the third time this session a banned family has been
found accumulating because a rule existed and nothing measured it.

## What it measures

**Binary contrast.** *Not X. Y.* in its several forms. A negation whose only job is
to set up the assertion after it. State the assertion.

**Definite-article series.** Three or more comma-separated noun phrases each opening
with *the*, where the referents are new. The article promises the reader has met
these already. In a list of new items it promises falsely, and the rhythm makes the
list feel like a definition when it is an example set.

**Determiner run.** Two or more consecutive short sentences opening on the same
determiner. Matched on the surface, not on part-of-speech tags: a tagger reads *The
impact fades.* as verbless because it takes *fades* for a plural noun, so a
fragment-detector built on tags reports things that are ordinary sentences. The run
is the honest signal, and it is the one Wendell actually flagged.

## What this is not

**None of the three is automatically a defect.** A binary contrast earns its place
when the reader genuinely holds X and has to put it down first. A determiner run is
a rhythm, and this book uses it deliberately inside the Examples, where a beat of
three fragments is the scene. The instrument reports sites; a reader rules.
"""
import io, os, re, sys, importlib.util
from collections import defaultdict

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

# The forms the shape actually takes in this manuscript, read off the 27 sites the
# first probe found rather than invented. Anchored so `not because` inside a longer
# clause ("he left not because he wanted to") is not counted — the shape is the
# negation standing as its own sentence or following a full stop.
BINARY = re.compile(
    r"(?:(?<=[.!?] )|(?<=\n)|^)Not because\b[^.!?]{0,120}[.!?]\s*(?:But )?[A-Z]"
    r"|\bdoes not \w+ because\b[^.!?]{0,120}\.\s*It \w+ because\b"
    r"|\bis not \w[^.!?]{0,80}\.\s*It(?:'s| is)\b"
    r"|[Tt]he question is ?n(?:'|o)t\b[^.!?]{0,80},? it(?:'s| is)\b"
    r"|[Ii]t(?:'s| is) not just \w[^.!?]{0,60}\bbut\b"
    r"|[Nn]ot (?:a|an|the) \w[^.!?]{0,40}\. (?:A|An|The) \w")

# Three or more comma-separated `the` phrases in one series.
SERIES = re.compile(r"\bthe [^,;:.!?]{2,40}, the [^,;:.!?]{2,40}, (?:and )?the [^,;:.!?]{2,60}",
                    re.I)

SENT = re.compile(r"(?<=[.!?])\s+")
DET = re.compile(r"^(The|A|An|Your|Its|His|Her|Their|Our|My)\b")


def runs(text):
    """Consecutive short sentences opening on the same determiner, 2 or more."""
    sents = [s.strip() for s in SENT.split(text) if s.strip()]
    out, cur, det = [], [], None
    for s in sents:
        m = DET.match(s)
        short = len(s.split()) <= 9
        if m and short and (det is None or m.group(1) == det):
            det = m.group(1)
            cur.append(s)
            continue
        if len(cur) >= 2:
            out.append(" ".join(cur))
        cur, det = ([s], m.group(1)) if (m and short) else ([], None)
    if len(cur) >= 2:
        out.append(" ".join(cur))
    return out


def main():
    verbose = "-v" in sys.argv
    out = None
    if "--write" in sys.argv:
        i = sys.argv.index("--write")
        out = sys.argv[i + 1] if i + 1 < len(sys.argv) else os.path.join(
            ROOT, "editorial_reports", "SHAPES_BOARD.md")

    lines = [l for l in fl.surfaces()
             if not l["text"].lstrip().startswith(("#", "|"))]
    found = defaultdict(list)
    per = defaultdict(lambda: defaultdict(int))
    for l in lines:
        for m in BINARY.finditer(l["text"]):
            found["binary contrast"].append((l, m.group(0)))
            per[l["rel"]]["binary contrast"] += 1
        for m in SERIES.finditer(l["text"]):
            found["definite-article series"].append((l, m.group(0)))
            per[l["rel"]]["definite-article series"] += 1
        for r in runs(l["text"]):
            found["determiner run"].append((l, r))
            per[l["rel"]]["determiner run"] += 1

    NAMES = ["binary contrast", "definite-article series", "determiner run"]
    L = ["# Shapes standing in for a plain statement — the board", "",
         "Generated by `instruments/shapes.py`. Body and margin prose; headings and",
         "table rows excluded. Named by Wendell 2026-08-01 in the sixth read-through",
         "batch; see the module docstring for what each shape is and is not.", "",
         "**Nothing here is automatically a defect.** The determiner run in particular",
         "is a deliberate rhythm inside the Examples. These are sites, not rulings.", "",
         "**One caveat on the binary-contrast count.** Five of them are the same",
         "sentence: *The tell that a quest is alive is not enthusiasm. It is",
         "anticipation with some dread underneath it.* — a deliberate refrain closing",
         "the quest section of ch3, ch4, ch5, ch6 and ch7. It is not five defects. It",
         "is one decision, and `ch4:744` says *It arrives as anticipation*, which makes",
         "the refrain inconsistent in exactly one place.", ""]
    total = sum(len(found[n]) for n in NAMES)
    L += ["## Totals — %d sites" % total, "", "| Shape | sites |", "|---|---|"]
    for n in NAMES:
        L.append("| %s | **%d** |" % (n, len(found[n])))
    L.append("")

    L += ["## Per component", "",
          "| Component | " + " | ".join(NAMES) + " | total |",
          "|---" * (len(NAMES) + 2) + "|"]
    spine = [rel for _, _, rel, _ in fl.bb.SPINE if rel]
    for rel in sorted(per, key=lambda r: spine.index(r) if r in spine else 999):
        row = [per[rel][n] for n in NAMES]
        L.append("| %s | %s | **%d** |" % (os.path.basename(rel),
                                           " | ".join(str(x) for x in row), sum(row)))
    L.append("")

    for n in NAMES:
        L += ["## %s — %d" % (n, len(found[n])), ""]
        for l, hit in found[n][:20 if not verbose else 600]:
            L.append("- `%s` · %s:%d" % (" ".join(hit.split())[:110], l["rel"], l["line"]))
        L.append("")

    text = "\n".join(L) + "\n"
    if out:
        os.makedirs(os.path.dirname(out), exist_ok=True)
        io.open(out, "w", encoding="utf-8").write(text)
        print("wrote %s — %d sites" % (os.path.relpath(out, ROOT), total))
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
