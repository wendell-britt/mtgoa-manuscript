# -*- coding: utf-8 -*-
"""
reader_run_scan.py — a deliberately small recall net for the Chapter 2 reader run.

The reader run identified failures a conventional grammar or style pass does not
reliably see: a body-state offered as explanation without an observable situation,
and rhetoric that instructs the reader how significant a line is instead of making
the line carry that significance.  This tool finds *candidates* for those two
questions.  It does not decide that a sentence fails, and it never edits prose.

The other reader-run questions are judgment calls and remain human checks:
  - Has the consequential actor been named? (agency_grep.py)
  - Does the passage preserve a real both/and rather than a false contrast?
  - Is a term introduced before it is used, and does the book spine place the
    promised material where the reader expects it?

    python3 instruments/reader_run_scan.py
    python3 instruments/reader_run_scan.py -v
    python3 instruments/reader_run_scan.py manuscript/ch3.md -v
    python3 instruments/reader_run_scan.py --spine -v
"""
import glob
import io
import os
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, os.pardir))
MANUSCRIPT = os.path.join(ROOT, "manuscript")
HEADMASTER = os.path.join(ROOT, "front_matter", "headmasters_letter.md")

# These are intentionally narrow phrases taken from the Chapter 2 ledger.  They do
# not make all embodiment suspect; they surface formulations that need a reader to
# ask whether a concrete event and observable consequence are doing the explaining.
SOMATIC = re.compile(
    r"\b(?:been\s+)?braced\b|\ba\s+tightening\b|\bvigilance\b|"
    r"\bdoesn[’']t\s+quite\s+release\b|\bthe\s+body\s+(?:tightens|tenses|does)\b",
    re.I,
)

# Not every imperative is staging.  These are the specific rhetorical frames the
# reader run rejected: they announce importance or prescribe a posture without
# adding information.  New patterns belong here only after a reader has caught them.
STAGING = re.compile(
    r"\bhold\s+(?:these\s+three\s+words|this\s+thought)\b|\bwhole\s+book\s+turns\s+on\b|"
    r"\bask\s+(?:it|this)\s+without\s+flinching\b|"
    r"\bworth\s+sitting\s+with\b|\bpicture\s+a\s+meeting\b",
    re.I,
)

RULES = (("somatic-inference", SOMATIC,
          "Does a concrete event and observable effect explain this body-state?"),
         ("rhetorical-staging", STAGING,
          "Does this tell the reader how important or brave a line is instead of showing it?"))


def quote(text, n=140):
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= n else text[:n - 1] + "…"


def targets(args):
    paths = [a for a in args if not a.startswith("-")]
    if paths:
        return [os.path.abspath(a) for a in paths]
    files = sorted(glob.glob(os.path.join(MANUSCRIPT, "ch[1-9].md")))
    if "--spine" in args and os.path.exists(HEADMASTER):
        # This is the reader's order at the one standalone insertion point, not its
        # storage directory.  build_book.py remains the authoritative full spine.
        insert = next((i for i, p in enumerate(files) if p.endswith("ch3.md")), len(files))
        files.insert(insert, HEADMASTER)
    return files


def scan(path):
    hits = []
    for lineno, line in enumerate(io.open(path, encoding="utf-8"), 1):
        if line.lstrip().startswith(("#", "<!--", ">")):
            continue
        for rule, pattern, question in RULES:
            if pattern.search(line):
                hits.append((rule, lineno, quote(line), question))
    return hits


def label(path):
    return os.path.relpath(path, ROOT)


def main():
    args = sys.argv[1:]
    verbose = "-v" in args or any(not a.startswith("-") for a in args)
    files = targets(args)
    print("candidates, not defects — every hit needs the Chapter 2 reader-run question")
    print("surface: %s\n" % ("reader spine" if "--spine" in args else "chapter files"))
    print("%-38s %18s %18s %8s" % ("file", "somatic-inference", "rhetorical-staging", "total"))
    print("-" * 88)
    totals = Counter()
    for path in files:
        hits = scan(path)
        counts = Counter(h[0] for h in hits)
        totals.update(counts)
        print("%-38s %18d %18d %8d" % (label(path), counts["somatic-inference"],
              counts["rhetorical-staging"], len(hits)))
        if verbose:
            for rule, lineno, text, question in hits:
                print("    %-18s %s:%d  %s" % (rule, label(path), lineno, text))
                print("    %-18s %s" % ("", question))
    print("-" * 88)
    print("%-38s %18d %18d %8d" % ("TOTAL", totals["somatic-inference"],
          totals["rhetorical-staging"], sum(totals.values())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
