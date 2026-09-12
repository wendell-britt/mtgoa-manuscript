# -*- coding: utf-8 -*-
"""paragraph_diff.py -- single-sentence surgery inside a paragraph nobody else touched.

Built 2026-09-09 to FR-D1 and FR-D2 of `specs/SPEC_CLAIMS_REGISTRY_2026-09-09.md`, last of the
five items and deliberately last. A content ruling was applied by editing one sentence of an
eight-sentence paragraph whose other seven were committed to the opposite claim. The result read
as nonsense and every instrument in the repo returned clean, because they are all sentence-scoped
or file-level frequencies and none of them looks at a paragraph.

    python3 instruments/paragraph_diff.py             # working tree against HEAD
    python3 instruments/paragraph_diff.py <ref>       # against another ref

## What it flags, and what it deliberately does not

A **changed paragraph in which most sentences are untouched** is where a contradiction gets made:
the edited sentence agrees with the ruling and its neighbours still argue the old one. A paragraph
rewritten wholesale is not this defect, and neither is a one-sentence paragraph.

**This is a smoke alarm and it was built after the registry on purpose.** On its own it can only
say *look at the neighbours*, which is noise. With `claims.yaml` behind it, it says *this paragraph
carries DL-78, ten carriers, and you changed one of them* — which is a finding. That is the whole
argument for the build order, and it is why FR-D2 exists.

Reports only. It never fails a run: a small, correct edit inside a settled paragraph is the normal
case, and a check that fires on the normal case gets switched off.
"""
import io, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)

# A paragraph is worth checking only if it argues at length. Below this it cannot contradict
# itself in the way this instrument exists to catch.
MIN_SENTENCES = 4
# Flag while a clear majority is untouched. At half or more changed the author was rewriting.
MAX_CHANGED_FRACTION = 0.5
SENT = re.compile(r"(?<=[.!?])\s+(?=[A-Z\"'*])")


def sentences(par):
    return [s.strip() for s in SENT.split(par.strip()) if s.strip()]


def git(args):
    try:
        return subprocess.run(["git"] + args, cwd=ROOT, capture_output=True, text=True).stdout
    except Exception:
        return ""


def changed_files(ref):
    out = git(["diff", "--name-only", ref, "--", "manuscript", "appendices",
               "front_matter", "back_matter"])
    return [f for f in out.split("\n") if f.strip().endswith(".md")]


def paragraphs(text):
    return [p for p in text.split("\n\n") if p.strip()]


def carriers_in(par):
    """FR-D2. Which registered claims have a carrier inside this paragraph."""
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("claims", os.path.join(HERE, "claims.py"))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        entries = mod.load()
    except Exception:
        return []
    hits = []
    for e in entries:
        n = sum(1 for c in (e.get("carriers") or []) if c.get("phrase", "\0") in par)
        if n:
            hits.append((e.get("id", "?"), n, len(e.get("carriers") or [])))
    return hits


def main():
    ref = next((a for a in sys.argv[1:] if not a.startswith("-")), "HEAD")
    findings = []
    for rel in changed_files(ref):
        before = git(["show", "%s:%s" % (ref, rel)])
        path = os.path.join(ROOT, rel)
        if not before or not os.path.exists(path):
            continue
        after = io.open(path, encoding="utf-8").read()
        old = {p.strip() for p in paragraphs(before)}
        for par in paragraphs(after):
            if par.strip() in old:
                continue
            sents = sentences(par)
            if len(sents) < MIN_SENTENCES:
                continue
            # How much of this paragraph survived the edit verbatim?
            old_sents = set()
            for op in old:
                old_sents |= set(sentences(op))
            kept = [s for s in sents if s in old_sents]
            changed = len(sents) - len(kept)
            if not changed or changed / float(len(sents)) >= MAX_CHANGED_FRACTION:
                continue
            findings.append((rel, changed, len(sents), carriers_in(par), sents, old_sents))

    print("paragraph diff — sentences changed inside paragraphs left otherwise intact\n")
    if not findings:
        print("  no partial-paragraph edits against %s" % ref)
        print("\nCLEAN — nothing changed one sentence and left its neighbours")
        return 0

    for rel, changed, total, claims, sents, old_sents in findings:
        print("  %s  %d of %d sentence(s) changed" % (rel, changed, total))
        for cid, hit, of in claims:
            print("      carries %s — %d of its %d carrier(s) are in this paragraph" % (cid, hit, of))
        for s in sents:
            print("      %s %s" % ("~" if s not in old_sents else " ", s[:94]))
        print("")
    print("READ THE NEIGHBOURS — %d paragraph(s). A changed sentence agrees with the new ruling;\n"
          "the sentences around it may still argue the old one. Reporting only." % len(findings))
    return 0


if __name__ == "__main__":
    sys.exit(main())
