# -*- coding: utf-8 -*-
"""
Re-scan the 2026-07-31 editorial reports against the manuscript as it stands now.

The eleven reports in `editorial_reports/2026-07-31/` were written against the book at
commit `625aaab`. Seven chapters have changed since: ch1 gained Carse, ch3 gained five
Examples and lost two book-awareness breaches, ch4 ch6 ch7 ch8 and ch9 had Examples
replaced or written, ch5 gained a register and five Examples it never had, and ch8's three
attributions moved below the seam.

**A finding whose evidence has moved is not a finding.** This checks every quoted piece of
evidence against the current files and sorts the findings three ways:

  LIVE     the evidence is still on the page. Act on it.
  GONE     the evidence is not. Either the edit fixed it or the prose moved underneath it,
           and only a reader can say which, so these are listed for adjudication rather
           than closed.
  PARTIAL  a finding quoting several pieces, some present and some not.

It does **not** re-run the editorial judgment. It says which findings are still about
something that exists, which is the cheap half, and leaves the expensive half to a reader.

    python3 instruments/rescan.py            # the summary
    python3 instruments/rescan.py --gone     # every GONE finding, with its dead quotes
"""
import io, os, re, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)
REPORTS = os.path.join(ROOT, "editorial_reports", "2026-07-31")

# Evidence is quoted between typographic or straight double quotes, after an Evidence label.
QUOTE = re.compile(r"[“\"]([^”\"\n]{25,})[”\"]")


def corpus():
    out = {}
    for pat in ("manuscript/*.md", "appendices/*.md", "front_matter/*.md",
                "back_matter/*.md", "marginalia/insertions.py"):
        for p in glob.glob(os.path.join(ROOT, pat)):
            out[os.path.basename(p)] = io.open(p, encoding="utf-8").read()
    out["__ALL__"] = "\n".join(out.values())
    return out


def findings(path):
    """Split a report into (id, title, evidence-quotes)."""
    text = io.open(path, encoding="utf-8").read()
    out = []
    # Three heading shapes across the eleven reports, found by the first run reporting
    # CH8 and ARCHITECT as empty when neither is: "### [S1] title" in most chapters,
    # "### [ST-1] title" in CH8, and "## A1 · title" in the whole-book Architect pass.
    pat = (r"^#{2,3} \[([A-Z]+-?\d+)\]\s*(.+?)$"
           r"|^## (A\d+) · (.+?)$")
    for m in re.finditer(pat, text, re.M):
        fid = m.group(1) or m.group(3)
        title = m.group(2) or m.group(4)
        start = m.end()
        nxt = re.search(pat, text[start:], re.M)
        body = text[start:start + nxt.start()] if nxt else text[start:]
        ev = ""
        em = re.search(r"\*\*Evidence:?\*\*:?(.*?)(?=\n- \*\*|\Z)", body, re.S)
        ev = em.group(1) if em else body
        out.append((fid, title.strip(), QUOTE.findall(ev)))
    return out


def norm(s):
    """Compare on words, not on markup.

    The reports bold the salient span INSIDE a quotation, so the quoted string is not
    verbatim: `the player at its center is **you**` never appears in the manuscript with
    those asterisks. The first run of this file counted forty-three findings as needing
    adjudication and a large share of them were this. Emphasis, smart quotes and en-dash
    variants are all stripped before matching."""
    s = s.replace("**", "").replace("*", "").replace("`", "")
    s = s.replace("\u2019", "'").replace("\u2018", "'")
    s = s.replace("\u201c", '"').replace("\u201d", '"')
    return " ".join(s.split())


def main():
    show_gone = "--gone" in sys.argv
    C = corpus()
    rows, tot = [], {"LIVE": 0, "GONE": 0, "PARTIAL": 0, "NOQUOTE": 0}
    detail = []

    for path in sorted(glob.glob(os.path.join(REPORTS, "*.md"))):
        name = os.path.basename(path)
        live = gone = partial = noq = 0
        for fid, title, quotes in findings(path):
            if not quotes:
                noq += 1
                continue
            hits = [q for q in quotes if norm(q)[:60] in norm(C["__ALL__"])]
            if len(hits) == len(quotes):
                live += 1
            elif hits:
                partial += 1
            else:
                gone += 1
                detail.append((name, fid, title, quotes))
        rows.append((name, live, partial, gone, noq))
        tot["LIVE"] += live; tot["GONE"] += gone
        tot["PARTIAL"] += partial; tot["NOQUOTE"] += noq

    print("%-28s %6s %8s %6s %8s" % ("report", "LIVE", "PARTIAL", "GONE", "no quote"))
    print("-" * 62)
    for r in rows:
        print("%-28s %6d %8d %6d %8d" % r)
    print("-" * 62)
    print("%-28s %6d %8d %6d %8d" % ("TOTAL", tot["LIVE"], tot["PARTIAL"],
                                     tot["GONE"], tot["NOQUOTE"]))
    n = sum(tot.values())
    print("\n%d findings. %d still quote text that is on the page." % (n, tot["LIVE"]))
    print("%d do not and need a reader to say whether the edit fixed them "
          "or the prose moved." % (tot["GONE"] + tot["PARTIAL"]))

    if show_gone:
        print("\n" + "=" * 62 + "\nGONE — evidence no longer in any shipping file\n" + "=" * 62)
        for name, fid, title, quotes in detail:
            print("\n%s [%s] %s" % (name, fid, title[:74]))
            for q in quotes[:2]:
                print("    dead: %s" % norm(q)[:96])
    return 0


if __name__ == "__main__":
    sys.exit(main())
