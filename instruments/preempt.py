# -*- coding: utf-8 -*-
"""
Where the prose explains itself instead of doing the thing.

    python3 instruments/preempt.py                  # the board
    python3 instruments/preempt.py -v               # every site
    python3 instruments/preempt.py --write FILE     # the full report

## The pattern, in Wendell's words

2026-08-01, reading Chapter 1:

> *"an emergent pattern is where the work is explaining itself before it is
> challenged. Instead of anticipating objections, validating them and writing the
> text on purpose, we've created modes that collapse that process and make insane
> sentences."*

His clearest instance is `ch1:131`:

> *"Here is the second, and I will say it plainly, because it is the objection
> that makes serious people wave the whole idea away:"*

**A clause that has to explain why something needs to be said plainly is not
plain.** The sentence narrates its own rhetorical status — announcing a reveal,
grading its own frankness, naming the objection it is about to answer — and by the
time it finishes doing that, it has not said the thing.

This is what collapsing the drafting process looks like on the page. Anticipating
an objection, deciding it is fair, and answering it is three separate acts of
writing. Compressed into one sentence, the anticipation and the answer arrive
stuck together, and the reader watches the machinery instead of getting the point.

## Three shapes

**Meta-narration** — `Here is the/what/where…`, `I will say it plainly`,
`I want to be careful here`. The sentence announces the move rather than making
it. The repository's own `/no-ai-slop` skill already bans this family under
*throat-clearing openers* and *faux-insight setups*; **no instrument has ever
checked for it**, which is why 69 of them are in the manuscript.

**Phantom contrast** — `the real prize`, `the actual work`, `the one nobody can
take back`. A comparative whose other half was never established. Wendell on
`ch1:121`: *"doesn't mean anything unless there are other prizes that CAN be
taken back."*

**Unfounded appeal** — `breaks the rule of every arcade you have ever played`
(`ch1:123`). The sentence asserts a shared rule or experience the book never set
up. Wendell: *"there are no rules we're referring to."*

## What this is not

It does not flag anticipating an objection. Doing that deliberately — stating it,
granting it, then answering — is good nonfiction and the book should have more of
it, not less. The defect is doing it *inside* the sentence that was supposed to
carry the claim.
"""
import io, os, re, sys, importlib.util
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    argv, sys.argv = sys.argv, [name]
    try:
        spec.loader.exec_module(mod)
    finally:
        sys.argv = argv
    return mod


fl = _load("find_line", os.path.join(HERE, "find_line.py"))

SHAPES = [
    ("meta-narration",
     # `Here they are` added 2026-08-01, batch seven: Wendell flagged it opening the
     # *Which Game Are You Playing* section. Same move as `Here is the`, one pronoun over.
     r"(Here is (?:what|where|why|how|the)\b|Here's (?:what|where|the)\b|"
     r"Here they are\b|Here is the (?:thing|point)\b|"
     r"I will say it plainly|let me be clear|I want to be careful here|"
     r"What most people get wrong|the part (?:most people|everyone)|"
     r"what nobody tells you|the uncomfortable truth)"),
    ("phantom contrast",
     r"\b(the real (?:prize|game|work|question|answer|thing|move|point|one)\b|"
     r"the actual (?:prize|game|work|question|answer|thing|move|point)\b|"
     r"the one (?:nobody|no one) can\b|what \w+ really is\b)"),
    ("unfounded appeal",
     r"(every \w+ you have ever \w+|any \w+ you have ever \w+|"
     r"we all know|as everyone knows|you already know that)"),
    # ADDED 2026-08-01, batch six. Wendell on `ch1:139` — "The third reason changes
    # everything:" — *"don't announce what it changes. If it isn't obvious then we're
    # projecting."* The first version of this file did not catch it: the sentence has
    # no throat-clearing opener and no phantom comparative. It grades its own payload
    # instead, which is the same defect one step further in — the prose telling the
    # reader how much the next clause matters rather than making it matter.
    ("stakes announcement",
     r"(changes everything|this is the (?:whole|entire|real) (?:move|point|thing)|"
     r"and that (?:is|'s) the (?:whole|entire) (?:point|move|thing)|"
     r"the most important (?:thing|part|move)|"
     r"if you (?:take|remember) (?:only )?one thing|"
     r"everything (?:changes|else) (?:from )?here)"),
    ("objection staged inside the claim",
     r"(because it is the objection|the objection that makes|"
     r"if that (?:sounds|feels|seems|landed)|if this (?:sounds|feels|seems)|"
     r"you (?:may|might) be (?:thinking|wondering)|I know how (?:that|this) sounds)"),
]


def main():
    verbose = "-v" in sys.argv
    out = None
    if "--write" in sys.argv:
        i = sys.argv.index("--write")
        out = sys.argv[i + 1] if i + 1 < len(sys.argv) else os.path.join(
            ROOT, "editorial_reports", "PREEMPT_BOARD.md")

    lines = [l for l in fl.surfaces()
             if not l["text"].lstrip().startswith(("#", "|"))]
    found = defaultdict(list)
    per = defaultdict(lambda: defaultdict(int))
    for l in lines:
        for name, pat in SHAPES:
            for m in re.finditer(pat, l["text"]):
                found[name].append((l, m.group(0)))
                per[l["rel"]][name] += 1

    L = ["# Pre-emptive self-justification — the board", "",
         "Generated by `instruments/preempt.py`. Where the prose explains itself",
         "instead of doing the thing. Named by Wendell 2026-08-01; see the module",
         "docstring for the pattern and the three shapes.", "",
         "**Nothing here is automatically a defect.** A deliberate objection —",
         "stated, granted, answered — is good nonfiction. The defect is the",
         "anticipation collapsed into the sentence that was meant to carry the claim.",
         ""]
    total = sum(len(v) for v in found.values())
    L.append("## Totals — %d sites" % total)
    L.append("")
    L.append("| Shape | sites |")
    L.append("|---|---|")
    for name, _ in SHAPES:
        L.append("| %s | **%d** |" % (name, len(found[name])))
    L.append("")

    L.append("## Per component")
    L.append("")
    spine = [rel for _, _, rel, _ in fl.bb.SPINE if rel]
    L.append("| Component | " + " | ".join(n for n, _ in SHAPES) + " | total |")
    L.append("|---" * (len(SHAPES) + 2) + "|")
    for rel in sorted(per, key=lambda r: spine.index(r) if r in spine else 999):
        row = [per[rel][n] for n, _ in SHAPES]
        L.append("| %s | %s | **%d** |" % (os.path.basename(rel),
                                           " | ".join(str(x) for x in row), sum(row)))
    L.append("")

    for name, _ in SHAPES:
        L.append("## %s — %d" % (name, len(found[name])))
        L.append("")
        for l, hit in found[name][:20 if not verbose else 500]:
            L.append("- `%s` · %s:%d" % (hit, l["rel"], l["line"]))
            L.append("  > %s…" % l["text"][:170].strip())
        L.append("")

    text = "\n".join(L) + "\n"
    if out:
        os.makedirs(os.path.dirname(out), exist_ok=True)
        io.open(out, "w", encoding="utf-8").write(text)
        print("wrote %s — %d sites" % (os.path.relpath(out, ROOT), total))
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
