# -*- coding: utf-8 -*-
"""empty_head.py — the definite article pointing at nothing.

Ruled by Wendell 2026-08-03: *"we've got to solve this definite article issue once and for
all. It's the new AI slop issue that our passes are creating faster than we can get rid of
them."* Then, narrowing it: *"'empty head noun' is what I'm looking for. But I do want to
push it further. It's not in my writing style to use the word 'thing' because of how
unspecific it is."*

## What the defect is

`the X` is a presupposition. It tells the reader *you already know which one I mean.*
That is legal four ways: an antecedent, a referent unique in the world, a clause that
supplies it on the spot, or canon the book has taught her. When none holds, the grammar
asserts shared knowledge that was never established — the same lie as *"you know the
loop,"* which Wendell killed on 2026-08-02, wearing a determiner instead of a verb.

**The article is the symptom. The empty head noun is the disease.** `the field`, `the
charge`, `the table` are contentful heads: the noun names something and the reader can
picture it. `the thing`, `the part`, `the piece` are placeholders — the modifier after
them does 100% of the work, which is the definition of a head noun contributing nothing.
Same article, different defect.

## Why an instrument and not another sweep

`marginalia/review.py` already carries a `say the noun` check, and it caught **4 of the
106** `the thing` sites in the manuscript. Two reasons, both structural:

1. **It is a hand-maintained list of ten literal strings.** Every repair pass invents a
   *new* vague phrase, and a blocklist only knows the phrases somebody already thought of.
   R-B produced `the people it concerns`, `the work`, `everybody involved` and `both camps`
   in a single 23-edit pass — none on the list, none seen.
2. **Its comment documents an exemption for the exact construction Wendell has now banned
   twice**: *"'the thing that gets done' is fine; 'the thing.' is not."* That is why
   `\bthe thing\b\s*[.,;]` catches 4 and misses 76.

So this tests the condition instead of enumerating strings, and it catches the phrase
nobody has written yet.

## Why the repair passes manufacture these

Worth stating, because it is the mechanism behind Wendell's *"faster than we can get rid of
them."* Every agency repair evicts an abstraction from a subject slot and has to put
something back. The cheapest legal filler is a definite noun phrase with a human-shaped
head and no antecedent. The R-ops have a systematic byproduct and no instrument saw it.

## Ranking

`the thing THAT…` ranks above `the thing.` — the opposite of the old check. A restrictive
clause is not a rescue; it is proof the head is a placeholder, because the clause is
carrying the meaning the noun refused to.

## Status

Reports; does not block. **266 hard sites and 288 soft** are standing in the manuscript
today, and gating on them would fail every review until the sweep lands. Promote to
`gate.py`'s banned pattern after the sweep — the carve-out is `Say the Thing Under the
Thing`, a named move in ch3 and ch4.

First run, HARD per 1,000 words: ch5 **4.51**, ch9 2.84, ch3 2.75 · ch7 **1.19**, ch8 1.96.
A 3.8× spread across chapters of one book is the argument that this is a defect rather
than a voice: ch7 already reads at a rate the rest of the book does not, without anybody
having tried.

    python3 instruments/empty_head.py                 # per file, both tiers
    python3 instruments/empty_head.py --sites         # every site with context
    python3 instruments/empty_head.py --strict        # exit 1 if any HARD site remains
"""
import io, os, re, sys, glob

DET = r"(?:the|this|that|these|those)"

# Tier 1 — the head contributes no content in any context. Wendell 2026-08-03 on `thing`:
# "because of how unspecific it is."
HARD = r"(?:thing|things|stuff|part|parts|piece|pieces|bit|bits|aspect|aspects|" \
       r"element|elements|factor|factors|area|areas|matter)"

# Tier 2 — the fillers the repair passes themselves produce. Scoped deliberately narrow.
#
# The first cut of this list included `one`, `way`, `people`, `place` and `point` and
# returned 790 sites, which is a number nobody acts on. Those words are usually doing real
# work in this book — *the way you show up*, *the people at the table* — and a watch list
# that flags them is a watch list that gets ignored.
#
# What is left is the set an agency repair reaches for when it evicts an abstraction from
# a subject slot and needs a human-shaped noun to put back. That is the complaint Wendell
# actually made: our passes create these faster than we remove them.
SOFT = r"(?:work|move|moves|situation|process|others|idea|ideas)"

# A restrictive clause after an empty head is aggravating, not exculpating: it proves the
# clause is carrying what the noun would not.
CLAUSE = r"(?:\s+(?:that|which|who|whom|you|he|she|they|I|we|it)\b)"

# Canon. `Say the Thing Under the Thing` is a named move — ch3 Move 5, and ch4's variant.
CANON = [
    re.compile(r"Say the Thing(?: Under the Thing)?"),
]

# Marginalia are a different voice and out of scope, same convention as gate.py.
MARG = re.compile(r"^(>|\s*<!--)", re.M)


def canon_spans(text):
    out = []
    for c in CANON:
        out += [(m.start(), m.end()) for m in c.finditer(text)]
    return out


def sites(text):
    """Return (tier, aggravated, matched_text, context) for every empty-head site."""
    skip = canon_spans(text)
    found = []
    for tier, heads in (("HARD", HARD), ("SOFT", SOFT)):
        pat = re.compile(r"\b(?:%s|a|an)\s+%s\b(%s?)" % (DET, heads, CLAUSE), re.I)
        for m in pat.finditer(text):
            if any(m.start() < b and m.end() > a for a, b in skip):
                continue
            ctx = text[max(0, m.start() - 44):m.end() + 34].replace("\n", " ").strip()
            found.append((tier, bool(m.group(1).strip()), m.group(0), ctx))
    return found


def main():
    show = "--sites" in sys.argv
    strict = "--strict" in sys.argv
    paths = [a for a in sys.argv[1:] if not a.startswith("--")] or \
        sorted(glob.glob("manuscript/ch?.md"))

    print("empty head nouns — a determiner pointing at a noun that carries no content")
    print("%-12s %7s %7s %7s %7s" % ("file", "HARD", "+clause", "SOFT", "/1k"))
    th = ta = ts = tw = 0
    for p in paths:
        text = MARG.sub("", io.open(p, encoding="utf-8").read())
        w = len(text.split())
        s = sites(text)
        h = [x for x in s if x[0] == "HARD"]
        agg = [x for x in h if x[1]]
        soft = [x for x in s if x[0] == "SOFT"]
        th += len(h); ta += len(agg); ts += len(soft); tw += w
        print("%-12s %7d %7d %7d %7.2f" % (os.path.basename(p), len(h), len(agg),
                                           len(soft), len(h) * 1000.0 / w if w else 0))
        if show:
            for tier, a, mt, ctx in sorted(s, key=lambda x: (x[0], not x[1])):
                print("      %-4s%s %s" % (tier, "!" if a else " ", ctx[:104]))
    print("%-12s %7d %7d %7d %7.2f" % ("TOTAL", th, ta, ts,
                                       th * 1000.0 / tw if tw else 0))

    if strict and th:
        print("\nSTRICT: %d hard site(s) remain" % th)
        return 1
    print("\nreporting only — promote to gate.py after the sweep")
    return 0


if __name__ == "__main__":
    sys.exit(main())
