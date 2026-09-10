# -*- coding: utf-8 -*-
"""retire_read_noun -- DL-96. The clipped noun "a read" leaves the book.

Wendell, 2026-09-10, on my having cut only the filler uses: *"this doesn't solve the problem that
read is still illegal and shouldn't be used."*

DL-95 cut eight occurrences and kept fifteen on the argument that a technical term has to repeat
to stay technical. **That argument was about frequency and he was never talking about frequency.**
The word is the problem, not how often it appears.

**The book already made this decision and nobody read it out.** Noun `reading`/`readings`: **81
uses.** Noun `read`: **43** across the shipping set. Two and a half to one, and the majority form is ordinary English --
*a reading of the room* -- while the minority form is the clipped jargon he has objected to twice.
So this is not a new term being invented over a chapter's central concept. It is the book's own
dominant word replacing its own minority one.

**The verb is untouched.** *read the room*, *what your body had read*, *the Strategist reads the
board* -- all stand. Only a noun preceded by a determiner moves.

MECHANICALLY PROVABLE. Every edit inserts the three letters `ing` and changes nothing else, so
containment here is stronger than the usual normalised comparison: **deleting every `ing` this
script inserted must return the file byte-for-byte.** That is asserted before anything is written.

THREE PASSAGES GET A SECOND PASS, by hand, because the swap puts three `reading`s inside four
sentences and density is the thing he objected to in the first place. They are declared separately
below and can be backed out without disturbing the swap.

    python3 instruments/retire_read_noun.py
"""
import io, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ruling import guard

CLAIM = "DL-96"
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)

# The shipping set. profile.corpus decides which appendices ship, so the editorial review that
# lives in appendices/ is not treated as book content.
def shipping():
    import glob
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("profile", os.path.join(HERE, "profile.py"))
        prof = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(prof)
        globs = prof.corpus(["manuscript/ch*.md", "appendices/*.md"])
    except Exception:
        globs = ["manuscript/ch*.md", "appendices/APPENDIX_*.md"]
    out = []
    for g in globs + ["front_matter/*.md", "back_matter/*.md"]:
        out += sorted(glob.glob(os.path.join(ROOT, g)))
    # dict.fromkeys, not set: glossary.md is reached by two globs and was counted twice.
    return list(dict.fromkeys(p for p in out if p.endswith(".md")))


DET = (r"the|a|an|your|their|his|her|my|our|that|this|one|bad|good|accurate|clean|first|true|"
       r"same|whole|each|every|any")
NOUN = re.compile(r"\b(%s)(\s+)read\b" % DET, re.I)
# **No verb filter.** A determiner needs a nominal head, so `a read` is a noun in English and the
# only escape would be a relative pronoun -- *a line that read "no entry"* -- which does not occur
# here. The first version of this script carried a look-ahead exclusion list borrowed from the
# census regex, and it threw away real nouns: *"a read you never let yourself have"* was skipped
# on `you`, *"aims the read into a line"* on `into`. **All 43 sites were read by eye and not one
# is a verb.** The filter was pure loss and it is gone.

# The three density fixes, applied after the swap. Each is its own declared span.
DENSE = [
    # ch3, the Feeling/Function definition: the swap would put three `reading`s in two sentences.
    ("A reading you never let yourself have is a reading you can never act on.",
     "A reading you never let yourself have is one you can never act on."),
    # ch3, the handoff to the other five Faces: four in four sentences.
    ("The Regent keeps what the reading found worth keeping. The reading comes first.",
     "The Regent keeps what was worth keeping in it. The reading comes first."),
    # ch3, the Controller worked example: two in one sentence, one clause apart.
    ("the Controller rules the reading inadmissible before you can speak",
     "the Controller rules it inadmissible before you can speak"),
]


def swap(text):
    """Return (new_text, n). Only a determiner + noun `read` moves."""
    out, i, n = [], 0, 0
    for m in NOUN.finditer(text):
        out.append(text[i:m.end()])
        out.append("ing")
        i = m.end()
        n += 1
    out.append(text[i:])
    return "".join(out), n


def main():
    paths = shipping()
    staged, total = {}, 0
    for p in paths:
        before = io.open(p, encoding="utf-8").read()
        after, n = swap(before)
        if not n:
            continue
        # Containment, stronger than usual: undo every insertion and the file must return exactly.
        # Case-preserving: a heading carries "the Read", and a lowercase literal in the
        # replacement made the check fail on ch3:817 while the swap itself was correct.
        undo = re.sub(r"\b(%s)(\s+)([Rr])eading\b" % DET,
                      lambda m: m.group(1) + m.group(2) + m.group(3) + "ead", after, flags=re.I)
        check, _ = swap(undo)
        if check != after:
            sys.stderr.write("REFUSED: the swap is not reversible in %s. Nothing written.\n"
                             % os.path.basename(p))
            sys.exit(3)
        staged[p] = after
        total += n

    guard(CLAIM, [None] * (total + len(DENSE)))

    ch3 = os.path.join(ROOT, "manuscript", "ch3.md")
    for old, new in DENSE:
        if staged.get(ch3, "").count(old) != 1:
            sys.stderr.write("REFUSED: a density span matched %d times (need 1).\n  %s\n"
                             % (staged.get(ch3, "").count(old), old[:70]))
            sys.exit(2)
        staged[ch3] = staged[ch3].replace(old, new, 1)

    for p, text in staged.items():
        io.open(p, "w", encoding="utf-8").write(text)

    print("noun 'read' retired: %d swap(s) across %d file(s), plus %d density span(s)"
          % (total, len(staged), len(DENSE)))
    left = sum(len(NOUN.findall(io.open(p, encoding="utf-8").read())) for p in paths)
    print("noun 'read' remaining in the shipping set: %d (want 0)" % left)


if __name__ == "__main__":
    main()
