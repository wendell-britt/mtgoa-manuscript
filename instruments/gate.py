# -*- coding: utf-8 -*-
"""
The standing voice gate from specs/MANUSCRIPT_FILE_CANON.md, as an instrument.

Scores each surface separately, because they are different registers by
different hands and a combined number hides which one regressed. Every counter
must read 0. Exits non-zero on any hit, so it can gate a commit.

Four surfaces, because four surfaces get printed:

  body        manuscript/ch1.md-ch9.md with the marginalia frame stripped
  marginalia  the frame blocks only
  appendices  the lettered appendices A-G
  matter      front matter and back matter

The last two were added 2026-07-29. Until then the gate read only manuscript/,
so ~10,000 words of shipping prose had never been held to the standing list.
Suppress them with --no-appendices when you are measuring a chapter edit in
isolation.

The `tokens` counter earns its keep on the matter surface: the front matter
carries ⟦ISBN-PRINT⟧, ⟦IMPRINT⟧, and the author-bio blanks, and the gate is what
stands between an unfilled placeholder and the typesetter.

    python3 instruments/gate.py                  # every printed surface
    python3 instruments/gate.py -v               # quote every hit with context
    python3 instruments/gate.py --no-appendices  # chapters only, the old behavior
"""
import re, io, os, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)
MS = os.path.join(ROOT, "manuscript")
APX = os.path.join(ROOT, "appendices")

# The appendices that ship. Everything else in appendices/ is a backup, an
# architecture decision record, or a review artifact, and is not printed.
SHIPPING_APPENDICES = [
    "APPENDIX_A_FOUR_ALLYSHIP_DOMAINS.md",
    "APPENDIX_B_QUESTS_CAMPAIGNS.md",
    "APPENDIX_C_FIVE_CHANNELS.md",   # C changed hands 2026-07-30 by Wendell's
                                     # ruling; the Key Terms glossary is retired
    "APPENDIX_D_EMOTIONAL_ALCHEMY_PRACTICES.md",
    "APPENDIX_E_321_SHADOW_PROCESS.md",
    "APPENDIX_F_POLARITY_MAP.md",
    "ON_THE_SHOULDERS_OF.md",
]
BLOCK = re.compile(
    r"<!-- (MARGINALIA|EPIGRAPH-BYLINE|POSTCARD) -->\n(.*?)\n<!-- /\1 -->", re.S)

# (name, pattern, flags) — flags matter: andbut and stacks are case-sensitive,
# and treating them otherwise invents violations that are not there.
COUNTERS = [
    ("andbut", r'(^|[.?!]["“”\'’]? |\*|\*\*|— |; )(And|But) ', re.M),
    # "rooms" plural banned 2026-07-29 by Wendell. The earlier rule read
    # \broom\b, which let the plural through; ch5 carried three.
    # 2026-07-31: the comparative and superlative were invisible. `quiet(ly)?` matched
    # `quiet` and `quietly` and walked past `quieter`, which sat in ch1 and ch5. Wendell
    # on the ch5 site: "how can you claim to hear something when you don't have ears. You
    # do have eyes so harder to see makes sense." The word was wrong there as a metaphor
    # before it was wrong as a banned word.
    # `thing` promoted 2026-08-03. Wendell: "sweep the marginalia and promote thing to
    # the gate." Body went 405 -> 0 uncovered and the marginalia 27 -> 0; everything that
    # remains is in CANON below. His reasoning, 2026-08-03: "it's not in my writing style
    # to use the word 'thing' because of how unspecific it is", and, on the classification
    # that had cleared 320 sites as idiom: "until I see a number of examples of 'the thing'
    # that are grammatical we're actually preserving something bad and saying it's ok
    # because we've done it before."
    ("banned", r'\brooms?\b|\bquiet(ly|er|est)?\b|\bgenuinely\b|\bthings?\b', re.I),
    ("emdash", r'[a-zA-Z0-9,]—[a-zA-Z0-9]', 0),
    ("A0", r'you (were|was) (taught|told|raised|trained)|somewhere along the way'
           r'|the village taught you', re.I),
    ("stacks", r'\bNot [^.!?]{1,60}[.!?]\s+(Not|Never|No)\b', 0),
    # Unfilled HEAD_REGISTERS biography placeholders. Deliberately introduced by
    # W6 and must not survive to print — see R9. This counter is the only thing
    # standing between a token and the typesetter.
    ("tokens", r'⟦[^⟧]*⟧', 0),
]


# Sentence-level exemptions, each one ruled by Wendell on a named date. Keyed on the
# exact sentence rather than the word, so an exemption cannot silently spread: change
# the sentence and the exemption stops applying, which is the behaviour we want.
#
# The alternative was weakening a counter's pattern book-wide, which trades one
# approved site for an unbounded number of unapproved ones.
EXEMPT = [
    ("banned",
     "the Sage's question is about rooms rather than about people",
     "2026-07-30 — Laloux entry, Appendix G. Wendell: \"we can leave rooms in this "
     "example. It's not load bearing.\""),
]


# CANON is not EXEMPT, and the difference is the reason there are two lists.
#
# EXEMPT approves one sentence. It is keyed on the whole sentence precisely so an approval
# cannot spread, which is right for a one-off like the Laloux `rooms` line.
#
# CANON approves a NAME. A named move keeps its name everywhere it appears, so keying on a
# sentence would mean re-approving the same title in every chapter that cites it. Each
# entry below is a ruling by Wendell on 2026-08-03, and each is a title or a thesis rather
# than a sentence somebody happened to write.
CANON = [
    ("banned", "Say the Thing Under the Thing",
     "ch3 Move 5. Ruled: option b, keep the move name and sweep the prose around it."),
    # FLAG WITHDRAWN 2026-08-03. I recorded this as an inconsistency and it is a rule.
    # ch3 lowercases a move name when the sentence is TELLING YOU TO DO IT and capitalises
    # it when the sentence is NAMING IT, and all five moves obey it:
    #   820 "Turn the dial up instead"      846 "Say what you can do now, to her, once"
    #   860 "Say the thing under the thing:" 866 all five lowercase in one run
    #   850 the heading   962 "*Say the Thing Under the Thing* becomes:"   981 the list
    # Capitalising 860 and 866 would have broken a set that was already consistent, so both
    # spellings are canon and both are exempt.
    ("banned", "Say the thing under the thing",
     "the same move as an imperative in running prose, ch3:860 and ch3:866."),
    ("banned", "*Say the Thing*",
     "ch4:752, the quest card."),
    ("banned", "Run It Again With One Thing Changed",
     "ch9 Move 4."),
    ("banned", "Run it again with one thing changed",
     "the same move in ch9's recaps at 576 and 590."),
    ("banned", "Right Thing the Easy Thing",
     "ch6's chapter subtitle. Wendell 2026-08-03: \"keep the right thing the easy thing.\""),
    ("banned", "right thing",
     "the Architect's thesis. Quoted three times inside ch6, once from ch5's closing "
     "handoff and twice in ch9 — a thesis rather than a heading, which is why it is here "
     "and not in EXEMPT."),
    ("banned", "easy thing",
     "the second half of the same thesis."),
    ("banned", "the right thing becomes the thing that actually gets done",
     "ch6:197, the thesis stated as a question. The second `thing` is inside the formula."),
    # The strongest exemption in the sweep, because the sentence diagnoses the placeholder.
    ("banned", "*This is my thing*",
     "ch8:769. Quoted self-talk that the chapter is convicting: \"It's a category that "
     "swallows all five, and once it's on the table nothing gets named specifically enough "
     "to move.\" The vagueness IS the diagnosis; naming it would destroy the specimen. "
     "FLAGGED as my judgement rather than Wendell's ruling."),
    ("banned", "not *my thing.*",
     "ch8:779, the same specimen in the recap."),
    ("banned", "you lose the things that told you who you were",
     "ch1:54. Ruled an exception by Wendell 2026-08-03. It survives on the rule rather "
     "than on precedent: the sentence before supplies the referent — \"The game hands you "
     "every bit of it\" — so the definite article has a real antecedent."),
]


def exempt_spans(text, counter):
    """Character spans in `text` that this counter must ignore."""
    spans = []
    for name, phrase, _reason in EXEMPT + CANON:
        if name != counter:
            continue
        i = text.find(phrase)
        while i >= 0:
            spans.append((i, i + len(phrase)))
            i = text.find(phrase, i + 1)
    return spans


def split_surfaces(text):
    """Return (body, marginalia) for one chapter."""
    marg = "\n".join(m.group(2) for m in BLOCK.finditer(text))
    return BLOCK.sub("", text), marg


def score(text):
    out = []
    for n, p, f in COUNTERS:
        skip = exempt_spans(text, n)
        out.append((n, [m for m in re.finditer(p, text, f)
                        if not any(a <= m.start() < b for a, b in skip)]))
    return out


def main():
    verbose = "-v" in sys.argv
    files = sorted(glob.glob(os.path.join(MS, "ch*.md")),
                   key=lambda f: int(re.search(r"ch(\d+)", os.path.basename(f)).group(1)))
    surfaces = {"body": "", "marginalia": ""}
    for f in files:
        b, m = split_surfaces(io.open(f, encoding="utf-8").read())
        surfaces["body"] += "\n" + b
        surfaces["marginalia"] += "\n" + m

    if "--no-appendices" not in sys.argv:
        text = ""
        for name in SHIPPING_APPENDICES:
            path = os.path.join(APX, name)
            if os.path.exists(path):
                text += "\n" + io.open(path, encoding="utf-8").read()
        surfaces["appendices"] = text

        matter = ""
        for d in (os.path.join(ROOT, "front_matter"), os.path.join(ROOT, "back_matter")):
            for path in sorted(glob.glob(os.path.join(d, "*.md"))):
                matter += "\n" + io.open(path, encoding="utf-8").read()
        surfaces["matter"] = matter

    names = [n for n, _, _ in COUNTERS]
    print("%-12s %s" % ("surface", " ".join("%8s" % n for n in names)))
    print("-" * 62)
    total = 0
    for label, text in surfaces.items():
        s = score(text)
        total += sum(len(ms) for _, ms in s)
        print("%-12s %s" % (label, " ".join("%8d" % len(ms) for _, ms in s)))
    print("-" * 62)

    if verbose:
        for label, text in surfaces.items():
            for name, ms in score(text):
                for m in ms:
                    ctx = text[max(0, m.start() - 70):m.end() + 70].replace("\n", " ")
                    print("\n%s [%s] %r\n    …%s…" % (label, name, m.group(0).strip(), ctx.strip()))
        print()

    print("GATE PASS — every counter reads 0" if total == 0
          else "GATE FAIL — %d hit(s). Re-run with -v to see them." % total)
    return 0 if total == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
