# -*- coding: utf-8 -*-
"""ch2_agency_ledger.py — the six ch2 fixes from the agency audit, seated on this branch.

Ruled by Wendell 2026-08-02, after the audit surfaced mid-session: "do all 4 in order."

## Where these came from, and why they were not already here

`SPEC_AGENCY_TRACEABILITY_AUDIT_20260802` ran on **the same day as this branch's hand pass**,
on `claude/book-analysis-sonnet-agents-2y8e4m`: ten agents, one rubric, nine chapters plus
the appendix surface, `instruments/agency_registry.yaml` as canon, and
`instruments/agency_grep.py` as a recall net. It logged **131 Tier-3 sites book-wide, 27 in
ch2**, and it applied the W-1, W-2 and R8 conversions to `manuscript/` on its own branch.

Neither branch knew about the other. This one re-derived the same defect class by hand from
Wendell's opening question — *"Who is the hidden agent behind all of this"* — and reached a
narrower and in places **wrong** version of the same conclusions. The six edits below are
the ch2 sites where the audit is right and this branch was wrong.

## The six

E1-E2, E4-E5 are **W-2**, which the registry records as `RULED 2026-08-02`:

> The book and chapter may take mechanical and directional verbs for structural navigation
> (covers, returns to, points to, put, handed, left). They MAY NOT take perception,
> intention, speech or social-causal verbs (asks, teaches, needs, wants, names, proposes,
> says). The conversion target is not automatic: -> `you` where the sentence is about what
> the reader gained, -> `I` where it is about a choice the author made.

**This branch used `This chapter asks…` as a precedent for legality.** It is the ruling's
own example of an illegal verb.

E3 is Grade 6 + social-causal. The registry's constraint text names the three verbs
verbatim: *"Culture does not train, reward, or punish."* **This branch declined this site
twice**, and justified it by citing `ch2:73` — *"The old allyship tells you what to do"* —
which LEDGER_CH2 flags as a Tier-3 defect in its own right. A ruling anchored on a flagged
site.

E6 is a **ROSTER-VIOLATION**: the Protector is one of the embodied three, restricted by
ch2 §6's own roster ruling to somatic rather than verbal action, and `calls` is a naming
act. LEDGER_CH2 notes the line four paragraphs earlier that gets it right — *"It does not
argue or explain; it braces"* — which is what makes the slip legible against the chapter's
own standard. **This branch left it and called it a great line.**

## One change from the audit's wording

E5 ships `recognize`, not the audit's `recognise`. This manuscript runs US spelling
17:0 on this word, 12:0 on `realize`, 24:3 on `organiz`.
"""
import io, sys

P = "manuscript/ch2.md"

E = [
    # W-2 -> I : a choice the author made.
    ("That's the pivot this chapter needs from you.",
     "That's the pivot I need from you."),

    ("This chapter asks whether you will stop treating your own somatic intelligence as "
     "something that belongs to someone else.",
     "I am asking whether you will stop treating your own somatic intelligence as "
     "something that belongs to someone else."),

    # Grade 6 + social-causal. "train" is named illegal in the registry's constraint text.
    ("That structure trains performance. It does not train play.",
     "Trained that way, you perform. You do not learn to be playful."),

    # W-2 -> you : what the reader gained.
    ("This chapter teaches you how to walk the book.",
     "Here you learn how to walk the book."),

    ("It is how the book teaches recognition.",
     "It is how you come to recognize them."),

    # ROSTER-VIOLATION. The Protector braces; it does not name.
    ("It trades contact for control and calls the trade safety.",
     "It trades contact for control, and the trade feels like safety."),
]


def main():
    t = io.open(P, encoding="utf-8").read()
    for i, (a, _b) in enumerate(E, 1):
        n = t.count(a)
        if n != 1:
            sys.exit("E%d anchor matched %d times, expected 1: %r" % (i, n, a[:70]))
    for a, b in E:
        t = t.replace(a, b)
    io.open(P, "w", encoding="utf-8").write(t)
    print("ch2.md — %d edits applied" % len(E))
    return 0


if __name__ == "__main__":
    sys.exit(main())
