# -*- coding: utf-8 -*-
"""
Seat the five missing Head register passages in ch3, ch5, ch6, ch7 and ch8.

`HEAD_REGISTERS.md` specified 60-120 words of register per chapter and left four
biographical facts to Wendell. Measured 2026-07-30: the pass never shipped for five of the
six Heads, and four of the placeholder tokens had zero occurrences in the manuscript, which
means the paragraph that would have carried them was never written. Ash is the exception and
his is already seated in ch4.

The passages come from three drafting passes recorded in `marginalia/specs/HEAD_VOICE_DIAL.md`
and collected at `marginalia/new_prose/HEAD_FACTS_pass3.md`. Each is written in that Head's
ruled genre from `SEVEN_VOICES.md`, and the set passes the blind test: every Head is the sole
extreme on at least one measured feature, so genre alone sorts them with the names stripped.

**Two deliberate departures from HEAD_REGISTERS, both recorded rather than smuggled.**

1. **Length.** These run 118 to 179 words against a stated 60-120. The budget was set before
   the genre work, and the genre is what made them separable -- a casebook entry that has to
   be a casebook entry cannot also be sixty words. Wendell should cut them if the page says
   otherwise; the argument for the length is the blind test, not the prose.

2. **Seating.** Ash's fact is woven mid-paragraph, one sentence. These are blocks. A woven
   sentence cannot carry a dated log entry or a numbered clause, and a block is native rather
   than intrusive here: if ch3's treatise *is* Voss's casebook, a session entry is the most
   ordinary thing that could appear in it. ch4 is left exactly as Wendell approved it.

    python3 instruments/head_facts_apply.py --dry
    python3 instruments/head_facts_apply.py
"""
import io, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")
DRAFTS = os.path.join(HERE, os.pardir, "marginalia", "new_prose", "HEAD_FACTS_pass3.md")

# (chapter, Head, the paragraph the passage goes after)
SEATS = [
    (3, "Voss", "The Shaman's practice is that staying."),
    (5, "Quill", "The Regent's actual practice is something harder and more alive:"),
    (6, "Vale", "Let me set something next to it, as a proposition rather than a diagnosis,"),
    (7, "Cross", "The problem is what it costs to generalize from it."),
    (8, "Orr", "Mastery is knowing which game you're playing and being able to put it down."),
]


def load():
    """Pull the six passages back out of the drafts file, so this script and that file
    cannot drift apart. The file is the source; this is the applicator."""
    text = io.open(DRAFTS, encoding="utf-8").read()
    out, cur, buf = {}, None, []
    for line in text.split("\n"):
        if line.startswith("## ") and " · " in line:
            if cur:
                out[cur] = "\n".join(buf).strip()
            cur = line.split("·")[0].replace("##", "").strip().split()[-1]
            buf = []
        elif cur is not None and line.startswith(">"):
            buf.append(line[2:] if line.startswith("> ") else line[1:])
    if cur:
        out[cur] = "\n".join(buf).strip()
    return out


def main():
    dry = "--dry" in sys.argv
    passages = load()
    missing = [h for _, h, _ in SEATS if h not in passages]
    if missing:
        raise SystemExit("drafts file has no passage for: %s" % ", ".join(missing))

    plan = []
    for ch, head, anchor in SEATS:
        p = os.path.join(MS, "ch%d.md" % ch)
        t = io.open(p, encoding="utf-8").read()
        if t.count(anchor) != 1:
            raise SystemExit("ch%d: anchor matched %d times: %r"
                             % (ch, t.count(anchor), anchor[:60]))
        # Insert after the end of the anchor's paragraph, never mid-paragraph.
        i = t.find(anchor)
        j = t.find("\n\n", i)
        if j < 0:
            raise SystemExit("ch%d: could not find the end of the anchor paragraph" % ch)
        body = passages[head]
        if body in t:
            raise SystemExit("ch%d: passage already present" % ch)
        plan.append((p, t[:j] + "\n\n" + body + t[j:], ch, head, len(body.split())))

    if dry:
        for _, _, ch, head, n in plan:
            print("ch%-2d %-6s %3d words -> after %r"
                  % (ch, head, n, dict((c, a) for c, h, a in SEATS)[ch][:52]))
        print("\n%d passages, every anchor matched exactly once" % len(plan))
        return 0

    for p, out, ch, head, n in plan:
        io.open(p, "w", encoding="utf-8").write(out)
    print("seated %d register passages: %s"
          % (len(plan), ", ".join("ch%d %s" % (c, h) for _, _, c, h, _ in plan)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
