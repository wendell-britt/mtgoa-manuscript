# -*- coding: utf-8 -*-
"""
The W9 ruler — em-dash, copula/1k and the <=6-word share, taken together.

SPEC_EMDASH_AND_DENSITY 1.4: *"Every batch reports em-dash count, copula/1k, and
<=6-word share together, or it is reporting a win it did not get."* The trap is
specific and it has fired before: converting dashes to full stops buys a lower
em-dash count with a higher short-sentence share, which is the register defect
this book already has. One number moving is not evidence.

1.4a also fixes the splitter, because the figures scattered across the specs were
each taken with a different one and are not comparable:

    re.split(r'(?<=[.!?])\\s+', text)   on marginalia-stripped body

That splitter is used here verbatim, so these numbers sit in 1.4a's table. It is
cruder than `stylo.py`'s -- it splits on abbreviations -- and that does not matter
as long as nothing mixes the two.

    python3 instruments/w9_ruler.py                 # per chapter and book
    python3 instruments/w9_ruler.py --save NAME     # record a baseline
    python3 instruments/w9_ruler.py --against NAME  # measure the delta
"""
import io, os, re, sys, json, glob

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)
MS = os.path.join(ROOT, "manuscript")
STORE = os.path.join(HERE, "w9_baselines.json")

sys.path.insert(0, HERE)
import emdash  # the prose-only definition, so both instruments agree on what prose is

COP = re.compile(r"\b(is|are|was|were|am|be|been|being)\b", re.I)
SPLIT = re.compile(r"(?<=[.!?])\s+")


def measure(text):
    """text is already marginalia-stripped prose lines, joined."""
    words = text.split()
    n = len(words)
    sents = [s for s in SPLIT.split(text) if s.strip()]
    ns = len(sents)
    short = sum(1 for s in sents if len(s.split()) <= 6)
    return {
        "words": n,
        "sents": ns,
        "emdash": text.count("—"),
        "copula": 1000.0 * len(COP.findall(text)) / n if n else 0.0,
        "short": 100.0 * short / ns if ns else 0.0,
        # 1.4 names the full stop as the trap door. There is a second one. A dash
        # whose tail names what came before converts to a colon, and doing that
        # 600 times would trade a dash habit for a colon habit -- the same defect
        # wearing different punctuation. SPEC_REPETITION already measures this
        # book at 10.7 colons per 1k against 2.9 for the control text, so it is
        # the counter most likely to absorb the sweep without anyone noticing.
        "colon": 1000.0 * text.count(":") / n if n else 0.0,
    }


def prose(path):
    t = io.open(path, encoding="utf-8").read()
    return "\n".join(line for _, line in emdash.prose_lines(t))


def scan():
    out = {}
    for p in sorted(glob.glob(os.path.join(MS, "ch*.md")),
                    key=lambda q: int(re.search(r"ch(\d+)", os.path.basename(q)).group(1))):
        out[os.path.basename(p)] = measure(prose(p))
    joined = "\n".join(prose(p) for p in sorted(
        glob.glob(os.path.join(MS, "ch*.md")),
        key=lambda q: int(re.search(r"ch(\d+)", os.path.basename(q)).group(1))))
    out["BOOK"] = measure(joined)
    return out


def load():
    return json.load(io.open(STORE, encoding="utf-8")) if os.path.exists(STORE) else {}


def row(name, d, base=None):
    if base is None:
        return "%-8s %8d %8.1f %8.1f %8.1f%% %9d" % (
            name, d["emdash"], d["copula"], d["colon"], d["short"], d["words"])
    return "%-8s %5d %+5d %6.1f %+5.1f %6.1f %+5.1f %6.1f%% %+5.1f" % (
        name, d["emdash"], d["emdash"] - base["emdash"],
        d["copula"], d["copula"] - base["copula"],
        d.get("colon", 0), d.get("colon", 0) - base.get("colon", 0),
        d["short"], d["short"] - base["short"])


def main():
    cur = scan()

    if "--save" in sys.argv:
        tag = sys.argv[sys.argv.index("--save") + 1]
        store = load()
        store[tag] = cur
        json.dump(store, io.open(STORE, "w", encoding="utf-8"), indent=1, sort_keys=True)
        print("saved baseline %r" % tag)
        return 0

    if "--against" in sys.argv:
        tag = sys.argv[sys.argv.index("--against") + 1]
        base = load().get(tag)
        if not base:
            print("no baseline %r — have: %s" % (tag, ", ".join(sorted(load()))))
            return 1
        print("against baseline %r\n" % tag)
        print("%-8s %5s %5s %6s %5s %6s %5s %7s %5s"
              % ("file", "em—", "d", "cop/1k", "d", "col/1k", "d", "<=6w", "d"))
        print("-" * 66)
        for k in cur:
            if k == "BOOK":
                print("-" * 66)
            print(row(k, cur[k], base.get(k, cur[k])))
        # The trap, checked rather than trusted.
        b, c = base["BOOK"], cur["BOOK"]
        print()
        if c["emdash"] < b["emdash"] and c["short"] > b["short"] + 0.5:
            print("LOOK — em-dashes fell %d but the <=6-word share rose %+.1f points."
                  "\nThat is 1.4's trap: the dashes became full stops. Convert to comma"
                  "\nor colon where the tail is not an independent clause."
                  % (b["emdash"] - c["emdash"], c["short"] - b["short"]))
        elif c["emdash"] < b["emdash"]:
            print("em-dashes %d -> %d, <=6-word share %+.1f, copula %+.1f/1k, "
                  "colon %+.1f/1k."
                  % (b["emdash"], c["emdash"], c["short"] - b["short"],
                     c["copula"] - b["copula"],
                     c.get("colon", 0) - b.get("colon", 0)))
            if c.get("colon", 0) > b.get("colon", 0) + 1.0:
                print("LOOK — colons rose %+.1f/1k. The dashes became colons, which is"
                      "\n1.4's trap through the other door." 
                      % (c.get("colon", 0) - b.get("colon", 0)))
        return 0

    print("%-8s %8s %8s %8s %9s %9s"
          % ("file", "em—", "cop/1k", "col/1k", "<=6w", "words"))
    print("-" * 56)
    for k in cur:
        if k == "BOOK":
            print("-" * 56)
        print(row(k, cur[k]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
