# -*- coding: utf-8 -*-
"""
prose_diet.py — the three grammar moves, measured.

Named 2026-07-29 after they were caught by eye in the W7 rewrites: leaning on
"is", on "it" without a clear antecedent, and on articles fronting nominalized
verbs. All three are ways of sounding like a sentence without committing to one,
and all three are nearly invisible one line at a time.

Implements the diagnostics four editors converge on:

  Lanham, *Revising Prose* — the Paramedic Method. Box the be-verbs, circle the
  prepositions, then ask "who is kicking whom?" and put the doer in the subject.
  Be-verbs are where the action went missing.

  Williams, *Style: Lessons in Clarity and Grace* — subjects should name
  characters, verbs should name their actions. When the action hides in a noun,
  turn the noun back into a verb. Williams licenses nominalization in four
  cases, which is why this is a candidate finder and not a gate.

  Sword, *The Writer's Diet* — five categories, three of which are these:
  be-verbs, zombie nouns, and the waste words *it / this / that / there*. Her
  rule for the last: use "it" and "this" only when you can state exactly which
  noun each refers to.

  Vague-pronoun-reference doctrine — search the draft for it/this/which/that,
  draw an arrow to the antecedent, and rewrite anything with no arrow.

**Thresholds are this book's own baseline, not absolute standards.** The
manuscript is written; the job is to stop new prose drifting heavier than the
prose around it. A chapter at the book average scores 1.00.

    python3 instruments/prose_diet.py              # per chapter vs baseline
    python3 instruments/prose_diet.py -v           # quote the orphan "it" sites
    python3 instruments/prose_diet.py FILE         # score a draft file
"""
import re, io, os, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")
# HANDBOOK and SIGNATURE added 2026-07-31, when they turned out to be counted inside every
# chapter's expository score. Measured on ch7 the effect is small, passive 1.75 against 1.77
# stripped, so it was not the cause of anything; stripping them is correct regardless, because
# an admissions page and a treatise signature are not the chapter's prose and are governed by
# HEAD_VOICE_DIAL rather than by this baseline.
BLOCK = re.compile(
    r"\n?\n<!-- (MARGINALIA|EPIGRAPH-BYLINE|POSTCARD|HANDBOOK|SIGNATURE) -->\n"
    r".*?\n<!-- /\1 -->\n", re.S)

BE     = re.compile(r"\b(is|are|was|were|be|been|being)\b", re.I)
COPULA = re.compile(r"^\W*[\w'][\w' ]{0,30}\s(is|are|was|were)\s", re.I)
WASTE  = re.compile(r"\b(it|this|that|there)\b", re.I)
# Sword's zombie nouns arrive wearing an article — that is what makes them
# findable. "the maintenance of", "a recognition that".
# WIDENED 2026-07-31. The first version required the noun immediately after the article, so
# "the polite version" and "the composed version" both walked through on one adjective.
# Wendell caught both by eye, twice, which is the whole argument for widening it.
# EMPTY, added 2026-07-31. Wendell, on a draft that passed all six counters:
# "I'm starting to hate the word 'Thing' like I'm starting to hate the word room.
# It's a wack-a-mole of empty words."
#
# He is describing a hole, not a preference. Driving `waste` down removes pronouns,
# and what replaces them is an empty noun the other six counters cannot see. Measured
# on the draft that prompted this: 23.1 per thousand, against 0.0 in both of the
# sections it was written to sit beside and 14.0 book-wide, while every existing
# counter reported it clean.
EMPTY = re.compile(r"\b(thing|things|something|anything|nothing|version|versions"
                   r"|stuff|way|ways|part|parts|aspect|aspects|element|elements"
                   r"|area|areas|piece|pieces|room|rooms)\b", re.I)

ZOMBIE = re.compile(r"\b(?:the|a|an)\s+(?:\w+\s+){0,2}"
                    r"\w+(?:tion|ment|ance|ence|ness|ity|ism|sion)\b", re.I)

# PASSIVE and AGENT, added 2026-07-31. Wendell: "we don't seem to be able to pick up
# something that a high school English teacher could catch."
#
# He is right, and the gap was specific. `BE` counts be-verbs and `ZOMBIE` counts
# nominalisations, and neither one sees the two things a teacher circles first: a verb with
# no doer, and a doer that cannot act.
PASSIVE = re.compile(
    r"\b(?:is|are|was|were|be|been|being)\s+(?:\w+ly\s+)?"
    r"(?:\w+ed|known|seen|done|made|taken|given|held|told|said|written|built|kept|left|"
    r"put|set|shown|drawn|brought|found|heard|lost|sent|meant|felt)\b(?!\s+(?:to|that))",
    re.I)

# Abstractions given human verbs. A candidate finder rather than a counter, because some of
# these are correct English -- a question can resolve, a cost can land. The judgement is
# whether a reader can name who did it. Reported under -v only.
AGENT_NOUNS = (r"version|story|thing|part|move|read|point|conversation|situation|feeling|"
               r"moment|question|answer|tightening|naming|charge|energy|work|process|system")
AGENT = re.compile(r"\b[Tt]he\s+(?:\w+\s+){0,2}(?:%s)\s+"
                   r"(?:arrives?|assembles?|lands?|moves?|tells?|carries|carry|does|do|"
                   r"wants?|decides?|knows?|sees?|takes?|gives?|holds?|starts?|begins?)\b"
                   % AGENT_NOUNS)
# "It is/was" opening a sentence with no noun behind it: Lanham's expletive,
# Sword's waste word, and the classic missing antecedent, all at once.
EXPLETIVE = re.compile(r"(?:^|(?<=[.!?]\s))\s*(It|There)\s+(is|was|are|were)\b")

# BASELINE IS EXTERNAL, DELIBERATELY.
#
# The first version of this file normalised against the manuscript's own
# average, which made the book incapable of failing its own test: every chapter
# scored ~1.00 and the tool reported nothing. SPEC_REPETITION_AND_CUTS had
# already settled the question the other way, against three outside books —
# MTGOA runs the copula at 62.8 per thousand against 28.8 in Igniting Joy, 2.2
# times the rate, and that spec names the short-declarative register as drift
# rather than voice. Normalising to it protected the defect. Its own warning
# applies: when a feature of the prose needs defending, check whose hand put it
# there before defending it.
#
# Target is Igniting Joy — Wendell's own book, so the bar is his voice working,
# not a stranger's. Elliott and Chou bracket it for sanity.
TARGET   = {"copula_1k": 28.8, "mean_sent": 18.8, "short_pct": 4.2, "hedge_1k": 2.8}
BRACKET  = {"copula_1k": (40.9, 41.1), "mean_sent": (23.7, 22.5),
            "short_pct": (12.4, 12.8), "hedge_1k": (12.2, 5.9)}
# Manuscript position as measured in SPEC_REPETITION_AND_CUTS, for reference.
MTGOA_WAS = {"copula_1k": 62.8, "mean_sent": 13.4, "short_pct": 27.5, "hedge_1k": 6.2}

# Retained for the pronoun check, which is a rate question rather than a
# comparative one. Book figures, not targets.
# zombie was 11.1 against the narrow regex. Widening the regex without re-measuring the
# baseline pushed all nine chapters above 1.00 on a counter nothing had changed in, which is
# a measurement bug rather than a finding. Re-measured 2026-07-31 at 15.0.
BASE = {"be": 50.3, "copula": 29.1, "waste": 56.3, "zombie": 15.0, "expletive": 2.4,
        # MEASURED across the nine chapters 2026-07-31, the day the counter was added.
        # The first value here was 5.6 and I had typed it rather than measured it, which is
        # the exact failure this file exists to catch. The book runs 3.1.
        "passive": 3.1,
        # measured across manuscript/ch*.md, 2026-07-31
        "empty": 14.0}

# REGISTERS — the criteria adjusting to the book, added 2026-07-31.
#
# Wendell: "the letter is ok because it is the register of a personal letter… I think ch5
# is also a reasonable exception. We should be updating our review criteria to adjust to
# these stylistic changes we are making as well."
#
# BASE was measured before the book grew genres. It is nine chapters of Wendell's own
# expository prose, and by that ruler a charter, a personal letter, a drill manual and a
# practitioner's casebook all read as defects. They are not defects. They are the
# `HEAD_VOICE_DIAL` doing exactly what it was written to do, and a ruler that punishes a
# voice the author ruled is a ruler measuring the wrong thing.
#
# So: a named register raises the ceiling on the specific counters its genre inflates, and
# on nothing else. Every entry carries the date, the ruling and the reason, which is
# `gate.py`'s EXEMPT convention. **An unnamed file gets BASE**, so this cannot spread by
# accident: a new file has to be added here on purpose, with a reason, by a person.
REGISTERS = {
    "headmasters_letter.md": {
        "be": 1.30, "copula": 1.30,
        "why": "a personal letter from one man to one reader. First person singular "
               "carries I am, we are, it is at a rate expository prose does not. Ruled "
               "2026-07-31: 'the letter is ok because it is the register of a personal "
               "letter.'",
    },
    # The same ruling as CH5_REGISTER below, reached through the chapter rather than the
    # draft. SPEC_REGISTER_BLOCKS_2026-07-31 §1: the charter is 409 words inside a
    # 10,000-word file, so a file-level exception fires on the draft and never on ch5.md.
    "ch5.md": {
        "blocks": [{
            "start": "**Clause four.**",
            "end": "It records no case of a keeper who stopped attempting it either.",
            # RATCHET, ruled by Wendell 2026-07-31. Each ceiling is the measured value of
            # the passage as it stands, on the em-dash budget's rule: it may be lowered when
            # the prose improves and it may never be raised to make a batch pass. Two of
            # these went DOWN from the numbers I guessed writing the spec, be from 1.60 and
            # expletive from 2.00, because a measurement beats an estimate in both
            # directions.
            "be": 1.40, "zombie": 1.84, "expletive": 1.89, "passive": 11.32,
            "why": "Quill's annotated charter, seated in ch5 Section 3, 399 words. A charter "
                   "states what shall be done without naming who does it, which is what "
                   "makes it a charter rather than a memo. It runs eleven times the book's "
                   "passive rate and that is the form rather than drift. Ruled 2026-07-31.",
        }],
    },
    "CH5_REGISTER": {
        "zombie": 1.60, "be": 1.60, "expletive": 2.00,
        "why": "Quill's annotated charter. HEAD_VOICE_DIAL 2a rules her third impersonal, "
               "fact and record, feeling only as a ledger entry, and a charter is nominal "
               "by construction: the dissolution, the refusal, the observation. Flattening "
               "the nominalisation would flatten the voice. Ruled 2026-07-31: 'I think ch5 "
               "is also a reasonable exception.'",
    },
}

# A limit worth knowing. The register is 400 words inside a 10,000-word chapter, so once it
# lands in ch5.md the chapter's own score swamps it and the exemption never fires. It fires
# on the draft file, which is where the check belongs anyway: before it lands.


def register_for(name):
    """The allowances that apply to a file, or {} for the book baseline."""
    for key, spec in REGISTERS.items():
        if key.lower() in name.lower():
            return spec
    return {}

# Two rulers, deliberately, because they answer different questions.
#
# COPULA_JUNE reproduces the regex SPEC_REPETITION_AND_CUTS used, so the book can
# be compared against its own June baseline of 62.8 and against Igniting Joy's
# 28.8 on the same terms. It counts a bare 's, which means it counts POSSESSIVES.
#
# That flaw was caught 2026-07-29 by a register agent working ch5, which noticed
# that "the Regent's" appears 34 times there and was contributing ~9% of the
# chapter's copula count. Measured book-wide: 758 's tokens, of which only 335
# are true contractions (it's, that's) and 423 are possessives. They inflate the
# ratio by 0.15x.
#
# COPULA_1K is the corrected measure and is what register() reports. Whether
# Igniting Joy's 28.8 carries the same inflation cannot be checked here — the
# corpus is gitignored — so the 28.8 target may itself be high. The direction and
# the per-chapter comparisons are unaffected either way, since every chapter is
# measured identically, and the approved 1.50x calibration came from Wendell
# READING ch8 Section 2, not from the number.
COPULA_JUNE = re.compile(r"\b(is|are|was|were|be|been|being)\b|'s\s|'re\s", re.I)
COPULA_1K = re.compile(
    r"\b(is|are|was|were|be|been|being)\b"
    r"|\b(?:it|that|there|this|he|she|what|who|here|one|everything|nothing)'s\s"
    r"|'re\s", re.I)
HEDGE = re.compile(r"\b(perhaps|somewhat|arguably|rather|fairly|quite|often|tends? to|"
                   r"generally|typically|might|maybe|sort of|kind of)\b", re.I)


def register(text):
    """The four metrics that are comparable to the external corpora."""
    S = sentences(text)
    lens = [len(s.split()) for s in S] or [0]
    w = max(len(text.split()), 1)
    return {
        "copula_1k": len(COPULA_1K.findall(text)) / w * 1000,
        "mean_sent": sum(lens) / len(lens),
        "short_pct": sum(1 for x in lens if x <= 6) / len(lens) * 100,
        "hedge_1k":  len(HEDGE.findall(text)) / w * 1000,
    }


def sentences(t):
    t = re.sub(r"```.*?```", " ", t, flags=re.S)
    t = re.sub(r"^[#>|\-*\s]*$", " ", t, flags=re.M)
    t = re.sub(r"\s+", " ", t)
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", t) if len(s.split()) > 3]


def score(text):
    w = max(len(text.split()), 1)
    S = sentences(text)
    n = max(len(S), 1)
    return {
        "be":        len(BE.findall(text)) / w * 1000,
        "copula":    sum(1 for s in S if COPULA.search(s)) / n * 100,
        "waste":     len(WASTE.findall(text)) / w * 1000,
        "zombie":    len(ZOMBIE.findall(text)) / w * 1000,
        "expletive": sum(1 for s in S if EXPLETIVE.match(s)) / n * 100,
        "passive":   len(PASSIVE.findall(text)) / w * 1000,
        "empty":     len(EMPTY.findall(text)) / w * 1000,
    }


def split_blocks(text, spec):
    """Return (body, [(block_text, block_spec), ...]).

    An anchor matching zero times or more than once is a HARD ERROR rather than a silent
    pass. A register is an exemption, and an exemption that stops applying without saying
    so is how a defect gets licensed by accident."""
    out = []
    for b in spec.get("blocks", []):
        for key in ("start", "end"):
            if text.count(b[key]) != 1:
                raise SystemExit("register anchor %r matched %d times, expected 1"
                                 % (b[key][:56], text.count(b[key])))
        i = text.index(b["start"])
        j = text.index(b["end"]) + len(b["end"])
        out.append((text[i:j], b))
        text = text[:i] + text[j:]
    return text, out


def read(f):
    """The scored surface of a file: frame blocks stripped, excepted blocks lifted out."""
    t = BLOCK.sub("", io.open(f, encoding="utf-8").read())
    return split_blocks(t, register_for(os.path.basename(f)))


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    verbose = "-v" in sys.argv
    if args:
        files = args
    else:
        files = sorted(glob.glob(os.path.join(MS, "ch*.md")),
                       key=lambda f: int(re.search(r"ch(\d+)", os.path.basename(f)).group(1)))

    keys = ["be", "copula", "waste", "zombie", "expletive", "passive", "empty"]
    print("ratio against the book's own baseline — 1.00 is average, >1.30 is heavy")
    print("a * marks a counter covered by a named register in REGISTERS\n")
    print(f"{'file':<12}" + "".join(f"{k:>11}" for k in keys))
    print("-" * (12 + 11 * len(keys)))
    worst = []
    for f in files:
        name = os.path.basename(f)
        body, blocks = read(f)
        reg = register_for(name)
        for label, text, spec in ([(name, body, reg)]
                                  + [("  block %d" % (n + 1), bt, bs)
                                     for n, (bt, bs) in enumerate(blocks)]):
            s = score(text)
            cells = []
            for k in keys:
                # Compare at the precision that is printed. A ratchet ceiling is copied from
                # this table by a human, so a true 1.8912 displayed as 1.89 must not report
                # heavy against a ceiling of 1.89. Rounding first makes the number on the
                # page and the number in REGISTERS the same number.
                r = round(s[k] / BASE[k], 2)
                cells.append(f"{r:>10.2f}" + ("*" if k in spec else " "))
                if r > spec.get(k, 1.30):
                    worst.append((label.strip() or name, k, r, k in spec, spec))
            print(f"{label:<12}" + "".join(cells))

    if worst:
        print("\nheavy:")
        for f, k, r, covered, spec in sorted(worst, key=lambda x: -x[2]):
            ceiling = spec.get(k, 1.30)
            print(f"  {f} {k} {r:.2f} over {ceiling:.2f}"
                  + (" (register ceiling)" if covered else ""))

    if verbose:
        print("\n--- passive: a verb with no doer ---")
        for f in files:
            t, _ = read(f)
            for s in sentences(t):
                m = PASSIVE.search(s)
                if m:
                    print(f"  {os.path.basename(f)}: [{m.group(0)}] {s[:88]}")

        print("\n--- agency: an abstraction doing a human verb (judgement) ---")
        for f in files:
            t, _ = read(f)
            for s in sentences(t):
                m = AGENT.search(s)
                if m:
                    print(f"  {os.path.basename(f)}: [{m.group(0).strip()}] {s[:88]}")

        print("\n--- expletive / orphan openers: no noun behind the pronoun ---")
        for f in files:
            t, _ = read(f)
            for s in sentences(t):
                if EXPLETIVE.match(s):
                    print(f"  {os.path.basename(f)}: {s[:96]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
