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
# ---------------------------------------------------------------- the fragment counter
#
# Added 2026-09-01, on Wendell's ruling that the ban reaches the manuscript.
#
# The house constraint used to read "fragments carry beats, never claims, and only in
# landing position." He revoked the whole clause, the word included, for being gameable:
# given a rule that pays out for rhythm, prose drifts toward sounding rhythmic in order
# to qualify, and the rule ends up protecting the habit it was written to constrain. The
# rule now has no exception, which is what makes it checkable.
#
# This is the one counter here that is a heuristic rather than a pattern, and it is why
# `score()` accepts a callable. The test is a short sentence with no finite verb.
# Imperatives are complete sentences and pass; so are sentences carrying a subject pronoun
# or a quantifier subject. Headings, table cells, list items and citation lines are not
# scanned, because a bullet list of noun phrases is a list rather than prose.
#
# **What it cannot do is separate a main clause from a subordinate one.** "Sixty cards,
# every one a question you send a friend" is a fragment, and the `send` inside the
# relative clause hides it. Catching that needs a parser, and the limit is stated here
# rather than left to be found.
#
# Copied from `export/voice-kit/tools/voice_lint.py`, where it was written and where the
# product repos run it. That is backwards from every other counter here, which the kit
# copies FROM this file. When one changes, re-copy rather than re-derive.

AUX = set("""am is are was were be been isnt arent wasnt werent
has have had hasnt havent hadnt do does did dont doesnt didnt
will would shall should can could may might must wont wouldnt cant couldnt
shouldnt mustnt cannot lets ive youve weve theyve ill youll well theyll
im youre were theyre hes shes its thats theres heres
id hed shed wed youd theyd itd whod""".split())

# High-frequency verbs whose finite forms carry no visible inflection.
IRREG = set("""go goes went come comes came make makes made take takes took
get gets got give gives gave say says said see sees saw know knows knew
think thinks thought find finds found tell tells told become becomes became
run runs ran read reads keep keeps kept let leave leaves left put puts
mean means meant hold holds held write writes wrote send sends sent
sit sits sat stand stands stood cost costs need needs want wants ask asks
hit shut split spread cast quit bet beat upset bid rid burst
work works fail fails call calls open opens close closes carry carries carried
name names named cut cuts fit fits fix fixes hurt set sets show shows shot
buy buys bought bring brings brought choose chooses chose lose loses lost
pay pays paid meet meets met hear hears heard feel feels felt
draw draws drew break breaks broke speak speaks spoke""".split())

# An imperative is a complete sentence with no visible subject, and this repo is full of
# them: "Follow the flinch." "Serve the relationship." "Then wait." Checked in FIRST
# POSITION ONLY, so a noun use elsewhere still counts as a fragment ("A hard call.").
BASE_VERBS = set("""ask answer avoid begin bring build buy call carry check choose close
accept acknowledge act add allow answer apologise apologize apply argue assume audit
avoid breathe detect exhale execute inhale validate welcome
belong break
bring calm cancel change
claim collect commit compare come count cut decide describe do draw drop end explain fail find finish fix follow
confirm consider count cover define delete draft drop end explain extend
enter fill finish focus get give go grow guess handle hear help hold imagine
keep kill know learn leave let list listen live look lose love make mark match meet
mention message move name notice note
adjust deploy feel honor iterate learn locate observe offer open own pause pay perform
pick picture place play point refactor
post prefer prepare propose prove pull push put repeat
quote raise reach read realize record refuse remember remind remove repair repeat
replace return
reply return run save say see seek send serve set settle show sit skip solve sort
sound speak spend split stand start state stay stop suppose switch
plan prepare protect publish reach share simulate sort state store take talk tell
test think throw track treat try turn expect
use wait walk want watch weigh work write""".split())
# A sentence opening with a subject pronoun has a subject, and almost certainly a finite
# verb the inflection tests cannot see ("They also share a scene").
# Only unambiguous pronouns. "one", "this", "that" are determiners at least as often
# ("One sitting.", "This rule.") and listing them hides exactly the shape we are after.
SUBJ_PRONOUNS = set("i you we they he she it who".split())
# Quantifier subjects take an uninflected verb the same way a plural pronoun does
# ("Some happen in the external world", "Most people turn back"). Three words minimum,
# so "Some of them." and "Both true." stay flagged.
QUANT_SUBJ = set("some most many few several all both others each either neither none people\ntwo three four five six seven eight nine ten rest remainder".split())
ABBREV = re.compile(r"\b(?:Mr|Mrs|Ms|Dr|Prof|St|Jr|Sr|vs|etc|e\.g|i\.e|No|Fig|Vol|Ch|pp|p|[A-Z])\.\s")

BASE_VERBS |= set("""declare deliver deny design discuss earn edit engage ensure establish
examine expect face flag force gather grant hand hide hope host include invite join judge
lead limit log manage map measure mind miss model order pass permit plot praise press
promise prove provide publish question rate react refer reflect register reject release
remain rename repeat report request require reserve resist resolve respect respond rest
restore retain reveal review revise reward risk roll rule satisfy scan score search secure
select sell separate shape share shift ship sign sketch slow source spare spot spread
stack stage stick strike study submit suggest supply support surface survive swap sweep
tag tap target teach tend thank tie time touch trace trade train transfer translate
trigger trim trust tune type undo unlock update upgrade urge value vary verify view visit
vote wake warn wave wear welcome win wipe wish withdraw wonder worry wrap yield""".split())

LEAD_ADVERBS = set("""then now so first next also always never please instead again
still just only rather even simply here there today tomorrow""".split())

# -ing is never finite on its own ("One sitting.", "An evening") — only -ed and -s are.
INFLECTED = re.compile(r"(?:ed|es|s)$")
WORDRX = re.compile(r"[A-Za-z][A-Za-z'’-]*")
SKIPLINE = re.compile(r"^\s*(?:#{1,6}\s|\||[-*+]\s|\d+[.)]\s|!\[|\[!)")
LINKRX = re.compile(r"\[([^\]]*)\]\([^)]*\)")
MARKS = re.compile(r"~~|[*_]{1,3}|^\s*>\s?", re.M)


def _has_finite_verb(words):
    for w in words:
        w = w.lower().replace("'", "").replace("’", "")
        if w in AUX or w in IRREG:
            return True
        if len(w) > 3 and INFLECTED.search(w):
            return True
    return False


def fragments(text, max_words=12):
    """Yield (offset, sentence) for sentences with no finite verb.

    Markdown is hard-wrapped, so a sentence routinely spans several source lines and the
    tail of a wrapped sentence looks exactly like a fragment. Lines are therefore joined
    into paragraphs first, carrying an index map so the reported offset still points at
    the real character. Offsets are into `text`, so the caller's line_of() still works.
    """
    def scan(buf, idx):
        # "Ms. G, christine and Tasshin" must not split at the title.
        buf = ABBREV.sub(lambda m: m.group(0).replace(".", "\u0001"), buf)
        off = 0
        for sent in re.split(r"(?<=[.!?])\s+", buf):
            sent = sent.replace("\u0001", ".")
            here, off = off, off + len(sent) + 1
            sent = sent.strip()
            if not sent or not sent.endswith((".", "!", "?")):
                continue
            words = WORDRX.findall(sent)
            if not words or len(words) > max_words:
                continue
            if not re.search(r"[a-z]", sent):          # ALL-CAPS labels
                continue
            if re.match(r"^[\W\d]*§[\w.§\u2013-]*[\W]*$", sent):   # "§4d.", "§5b."
                continue
            # A blanked code span at the head of a sentence leaves it starting mid-clause
            # (", following Publishing Base v0.1..."), which is an artifact, not a fragment.
            if not re.match(r"^[\"\u201c\u2018'(\[]?[A-Z0-9]", sent):
                continue
            if "  " in sent:      # a blanked code span left a gap; the sentence is not whole
                continue
            if sent.count("(") != sent.count(")"):     # a split parenthetical
                continue
            head = [w.lower() for w in words]
            # A subject pronoun with anything after it almost always brings a finite verb
            # the inflection tests cannot see: "From there you play the next move cleanly",
            # "The rest of the time they interrupt."
            if any(w in SUBJ_PRONOUNS for w in head[:-1]):
                continue
            # A quantifier subject takes an uninflected verb the same way a plural
            # pronoun does, but only when a verb actually follows it: "the two look
            # identical" is a clause, "Two people at one keyboard" is not.
            if any(w in QUANT_SUBJ and head[i + 1] in (BASE_VERBS | IRREG)
                   for i, w in enumerate(head[:-1])):
                continue
            while head and head[0] in LEAD_ADVERBS:
                head.pop(0)
            if head and head[0] in BASE_VERBS:         # imperative
                continue
            if _has_finite_verb(words):
                continue
            yield idx[min(here, len(idx) - 1)], sent

    buf, idx, pos, skipping = "", [], 0, False
    for line in text.split("\n"):
        start, pos = pos, pos + len(line) + 1
        if not line.strip():
            for hit in scan(buf, idx):
                yield hit
            buf, idx, skipping = "", [], False
            continue
        # A citation line is a list of link titles, not prose. Two or more links and
        # little else outside them: skip it.
        if len(LINKRX.findall(line)) >= 2 and len(LINKRX.sub("", line).strip()) < 40:
            for hit in scan(buf, idx):
                yield hit
            buf, idx, skipping = "", [], True
            continue
        if SKIPLINE.match(line):
            for hit in scan(buf, idx):
                yield hit
            buf, idx, skipping = "", [], True
            continue
        # A wrapped list item continues on an indented line and is still list, not prose.
        # Without this, the tail of every wrapped bullet reads as a fragment.
        if skipping and line[:1].isspace():
            continue
        skipping = False
        clean = MARKS.sub("", LINKRX.sub(r"\1", line))
        # Rebuild the index map by locating each kept character in the source line.
        j = 0
        for ch in clean:
            k = line.find(ch, j)
            if k < 0:
                k = j
            idx.append(start + k)
            j = k + 1
        buf += clean
        buf += " "
        idx.append(start + len(line))
    for hit in scan(buf, idx):
        yield hit

class _Hit(object):
    """A regex-match-alike, so a callable counter reports like every other one."""

    def __init__(self, start, text):
        self._s, self._t = start, text

    def start(self):
        return self._s

    def end(self):
        return self._s + len(self._t)

    def group(self, _n=0):
        return self._t


def fragment_hits(text):
    return [_Hit(off, sent) for off, sent in fragments(text)]


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
    # Production tags — `**[DISSATISFACTION → SATISFACTION] …**`, `[TRANSLATE]`,
    # `[CONTROL]`. Added 2026-08-09 after Wendell read `[TRANSLATE]` on a printed
    # page: "this shouldn't be in the text. We spend a lot of time removing these
    # artifacts."
    #
    # **They were removed twice and came back twice, and neither loss was an
    # argument.** Ruled out 2026-06-03; the fix landed in the retired `chapters/`
    # tree while `manuscript/` became canon, and the acceptance grep only checked
    # the tree that had been fixed. Fixed again 2026-08-07 in `5ac778f`, which
    # took ch7 from 16 to 0 — and the merge that delivered it, `485d004`, had one
    # parent at 0 and one at 23 and kept the 23. The merge notes for that day
    # still say the tags were removed. They were; the merge put them back.
    #
    # A gate is the only form of this fix that survives a merge, because it fails
    # the build rather than trusting a checklist. It greps `manuscript/` and only
    # `manuscript/`, which is the lesson `SPEC_BRACKET_TAGS_2026-07-29.md` §2 drew
    # from the first loss.
    #
    # Scoped to a bracketed run of two or more capitals so ordinary bracketed
    # prose and single-letter references are untouched.
    ("prodtag", r'\[[A-Z][A-Z0-9 →/&—-]{1,40}\]', 0),
    ("fragment", fragment_hits, 0),
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
    # RETIRED 2026-08-07. Three CANON entries lived here exempting ch3's Move 5 from
    # the `thing` ban. Wendell, reversing the 2026-08-03 "option b, keep the move name"
    # ruling: "this should've already been ruled on and changed." The exemption was
    # holding the book's most-repeated banned word in place as its own move name, twice
    # in one title, while every other site in the manuscript was swept to zero. The move
    # is `Say the Unsaid Charge` now, which needs no exemption. ch3 already used "the
    # unsaid charge" three times for the same referent before the rename.
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
        hits = p(text) if callable(p) else re.finditer(p, text, f)
        out.append((n, [m for m in hits
                        if not any(a <= m.start() < b for a, b in skip)]))
    return out


def draft_surfaces(paths):
    """Score named files instead of the board.

    Added 2026-08-05. Until today `main` globbed the manuscript and silently
    discarded any path handed to it, so `gate.py somedraft.md` printed a verdict
    on the shipped book. Four domain sections were drafted against that reading
    before one of them checked. Same failure as the six board-only instruments
    `draftprobe.py` was built to wrap: an instrument that answers a question you
    did not ask is worse than one that refuses, because the answer looks fine.
    """
    surfaces = {}
    for p in paths:
        b, m = split_surfaces(io.open(p, encoding="utf-8").read())
        surfaces[os.path.basename(p)] = b
        if m.strip():
            surfaces[os.path.basename(p) + " (marginalia)"] = m
    return surfaces


def main():
    verbose = "-v" in sys.argv
    paths = [a for a in sys.argv[1:]
             if not a.startswith("-") and os.path.isfile(a)]
    if paths:
        return report(draft_surfaces(paths), verbose)

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

    return report(surfaces, verbose)


def report(surfaces, verbose):
    width = max([12] + [len(l) for l in surfaces])
    names = [n for n, _, _ in COUNTERS]
    print("%-*s %s" % (width, "surface", " ".join("%8s" % n for n in names)))
    print("-" * (width + 50))
    total = 0
    for label, text in surfaces.items():
        s = score(text)
        total += sum(len(ms) for _, ms in s)
        print("%-*s %s" % (width, label, " ".join("%8d" % len(ms) for _, ms in s)))
    print("-" * (width + 50))

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
