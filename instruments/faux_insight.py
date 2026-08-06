# -*- coding: utf-8 -*-
"""faux_insight.py — `most people skip`, out of all four sites.

Ruled by Wendell 2026-08-03, after a `/no-ai-slop` detect run over the whole day's diff:
*"make the four cuts but make sure to rewrite so that whatever the cut leaves out stays
voice aligned."*

`no-ai-slop/SKILL.md` lists the pattern by name: *"This is the part most people skip…
These flatter the writer as the lone expert. Cut the setup and make the claim stand on its
own."*

## Two of the four are mine, from today

`ch6:197` — the tier-1 pass changed `part` to `step` and left the phrase standing. **I
fixed the noun the empty-head instrument sees and walked past the phrase this skill bans by
name.** `ch7:691` — I rewrote the tail of that sentence in the ch7 `thing` sweep and did not
look at its head.

Same shape as `quiet` → `careful` earlier in the week: two instruments, each blind to the
other's target, and a fix for one produces a clean pass on both. The `thing` sweep ran
before the slop pass every time, which is the order the review prescribes, and the order is
what let this through.

## Why each cut needed a rewrite rather than a deletion

Wendell's instruction is the whole job here. Three of the four had a `because` or a `Then`
hanging off the flattery, so deleting the clause leaves a subordinate with nothing to
attach to.

**`ch3:205`** — *"and most people skip this one, because joy feels like the easy one and it
is not"*. The `because` was explaining the skipping. It becomes a relative clause on joy
itself, which keeps the contrast that was doing the real work — joy **looks** like the easy
channel — and keeps the sentence's three-part *when… when… when* cadence intact.

**`ch6:197`** — *"Then (here comes the step most people skip)"*. Deleting the parenthetical
leaves *"Then *and now:*"*, which is not a sentence. It takes a naming clause instead:
**the question that finishes it**. That says what the step *is* rather than who fails to
take it, and it is true — the preceding paragraph asks three diagnostic questions and this
is the fourth that turns diagnosis into design.

**`ch7:691`** — *"a structure for repair that most people skip because it requires
uncomfortable sentences"*. Same dangling `because`. The structure keeps its difficulty
without the audience: *"and it runs on uncomfortable sentences in a specific order."*

**`ch7:699`** — the only clean deletion. *"This is the step most people skip. Repair is not
the same as reconciliation."* The second sentence is already the clarifier, and steps 1 and
2 open the same way — *"Not your interpretation of what broke"*, *"Not their part. Yours."*
Cutting the first sentence puts step 3 in the shape its siblings already have.

Anchors are exact and unique. A missed or duplicated anchor aborts with nothing written.
"""
import io, os, sys

EDITS = [
    ("manuscript/ch3.md", [
        ("When you do this with joy, and most people skip this one, because joy feels like "
         "the easy one and it is not (it requires you to stop moving,",
         "When you do this with joy, which feels like the easy one and is not (it requires "
         "you to stop moving,"),
    ]),
    ("manuscript/ch6.md", [
        ("Then (here comes the step most people skip) *and now:",
         "Then the question that finishes it: *and now:"),
    ]),
    ("manuscript/ch7.md", [
        ("the Diplomat has a specific structure for repair that most people skip because "
         "it requires uncomfortable sentences in a specific order.",
         "the Diplomat has a specific structure for repair, and it runs on uncomfortable "
         "sentences in a specific order."),
        ("**3. Name what you're not asking for.** This is the step most people skip. "
         "Repair is not the same as reconciliation.",
         "**3. Name what you're not asking for.** Repair is not the same as "
         "reconciliation."),
    ]),
]


def main():
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
    for rel, edits in EDITS:
        t = io.open(os.path.join(root, rel), encoding="utf-8").read()
        for i, (a, _b) in enumerate(edits, 1):
            n = t.count(a)
            if n != 1:
                sys.exit("%s E%d matched %d times: %r" % (rel, i, n, a[:60]))
    n = 0
    for rel, edits in EDITS:
        p = os.path.join(root, rel)
        t = io.open(p, encoding="utf-8").read()
        for a, b in edits:
            t = t.replace(a, b)
        io.open(p, "w", encoding="utf-8").write(t)
        n += len(edits)
    print("%d edits applied across %d files" % (n, len(EDITS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
