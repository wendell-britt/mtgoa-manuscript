# -*- coding: utf-8 -*-
"""ch2_ledger_nine.py — the nine outstanding LEDGER_CH2 `fix` sites.

Ruled by Wendell 2026-08-02: "do all 9 and fix the snags."

Proposals come from `editorial_reports/agency/LEDGER_CH2.md`, not from this branch's own
re-derivation. Ops as logged there: R4 ×1, R6 ×1, R1 ×7.

## The three snags, and how each was fixed

**Snag 1 — an absolute of the kind Wendell struck down earlier the same day.** The ledger's
E5 read *"None of them told you how to be the kind of person who could do it sustainably."*
His ruling on the same shape, hours earlier: *"Very few trainings build… this take is too
strong and indefensible."* Shipped as **"Very few of them told you"**, which is his own
wording for the hedge.

The ledger also wrote `could`, which breaks tense with the four appositive fragments
following it (*Who can show up… Who can hold complexity…*). Kept as `can`.

**Snag 2 — `the old allyship` appears five times in one subsection and the ledger converts
three.** Resolved by verb class rather than by uniformity, which turns out to be the
distinction the rule is drawing anyway. The three converted sites take perception, speech
and intention verbs (*mistaking*, *ask*, *assumes*, *tells*) — things only a person does.
The two left take causal verbs (*produced real wins*, *produces moments of brilliance*),
and an approach really does produce outcomes; the registry rates causal lowest severity and
calls it dead metaphor rather than category error. So the subsection now reads *the trainers
never asked* beside *the old allyship produced real wins*, and the difference between those
two subjects is the finding, not an inconsistency.

**Snag 3 — a weakened antecedent.** The ledger's E3 leaves *the old allyship* inside a
relative clause, so the following *"It had a theory of change. It went like this:"* has two
pronouns reaching past it. Merged into **"Their theory of change went like this:"** — one
sentence instead of two, owner named, both orphan pronouns gone.

## The one site this branch broke and is now repairing

E2. Ledger site L41 was *"a world that demands capacities we were never taught to build"*,
op R6, proposal *"where employers, movements, and communities expect capacities…"*. This
branch's `we`-cleanup replaced it with *"Allyship asks for capacities most training never
reaches"* — a Grade-0-shaped subject on a speech verb, which fails to fire only because
`allyship` is not a registry entity. Now carries the ledger's named groups **and** Wendell's
ruled hedge (*most training never reaches*), which the original R6 proposal predates.

Anchors are exact and unique. A missed or duplicated anchor aborts with nothing written.
"""
import io, sys

P = "manuscript/ch2.md"

E = [
    # R4 — the author's own framework, so the asking really happened in his head.
    ("The daemon work doesn't ask you to fix the Shadow. It asks you to find out what it "
     "has been protecting.",
     "I don't ask you to fix the Shadow. I ask you to find out what it has been "
     "protecting."),

    # R6 — dissolve to transmission. Repairs a site this branch introduced.
    ("Allyship asks for capacities most training never reaches, and most training does not "
     "say so.",
     "Employers, movements and communities expect capacities that most training never "
     "reaches, and most training does not say so."),

    # R1 + snag 3.
    ("The old allyship's fatal flaw was mistaking information for transformation. It had a "
     "theory of change. It went like this:",
     "The trainers who built the old allyship mistook information for transformation. "
     "Their theory of change went like this:"),

    # R1 — speech + intention on the same unlicensed subject, two sentences running.
    ("The old allyship does not ask about that. It assumes the person executing the right "
     "actions has the body to do it.",
     "The trainers behind the old allyship never asked about that. They assumed you would "
     "have the body to execute the actions regardless."),

    # R1 + snag 1.
    ("The old allyship tells you what to do. It doesn't tell you how to be the kind of "
     "person who can do it sustainably.",
     "Coaches and workshops told you what to do. Very few of them told you how to be the "
     "kind of person who can do it sustainably."),

    # R1 ×2 — "Culture does not train, reward, or punish" is the registry's own constraint
    # text, and `reward` and `punish` are two of the three verbs it names verbatim.
    ("- What pattern does this group reward when things get uncertain?",
     "- What pattern do the people in this group end up rewarding when things get "
     "uncertain?"),

    ("- What pattern does this system punish when someone tells the truth?",
     "- What pattern do the people running this system end up punishing when someone tells "
     "the truth?"),

    # R1 — the generic old-model apparatus, so restoring the teachers fits where testimony
    # would not.
    ("Maybe you did everything the work asked.",
     "Maybe you did everything your teachers and workshops asked of you."),

    # R1 — autobiographical. The friends are the real subject two sentences earlier; the
    # sentence had handed the asking to the phone call.
    ("The call meant to support me asked me to hold their unprocessed feelings about a "
     "Black man's murder.",
     "Meant to support me, they were really asking me to hold their unprocessed feelings "
     "about a Black man's murder."),
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
