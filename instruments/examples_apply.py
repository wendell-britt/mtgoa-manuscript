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

    plan, problems = [], []
    for h, new in pairs:
        got = seats.get(h, [])
        if len(got) != 1:
            problems.append("draft heading %r matches %d Example(s) in ch%d"
                            % (h[:44], len(got), ch))
            continue
        plan.append((got[0], h, new))
    claimed = set(i for i, _, _ in plan)
    for h, idxs in seats.items():
        for i in idxs:
            if i not in claimed:
                problems.append("ch%d Example under %r has no draft" % (ch, (h or "?")[:44]))

    if problems:
        for p in problems:
            print("  -> %s" % p)
        raise SystemExit("%d problem(s). Nothing written." % len(problems))

    if dry:
        for i, h, new in plan:
            old = lines[i].strip()
            print("L%-5d %s" % (i + 1, h[:56]))
            print("    was %3d words  %s..." % (len(old.split()), old[13:75]))
            print("    now %3d words  %s...\n" % (len(new.split()), new[13:75]))
        print("%d Example(s), every heading matched exactly once" % len(plan))
        return 0

    for i, _, new in plan:
        lines[i] = new
    io.open(path, "w", encoding="utf-8").write("\n".join(lines))
    print("ch%d: seated %d Examples" % (ch, len(plan)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
