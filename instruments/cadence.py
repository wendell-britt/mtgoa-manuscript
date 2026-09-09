# -*- coding: utf-8 -*-
"""cadence -- the two sentence-molds the eye catches and the counters miss.

Wendell highlighted the whole back half of ch3 (pp.66-95) in the proof and wrote
"Rework." The marks were not logic errors and not repeated ideas (dupes is clean).
They were two sentence-shapes, run until the prose went monotone:

  VERDICT   a short demonstrative-copula sentence that lands a summary --
            "That is the mechanism." "It was not." "The Grow stage is the integration."
  COMPOUND  a clause tacked on with ", and ..." -- "...and the picking exhausts you."

The chapter's default sentence became "X, and Y. That is Z." telling.py flagged 2
labels across that 300-line stretch and trailing_and.py flagged 1; the eye flagged
scores. This measures both molds per paragraph so a rework targets the dense windows.

It is a LOCATOR, not a target to minimise. Breaking a run-on into short sentences
trades a COMPOUND for a VERDICT on purpose; the good verdicts earn their drumbeat.
Chase the number and you flatten the voice. Read the hotspots; let the ear decide.

    python3 instruments/cadence.py FILE [FILE...]

Prints one score line per file (basename first, for review.py) then the densest
paragraphs. Exit code = count of paragraphs at load >= 4.
"""
import re, io, sys, os

VERDICT = re.compile(r"^(That|This|It|These|Those|Both|Here|Theirs)\s+(is|was|are|were|'s)\b", re.I)
SHORT_COP = re.compile(r"^\w[\w' ]{0,40}?\b(is|was|are|were)\b")
COMPOUND = re.compile(r",\s+and\b")

def sentences(t):
    t = re.sub(r"\s+", " ", t)
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+(?=[A-Z“\"*])", t) if s.strip()]

def paragraphs(fn):
    out, buf, start = [], [], 1
    for i, l in enumerate(io.open(fn, encoding="utf-8").read().split("\n"), 1):
        s = l.strip()
        if s.startswith(("<!--", ">", "#", "|")):      # frames, marginalia, headings, tables
            continue
        if not s:
            if buf: out.append((start, " ".join(buf))); buf = []
            continue
        if not buf: start = i
        buf.append(s)
    if buf: out.append((start, " ".join(buf)))
    return out

def score(fn):
    base = os.path.basename(fn)
    V = C = S = 0
    rows = []
    for ln, p in paragraphs(fn):
        sents = sentences(p)
        if not sents: continue
        v = sum(1 for s in sents if VERDICT.match(s) or (len(s.split()) <= 7 and SHORT_COP.match(s)))
        c = len(COMPOUND.findall(p))
        V += v; C += c; S += len(sents)
        if v + c >= 4:
            rows.append((v + c, ln, v, c, len(sents), p))
    rv = 100.0 * V / max(S, 1)
    rc = 100.0 * C / max(S, 1)
    print("%s   verdict %d (%.1f/100)  compound %d (%.1f/100)  hot %d"
          % (base, V, rv, C, rc, len(rows)))
    for load, ln, v, c, ns, p in sorted(rows, reverse=True)[:8]:
        print("  %s:%d  load %d  (%d verdict / %d and, %d sent)" % (base, ln, load, v, c, ns))
        print("      %s" % p[:120])
    return len(rows)

if __name__ == "__main__":
    sys.exit(min(sum(score(f) for f in sys.argv[1:]), 120))
