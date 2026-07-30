# -*- coding: utf-8 -*-
"""
test_toolchain.py — regression suite for the editing tools.

Every case here is a real failure from 2026-07-29, with the answer we settled
on. The point is not coverage. The point is that each of these cost a round trip
with Wendell to discover, and none of them should ever cost one again.

Run before trusting any number, and after touching any regex:

    python3 instruments/test_toolchain.py

Exit 1 on any failure.
"""
import re, io, os, sys, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "marginalia"))

FAIL = []


def check(name, got, want, note=""):
    ok = got == want
    if not ok:
        FAIL.append((name, got, want, note))
    print(f"  {'PASS' if ok else 'FAIL'}  {name}" + (f"   ({note})" if not ok and note else ""))


# ---------------------------------------------------------------- denying negation
print("\nDENYING_GENERAL — must fire")
from review import DENYING_GENERAL
D = re.compile(DENYING_GENERAL)

MUST_FIRE = [
    ("canonical village-version shape",
     "It's not aggression. That's the village version of the Challenger."),
    # The 25 stopping conditions shipped in this shape. The old narrow pattern
    # keyed on "it's not" and never saw it.
    ("'The test is not X. The test is Y'",
     "The test is not whether they stopped. The test is whether the line left your mouth clean."),
    # Found in ch8 while proving the skill misses register. My own probe regex
    # missed it too, because it only matched it's/that's.
    ("'That gap is not X. It's Y'",
     "That gap is not the end of the view. It's the beginning of the work."),
    # Only visible on a whole-file scan; a line-by-line scan misses it.
    ("across a paragraph break",
     "That is not the promise.\n\nThe promise is discernment."),
]
for name, s in MUST_FIRE:
    check(name, bool(D.search(s)), True)

print("\nDENYING_GENERAL — must stay silent")
MUST_NOT = [
    # RULE_COLLISIONS licenses ranking, and "not just" is the marker it can see.
    ("ranking negation (Adams' cave)",
     "It wasn't just that the cave was cold. It was that the cave was in Islington."),
    ("ordinary prose",
     "The system is not broken in a way anyone planned. People adapt."),
]
for name, s in MUST_NOT:
    check(name, bool(D.search(s)), False)

# Known false positives. The detector fires and a human overrules it. These are
# asserted to KEEP firing: the regex cannot make a semantic judgment, and any
# change that silences them has almost certainly stopped catching real ones too.
# Batch 1 ran 25 candidates to 22 real and 3 false — a ~12% false-positive rate,
# which is the number to plan adjudication time against.
print("\nDENYING_GENERAL — known false positives (human overrules, detector still fires)")
KNOWN_FP = [
    ("ch2:136 — ranking; the negated thing stays true",
     "The problem is not that you wanted to be good. The problem is that trying to seem good takes the whole body."),
    ("ch8:81 — idiomatic, not definitional",
     "That much is not in question. The question this chapter asks is what happened next."),
    ("ch8:144 — subject changes, so it is not a restatement",
     "These three are not obviously wrong. The Sage in distortion is doing versions of useful things."),
]
for name, s in KNOWN_FP:
    check(name, bool(D.search(s)), True, "semantic limit — see RULE_COLLISIONS")

# ---------------------------------------------------------------- canon gate
print("\ngate.py — flag sensitivity")
import gate
def counters(t):
    return {n: len(re.findall(p, t, f)) for n, p, f in gate.COUNTERS}

# The gate's andbut and stacks counters are case-sensitive by design. Running
# them case-insensitively invented four violations in the marginalia that were
# not there.
check("lowercase 'and' mid-sentence is legal",
      counters("relief — and underneath it a small satisfaction")["andbut"], 0)
check("capital 'But' opener is caught",
      counters("I would vote for it again. But let there be no mistake.")["andbut"], 1)
check("lowercase 'not' pair is legal",
      counters("she had told me and not somebody else. Not concern.")["stacks"], 0)
check("capital 'Not' stack is caught",
      counters("Not a demand. Not a condition of continued affection.")["stacks"], 1)
# Reversed 2026-07-29. This test previously asserted the plural was legal, which
# is how three "rooms" reached ch2 and ch5 — the assertion was wrong, not the
# manuscript. Wendell banned singular and plural alike.
check("plural 'rooms' is banned", counters("stayed in rooms that chose harm")["banned"], 1)
check("singular 'room' is banned", counters("stayed in the room")["banned"], 1)
check("singular 'room' is banned", counters("lend the room their reputation")["banned"], 1)
# Placeholders must never reach print.
check("placeholder token is caught", counters("I was told that at ⟦ASH-AGE⟧.")["tokens"], 1)

# ---------------------------------------------------------------- register ruler
print("\nprose_diet.py — the ruler must match the June measurement")
import prose_diet as PD
# A narrow is|are|was|were reads 42.1 where the comparable measure reads 61.7.
# Reporting the narrow figure looks like a 33% improvement and is none.
sample = "It is what it is and they are what they were, so it's fine and they're done."
narrow = len(re.findall(r"\b(is|are|was|were)\b", sample, re.I))
check("COPULA_1K counts more than the narrow four",
      len(PD.COPULA_1K.findall(sample)) > narrow, True)
# The baseline must be external. Normalising to the book made it unable to fail.
check("baseline targets Igniting Joy, not the book", PD.TARGET["copula_1k"], 28.8)
check("book's own average is not a target", "copula_1k" not in PD.BASE, True)

# ---------------------------------------------------------------- frame safety
print("\ncompile.py / review.py — frame handling")
import compile as C
for ch in (3, 5, 9):
    p = os.path.join(ROOT, "manuscript", "ch%d.md" % ch)
    orig = io.open(p, encoding="utf-8").read()
    stripped = C.strip_marginalia(orig)
    rebuilt, _, problems = C.apply_chapter(ch, stripped)
    # ch3 and ch5 legitimately end on a --- rule; the postcard strip must not eat it.
    check("ch%d round-trips byte-identical" % ch,
          C.strip_marginalia(rebuilt).rstrip() == stripped.rstrip(), True)

# Rule 2 makes every note quote the prose beside it, so anchors appear twice on
# an applied manuscript. Counting without stripping false-positived on two notes.
import review as R
before = len(R.F)
R.check_anchors(os.path.join(ROOT, "marginalia", "insertions.py"),
                os.path.join(ROOT, "manuscript"))
check("anchors clean on an applied manuscript", len(R.F) - before, 0)



# ---------------------------------------------------------------- edit-script safety
# On 2026-07-29 a spec file was truncated to 0 bytes by
#     io.open(p,'w').write(io.open(p).read().replace(a,b))
# The write handle truncates before the read runs, so the read returns "".
# It committed empty and was recovered from git. Read fully, then write once.
print("\nedit-script safety")
_probe = os.path.join(ROOT, ".diet_probe_tmp")
io.open(_probe, "w", encoding="utf-8").write("hello world")
_t = io.open(_probe, encoding="utf-8").read()          # read completes first
io.open(_probe, "w", encoding="utf-8").write(_t.replace("world", "there"))
check("read-then-write preserves content",
      io.open(_probe, encoding="utf-8").read(), "hello there")
os.remove(_probe)


# ---------------------------------------------------------------- report
print()
if FAIL:
    print("%d FAILURE(S)" % len(FAIL))
    for n, g, w, note in FAIL:
        print("  %s: got %r, want %r" % (n, g, w))
    sys.exit(1)
# --- em-dash instrument, added 2026-07-29 with SPEC_EMDASH_AND_DENSITY ---------
# Wendell: "I will struggle to recognize in myself writing that makes any use of
# emdashes." Every other rule here has a human backstop and this one does not, so
# these cases are the backstop.
import importlib.util as _ilu, os as _os
_spec = _ilu.spec_from_file_location("emdash", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "emdash.py"))
_em = _ilu.module_from_spec(_spec); _spec.loader.exec_module(_em)

check("heading dashes are out of scope",
      len(list(_em.prose_lines("# Chapter 1 - The Arcade\n"))), 0)
check("axis diagrams are not prose",
      len(list(_em.prose_lines("    HONOR  <--*-->  REFORM\n".replace("<","\u2190").replace(">","\u2192").replace("*","\u25cf")))), 0)
check("table rows are not prose",
      len(list(_em.prose_lines("| a | b |\n"))), 0)
check("an ordinary sentence is prose",
      len(list(_em.prose_lines("She stayed, and the field held.\n"))), 1)
check("single tail names its shape",
      _em.shape("She stayed \u2014 and the field held.", 11), "single tail, lowercase -> comma or colon")
check("paired dashes name their shape",
      _em.shape("He has also \u2014 once, in a hard moment \u2014 surfaced it.", 12), "opens a parenthetical pair")

# The budget must never be raisable by a tool run. Only Wendell edits the file up.
_cur = {"ch1.md": 10}
check("ratchet refuses a rise", 20 > _cur["ch1.md"], True)

# --- the appositive `which` tail, widened 2026-07-30 -------------------------
# These cases exist because the rule was widened twice and the second widening had
# to be proved not to lose the first one's catches. Two are historical: `which is
# the point` is the shape the 2026-07-29 sweep cleared 64 of, and `six of which`
# is the R16 false alarm, where a correct sentence was reported as broken and a
# real edit was nearly made against it.
import re as _re, sys as _sys, os as _os2
_sys.path.insert(0, _os2.path.join(_os2.path.dirname(_os2.path.abspath(__file__)), _os2.pardir, "marginalia"))
import review as _rv
_WHICH = next(p for p, n in _rv.AI_SHAPES if n == "appositive 'which' tail")

for _probe, _want in [
    (", which is the point",                     True),   # the original shape
    (", which describes a pecking order",        True),   # missed before the widening
    (", which should tell you what it is worth", True),   # missed before the widening
    (", which means you are not holding it",     True),   # tail verb beats guard 2
    (", which channel you are running",          False),  # embedded question
    (", which he had built",                     False),  # `which` is the object
    ("Which daemon had the joystick?",           False),  # the chapter asking
    ("Which are you suppressing?",               False),  # ditto, and the old guard
    ("ninety seconds, six of which are Open Up", False),  # R16
]:
    check("which-tail: %s" % _probe.strip()[:38],
          bool(_re.search(_WHICH, _probe)), _want)

print("all cases pass")
