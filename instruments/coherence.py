# -*- coding: utf-8 -*-
"""
coherence.py — the linter for the linters. Checks the editorial pipeline against itself.

    python3 instruments/coherence.py            # the board: one row per check
    python3 instruments/coherence.py -v          # every finding, in full

## Why this exists

Wendell, 2026-09-03: *"how do we check that the editorial pipeline is coherent and consistent.
I'm wanting to use this on multiple projects. Basically anything that I'm writing must follow
these rules."*

**The pass checks the prose. Nothing checked the pass.** It was coherent by luck: every step in
`review.py` happened to resolve to a real file, every baseline constant happened to match what
its instrument measured, every instrument a spec named happened to exist. None of that was
enforced, so any of it could rot on the next edit — a renamed instrument, a book that drifted
past its own baseline, a spec citing a step number that moved.

**This is the call site for the pipeline's own standing rule.** `EDITORIAL_AUTHORITIES` says *"a
rule with no call site is a rule nobody keeps."* The same is true one level up: a pipeline with
no self-check is a pipeline that silently diverges. This runs the check.

## The checks

The profile lives in `editorial.yaml` (see `profile.py`), and these checks validate it against
reality — the manifest is the source of truth, not any hardcoded constant.

- **manifest** — `editorial.yaml` exists, parses, and every instrument it names (`pass`,
  `project_only`, and each baseline) is a real file. A profile that points at nothing fails here.
- **wiring** — every instrument named in `review.py` (draft loop and book steps) exists on disk.
  A renamed or deleted instrument fails here instead of at 2 a.m. mid-review.
- **pass-wire** — every scanner the manifest's `pass` declares is actually wired into `review.py`.
  A declared-but-unrun scanner is the manifest and the orchestration disagreeing.
- **drift** — every manifest baseline still measures within tolerance on the current corpus. A
  book edited past its own baseline is caught before the number it prints becomes a lie.
- **register** — every ``instrument.py`` named in `EDITORIAL_AUTHORITIES` exists. The register
  claims each authority has a call site; this proves the claim.
- **orphan** — every instrument with a manifest baseline is wired into `review.py`. An instrument
  nobody runs is the exact failure the register warns of: `fragment.py`, `antecedent.py` and
  `notstack.py` each existed for days before anything called them.
- **doc-figure** — a named book-wide count in an instrument's docstring (e.g. "302 ... across the
  book") that no longer matches what the instrument measures. Reported, not failed: a docstring
  figure is prose, and a drifted one is a note to update, not a broken build.

## Portability

The checks are generic — no title of this book appears in them. What varies per project is the
*content*, and it now lives in one declared file: `editorial.yaml`. Copy `instruments/` to a new
project, write its `editorial.yaml`, and this same checker validates that project's profile
against that project's reality. See `specs/EDITORIAL_PIPELINE_COHERENCE_2026-09-03.md` for the
universal/profile split.
"""
import os, re, sys, subprocess, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, os.pardir))
REVIEW = os.path.join(HERE, "review.py")
REGISTER = os.path.join(ROOT, "specs", "EDITORIAL_AUTHORITIES_2026-09-01.md")


def _load_profile():
    spec = importlib.util.spec_from_file_location("profile", os.path.join(HERE, "profile.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


prof = _load_profile()

# Per-instrument adapters: how to read the rate a baseline instrument actually measures on the
# book. The coherence checker is allowed to know its instruments; a manifest would externalise
# this, which is the portability step held for Wendell's call.
def _rate_from_book_row(out):
    """Instruments that print a 'the book ... N.N%' data row (telling, light_verb)."""
    for line in out.splitlines():
        if line.strip().lower().startswith("the book"):
            pcts = re.findall(r"(\d+\.\d+)%", line)
            if pcts:
                return float(pcts[-1])
    return None

def _rate_trailing_and(out):
    """'... 771 LOOSE, 12 RANK across 5643 sentence(s)' -> LOOSE / sentences."""
    m = re.search(r"(\d+)\s+LOOSE.*?across\s+(\d+)\s+sentence", out)
    if m:
        loose, sents = int(m.group(1)), int(m.group(2))
        return round(100.0 * loose / max(sents, 1), 1)
    return None

MEASURERS = {
    "telling.py": _rate_from_book_row,
    "light_verb.py": _rate_from_book_row,
    "trailing_and.py": _rate_trailing_and,
}
DRIFT_TOLERANCE = 0.4   # percentage points between the declared constant and the measured rate


def wired_instruments():
    """Every instrument filename review.py references, draft loop and book steps."""
    src = open(REVIEW, encoding="utf-8").read()
    names = set()
    # book steps: ["instruments/gate.py", ...], ["marginalia/review.py"], ["prose_diet.py"]
    for m in re.finditer(r'"((?:instruments/|marginalia/)?[a-z_0-9]+\.py)"', src):
        names.add(os.path.basename(m.group(1)))
    return names


def run_book(fn):
    p = subprocess.run([sys.executable, os.path.join(HERE, fn)],
                       capture_output=True, text=True, cwd=ROOT, timeout=180)
    return p.stdout + p.stderr


def _instrument_exists(name):
    """`telling` or `telling.py` -> True if instruments/telling.py is on disk."""
    fn = name if name.endswith(".py") else name + ".py"
    return os.path.exists(os.path.join(HERE, fn))


def check_manifest():
    """editorial.yaml exists, parses, and every instrument it names is real."""
    if not prof.exists():
        return ["no editorial.yaml — the pipeline is running on instrument defaults, and "
                "coherence cannot validate a profile that is not declared"]
    findings = []
    for name in prof.pass_list() + prof.project_only():
        if not _instrument_exists(name):
            findings.append("manifest names instrument '%s' but instruments/%s.py is missing"
                            % (name, name))
    for name in prof.baselines():
        if not _instrument_exists(name):
            findings.append("manifest declares a baseline for '%s' but instruments/%s.py is "
                            "missing" % (name, name))
    return findings


def check_wiring():
    findings = []
    for name in sorted(wired_instruments()):
        for base in (HERE, os.path.join(ROOT, "marginalia")):
            if os.path.exists(os.path.join(base, name)):
                break
        else:
            findings.append("wired in review.py but missing on disk: %s" % name)
    return findings


def check_pass_wiring():
    """Every instrument the manifest's `pass` declares is actually wired into review.py.
    A declared scanner that nothing runs is the manifest and the orchestration disagreeing."""
    wired = wired_instruments()
    findings = []
    for name in prof.pass_list():
        if (name + ".py") not in wired:
            findings.append("manifest `pass` lists '%s' but review.py does not wire it" % name)
    return findings


def check_drift():
    """Every manifest baseline still measures within tolerance on the current corpus."""
    findings = []
    for name, declared in sorted(prof.baselines().items()):
        fn = name + ".py"
        meas = MEASURERS.get(fn)
        if not meas:
            findings.append("manifest baseline '%s' has no measurer in coherence.py — add one "
                            "so its drift is checked" % name)
            continue
        rate = meas(run_book(fn))
        if rate is None:
            findings.append("%s: could not read a measured rate from its output" % name)
        elif abs(rate - float(declared)) > DRIFT_TOLERANCE:
            findings.append("%s: manifest says %.1f%% but it measures %.1f%% now (drift %.1f > %.1f)"
                            % (name, float(declared), rate, abs(rate - float(declared)),
                               DRIFT_TOLERANCE))
    return findings


def check_register():
    if not os.path.exists(REGISTER):
        return ["register not found: %s" % os.path.relpath(REGISTER, ROOT)]
    src = open(REGISTER, encoding="utf-8").read()
    findings = []
    for name in sorted(set(re.findall(r"`([a-z_0-9]+\.py)`", src))):
        if not os.path.exists(os.path.join(HERE, name)):
            findings.append("named in EDITORIAL_AUTHORITIES but missing: %s" % name)
    return findings


def check_orphan():
    """An instrument that declares a baseline in the manifest but is not run by review.py."""
    wired = wired_instruments()
    findings = []
    for name in sorted(prof.baselines()):
        if (name + ".py") not in wired:
            findings.append("has a manifest baseline but is not wired into review.py: %s" % name)
    return findings


def check_doc_figures():
    """A docstring count 'N ... across the book' that no longer matches the measured count."""
    findings = []
    for fn, meas in (("telling.py", None),):
        src = open(os.path.join(HERE, fn), encoding="utf-8").read()
        for m in re.finditer(r"(\d{3,})\s+(?:times|absolutes)?[^.\n]*?across the book", src):
            claimed = int(m.group(1))
            out = run_book(fn)
            # telling's ABSOLUTE count is the third integer on the book row
            row = next((l for l in out.splitlines()
                        if l.strip().lower().startswith("the book")), "")
            nums = re.findall(r"\b(\d+)\b", row)
            measured = int(nums[2]) if len(nums) >= 3 else None
            if measured is not None and measured != claimed:
                findings.append("%s docstring says %d 'across the book' but it measures %d"
                                % (fn, claimed, measured))
    return findings


CHECKS = [
    ("manifest ", check_manifest, True),
    ("wiring   ", check_wiring, True),
    ("pass-wire", check_pass_wiring, True),
    ("drift    ", check_drift, True),
    ("register ", check_register, True),
    ("orphan   ", check_orphan, True),
    ("doc-figure", check_doc_figures, False),   # reports, does not fail the board
]


def main():
    verbose = "-v" in sys.argv
    print("coherence — the pipeline checked against itself")
    print("-" * 60)
    failed = 0
    allfindings = []
    for tag, fn, hard in CHECKS:
        findings = fn()
        status = "ok  " if not findings else ("FAIL" if hard else "LOOK")
        if findings and hard:
            failed += 1
        print("  %s  %s  %s" % (tag, status,
                                "clean" if not findings else "%d finding(s)" % len(findings)))
        allfindings += [(tag.strip(), f) for f in findings]
    print("-" * 60)
    if allfindings and (verbose or True):
        print("")
        for tag, f in allfindings:
            print("  [%s] %s" % (tag, f))
    print("")
    print("COHERENCE %s" % ("PASS — the pipeline is internally consistent" if not failed
                            else "FAIL — %d hard check(s) failing" % failed))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
