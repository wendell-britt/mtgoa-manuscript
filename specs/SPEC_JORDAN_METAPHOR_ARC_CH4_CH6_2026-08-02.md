# SPEC — Jordan's metaphorical development, Chapters 4–6

**Status:** Proposed editorial integration. No canonical chapter prose changes by this spec.

**Source of truth:** `manuscript/ch4.md`, `manuscript/ch5.md`, `manuscript/ch6.md`
on `master` after `6293ef3` (2026-08-02).

**Companion:** `specs/SPEC_JORDAN_METAPHOR_ARC_CH1_CH3_2026-08-02.md`.

**Purpose:** Continue the Jordan / conceptual-metaphor audit through the middle
three Faces. Jordan moves from an embodied, corrigible read to proportionate
boundary, accountable stewardship, and structural change that other people can
contest and carry forward.

This is a proposal. Do not insert candidate language into `manuscript/` without
Wendell approving the full before/after text and the normal edit protocol.

---

## 1 · The transformation to protect

| Chapter | Jordan arrives inside | The chapter gives her | She leaves able to say |
|---|---|---|---|
| Ch4 — Challenger | A no makes me cruel or unsafe. | Boundary as line, cost, and proportionate consequence. | “I can hold a boundary without treating my activation as complete moral knowledge.” |
| Ch5 — Regent | Inheritance means obedience or rejection. | Stewardship across time. | “I can preserve a value without preserving an arrangement that harms people.” |
| Ch6 — Architect | I must fix people or resolve every incident. | Condition, leverage, design, and handoff. | “I can change a condition without using systems language to step away from people.” |

The cumulative movement is:

`CORRIGIBLE READ → PROPORTIONATE BOUNDARY → SHARED STEWARDSHIP → CONTESTABLE DESIGN`

Each Face corrects the preceding Face's shadow. Do not present the sequence as a
ladder that Jordan completes before acting; it is a repertoire she returns to.

---

## 2 · Cross-chapter check: Authority, Impact, Revision

Before every substantial reader-facing move in these three chapters, the prose
must make the following questions available:

1. **Authority:** Is this mine to name, refuse, reform, or design?
2. **Impact:** Who receives the benefit, and who bears the cost?
3. **Revision:** Who can correct, contest, or change this after I act?

This is the bridge from the book's consent-based definition of allyship to its
actual practices. It joins Challenger proportionality, Regent stewardship, and
Architect handoff.

---

## 3 · Chapter 4 — The Challenger

### Preserve

- Charge → Aim → Act → Stand → Exit, especially the separation of Stand from Exit.
- The distinction between Reckoning and threat.
- The claim that a clean no can maintain relationship without dissolving a boundary.
- The existing distinction between the Shaman's read and the Challenger's violation claim.

### Gaps and requirements

#### [METAPHOR_SHADOW] A clean no does not confer unbounded authority

Line, Demand, Refusal, and Reckoning need a decision point. Jordan must distinguish
her own boundary from a collective demand or a harm she can name without controlling
the decision.

**Required function:** Before the five modes, ask whether this is Jordan's boundary,
a request for collective change, or a harm most affected people must define.

#### [METAPHOR_COLLISION] Preserve the Village fable without collective mind

The agency audit identifies the Village fable as both a protected voice device and
the largest concentration of collective agency language. Do not auto-remove the
fable. When its claims matter to the chapter's argument, restore people, incentives,
practices, or visible decisions as the subject.

**Constraint:** Preserve comedy and fable register. Do not replace every “village”
instance mechanically; first obtain Wendell's ruling on the protected device.

#### [TRANSFER_GAP] Carry Shaman humility into Challenger action

The chapter must state that charge is a read to investigate, not proof that
confrontation is automatically correct.

**Exit condition:** Jordan can choose a proportionate mode and name the authority
and cost of her move.

---

## 4 · Chapter 5 — The Regent

### Preserve

- Honor ↔ Reform as an alternative to obedience versus rejection.
- Inherit → Honor → Steward → Reform → Entrust.
- The conversion of one person’s line into a durable, revisable collective practice.

### Gaps and requirements

#### [AGENCY_GAP] Inheritance must have people, cost, and revision rights

Tradition, inheritance, Village, and office can become the agents of the chapter.
Every major inheritance claim must identify at least one of: who passed it on, who
benefits or bears its cost, who may revise it, or what practice keeps it in place.

#### [METAPHOR_OVERREACH] Stewardship cannot sanctify attachment

Honor must include the question of who was excluded or harmed, and whether affected
people have a real role in changing the arrangement.

#### [TRANSFER_GAP] Make governance the carry-forward of a clean no

State that a line becomes a tradition only when more than one person can name, test,
and change it. Otherwise it remains individual resolve.

**Exit condition:** Jordan can identify both the value worth carrying and the
governance needed to keep it from becoming a cage.

---

## 5 · Chapter 6 — The Architect

### Preserve

- “Fixing the Condition Instead of the Person.”
- Structure ↔ Agency polarity.
- Observe → Model → Design → Deploy → Hand Off.
- The claim that handoff includes the recipient's ability to change the design.

### Gaps and requirements

#### [METAPHOR_SHADOW] Structural explanation does not erase agency

The chapter needs an explicit reciprocal rule: personal responsibility does not
erase conditions, and structural explanation does not erase a person's action.

#### [AGENCY_GAP] Use mechanism-on-page

The current agency audit identifies document speech and system personification as
this chapter's characteristic slip. Prefer the decision-maker, incentive, record,
or process that produces an outcome over maps, charts, reports, and systems that
“say,” “teach,” “reward,” or “understand.”

This is not only a grammar repair. It tells Jordan where to look when she wants to
change a condition.

#### [CONSENT_GAP] Co-design and revision must be explicit

Before Deploy or Hand Off, require the reader to ask: who lives with this design,
who can refuse it, and who can revise it after the designer leaves?

#### [SEQUENCE_GAP] Diplomat is a check on design, not a post-design permission

The chapter order may remain Architect then Diplomat. The handoff must avoid implying
that relationship begins only after structure. The Architect makes a condition; the
Diplomat tests whether people can enter, contest, and live inside it.

**Exit condition:** Jordan can hand over both an operating practice and the reasoning
needed to change it.

---

## 6 · Implementation protocol

1. Read only canonical `manuscript/ch4.md`–`ch6.md` and current agency ledgers.
2. Treat the Village ruling as Wendell-only; do not run a mechanical replacement pass.
3. Locate the smallest existing paragraphs that can carry each missing function.
4. Draft full before/after prose in conversation and wait for approval per site.
5. Apply approved prose through `instruments/spec_edit.py`; run `dupes.py` first.
6. Run relevant instruments, including the agency checks where the prose touches an
   agency-audit site.
7. Commit approved chapter prose separately from this planning spec.

## 7 · Completion criteria

- Every major boundary move distinguishes authority, impact, and revision.
- Regent inheritance language identifies human carriers and revision rights.
- Architect prose makes mechanism visible without treating people as inputs.
- Co-design and contestability are explicit before a handoff.
- No Village-fable changes land before Wendell rules on its protected status.
- Jordan reaches the Diplomat with both a designed condition and a reason to ask how
   people can genuinely inhabit it.

## 8 · Handoff

Next diagnostic tranche: Chapters 7–9.

- Ch7 Diplomat: care, impact, terms, field, and false equivalence.
- Ch8 Sage: board, altitude, perspective, humility, and return.
- Ch9 Player: authorship, iteration, one-person feedback, and shared pen.

Keep the final audit separate from prose implementation sessions.
