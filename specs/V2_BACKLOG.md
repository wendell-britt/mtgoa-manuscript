# V2 BACKLOG — what v1 solves on paper and v2 should solve with software

**Opened 2026-08-01.** DL-20 took the app out of v1, on the reasoning that a wrong
pointer in a printed book cannot be patched. That ruling was about routing, not about
scope: several problems in the book have a paper answer that works and a software answer
that works better. This file records the second kind so the v1 solutions are not mistaken
later for the whole intent.

Nothing here is a v1 deliverable. Nothing here may be referenced from any shipping
surface — see `SPEC_REMOVE_APP_V1_2026-07-31.md` and `instruments/shipcheck.py`, which
counts any such reference as blocker one.

---

## 1 · Matchmaking — pairing readers with an accountability partner

**Ruled by Wendell 2026-08-01:** *"this is something that I want the app to be able to
provide — matchmaking services."*

**The problem it answers.** Appendix B's four campaigns are the only complete practice
map in the book: a clean 2-2-2-2 across every domain and every daemon, matching Appendix
A's affinity table. Every one of them requires another person — a partner, a team, a
community, an audience. `SPEC_WORKBOOK_SCOPE.md:53` requires that *"a reader without a
coach can complete every exercise alone."* So the route that completes the practice is
the route a solo reader cannot take, and the book has no way to hand her a person.

**What v1 does instead.** *The Ask*, a solo Raise Awareness quest seated at the head of
The Four Campaigns, which turns finding the partner into the first rep rather than a
precondition. It is a real answer and not a placeholder: the shadow that stops the ask is
the Victim's *I do not have anybody*, so the quest is practice in the exact thing it
unblocks.

**What it does not answer, and what v2 should.** *The Ask* assumes she knows one person
who has watched her try and not laughed. Some readers do not, and those are
disproportionately the readers the campaigns would help most. Matchmaking is the case
where software beats paper outright, because the book cannot introduce two strangers and
an app can.

**Design constraints carried forward from v1.** Whatever v2 builds should preserve the
three properties the paper version has: the ask is finite (three weeks, a stated end
date), the partner's job is small and specific (hear one capture a week, ask one
question), and the prediction is captured next to the outcome, because the gap between
them is the BAR.

---

## 2 · Reserved

The app integration that DL-20 deferred — `SPEC_REMOVE_APP_V1_2026-07-31.md:5`,
*"take the app out for v1 and let v2 carry the integration"* — belongs here as it gets
specified. The superpower quiz (open ruling 3) and the quest capture's named home (open
ruling 5) are the two nearest candidates.
