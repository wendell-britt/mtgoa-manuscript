# -*- coding: utf-8 -*-
"""claims.py -- the ruled facts of this book, and whether the prose still carries them.

Built 2026-09-09 to `specs/SPEC_CLAIMS_REGISTRY_2026-09-09.md`, after a content ruling was applied
to one sentence in a paragraph whose other three sentences argued the opposite and the whole
pipeline reported clean. Wendell: *"nonsense sentence."* Every instrument in this repo is
sentence-scoped or a file-level frequency, so none of them can see a paragraph disagreeing with
itself. This one does not read arguments either. **It guards spans a person already found.**

    python3 instruments/claims.py              # the board
    python3 instruments/claims.py -v           # every finding, in full
    python3 instruments/claims.py --incomplete # only: is any ruling half-applied (shipcheck)
    python3 instruments/claims.py --shape      # only: is the registry itself well-formed

## What it checks

    carriers     every quoted span still occurs EXACTLY ONCE in its named file
    forbidden    a phrase a ruling removed has not come back anywhere in the corpus
    declares     a pattern a ruling banned is still declared in editorial.yaml
    applied      a ruling recorded as `N of M` with N < M is work that was started

## Why drift does not stop a press

A carrier that has moved is **ambiguous**: somebody broke a ruling, or somebody improved a
sentence and left the entry stale. An ambiguous signal at press stakes gets muted rather than
read, and the muting is silent. So drift fails `review.py` and `coherence.py` and nothing else.
`applied: 1 of 4` is unambiguous — the work was started and not finished — and that one is a
`shipcheck.py` blocker, which is why `--incomplete` exists as its own exit code.

## What it cannot do

It does not find a carrier. Three of DL-78's four changed spans carried the old fact in metaphor
and matched no search for it; only reading the paragraph found them. **The census is a read, and
this file makes the read durable.** Its value begins at the first ruling made under it, so it
would not have caught the defect that caused it to be written.
"""
import io, os, re, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)
REGISTRY = os.path.join(HERE, "claims.yaml")
LOG = os.path.join(ROOT, "specs", "DECISION_LOG.md")

APPLIED = re.compile(r"^\s*(\d+)\s+of\s+(\d+)\s*$")


def _yaml():
    try:
        import yaml
    except ImportError:
        sys.stderr.write("claims.py needs pyyaml\n")
        sys.exit(2)
    return yaml


def load():
    """Every entry in the registry, in file order."""
    if not os.path.exists(REGISTRY):
        return []
    with io.open(REGISTRY, encoding="utf-8") as fh:
        doc = _yaml().safe_load(fh) or {}
    return doc.get("claims") or []


def corpus():
    """The declared corpus from editorial.yaml, falling back to the globs it declares today."""
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("profile", os.path.join(HERE, "profile.py"))
        prof = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(prof)
        globs = prof.corpus(["manuscript/ch*.md"])
    except Exception:
        globs = ["manuscript/ch*.md", "appendices/APPENDIX_*.md",
                 "appendices/ON_THE_SHOULDERS_OF.md", "front_matter/*.md", "back_matter/*.md"]
    out = []
    for g in globs:
        out += sorted(glob.glob(os.path.join(ROOT, g)))
    return out


def is_claim(e):
    """An entry with a ruler is a claim and fails. Without one it is a candidate and reports."""
    return bool(str(e.get("ruled_by") or "").strip())


def _read(path):
    try:
        return io.open(path, encoding="utf-8").read()
    except IOError:
        return None


def check_entry(e):
    """(hard, soft) findings for one entry. `hard` fails the run; `soft` is reported only."""
    hard, soft = [], []
    cid = e.get("id", "?")
    fact = " ".join(str(e.get("fact") or "").split())[:96]
    bucket = hard if is_claim(e) else soft

    for c in e.get("carriers") or []:
        rel, phrase = c.get("file", ""), c.get("phrase", "")
        text = _read(os.path.join(ROOT, rel))
        if text is None:
            bucket.append("%s  file not found: %s" % (cid, rel))
            continue
        n = text.count(phrase)
        if n == 0:
            bucket.append("%s  carrier gone from %s\n        fact: %s\n        phrase: %s"
                          % (cid, rel, fact, phrase))
        elif n > 1:
            bucket.append("%s  carrier is ambiguous in %s (%d occurrences)\n        fact: %s"
                          "\n        phrase: %s" % (cid, rel, n, fact, phrase))

    for phrase in e.get("forbidden") or []:
        for path in corpus():
            text = _read(path)
            if text and phrase in text:
                bucket.append("%s  removed phrase is back in %s\n        fact: %s\n        phrase: %s"
                              % (cid, os.path.relpath(path, ROOT), fact, phrase))

    declares = e.get("declares")
    if declares:
        decl = _read(os.path.join(ROOT, str(e.get("declared_in") or "editorial.yaml")))
        if decl is None:
            bucket.append("%s  declaring file not found: %s" % (cid, e.get("declared_in")))
        elif declares not in decl:
            bucket.append("%s  the rule is no longer declared in %s\n        fact: %s"
                          "\n        pattern: %s" % (cid, e.get("declared_in"), fact, declares))
    return hard, soft


def incomplete():
    """Rulings recorded as started and not finished. Unambiguous, so this one blocks the press."""
    out = []
    for e in load():
        m = APPLIED.match(str(e.get("applied") or ""))
        if not m:
            continue
        done, total = int(m.group(1)), int(m.group(2))
        if done < total:
            out.append("%s  applied %d of %d — %s"
                       % (e.get("id", "?"), done, total,
                          " ".join(str(e.get("fact") or "").split())[:72]))
    return out


def shape():
    """The registry checked against itself. Wired into coherence.py."""
    entries = load()
    findings, seen = [], set()
    logged = set(re.findall(r"DL-\d+", _read(LOG) or ""))
    for e in entries:
        cid = e.get("id")
        if not cid:
            findings.append("an entry has no id")
            continue
        if not re.match(r"^DL-\d+$", str(cid)):
            findings.append("%s is not a DL-nn id; there is no second id space" % cid)
        if cid in seen:
            findings.append("%s appears twice" % cid)
        seen.add(cid)
        if logged and cid not in logged:
            findings.append("%s has no entry in DECISION_LOG.md" % cid)
        if not (e.get("carriers") or e.get("forbidden") or e.get("declares")):
            findings.append("%s guards nothing: no carriers, no forbidden phrases, no declares"
                            % cid)
        if not str(e.get("fact") or "").strip():
            findings.append("%s has no fact" % cid)
        if not str(e.get("scope") or "").strip():
            findings.append("%s has no scope; an entry records the method it used" % cid)
        applied = str(e.get("applied") or "")
        if applied and not APPLIED.match(applied):
            findings.append("%s applied is %r, which is not `N of M`" % (cid, applied))
        for c in e.get("carriers") or []:
            if not c.get("phrase"):
                findings.append("%s has a carrier with no phrase" % cid)
            rel = str(c.get("file") or "")
            if re.search(r":\d+\s*$", rel):
                findings.append("%s has a line number in a carrier: %s" % (cid, rel))
            # FR-C7. Found by acceptance test A7, which named a file that does not exist and
            # got `claims  ok  clean` from coherence: the drift check caught it on a different
            # run and the SHAPE check, whose job this is, did not look.
            elif not rel or not os.path.exists(os.path.join(ROOT, rel)):
                findings.append("%s names a file that does not exist: %s" % (cid, rel or "(empty)"))
        if e.get("declared_in") and not os.path.exists(os.path.join(ROOT, str(e["declared_in"]))):
            findings.append("%s names a declaring file that does not exist: %s"
                            % (cid, e["declared_in"]))
    return findings


def coverage():
    """What the registry does NOT guard. A short registry must never read like coverage."""
    entries = load()
    logged = sorted(set(re.findall(r"DL-\d+", _read(LOG) or "")))
    guarded = {e.get("id") for e in entries if is_claim(e)}
    return len(guarded), len(entries) - len(guarded), max(0, len(logged) - len(guarded)), len(logged)


def main():
    verbose = "-v" in sys.argv

    if "--shape" in sys.argv:
        f = shape()
        print("claims registry — %s" % ("well-formed" if not f else "%d finding(s)" % len(f)))
        for x in f:
            print("  %s" % x)
        return 1 if f else 0

    if "--incomplete" in sys.argv:
        f = incomplete()
        print("claims — %s" % ("no ruling half-applied" if not f
                               else "%d ruling(s) started and not finished" % len(f)))
        for x in f:
            print("  %s" % x)
        return 1 if f else 0

    entries = load()
    if not entries:
        print("claims — registry is empty; nothing is guarded")
        return 0

    hard, soft = [], []
    for e in entries:
        h, s = check_entry(e)
        hard += h
        soft += s

    guarded, candidates, unregistered, logged = coverage()
    print("claims — ruled facts, and whether the prose still carries them\n")
    print("  %-9s %d claim(s) guarded, %d span(s) and phrase(s) watched"
          % ("guarded", guarded, sum(len(e.get("carriers") or []) + len(e.get("forbidden") or [])
                                     for e in entries)))
    print("  %-9s %d candidate(s) — censused, unruled, reported only" % ("candidate", candidates))
    print("  %-9s %d of %d DECISION_LOG ruling(s) have no entry here and are not guarded"
          % ("uncovered", unregistered, logged))
    print("  %-9s %d" % ("drift", len(hard)))

    show = hard if not verbose else hard + soft
    for x in show[:None if verbose else 6]:
        print("\n  [%s] %s" % ("DRIFT" if x in hard else "candidate", x))
    if not verbose and len(hard) > 6:
        print("\n  ... %d more. Re-run with -v." % (len(hard) - 6))
    if soft and not verbose:
        print("\n  %d candidate finding(s) not shown; they never fail. Re-run with -v." % len(soft))

    print("\n%s" % ("CLAIMS PASS — every guarded span is where its ruling left it" if not hard
                    else "CLAIMS FAIL — %d guarded span(s) moved. Restore the span, or update the "
                         "phrase in claims.yaml." % len(hard)))
    return 1 if hard else 0


if __name__ == "__main__":
    sys.exit(main())
