# -*- coding: utf-8 -*-
"""
light_verb.py — the weak verb: a nothing-verb faking the work a real one should do.

    python3 instruments/light_verb.py DRAFT.md [...]   # draft mode, one row per file
    python3 instruments/light_verb.py                  # the book, as the baseline
    python3 instruments/light_verb.py -v               # every site

## Why this exists

Wendell, reading the proof, 2026-09-02, on *"praise lands warm"* and *"it leaves you smaller"*:
*"'lands warm' — what the fuck does landing warm mean? Land is another one of those nothing
words that gets overused."* And, on *"it leaves you smaller"*: *"who is the it that makes you
smaller and how can they leave you?"*

**Two verbs, one failure: the verb does no work, and the sentence pretends it does.** *Land*
and *leave* and *make* borrow the look of a physical action and spend it on an abstraction that
cannot perform one. The red-team (`specs/REDTEAM_WRITE_WITHOUT_THESE_ISSUES_2026-09-02.md`)
named this the one buildable half of the solve: **catch the enumerable weak-verb class
mechanically, before the draft reaches him.** This is that half.

## The two shapes, and why they are different

**DELEXICAL — the buried verb.** *make a decision* (decide), *reach a conclusion* (conclude),
*conduct an investigation* (investigate), *provide assistance* (help). A light verb — *make,
take, give, have, do, get, provide, perform, conduct, reach* — plus a nominalization that hides
the real verb inside a noun. Strunk Rule 13 (*omit needless words*) and Williams (*Style*: put
the action in the verb, not the noun) both name it. **This tier is gradeable and driven down**:
the fix is mechanical — recover the buried verb, drop the noun.

**DEAD — the fake-concrete verb.** *praise lands warm*, *the shame sits there*, *it leaves you
smaller*. A motion or placement verb — *land, leave, sit, hang, settle, run, move* — handed an
abstract or a bare-demonstrative subject that cannot move or be placed. On a concrete subject
the same verb is fine (*she left the room*), so **this tier is surfaced, not graded**: whether
the subject can really do the verb is a reading call, not the instrument's. It is the shape
Wendell caught by eye that no counter saw.

## The remediation (Williams, and Wendell)

**Recover the action.** *make a decision* → *decide*. Not a better noun; the verb.
**Give the verb a subject that can do it.** *it leaves you smaller* → name who, and let them do
something a person can do: *when you take the grade, their read of your work outranks your own*.
The dead verb is the same tell as the copula-label in `telling.py`: **a symptom that the thought
under it is unfinished.** The writer reached for *lands* because the real verb was not worked out.

## What it cannot decide (the honest ceiling)

**This is an existence check on a word list — the same instrument every prose linter in the wild
is** (write-good, proselint, Vale). Their shared lesson is the ceiling: write-good ships its
ban-all-*to-be* mode (E-Prime) OPT-IN because banning a verb class produces false positives, and
proselint's own authors conclude every such tool is incomplete. So this reports a rate against
the book's own baseline, not zero — a light verb on a concrete object is often exactly right
(*take the medication*, *give the book*), and the DELEXICAL match cannot always tell the
delexical *take action* from the literal *take the road*. **It surfaces candidates. The reader
clears the earned ones**, exactly as with `telling.py`, and the irreducible class — a strong verb
with no real referent — stays his eye's, per the red-team.
"""
import io, os, re, sys, importlib.util

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
dl = _load("draft_lines", os.path.join(HERE, "draft_lines.py"))

SENT = re.compile(r"(?<=[.!?])\s+")

# DELEXICAL: a light verb + an optional article + a nominalization that hides the real verb.
# The light-verb list is the linguistics core (do, make, take, give, have, get) plus the Latinate
# performers editors flag most (provide, perform, conduct, achieve, reach, offer, gain). The
# nominalization is caught by suffix -- high-precision, and it deliberately misses the bare
# deverbal noun (take a look, give a push), which needs a hand-built list this does not keep.
LIGHT = (r"make|makes|made|making|take|takes|took|taken|taking|give|gives|gave|given|giving|"
         r"have|has|had|having|do|does|did|doing|get|gets|got|gotten|getting|"
         r"provide|provides|provided|providing|perform|performs|performed|performing|"
         r"conduct|conducts|conducted|conducting|achieve|achieves|achieved|achieving|"
         r"reach|reaches|reached|reaching|offer|offers|offered|offering|gain|gains|gained|gaining")
NOMINAL = r"\w{3,}(?:tion|sion|ment|ance|ence|ity|ism)"
DELEXICAL = re.compile(r"\b(?:%s)\s+(?:a |an |the )?(%s)\b" % (LIGHT, NOMINAL), re.I)

# The bare-noun light-verb construction the suffix regex cannot see: "make an effort" (try),
# "take advantage of" (exploit), "do harm to" (harm). These are the class Wendell meant by
# "someone has made a list of these" -- and someone has: this set is drawn from write-good's
# `too-wordy` list (read from the npm package, verified against source, not a summary), which
# ships "make an effort", "do damage to", "do harm to", "have a tendency to", "took advantage
# of" as wordiness, plus the canonical delexical constructions the British Council teaches.
LIGHT_PHRASE = re.compile(
    r"\b(?:mak(?:e|es|ing)|made)\s+(?:a |an |the )?"
    r"(?:effort|choice|attempt|difference|comparison|distinction|assumption|mention|use of)\b"
    r"|\b(?:tak(?:e|es|ing)|took|taken)\s+(?:a |an |the )?"
    r"(?:action|step|advantage of|account of|control of)\b"
    r"|\b(?:giv(?:e|es|ing)|gave|given)\s+(?:a |an |the )?"
    r"(?:consideration|explanation|description|demonstration|rise to|permission)\b"
    r"|\b(?:hav(?:e|es|ing)|has|had)\s+(?:a |an |the )?"
    r"(?:tendency to|impact on|preference for)\b"
    r"|\b(?:do|does|doing|did|done)\s+(?:a |an |the )?(?:harm|damage)\b"
    r"|\bput(?:s|ting)?\s+(?:emphasis|pressure|stress|a strain)\s+on\b", re.I)
# Nouns that carry a flagged suffix but bury no verb -- the cheap precision win. Chasing this
# list past the obvious offenders is the Goodhart trap the red-team named, so it stays short:
# every entry was read off a false positive in the first book-wide run.
NOT_DEVERBAL = {
    "reality", "conscience", "section", "foundation", "presence", "absence", "sentence",
    "distance", "science", "patience", "silence", "audience", "experience", "difference",
    "reference", "evidence", "confidence", "sequence", "counterbalance", "instance",
    "quality", "quantity", "city", "priority", "majority", "minority", "security",
    "university", "community", "identity", "activity", "opportunity", "authority",
    "responsibility", "ability", "reality", "capacity", "intimacy",
}

# DEAD: a motion/placement verb on a subject that cannot move -- an abstraction or a bare
# demonstrative. `land` and `leave` are the two Wendell named; the rest are the same fake-concrete
# family. Surfaced, never graded: on a concrete subject every one of these is a real verb.
DEADV = (r"lands?|landed|landing|leaves?|left|leaving|sits?|sat|sitting|hangs?|hung|hanging|"
         r"settles?|settled|settling|sinks?|sank|sunk|sinking|runs?|ran|running|"
         r"moves?|moved|moving|travels?|travell?ed|travell?ing|rides?|rode|carries|carried")
# The book's recurring abstractions, plus any nominalization-suffixed noun, plus a bare
# demonstrative. Kept explicit so the tier stays low-noise and aimed at the flagged family.
ABSTRACT = (r"praise|encouragement|shame|fear|trust|power|love|hope|doubt|guilt|grief|anger|joy|"
            r"help|care|respect|control|comfort|silence|attention|presence|absence|meaning|truth|"
            r"belief|faith|pride|courage|kindness|cruelty|authority|condescension|approval|"
            r"validation|recognition|feedback|criticism|praise|worth|grade|verdict")
DEAD = re.compile(r"\b(it|this|that|these|those|%s|\w{4,}(?:tion|sion|ment|ness))\s+"
                  r"(?:\w+ly\s+)?(?:%s)\b" % (ABSTRACT, DEADV), re.I)

# Measured 2026-09-03 by this file on the book's own body prose: 39 DELEXICAL and 124 DEAD across
# 5,985 sentences. DEAD runs high because most of its subjects are concrete and fine -- which is
# why it is surfaced, not graded.
BOOK_BASELINE = 0.7      # per cent of sentences carrying a DELEXICAL hit


def sites(text):
    out = []
    sents = [" ".join(s.split()) for s in SENT.split(text)]
    sents = [s for s in sents if len(s.split()) > 3]
    for s in sents:
        m = DELEXICAL.search(s)
        suffix_hit = m and m.group(1).lower() not in NOT_DEVERBAL
        if suffix_hit or LIGHT_PHRASE.search(s):
            out.append(("DELEXICAL", s))
        if DEAD.search(s):
            out.append(("DEAD", s))
    return out, len(sents)


def main():
    verbose = "-v" in sys.argv
    paths = dl.paths_from(sys.argv[1:])
    if paths:
        groups = [(os.path.basename(p), dl.prose(dl.surfaces([p]))) for p in paths]
    else:
        groups = [("the book", [l for l in fl.surfaces() if l["surface"] == "body"
                                and not l["text"].lstrip().startswith(("#", "|", ">", "-", "*"))])]

    print("light verb — the buried verb (DELEXICAL) and the fake-concrete verb (DEAD); see the docstring")
    print("%-24s %6s %5s %7s %8s" % ("file", "DELEX", "DEAD", "sents", "delex%"))
    print("-" * 56)
    bad, rows, total = 0, [], 0
    for label, lines in groups:
        hits, n = [], 0
        for l in lines:
            h, c = sites(l["text"])
            hits += [(t, s, l) for t, s in h]
            n += c
        dx = sum(1 for t, _s, _l in hits if t == "DELEXICAL")
        dv = sum(1 for t, _s, _l in hits if t == "DEAD")
        rate = 100.0 * dx / max(n, 1)
        flag = "" if rate <= BOOK_BASELINE + 2 else "  HEAVY"
        print("%-24s %6d %5d %7d %7.1f%%%s" % (label[:24], dx, dv, n, rate, flag))
        # On a draft, both tiers are candidates to look at. Book-wide DEAD is a backlog rather
        # than a build failure (its subjects are often concrete), so it does not inflate `bad`.
        bad += dx + (dv if paths else 0) + (1 if flag else 0)
        rows += hits
        total += n
    print("-" * 56)

    order = {"DELEXICAL": 0, "DEAD": 1}
    shown = sorted(rows, key=lambda r: order[r[0]])
    if shown:
        print("")
        for tier, s, l in (shown if verbose else shown[:12]):
            print("  %-9s %s:%d" % (tier, os.path.basename(l["rel"]), l["line"]))
            print("      > %s" % s[:130])
        if not verbose and len(shown) > 12:
            print("  … %d more, run with -v" % (len(shown) - 12))

    # Summary LAST, so review.py's book board reads it off lines[-1] rather than a site quote.
    print("")
    print("book baseline %.1f%% DELEXICAL. An existence check has a false-positive floor; the "
          "instrument surfaces, the reader clears." % BOOK_BASELINE)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
