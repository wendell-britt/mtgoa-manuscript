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
    python3 marginalia/compile.py --verify    # body round-trips AND frames match insertions.py
    python3 marginalia/compile.py --regen     # rewrite insertions.py from the manuscript

DL-89, ruled 2026-09-09: **the manuscript is authoritative and insertions.py is regenerated from
it.** The source had 8 commits ever against the manuscript's 49, had never won a disagreement, and
destroyed approved prose the one time it was consulted. Retiring it would break --verify's three
consumers including a shipcheck category, so it keeps its consumers and loses its authority.

Two things changed on that ruling.

**--verify used to strip every frame from both sides and compare the body** -- the half that is
always identical. It reported "round-trip OK" over an eight-block divergence for six weeks. It now
compares frame text as well, so staleness is a ship blocker, and --regen is the one command that
clears it.

**--apply now refuses unless it can prove it reproduces the chapter it is about to overwrite.**
Making it idempotent instead was tried and abandoned: the manuscript and apply() disagree about
whitespace around a block, apply() writes two blank lines after a close tag where the hand-placed
blocks carry one, and reconciling that means rewriting the strip/apply whitespace contract under
seven live chapters to buy a mode whose job finished in June. **Refusing gives the same guarantee
for none of the risk.** A chapter that is not a fixed point is left untouched and named.
"""
import sys, os, re, io

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)
MS = os.path.join(ROOT, "manuscript")
sys.path.insert(0, HERE)

from insertions import (FRONT, BYLINE_NOTE, HANDBOOK, NOTES, POSTCARD, RECORDS,
                        SIGNATURE)

# Ch2 left the frame on 2026-08-01 and now sits with ch1: no byline, no epigraph, no
# margin. The fiction opens at front_matter/headmasters_letter.md, which falls between
# ch2 and ch3 in the spine, so nothing in-world may appear before it.
CHAPTERS = [3, 4, 5, 6, 7, 8, 9]
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
# 2026-09-09: the reader-facing headings lost their numbers (strike_scaffolding.py);
# the seam now keys on the invisible section anchor that precedes the heading.
SEAM_RE = re.compile(r"\n---\n\n<!-- SECTION 4 -->", re.M)
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


BODY_RE = re.compile(r"<!-- (%s|POSTCARD) -->\n(.*?)\n<!-- /\1 -->" % "|".join(KINDS), re.S)


def unquote(body):
    return "\n".join(l[2:] if l.startswith("> ") else ("" if l.strip() == ">" else l)
                      for l in body.split("\n")).strip()


def frames(txt):
    """(kind, text) for every framed block in document order, quote prefixes removed."""
    return [(k, unquote(b)) for k, b in BODY_RE.findall(txt)]


def divergence(ch):
    """(problems, [(held, live)]) -- what insertions.py holds against what the chapter carries."""
    ms = io.open(path(ch), encoding="utf-8").read()
    held_txt, _, problems = apply_chapter(ch, strip_marginalia(ms))
    if problems:
        return problems, []
    live, held = frames(ms), frames(held_txt)
    if [k for k, _ in live] != [k for k, _ in held]:
        return ["frame kinds differ: %d live, %d held" % (len(live), len(held))], []
    return [], [(h, l) for (_, h), (_, l) in zip(held, live) if h != l]


def fixed_point(ch):
    """Does apply(strip(chapter)) reproduce the chapter exactly? --apply's licence to write."""
    ms = io.open(path(ch), encoding="utf-8").read()
    rebuilt, _, problems = apply_chapter(ch, strip_marginalia(ms))
    return not problems and rebuilt.rstrip() == ms.rstrip()


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

    # DL-90. A Head's own record, boxed. Same insertion shape as NOTES and the same frame kind
    # as the admissions page, because it is the same sort of object: a document inside the
    # document. Italic in the source is what separates a private record from the filed form.
    for anchor, text in RECORDS.get(ch, []):
        c = txt.count(anchor)
        if c != 1:
            problems.append("RECORD anchor %s (%d matches): %r"
                            % ("MISSING" if c == 0 else "AMBIGUOUS", c, anchor[:60]))
            continue
        i = txt.find(anchor)
        j = txt.find("\n\n", i)
        j = len(txt) if j == -1 else j
        txt = txt[:j] + "\n" + block(text, "HANDBOOK") + txt[j:]
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


SRC = os.path.join(HERE, "insertions.py")


def regen():
    """DL-89. Rewrite insertions.py so it holds the frame text the manuscript carries.

    Atomic: the file goes back if the result does not verify. The patch is an exact string match,
    one occurrence, so an entry the compiler composes rather than stores -- ch8's three-tuple
    notes, where a signature is appended before boxing -- refuses instead of being mangled.

    Text only. Anchors are deliberately out of scope: two of them are stale (ch4's
    "The Skeptic, Up Close" and ch8's "The Damaged Self, Up Close" now sit a paragraph above
    their block), and a fix for that cannot be proved by the fixed-point test, because the
    whitespace contract keeps five chapters off it anyway. Unproven machinery is what this
    ruling exists to clear up, so the staleness is contained by --apply's refusal and recorded
    rather than patched."""
    pending = []
    for ch in CHAPTERS:
        problems, diff = divergence(ch)
        if problems:
            for x in problems:
                sys.stderr.write("ch%d: %s\n" % (ch, x))
            sys.stderr.write("REFUSED: resolve the anchors first. Nothing written.\n")
            return 1
        pending += diff
    if not pending:
        print("insertions.py already holds what the manuscript carries. Nothing to do.")
        return 0

    before = io.open(SRC, encoding="utf-8").read()
    after = before
    for held, live in pending:
        if after.count(held) != 1:
            sys.stderr.write("REFUSED: an entry appears %d times in insertions.py (need 1). "
                             "It is composed rather than stored.\n  %r\n"
                             % (after.count(held), held[:70]))
            return 1
        after = after.replace(held, live, 1)
    io.open(SRC, "w", encoding="utf-8").write(after)

    import importlib, insertions
    importlib.reload(insertions)
    globals().update({k: getattr(insertions, k) for k in
                      ("FRONT", "BYLINE_NOTE", "HANDBOOK", "NOTES", "POSTCARD", "RECORDS",
                       "SIGNATURE")})
    left = sum(len(divergence(ch)[1]) for ch in CHAPTERS)
    if left:
        io.open(SRC, "w", encoding="utf-8").write(before)
        sys.stderr.write("REFUSED: %d block(s) still diverge after the rewrite. "
                         "insertions.py restored.\n" % left)
        return 1
    print("insertions.py regenerated from the manuscript: %d block(s) updated, 0 diverging."
          % len(pending))
    return 0


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "--check"
    if mode == "--regen":
        return regen()
    if mode not in ("--check", "--apply", "--strip", "--verify"):
        print(__doc__)
        return 2

    if mode == "--strip":
        # DL-89. **--strip is the destructive step**, not --apply. --apply already refuses a
        # chapter that still has its frames; the way prose dies is strip-then-apply, because
        # stripping discards the authoritative copy and leaves insertions.py as the only one.
        # So this refuses unless apply() provably reproduces the chapter it is about to empty.
        # On 2026-09-09 that is five of seven, and those five are exactly the chapters where
        # this pair would have moved a paragraph.
        blocked = [ch for ch in CHAPTERS if not fixed_point(ch)]
        if blocked and "--force" not in sys.argv:
            for ch in blocked:
                print("ch%-2d REFUSED: apply() does not reproduce this chapter, so stripping "
                      "would not be reversible." % ch)
            print("\n%d chapter(s) refused. Nothing written. Pass --force with a reason in the "
                  "commit if\nyou mean to lose the frames." % len(blocked))
            return 1
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
            # DL-89. The body is the half that is always identical; compare the frames too, or
            # an eight-block divergence sits here for six weeks reporting "round-trip OK".
            _, diff = divergence(ch)
            if not ok:
                status = "ROUND-TRIP FAILED"; bad += 1
            elif diff:
                status = "%d FRAME BLOCK(S) STALE — run --regen" % len(diff); bad += 1
            else:
                status = "round-trip OK, frames match"
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
           "--verify": "Body text round-trips byte-identical and every frame block matches "
                       "insertions.py."}[mode])
    return 0


if __name__ == "__main__":
    sys.exit(main())
