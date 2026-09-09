# -*- coding: utf-8 -*-
"""box_the_records -- DL-90. Four Head's records, boxed and italicised.

Wendell, 2026-09-09, on the census: *"make sure they are italicized and I do think putting them in
boxes makes sense."*

The four passages are a Head's own record — Voss's session log, Quill's register of clauses with
her notes in two blocks, Cross's casebook — sitting in ordinary text with nothing attributing them.
All four were licensed by *"above the signature, only the Head"* until DL-85 retired that rule this
morning. Nothing was edited and nothing broke; the license was withdrawn from underneath them.

They take the **HANDBOOK** frame rather than a seventh kind. HANDBOOK is already *"a document
inside the document"*, which is exactly what these are, and inventing a frame for the same object
is the second-kingdom mistake Wendell's Governor spec names. Italic in the source separates a
private record from the filed admissions form that shares the box.

The manuscript is the compiled artefact, so each passage is removed from the body and re-inserted
from `insertions.RECORDS` — otherwise `compile.py --verify` would strip a box nothing could
rebuild. ch5 also loses one horizontal rule, which was separating the clause register from the
fable and is redundant once the register is in a box.

    python3 instruments/box_the_records.py
"""
import io, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "marginalia"))
from ruling import guard                            # FR-E1

CLAIM = "DL-90"                                     # the ruled fact in instruments/claims.yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)

# (chapter, first line, last line) of each passage as it stands before this runs, 1-indexed.
EDITS = [(3, 170, 176), (5, 113, 147), (5, 211, 217), (7, 145, 155)]


def main():
    guard(CLAIM, EDITS)                             # FR-E3

    import importlib
    ins = importlib.import_module("insertions")

    # THE BLOCK IS WRITTEN STRAIGHT INTO THE MANUSCRIPT, not rebuilt with apply_chapter.
    # The first version of this script rebuilt each chapter from insertions.py and **reverted
    # the ch3 proof-mark reworks** -- DL-89's footgun, fired by the script written to avoid it.
    # insertions.py is stale against the manuscript by 116 lines across five chapters, and
    # `--verify` cannot see it because it compares the body with every frame stripped. So the
    # record goes in where it already sits, and RECORDS carries the same text for a future build.
    staged, problems = {}, []
    by_ch = {}
    for ch, a, b in EDITS:
        by_ch.setdefault(ch, []).append((a, b))

    for ch, spans in sorted(by_ch.items()):
        rel = "manuscript/ch%d.md" % ch
        lines = io.open(os.path.join(ROOT, rel), encoding="utf-8").read().split("\n")
        records = list(ins.RECORDS.get(ch, []))
        for a, b in sorted(spans, reverse=True):
            passage = "\n\n".join(p.strip() for p in "\n".join(lines[a - 1:b]).split("\n\n")
                                   if p.strip())
            match = [r for r in records if _same(r[1], passage)]
            if len(match) != 1:
                problems.append("ch%d:%d-%d matched %d RECORDS entr(y/ies)"
                                % (ch, a, b, len(match)))
                continue
            records.remove(match[0])
            lo, hi = a - 1, b
            k = lo
            while k > 0 and not lines[k - 1].strip():
                k -= 1
            if k > 0 and lines[k - 1].strip() == "---":     # the rule only fenced the passage
                lo = k - 1
            block = ["<!-- HANDBOOK -->"]
            block += ["> " + l if l.strip() else ">" for l in match[0][1].split("\n")]
            block += ["<!-- /HANDBOOK -->"]
            lines[lo:hi] = block
        staged[rel] = "\n".join(lines)

    for ch in sorted(by_ch):
        rel = "manuscript/ch%d.md" % ch
        want = len(ins.RECORDS.get(ch, []))
        got = staged[rel].count("<!-- HANDBOOK -->") - 1     # minus the admissions page
        if got != want:
            problems.append("ch%d: %d record box(es), expected %d" % (ch, got, want))
        for anchor, _ in ins.RECORDS.get(ch, []):
            if anchor not in staged[rel]:
                problems.append("ch%d: RECORDS anchor missing: %r" % (ch, anchor[:50]))

    if problems:
        sys.stderr.write("REFUSED, nothing written:\n  " + "\n  ".join(problems) + "\n")
        sys.exit(2)

    for rel, text in sorted(staged.items()):
        io.open(os.path.join(ROOT, rel), "w", encoding="utf-8").write(text)
    print("boxed %d record(s) across %d chapter(s)" % (len(EDITS), len(by_ch)))


def _same(a, b):
    """RECORDS text against the manuscript passage, ignoring italic markers and wrapping."""
    norm = lambda s: " ".join(s.replace("*", "").split())
    return norm(a) == norm(b)


if __name__ == "__main__":
    main()
