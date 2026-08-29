# -*- coding: utf-8 -*-
"""
Fragments carrying claims, and fragments outside landing position.

    python3 instruments/fragment.py                  # the board
    python3 instruments/fragment.py -v               # every site
    python3 instruments/fragment.py --write FILE     # the full report
    python3 instruments/fragment.py DRAFT.md [...]   # draft mode, one row per file
    python3 instruments/fragment.py --deep           # the book, with the second tier on

## Draft mode, added 2026-08-29

Wendell, on marketing copy that had gone through the whole pass and come back `clean`:
*"fragments are bad. I speak in complete sentences."* — **and then, on being shown that
this file exists and says in its own docstring that he has caught the defect by eye
twice:** *"how are our skills not catching this?"*

The answer was that it could not read a draft. It had no FILE branch, so every argument
was ignored and it scanned the printed book instead, which is the one place the prose had
already landed. See `specs/GAP_DRAFT_REVIEW_INSTRUMENTS_2026-08-29.md`.

**The verb lexicon still comes from the corpus in draft mode, and that is not a shortcut.**
The whole design rests on aggregating 6,000 sentences to survive a tagger that is
unreliable per instance; a lexicon built from a 500-word draft would exonerate nothing and
flag ordinary prose. Corpus for the lexicon, draft for the sites.

## Why this exists

`marginalia/specs/REVISION_INSTRUMENT.md` Part 1 lists five constraints that are
"always on, never chosen". Four of them have instruments. This is the fifth:

> **Beat placement** — fragments carry beats, never claims, and only in landing
> position.

Wendell has caught it by eye twice. Batch six, on `ch1:175`: *"The being-needed.
The safety of the line you never cross. The exhaustion you wear like proof."* --
**"more of the sentence fragments and definite articles."** And 2026-08-03, on a
drafted ch1 paragraph: *"Same instrument, same three readings, a different chair.
This isn't a sentence."* Both were in prose that had passed gate, diet and the
five pattern instruments, because none of them looks for a missing verb.

## The tagger cannot do this pointwise, and that is the whole design problem

`shapes.py` already recorded why it matched surfaces instead of tags:

> *a tagger reads `The impact fades.` as verbless because it takes `fades` for a
> plural noun, so a fragment-detector built on tags reports things that are
> ordinary sentences.*

Measured here, that is not a small effect. A naive "no finite-verb tag" scan
returns **694 fragments in 6,174 sentences, 11.2%**, and the long tail is almost
all ordinary prose. On this book's own sentences the tagger gives:

    Most calls to allyship arrive ...   allyship/VB   arrive/JJ
    Vigilance runs at a higher price    runs/NNS      buys/JJ
    The impact fades.                   fades/NNS
    Find it.                            Find/IN

**So the tagger is unreliable per instance and useful in aggregate.** Across
6,000 sentences the union of every word it has ever tagged `VB*` or `MD` is a
verb vocabulary for this book, and every one of the words it mangled above
appears in it, because each is tagged correctly somewhere else. A sentence is a
fragment candidate only when **no token in it is ever a verb anywhere in the
manuscript.**

That single change takes 694 raw hits to 170. The closed-class floor below then
recovers 16 more that a poisoned lexicon had been exonerating, so the board reads
**125 candidates and 45 legal landings**. Both sentences Wendell caught by eye
are in it, and all four mangled sentences above come back clean.

## What it reports, and what it refuses to decide

**LANDING** — a fragment in the last sentence of its paragraph. The rule permits
this, so it is printed and not counted.

**MID** — a fragment anywhere else. A candidate.

**NEGATIVE OPENER** — a fragment beginning `Not ...`, printed as its own class
because it is the same defect `/no-ai-slop` bans as *negative listing* and
`shapes.BINARY` catches only in its full two-part form. **The two instruments
found this family independently, which is the strongest evidence either of them
is measuring something real.**

**Beat or claim is not decided here.** Length is printed as the only proxy and
it is a weak one: a two-word fragment is nearly always a beat and a twenty-word
fragment nearly always a claim, and the middle needs a reader. Every other
instrument in this directory ends the same way and for the same reason.

## What it skips, and why each one is a genre rather than a defect

Headings, tables, block quotes and list items. `front_matter/copyright.md` and
`back_matter/acknowledgements.md`, where a page of names and a legal notice are
fragments by construction: *Patrice Hutton and the staff of Writers In Baltimore
Schools.* is not a beat-placement error, it is a thank-you.

## One known false positive, left in rather than hidden

`ch1:60` reports as `(Yes, already.` — the sentence splitter breaks on the open
parenthesis and hands this instrument half a clause. The fix belongs in
`density.sentences()` rather than here, and suppressing it locally would hide a
splitter bug from every other instrument that shares it.
"""
import io, os, re, sys, importlib.util
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    argv, sys.argv = sys.argv, [name]
    try:
        spec.loader.exec_module(mod)
    finally:
        sys.argv = argv
    return mod


fl = _load("find_line", os.path.join(HERE, "find_line.py"))
dn = _load("density", os.path.join(HERE, "density.py"))
dl = _load("draft_lines", os.path.join(HERE, "draft_lines.py"))

# Fragments are the form these files are written in. A dedication is not a beat.
EXEMPT_SURFACE = ("copyright.md", "acknowledgements.md", "dedication.md",
                  "kickstarter_backers.md")

SKIP_LINE = ("#", "|", ">", "-", "*", "1.", "2.", "3.", "4.", "5.", "6.", "7.")

# Words that carry no verb reading anywhere and would otherwise never be learned,
# because the corpus is one book. Kept deliberately short.
EXTRA_VERBS = set("""ought shall must lest""".split())

# CLOSED CLASS — never admitted to the lexicon whatever the tagger says.
#
# Added after the first regression run failed. `Same instrument, same three
# readings, a different chair.` came back clean, and the token that cleared it was
# **`a`**: somewhere in 6,000 sentences the tagger called an article a verb, and
# one garbage entry in an aggregate lexicon silently exonerates every sentence
# containing that word. Aggregation fixes per-instance noise and amplifies
# per-instance nonsense, so the lexicon needs a floor as well as a source.
NEVER_VERB = set("""a an the of and or but nor so yet in on at for with from by as
into onto upon about after before during through under over between among against
that this these those it its itself he him his she her hers they them their theirs
we us our ours you your yours i me my mine who whom whose which what when where why
how not no never nothing nobody none very just only also too more most less least
all some any each every both either neither one two three four five six seven eight
nine ten first second third next last other another same such own here there then
than if because while although though unless until since whether
per via etc vs""".split())

NEG_OPEN = re.compile(r"^(Not|Never|Nothing|Nobody|No)\b", re.I)

# THE SECOND TIER, added 2026-08-29, because the first one does not catch the defect
# Wendell actually keeps reporting.
#
# Run against the three fragments he rejected in the KDP description on 2026-08-29 --
# *"The meeting where somebody gets talked over. The decision that lands on whoever can
# least afford it. The group chat where everybody stops typing for four hours"* -- the
# lexicon tier returned **zero**. Correctly, on its own terms: it flags a string in which
# no token is ever a verb anywhere in the book, and every one of those has a perfectly
# good verb (`gets`, `lands`, `stops`) sitting inside a relative clause.
#
# **So the shape that keeps shipping is not a verbless string. It is a noun phrase whose
# only verbs belong to something else** -- a head with no predicate, wearing a relative
# clause. That is what a definite article plus a `where`/`that` produces, and it is why
# the family reads as prose to every counter in this directory.
#
# The test: walk to the first subordinator or relative pronoun. If no finite verb has
# appeared before it, the head noun has no predicate.
FINITE = ("VBZ", "VBD", "VBP", "MD")
SUBORD = set("""who whom whose which that where when while because if unless until since
whoever whatever whichever wherever whenever
although though so as after before""".split())

# THE OPENER RESTRICTION IS WHAT MAKES THE TIER USABLE, and it was added after the first
# version reported *"Under ten percent of the people who started it finished"* -- a
# complete sentence whose main verb sits after the relative clause, so the walk hit `who`
# before reaching `finished`.
#
# Counting verbs against subordinators fixes that one and breaks a real fragment:
# *"The group chat where everybody stops typing for four hours and then carries on"* has
# two finite verbs to one subordinator, both inside the relative clause, because
# coordination is invisible to a count.
#
# **So the restriction is on the opener rather than on the arithmetic.** The defect is a
# headed noun phrase with no predicate, so the tier only looks at sentences that open on
# one. `Under ten percent…` opens on a preposition and is never considered; `The meeting
# where…`, `The decision that…`, `Six roles…` and `Thirty moves…` all are.
HEAD_OPEN = ("DT", "CD", "PRP$", "JJ", "NN", "NNS", "NNP", "NNPS")


def headless(tags):
    """True when a headed noun phrase reaches a subordinator without a finite verb."""
    if not tags:
        return False
    tok0, tag0 = tags[0][0].lower(), tags[0][1]
    if tok0 in SUBORD:
        return False                       # *"Because the meeting ran long, she left."*
    if tag0 not in HEAD_OPEN and not NEG_OPEN.match(tags[0][0]):
        return False
    reached = False
    for tok, tag in tags:
        if tag in FINITE and not reached:
            return False                   # the head has its own predicate
        if tok.lower() in SUBORD:
            reached = True
    if not reached:
        return False                       # no subordinator: the lexicon tier owns it
    # One more filter, for the shape the opener restriction lets through:
    # *"The people who started it finished."* — a headed noun phrase whose main verb sits
    # AFTER the relative clause. Each subordinator claims one finite verb; a main clause
    # needs one the subordinators have not claimed.
    nfin = sum(1 for _t, g in tags if g in FINITE)
    nsub = sum(1 for t, _g in tags if t.lower() in SUBORD)
    return nfin <= nsub


def verb_lexicon(lines, pos_tag, word_tokenize):
    """Every word this corpus ever presents as a verb. See the docstring."""
    lex = set(EXTRA_VERBS)
    for l in lines:
        for w, t in pos_tag(word_tokenize(l["text"])):
            lw = w.lower()
            if (t.startswith("VB") or t == "MD") and lw not in NEVER_VERB and lw.isalpha():
                lex.add(lw)
    return lex


def sites(text, lex, pos_tag, word_tokenize, min_words=2, deep=False):
    """Fragment candidates in one paragraph, with position and length.

    `deep` turns on the headed-noun-phrase tier. **Draft mode only by default**, and the
    reason is a measurement rather than a preference: book-wide the tier takes the board
    from 125 candidates to 296, and a board nobody reads is worse than a smaller one that
    gets worked. On a 500-word draft the asymmetry inverts — a false positive costs one
    glance and a false negative ships. `--deep` opts the book in deliberately.
    """
    out = []
    sents = dn.sentences(text)
    for i, s in enumerate(sents):
        st = s.strip()
        if len(st.split()) < min_words:
            continue
        words = word_tokenize(st)
        toks = [w.lower() for w in words]
        # Tier 1, verbless by corpus lexicon. Tier 2, a head noun with no predicate.
        # Either one makes it a candidate; neither alone was enough.
        if any(t in lex for t in toks) and not (deep and headless(pos_tag(words))):
            continue
        kind = "NEG" if NEG_OPEN.match(st) else ("LANDING" if i == len(sents) - 1 else "MID")
        out.append((kind, len(st.split()), st))
    return out


def draft(paths, lex, pos_tag, word_tokenize, verbose):
    """One row per file, then the sites. The shape `review.py` greps for a basename in."""
    print("fragments — a sentence with no verb. LANDING is legal; MID and NEG are candidates")
    print("%-22s %5s %5s %8s" % ("file", "MID", "NEG", "LANDING"))
    print("-" * 44)
    rows, bad = [], 0
    for l in dl.prose(dl.surfaces(paths)):
        for kind, n, st in sites(l["text"], lex, pos_tag, word_tokenize, deep=True):
            rows.append((l, kind, n, st))
    per = defaultdict(lambda: defaultdict(int))
    for l, kind, _n, _st in rows:
        per[os.path.basename(l["rel"])][kind] += 1
    for p in paths:
        r = per[os.path.basename(p)]
        print("%-22s %5d %5d %8d" % (os.path.basename(p)[:22], r["MID"], r["NEG"], r["LANDING"]))
        bad += r["MID"] + r["NEG"]
    hits = [r for r in rows if r[1] in ("MID", "NEG")]
    if hits:
        print("")
        for l, kind, n, st in (hits if verbose else hits[:12]):
            print("  %-7s %dw  %s:%d" % (kind, n, os.path.basename(l["rel"]), l["line"]))
            print("      > %s" % st[:120])
        if not verbose and len(hits) > 12:
            print("  … %d more, run with -v" % (len(hits) - 12))
    return 1 if bad else 0


def main():
    verbose = "-v" in sys.argv
    out = None
    if "--write" in sys.argv:
        i = sys.argv.index("--write")
        out = sys.argv[i + 1] if i + 1 < len(sys.argv) else os.path.join(
            ROOT, "editorial_reports", "FRAGMENT_BOARD.md")

    pos_tag, word_tokenize = dn.tagger()
    if pos_tag is None:
        print("Tagger unavailable — no report.")
        return 0

    lines = [l for l in fl.surfaces() if not l["text"].lstrip().startswith(SKIP_LINE)]
    lex = verb_lexicon(lines, pos_tag, word_tokenize)

    # DRAFT MODE. The lexicon above is built from the corpus whatever the mode, because
    # aggregation is what makes the tagger usable at all -- see the docstring.
    paths = dl.paths_from(sys.argv[1:])
    if paths:
        return draft(paths, lex, pos_tag, word_tokenize, verbose)

    deep = "--deep" in sys.argv
    found = defaultdict(list)
    per = defaultdict(lambda: defaultdict(int))
    for l in lines:
        if any(e in l["rel"] for e in EXEMPT_SURFACE):
            continue
        for kind, n, st in sites(l["text"], lex, pos_tag, word_tokenize, deep=deep):
            found[kind].append((l, n, st))
            per[l["rel"]][kind] += 1

    L = ["# Fragments — the board", "",
         "Generated by `instruments/fragment.py`. Body prose only.", "",
         "`REVISION_INSTRUMENT.md` Part 1: **fragments carry beats, never claims, and",
         "only in landing position.** The fifth always-on constraint, and the last one",
         "to get an instrument.", "",
         "**LANDING is legal** and is printed for completeness rather than counted.",
         "**MID** is a candidate. **NEG** is a fragment opening on a negation, which is",
         "`/no-ai-slop`'s *negative listing* found from the other direction.", "",
         "Verb lexicon: **%d words**, derived from the corpus because the tagger cannot" % len(lex),
         "be trusted on any single sentence. See the module docstring.", ""]

    L.append("## Totals")
    L.append("")
    L.append("| class | sites | rule |")
    L.append("|---|---|---|")
    for k, rule in (("MID", "candidate — a fragment outside landing position"),
                    ("NEG", "candidate — negative listing"),
                    ("LANDING", "legal — printed, not counted")):
        L.append("| **%s** | %d | %s |" % (k, len(found[k]), rule))
    L.append("")
    counted = len(found["MID"]) + len(found["NEG"])
    L.append("**%d candidate(s)** across %d component(s)." % (
        counted, len({l["rel"] for k in ("MID", "NEG") for l, _, _ in found[k]})))
    L.append("")

    L.append("## Per component")
    L.append("")
    L.append("| component | MID | NEG | LANDING |")
    L.append("|---|---|---|---|")
    for rel in sorted(per):
        r = per[rel]
        if not (r["MID"] or r["NEG"]):
            continue
        L.append("| `%s` | %d | %d | %d |" % (rel, r["MID"], r["NEG"], r["LANDING"]))
    L.append("")

    for k, title in (("NEG", "Negative openers"), ("MID", "Outside landing position"),
                     ("LANDING", "Landing position — legal")):
        L.append("## %s — %d" % (title, len(found[k])))
        L.append("")
        rows = sorted(found[k], key=lambda r: -r[1])
        for l, n, st in (rows if verbose else rows[:20]):
            L.append("- **%dw** · `%s:%s`" % (n, l["rel"], l["line"]))
            L.append("  > %s" % st[:150])
        if not verbose and len(rows) > 20:
            L.append("")
            L.append("*%d more. Run with `-v`.*" % (len(rows) - 20))
        L.append("")

    text = "\n".join(L)
    if out:
        io.open(out, "w", encoding="utf-8").write(text + "\n")
        print("wrote %s" % out)
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
