# Canon collision — the book's 1:1 against `CANONICAL_ALLYSHIP_SUPERPOWERS.md`

**Created:** 2026-08-05
**The canon:** `CANONICAL_ALLYSHIP_SUPERPOWERS.md`, on `codex/ch2-editorial-review-2026-08-02`,
authored by codex. Declares itself *"the repository-local source of truth for the superpower
taxonomy."*
**The book:** `manuscript/ch2.md`–`ch9.md` on this branch.
**Status:** comparison, three paths, **Path C ruled and APPLIED 2026-08-05.**

**Applied, eight edits.** Seven drafted and reviewed, one found during application:
`ch3:756`, `ch3:977` (found in the sweep — a second possessive, *The Challenger's superpower is the
ability to name what's unacceptable*, now *The next chapter trains…*), `ch4:597`, `ch5:597`,
`ch6:464`, `ch7:592`, `ch8:639` twice (the compound and the Coach half), and the new distinction
sentence after `ch2:334`. Book-wide `review.py` green on all six; round-trip byte-identical.

**The membrane held.** Re-counted after applying: **0** unquoted *school* mentions in the teaching
voice of every one of ch3–ch8, unchanged from before the sweep. The word *school* appears in the
new prose exactly once, at `ch2:334`, in the voice that already discusses the apparatus at
`ch2:236`.

**`ch6:628` closed 2026-08-05**, a ninth edit, on Wendell's word. It read *"Intent, though, is not
the superpower. The superpower is the Strategist."* Repeating the sweep's phrasing would have put
*this chapter trains the Strategist* into ch6 twice, so the fix went the other way: the passage's
work is a **contrast** — structural generosity is the intent, and the Strategist is the thing the
intent is not — so *superpower* becomes *skill* and the site stops making a taxonomy claim at all.
The chapter's one binding now lives at `ch6:464` and nowhere else.

**Corrected the same day, twice over.** The first attempt read *"The skill is the Strategist"*, and
Wendell: *"awkward. The skill isn't the Strategist. The Strategist is the name for the superpower."*
Subject and predicate were the wrong way round — a name was being equated with the thing it names.
He also caught **`the push`**, a definite article with nothing behind it. Final:

> Intent, though, is not the skill. **Strategist** names the skill: knowing where a small push
> moves the most, and when to make it.

`Strategist` now does what a name does, and the push is indefinite and self-contained, echoing the
chapter's own formulation at `ch6:485`: *"where does the smallest push create the largest
movement?"*

**Measured against the shipped sentence:** `be 2.59 → 2.07 · copula 2.58 → 1.72 · waste 1.93 →
1.85`. The residual heaviness belongs to the neighbouring shipped sentences, which is what the
voice linter's abstraction-in-subject warning points at.

**`ch6:464` uses `the push` as well and is left alone**, because there it has an antecedent two
paragraphs up at `ch6:462`: *"the pressure has built to the point that one push will do what a year
of argument could not."* Recoverable, so the article is earned. `ch6:628` sat 164 lines downstream
of that with nothing in between, which is what made it orphaned rather than merely repeated.

**Full inventory after the sweep**, every remaining *superpower* in the manuscript, classified by
which side of the membrane it sits on:

| Site | Side | What it is | Verdict |
|---|---|---|---|
| `ch2:95`, `ch2:334`, `ch2:340`, `ch2:341` | teaching | the reader's own, wound-derived, second person | correct, must stay |
| `ch2:345` | teaching | the new distinction sentence | applied 2026-08-05 |
| `ch3:213` | **fiction** | *"That is the Shaman's superpower"* | **left, correctly** — see below |
| `ch3:985` | teaching | *"The system did not give you your superpower"*, the reader's own | correct |
| `ch7:810` | teaching | chapter-summary bullet: *"The Diplomat's twenty cards, and the superpower they are for: Connector"* | **open, see below** |
| `ch8:576` | teaching | no binding; the word appears in unrelated prose | fine |
| `ch9:83`, `ch9:664` | teaching | the toolkit line and the sheet line | fine |

**`ch3:213` is the sweep stopping at the membrane, and that is the correct behaviour.** It sits at
line 213 against ch3's signature at 245, so it is inside the treatise — **Maera Voss, Keeper of
First Signals, Head of the School of the Body**, speaking. Her own paragraph two lines up says
*"harder than anything else the School of the Body teaches."* A character in the fiction may call
emotional alchemy the Shaman's superpower; that is her voice, not the book asserting a taxonomy.
Sweeping it would have done the reverse of the damage this sweep was checked for — flattening the
fiction into the teaching text instead of the other way round.

**`ch7:810` is genuinely open.** *"The Diplomat's twenty cards, and the superpower they are for:
Connector"* binds a Face's card set to a superpower rather than the Face itself, and cards are not
in the canon's forbidden list (Face, Domain, Role). The deck's own architecture may group those
twenty cards by superpower, in which case the bullet is a fact about the deck. Not edited without
a ruling.

**Shape of the branch, which matters for anything that follows:** 346 files, **none in
`manuscript/`**, 71 commits, and **no merge base with `master`**. It is a parallel documentation
line pushed into this repo, not a fork of the book. Nothing can be merged from it in the ordinary
way; the file would be copied across, or the book would reference it where it stands.

---

## 1 · What agrees

- **The six names match exactly:** Connector, Strategist, Disruptor, Escape Artist, Alchemist,
  Storyteller. The book, the canon, and `MTGOA_TEAL_080525.md` all carry the same set.
- **Five of the six definitions are compatible**, the canon's being broader and the book's being
  the same claim narrowed to one altitude.
- **`ch2:334` and the canon's short form agree almost word for word.** The book: *"the reliable
  capacity you built to survive your wounds."* The canon: *"shaped by practiced gifts, lived
  experience, and playstyle."* Same object.
- **Neither treats a superpower as a moral rank or a fixed identity.**

## 2 · What conflicts

### 2.1 The 1:1 map — the live one

> **Canon, Chapter rules:** *Do not map Superpower → Face, Superpower → Domain, or Superpower →
> Role one-to-one.*
> **Canon, Non-Negotiable Distinctions:** *The six Face chapters are therefore **not** one chapter
> per superpower.*

The book maps 1:1 at all six sites, and five of the six use the possessive, which is the strongest
ownership phrasing available:

| Site | The sentence | Form |
|---|---|---|
| `ch3:756` | The superpower under that move is the Alchemist. | attached to a move |
| `ch4:597` | **The Challenger's superpower** is the willingness to be unwelcome… | possessive |
| `ch5:597` | **the Regent's superpower**, and the superpower is the Storyteller | possessive |
| `ch6:464` | **The Architect's superpower** is the Strategist | possessive |
| `ch7:592` | **The Diplomat's superpower** is not making contact… | possessive |
| `ch8:639` | **the Sage's superpower** … Escape Artist half … Coach half | possessive |

**Four of the six predate 2026-08-04.** The ruling that day named the Regent's the Storyteller and
the Architect's the Strategist, which **completed** a map that had been 4-of-6 and incomplete. The
book moved further from the canon that day, not closer, and the canon was not visible from here at
the time.

**Where it reaches the reader:** `ch9:664` instructs her to write *"the superpower its chapter
named"* — the 1:1 arriving as an action rather than a description. The sentence immediately after
it does concede the point: *"Its answer does not have to match the superpower your Face came
with."* So the book already half-states the distinction the canon asks for.

### 2.2 Coach

> **Canon:** Coach is *"a cross-cutting, integrative practice… not a seventh primary territory and
> must not be a seventh forced-choice quiz result."*

`ch8:639` makes Coach **half of a superpower belonging to a Face**, which breaks the Coach rule and
the 1:1 rule in a single sentence. **The content agrees and only the taxonomy collides:** the
canon's Coach *"sees the next level a person is avoiding… returns agency to its owner… speaks to the
person one level up without carrying them there"* is what ch8's Coach half does.

This needs its own call under **either** path below. It is not covered by a seating exception.

### 2.3 The epithets and shadow names — zero adoption

The canon gives every superpower a second name and two named shadows. **Not one appears in the
manuscript:**

| | canon's second name | shadows | hits in `manuscript/` |
|---|---|---|---|
| Connector | the Webweaver | — | **0** |
| Strategist | the System Seer | — | **0** |
| Disruptor | the Sacred Spark | Chaos Bringer, Caged Rebel | **0 / 0 / 0** |
| Escape Artist | the Framebreaker | Ghost, Martyr | **0 / 0 / 1** |
| Alchemist | the Emotional Transmuter | Emotional Overload, Detached Observer | **0** |
| Storyteller | the Meaning Weaver | Manipulator, Lost Author | **0** |
| Coach | — | Taskmaster, Empty Cheerleader | **0 / 0** |

Not a defect on its own. It becomes one the moment the quiz returns *"Connector — the Webweaver"*
to a reader holding a book that never uses the word. **`ch9:664` points at that quiz.**

Note also `System Seer` against ch8's `Panoramic Seer` mode — two Seers on different Faces.

### 2.4 Storyteller now has three definitions

| Source | The claim |
|---|---|
| **Canon** | shapes *"meaning, memory, morale, narrative, and public imagination"* |
| **TEAL** `:16788` | *"poignance, the art of feeling the weight of loss and weaving it into meaning"* |
| **Book** `ch5:597` | what you received, put into a form the next person can receive: the account of where this came from, what it cost |

The book's is the narrowest and the furthest from canon, and it is the one named on 2026-08-04.
The canon's Storyteller would sit as comfortably in ch8 as in ch5, which is itself an argument for
the canon's position.

---

## 3 · Path A — rule the seating an architecture exception

**Premise:** the canon's own escape hatch. *"Do not relabel a Face chapter as a superpower chapter
**unless the manuscript architecture explicitly changes.**"* The book is not relabelling chapters;
it names one superpower inside each Face chapter as the place that capacity is easiest to watch.
Rule that as deliberate, record it, and leave the six sites alone.

**Not free.** The canon requires a Face chapter to *"state the distinction when ambiguity is
likely,"* and six possessives make ambiguity certain. Path A therefore costs **one sentence in the
book**, at `ch2:334` where the superpower is defined and before any Face chapter names one:

> A superpower is not a Face. Each chapter ahead trains one, because that is where it is easiest to
> watch, and any of the six can be run through any of them.

**And an amendment to the canon**, drafted:

> ### Exception — the manuscript's per-Face seating
>
> Ruled by Wendell, 2026-08-05. `manuscript/ch3.md`–`ch8.md` each name one superpower inside one
> Face chapter. This is **pedagogy, not taxonomy**: a chapter is the easiest place to watch one
> superpower work at one altitude. It does not claim the Face owns the superpower, and it does not
> license the quiz to map a result to a Face. Every quiz rule above stands unchanged. The
> manuscript states the distinction at `ch2:334` and again at `ch9:664`.

**Coach, under Path A:** still needs deciding. Either ch8 stops calling Coach half of a superpower,
or the canon records the compound as a second exception. The seating exception does not cover it.

**Cost:** one sentence in the manuscript, one section in the canon. **Nothing already shipped is
rewritten.**

## 4 · Path B — unwind the 1:1

Convert every possessive to a training relation, so no Face owns a superpower. Drafted, whole
sentences, six sites plus the distinction sentence:

| Site | before | after |
|---|---|---|
| `ch3:756` | The superpower under that move is the Alchemist. | **This move trains the Alchemist,** the one who takes the charge the Controller called a foul and spends it. |
| `ch4:597` | That is the Disruptor's foundation. **The Challenger's superpower is** the willingness to be unwelcome… | That is the Disruptor's foundation. **The Challenger trains it as** the willingness to be unwelcome… |
| `ch5:597` | That lays the foundation of the Regent's superpower, **and the superpower is the Storyteller:** what you received… | That lays **the foundation the Storyteller works from:** what you received… |
| `ch6:464` | **The Architect's superpower is the Strategist:** knowing where the push goes… | **The Architect trains the Strategist:** knowing where the push goes… |
| `ch7:592` | **The Diplomat's superpower is not making contact;** the Bridge-Builder does that in the first hour. | **The Diplomat trains it well past making contact,** which the Bridge-Builder does in the first hour. |
| `ch8:639` | That combination makes **the Sage's superpower** possible, and the superpower is a compound… | That combination **is what the Escape Artist runs on, and this chapter trains it beside the practice that makes an exit worth taking.** |
| `ch2:334` | — | *(the distinction sentence from Path A, which Path B also needs)* |

**Measured on the drafted replacements as a batch:** gate clean, `be 0.84 · copula 1.25 · waste
1.40 · zombie 0.70 · expletive 0.00 · passive 0.00 · empty 0.75`, voice linter clean. Waste is over
on a 160-word sample and every hit is *it* pointing at the superpower named in the same sentence.

**Note on the phrasing that did not survive drafting.** The obvious frame — *"The superpower the
Challenger trains is…"* — scored `be 1.40 · copula 1.56`, heavy on two counters, because it turns
a possessive into a relative clause and a copula six times over. The active frame above is the
version that measures clean. **Path B's cost is partly a prose cost, and it is real.**

**Path B also resolves Coach for free:** ch8's rewrite drops the compound and leaves Escape Artist
as the superpower with coaching as the practice beside it, which is the canon's position exactly.

**Cost:** six edits to shipped prose plus one new sentence, and it unwinds the naming that was
ruled on 2026-08-04 — the names stay, their ownership goes.

---

## 4.5 · Path C — the school trains the class. **RULED 2026-08-05.**

Wendell: *"a mix of A and B is necessary. It seems like the school trains certain classes (which
would be the superpowers), so this can help with the collision even though in the real world all of
the superpowers can be applied at any level."*

**This resolves the collision on a frame the book already owns.** Every Face chapter is already a
school, reader-facing, in shipped prose, and the six map one to one onto the six Faces:

| Chapter | School | trains |
|---|---|---|
| ch3 Shaman | **School of the Body** (11 uses) | the Alchemist |
| ch4 Challenger | **School of the Line** (5) | the Disruptor |
| ch5 Regent | **School of the Oath** (5) | the Storyteller |
| ch6 Architect | **School of the Pattern** (10) | the Strategist |
| ch7 Diplomat | **School of the Bridge** (8) | the Connector |
| ch8 Sage | **School of the Horizon** (5) | the Escape Artist |

A school **trains** a class. It does not own it, and a graduate uses it anywhere. That is Path B's
compliance — no Face possesses a superpower — carried by Path A's seating, which survives intact
because a school teaching one class is what a school is for. `ch2:236` already states the principle
the ruling needs: *"The school is somewhere to stand while you practice, and that is the whole of
its job."*

**Against the canon:** *Do not map Superpower → Face one-to-one* is satisfied, because the mapping
is now school-to-curriculum rather than Face-to-property. **Coach resolves inside ch8's rewrite**,
where the compound becomes a class and a practice, which is the canon's position.

**Measured against the same six spans as they currently stand:**

| | be | copula | waste | zombie | expletive | passive | empty |
|---|---|---|---|---|---|---|---|
| the six sites now | 1.23 | 2.29 | 0.94 | 0.83 | 2.31 | 1.00 | 0.67 |
| Path C | **0.86** | **1.37** | 1.05 | 0.79 | **0.00** | 1.28 | 0.85 |

Better on five of seven, and the two that rise stay in band. Copula still reads over 1.30 and it is
**inherited**: the current prose runs 2.29 there, so Path C cuts it by 40% without reaching the
line. Gate clean, voice linter clean.

**Path C is what gets drafted and applied. A and B below are kept as the record of what was
weighed.**

---

## 5 · Recommendation

**Path A**, with a separate ruling on Coach.

The per-Face seating is load-bearing pedagogy: the Alchemist means something after ch3 teaches
charge and nothing before it, and that sequencing is why the book has six Face chapters rather than
six superpower chapters. The canon is written to govern **the quiz**, where 1:1 mapping would
genuinely mislead a reader into thinking her Face determines her leverage. Nothing in the canon is
harmed by a book that seats a superpower per chapter while telling the reader plainly that the two
axes are independent — and `ch9:664` already tells her that.

Path B is the more literal compliance and it costs six edits to shipped prose, a measurable prose
penalty in the natural phrasing, and the reversal of a ruling made yesterday.

**On Coach I lean the other way: take the canon's position.** ch8's compound is book-era — Coach
appears 8 times in TEAL against 117–155 for each of the six — and the canon's reasoning is sound:
a coaching move is a thing you do for another person, not a territory you occupy. That is one
edit, at `ch8:639`, and it does not depend on which path is chosen for the seating.

---

## 6 · What neither path fixes

- **The epithets.** If the quiz returns second names the book never uses, the reader meets new
  vocabulary at the moment `ch9:664` sends her out. Either the book adopts them, the quiz drops
  them, or somebody decides the mismatch is acceptable. **Nobody has looked at the live page yet**
  — see `SOURCES/SUPERPOWERS_PAGE.md`, where the page-side slots are still empty.
- **Storyteller's three definitions.** The book's is the narrowest of the three and is not obviously
  the Regent's material rather than the Sage's.
- **The branch has no merge base.** However this resolves, somebody has to decide whether the canon
  file lives in this repo or is referenced where it stands.
