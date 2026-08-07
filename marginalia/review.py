#!/usr/bin/env python3
"""
review.py — MTGOA voice linter.

Implements the standing rules established 2026-07-28. Run BEFORE any draft is shown
to Wendell. Flags candidates; a human or a review agent adjudicates.

Repo-native port of the 2026-07-28 handoff's review.py. Three changes from the
original, all mechanical — every rule, pattern, and threshold is untouched:

  1. Default path is manuscript/, and chapter numbers resolve from ch{N}.md as
     well as the old CHAPTER{N} draft names.
  2. Body mode strips the marginalia blocks first and marginalia mode reads only
     them, so each surface gets its own numbers — the original ran its sentence-
     level regexes over both at once, which double-counted the margin against
     the body baseline.
  3. --anchors defaults to marginalia/insertions.py against manuscript/
     (compile.py --check performs the same test; both are kept so the handoff's
     loop runs as documented).

    python3 marginalia/review.py                            # body mode on manuscript/
    python3 marginalia/review.py --mode marginalia          # the margin only
    python3 marginalia/review.py --mode voice               # genre + flavor markers per Head
    python3 marginalia/review.py --anchors                  # verify anchor uniqueness

Exit code 1 if any BLOCK-severity finding. Nothing here is a hard rule; every finding
is a candidate. The rules are documented in specs/RULE_COLLISIONS.md and
specs/VOICE_SYNTHESIS.md; the voice profiles in specs/SEVEN_VOICES.md.
This linter finds candidates. The hard canon gate (banned words, And/But
openers, negation stacks) is instruments/gate.py, and its zeros are not
negotiable; the two tools are complementary, not alternatives.
"""
import re, sys, os, glob, argparse
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_MS = os.path.join(HERE, os.pardir, "manuscript")
DEFAULT_INSERTIONS = os.path.join(HERE, "insertions.py")
MARG_BLOCK = re.compile(
    r"\n?\n<!-- (MARGINALIA|EPIGRAPH-BYLINE|POSTCARD) -->\n.*?\n<!-- /\1 -->\n", re.S)

def chapter_num(name):
    m = re.search(r"(?:CHAPTER|\bch)(\d+)", name)
    return int(m.group(1)) if m else None

# ---------------------------------------------------------------- helpers

def sentences(text):
    text = re.sub(r"\s+", " ", text)
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]

def paragraphs(text):
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)          # strip insertion markers
    text = re.sub(r"^\s*[|>#\-*].*$", "", text, flags=re.M)      # tables, quotes, headings, lists
    return [p.strip() for p in re.split(r"\n\s*\n", text) if len(p.split()) > 25]

F = []
def flag(sev, rule, where, detail):
    F.append((sev, rule, where, detail))

HEDGES = r"\b(perhaps|somewhat|arguably|rather|fairly|quite|often|tends? to|generally|typically|might|maybe|sort of|kind of|in some sense|to some extent)\b"
MINIMIZERS = r"\b(simply|just|merely)\b"
# "say the noun" — a noun phrase that POINTS at something and never supplies it.
# Only fires when the phrase ENDS a sentence or is followed by a full stop / comma-clause,
# i.e. the reader is left holding it. "the thing that gets done" is fine; "the thing." is not.
VAGUE = [
    r"\bthe word\b\s*[.,;]",
    r"\bthe thing\b\s*[.,;]",
    r"\bone of these\b\s*[.,;]",
    r"\bthat feeling\b\s*[.,;]",
    r"\bthe result\b\s*[.,;]",
    r"\bsomething like that\b",
    r"\bthe honest (word|version|one)\b",
    r"\bthere was a \w+\.",              # "There was a committee." — gesture at an event
    r"\bfor (reasons|a while)\b\s*[.,;]",
    r"\bsomething (I|he|she|they) (?:had )?(?:never )?(?:said|did|knew)\b\s*[.,;]",
]
# Two exemptions on VAGUE, both added 2026-08-07 after adjudicating fourteen BLOCKs.
# Five of the fourteen were this rule firing on prose that supplies its referent, and a
# rule that cries wolf five times in fourteen is a rule nobody reads the output of.
#
# 1. `Say the Thing Under the Thing` is a NAMED MOVE, taught in ch3 and ch4. `gate.py`
#    carves it out in four places; this linter carved it nowhere, so the book's own
#    vocabulary read as the defect the vocabulary was invented to name. Same shape as
#    every other split-brain finding on this branch: the ruling lived in one instrument.
#
# 2. `the word` is a META-REFERENCE -- it points at a lexical item, not at a thing in the
#    world, and the item is almost always in the same sentence. The three live sites:
#    *"whether or not anybody in the space would use the word"*, *"Some of you are
#    resisting the word"*, *"the more expensive of the two, in every sense of the word"*.
#    In each the word being pointed at (allyship, Founder, expensive) is right there.
#    Discriminated on the naming verb rather than on a list of our own sentences, so it
#    generalises to the sentence nobody has written yet.
NAMED_MOVES = re.compile(r"say the thing under the thing", re.I)
META_WORD = re.compile(r"(?:\b(?:use[sd]?|using|say|says|said|call(?:s|ed)?|resist(?:s|ing|ed)?|"
                       r"hear[sd]?|writ(?:e|es|ten))\b[^.;]{0,40}|in every sense of\s+)$", re.I)


def vague_exempt(text, m):
    """True when a VAGUE hit supplies its own referent and is not a defect."""
    for nm in NAMED_MOVES.finditer(text):
        if nm.start() <= m.start() < nm.end():
            return True
    if re.match(r"\bthe word\b", m.group(0), re.I):
        head = text[max(0, m.start() - 60):m.start()]
        return bool(META_WORD.search(head))
    return False


# abstraction nouns most likely to sit in a subject slot
ABSTRACT = r"\b(conditioning|positionality|institutionalization|relationality|embodiment|intentionality|systemic\w*|structural\w*|accountability|awareness|engagement|alignment)\b"

# ---------------------------------------------------------------- voice profiles
# From claude_SEVEN_VOICES.md. Each treatise is a genre of in-world nonfiction; the
# markers below are the surface signatures that make the genre legible without
# telegraphing. Applies to Sections 1-3 (the treatise half) only.
#
# "require" = markers that should be PRESENT (absence is the finding)
# "forbid"  = markers that should be ABSENT
# rates are per 1,000 words

VOICES = {
    3: dict(name="Maera Voss", school="Body", genre="practitioner's casebook",
        flavor="Castaneda + Baba Yaga — withholds on purpose; the refusal is the teaching",
        require=[
            ("numbered observation", r"(?m)^\s*(?:\d+[.)]|#### \w*\s*\d)", 1),
            ("recorded wrong reading", r"\b(I (was|had been) wrong|it was not|I recorded \w+\. It)", 1),
            ("sensation noun", r"\b(jaw|chest|throat|shoulders|breath|stomach|hands|spine)\b", 3),
            ("refusal to name", r"\b(I will not tell you|I am not going to say|you would take the word)\b", 1),
        ],
        forbid=[("should", r"\byou should\b", 2)]),

    4: dict(name="Corin Ash", school="Line", genre="drill manual",
        flavor="Worf / Sisko / Tigh — conviction that has been paid for",
        require=[
            ("imperative opener", r"(?m)^(?:State|Say|Do not|Draw|Stop|Again|Hold|Run)\b", 3),
            ("self-interruption", r"\b(Objection|You will say|They will tell you|I am not guessing)\b", 1),
            ("stated cost", r"\b(cost me|six years|it cost|I was told)\b", 1),
        ],
        forbid=[("hedge particle", HEDGES, 1)]),

    5: dict(name="Sera Quill", school="Oath", genre="annotated charter",
        flavor="McGonagall / Brienne — upholds the institution and will burn a rule",
        require=[
            ("numbered clause", r"(?i)\b(clause|article|section) (?:\w+|\d+)\b", 2),
            ("citation of prior practice", r"(?i)\b(as held|under \w+|it has been kept|recorded here|the practice as)\b", 1),
            ("written vs kept", r"(?i)\b(as written|as kept|intact|passed named)\b", 1),
        ],
        forbid=[("contemporary vocabulary", r"(?i)\b(email|calendar|meeting|Slack|onboarding|KPI|rota)\b", 1)]),

    6: dict(name="Irix Vale", school="Pattern", genre="engineering monograph",
        flavor="an engineer who talks about buildings the way people talk about friends",
        require=[
            ("figure reference", r"(?i)\b(see figure|figure \w+|the diagram (above|below))\b", 1),
            ("in practice", r"(?i)\bin practice\b", 2),
            ("stated tolerance", r"(?i)\b(holds (up to|to about)|fails (past|above|beyond)|specified at)\b", 1),
        ],
        forbid=[]),

    7: dict(name="Elian Cross", school="Bridge", genre="negotiation casebook",
        flavor="Picard + Deanna Troi — earned principle; reads the field; overridden and offers anyway",
        require=[
            ("case marker", r"(?i)(?m)^\**Case\b|\bcase (?:one|two|three|\d+)\b", 1),
            ("direct quotation", r'(?:said|heard|meant)[:,]?\s*[\"\u201c\*]', 2),
            ("both protections named", r"(?i)\b(each of them was protecting|what (?:she|he|they) (?:was|were) protecting|both sides)\b", 1),
        ],
        forbid=[]),

    8: dict(name="Thalen Orr", school="Horizon", genre="commentary on the other five",
        flavor="Aguefort / Last Jedi Luke / Iroh — mercurial, warm, deflects toward himself",
        require=[
            ("cites another school", r"\b(Corin|Maera|Sera|Irix|Elian|the (Line|Body|Oath|Pattern|Bridge))\b", 2),
            ("courteous disagreement", r"(?i)\b(would say|is right within|which is the qualification|and yet)\b", 1),
        ],
        forbid=[]),
}


def check_voice(text, where, ch):
    v = VOICES.get(ch)
    if not v:
        return
    words = max(len(text.split()), 1)
    for label, pat, per_k in v["require"]:
        n = len(re.findall(pat, text))
        rate = n * 1000 / words
        if rate < per_k:
            flag("WARN", f"voice[{v['name']}] missing marker", where,
                 f"{label}: {n} ({rate:.1f}/1k, want >={per_k}) — genre={v['genre']}")
    for label, pat, per_k in v["forbid"]:
        n = len(re.findall(pat, text, re.I))
        rate = n * 1000 / words
        if rate > per_k:
            flag("BLOCK", f"voice[{v['name']}] forbidden marker", where,
                 f"{label}: {n} ({rate:.1f}/1k, max {per_k})")
    if not any(re.search(p, text) for _, p, _ in v["require"]):
        flag("BLOCK", f"voice[{v['name']}] genre absent", where,
             f"no marker of '{v['genre']}' found — reads as house voice, not as {v['name']}")


def treatise_half(text):
    """Sections 1-3 only. The treatise is in-world; Section 4+ is Wendell."""
    m = re.search(r"\n## Section 4", text)
    return text[:m.start()] if m else text

# ---------------------------------------------------------------- rules

# Denying negation, general form: a negated predicate followed by the same
# subject restated positively. The two narrow patterns below key on the literal
# strings "it's not" and "isn't the", which is why "The test is not X. The test
# is Y" — the same shape in different words — went undetected through 2026-07-29,
# including in ch7's five live stopping conditions and in the form three source
# specs prescribed for reuse. Excludes "not just/only/merely", which is ranking
# negation and licensed by RULE_COLLISIONS.
_SUBJ = (r"(?:It|That|There|This|The\s+[\w'’]+(?:\s+[\w'’]+){0,3}"
         r"|[A-Z][\w'’]+(?:\s+[\w'’]+){0,3})")
DENYING_GENERAL = (
    rf"\b{_SUBJ}\s*(?:'s|’s|\s+is|\s+are|\s+was|\s+were|n'?t)\s+not\s+"
    rf"(?!just\b|only\b|merely\b|even\b|always\b)"
    rf"[^.;!?]{{3,80}}[.;!?—]\s*"
    rf"(?:It'?s|That'?s|They|The\s+[\w'’ ]{{2,28}}\s+is|It\s+is|That\s+is|they\s+were|it\s+is|they\s+are)\b")
# The em-dash in the separator class above was added 2026-07-29. The earlier
# pattern required a full stop, so "X is not A — it is B" was invisible to it.
# 22 instances were sitting in the manuscript unflagged.

AI_SHAPES = [
    (DENYING_GENERAL, "denying negation (X is not A. X is B)"),
    (r"(?i)\bit'?s not\s+[^.;]{3,40}[.;]\s*(it'?s|that'?s)\b", "denying negation (It's not X. It's Y)"),
    (r"(?i)\bnot\s+(just|only|merely)\s+[^,;.]{3,50},\s*but\b", "not-just-but construction"),
    # Widened 2026-07-29: the narrow form required which-is-the/a/what/why/how and
    # let ", which is easy to mistake for" through my own pre-flight. It caught both
    # the comma-tail and the sentence-initial fragment, since ". Which is its own
    # kind of problem." had been slipping past a comma-anchored rule.
    #
    # Widened again 2026-07-30, ruled a blocker by Wendell. The verb slot was still
    # is/was/are/were, so the tic went undetected the moment it wore a different
    # verb. Three went into the author's note on three consecutive review rounds —
    # `which describes`, `which should`, `which is` — and only the last was visible
    # to this instrument. The other two were caught by reading, which is exactly the
    # work an instrument exists to stop doing. Against the shipping surfaces the
    # count goes 22 -> 79, with no case the old pattern caught and this one misses.
    #
    # The tic is `which` acting as the SUBJECT of a clause that comments on what
    # precedes it. Three guards separate that from ordinary English, and all three
    # sit ahead of the \w+ so backtracking cannot dodge one — an earlier attempt put
    # the question guard after \w+, and the engine matched "Which ar" so the
    # lookahead would pass.
    #
    #   1. no question. "Which daemon had the joystick?" is the chapter asking.
    #   2. no embedded question. "which channel you are running" is a noun clause.
    #   3. no following subject. "the house, which he had built" is a relative
    #      clause where `which` is the object, and is not the tic.
    #
    # Guard 2 would also swallow "which means you are not holding an archetype",
    # a real tail, so the common tail verbs are whitelisted ahead of it and bypass
    # it. Missing a tail is the failure this widening exists to fix; a false
    # positive only costs an adjudication, and this rule is a WARN.
    (r"(?i)(?:,\s*|(?<=[.!?])\s+)which\s+"
     r"(?![^.!?]{0,90}\?)"
     r"(?:"
     r"(?:is|was|are|were|means|meant|makes|made|gives|gave|leaves|left|has|had"
     r"|helps|helped|hands|handed|turns|keeps|kept|costs|lets|allows|requires"
     r"|involves|includes|suggests|explains|describes|sounds|looks|becomes"
     r"|comes|came|should|would|could|will|may|might|can|does|did|do)\b"
     r"|"
     r"(?![\w-]+\s+(?:you|we|they|I|he|she|it)\b)"
     r"(?!(?:he|she|it|they|we|i|you|the|a|an|his|her|their|its|my|our|your"
     r"|anyone|someone|everyone|nobody|of|one|ever|way|kind|sort|type|other"
     r"|two|three|four|five|six|twenty)\b)"
     r"\w+"
     r")", "appositive 'which' tail"),
    (r"(?i)\bisn'?t (?:about|the) [^.;]{3,40}[.;]\s*(it'?s|that'?s)\b", "denying negation variant"),
    (r"(?i)\bin a world where\b", "AI opener"),
    (r"(?i)\bat the end of the day\b", "filler idiom"),
    (r"(?i)\b(?:the|a) (?:profound|powerful|beautiful) (?:truth|realization|insight)\b", "constructed profundity"),
]

def check_prose(text, where, mode):
    paras = paragraphs(text)
    words = len(text.split())
    if not paras:
        return

    # --- AI-shape patterns
    for pat, name in AI_SHAPES:
        for m in re.finditer(pat, text):
            sev = "BLOCK" if "denying negation" in name else "WARN"
            flag(sev, name, where, m.group(0)[:70].replace("\n", " "))

    # --- say the noun
    for pat in VAGUE:
        for m in re.finditer(pat, text, re.I):
            if vague_exempt(text, m):
                continue
            ctx = text[max(0, m.start()-40):m.end()+40].replace("\n", " ")
            flag("BLOCK", "say the noun", where, "…" + ctx.strip() + "…")

    # --- hedge density (per 1k words)
    h = len(re.findall(HEDGES, text, re.I))
    if words and h * 1000 / words > 6:
        flag("WARN", "hedge density", where, f"{h} hedges, {h*1000/words:.1f}/1k words (target <6)")

    # --- minimizers
    mz = len(re.findall(MINIMIZERS, text, re.I))
    if words and mz * 1000 / words > 4:
        flag("INFO", "minimizer density", where, f"{mz} ({mz*1000/words:.1f}/1k) — check for defensive use")

    # --- three consecutive long sentences
    for p in paras:
        ss = sentences(p)
        run = 0
        for s in ss:
            run = run + 1 if len(s.split()) > 25 else 0
            if run >= 3:
                flag("WARN", "3 consecutive sentences >25 words", where, s[:70] + "…")
                break

    # --- abstraction noun in subject position
    for p in paras:
        for s in sentences(p):
            head = " ".join(s.split()[:5])
            if re.search(ABSTRACT, head, re.I):
                flag("WARN", "abstraction noun in subject slot", where, s[:70] + "…")

    # --- punchline last: final sentence should not be the longest
    for p in paras:
        ss = sentences(p)
        if len(ss) >= 3:
            lens = [len(s.split()) for s in ss]
            if lens[-1] == max(lens) and lens[-1] > sum(lens) / len(lens) * 1.6:
                flag("INFO", "paragraph ends on its longest sentence", where, ss[-1][:70] + "…")

    # --- sentence-length variance
    allsents = [len(s.split()) for p in paras for s in sentences(p)]
    if len(allsents) > 12:
        mean = sum(allsents) / len(allsents)
        var = sum((x - mean) ** 2 for x in allsents) / len(allsents)
        if var ** 0.5 < 5:
            flag("WARN", "low sentence-length variance", where,
                 f"sd={var**0.5:.1f} (target >5) — no drum hits")

    # --- em-dash density (AI tell)
    em = text.count("—")
    if words and em * 1000 / words > 12:
        flag("INFO", "em-dash density", where, f"{em} ({em*1000/words:.1f}/1k)")

    # --- marginalia-specific
    if mode == "marginalia":
        for note in re.findall(r"<!-- MARGINALIA -->(.*?)<!-- /MARGINALIA -->", text, re.S):
            n = len(note.split())
            if n > 160:
                flag("WARN", "note over length", where, f"{n} words (norm 60-120)")
            if n < 25:
                flag("INFO", "very short note", where, f"{n} words")


def check_moves(text, where):
    moves = len(re.findall(r"^### Move ", text, re.M))
    tests = len(re.findall(r"\*\*The test:\*\*", text))
    if moves and tests < moves:
        flag("BLOCK", "moves without stopping condition", where,
             f"{moves} moves, {tests} tests — {moves-tests} missing")


def check_anchors(insertions_path, chapter_dir):
    sys.path.insert(0, os.path.dirname(os.path.abspath(insertions_path)) or ".")
    import insertions as I
    files = {}
    for f in glob.glob(os.path.join(chapter_dir, "*.md")):
        n = chapter_num(os.path.basename(f))
        if n is not None:
            files[n] = f
    for ch, rows in I.NOTES.items():
        if ch not in files:
            flag("WARN", "anchor check", f"ch{ch}", "chapter file not found"); continue
        # Strip the frame before counting: Rule 2 makes every note grab a phrase
        # from the prose beside it, so on an applied manuscript the anchor text
        # legitimately appears twice — once in the body, once quoted in the note.
        txt = MARG_BLOCK.sub("", open(files[ch]).read())
        # ch8's rows carry a third field, the signature, because in that chapter the
        # margin changes hands and six people sign what they wrote. Every other chapter
        # is a 2-tuple. Unpacking exactly two crashed check_anchors on ch8 from the day
        # the signatures landed (2026-07-30) until this was found on 2026-08-01, which
        # meant test_toolchain.py had been dying before its last assertion ran.
        for row in rows:
            anchor = row[0]
            n = txt.count(anchor)
            if n != 1:
                flag("BLOCK", "anchor not unique", f"ch{ch}",
                     f"{n} occurrences: {anchor[:50]}")

# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path", nargs="?", default=DEFAULT_MS,
                    help="file or directory of .md (default: manuscript/)")
    ap.add_argument("--mode", default="body", choices=["body", "marginalia", "voice"])
    ap.add_argument("--anchors", nargs="?", const=DEFAULT_INSERTIONS,
                    metavar="INSERTIONS_PY",
                    help="verify anchor uniqueness against a chapter dir")
    a = ap.parse_args()

    if a.anchors:
        check_anchors(a.anchors, a.path if a.path != DEFAULT_MS else DEFAULT_MS)
    else:
        paths = ([a.path] if os.path.isfile(a.path)
                 else sorted(glob.glob(os.path.join(a.path, "**", "*.md"), recursive=True)))
        for p in paths:
            t = open(p, encoding="utf-8").read()
            w = os.path.basename(p)
            if a.mode == "voice":
                ch = chapter_num(w)
                if ch is None:
                    continue
                if ch not in VOICES:
                    flag("INFO", "voice", w, "no profile (Ch2 = Caretaker, Ch9 = student)")
                    continue
                check_voice(treatise_half(MARG_BLOCK.sub("", t)), w, ch)
            elif a.mode == "marginalia":
                marg = "\n\n".join(
                    m.group(0) for m in re.finditer(
                        r"<!-- (MARGINALIA|EPIGRAPH-BYLINE|POSTCARD) -->\n.*?\n<!-- /\1 -->",
                        t, re.S))
                if marg:
                    check_prose(marg.replace("\n> ", "\n").replace("\n>", "\n"), w, a.mode)
            else:
                check_prose(MARG_BLOCK.sub("", t), w, a.mode)
                check_moves(t, w)

    order = {"BLOCK": 0, "WARN": 1, "INFO": 2}
    F.sort(key=lambda x: (order[x[0]], x[2], x[1]))
    counts = Counter(f[0] for f in F)

    if not F:
        print("clean — no findings"); return 0

    cur = None
    for sev, rule, where, detail in F:
        if (sev, where) != cur:
            cur = (sev, where); print(f"\n[{sev}] {where}")
        print(f"    {rule}: {detail}")

    print("\n" + "-" * 66)
    print(f"BLOCK {counts['BLOCK']}   WARN {counts['WARN']}   INFO {counts['INFO']}")
    print("""
BLOCK = fix before showing Wendell.
WARN  = look at it; may be correct.
INFO  = pattern data, not a defect.

Nothing here is automatic. Denying negations pass if the negated thing is STILL TRUE
when the sentence ends (ranking), and fail if it was set up to be knocked down (denying).
Vague nouns pass only if the noun is named within two sentences.
""")
    return 1 if counts["BLOCK"] else 0

if __name__ == "__main__":
    sys.exit(main())
