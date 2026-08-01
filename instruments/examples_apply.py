# -*- coding: utf-8 -*-
"""
Seat a chapter's Example beats from its drafts file.

`specs/SPEC_EXAMPLES_2026-07-31.md` rebuilds all 25 existing Examples and writes 10 more,
under the doubled position and the register at §2a. This applies one chapter at a time.

The drafts file is the source and this is the applicator, which is the arrangement
`handbook_seat.py` and `head_facts_apply.py` already use: edit the draft, re-run this, and
the two cannot drift.

**Matching is by Move heading, not by position.** An Example belongs to the Move it sits
under, and pairing them by index would silently mis-seat the whole chapter the first time a
Move is added or reordered. Every heading in the draft must match exactly one in the chapter,
and every Example in the chapter must be claimed, or nothing is written.

    python3 instruments/examples_apply.py 3 --dry
    python3 instruments/examples_apply.py 3
"""
import io, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)
DRAFTS = os.path.join(ROOT, "marginalia", "new_prose")


def parse(ch):
    """(heading, example) pairs from the prose below the drafts file's last rule."""
    p = os.path.join(DRAFTS, "EXAMPLES_ch%d.md" % ch)
    body = io.open(p, encoding="utf-8").read().rsplit("\n---\n", 1)[1]
    out, head = [], None
    for blk in body.strip().split("\n\n"):
        blk = blk.strip()
        if blk.startswith("###"):
            head = blk.lstrip("#").strip()
        elif blk.startswith("**Example:**") and head:
            out.append((head, " ".join(blk.split())))
            head = None
    return out


def main():
    ch = int([a for a in sys.argv[1:] if a.isdigit()][0])
    dry = "--dry" in sys.argv
    pairs = parse(ch)
    path = os.path.join(ROOT, "manuscript", "ch%d.md" % ch)
    lines = io.open(path, encoding="utf-8").read().split("\n")

    # Where each Example lives, and which Move heading owns it.
    seats, head = {}, None
    for i, l in enumerate(lines):
        s = l.strip()
        if s.startswith("#"):
            head = s.lstrip("#").strip()
        elif s.startswith("**Example:**"):
            seats.setdefault(head, []).append(i)

    # Where an Example could be inserted: ch5's Moves run What it is / In practice / The
    # test, with no Example slot at all, which is why that chapter has never carried one.
    # The scene belongs between the instruction and the check.
    tests, ends, head = {}, {}, None
    for i, l in enumerate(lines):
        s = l.strip()
        if s.startswith("#"):
            if head:
                ends[head] = i
            head = s.lstrip("#").strip()
        elif s.startswith("**The test:**") and head:
            tests.setdefault(head, i)
    if head:
        ends[head] = len(lines)

    plan, inserts, moves, problems = [], [], [], []
    for h, new in pairs:
        got = seats.get(h, [])
        if len(got) == 1:
            # ch8's Move 2 carries its Example AFTER its test, which every other Move in
            # the book has the other way round. Replacing in place would preserve the
            # inversion, so an out-of-order Example is lifted and reseated.
            if h in tests and got[0] > tests[h]:
                moves.append((got[0], tests[h], h, new))
            else:
                plan.append((got[0], h, new))
        elif not got and h in tests:
            inserts.append((tests[h], h, new))
        elif not got and h in ends:
            # ch8's Moves 3 and 5 have neither an Example nor a test, so the scene goes at
            # the end of the Move's own section, before the next heading.
            inserts.append((ends[h], h, new))
        else:
            problems.append("draft heading %r matches %d Example(s), no test and no end"
                            % (h[:40], len(got)))
    claimed = set(i for i, _, _ in plan) | set(i for i, _, _, _ in moves)
    for h, idxs in seats.items():
        for i in idxs:
            if i not in claimed:
                problems.append("ch%d Example under %r has no draft" % (ch, (h or "?")[:44]))

    if problems:
        for p in problems:
            print("  -> %s" % p)
        raise SystemExit("%d problem(s). Nothing written." % len(problems))

    if dry:
        for i, h, new in inserts:
            print("L%-5d %s" % (i + 1, h[:56]))
            print("    INSERT %3d words  %s...\n" % (len(new.split()), new[13:75]))
        for i, h, new in plan:
            old = lines[i].strip()
            print("L%-5d %s" % (i + 1, h[:56]))
            print("    was %3d words  %s..." % (len(old.split()), old[13:75]))
            print("    now %3d words  %s...\n" % (len(new.split()), new[13:75]))
        for old, new_i, h, new in moves:
            print("L%-5d %s" % (old + 1, h[:56]))
            print("    REORDER to L%d  %s...\n" % (new_i + 1, new[13:70]))
        print("%d replaced, %d inserted, %d reordered, every heading matched exactly once"
              % (len(plan), len(inserts), len(moves)))
        return 0

    for i, _, new in plan:
        lines[i] = new
    # Drop the out-of-order originals first, marking rather than deleting so the indices
    # gathered above stay valid, then insert everything bottom-up.
    for old, _, _, _ in moves:
        lines[old] = None
    for i, _, new in sorted(inserts + [(n, h, x) for _, n, h, x in moves],
                            key=lambda x: -x[0]):
        lines[i:i] = [new, ""]
    lines = [l for l in lines if l is not None]
    io.open(path, "w", encoding="utf-8").write("\n".join(lines))
    print("ch%d: %d replaced, %d inserted, %d reordered"
          % (ch, len(plan), len(inserts), len(moves)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
