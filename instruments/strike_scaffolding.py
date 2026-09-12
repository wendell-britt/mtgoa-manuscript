# -*- coding: utf-8 -*-
"""strike_scaffolding -- take the build frame out of the reader's headings (2026-09-09).

Wendell, on the proof: "'Section 1: Urgency' ... a holdout from when I was creating the
chapters based on the Kotter model. It doesn't mean anything to a reader and yet it snuck
into multiple revisions." The 6-GM panel (PANEL_PROOF_MARKS_6FACE_2026-09-09.md, Round 2)
ruled: strike book-wide, under one rule, with the build's anchors kept invisible.

What this does, once, to manuscript/ch2-ch9:

  1. Above every `## Section N: Label` it inserts `<!-- SECTION N -->`. That comment is
     the build's anchor from now on: marginalia/compile.py finds the treatise seam by it
     and marginalia/insertions.py anchors notes to it. pandoc drops HTML comments in the
     PDF and they are invisible in the EPUB; gate and the round-trip ignore them because
     they are not a marginalia kind.
  2. If the label is a template slot (identical text in three or more chapters, plus
     'Urgency' by name) AND an italic `### *subtitle*` follows, the subtitle becomes the
     H2 and the H3 line is dropped. The reader-facing name was already on the page.
  3. Otherwise the H2 keeps its label with the number removed.
  4. Seventeen in-prose cross-references ("in Section 4") are rewritten to refer by
     content or position, each one listed in PROSE_REFS below so the diff shows it.
  5. compile.py's SEAM_RE and insertions.py's anchors are rekeyed to the comment.

Every template heading in ch2-ch9 carries an italic subtitle (some after a blank line),
so every one is promoted; nothing is written new. The one content heading without a
subtitle, ch2 "Who's Holding the Joystick", keeps its name minus the number.

    python3 instruments/strike_scaffolding.py          # apply
"""
import io, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)
MS = os.path.join(ROOT, "manuscript")

TEMPLATE = {"The Exile", "The Distortion", "The Concept", "The Practice", "The Game",
            "Recap and Transition", "Urgency"}
H2 = re.compile(r"^## Section (\d+)\s*[:.]\s*(.+?)\s*$")
SUB = re.compile(r"^### \*(.+?)\*\s*$")

PROSE_REFS = [
 ("ch3", "which is the distortion Section 2 described.",
         "which is the distortion described earlier in this chapter."),
 ("ch3", "Everything in Section 4 was the instrument.",
         "Everything in the practice was the instrument."),
 ("ch3", "Section 4 taught you to run that alone.",
         "The practice taught you to run that alone."),
 ("ch3", "Section 4 taught you to name the channel for yourself,",
         "The practice taught you to name the channel for yourself,"),
 ("ch3", "A channel named only to yourself belongs to Section 4.",
         "A channel named only to yourself belongs to the interior practice."),
 ("ch4", "You drew the Force ↔ Restraint axis in Section 4.",
         "You drew the Force ↔ Restraint axis earlier in this chapter."),
 ("ch4", "and Section 4 named what each one costs alone.",
         "and the axis named what each one costs alone."),
 ("ch5", "You drew the Honor ↔ Reform axis in Section 4.",
         "You drew the Honor ↔ Reform axis earlier in this chapter."),
 ("ch6", "That repeats the exile in Section 1, in miniature",
         "That repeats the exile that opened this chapter, in miniature"),
 ("ch6", "You drew the Structure ↔ Agency axis in Section 4.",
         "You drew the Structure ↔ Agency axis earlier in this chapter."),
 ("ch6", "Section 3 named the drift;",
         "This chapter already named the drift;"),
 ("ch7", "What it is *for* arrives at the end of Section 5.",
         "What it is *for* arrives with the Victim, later in this chapter."),
 ("ch7", "Section 1 ran the sequence and said why each stage earns the next.",
         "The opening exile ran the sequence and said why each stage earns the next."),
 ("ch7", "You met it in Section 3: allyship means never causing harm.",
         "You met it earlier in this chapter: allyship means never causing harm."),
 ("ch7", "You drew the Care ↔ Impact axis in Section 4.",
         "You drew the Care ↔ Impact axis earlier in this chapter."),
 ("ch7", "go back to the Care ↔ Impact axis you drew in Section 4 before you try to close.",
         "go back to the Care ↔ Impact axis you drew earlier before you try to close."),
 ("ch8", "You drew the Which Game ↔ Which Altitude axis in Section 4.",
         "You drew the Which Game ↔ Which Altitude axis earlier in this chapter."),
 ("ch9", "Section 4 asked which ones you live in",
         "The practice asked which ones you live in"),
]


def retitle(text):
    lines = text.split("\n")
    out, i, promoted, kept = [], 0, 0, 0
    while i < len(lines):
        m = H2.match(lines[i])
        if not m:
            out.append(lines[i]); i += 1; continue
        n, label = m.group(1), m.group(2).strip()
        j = i + 1
        while j < len(lines) and not lines[j].strip():
            j += 1
        sm = SUB.match(lines[j]) if j < len(lines) else None
        out.append("<!-- SECTION %s -->" % n)
        if label in TEMPLATE and sm:
            title = sm.group(1).strip().strip('"“”')
            out.append("## " + title)
            promoted += 1
            i = j + 1
        else:
            out.append("## " + label)
            kept += 1
            i += 1
    return "\n".join(out), promoted, kept


def main():
    for ch in range(2, 10):
        p = os.path.join(MS, "ch%d.md" % ch)
        t = io.open(p, encoding="utf-8").read()
        for tag, old, new in PROSE_REFS:
            if tag != "ch%d" % ch:
                continue
            c = t.count(old)
            assert c == 1, "ch%d prose ref matched %d times: %r" % (ch, c, old[:50])
            t = t.replace(old, new)
        t, promoted, kept = retitle(t)
        io.open(p, "w", encoding="utf-8").write(t)
        print("ch%d: promoted %d, kept %d" % (ch, promoted, kept))

    cp = os.path.join(ROOT, "marginalia", "compile.py")
    c = io.open(cp, encoding="utf-8").read()
    old = 'SEAM_RE = re.compile(r"\\n---\\n\\n## Section 4", re.M)'
    assert c.count(old) == 1, "SEAM_RE not found once"
    c = c.replace(old,
        '# 2026-09-09: the reader-facing headings lost their numbers (strike_scaffolding.py);\n'
        '# the seam now keys on the invisible section anchor that precedes the heading.\n'
        'SEAM_RE = re.compile(r"\\n---\\n\\n<!-- SECTION 4 -->", re.M)')
    io.open(cp, "w", encoding="utf-8").write(c)
    print("compile.py: SEAM_RE rekeyed")

    ip = os.path.join(ROOT, "marginalia", "insertions.py")
    s = io.open(ip, encoding="utf-8").read()
    s2, n = re.subn(r'^\("## Section (\d+)",', r'("<!-- SECTION \1 -->",', s, flags=re.M)
    assert n == 8, "expected 8 insertion anchors, rekeyed %d" % n
    io.open(ip, "w", encoding="utf-8").write(s2)
    print("insertions.py: %d anchors rekeyed" % n)


if __name__ == "__main__":
    main()
