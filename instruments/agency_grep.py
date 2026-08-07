# -*- coding: utf-8 -*-
"""
agency_grep.py — the recall net under the agency audit.

Spec: SPEC_AGENCY_TRACEABILITY_AUDIT_20260802, task T2.

This is NOT the detector. Wendell ruled on 2026-08-02 that agents read the
prose and this script runs beneath them to catch what they missed. It is
deliberately high-recall and low-precision: it fires on every registry entity
that appears near an agentive verb, and it does not attempt to parse. Its
output is a candidate list to diff against the agents' ledgers, so that a site
found by neither is at least a site nobody silently dropped.

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

    ent2grade, licensed, partial = {}, {}, {}
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
    e1 = set()
    for lemma in ((reg.get("exceptions") or {}).get("E-1") or {}).get("licensed_verbs") or []:
        e1.update(s.lower() for s in surfaces(lemma))
    return verb2class, class_sev, ent2grade, licensed, partial, e1


def tier(cls, grade, licensed, verb=None, partial=None, e1=None):
    """Severity tier per the registry's `tiers` block."""
    if cls in licensed.get(grade, set()):
        return 0                                   # licensed; not a finding
    if verb and (partial or {}).get(grade, {}).get(cls) and verb in partial[grade][cls]:
        return 0                                   # W-1 partial license
    if verb and e1 and grade == 3 and verb in e1:
        return 0                                   # E-1, ruled STANDING
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


def scan(path, verb2class, ent2grade, licensed, partial=None, e1=None):
    """Every (entity, verb) pair inside a ±5-token window. High recall by design."""
    hits = []
    body = read_body(path)
    for lineno, line in enumerate(body.splitlines(), 1):
        if not line.strip() or line.lstrip().startswith(("#", "|", "---")):
            continue
        for sent in sentences(line):
            low = sent.lower()
            toks = re.findall(r"[a-z']+", low)
            for ent, grade in ent2grade.items():
                if ent not in low:
                    continue
                head = ent.split()[-1]
                if head not in toks:
                    continue
                for i, t in enumerate(toks):
                    if t != head:
                        continue
                    # subject window: the verb sits to the RIGHT of the subject
                    for j in range(i + 1, min(i + 6, len(toks))):
                        cls = verb2class.get(toks[j])
                        if not cls:
                            continue
                        # a person intervening owns the verb, not the abstraction
                        if any(ent2grade.get(toks[k]) == 1 for k in range(i + 1, j)):
                            break
                        t_ = tier(cls, grade, licensed, toks[j], partial, e1)
                        if t_ == 0:
                            break
                        hits.append({
                            "file": os.path.relpath(path, ROOT), "line": lineno,
                            "subject": ent, "grade": grade, "verb": toks[j],
                            "class": cls, "tier": t_, "sentence": sent,
                            "flags": flags_for(ent, grade, cls, sent),
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
    ap.add_argument("--include-legacy", action="store_true",
                    help="add MTGOA_TEAL_080525.md as the untreated baseline")
    a = ap.parse_args()

    reg = load_registry()
    v2c, _sev, e2g, lic, partial, e1 = build_index(reg)
    files = [os.path.join(ROOT, p) for p in a.paths] or targets(a.include_legacy)

    rows = []
    for f in files:
        rows += scan(f, v2c, e2g, lic, partial, e1)
    report(rows, files, a.report)
    return 0


if __name__ == "__main__":
    sys.exit(main())
