# -*- coding: utf-8 -*-
"""
Who is doing it — misattributed agency, measured.

    python3 instruments/agency.py                  # the board
    python3 instruments/agency.py -v               # every site
    python3 instruments/agency.py --write FILE     # the full report

## Why this exists

Wendell, 2026-08-01, reading Chapter 1: *"definitions don't ask things of people.
The book in general has a missattributed agent problem."* Nine of the twelve lines
he flagged in that batch are an abstraction performing a human act — guilt tells
you, allyship springs a trap, the question flips, the definition guards, the game
would rather you not notice, a book runs on guilt.

`prose_diet.py` has carried an `agency` check since July. Run against Chapter 1 it
returns **zero**. Its pattern needs a literal `the`, then one of twenty listed
nouns, then one of eighteen listed verbs — so it cannot see a bare abstract
subject (*Allyship springs the trap*), and its noun list does not contain the
abstractions this book is actually built from: guilt, shame, help, harm, damage,
definition, game, myth, trap. The check was not wrong so much as too small to
find anything, and it had been reporting clean for two weeks.

## What is measured

Real part-of-speech tags, not a word list. For each sentence the subject of the
main clause is found, its head noun classified, and the verb classified.

**Tier 1 — an inanimate subject with a mental or speech verb.** An abstraction
cannot want, tell, ask, decide, notice, refuse or prefer. Wendell's own test:
*"games can't want things like this."* These are defects, not metaphors.

**Tier 2 — an inanimate subject with a volitional physical verb.** *The trap
springs, the scoreboard goes dark.* Some of these are live metaphor and belong in
the book. Candidates, adjudicated by a reader.

**Tier 3 — the agentless rate.** The share of sentences with no animate subject at
all. This is Wendell's other question about *The help never lands*: **"where is
the agent in the sentence."** It is the number to watch, because it is the one
that ties this to the reading-cost finding.

## What it connects to

`density.py` measured 79% of sentence transitions opening on new information,
against 57% in the passages Wendell selected as the book at its best. A sentence
whose subject is an abstraction cannot pick up a person from the sentence before
it — there is no person in it. So misattributed agency is not a separate defect
from the integration cost. It is a mechanical cause of it, and this instrument
reports the correlation directly.
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

WORD = re.compile(r"[A-Za-z][A-Za-z'’-]*")

# Subjects that can act. Pronouns, and the human nouns this book uses.
ANIMATE = set("""i you we they he she me us them myself yourself ourselves who whoever
person people reader readers ally allies student students colleague colleagues
friend friends parent parents child children partner partners manager
teacher teachers head heads headmaster caretaker keeper somebody someone
anyone everyone nobody wendell jordan maera ash quill vale cross orr bram tull
architect challenger regent diplomat sage shaman player villager villagers
one
protector controller skeptic fixer healer victim daemon daemons
self body auditor referee
face faces
dana priya marcus nia sam rosa imani""".split())

# The seven daemons joined ANIMATE on 2026-08-03, ruled by Wendell. They were
# absent while the six Faces were present, which is the same class of subject:
# `ch2:248` defines a daemon as a part that runs on its own, and Section 7's
# whole walk is `The Protector has the joystick` seven times over. 39 of the
# 207 Tier-1 sites this instrument reported were that personification, so 19%
# of the book's headline agency number was the book working correctly.
# `self` and `body` are here for the Damaged Self and the Emotional Body, whose
# head noun is the second word.
#
# `auditor` and `referee` joined 2026-08-03 on the same reasoning: they are the
# Skeptic's and the Controller's names inside ch4 and ch3, used as often as the
# formal terms. `The auditor will tell you...` is a daemon speaking, not an
# abstraction acting.
#
# `face`/`faces` and the named people joined on the same ruling, 2026-08-03. The six
# Faces were already here by name and the generic word was not, so `the six Faces
# carries its own word` scored while `the Diplomat carries` did not. The named
# hypothetical people the Examples use -- Dana ch3:896, Priya ch4:632, Marcus
# ch5:607, Nia ch7:594, Sam ch8:630, Rosa ch9:528, Imani ch2 -- are people, and the
# gap stayed invisible only while no Example subject had a name: `imani` **want** at
# ch2:393 was the single new Tier 1 site across a day of added canon, and it was a
# false positive.

# An abstraction cannot hold a mental state or perform a speech act. Wendell's
# test: "games can't want things like this."
MENTAL = set("""want wants wanted wish wishes know knows knew think thinks thought
believe believes believed decide decides decided notice notices noticed
refuse refuses refused prefer prefers preferred expect expects expected
wonder wonders wondered intend intends intended mean means meant
tell tells told ask asks asked say says said promise promises promised
admit admits admitted insist insists insisted warn warns warned
argue argues argued claim claims claimed answer answers answered
remember remembers remembered forget forgets forgot care cares cared
agree agrees agreed""".split())

# Volitional physical acts. Legitimate as live metaphor, so reported as candidates.
VOLITIONAL = set("""spring springs sprung guard guards guarded hand hands handed
give gives gave take takes took hold holds held keep keeps kept
build builds built break breaks broke make makes made push pushes pushed
pull pulls pulled carry carries carried run runs ran teach teaches taught
protect protects protected invite invites invited demand demands demanded
offer offers offered send sends sent bring brings brought
score scores scored reward rewards rewarded punish punishes punished""".split())

BE = set("is are was were be been being am".split())


def head_of_subject(tags):
    """The head noun (or pronoun) of the main clause subject, and its verb.

    Walks to the first finite verb and takes the last nominal before it. Crude
    against relative clauses, which is why the rate matters more than any one hit.
    """
    subj = None
    for i, (tok, tag) in enumerate(tags):
        if tag in ("PRP", "NN", "NNS", "NNP", "NNPS"):
            subj = tok.lower()
        elif tag in ("VBZ", "VBP", "VBD", "MD"):
            if subj is None:
                return None, None
            # Step past a modal or auxiliary to the verb carrying the meaning.
            verb = tok.lower()
            for tok2, tag2 in tags[i + 1:]:
                if tag2.startswith("VB") and tok2.lower() not in BE:
                    verb = tok2.lower()
                    break
                if tag2 not in ("RB", "RBR", "RBS", "MD") and not tag2.startswith("VB"):
                    break
            return subj, verb
        elif tag in (",", ":", "IN", "WDT", "WP") and subj is not None:
            continue
    return subj, None


def classify(text, pos_tag, word_tokenize):
    toks = [t for t in word_tokenize(text) if WORD.match(t) or t in ",:"]
    if not toks:
        return None
    subj, verb = head_of_subject(pos_tag(toks))
    if subj is None:
        return None
    animate = subj in ANIMATE
    tier = None
    if not animate and verb:
        if verb in MENTAL:
            tier = 1
        elif verb in VOLITIONAL:
            tier = 2
    return {"subj": subj, "verb": verb, "animate": animate, "tier": tier}


def report(lines, verbose):
    pos_tag, word_tokenize = dn.tagger()
    if pos_tag is None:
        return ["Tagger unavailable — no report."]

    L, add = [], None
    L = []
    add = L.append

    body = dn.paragraphs(lines)
    per = defaultdict(lambda: {"n": 0, "animate": 0, "t1": [], "t2": []})
    all_sents = []
    for l in body:
        for s in dn.sentences(l["text"]):
            c = classify(s, pos_tag, word_tokenize)
            if not c:
                continue
            rec = per[l["rel"]]
            rec["n"] += 1
            if c["animate"]:
                rec["animate"] += 1
            if c["tier"] == 1:
                rec["t1"].append((l, s, c))
            elif c["tier"] == 2:
                rec["t2"].append((l, s, c))
            all_sents.append((l, s, c))

    tot = sum(v["n"] for v in per.values())
    anim = sum(v["animate"] for v in per.values())
    t1 = [x for v in per.values() for x in v["t1"]]
    t2 = [x for v in per.values() for x in v["t2"]]

    add("## 1 · The agentless rate")
    add("")
    add("The share of sentences whose main-clause subject is a person. Wendell's")
    add("question about *The help never lands* — **where is the agent in the")
    add("sentence** — asked of every sentence in the book.")
    add("")
    add("| | sentences | animate subject | agentless |")
    add("|---|---|---|---|")
    add("| **whole body** | %d | %d | **%.0f%%** |"
        % (tot, anim, 100.0 * (tot - anim) / tot if tot else 0))

    # The control, again Wendell's own.
    by_key = {(l["rel"], l["line"]): l for l in body}
    anchors = [by_key[k] for k in dn.ANCHOR if k in by_key]
    an, aa = 0, 0
    for l in anchors:
        for s in dn.sentences(l["text"]):
            c = classify(s, pos_tag, word_tokenize)
            if c:
                an += 1
                aa += 1 if c["animate"] else 0
    if an:
        add("| **the five voice anchors** | %d | %d | **%.0f%%** |"
            % (an, aa, 100.0 * (an - aa) / an))
    add("")

    add("## 2 · Tier 1 — an abstraction with a mental or speech verb")
    add("")
    add("An abstraction cannot want, tell, ask, decide or notice. These are defects.")
    add("")
    add("**%d sites.**" % len(t1))
    add("")
    for l, s, c in t1[:30 if not verbose else 400]:
        add("- `%s` **%s** · %s:%d" % (c["subj"], c["verb"], l["rel"], l["line"]))
        add("  > %s" % s[:170])
    add("")

    add("## 3 · Tier 2 — an abstraction with a volitional physical verb")
    add("")
    add("Live metaphor sometimes, defect sometimes. Candidates for a reader.")
    add("")
    add("**%d sites.**" % len(t2))
    add("")
    for l, s, c in t2[:20 if not verbose else 400]:
        add("- `%s` **%s** · %s:%d" % (c["subj"], c["verb"], l["rel"], l["line"]))
        add("  > %s" % s[:170])
    add("")

    add("## 4 · Per component")
    add("")
    spine = [rel for _, _, rel, _ in fl.bb.SPINE if rel]
    add("| Component | sentences | agentless | tier 1 | tier 2 |")
    add("|---|---|---|---|---|")
    for rel in sorted(per, key=lambda r: spine.index(r) if r in spine else 999):
        v = per[rel]
        add("| %s | %d | **%.0f%%** | %d | %d |"
            % (os.path.basename(rel), v["n"],
               100.0 * (v["n"] - v["animate"]) / v["n"] if v["n"] else 0,
               len(v["t1"]), len(v["t2"])))
    add("")

    # ------------------------------------------------- the correlation that matters
    add("## 5 · Does agency explain the reading cost?")
    add("")
    add("`density.py` found 79% of sentence transitions opening on new information.")
    add("If a sentence with no person in it cannot pick up a person from the sentence")
    add("before it, the two findings are one finding. Measured directly:")
    add("")
    gn_ani = gn_ani_t = gn_inan = gn_inan_t = 0
    for l in body:
        ss = dn.sentences(l["text"])
        for a, b in zip(ss, ss[1:]):
            c = classify(b, pos_tag, word_tokenize)
            if not c:
                continue
            head = dn.content(" ".join(WORD.findall(b)[:6]))
            if not head:
                continue
            new = not (head & dn.content(a))
            if c["animate"]:
                gn_ani_t += 1
                gn_ani += 1 if new else 0
            else:
                gn_inan_t += 1
                gn_inan += 1 if new else 0
    add("| Sentence subject | transitions | starts on new information |")
    add("|---|---|---|")
    if gn_ani_t:
        add("| a person | %d | **%.0f%%** |" % (gn_ani_t, 100.0 * gn_ani / gn_ani_t))
    if gn_inan_t:
        add("| not a person | %d | **%.0f%%** |" % (gn_inan_t, 100.0 * gn_inan / gn_inan_t))
    add("")
    return L


def main():
    verbose = "-v" in sys.argv
    out = None
    if "--write" in sys.argv:
        i = sys.argv.index("--write")
        out = sys.argv[i + 1] if i + 1 < len(sys.argv) else os.path.join(
            ROOT, "editorial_reports", "AGENCY_BOARD.md")
    header = [
        "# Misattributed agency — the board",
        "",
        "Generated by `instruments/agency.py`. Body prose only.",
        "",
        "Wendell named this pattern by reading Chapter 1: *\"definitions don't ask",
        "things of people. The book in general has a missattributed agent problem.\"*",
        "`prose_diet.py`'s existing agency check returns zero on that chapter.",
        "",
    ]
    text = "\n".join(header + report(fl.surfaces(), verbose)) + "\n"
    if out:
        os.makedirs(os.path.dirname(out), exist_ok=True)
        io.open(out, "w", encoding="utf-8").write(text)
        print("wrote %s" % os.path.relpath(out, ROOT))
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
