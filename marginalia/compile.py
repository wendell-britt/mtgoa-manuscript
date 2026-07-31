# -*- coding: utf-8 -*-
"""
Apply the marginalia frame to the canonical chapters.

Repo-native port of the 2026-07-28 handoff's compile.py. Two things changed from
the original, both deliberate:

  1. Source is manuscript/ch{N}.md, not the /mnt/project docs. The project docs
     carried a STATUS header that is not book content, and their ch2 was one
     revision behind the working file — compiling from them silently dropped a
     seven-line passage. Compiling from canon cannot drift.
  2. --check dry-runs every anchor and writes nothing. Run it before --apply.

Insertions are wrapped in HTML comments so they stay greppable and strippable:
strip_marginalia() is the exact inverse of apply, and --verify proves it by
round-tripping every chapter back to byte-identical body text.

    python3 marginalia/compile.py --check     # anchors only, no writes
    python3 marginalia/compile.py --apply     # write marginalia into manuscript/
    python3 marginalia/compile.py --strip     # remove it again
    python3 marginalia/compile.py --verify    # apply+strip == original
"""
import sys, os, re, io

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)
MS = os.path.join(ROOT, "manuscript")
sys.path.insert(0, HERE)

from insertions import FRONT, BYLINE_NOTE, HANDBOOK, NOTES, POSTCARD, SIGNATURE

CHAPTERS = [2, 3, 4, 5, 6, 7, 8, 9]
# HANDBOOK added 2026-07-30. SPEC_SCHOOL_HANDBOOKS §8: it must join KINDS or --strip
# orphans six pages and --apply duplicates them, compounding on every cycle.
KINDS = ("MARGINALIA", "EPIGRAPH-BYLINE", "HANDBOOK", "SIGNATURE")
BLOCK_RE = re.compile(
    r"\n?\n<!-- (%s) -->\n.*?\n<!-- /\1 -->\n" % "|".join(KINDS), re.S)
# The postcard carries its own horizontal rule. Match the rule together with the
# block so stripping cannot eat a --- that belongs to the chapter: ch3 and ch5
# both legitimately end with one.
POSTCARD_RE = re.compile(r"\n+---\n+<!-- POSTCARD -->\n.*?\n<!-- /POSTCARD -->\n?", re.S)
ANY_BLOCK_RE = re.compile(r"<!-- (%s|POSTCARD) -->" % "|".join(KINDS))
FRONT_RE = re.compile(r"(^# CHAPTER.*?\n(?:.*?\n)??^## \*.*?\*\s*$)", re.M)
# The seam: the rule that closes Section 3. Verified 2026-07-30 to occur exactly once
# in each of ch3-ch8.
SEAM_RE = re.compile(r"\n---\n\n## Section 4", re.M)
# Trailing italic apparatus at the foot of Section 3 -- `*Back to the chapter.*` and the
# Appendix F pointer. These belong to the book rather than to the Head, so the signature
# goes ABOVE them and they land on the author's side of the boundary without moving.
# That is what makes this a zero-word change instead of a seven-line relocation.
APPARATUS_RE = re.compile(r"^\*[^*\n][^\n]*\*$")


def path(ch):
    return os.path.join(MS, "ch%d.md" % ch)


def block(text, kind):
    body = "\n".join("> " + l if l.strip() else ">"
                     for l in text.strip().split("\n"))
    return "\n<!-- %s -->\n%s\n<!-- /%s -->\n" % (kind, body, kind)


def seam_point(txt):
    """Index where a treatise signature is inserted: the end of Section 3, above any
    trailing italic apparatus. Returns None if the chapter has no Section 4."""
    m = SEAM_RE.search(txt)
    if not m:
        return None
    lines = txt[:m.start()].split("\n")
    while lines and (not lines[-1].strip() or APPARATUS_RE.match(lines[-1].strip())):
        lines.pop()
    return len("\n".join(lines))


def strip_marginalia(txt):
    return BLOCK_RE.sub("", POSTCARD_RE.sub("\n", txt))


def apply_chapter(ch, txt):
    """Return (new_text, n_inserted, problems)."""
    problems = []
    if ANY_BLOCK_RE.search(txt):
        return txt, 0, ["already has marginalia — strip first"]

    m = FRONT_RE.search(txt)
    if not m:
        return txt, 0, ["FRONT anchor miss"]
    front = block(FRONT[ch], "EPIGRAPH-BYLINE")
    n = 1
    # The school's admissions page sits between the testimonials and the margin: the
    # annotator is commenting on the Head, and that reads better once the Head has spoken.
    if ch in HANDBOOK:
        front += block(HANDBOOK[ch], "HANDBOOK")
        n += 1
    if ch in BYLINE_NOTE:
        front += block(BYLINE_NOTE[ch], "MARGINALIA")
    txt = txt[:m.end()] + "\n" + front + txt[m.end():]

    for entry in NOTES[ch]:
        # ch8's notes carry a third field, the signature, because in that chapter the
        # margin changes hands and five Heads plus Tull sign what they wrote. Every
        # other chapter is a 2-tuple and stays anonymous. A signature of None inside
        # ch8 is the anonymous hand returning, which is the reveal.
        anchor, note = entry[0], entry[1]
        signature = entry[2] if len(entry) > 2 else None
        c = txt.count(anchor)
        if c != 1:
            problems.append("anchor %s (%d matches): %r"
                            % ("MISSING" if c == 0 else "AMBIGUOUS", c, anchor[:60]))
            continue
        i = txt.find(anchor)
        j = txt.find("\n\n", i)
        j = len(txt) if j == -1 else j
        if signature:
            # Not italic and no dash. The name is apparatus rather than anybody's
            # voice, which is the rule the treatise signatures already follow.
            note = note.rstrip() + "\n\n" + signature
        txt = txt[:j] + "\n" + block(note, "MARGINALIA") + txt[j:]
        n += 1

    if ch in SIGNATURE:
        i = seam_point(txt)
        if i is None:
            problems.append("SEAM anchor miss")
        else:
            txt = txt[:i] + "\n" + block(SIGNATURE[ch], "SIGNATURE") + txt[i:]
            n += 1

    if ch == 9:
        txt = txt.rstrip() + "\n\n---\n" + block(POSTCARD, "POSTCARD")
        n += 1

    return txt, n, problems


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "--check"
    if mode not in ("--check", "--apply", "--strip", "--verify"):
        print(__doc__)
        return 2

    if mode == "--strip":
        for ch in CHAPTERS:
            t = io.open(path(ch), encoding="utf-8").read()
            io.open(path(ch), "w", encoding="utf-8").write(strip_marginalia(t))
            print("ch%-2d stripped" % ch)
        return 0

    print("%3s %9s %8s  %s" % ("ch", "inserted", "+words", "status"))
    print("-" * 58)
    bad = 0
    for ch in CHAPTERS:
        orig = io.open(path(ch), encoding="utf-8").read()
        # --check and --verify must work whether or not the frame is applied;
        # only --apply cares, and it refuses rather than double-inserting.
        if mode != "--apply":
            orig = strip_marginalia(orig)
        new, n, problems = apply_chapter(ch, orig)
        bad += len(problems)

        if mode == "--verify":
            ok = strip_marginalia(new).rstrip() == orig.rstrip()
            status = "round-trip OK" if ok else "ROUND-TRIP FAILED"
            bad += 0 if ok else 1
        else:
            status = "ok" if not problems else "%d PROBLEM(S)" % len(problems)

        print("%3d %9d %8d  %s" % (ch, n, len(new.split()) - len(orig.split()), status))
        for p in problems:
            print("      -> %s" % p)

        if mode == "--apply" and not problems:
            io.open(path(ch), "w", encoding="utf-8").write(new)

    print("-" * 58)
    if bad:
        print("%d problem(s). Nothing written." % bad if mode != "--apply"
              else "%d problem(s); affected chapters left untouched." % bad)
        return 1
    print({"--check": "All anchors resolve. Re-run with --apply to write.",
           "--apply": "Written to manuscript/.",
           "--verify": "Body text round-trips byte-identical."}[mode])
    return 0


if __name__ == "__main__":
    sys.exit(main())
