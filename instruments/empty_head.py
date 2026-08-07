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

Reports; does not block.

    first run  2026-08-03      HARD 266  (89 aggravated)  SOFT 288  2.44 /1k
    after the `thing` sweep    HARD 136  (28 aggravated)  SOFT 291  1.25 /1k
    after the tier-1 sweep     HARD  16  ( 5 aggravated)  SOFT 291  0.15 /1k

`thing` is done book-wide: 405 body instances to 31, and the 31 are the three carve-outs
below plus five odds. **HARD is now the rest of tier 1** — `part`, `piece`, `stuff`,
`aspect`, `element`, `factor`, `area`, `matter` — which nobody has swept yet and which is
the obvious next pass.

The first run reported a 3.8× spread across chapters, ch5 at 4.51 against ch7 at 1.19, and
argued from it that this was a defect rather than a voice. The sweep confirmed it: nothing
was lost anywhere, and fourteen sampled sites tested one at a time all improved.

**Promotion path.** `\bthings?\b` into `gate.py`'s banned pattern, with the three CANON
carve-outs. Not done here, because the 26 marginalia sites and the five odds are unruled.

    python3 instruments/empty_head.py                 # per file, both tiers
    python3 instruments/empty_head.py --sites         # every site with context
    python3 instruments/empty_head.py --strict        # exit 1 if any HARD site remains
    python3 instruments/empty_head.py --diff [REV]    # what a change set ADDED vs REMOVED

**Run `--diff` after every repair pass.** It is the only mode that answers the question
that produced this file, and it exits 1 when a pass is net-positive on either tier.
"""
import io, os, re, sys, glob

DET = r"(?:the|this|that|these|those)"

# Tier 1 — the head contributes no content IN THIS BOOK. Wendell 2026-08-03 on `thing`:
# "because of how unspecific it is."
#
# CORRECTED 2026-08-03 after the tier-1 sweep, which found the list over-broad by 98 of
# 125. `part` and `parts` are OUT: the daemon system is parts work -- "Those parts are
# daemons", "a part of you has already felt", "the part that audits your charge", and ch8's
# section heading "The Part That Turned a Difference Into a Defect". ch5 and ch6 add a
# second contentful sense, a part of a structure: "This part is load-bearing", "whether the
# parts add up to a whole".
#
# `piece`, `pieces` and `matter` are OUT for the same reason, in fixed compounds where the
# head works: a piece of evidence, a piece of feedback, moving a piece on the board,
# allyship is a matter of following the right people, any say in the matter.
#
# THE LESSON, and it is the same one `field` and `charge` taught from the other direction:
# a head noun is empty only in a particular book. `thing` was empty everywhere here. `part`
# is a term of art here. A generic list cannot know that, so this one is now a list of
# words THIS MANUSCRIPT has no use for.
HARD = r"(?:thing|things|stuff|bit|bits|aspect|aspects|" \
       r"element|elements|factor|factors|area|areas)"

# Tier 2 — the fillers a repair pass reaches for. **MEANINGFUL ONLY IN --diff MODE.**
#
# Membership is unchanged and the SCOPE is what was wrong. Measured book-wide, these 283
# sites are almost all legitimate:
#
#   move 107   game canon — the five moves, the Control move, the Translate move
#   work 103   the book's own subject: "the work in this book", "you did the work"
#   situation 45   contentful, and "**The Situation:**" is a card heading format
#   process / others / idea 28   mostly quoted speech or a real antecedent
#
# So the book-wide SOFT number never meant anything. The diff number does, and the two
# answer different questions. `the work` is canon in the manuscript and suspicious in a
# line I added ten minutes ago, which is exactly Wendell's complaint: "our passes are
# creating them faster than we can get rid of them." A book-wide count cannot see that,
# because the book is allowed to say `the work` and I am not, mid-repair, without checking.
#
# Measured on this session's own diff, 445 lines added and 429 removed:
#
#   HARD   added 5   removed 135   net -130     <- the sweep worked
#   SOFT   added 66  removed  63   net   +3     <- neutral, not a leak
#
# The +3 is the finding. The passes are NOT generating tier-2 filler at a rate worth a
# book-wide watch list, and the instrument was reporting 283 legitimate sites as if they
# were a backlog.
SOFT = r"(?:work|move|moves|situation|process|others|idea|ideas)"

# A restrictive clause after an empty head is aggravating, not exculpating: it proves the
# clause is carrying what the noun would not.
CLAUSE = r"(?:\s+(?:that|which|who|whom|you|he|she|they|I|we|it)\b)"

# Canon. `Say the Thing Under the Thing` is a named move — ch3 Move 5, and ch4's variant.
CANON = [
    # Ruled by Wendell 2026-08-03, option b: move and card names survive the sweep.
    re.compile(r"Say the Thing(?: Under the Thing)?"),
    re.compile(r"Run It Again With One Thing Changed", re.I),
    # Ruled 2026-08-03: "keep the right thing the easy thing." The Architect's thesis --
    # ch6's subtitle, quoted three times inside ch6, once from ch5's closing handoff and
    # twice in ch9. Twelve instances across three chapters, so a thesis, not a heading.
    re.compile(r"(?:right|easy) thing", re.I),
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


def diff_mode(rev):
    """Score added lines against removed lines. This is where SOFT means something."""
    import subprocess
    out = subprocess.run(["git", "diff", rev, "--", "manuscript/"],
                         stdout=subprocess.PIPE).stdout.decode("utf-8", "replace")
    add = [l[1:] for l in out.split("\n") if l.startswith("+") and not l.startswith("+++")]
    rem = [l[1:] for l in out.split("\n") if l.startswith("-") and not l.startswith("---")]
    print("empty heads in a change set — %s" % rev)
    print("%-6s %8s %8s %7s" % ("", "added", "removed", "net"))
    worst = 0
    for name, heads in (("HARD", HARD), ("SOFT", SOFT)):
        pat = re.compile(r"\b(?:%s|a|an)\s+%s\b" % (DET, heads), re.I)
        a_ = sum(len(pat.findall(l)) for l in add)
        r_ = sum(len(pat.findall(l)) for l in rem)
        print("%-6s %8d %8d %+7d" % (name, a_, r_, a_ - r_))
        worst = max(worst, a_ - r_)
    print("\n%d line(s) added, %d removed" % (len(add), len(rem)))
    print("a positive net means the pass put in more placeholders than it took out")
    return 1 if worst > 0 else 0


def main():
    show = "--sites" in sys.argv
    strict = "--strict" in sys.argv
    if "--diff" in sys.argv:
        i = sys.argv.index("--diff")
        rev = sys.argv[i + 1] if len(sys.argv) > i + 1 else "origin/master...HEAD"
        return diff_mode(rev)
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
