# -*- coding: utf-8 -*-
"""Run the pattern instruments against a draft file, before it lands.

    python3 instruments/draftprobe.py DRAFT.md

## Why this exists

`shapes`, `preempt`, `assumed`, `antecedent`, `agency` and `fragment` are
board-only: they walk the manuscript spine and ignore any path handed to them. So step 3 of the
review process has been checking those families by eye on every draft since
they were built. This harness imports their compiled patterns and applies them
to one file.

**`agency.py` was the expensive one.** It has a board of its own, and it is in
neither of `review.py`'s chains -- not the draft path (gate + diet + hand slop)
and not the six-step board (gate, diet, em-dash, seam, citations, round-trip).
So it never runs as part of the review process and it has never seen a draft.
Worse, `prose_diet -v` prints a section labelled *agency* which is a narrower
separate check, so the output looked like agency had run. Wendell caught `the
trust that decides it` in a draft that had passed gate, diet and a hand slop
pass -- `agency.py`'s own lists score it Tier 1, because `trust` is not in
ANIMATE and `decides` is in MENTAL.

**Its ANIMATE list held the six Faces and not the seven daemons** until
2026-08-03, when Wendell ruled the daemons in. That fix lives upstream now and
the board moved 207/294 to 177/285. BOOK_ANIMATE below carries what is left:
the named hypothetical people the Examples use, who score zero on the board
today and appear the moment a draft introduces a new one.

## The two checks defined here rather than imported

**bare definite abstraction.** Wendell, 2026-08-03, on *"with the caring intact
and the skill intact"*: *"illegal use of the definite pronoun. If we don't have
a rule for this we need to make sure that all uses of 'the' have antecedents
that are named."* `shapes.SERIES` only catches three or more in a comma series;
a single `the <abstraction>` standing over nothing passed clean. Full
coreference is out of scope, so this reports `the` + an uncountable abstraction
whose stem has not appeared earlier in the passage. A reader rules each one.

**antecedent.** Added 2026-08-03, closing the last of the five. It reports a
pronoun with no candidate noun anywhere in its paragraph, plus one whose nearest
candidate sits past the distance limit -- 172 and 5 sites respectively, book-wide.

**And it would not have caught the sentence that prompted it, which is worth
recording rather than papering over.** The bio's first draft read *Wendell Britt
spent fifteen years in customer service. For the rest of it he has been the
meddling kid.* `it` points at nothing -- the sentence never said *life* -- but
`service` sits three words back, so distance reports the paragraph clean. **The
defect is a pronoun whose nearest noun is close and wrong**, and no instrument in
this harness can see that: they all measure position, and this one needs meaning.
A reader caught it and a reader is what it takes.

**fragment.** Added 2026-08-03, the sixth and the last of the always-on
constraints to get an instrument. It needs the corpus verb lexicon rather than
the draft's own words, because one paragraph does not contain enough verbs to
learn from, so it builds the lexicon off the spine and scans the draft with it.

**not-at-the-level-of.** `shapes.BINARY` does not match *Not at the level of X,
and not at the level of Y* -- the negation is adverbial rather than a bare
predicate, so every anchored alternative in that regex misses it. Reported here
until the form is added upstream.
"""
import io, os, re, sys, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    argv, sys.argv = sys.argv, [name]
    try:
        spec.loader.exec_module(mod)
    finally:
        sys.argv = argv
    return mod


# Uncountable abstractions that take a bare `the` and frequently stand over
# nothing. Read off the sites this book actually produces rather than invented.
ABSTRACTION = """caring care skill trust harm help healing damage work effort
courage shame grief rage safety belonging power privilege consent intention
attention repair reckoning practice discipline vulnerability accountability
labor labour wound wounding""".split()

# EMPTY nouns are reported on EVERY occurrence, with no antecedent logic at all.
# Added 2026-08-03 after Wendell caught `the thing runs after you leave` in prose
# that had passed gate, diet and the abstraction check. The check missed it for a
# reason worth keeping: it suppresses a noun once the stem appears earlier in the
# passage, and an earlier `the true thing` had put `thing` on the seen list.
#
# **For an abstraction a prior mention is a real antecedent. For an empty noun it
# never is.** `the trust` after `their trust` points at something; `the thing`
# after `the true thing` points at nothing, twice. `prose_diet`'s `empty` counter
# sees these words but only as a ratio, and a ratio cannot fail one sentence.
EMPTY = """thing things something version versions way ways part parts
result results point points""".split()

BARE_DEF = re.compile(r"\bthe (%s)\b" % "|".join(ABSTRACTION), re.I)
BARE_EMPTY = re.compile(r"\bthe (%s)\b" % "|".join(EMPTY), re.I)

# The not-X-but-Y form shapes.BINARY cannot see.
ADVERBIAL_NOT = re.compile(
    r"\bNot (?:at|in|on|for|about|because of) [^.!?]{0,60}?,? and not "
    r"(?:at|in|on|for|about|because of)\b[^.!?]{0,60}", re.I)


# Named hypothetical people the Examples use (Dana ch3:896, Priya ch4:632,
# Marcus ch5:607, Nia ch7:594, Sam ch8:630, Rosa ch9:528) are people and are
# missing from agency.py's ANIMATE. They score zero on the board, so this is a
# draft-time list only. Reported as RULED rather than dropped.
BOOK_ANIMATE = set("""dana priya marcus nia sam rosa imani""".split())


def compiled(entry):
    return re.compile(entry, re.I) if isinstance(entry, str) else entry


def main():
    text = io.open(sys.argv[1], encoding="utf-8").read()
    paras = [p for p in text.split("\n\n") if p.strip() and not p.lstrip().startswith("#")]
    body = "\n\n".join(paras)

    shapes = load("shapes")
    preempt = load("preempt")
    assumed = load("assumed")
    agency = load("agency")
    antecedent = load("antecedent")
    fragment = load("fragment")

    hits = 0

    print("=== shapes ===")
    for label, pat in (("binary contrast", shapes.BINARY),
                       ("binary contrast (adverbial)", ADVERBIAL_NOT),
                       ("definite-article series", shapes.SERIES)):
        for m in pat.finditer(body):
            hits += 1
            print("  %-28s %s" % (label, m.group(0)[:96].replace("\n", " ")))
    for r in shapes.runs(body):
        hits += 1
        print("  %-28s %s" % ("determiner run", r[:96]))

    # A `the <abstraction>` is legal once the abstraction has been named. Only
    # the first mention in the passage can be standing over nothing, so later
    # ones are skipped rather than reported as a pile.
    print("=== definite antecedent ===")
    seen = set()
    for m in BARE_DEF.finditer(body):
        noun = m.group(1).lower()
        before = body[:m.start()].lower()
        if noun in seen:
            continue
        seen.add(noun)
        # named earlier means the stem appears before this `the`, not counting
        # the article phrase itself
        if re.search(r"\b%s\b" % noun, before):
            continue
        hits += 1
        s = body.rfind(".", 0, m.start()) + 1
        print("  %-28s [the %s] %s" % ("bare definite abstraction", noun,
                                       body[s:s + 80].strip().replace("\n", " ")))
    for m in BARE_EMPTY.finditer(body):
        hits += 1
        s = body.rfind(".", 0, m.start()) + 1
        print("  %-28s [the %s] %s" % ("definite + empty noun", m.group(1).lower(),
                                       body[s:s + 80].strip().replace("\n", " ")))

    # fragment.py needs the corpus verb lexicon, which is built from the spine and
    # not from the draft: one paragraph does not contain enough verbs to learn from.
    print("=== fragment ===")
    fp, fw = fragment.dn.tagger()
    if fp is None:
        print("  tagger unavailable")
    else:
        flines = [l for l in fragment.fl.surfaces()
                  if not l["text"].lstrip().startswith(fragment.SKIP_LINE)]
        flex = fragment.verb_lexicon(flines, fp, fw)
        for para in paras:
            if para.lstrip().startswith(fragment.SKIP_LINE):
                continue
            for kind, n, st in fragment.sites(para, flex, fp, fw):
                if kind != "LANDING":
                    hits += 1
                print("  %-28s [%s %dw] %s" % ("fragment", kind, n, st[:58]))

    print("=== preempt ===")
    for label, pat in preempt.SHAPES:
        for m in compiled(pat).finditer(body):
            hits += 1
            print("  %-28s %s" % (label, m.group(0)[:90].replace("\n", " ")))

    print("=== assumed ===")
    for group, name in ((assumed.CLAIMS, "CLAIM"), (assumed.HISTORY, "HISTORY"),
                        (assumed.EXPERIENCE, "EXPERIENCE")):
        for label, pat in group:
            for m in compiled(pat).finditer(body):
                hits += 1
                print("  %-10s %-22s %s" % (name, label, m.group(0)[:66].replace("\n", " ")))
    for m in assumed.INVITE.finditer(body):
        print("  %-10s %-22s %s" % ("INVITE", "(good)", m.group(0)[:66].replace("\n", " ")))

    # antecedent.sites() works per paragraph, because the defect it names is a
    # pronoun whose referent sits outside the paragraph holding it.
    print("=== antecedent ===")
    ap, aw = antecedent.dn.tagger()
    if ap is None:
        print("  tagger unavailable")
    else:
        for para in paras:
            if para.lstrip().startswith(("|", ">")):
                continue
            for pron, sent, dist, _ in antecedent.sites(para, ap, aw):
                hits += 1
                why = "no antecedent in the paragraph" if dist is None else "%d words back" % dist
                print("  %-28s [%s] %s -- %s" % ("orphan pronoun", pron,
                                                 sent.strip()[:56], why))

    # agency.py's own classify(), over the draft's sentences and its subclauses.
    # head_of_subject walks to the first finite verb, so a defect sitting inside
    # a relative clause -- `the trust that decides it` -- is invisible unless the
    # clause is offered as its own unit. Splitting on that/which/who does it.
    print("=== agency ===")
    pos_tag, word_tokenize = agency.dn.tagger()
    if pos_tag is None:
        print("  tagger unavailable")
    else:
        units = []
        for sent in re.split(r"(?<=[.!?])\s+", body):
            s = sent.strip()
            if not s or s.startswith(("#", "|")):
                continue
            units.append(s)
            for m in re.finditer(
                    r"\b((?:the|a|an|their|her|his|your|its) \w+ (?:that|which) \w+(?: \w+)?)",
                    s, re.I):
                units.append(m.group(1))
        for u in units:
            c = agency.classify(u, pos_tag, word_tokenize)
            if not c or c["tier"] is None:
                continue
            ruled = c["subj"] in BOOK_ANIMATE
            label = "TIER 1 mental" if c["tier"] == 1 else "candidate volitional"
            if ruled:
                label = "RULED animate (book)"
            elif c["tier"] == 1:
                hits += 1
            print("  %-28s [%s %s] %s" % (label, c["subj"], c["verb"], u[:66]))

    print("\n%d pattern hit(s)" % hits)


if __name__ == "__main__":
    main()
