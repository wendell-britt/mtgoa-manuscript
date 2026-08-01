# -*- coding: utf-8 -*-
"""
What stops this book shipping today.

The editorial system ranks findings by what they cost to fix: claim error, blocked,
continuity, verify, structural, line. That is the right order for *editing* and the wrong
order for *shipping*, and on the 1st those are different questions. `rescan.py --list`
answers the first. This answers the second.

A blocker is something that makes the artefact wrong or incomplete in a reader's hands.
Everything else is quality, and quality does not stop a press.

    python3 instruments/shipcheck.py          # the board
    python3 instruments/shipcheck.py -v       # every blocking site

Ordered by Wendell's ruling 2026-08-01: the app removal is blocker one. The book routes
readers to a product that is not shipping with v1, and a wrong pointer in a printed book
cannot be patched.
"""
import io, os, re, sys, glob, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)
SURFACES = ("manuscript/*.md", "appendices/*.md", "front_matter/*.md", "back_matter/*.md")

# Generic uses that are not this product and must survive any app sweep. Keyed on the
# sentence, same discipline as gate.py's EXEMPT: change the sentence and the exemption
# stops applying.
APP_EXEMPT = [
    ("takes a mindfulness app",
     "generic prose about mindfulness apps, not this product"),
]
APP = re.compile(r"→ app|\bthe app\b|\bapp's\b|bars-engine", re.I)


def files():
    for pat in SURFACES:
        for p in sorted(glob.glob(os.path.join(ROOT, pat))):
            if "backup" in os.path.basename(p):
                continue
            yield p


def app_sites():
    out = []
    for p in files():
        for i, line in enumerate(io.open(p, encoding="utf-8").read().split("\n"), 1):
            if not APP.search(line):
                continue
            if any(ex in line for ex, _ in APP_EXEMPT):
                continue
            out.append((os.path.relpath(p, ROOT), i, line.strip()))
    return out


def run(cmd):
    try:
        r = subprocess.run(["python3"] + cmd, cwd=ROOT, capture_output=True, text=True)
        return r.returncode, r.stdout + r.stderr
    except Exception as e:                                    # pragma: no cover
        return 1, str(e)


def main():
    verbose = "-v" in sys.argv
    rows = []

    sites = app_sites()
    rows.append(("1", "app routing", len(sites),
                 "the book points readers at a product not shipping with v1"))

    code, out = run(["instruments/placeholders.py"])
    n = 0
    m = re.search(r"PLACEHOLDERS FOUND: (\d+)", out)
    if m:
        n = int(m.group(1))
    rows.append(("2", "placeholders", n, "these typeset verbatim"))

    code, out = run(["instruments/build_book.py"])
    gaps = re.findall(r"^\s*GAP\s+(.+?)\s{2,}", out, re.M)
    rows.append(("3", "build gaps", len(gaps),
                 "the spine does not assemble complete: " + ", ".join(gaps) if gaps
                 else "the spine assembles"))

    code, out = run(["instruments/gate.py"])
    rows.append(("4", "gate", 0 if "GATE PASS" in out else 1,
                 "banned words, And/But openers, glued em-dashes, live tokens"))

    code, out = run(["instruments/emdash.py"])
    rows.append(("5", "em-dash budget", 0 if "within budget" in out else 1,
                 "the ratchet only goes down"))

    code, out = run(["marginalia/compile.py", "--verify"])
    rows.append(("6", "marginalia round-trip", 0 if "byte-identical" in out else 1,
                 "the frame must not alter the body"))

    print("SHIP CHECK — what stops this book reaching a reader\n")
    print("%-3s %-24s %8s   %s" % ("#", "blocker", "count", "why it blocks"))
    print("-" * 96)
    total = 0
    for rank, name, n, why in rows:
        total += n
        print("%-3s %-24s %8s   %s" % (rank, name, n if n else "clear", why[:56]))
    print("-" * 96)
    print("\n%s" % ("SHIPPABLE — no blocker outstanding" if not total
                    else "%d blocking item(s) across %d categor(y/ies)"
                    % (total, sum(1 for r in rows if r[2]))))

    if verbose and sites:
        print("\n" + "=" * 96)
        print("APP ROUTING — %d site(s)" % len(sites))
        print("=" * 96)
        cur = None
        for f, i, line in sites:
            if f != cur:
                cur = f
                print("\n  %s" % f)
            print("    %-5d %s" % (i, line[:84]))
        if APP_EXEMPT:
            print("\n  exempt, and must survive any sweep:")
            for phrase, why in APP_EXEMPT:
                print("    %-34s %s" % (phrase, why))
    return 0


if __name__ == "__main__":
    sys.exit(main())
