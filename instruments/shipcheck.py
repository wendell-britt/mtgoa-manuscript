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
# Scan what the spine actually assembles, not the directories it lives in. Until
# 2026-08-01 this globbed `appendices/*.md` and counted two files that do not ship --
# APPENDIX_C_KEY_TERMS.md, superseded by APPENDIX_C_FIVE_CHANNELS.md, and
# BAR_PROMPT_VOICE_AUDIT.md, an audit artefact -- which inflated blocker one by four
# sites. A ship check that counts non-shipping files is not measuring shipping.
def spine_files():
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "bb", os.path.join(HERE, "build_book.py"))
    bb = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bb)
    out = [os.path.join(ROOT, rel) for _, _, rel, _ in bb.SPINE
           if rel and os.path.exists(os.path.join(ROOT, rel))]
    out += sorted(glob.glob(os.path.join(ROOT, "manuscript", "ch*.md")))
    return out

# Generic uses that are not this product and must survive any app sweep. Keyed on the
# sentence, same discipline as gate.py's EXEMPT: change the sentence and the exemption
# stops applying.
APP_EXEMPT = [
    ("takes a mindfulness app",
     "generic prose about mindfulness apps, not this product"),
]
APP = re.compile(r"→ app|\bthe app\b|\bapp's\b|bars-engine", re.I)


def files():
    seen = set()
    for p in spine_files():
        if p not in seen:
            seen.add(p)
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


# ---------------------------------------------------------------- elevated 2026-08-01
# Wendell: "elevate existing problems into the blockers for ship." Three rows added, each
# because it makes the artefact wrong or incomplete in a reader's hands, which is this
# file's whole test. Quality findings stay in `rescan.py --list` where they belong.
#
# PROMISES. Chapter 1 tells the reader, in the imperative, that specific things will be
# hers by the end. A promise the book makes and does not keep is the failure mode the
# editorial OS ranks first -- it threatens the central promise -- and it cannot be patched
# after printing. Each row states the ch1 anchor and the test for closure on ch9, so the
# count is auditable rather than asserted. Two of the six close; `a line in every chapter`
# closed 2026-08-01 when A2's six sheet lines were seated.
PROMISES = [
    ("the Reader's Oath", "ch1:213-233, sworn out loud",
     r"\boath\b"),
    ("the myth she wrote", "ch1:203, 'the one that runs you hardest'",
     r"\bmyth"),
    ("her superpower", "ch1:209, 'you will only spot in motion'",
     r"superpower.{0,200}?\b(name it|write it|write down|capture it|fill it)"),
    ("the BAR deck", "ch1:249, 'a deck no one else could have built'",
     r"your deck\b|deck you (built|made)|deck of your own"),
    ("her autopilot", "ch1:209, 'you will catch yourself running'",
     r"autopilot.{0,300}?Fill it in"),
]


def unkept():
    """ch1 promises that ch9 never closes. Each test is a regex on ch9 alone."""
    ch9 = io.open(os.path.join(ROOT, "manuscript", "ch9.md"), encoding="utf-8").read()
    out = [(n, w) for n, w, pat in PROMISES if not re.search(pat, ch9, re.I | re.S)]
    # The sixth promise is not a ch9 test: ch1:209 promises "a line added in every
    # chapter ahead", which is kept in ch3-ch8 or nowhere.
    seated = sum(1 for i in range(3, 9)
                 if "Add a line to the sheet" in io.open(
                     os.path.join(ROOT, "manuscript", "ch%d.md" % i),
                     encoding="utf-8").read())
    if seated != 6:
        out.append(("a line in every chapter", "ch1:209, seated in %d/6" % seated))
    return out


def claim_errors():
    """Live band-1 findings. `rescan.py` re-derives against the page, so a finding whose
    quote has moved does not count. A stated fact that is wrong prints wrong."""
    code, out = run(["instruments/rescan.py", "--list"])
    blk = re.search(r"### 1 CLAIM ERROR.*?(?=\n### )", out, re.S)
    if not blk:
        return 0
    rows = re.findall(r"^  CH\d+\s+\S+\s+(LIVE|PARTIAL)\s+(.*)$", blk.group(0), re.M)
    # Two ways a finding stops counting, and they mean different things. WITHDRAWN: it was
    # never an error. FIXED: it was, and the prose now says otherwise. Before FIXED existed
    # (added 2026-08-01) ten repaired findings still counted, because rescan checks whether a
    # finding's quote survives, not whether its claim is still true, and only a reader can
    # close that gap. A board that cannot record a repair overstates the category it ranks first.
    CLOSED = ("WITHDRAWN", "FIXED")
    return sum(1 for _, text in rows if not any(k in text.upper() for k in CLOSED))


def toolchain_ok():
    """The guard on every other row. On 2026-08-01 `check_anchors` was raising ValueError
    on ch8's three-field rows and aborting the whole self-test, so ch8's anchors went
    unverified and the suite reported nothing after that point. A crashed guard and a
    clean guard look identical from outside; this row tells them apart."""
    code, out = run(["instruments/test_toolchain.py"])
    return "all cases pass" in out and "Traceback" not in out


def main():
    verbose = "-v" in sys.argv
    rows = []

    sites = app_sites()
    rows.append(("1", "app routing", len(sites),
                 "the book points readers at a product not shipping with v1"))

    miss = unkept()
    rows.append(("2", "unkept ch1 promises", len(miss),
                 "the book promises these by the last chapter and never closes them"))

    rows.append(("3", "claim errors", claim_errors(),
                 "a stated fact is wrong, and print cannot be patched"))

    code, out = run(["instruments/placeholders.py"])
    n = 0
    m = re.search(r"PLACEHOLDERS FOUND: (\d+)", out)
    if m:
        n = int(m.group(1))
    rows.append(("4", "placeholders", n, "these typeset verbatim"))

    code, out = run(["instruments/build_book.py"])
    gaps = re.findall(r"^\s*GAP\s+(.+?)\s{2,}", out, re.M)
    rows.append(("5", "build gaps", len(gaps),
                 "the spine does not assemble complete: " + ", ".join(gaps) if gaps
                 else "the spine assembles"))

    code, out = run(["instruments/gate.py"])
    rows.append(("6", "gate", 0 if "GATE PASS" in out else 1,
                 "banned words, And/But openers, glued em-dashes, live tokens"))

    code, out = run(["instruments/emdash.py"])
    rows.append(("7", "em-dash budget", 0 if "within budget" in out else 1,
                 "the ratchet only goes down"))

    code, out = run(["marginalia/compile.py", "--verify"])
    rows.append(("8", "marginalia round-trip", 0 if "byte-identical" in out else 1,
                 "the frame must not alter the body"))

    rows.append(("9", "toolchain self-test", 0 if toolchain_ok() else 1,
                 "a crashed guard and a clean guard look identical from outside"))

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

    if verbose and miss:
        print("\n" + "=" * 96)
        print("UNKEPT PROMISES — %d" % len(miss))
        print("=" * 96)
        for name, where in miss:
            print("  %-26s %s" % (name, where))

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
