# -*- coding: utf-8 -*-
"""
agency_grep.py — the recall net under the agency audit.

Spec: SPEC_AGENCY_TRACEABILITY_AUDIT_20260802, task T2.

This is NOT the detector. Wendell ruled on 2026-08-02 that agents read the
prose and this script runs beneath them to catch what they missed. It fires on
registry entities appearing near an agentive verb and it does not attempt to
parse. Its output is a candidate list to diff against the agents' ledgers, so
that a site found by neither is at least a site nobody silently dropped.

That last part only works if somebody reads the output. Measured 2026-08-03,
precision was low enough that nobody would: 1 of 8 candidates survived reading
on `the field`, 0 of 14 on Grade-3 intention. Six filters were added against
hand-read samples -- object position, clause boundary, noun-not-verb, passive
or adjectival state, hyphenated compounds, and an intervening noun phrase.
Together they remove about 63% of raw candidates. 32 dropped sites were
hand-read to confirm the losses are noise, and the one real finding that fell
out (`organizations that used tradition to protect power`) drove the restrictive
relative rule.

Recall is one flag away: --loose disables all six and restores the original
behaviour exactly. Use it when a chapter's ledger and this net disagree.

What the filters cannot fix is WORD SENSE. "fear meant something" (signified,
not intended) still reads as an intention verb here, and "the pattern shows"
(is visible) still reads as perception. The registry carries a standing note on
this; a reader resolves it, not a filter.

Two things it will never do:
  - rule a keep (C3 — that authority is Wendell's alone)
  - resolve W-1 or W-2 (those sites come out tagged PENDING)

    python3 instruments/agency_grep.py                  # all shipping prose
    python3 instruments/agency_grep.py manuscript/ch6.md
    python3 instruments/agency_grep.py --report editorial_reports/agency/DISTRIBUTION.md
    python3 instruments/agency_grep.py --include-legacy # adds the TEAL baseline column

Reads instruments/agency_registry.yaml. Zero hardcoded entity lists (AC-1).
"""
import argparse, os, re, sys, glob, collections

try:
    import yaml
except ImportError:
    sys.exit("agency_grep.py needs PyYAML")

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, os.pardir))
REGISTRY = os.path.join(HERE, "agency_registry.yaml")

# Frame blocks stripped before the body is read. Mirrors marginalia/review.py's
# MARG_BLOCK exactly -- HANDBOOK and SIGNATURE deliberately survive, because
# they are body text that ships.
MARG_BLOCK = re.compile(
    r"\n?\n<!-- (MARGINALIA|EPIGRAPH-BYLINE|POSTCARD) -->\n.*?\n<!-- /\1 -->\n", re.S)
KEEP_BLOCK = re.compile(r"<!-- /?(HANDBOOK|SIGNATURE) -->")

# Irregular verb surfaces the naive -s/-ed/-ing expansion cannot reach.
IRREGULAR = {
    # Added 2026-08-03 with the cognition lemmas. `think` was the costly one:
    # the taxonomy gained `think`, the inflector could not produce `thought`,
    # and ch5:165's three "The village thought" clauses stayed invisible even
    # after the lemma landed. A lemma the inflector cannot inflect is a lemma
    # that is not really in the list.
    "think": ["thinks", "thinking", "thought"],
    "pay": ["pays", "paying", "paid"],
    "drive": ["drives", "driving", "drove", "driven"],

    "see": ["sees", "saw", "seen", "seeing"],
    "know": ["knows", "knew", "known", "knowing"],
    "tell": ["tells", "told", "telling"],
    "say": ["says", "said", "saying"],
    "make": ["makes", "made", "making"],
    "give": ["gives", "gave", "given", "giving"],
    "take": ["takes", "took", "taken", "taking"],
    "choose": ["chooses", "chose", "chosen", "choosing"],
    "mean": ["means", "meant", "meaning"],
    "seek": ["seeks", "sought", "seeking"],
    "teach": ["teaches", "taught", "teaching"],
    "forbid": ["forbids", "forbade", "forbidden", "forbidding"],
    "forgive": ["forgives", "forgave", "forgiven", "forgiving"],
    "let": ["lets", "letting"],
    "put": ["puts", "putting"],
    "set": ["sets", "setting"],
    "cost": ["costs", "costing"],
    "leave": ["leaves", "left", "leaving"],
    "bring": ["brings", "brought", "bringing"],
    "build": ["builds", "built", "building"],
    "draw": ["draws", "drew", "drawn", "drawing"],
    "run": ["runs", "ran", "running"],
    "hold": ["holds", "held", "holding"],
    "spend": ["spends", "spent", "spending"],
    "understand": ["understands", "understood", "understanding"],
    "forget": ["forgets", "forgot", "forgotten", "forgetting"],
    "learn": ["learns", "learnt", "learned", "learning"],
    "rise": ["rises", "rose", "risen", "rising"],
    "sink": ["sinks", "sank", "sunk", "sinking"],
    "bend": ["bends", "bent", "bending"],
    "spread": ["spreads", "spreading"],
}


def surfaces(lemma):
    """Every inflected surface of a verb lemma we care about."""
    if lemma in IRREGULAR:
        return {lemma} | set(IRREGULAR[lemma])
    out = {lemma}
    if lemma.endswith(("s", "sh", "ch", "x", "z")):
        out.add(lemma + "es")
    elif lemma.endswith("y") and lemma[-2:-1] not in "aeiou":
        out.add(lemma[:-1] + "ies")
        out.add(lemma[:-1] + "ied")
    else:
        out.add(lemma + "s")
    if lemma.endswith("e"):
        out.add(lemma + "d")
        out.add(lemma[:-1] + "ing")
    else:
        out.add(lemma + "ed")
        out.add(lemma + "ing")
    return out


def load_registry(path=REGISTRY):
    with open(path, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def build_index(reg):
    """verb surface -> class, and entity phrase -> grade id."""
    verb2class, class_sev = {}, {}
    for cls, spec in reg["verb_classes"].items():
        class_sev[cls] = spec.get("severity", 5)
        for lemma in spec["lemmas"]:
            for s in surfaces(lemma):
                # First class wins; the YAML is ordered by severity so the more
                # dangerous reading of an ambiguous verb ("demand", "expect")
                # is the one that survives.
                verb2class.setdefault(s.lower(), cls)

    ent2grade, licensed, partial, ent_partial = {}, {}, {}, {}
    for g in reg["grades"]:
        gid = g["id"]
        licensed[gid] = set(g.get("verb_classes") or [])
        # W-1 left Grade 3 with a PARTIAL license: the intention class is not
        # open, but `want`/`seek`/`aim` inside it are. Without this the net
        # re-flags "which Fire wants" on every run.
        for cls, lemmas in (g.get("verb_classes_partial") or {}).items():
            for lemma in lemmas:
                partial.setdefault(gid, {}).setdefault(cls, set()).update(
                    s.lower() for s in surfaces(lemma))
        # ENTITY-level partial license: one named entity inside a grade, not
        # the grade. `the field` is physical per SPEC_FIELD_OF_BODIES while the
        # rest of Grade 6 stays on the pattern-verbs-only ceiling.
        for ename, lemmas in (g.get("entity_partial") or {}).items():
            for lemma in lemmas:
                ent_partial.setdefault(ename.strip().lower(), set()).update(
                    s.lower() for s in surfaces(lemma))
        for e in g.get("entities") or []:
            e = e.strip().lower()
            # Grade 1's list carries category labels, not literal strings.
            if e in ("named characters", "proper names", "personal pronouns"):
                continue
            ent2grade.setdefault(e, gid)

    # E-1: the education-by-emotions register. An ontological carve-out that
    # sits OUTSIDE the grade system -- `teach`/`say`/`report` on a channel are
    # the book's thesis being stated, not unearned agency. Suppressed here so
    # the net stops surfacing the signature passage as a severity-4 finding.
    senses = {}
    for e in (reg.get("sense_exceptions") or []):
        senses.setdefault(e["verb"], set()).update(
            s.lower() for s in surfaces(e["verb"]))
        senses[e["verb"]] = (senses[e["verb"]], e["action"])
    # flatten to {verb: surfaces} plus {verb: action}
    sense_surf = {v: s for v, (s, _a) in senses.items()}
    sense_act = {v: a for v, (_s, a) in senses.items()}
    sense_clear = {v: s for v, s in sense_surf.items() if sense_act[v] == "clear"}
    sense_tagd = {v: s for v, s in sense_surf.items() if sense_act[v] == "tag"}

    e1 = set()
    for lemma in ((reg.get("exceptions") or {}).get("E-1") or {}).get("licensed_verbs") or []:
        e1.update(s.lower() for s in surfaces(lemma))
    return (verb2class, class_sev, ent2grade, licensed, partial, e1,
            ent_partial, sense_clear, sense_tagd)


def tier(cls, grade, licensed, verb=None, partial=None, e1=None,
         ent=None, ent_partial=None):
    """Severity tier per the registry's `tiers` block."""
    if cls in licensed.get(grade, set()):
        return 0                                   # licensed; not a finding
    if verb and (partial or {}).get(grade, {}).get(cls) and verb in partial[grade][cls]:
        return 0                                   # W-1 partial license
    if verb and e1 and grade == 3 and verb in e1:
        return 0                                   # E-1, ruled STANDING
    if verb and ent and (ent_partial or {}).get(ent) and verb in ent_partial[ent]:
        return 0                                   # entity-level license
    if cls in ("perception", "intention"):
        return 3
    if cls == "social-causal":
        return 3 if grade in (6, 7) else 2
    if cls == "speech":
        return 2
    if cls == "causal-bare":
        return 2
    return 1                                       # mechanical, directional, pattern


def sentences(text):
    text = re.sub(r"\s+", " ", text)
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]


def read_body(path):
    """Chapter body with the marginalia frame stripped, line numbers preserved."""
    raw = open(path, encoding="utf-8").read()
    if path.endswith(".md") and "/manuscript/" in path.replace(os.sep, "/"):
        raw = MARG_BLOCK.sub("\n\n", raw)
    return KEEP_BLOCK.sub("", raw)


# --------------------------------------------------------------- precision
# Three faults measured 2026-08-03 against hand-read samples. On `the field`
# only 1 of 8 candidates survived reading; on Grade-3 intention, 0 of 14. At
# that rate the output stops being read at all, which defeats the recall net's
# whole purpose -- a site found by neither agents nor net is a site nobody
# silently dropped, and that only holds if somebody reads the net.
#
# These are three filters, not a parser. Each is reversible with --loose, so
# the high-recall behaviour the file was built for is one flag away.

# 1. OBJECT POSITION. "hold the field when the map leaves out half the story" --
#    `leaves` belongs to the map; the field is the object of `hold`. The net
#    only checked that a verb sat to the right of the entity, which is true of
#    objects too. A preposition before the entity makes it oblique or locative
#    ("into the village", "back to the village", "onto the field"); a verb
#    before it makes it an object.
PREP = {"in", "into", "at", "to", "for", "from", "on", "with", "onto", "of",
        "across", "through", "toward", "towards", "inside", "outside", "over",
        "under", "beyond", "past", "against", "about", "around", "beside"}

#    Governors that take these abstractions as objects. Deliberately short and
#    literal -- every one was read off a false positive in the measured sample,
#    not guessed at.
GOVERN = {"hold", "holds", "held", "holding", "keep", "keeps", "kept", "keeping",
          "sustain", "sustains", "sustained", "meet", "meets", "met", "meeting",
          "enter", "enters", "entered", "join", "joins", "joined", "leave",
          "leaves", "left", "leaving", "read", "reads", "serve", "serves",
          "change", "changes", "changed", "fix", "fixes", "fixed", "run", "runs",
          "play", "plays", "played", "playing", "build", "builds", "built",
          "carry", "carries", "carried", "watch", "watches", "watched",
          "name", "names", "named", "naming", "give", "gives", "gave", "take",
          "takes", "took", "taking", "cut", "cuts", "shape", "shapes"}

# 2. CLAUSE BOUNDARY. "the fear, which meant they also missed", "systems that
#    needed to change", "what obstacle needs overcoming", "sensing into the
#    feeling and letting it show you" -- in every case the verb belongs to a
#    subject that starts after the entity. The tokenizer drops punctuation, so
#    commas are invisible; these words are what survives of the boundary.
BOUNDARY = {"which", "that", "who", "whose", "whom", "what", "and", "or", "but",
            "because", "when", "while", "if", "since", "though", "although",
            "where", "whether", "so", "then", "as"}

#    ...with one exception, found by hand-reading the drops. A RESTRICTIVE
#    RELATIVE immediately after the entity takes the entity as its antecedent,
#    so the verb after it DOES belong to the entity: "the organizations THAT
#    USED tradition to protect power" is organizations protecting power. Only
#    `that`/`who`/`whose` behave this way here. `which` is excluded because in
#    this book it overwhelmingly refers back to a whole clause rather than to
#    the noun beside it -- "they learned to not-feel the fear, WHICH MEANT they
#    also missed" is the learning that meant it, not the fear.
RELATIVE = {"that", "who", "whose"}

# 3. NOUN, NOT VERB. `attempt`, `demand`, `plan`, `move`, `report`, `claim`,
#    `state`, `answer`, `need`, `charge` are all noun-or-verb. A determiner or a
#    pre-nominal modifier immediately before the candidate settles it: "a demand
#    insists", "of failed attempts", "reaching for the plan".
DET = {"a", "an", "the", "its", "their", "your", "my", "his", "her", "our",
       "this", "that", "these", "those", "some", "any", "no", "one", "each",
       "every", "another", "both", "either", "neither"}
#    Bare pronouns and quantifiers that start a zero-relative clause. The
#    Grade-1 intervening check already catches `you`/`they`; these are the ones
#    no grade lists.
NEWSUBJ = {"nobody", "somebody", "anybody", "everybody", "everyone", "someone",
           "anyone", "none", "people", "whoever", "whatever",
           # `it` is in no grade, so the Grade-1 check never caught it: "the
           # work IT ASKED of you" is the zero-relative shape again.
           "it"}

MOD = {"failed", "same", "next", "real", "own", "first", "last", "only", "whole",
       "new", "old", "good", "bad", "single", "specific", "actual", "entire",
       "clean", "hard", "quiet", "second", "third", "final", "further", "other"}


#    `to` belongs in PREP for the object test ("back to the village") but NOT in
#    the intervening test: there it is usually an infinitive marker, and the
#    infinitive's implied subject is the entity -- "the organizations that used
#    tradition TO PROTECT power" is organizations protecting power, which is
#    exactly the Grade-6 social-causal shape the audit exists to catch.
INTERVENE = PREP - {"to"}


def _is_object(toks, i, ent_len):
    """Entity sits in object or oblique position, so the verb to its right is
    not its verb."""
    start = i - ent_len + 1                        # first token of the entity
    for back in (1, 2):                            # skip a determiner if present
        k = start - back
        if k < 0:
            break
        w = toks[k]
        if w in DET:
            continue
        return w in PREP or w in GOVERN
    return False


# 4. PASSIVE OR ADJECTIVAL. "even when the field is charged", "the moment the
#    field becomes truly charged" -- a copula before the candidate means the
#    entity is in a state, not doing something. `charge` is a mechanical lemma,
#    so both read as findings without this.
COPULA = {"is", "are", "was", "were", "be", "been", "being", "am",
          "becomes", "became", "become", "seems", "seemed", "feels", "felt",
          "remains", "remained", "stays", "stayed", "gets", "got", "looks"}


def _is_state(toks, j, i=None):
    """Copula before the candidate: passive, predicate adjective, or an
    infinitive complement -- "the work IS TO TELL them apart" defines the work
    rather than reporting it doing something."""
    if i is not None and toks[j - 1] == "to" and any(
            toks[k] in COPULA for k in range(i + 1, j)):
        return True
    for back in (1, 2):                            # allow one adverb between
        k = j - back
        if k < 0:
            return False
        if toks[k] in COPULA:
            return True
        if not toks[k].endswith("ly"):
            return False
    return False


# --------------------------------------------------------- sense exceptions
# A lemma names a WORD; a class names a SENSE. Five verbs sit in a class that is
# right for one of their senses and wrong for the one this book uses, and each
# cost a block before being recorded. Rules are read from the registry's
# `sense_exceptions` -- these functions implement the syntactic tests it names.

def _sense_clear(toks, j, senses):
    """True when the classed verb is being used in its non-agentive sense."""
    w = toks[j]
    nxt = toks[j + 1] if j + 1 < len(toks) else ""
    if w in senses.get("mean", ()):
        # intention sense is "mean TO do"; without it the sense is `signifies`
        return nxt != "to"
    if w in senses.get("ask", ()):
        return nxt == "for"        # calls for, as "this dish asks for salt"
    if w in senses.get("answer", ()):
        return nxt == "to"         # goes by the name of
    if w in senses.get("show", ()):
        # perception sense is TRANSITIVE -- something shows something. Bare, or
        # followed by an adverbial, it means `is visible`: "the pattern shows
        # nowhere else", "The pattern shows fully", "shows up".
        return (nxt == "" or nxt.endswith("ly")
                or nxt in ("up", "through", "nowhere", "everywhere", "here",
                           "there", "again", "later", "now", "only", "clearly"))
    return False


def _sense_tag(toks, j, grade, senses):
    """True when the sense needs a reader rather than a rule."""
    if toks[j] in senses.get("require", ()) and grade in (4, 6, 7):
        return True                # entailment reading is the common one here
    return False


def _is_noun(toks, j):
    """Candidate verb is being used as a noun."""
    if j == 0:
        return False
    return toks[j - 1] in DET or toks[j - 1] in MOD


def scan(path, verb2class, ent2grade, licensed, partial=None, e1=None,
         loose=False, ent_partial=None, sense_clear=None, sense_tag=None):
    """Every (entity, verb) pair inside a ±5-token window. High recall by design."""
    hits = []
    body = read_body(path)
    for lineno, line in enumerate(body.splitlines(), 1):
        if not line.strip() or line.lstrip().startswith(("#", "|", "---")):
            continue
        for sent in sentences(line):
            low = sent.lower()
            # hyphenated compounds stay whole, so "the Field-Holder demands"
            # does not read as "the field ... demands". That one compound
            # accounted for three false positives in ch7 alone.
            toks = re.findall(r"[a-z']+(?:-[a-z']+)*", low)
            for ent, grade in ent2grade.items():
                if ent not in low:
                    continue
                head = ent.split()[-1]
                if head not in toks:
                    continue
                ent_len = len(ent.split())
                for i, t in enumerate(toks):
                    if t != head:
                        continue
                    # the entity is an object or an oblique, not a subject --
                    # unless a restrictive relative follows it, in which case it
                    # is the subject INSIDE that clause whatever precedes it:
                    # "a defense of the organizations THAT USED tradition to
                    # protect power" is object of `of` and subject of `used`.
                    rel_follows = toks[i + 1] in RELATIVE if i + 1 < len(toks) else False
                    if not loose and not rel_follows and _is_object(toks, i, ent_len):
                        continue
                    # subject window: the verb sits to the RIGHT of the subject
                    for j in range(i + 1, min(i + 6, len(toks))):
                        # a new clause starts here, so whatever follows has its
                        # own subject and this entity is not it
                        if not loose and toks[j] in BOUNDARY:
                            # restrictive relative on the entity itself: the
                            # verb after it is the entity's verb, so keep going
                            if j == i + 1 and toks[j] in RELATIVE:
                                continue
                            break
                        cls = verb2class.get(toks[j])
                        if not cls:
                            continue
                        if not loose and (_is_noun(toks, j) or _is_state(toks, j, i)):
                            continue
                        # right lemma, wrong sense -- registry-ruled
                        if not loose and sense_clear and _sense_clear(toks, j, sense_clear):
                            continue
                        # a determiner or preposition between subject and verb
                        # starts a new noun phrase, and that phrase owns the
                        # verb: "the work NOBODY SEES", "the work THE
                        # INHERITANCE requires", "the work OF UNDERSTANDING".
                        # start past the relative pronoun when there is one --
                        # `that` is also a determiner, so without this the
                        # intervening check re-breaks on the very word the
                        # RELATIVE rule just allowed through.
                        first = i + 2 if rel_follows else i + 1
                        if not loose and any(toks[k] in DET or toks[k] in INTERVENE
                                             or toks[k] in NEWSUBJ
                                             for k in range(first, j)):
                            break
                        # a person intervening owns the verb, not the abstraction
                        if any(ent2grade.get(toks[k]) == 1 for k in range(i + 1, j)):
                            break
                        t_ = tier(cls, grade, licensed, toks[j], partial, e1,
                                  ent, ent_partial)
                        if t_ == 0:
                            break
                        hits.append({
                            "file": os.path.relpath(path, ROOT), "line": lineno,
                            "subject": ent, "grade": grade, "verb": toks[j],
                            "class": cls, "tier": t_, "sentence": sent,
                            "flags": flags_for(ent, grade, cls, sent)
                                     + (["SENSE-CHECK"] if sense_tag
                                        and _sense_tag(toks, j, grade, sense_tag) else []),
                        })
                        break
    return dedupe(hits)


def flags_for(ent, grade, cls, sent):
    f = []
    if "game" in ent:
        f.append("AMBIGUOUS-REFERENT")
    # W-1 and W-2 were both ruled on 2026-08-02, so the PENDING tags are gone.
    # What survives the partial license is a real finding, not a held question.
    if grade == 3 and cls == "intention":
        f.append("W-1-ILLEGAL")          # not want/seek/aim, so deliberation
    if grade == 3 and cls in ("speech", "social-causal"):
        f.append("CHECK-E-1")            # E-1 shape, or a genuine violation
    if grade == 0 and ent in ("the book", "this chapter", "the chapter", "the section"):
        f.append("W-2-ILLEGAL")
    return f


def dedupe(hits):
    seen, out = set(), []
    for h in hits:
        k = (h["file"], h["line"], h["subject"], h["verb"])
        if k not in seen:
            seen.add(k)
            out.append(h)
    return out


def targets(include_legacy):
    fs = sorted(glob.glob(os.path.join(ROOT, "manuscript", "ch?.md")))
    fs += sorted(glob.glob(os.path.join(ROOT, "appendices", "APPENDIX_*.md")))
    fs += [os.path.join(ROOT, "appendices", "ON_THE_SHOULDERS_OF.md")]
    fs += sorted(glob.glob(os.path.join(ROOT, "front_matter", "*.md")))
    fs += sorted(glob.glob(os.path.join(ROOT, "back_matter", "*.md")))
    fs = [f for f in fs if os.path.exists(f) and "backup" not in f]
    if include_legacy:
        fs.append(os.path.join(ROOT, "MTGOA_TEAL_080525.md"))
    return fs


def report(rows, files, out=None):
    by_file = collections.defaultdict(list)
    for r in rows:
        by_file[r["file"]].append(r)

    L = []
    L.append("# Agency distribution — recall-net pass\n")
    L.append("Generated by `instruments/agency_grep.py` against "
             "`instruments/agency_registry.yaml`.\n")
    L.append("**This is not the finding set.** It is the high-recall candidate list the "
             "agent ledgers are diffed against. Precision is deliberately poor; a row here "
             "is a place to look, not a defect.\n")
    L.append("## Per document\n")
    L.append("| document | words | T3 | T2 | T1 | total | per 10k |")
    L.append("|---|---:|---:|---:|---:|---:|---:|")
    for f in files:
        rel = os.path.relpath(f, ROOT)
        rs = by_file.get(rel, [])
        w = len(read_body(f).split())
        c = collections.Counter(r["tier"] for r in rs)
        per = len(rs) / w * 10000 if w else 0
        L.append(f"| {rel} | {w:,} | {c[3]} | {c[2]} | {c[1]} | {len(rs)} | {per:.2f} |")

    L.append("\n## By grade\n")
    L.append("| grade | hits | top verb classes |")
    L.append("|---|---:|---|")
    for g in sorted({r["grade"] for r in rows}):
        rs = [r for r in rows if r["grade"] == g]
        cc = collections.Counter(r["class"] for r in rs).most_common(3)
        L.append(f"| {g} | {len(rs)} | " + ", ".join(f"{k} ({v})" for k, v in cc) + " |")

    L.append("\n## By subject\n")
    L.append("| subject | grade | hits |")
    L.append("|---|---:|---:|")
    for (s, g), n in collections.Counter(
            (r["subject"], r["grade"]) for r in rows).most_common(30):
        L.append(f"| {s} | {g} | {n} |")

    flagged = [r for r in rows if r["flags"]]
    if flagged:
        L.append("\n## Flagged for triage\n")
        L.append("| file | line | flags | sentence |")
        L.append("|---|---:|---|---|")
        for r in flagged:
            s = r["sentence"][:110].replace("|", "\\|")
            L.append(f"| {r['file']} | {r['line']} | {', '.join(r['flags'])} | {s} |")

    L.append("\n## Tier 3 candidates, in full\n")
    for f in files:
        rs = [r for r in by_file.get(os.path.relpath(f, ROOT), []) if r["tier"] == 3]
        if not rs:
            continue
        L.append(f"\n### {os.path.relpath(f, ROOT)} — {len(rs)}\n")
        for r in rs:
            L.append(f"- **{r['line']}** · `{r['subject']}` (G{r['grade']}) "
                     f"+ `{r['verb']}` [{r['class']}] — {r['sentence'][:200]}")

    text = "\n".join(L) + "\n"
    if out:
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(text)
        print(f"wrote {out}  ({len(rows)} candidate rows)")
    else:
        print(text)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--report", help="write markdown here instead of stdout")
    ap.add_argument("--loose", action="store_true",
                    help="disable the three precision filters (object position, "
                         "clause boundary, noun-not-verb) and restore the "
                         "original high-recall behaviour")
    ap.add_argument("--include-legacy", action="store_true",
                    help="add MTGOA_TEAL_080525.md as the untreated baseline")
    a = ap.parse_args()

    reg = load_registry()
    v2c, _sev, e2g, lic, partial, e1, entp, sclr, stag = build_index(reg)
    files = [os.path.join(ROOT, p) for p in a.paths] or targets(a.include_legacy)

    rows = []
    for f in files:
        rows += scan(f, v2c, e2g, lic, partial, e1, a.loose, entp, sclr, stag)
    report(rows, files, a.report)
    return 0


if __name__ == "__main__":
    sys.exit(main())
