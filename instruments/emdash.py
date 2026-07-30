# -*- coding: utf-8 -*-
"""
Em-dash counter, prose only, per chapter — the instrument for SPEC_EMDASH_AND_DENSITY.

Prose only matters. Three earlier counts (1,290 / 1,274 / 1,122) were each wrong
by a different amount because they swept in things that are not sentences: the
ASCII axis diagrams (←——●——→), the BAR-grid table rows, fenced blocks, and list
bullets that open with a dash. Headings are excluded too — `# Chapter 1 — The
Infinite Arcade` is title typography and the ruling does not reach it.

    python3 instruments/emdash.py         # per chapter against the budget
    python3 instruments/emdash.py -v      # quote every dash with its shape
    python3 instruments/emdash.py --json  # for the ratchet in gate.py
"""
import re, io, os, sys, glob, json

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")
BUDGET = os.path.join(HERE, "emdash_budget.json")

BLOCK = re.compile(r"<!-- (MARGINALIA|EPIGRAPH-BYLINE|POSTCARD) -->\n(.*?)\n<!-- /\1 -->", re.S)
FENCE = re.compile(r"```.*?```", re.S)
# Bold structural labels are headings too. `**[TRANSLATE] Translate 1 — Anxiety
# → Interest**` is a section title with a subtitle, not a sentence, and the dash
# in it is typography. ch7 alone carries 13.
HEADING = re.compile(r"^#{1,6}\s"
                     r"|^\*\*?[A-Z][^*]{0,60}\*\*?$"
                     r"|^\*\*\[[A-Z /\u2192]+\][^*]{0,80}\*\*$")


def prose_lines(text):
    """Yield (lineno, line) for lines that are prose: no tables, diagrams,
    bullets-opening-with-a-dash, fences, or headings."""
    text = FENCE.sub(lambda m: "\n" * m.group(0).count("\n"), BLOCK.sub("", text))
    for i, line in enumerate(text.split("\n"), 1):
        s = line.strip()
        if not s or s.startswith("|") or s.startswith("—"):
            continue
        # The bullet is the reliable axis-diagram marker. Keying on the arrows
        # instead was a false negative worth 70 prose em-dashes: this book uses
        # "→" constantly in ordinary sentences (Fire/Anger → Triumph, Obedience →
        # True Allegiance), and every one of those lines was being skipped. Only
        # four lines in the manuscript are real diagrams, and all four have "●".
        if "●" in s:
            continue
        if HEADING.match(s):
            continue
        yield i, line


def shape(line, pos):
    """Name the decision the dash avoided, so the fix is not freehand."""
    right = line[pos + 1:pos + 90]
    left = line[max(0, pos - 90):pos]
    if "—" in left:
        return "closes a parenthetical pair"
    if re.search(r"—[^—]{1,70}—", line[pos:pos + 90]):
        return "opens a parenthetical pair"
    if re.match(r"\s*\*", right):
        return "introduces an italic quote -> colon"
    if re.match(r"\s*[a-z]", right):
        return "single tail, lowercase -> comma or colon"
    return "single tail -> comma or full stop"


def scan():
    out = {}
    for f in sorted(glob.glob(os.path.join(MS, "ch*.md")),
                    key=lambda p: int(re.search(r"ch(\d+)", os.path.basename(p)).group(1))):
        hits, words = [], 0
        for ln, line in prose_lines(io.open(f, encoding="utf-8").read()):
            words += len(line.split())
            for m in re.finditer("—", line):
                hits.append((ln, shape(line, m.start()), line.strip()))
        out[os.path.basename(f)] = {"count": len(hits), "words": words, "hits": hits}
    return out


def load_budget():
    if os.path.exists(BUDGET):
        return json.load(io.open(BUDGET, encoding="utf-8"))
    return {}


def main():
    res = scan()
    if "--json" in sys.argv:
        print(json.dumps({k: v["count"] for k, v in res.items()}))
        return 0

    budget = load_budget()
    print("%-10s %8s %8s %9s %8s" % ("file", "dashes", "/1k", "budget", "status"))
    print("-" * 48)
    total = over = 0
    for name, d in res.items():
        rate = d["count"] / d["words"] * 1000 if d["words"] else 0
        cap = budget.get(name)
        if cap is None:
            status = "unset"
        elif d["count"] > cap:
            status = "OVER +%d" % (d["count"] - cap); over += 1
        elif d["count"] < cap:
            status = "-%d ratchet" % (cap - d["count"])
        else:
            status = "at cap"
        print("%-10s %8d %8.1f %9s %8s"
              % (name, d["count"], rate, "—" if cap is None else cap, status))
        total += d["count"]
    print("-" * 48)
    print("%-10s %8d" % ("TOTAL", total))

    if "-v" in sys.argv:
        for name, d in res.items():
            for ln, sh, line in d["hits"]:
                print("\n%s:%d  [%s]\n    %s" % (name, ln, sh, line[:200]))

    if over:
        print("\nBUDGET EXCEEDED in %d chapter(s). The budget only ratchets down;"
              "\nraising it is Wendell's call and nobody else's — see"
              "\nspecs/SPEC_EMDASH_AND_DENSITY_2026-07-29.md §3." % over)
        return 1
    print("\nwithin budget" if budget else "\nno budget set — run --set to record the current count as the cap")
    return 0


if __name__ == "__main__":
    if "--set" in sys.argv:
        cur = {k: v["count"] for k, v in scan().items()}
        old = load_budget()
        raised = {k: (old[k], v) for k, v in cur.items() if k in old and v > old[k]}
        if raised:
            print("REFUSED — the budget only ratchets down. These would rise:")
            for k, (o, n) in raised.items():
                print("  %s %d -> %d" % (k, o, n))
            sys.exit(1)
        json.dump(cur, io.open(BUDGET, "w", encoding="utf-8"), indent=1, sort_keys=True)
        print("budget set: %s" % cur)
        sys.exit(0)
    sys.exit(main())
