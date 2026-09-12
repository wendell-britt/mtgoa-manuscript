# -*- coding: utf-8 -*-
"""ruling.py -- two lines that make a ruling script prove it did the whole census.

Built 2026-09-09 to FR-E1 through FR-E5 of `specs/SPEC_CLAIMS_REGISTRY_2026-09-09.md`. A content
ruling was applied to one span of four and reported as done, because *applied* was the only status
available and applied-to-one looked exactly like applied-to-all.

Every tranche script in this repo already asserts `count == 1` per edit and writes atomically.
This extends that assertion **from the string to the claim**: a script that applies a ruling names
the claim and the number of spans the census found, and refuses to run when its own edit list
disagrees. The census stops being something remembered and becomes something the build requires.

Two lines and one import, which is the whole design constraint (FR-E4). A control that is
expensive at the moment of use gets satisfied rather than obeyed, and this book has the
`quiet` → `careful` substitution on file as the proof:

    from ruling import guard
    guard("DL-78", EDITS)          # refuses unless len(EDITS) == the entry's `applied` total

**It checks `applied`, never `carriers` (FR-E3).** Those are two censuses taken at different times
and they are not the same number. `applied` counts the spans that had to CHANGE and closes when
the script runs. `carriers` lists the spans that CARRY the fact from now on and stays open
forever. DL-78 is four and ten. The first draft of this requirement asserted one against the
other and would have refused to run on the one ruling the spec was written to seed itself with.
"""
import io, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
APPLIED = re.compile(r"^\s*(\d+)\s+of\s+(\d+)\s*$")


def _entries():
    sys.path.insert(0, HERE)
    import importlib.util
    spec = importlib.util.spec_from_file_location("claims", os.path.join(HERE, "claims.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


def guard(claim_id, edits, quiet=False):
    """Refuse, atomically and before any write, unless this script applies the whole census.

    Exits nonzero rather than raising, so a tranche script fails the way every other one does.
    """
    entry = next((e for e in _entries() if e.get("id") == claim_id), None)

    # FR-E2. No entry means no census was taken, and a ruling with no census has not been
    # applied, it has been started. The fix is to write the entry, not to remove the guard.
    if entry is None:
        sys.stderr.write(
            "REFUSED: %s has no entry in instruments/claims.yaml.\n"
            "A content ruling needs its census recorded before it is applied: the fact, why the\n"
            "carriers were easy to miss, the spans that must change, and the spans that carry it\n"
            "afterwards. See specs/SPEC_CLAIMS_REGISTRY_2026-09-09.md.\n" % claim_id)
        sys.exit(3)

    m = APPLIED.match(str(entry.get("applied") or ""))
    if not m:
        sys.stderr.write("REFUSED: %s has no `applied: N of M` count to check against.\n" % claim_id)
        sys.exit(3)

    total = int(m.group(2))
    n = len(edits)
    if n != total:
        sys.stderr.write(
            "REFUSED: %s censused %d span(s) and this script carries %d edit(s).\n"
            "Nothing written. Either the script is short of the census, or the census is stale.\n"
            "Applying a ruling to some of its spans is what produced this guard.\n"
            "  fact: %s\n" % (claim_id, total, n,
                             " ".join(str(entry.get("fact") or "").split())[:88]))
        sys.exit(4)

    if not quiet:
        print("%s: %d of %d spans, census matched" % (claim_id, n, total))
    return entry
