# -*- coding: utf-8 -*-
"""
The readability pass — difficulty spikes, rhythm, and cohesion, against this book.

    python3 instruments/readability.py                # the board
    python3 instruments/readability.py -v             # every site
    python3 instruments/readability.py --write FILE   # the full report

## Why this does not try to make the book easier

The obvious readability pass runs a formula, finds a grade level, and simplifies
until the number comes down. That would be the wrong pass for this manuscript, and
the repository already has the measurement that says so.

`specs/MANUSCRIPT_FILE_CANON.md` records MTGOA at **Flesch 73.7, grade 6.3**
against *Igniting Joy* — Wendell's own book, the control — at **50.7 and 10.6**.
The book is already far easier than the writer's established voice.
`SPEC_REPETITION_AND_CUTS` ruled the short-declarative register **drift, not
voice**, with 19.4% of sentences at six words or fewer against the control's 4.2%.

So a pass that pushed the grade level down would be automating the defect.

## What the formulas are worth, and what they miss

Flesch-Kincaid and its relatives measure two surface proxies — word length and
sentence length — and were built before anyone could compute the rest. The
literature is blunt about the consequence: they ignore cohesion, semantics and
pragmatics, and a *more* cohesive text can score as *harder* while reading easier.
Graesser and McNamara's Coh-Metrix work is the standard reply, scaling text on
five dimensions instead of one: narrativity, syntactic simplicity, word
concreteness, referential cohesion, and deep (causal) cohesion.

Two of those five are computable here without a psycholinguistic database, and
they are the two that matter for a book like this one:

**Referential cohesion** — content words shared between neighbouring paragraphs.
Where the overlap falls to nothing, the reader is bridging a gap the prose did not
build. That is a real stumble, and no formula sees it.

**Deep cohesion** — the density of causal, contrastive and temporal connectives.
Low density means the logic is there and unmarked, so the reader has to infer the
joins.

## The findings that are actually actionable

**Difficulty spikes, not averages.** A book at grade 6.3 with one paragraph at
grade 16 has one readability defect, and the average hides it. Every paragraph is
scored against the book's own median, and the outliers are the report.

**Monotony, which is this book's version of the problem.** The research on prose
rhythm treats constant sentence length as the defect — long or short, either one
tires a reader. So the counter here is not mean length but **runs**: four or more
consecutive sentences of six words or fewer is a rhythm a reader can hear.

Everything is reported against the book's own distribution. Nothing is rewritten.
"""
import io, os, re, sys, math, importlib.util
from collections import defaultdict, Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)
LETTER = "front_matter/headmasters_letter.md"


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

SENT = re.compile(r"(?<=[.!?])\s+")
WORD = re.compile(r"[A-Za-z][A-Za-z'’-]*")

# Connectives, by the job they do. Coh-Metrix's deep-cohesion dimension counts
# causal, intentional and temporal links; these are the surface markers of them.
CONNECTIVES = {
    "causal": r"\b(because|since|therefore|so that|as a result|consequently|"
              r"which is why|that is why|hence|thus)\b",
    "contrastive": r"\b(but|however|although|though|whereas|yet|instead|"
                   r"rather than|on the other hand|even so)\b",
    "temporal": r"\b(then|after|before|until|while|once|meanwhile|"
                r"by the time|as soon as)\b",
    "additive": r"\b(and also|moreover|furthermore|in addition|besides)\b",
}

# Words too common to count as a shared topic between two paragraphs.
STOP = set("""a an the and or but if then than that this these those of to in on at by for with
from as is are was were be been being it its it's you your yours i me my we our us they them
their he she his her not no nor do does did done have has had will would can could should may
might must so such about into over under out up down off just only very more most some any
what which who whom when where why how all both each few other own same too also there here
one two three four five six seven eight nine ten""".split())


def syllables(word):
    """Vowel-group count with the usual corrections. Good enough for a formula."""
    w = word.lower().strip("'’-")
    if not w:
        return 0
    groups = re.findall(r"[aeiouy]+", w)
    n = len(groups)
    if w.endswith("e") and not w.endswith(("le", "ee", "ye")) and n > 1:
        n -= 1
    if w.endswith(("les", "le")) and len(w) > 2 and w[-3] not in "aeiouy":
        n += 0
    return max(1, n)


def measure(text):
    sents = [s for s in SENT.split(text.strip()) if s.strip()]
    words = WORD.findall(text)
    if not sents or not words:
        return None
    syl = [syllables(w) for w in words]
    nw, ns, nsyl = len(words), len(sents), sum(syl)
    poly = sum(1 for s in syl if s >= 3)
    letters = sum(len(w) for w in words)

    asl = nw / ns
    asw = nsyl / nw
    flesch = 206.835 - 1.015 * asl - 84.6 * asw
    fk = 0.39 * asl + 11.8 * asw - 15.59
    fog = 0.4 * (asl + 100.0 * poly / nw)
    smog = 1.0430 * math.sqrt(poly * (30.0 / ns)) + 3.1291 if ns else 0
    coleman = 0.0588 * (letters * 100.0 / nw) - 0.296 * (ns * 100.0 / nw) - 15.8
    ari = 4.71 * (letters / nw) + 0.5 * asl - 21.43
    return {"words": nw, "sents": ns, "asl": asl, "asw": asw,
            "flesch": flesch, "fk": fk, "fog": fog, "smog": smog,
            "coleman": coleman, "ari": ari, "poly_pct": 100.0 * poly / nw,
            "lengths": [len(WORD.findall(s)) for s in sents]}


def content_words(text):
    return {w.lower() for w in WORD.findall(text)
            if w.lower() not in STOP and len(w) > 3}


def median(xs):
    xs = sorted(xs)
    n = len(xs)
    if not n:
        return 0.0
    return xs[n // 2] if n % 2 else (xs[n // 2 - 1] + xs[n // 2]) / 2.0


def paragraphs(lines):
    """Body prose only. Headings, list items, and table rows are not paragraphs."""
    out = []
    for l in lines:
        t = l["text"].strip()
        if not t or t.startswith(("#", "|", ">", "- ", "* ", ":::")) or re.match(r"^\d+\.\s", t):
            continue
        if len(WORD.findall(t)) < 25:          # too short to score meaningfully
            continue
        out.append(l)
    return out


def surface_of(l):
    return "letter" if l["rel"] == LETTER else l["surface"]


def report(lines, verbose):
    L, add = [], None
    L = []
    add = L.append

    body = [l for l in paragraphs(lines) if surface_of(l) == "body"]
    scored = []
    for l in body:
        m = measure(l["text"])
        if m:
            scored.append((l, m))

    # ---------------------------------------------------------------- whole book
    whole = measure("\n".join(l["text"] for l in body))
    add("## 1 · The formulas, for the record")
    add("")
    add("Six formulas on the body prose. They agree with each other because they")
    add("measure the same two things — word length and sentence length. None of them")
    add("sees cohesion, which is the [documented reason](https://www.tandfonline.com/doi/full/10.1080/10888438.2024.2422365)")
    add("a more cohesive text can score harder and read easier.")
    add("")
    add("| Measure | MTGOA body | *Igniting Joy* (control) | Reading |")
    add("|---|---|---|---|")
    add("| Flesch Reading Ease | **%.1f** | 50.7 | higher = easier |" % whole["flesch"])
    add("| Flesch-Kincaid grade | **%.1f** | 10.6 | US school grade |" % whole["fk"])
    add("| Gunning Fog | **%.1f** | — | years of education |" % whole["fog"])
    add("| SMOG | **%.1f** | — | years of education |" % whole["smog"])
    add("| Coleman-Liau | **%.1f** | — | US school grade |" % whole["coleman"])
    add("| Automated Readability | **%.1f** | — | US school grade |" % whole["ari"])
    add("| Mean sentence length | **%.1f** | 17.9 | words |" % whole["asl"])
    add("| Polysyllabic words | **%.1f%%** | — | 3+ syllables |" % whole["poly_pct"])
    add("")
    add("The control figures come from `specs/MANUSCRIPT_FILE_CANON.md`, which")
    add("measured *Igniting Joy* through the same pipeline. **The book is easier than")
    add("its own author's voice, by four grade levels.** That is the context for")
    add("everything below: the work is not to bring these numbers down.")
    add("")

    # -------------------------------------------------------- difficulty spikes
    # A one-sentence paragraph makes every formula report the paragraph's whole
    # length as its average sentence length, so a 77-word colon list came back at
    # grade 30. That is a long *sentence*, which §7 already owns. Spikes are scored
    # on paragraphs with something to average.
    multi = [(l, m) for l, m in scored if m["sents"] >= 2]
    singles = sorted([(m["words"], l) for l, m in scored
                      if m["sents"] == 1 and m["words"] >= 40], key=lambda r: -r[0])
    fks = [m["fk"] for _, m in multi]
    med, hi = median(fks), sorted(fks)[int(len(fks) * 0.97)] if fks else 0
    add("## 2 · Difficulty spikes — the actionable finding")
    add("")
    add("Every body paragraph scored against the book's own median of **%.1f**." % med)
    add("A reader does not stumble on an average; she stumbles on the one paragraph")
    add("that is four grades harder than the ones around it.")
    add("")
    spikes = sorted([(m["fk"], l, m) for l, m in multi if m["fk"] >= hi],
                    key=lambda r: -r[0])
    add("Scored on the %d paragraphs that have two or more sentences. Top of the "
        "distribution — %d at or above the 97th percentile (grade %.1f):"
        % (len(multi), len(spikes), hi))
    add("")
    for fkv, l, m in spikes[:14 if not verbose else 200]:
        add("- **grade %.1f** · %s:%d — %d words, %d sentence(s), mean %.0f words"
            % (fkv, l["rel"], l["line"], m["words"], m["sents"], m["asl"]))
        add("  > %s…" % l["text"][:150].strip())
    add("")

    add("### Paragraphs that are one long sentence")
    add("")
    add("A separate class, and a real one: the paragraph and the sentence are the")
    add("same unit, so the reader gets no landing between them.")
    add("")
    add("**%d body paragraphs are a single sentence of 40 words or more.**" % len(singles))
    add("")
    for n, l in singles[:10 if not verbose else 100]:
        add("- **%d words, one sentence** · %s:%d" % (n, l["rel"], l["line"]))
        add("  > %s…" % l["text"][:130].strip())
    add("")

    # ------------------------------------------------------------------- rhythm
    add("## 3 · Rhythm — runs, not averages")
    add("")
    add("Prose-rhythm research treats *constant* sentence length as the defect,")
    add("short or long. This book's version is the short run. A counter on mean")
    add("length cannot see it, so this counts consecutive sentences of six words or")
    add("fewer, which is what a reader hears.")
    add("")
    # Not every run is drift. `Shaman. Challenger. Regent. Architect.` is a roster,
    # and `You know what you feel. You know where you stand.` is anaphora — both are
    # devices a writer chose, and reporting them as monotony would be telling
    # Wendell his best rhetorical move is a defect. A run counts as a device when
    # the short sentences share an opening word, or when most of them are two words
    # or fewer. Everything else is the drift the register spec named.
    def classify(sents):
        firsts = [WORD.findall(s)[0].lower() for s in sents if WORD.findall(s)]
        if not firsts:
            return "drift"
        top = Counter(firsts).most_common(1)[0][1]
        if top >= max(2, int(0.6 * len(firsts))):
            return "anaphora"
        if sum(1 for s in sents if len(WORD.findall(s)) <= 2) >= 0.6 * len(sents):
            return "roster"
        return "drift"

    runs = []
    for l, m in scored:
        sents = [s for s in SENT.split(l["text"]) if s.strip()]
        cur = []
        for s, n in zip(sents, m["lengths"]):
            if n <= 6:
                cur.append(s)
            else:
                if len(cur) >= 4:
                    runs.append((len(cur), l, classify(cur)))
                cur = []
        if len(cur) >= 4:
            runs.append((len(cur), l, classify(cur)))
    runs.sort(key=lambda r: -r[0])
    kinds = Counter(k for _, _, k in runs)
    add("**%d paragraphs carry a run of four or more short sentences** — "
        "%d drift, %d anaphora, %d roster."
        % (len(runs), kinds["drift"], kinds["anaphora"], kinds["roster"]))
    add("")
    add("The drift ones are the finding. The other two are devices, listed after.")
    add("")
    for kind in ("drift", "anaphora", "roster"):
        sel = [r for r in runs if r[2] == kind]
        if not sel:
            continue
        add("**%s — %d**" % (kind, len(sel)))
        for n, l, _ in sel[:8 if not verbose else 200]:
            add("- **%d in a row** · %s:%d" % (n, l["rel"], l["line"]))
            add("  > %s…" % l["text"][:150].strip())
        add("")

    lens = [n for _, m in scored for n in m["lengths"]]
    mean = sum(lens) / float(len(lens)) if lens else 0
    sd = math.sqrt(sum((x - mean) ** 2 for x in lens) / len(lens)) if lens else 0
    add("Sentence length across the body: mean **%.1f**, median **%.0f**, "
        "SD **%.1f**, coefficient of variation **%.2f**."
        % (mean, median(lens), sd, sd / mean if mean else 0))
    add("")
    add("| Band | Share |")
    add("|---|---|")
    for lo, hi_, name in ((0, 6, "≤6 words — the short run"),
                          (7, 14, "7–14"), (15, 25, "15–25 — the explaining band"),
                          (26, 40, "26–40"), (41, 999, "41+ — check these by ear")):
        share = 100.0 * sum(1 for x in lens if lo <= x <= hi_) / len(lens)
        add("| %s | %.1f%% |" % (name, share))
    add("")

    # ------------------------------------------------- referential cohesion
    add("## 4 · Referential cohesion — where the thread drops")
    add("")
    add("Content-word overlap between each paragraph and the one before it, within a")
    add("chapter. Coh-Metrix calls this referential cohesion: shared words and ideas")
    add("form the thread a reader follows. Where the overlap is zero, she is bridging")
    add("a gap the prose did not build.")
    add("")
    # A heading between two paragraphs is a topic change the reader was told about,
    # so zero overlap across one is the structure working rather than a dropped
    # thread. Without this filter the check reported 194 gaps, and the first
    # handful were all section breaks.
    heads = defaultdict(set)
    for l in lines:
        if l["text"].lstrip().startswith("#"):
            heads[l["rel"]].add(l["line"])

    def head_between(rel, a, b):
        return any(a < n < b for n in heads[rel])

    gaps = []
    by_file = defaultdict(list)
    for l, m in scored:
        by_file[l["rel"]].append(l)
    overlaps = []
    per_file = defaultdict(list)
    for rel, ls in by_file.items():
        for a, b in zip(ls, ls[1:]):
            if b["line"] - a["line"] > 6 or head_between(rel, a["line"], b["line"]):
                continue
            ca, cb = content_words(a["text"]), content_words(b["text"])
            if not ca or not cb:
                continue
            ov = len(ca & cb) / float(min(len(ca), len(cb)))
            overlaps.append(ov)
            per_file[rel].append(ov)
            if ov == 0.0:
                gaps.append((rel, a, b))
    add("Mean overlap **%.2f** across %d adjacent pairs, headings excluded. "
        "**%d pairs share no content word at all.**"
        % (sum(overlaps) / len(overlaps) if overlaps else 0, len(overlaps), len(gaps)))
    add("")
    add("Per component, lowest first — a component well under the book's mean is the")
    add("one to read for thread, rather than any single pair:")
    add("")
    add("| Component | pairs | mean overlap |")
    add("|---|---|---|")
    for rel in sorted(per_file, key=lambda r: sum(per_file[r]) / len(per_file[r])):
        vals = per_file[rel]
        add("| %s | %d | %.2f |" % (os.path.basename(rel), len(vals),
                                    sum(vals) / len(vals)))
    add("")
    add("The individual zero-overlap pairs:")
    add("")
    for rel, a, b in gaps[:12 if not verbose else 200]:
        add("- %s:%d → :%d" % (rel, a["line"], b["line"]))
        add("  > …%s" % a["text"][-90:].strip())
        add("  > %s…" % b["text"][:90].strip())
    add("")

    # ------------------------------------------------------------ deep cohesion
    add("## 5 · Deep cohesion — connective density per chapter")
    add("")
    add("Causal, contrastive and temporal markers per thousand words. Low density")
    add("means the logic is present and unmarked, and the reader supplies the joins.")
    add("")
    add("| Chapter | words | causal | contrastive | temporal | total /1k |")
    add("|---|---|---|---|---|---|")
    spine_order = [rel for _, _, rel, _ in fl.bb.SPINE if rel]
    ordered = sorted(by_file, key=lambda r: spine_order.index(r)
                     if r in spine_order else 999)
    for rel in ordered:
        blob = "\n".join(l["text"] for l in by_file[rel])
        nw = len(WORD.findall(blob))
        counts = {k: len(re.findall(p, blob, re.I)) for k, p in CONNECTIVES.items()}
        tot = sum(counts.values())
        add("| %s | %d | %.1f | %.1f | %.1f | **%.1f** |"
            % (os.path.basename(rel), nw,
               1000.0 * counts["causal"] / nw, 1000.0 * counts["contrastive"] / nw,
               1000.0 * counts["temporal"] / nw, 1000.0 * tot / nw))
    add("")

    # --------------------------------------------------------- long paragraphs
    add("## 6 · Paragraph length outliers")
    add("")
    wlens = [m["words"] for _, m in scored]
    pmed = median(wlens)
    big = sorted([(m["words"], l) for l, m in scored], key=lambda r: -r[0])
    add("Median body paragraph is **%.0f words**. The longest:" % pmed)
    add("")
    for n, l in big[:10 if not verbose else 60]:
        add("- **%d words** (%.1f× median) · %s:%d" % (n, n / pmed, l["rel"], l["line"]))
    add("")

    # ------------------------------------------------------------ long sentences
    add("## 7 · Sentences over 45 words")
    add("")
    longs = []
    for l, m in scored:
        for s in SENT.split(l["text"]):
            n = len(WORD.findall(s))
            if n >= 45:
                longs.append((n, l, s.strip()))
    longs.sort(key=lambda r: -r[0])
    add("**%d sentences run 45 words or longer.** At this length a reader is holding "
        "the opening in memory while the clause resolves." % len(longs))
    add("")
    for n, l, s in longs[:12 if not verbose else 200]:
        add("- **%d words** · %s:%d" % (n, l["rel"], l["line"]))
        add("  > %s" % s[:190])
    add("")
    return L


def main():
    verbose = "-v" in sys.argv
    out = None
    if "--write" in sys.argv:
        i = sys.argv.index("--write")
        out = sys.argv[i + 1] if i + 1 < len(sys.argv) else os.path.join(
            ROOT, "editorial_reports", "READABILITY_BOARD.md")

    lines = fl.surfaces()
    header = [
        "# Readability board",
        "",
        "Generated by `instruments/readability.py` against the printed body prose.",
        "The margin and the Headmaster's letter are excluded: they are other people's",
        "voices and are scored on their own terms elsewhere.",
        "",
        "**This pass does not try to make the book easier.** It is already four grade",
        "levels easier than *Igniting Joy*, the author's own control text. See §1.",
        "",
    ]
    text = "\n".join(header + report(lines, verbose)) + "\n"
    if out:
        os.makedirs(os.path.dirname(out), exist_ok=True)
        io.open(out, "w", encoding="utf-8").write(text)
        print("wrote %s" % os.path.relpath(out, ROOT))
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
