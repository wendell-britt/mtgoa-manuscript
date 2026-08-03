# -*- coding: utf-8 -*-
"""Run the pattern instruments against a draft file, before it lands.

    python3 instruments/draftprobe.py DRAFT.md

## Why this exists

`shapes`, `preempt`, `assumed`, `antecedent` and `agency` are board-only: they
walk the manuscript spine and ignore any path handed to them. So step 3 of the
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

**And its ANIMATE list holds the six Faces but not the seven daemons**, which
this book personifies on purpose: `ch2:248` defines a daemon as a part that
acts on its own, and the first walk is `The Protector has the joystick` seven
times over. 39 of the board's 207 Tier 1 sites are daemon subjects. The board's
number is cited in specs, so it is left alone; BOOK_ANIMATE below rules them
for drafts and prints the ruling rather than hiding it.

## The two checks defined here rather than imported

**bare definite abstraction.** Wendell, 2026-08-03, on *"with the caring intact
and the skill intact"*: *"illegal use of the definite pronoun. If we don't have
a rule for this we need to make sure that all uses of 'the' have antecedents
that are named."* `shapes.SERIES` only catches three or more in a comma series;
a single `the <abstraction>` standing over nothing passed clean. Full
coreference is out of scope, so this reports `the` + an uncountable abstraction
whose stem has not appeared earlier in the passage. A reader rules each one.

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

BARE_DEF = re.compile(r"\bthe (%s)\b" % "|".join(ABSTRACTION), re.I)

# The not-X-but-Y form shapes.BINARY cannot see.
ADVERBIAL_NOT = re.compile(
    r"\bNot (?:at|in|on|for|about|because of) [^.!?]{0,60}?,? and not "
    r"(?:at|in|on|for|about|because of)\b[^.!?]{0,60}", re.I)


# Subjects agency.py's ANIMATE does not carry but this book treats as agents:
# the seven daemons, and the named hypothetical people the Examples use
# (Dana ch3:896, Priya ch4:632, Marcus ch5:607, Nia ch7:594, Sam ch8:630,
# Rosa ch9:528). Reported as RULED rather than dropped.
BOOK_ANIMATE = set("""protector controller skeptic fixer healer victim daemon
daemons self body dana priya marcus nia sam rosa imani""".split())


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
