# SPEC — The Example beats, under the doubled position

**2026-07-31. Wendell: "nope we're gonna do all 20. We have a spec for this yes? This is also
the place where our protected classes are going to show up."**

Three specs cover pieces of this and none of them covers the Example itself. This is that
spec, and it exists so 35 of these can be written to one form instead of 35 judgement calls.

| what it gives | where |
|---|---|
| the six target types, and the protected classes each position most often holds | `SPEC_FACE_TARGETS_2026-07-30.md` §1, §2 |
| self-versus-other, and the gory-details brief | `SPEC_WAVE_REALIGNMENT_2026-07-29.md` §11.3 |
| the doubled position, and why the Examples kept failing | `SPEC_SCHOOL_HANDBOOKS_2026-07-30.md` §199, §310 |
| the form below | here |

---

## 0 · Two facts to have before starting

**The job is 35, not 20.** Counted today:

| ch | Face | have | want | gap |
|---|---|---|---|---|
| 3 | Shaman · Body | 5 | 5 | |
| 4 | Challenger · Line | 5 | 5 | |
| 5 | **Regent · Oath** | **0** | 5 | **5 to write** |
| 6 | Architect · Pattern | 5 | 5 | |
| 7 | Diplomat · Bridge | 3 | 5 | 2 to write |
| 8 | Sage · Horizon | 2 | 5 | 3 to write |
| 9 | Player | 5 | 5 | |
| | | **25** | **35** | **10 to write** |

The 20 in `SPEC_WAVE_REALIGNMENT` §11.1 was a count taken on 2026-07-29, before ch4's five
were written. **The Regent chapter has never had a single Example**, which no document
records.

**An override, recorded rather than smuggled.** `SPEC_WAVE_REALIGNMENT` §11.4 says: *"Do not
rewrite the 20 that exist to hit a ratio… The imbalance is a gap in what was written, not an
error in what was written."* Wendell has overruled that. All 25 get revised. The §11.4
argument was sound when the only lever was a ratio; the doubled position is a different lever,
and it changes what an Example is for rather than what it counts toward.

## 1 · The form

Six requirements. An Example that misses one is not finished.

1. **A person in the Face's target position**, from `SPEC_FACE_TARGETS` §2 — not a system, a
   team, a dashboard or a process. Eight of the current 25 have no person in them at all.
2. **The doubled position, visible.** The reader has been in that position and is now standing
   next to somebody else in it. *You cannot give away a thing you have never had in your
   hands.* This is the load-bearing one, and it is what makes the Example allyship rather than
   either self-advocacy or rescue.
3. **The move, executed, in words.** The sentence said, or the specific thing done. Not *you
   speak up.*
4. **The cost, in the currency of the scene.** Standing, a review, a relationship, being the
   difficult one at that table. Never *it costs something.*
5. **The outcome stays theirs.** What the other person does with it is not entered as the
   reader's result. This is Loop A's consent hinge and the book's one non-negotiable rule.
6. **Legible to Jordan.** A scene she could have been in this week.

### The doubled position, concretely

Not *I had this problem, therefore I understand yours.* That is the saviour move wearing
humility. It is: **the reader recognises the position from the inside, which is what lets them
see it early and read it accurately, and they are not the one in it this time.** The recognition
is the qualification. The distance is what makes the help usable.

Where it shows on the page: one clause, not a paragraph. *You know what that pause is because
you have made it.*

## 2 · Where the protected classes go

**The stance is `SPEC_FACE_TARGETS` §1 and it does not change.** The statutory list, named
because it is the one list that cannot be called a fashion and cannot be accused of leaving
somebody out on a whim.

**In the Examples the class is shown, not labelled.** An Example does not say *a disabled
colleague*. It shows the accommodation request being treated as an opening offer, and the
reader knows. The statutory list belongs in the apparatus, where a reader can check it; the
Examples are where she meets a person.

**Distribution, per chapter, per `SPEC_FACE_TARGETS` §2.** Each chapter's five draw from that
Face's four listed classes, and no chapter runs the same class twice unless the Face's own
entry says it is that Face's home class.

| ch | Face's four |
|---|---|
| 3 | race and color · invisible or undiagnosed disability · gender identity · religion |
| 4 | citizenship and immigration status · disability accommodation · pregnancy · age 40+ |
| 5 | religion · national origin · race and color · age 40+ |
| 6 | **disability, the home class** · national origin · pregnancy and familial status · religion |
| 7 | citizenship and immigration status · familial status and race · disability · age 40+ |
| 8 | disability, chronic and psychiatric · age · genetic information · veteran status |
| 9 | none. ch9 is the Player designing their own game, and the beneficiary is whoever they build for |

**The floor clause, from §1.** The list is a floor rather than a ceiling, and the moves work
identically on positions no statute protects: class, caste, a record, body size, caregiving,
being new, being the only one. **At least one Example per chapter should sit outside the
statutory list**, or the book teaches that unprotected harm is permitted harm.

**Disability appears in all six**, which §1.3 says is a teaching point rather than a gap.

## 3 · The balance rule, replacing §11.3's floor

§11.3 asked for at least two of five with another person as beneficiary. Under the doubled
position that floor is too low and the wrong axis. **Four of five have another person as the
beneficiary; the fifth is the reader's own position, and it is the one that earns the other
four.** A chapter with no self-Example teaches rescue.

`SPEC_WAVE_REALIGNMENT` §11.4 was right that ch3's attribution Example is correctly
self-advocacy. Under this rule it becomes the designated fifth rather than an exception.

## 4 · How this gets checked

- `instruments/example_audit.py`, to be written: person present, beneficiary, class shown,
  cost named, outcome left open.
- `gate.py` and the em-dash budget, both of which are at cap and stay there.
- `seam_sweep.py`: every Example in ch3 to ch8 sits **below** the seam, in Wendell's half, so
  nothing here touches the membrane. Confirmed before drafting.
