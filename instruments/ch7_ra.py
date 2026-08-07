# -*- coding: utf-8 -*-
"""ch7_ra.py — R-A: charge with an owner.

Ruled by Wendell 2026-08-03: *"everything else lands"* — the R-A draft minus `ch7:351`,
which reached him carrying `the thing that charges the field` and was rejected on the empty
head noun. 351 is held back for a redraft; the other four ship here.

## What R-A turned out to be, after the branch comparison

The metaphor audit asked for body vocabulary — *"the charge located in a chest, a jaw, a
held breath."* Local `master` carries a de-somatize sprint (`2ec7b74`, `2e4d5ea`) whose
directive is the opposite: *evoke embodiment via metaphor and external scene; stop
narrating or prescribing the reader's interior state.* Wendell restated it to me this
session. The audit was written without that history in view, and following it would have
reversed a standing ruling and multiplied `ch7:443`, which already breaks it.

The same 6-Face call that stripped the body-feel prescriptions **kept `the charge`** — "the
book's coined term, grants agency." So the vehicle was already chosen. Charge is the body
vocabulary. It only needed an owner.

## The finding the sites come from

Every Face in ch7 names where the charge came from, except the one whose job is holding it:

    177  "comes not from one side being wrong but from getting stuck on one so long"
    371  "When conflict charges a field"
    441  "The charge of the swallowed no"
    453  "When competing demands charge a field"
    802  "the charge of everyone's discomfort"

Against five sourceless sites, all inside the Field-Holder deep-dive. Charge with no source
is the container reading in another costume: it makes the field a place that has weather
rather than something people are doing to each other.

`ch7:802` is the model, the same way `ch7:359` was the model for R-B. The repair is the
chapter's own form, not an import.

## Not here

`ch7:349`, `ch7:365` and `ch7:605` read as sourceless in isolation and are not. Each sits in
a triad whose later clauses supply the people — *everyone present wants to fight, flee, or
freeze*; *the people making it*; *the camps dig in*. Fixing the first clause of those would
be a repair to a sentence that already works.

`ch7:77` and `ch7:95` are compressed definitions in the Faces list. A source clause bloats
them and the definition is not where the charge is being felt.

Anchors are exact and unique. A missed or duplicated anchor aborts with nothing written.
"""
import io, sys

P = "manuscript/ch7.md"

E = [
    # 353 — the distortion paragraph. "The field stays charged" states the physics with
    # nobody in it; ownership is the whole point of the Field-Holder's refusal to fix.
    ("Real Field-Holding contains the charge rather than removing it. The field stays "
     "charged. The Field-Holder does not calm it down.",
     "Real Field-Holding contains the charge rather than removing it. Whoever brought the "
     "charge keeps it. The Field-Holder does not take it off them or talk anyone down."),

    ("because a charged field costs more to hold than a calm one",
     "because a field with somebody's real stake in it costs more to hold than a calm one"),

    ("the behavioral pattern of withdrawing the moment the field becomes charged.",
     "the behavioral pattern of withdrawing the moment somebody charges it."),

    ("a commitment to staying present when the field becomes charged.",
     "a commitment to staying present when somebody charges it."),

    ("You have made yourself a reliable structure because you decided in advance, before "
     "the charge arrived.",
     "You have made yourself a reliable structure because you decided in advance, before "
     "anybody charged it."),
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
    print("ch7.md — %d edits applied" % len(E))
    return 0


if __name__ == "__main__":
    sys.exit(main())
