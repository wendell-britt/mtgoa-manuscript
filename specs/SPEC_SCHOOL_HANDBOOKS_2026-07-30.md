# SPEC — The School Handbooks

**2026-07-30. Wendell: "we need to make a spec where the face introduces themselves to
the reader as though they are a prospective student of the school. We can lean into the
genre of the student handbook style HARD here in a way that will deepen immersion."**

---

## 1 · What this is

A short admissions page at the head of each treatise chapter, written by the Head, addressed
to the reader as somebody thinking about enrolling. Six of them, ch3–ch8.

**The genre is the point.** A prospectus has furniture nobody has to be taught: who we take,
what you will be able to do, what it costs, what we do not teach, entry requirements, a
warning. Dropping emotional content into that form is the whole joke and the whole
immersion, and it works because the form is doing the explaining. *"We are for the person
whose no does not carry"* reads as an admissions criterion and lands as a definition of
allyship.

## 2 · Where it sits, and why the chapter becomes a document stack

The signature move already made each chapter a bounded document. The handbook completes the
stack:

```
# CHAPTER 4: THE CHALLENGER
## The Clean "No" as the Foundation of Real Allyship

  EPIGRAPH-BYLINE   ← what a student and a citizen say about this school
  HANDBOOK          ← what the school says about itself          ** new **
  MARGINALIA        ← what the annotator says about the Head

## Section 1: The Exile        ┐
## Section 2: The Distortion   │ the treatise
## Section 3: The Concept      ┘
        SIGNATURE              ← the treatise closes

## Section 4–7                 ← Wendell Britt on allyship
```

Testimonial, prospectus, treatise, signature. Every surface is a document type a reader
already knows how to read, and no voice has to explain another.

**It goes above the marginalia deliberately.** The annotator is commenting on the Head; the
annotator's note reads better once the Head has spoken for themselves.

## 3 · What it carries that the book actually needs

This is not flavour with a job bolted on. Four things the book is currently missing have no
better home:

| clause | what it delivers | currently |
|---|---|---|
| **Who we are for** | the six Face targets from `SPEC_FACE_TARGETS_2026-07-30.md` §2 | specced, nowhere in the book |
| **What you will be able to do** | Loop A's graded success, stated as an outcome | specced, nowhere in the book |
| **Entry requirements** | the developmental arc made concrete — each school points back one | asserted, never operationalised |
| **What we do not teach** | **referral**, which is Loop A's GAP 4: *"A good ally is not always the carrier. Connection, referral, delegation, or decline can be the most skillful contribution."* The gap analysis calls this *"real missing content"* and books it for a second edition | **absent from nine chapters** |

The last row is the strongest argument for the whole feature. A school that says *"if what
they need is repair, the School of the Bridge is across the yard and better at it than we
are"* **teaches referral by performing it**, in a genre where referral is unremarkable. That
closes a documented loop gap for free, in a place a reader will actually read.

## 4 · The clause set

Six clauses, in this order, ~180–250 words total. Not every school uses every clause; a
school that skips one is characterising itself by the omission.

1. **Who we are for.** The target, in the school's own words. One or two sentences, and it
   names the person helped rather than the student.
2. **What you will be able to do.** Concrete and small. The smaller the better — a school
   that promises little and means it is more convincing than one that promises range.
3. **What it costs.** Not fees. What the training takes out of you.
4. **What we do not teach.** The referral clause. Names another school by name.
5. **Entry.** What you must already be able to do. Points back along the arc.
6. **A word from the Head.** The one place first person appears, and the only place the
   Head's single biographical fact may be spent.

## 5 · Constraints, all of them already ruled

- **`HEAD_REGISTERS` rule 1 holds.** No Head names a channel, a feeling-word, or an
  operation. The handbook describes; Chapter 3 names.
- **One fact per Head, reused.** Clause 6 may reference the Head's single fact. It may not
  add a second. `PRODUCTION_PLAN`'s do-not-build list bans backstory.
- **First person only where the cost is** — so clauses 1–5 are institutional *we*, and
  clause 6 is *I*. That asymmetry is the register doing its job for free.
- **Nothing crosses the membrane.** No clause mentions the book, the chapter, the reader-as-
  reader, or the author. The sweep will enforce this: `seam_sweep.py` brackets from Section 1
  today and must be widened to start at the handbook.
- **Banned-word gate applies.** *Rooms* in particular — an admissions page wants to say
  "read the room" and cannot.

## 6 · Worked sample — the School of the Line (ch4)

Ash is the only Head whose register landed and whose facts are filled, so he is the honest
test case.

> **THE SCHOOL OF THE LINE**
> *for those considering the second treatise*
>
> **Who we are for.** The person whose *no* does not carry. They have refused twice,
> pleasantly, and been heard both times as opening a negotiation. We do not train them. They
> are not the problem. We train the person standing next to them who has the standing to
> spend and has not spent it.
>
> **What you will be able to do.** Say one sentence and not add a second. That is the entire
> curriculum. Most students need a year.
>
> **What it costs.** You will be unwelcome. Not always and not forever, but reliably, and
> sooner than you have planned for. Students who need to be liked do finish. They finish
> slower and they pay in instalments.
>
> **What we do not teach.** Repair. If what the situation needs is a relationship that
> survives the line, the School of the Bridge is across the yard and better at it than we
> are. Send them. Sending them is not a failure of this school; failing to is.
>
> **Entry.** You must be able to name what you felt in the last moment you said nothing. If
> you cannot, the School of the Body takes first-years every season and we will still be here.
>
> **A word from the Head.** I was told at nineteen that a clean no was aggression, by people
> who meant well, and I believed them for another thirty years. I am not going to argue you
> out of the same instruction. I am going to make you say the sentence out loud until you can
> hear which one of us is right.

248 words. No channel named, no second fact, institutional *we* through five clauses and *I*
only in the last. The referral clause names the School of the Bridge and gives it away
without hedging.

## 7 · Mechanism

Identical to the signature, which is now a proven pattern: a `HANDBOOK` dict in
`marginalia/insertions.py`, a fourth entry in `compile.py`'s `KINDS`, and an anchor. The
anchor is the end of the `EPIGRAPH-BYLINE` block, which is inserted before it in the same
pass, so ordering is deterministic.

Two things must be done or the frame corrupts:

- **`KINDS` must learn the new kind** or `--strip` orphans the block and `--apply`
  duplicates it, compounding every cycle.
- **`--verify` must pass** before and after. It round-trips every chapter to byte-identical
  body text and is the only real proof.

`seam_sweep.py` needs its bracket moved up to the handbook, or six new blocks of Head prose
go unmeasured.

## 8 · What Wendell supplies

1. **Sign-off on the clause set and the order** (§4), and on the sample's register (§6).
2. **The four missing Head facts** — `VOSS-SPAN`, `QUILL-CLAUSE`, `VALE-SYSTEM`,
   `ORR-DEFLECTION`. Clause 6 cannot be written without them, for five of the six.
3. **The referral map.** Which school each school sends people to. Ash → Bridge is obvious;
   the other five are a ruling, and they are worth getting right because this is the book's
   only teaching on not being the carrier.
4. **Whether the Horizon gets one.** `MARGIN_ARC` establishes that the Horizon was a place
   before it was a school and that the annotator is the one who stopped saying it that way.
   An admissions page for the Horizon touches that, and the ch8 reveal is worth protecting.

## 9 · Risks

- **Length.** Six pages of new front-of-chapter material in a book that was just cut from 219
  named units to 99. It adds words, not units, and the reader can skip a prospectus in a way
  they cannot skip a move list — but it is real and it should be watched.
- **The joke wearing out.** Six of anything is where a bit becomes a format. The defence is
  clause omission: a school that declines to state what it costs has told you something.
- **Competing with the Exile.** Section 1 already explains why the Face left the village. The
  handbook must not re-explain it. The handbook says who the school is *for*; the Exile says
  why it *exists*. Different questions, and the drafts should be checked against each other.

## 10 · How this gets checked

```
python3 marginalia/compile.py --verify            # must round-trip, before and after
python3 instruments/gate.py                       # rooms/quiet/genuinely in six new pages
python3 instruments/on_body.py 'python3 instruments/seam_sweep.py'   # bracket must start at the handbook
grep -c "School of the" manuscript/ch[3-8].md     # every referral clause names one
```
