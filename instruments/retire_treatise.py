# -*- coding: utf-8 -*-
"""retire_treatise -- DL-85 applied: there are no treatises, and the margin annotates this book.

Wendell, 2026-09-09, ruling option B of specs/SPEC_WHOSE_VOICE_CH2_CH3_2026-09-09.md: *"I think we
should change the promise… the admissions page IS the treatise. There aren't any treatises anywhere
in the book."* Then, on the last open question: *"the margin is annotating this book."*

WHAT WAS WRONG. `ch2:577` promised *"six chapters, each opening with a treatise by the person who
runs one of the six schools: their method, in their voice, carrying their bias and their quarrel
with the other five."* Sections 1-3 do not do that. They are the fable, the concept and the
Polarity Map, in the book's own voice, addressing the reader as *you* 81 times in ch3's 2,810
words. The claim had ten carriers and all ten agreed with each other and none with the prose.

WHAT CHANGES, ten edits in four kinds:

  1  the promise at ch2:577, rewritten short and moved off the description of the sections
  6  signatures, out of their own frame at the seam and INSIDE the admissions box they belong to
  1  marginal noun swap, ch6:557, which only ever told a story about a document being submitted
  2  marginal rewrites, ch6:77 and ch7:159, which cannot take a swap because they point at
     sentences of the author's prose and one of them names a Head as the author

THE SIGNATURE MOVE IS NOT A REVERSAL OF 2026-07-30. What came off the top of the chapter then was
the full byline, because a submitted document is signed at the end of itself. It still is. What
changes is WHICH document: the admissions page, which the Head actually wrote and which opens
"Admissions. Filed as required." The signature goes inside that box, where the Headmaster's letter
already puts its own sign-off, rather than floating after it and attributing 2,800 words it does
not contain.

    python3 instruments/retire_treatise.py
"""
import io, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ruling import guard                        # FR-E1

CLAIM = "DL-85"                                 # the ruled fact in instruments/claims.yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)

SIGN = {
    3: "Maera Voss, Keeper of First Signals,\nHead of the School of the Body",
    4: "Corin Ash, Master of the Clean No,\nHead of the School of the Line",
    5: "Sera Quill, Keeper of Continuance,\nHead of the School of the Oath",
    6: "Irix Vale, Patternwright,\nHead of the School of the Pattern",
    7: "Elian Cross, Keeper of the Walk-Away Terms,\nHead of the School of the Bridge",
    8: "Thalen Orr, Keeper of the Far Game,\nHead of the School of the Horizon",
}

OLD_PROMISE = (
    "Turn the page and a letter is waiting, from the Headmaster. After it, six chapters, each "
    "opening with a treatise by the person who runs one of the six schools: their method, in their "
    "voice, carrying their bias and their quarrel with the other five. It runs as ordinary text "
    "until you reach a signature at the close of its third section. That is where a submitted "
    "document signs itself. Everything past that signature is me.\n"
    "\n"
    "The boxed inserts belong to the school as well: an admissions page saying who they take and "
    "what it costs, students and citizens on the record about what the teaching did to them. The "
    "margin is a hand that never signs.")

NEW_PROMISE = (
    "Turn the page for a letter from the Headmaster of a fictional school. After it, every chapter "
    "opens with one school's admissions page: who they take, what it costs, what you can do when "
    "you leave.")

# The two notes that cannot take a noun swap, and the one that can.
NOTES = [
    ('*"Also not not saying it" is the most honest line in this treatise, and Irix wrote it about',
     '*"Also not not saying it" is the most honest line about Irix on the page, and I do not think'),
    ("themselves without appearing to notice.*", "they have noticed.*"),
    ("*Their first draft of this treatise arrived on time and was then withdrawn, because there was a",
     "*Their first draft of this page arrived on time and was then withdrawn, because there was a"),
    ("*This is the sentence in the treatise I have quoted most and understood last.*",
     "*This is the sentence I have quoted most and understood last.*"),
]

# Every edit this script makes, counted for the guard. Six signatures, the promise, three notes.
EDITS = [("signature", ch) for ch in sorted(SIGN)] + [("promise", 2)] + \
        [("note", i) for i in range(3)]

SIG_BLOCK = re.compile(r"\n<!-- SIGNATURE -->\n(?:> .*\n)+<!-- /SIGNATURE -->\n")


def stage_chapter(ch):
    """Signature out of its own frame, into the last line of the admissions box."""
    rel = os.path.join("manuscript", "ch%d.md" % ch)
    text = io.open(os.path.join(ROOT, rel), encoding="utf-8").read()

    hits = SIG_BLOCK.findall(text)
    if len(hits) != 1:
        return None, "ch%d: %d signature block(s), need 1" % (ch, len(hits))
    text = SIG_BLOCK.sub("", text, count=1)

    close = "<!-- /HANDBOOK -->"
    if text.count(close) != 1:
        return None, "ch%d: %d handbook close(s), need 1" % (ch, text.count(close))
    block = "\n".join("> " + l for l in SIGN[ch].split("\n"))
    text = text.replace(close, ">\n%s\n%s" % (block, close), 1)
    return (rel, text), None


def main():
    guard(CLAIM, EDITS)                          # FR-E3

    # Staging is keyed BY PATH, not appended. The first version of this script appended
    # (path, text) tuples and staged ch6 and ch7 twice -- once for the signature move, once for
    # the marginal notes, each read fresh from disk -- so the second write silently discarded the
    # first. Both chapters kept their signature block and the script still reported success.
    staged, problems = {}, []

    def stage(rel, text):
        staged[rel] = text

    def current(rel):
        return staged.get(rel) or io.open(os.path.join(ROOT, rel), encoding="utf-8").read()

    for ch in sorted(SIGN):
        got, err = stage_chapter(ch)
        (problems.append(err) if err else stage(*got))

    # ch2's promise. Two paragraphs collapse to one.
    rel = "manuscript/ch2.md"
    t = current(rel)
    if t.count(OLD_PROMISE) != 1:
        problems.append("ch2: promise matched %d times, need 1" % t.count(OLD_PROMISE))
    else:
        stage(rel, t.replace(OLD_PROMISE, NEW_PROMISE, 1))

    # The three marginal notes live in BOTH the compiled chapters and insertions.py, and the two
    # have drifted (DL-89), so each is edited in place rather than recompiled.
    for rel in ("manuscript/ch6.md", "manuscript/ch7.md", "marginalia/insertions.py"):
        t = current(rel)
        for old, new in NOTES:
            if old in t:
                t = t.replace(old, new)
        stage(rel, t)

    # insertions.py: the signature text moves into the handbook, and SIGNATURE empties out.
    rel = "marginalia/insertions.py"
    t = current(rel)
    for ch, sig in sorted(SIGN.items()):
        head, tail = ("Head of the School of the %s" %
                      sig.split("School of the ")[1]), None
        # anchor on the closing of each HANDBOOK entry: the entry ends with `""",`
        m = re.search(r"(    %d: \"\"\".*?)\"\"\"," % ch, t, re.S)
        if not m:
            problems.append("insertions: no HANDBOOK entry for ch%d" % ch)
            continue
        if m.group(1).rstrip().endswith(sig.split("\n")[0].rstrip(",")):
            continue
        t = t[:m.end(1)] + "\n\n" + sig + "\"\"\"," + t[m.end():]
    old_sig = re.search(r"SIGNATURE = \{.*?\n\}\n", t, re.S)
    if not old_sig:
        problems.append("insertions: SIGNATURE dict not found")
    else:
        t = t[:old_sig.start()] + (
            "# SIGNATURE emptied 2026-09-09, DL-85. The six sign-offs moved INSIDE the admissions\n"
            "# box in HANDBOOK above, because that is the document the Head actually wrote. They\n"
            "# used to sit in their own frame at the seam and attribute 2,800 words of the author's\n"
            "# prose. The name is kept so compile.py's import and its branch stay valid.\n"
            "SIGNATURE = {}\n") + t[old_sig.end():]
        stage(rel, t)

    if problems:
        sys.stderr.write("REFUSED, nothing written:\n  " + "\n  ".join(problems) + "\n")
        sys.exit(2)

    for rel, text in sorted(staged.items()):
        io.open(os.path.join(ROOT, rel), "w", encoding="utf-8").write(text)
    print("retired the treatise: %d file(s) written" % len(staged))


if __name__ == "__main__":
    main()
