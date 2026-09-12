# -*- coding: utf-8 -*-
"""headings -- construction scaffolding showing through in the reader's headings.

Wendell, 2026-09-09, on the proof: "'Section 1: Urgency' ... a stupid heading that's a
holdout from when I was creating the chapters based on the Kotter model. It doesn't
mean anything to a reader and yet it snuck into multiple revisions."

It survived because the author cannot see his own scaffolding; he built with it.
This check sees it for him. Three signatures of the build frame in a heading:

  NUMBERED   `## Section N:` -- the outline's numbering
  TEMPLATE   the same H2 text in three or more chapters -- a slot label
             ("Recap and Transition", "The Practice"), not a content name
  KOTTER     a change-model word standing as a heading (Urgency, Coalition, Vision...)

The build may keep its anchors in an invisible `<!-- SECTION N -->` comment; that is
not a heading and this does not flag it.

    python3 instruments/headings.py FILE [FILE...]     # one or more chapters
    python3 instruments/headings.py                    # manuscript/ch1-9

Prints one score line per file (basename first, for review.py) then the hits.
Exit code = number of hits.
"""
import re, io, os, sys, glob, collections

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

NUMBERED = re.compile(r"^## Section \d+\s*[:\.]", re.M)
H2 = re.compile(r"^## (?!\*)(.+?)\s*$", re.M)          # skip the italic chapter subtitle
KOTTER = re.compile(r"^(Urgency|Coalition|Vision|Communicat\w*|Empower\w*|Enabl\w*|"
                    r"Short-?term Wins|Consolidat\w*|Anchor\w*|Institutionali\w*)$", re.I)

def h2_texts(txt):
    out = []
    for m in H2.finditer(txt):
        t = re.sub(r"^Section \d+\s*[:\.]\s*", "", m.group(1)).strip()
        out.append(t)
    return out

def main(paths):
    if not paths:
        paths = sorted(glob.glob(os.path.join(MS, "ch[0-9].md")))
    texts = {p: io.open(p, encoding="utf-8").read() for p in paths}
    seen = collections.Counter()
    for p, t in texts.items():
        for h in set(h2_texts(t)):
            seen[h] += 1
    total = 0
    for p, t in texts.items():
        base = os.path.basename(p)
        hits = []
        for m in NUMBERED.finditer(t):
            hits.append(("NUMBERED", m.group(0).strip()))
        for h in h2_texts(t):
            if seen[h] >= 3:
                hits.append(("TEMPLATE", "%s  (in %d chapters)" % (h, seen[h])))
            if KOTTER.match(h):
                hits.append(("KOTTER", h))
        total += len(hits)
        print("%s   headings %d   scaffold hits %d" % (base, len(h2_texts(t)), len(hits)))
        for kind, what in hits[:12]:
            print("  %-9s %s" % (kind, what))
    return total

if __name__ == "__main__":
    sys.exit(min(main(sys.argv[1:]), 120))
