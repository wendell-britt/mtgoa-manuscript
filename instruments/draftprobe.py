"""Run the pattern instruments' own regexes against a draft file.

shapes/preempt/assumed/antecedent are board-only: they walk the manuscript
spine and ignore argv paths. This harness imports their compiled patterns and
applies them to one draft, so a draft can be checked before it lands.
"""
import io, os, re, sys, importlib.util

INSTR = "/home/user/mtgoa-manuscript/instruments"


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(INSTR, name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    argv, sys.argv = sys.argv, [name]
    try:
        spec.loader.exec_module(mod)
    finally:
        sys.argv = argv
    return mod


text = io.open(sys.argv[1], encoding="utf-8").read()
paras = [p for p in text.split("\n\n") if p.strip() and not p.lstrip().startswith("#")]
body = "\n\n".join(paras)

shapes = load("shapes")
preempt = load("preempt")
assumed = load("assumed")

hits = 0
print("=== shapes ===")
for label, pat in (("binary contrast", shapes.BINARY), ("definite-article series", shapes.SERIES)):
    for m in pat.finditer(body):
        hits += 1
        print("  %-24s %s" % (label, m.group(0)[:100].replace("\n", " ")))
for r in shapes.runs(body):
    hits += 1
    print("  %-24s %s" % ("determiner run", r[:100]))

print("=== preempt ===")
for entry in preempt.SHAPES:
    label, pat = entry[0], re.compile(entry[1], re.I) if isinstance(entry[1], str) else entry[1]
    for m in pat.finditer(body):
        hits += 1
        print("  %-28s %s" % (label, m.group(0)[:90].replace("\n", " ")))

print("=== assumed ===")
for group, name in ((assumed.CLAIMS, "CLAIM"), (assumed.HISTORY, "HISTORY"),
                    (assumed.EXPERIENCE, "EXPERIENCE")):
    for entry in group:
        label, pat = entry[0], re.compile(entry[1]) if isinstance(entry[1], str) else entry[1]
        for m in pat.finditer(body):
            hits += 1
            print("  %-10s %-20s %s" % (name, label, m.group(0)[:70].replace("\n", " ")))
for m in assumed.INVITE.finditer(body):
    print("  %-10s %-20s %s" % ("INVITE", "(good)", m.group(0)[:70].replace("\n", " ")))

print("\n%d pattern hit(s)" % hits)
