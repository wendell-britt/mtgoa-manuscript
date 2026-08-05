# SOURCE — the six superpowers, book side and page side

**Created:** 2026-08-04
**Why this file exists:** `ch9:664` now routes the reader to masteringallyship.com for the superpower
she built out of her own history. The page sits outside the repo, so no instrument here can read it:
`gate.py` cannot scan it, `citation_audit.py` cannot check it, `compile.py --verify` cannot
round-trip it. **Drift between what the page says and what the book says would be invisible.**
This file is the drift check, and it is the third condition of
`SUPERPOWER_PLACEMENT_6FACE_ANALYSIS.md`.

**What the page is, ruled 2026-08-04:** it diagnoses **the superpowers, not the Faces**. See the section
below on why that distinction had to reach the prose.

**Status:** book side filled from the manuscript. **Page side is empty and only Wendell can fill
it** — the environment's network policy blocks masteringallyship.com, so the page could not be
read from here. Not drafted, on the `author-slot` rule: inventing what the page says is exactly
the failure that rule exists to prevent.

**Not a shipping surface.** `placeholders.py` scans `manuscript/`, `appendices/`, `front_matter/`
and `back_matter/` only, so the slots below cannot reach a reader or raise shipcheck's placeholder
count. Verified 2026-08-04.

---

## The six, as the book has them

Each is quoted or closely paraphrased from the site named. These are the strings the page has to
agree with.

### Shaman — **the Alchemist** · `ch3:756`

> The superpower under that move is the Alchemist. The Alchemist is the one who takes the charge
> the Controller called a foul (the fear, the "not ready," the "not yet") and spends it.

`WENDELL:` the page's wording for the Alchemist.

### Challenger — **the Disruptor** · `ch4:597`

> The Challenger's superpower is the willingness to be unwelcome on a charge you have checked and
> chosen to trust, clarity without cruelty, held steady long enough to say one sentence and stay
> for what follows.

`WENDELL:` the page's wording for the Disruptor.

### Regent — **the Storyteller** · `ch5:597`

> That lays the foundation of the Regent's superpower, and the superpower is the Storyteller: what
> you received, put into a form the next person can receive. The account of where this came from,
> what it cost, what broke, what still holds, and why any of it is worth their time.

Named 2026-08-04 by Wendell's ruling. **If the page predates that ruling it will not carry this
name at all** — first thing to check.

`WENDELL:` the page's wording for the Storyteller.

### Architect — **the Strategist** · `ch6:464`

> The Architect's superpower is the Strategist: knowing where the push goes and when to make it,
> and then, because you also know what the map is for, building the thing so the next person can
> run it without you.

Named 2026-08-04 by the same ruling, same caveat. Note also that **Strategist is the Fire/Anger
mode in the ch6 table at `ch6:285`** — the only Face where the superpower shares a name with one
of its own five modes. If the page lists modes as well, it will collide there and the collision is
known and accepted.

`WENDELL:` the page's wording for the Strategist.

### Diplomat — **the Connector** · `ch7:592`

> The Diplomat's superpower is not making contact; the Bridge-Builder does that in the first hour.
> It is connection that has survived being told the truth.

`WENDELL:` the page's wording for the Connector.

### Sage — **Escape Artist + Coach**, a compound · `ch8:639`

> The Escape Artist half is the capacity to get out of a game… The Coach half is what the exit
> makes available. A coach who cannot leave the game is not coaching.

The only compound of the six. **A page that lists six single names will be wrong here**, and this
is the likeliest drift site in the set.

`WENDELL:` the page's wording for the Sage compound.

---

## TEAL side — the definitions in the source manuscript

`MTGOA_TEAL_080525.md` is the earlier version of the text the superpower content came from, and it
carries **all six**, each with a full chapter: Alchemist 123 mentions, Storyteller 155, Strategist
131, Connector 135, Escape Artist 133, Disruptor 117. **These are not the page**, and they do not
fill the `WENDELL:` slots above — but if the page was built from this material, this is the closest
thing to it the repo holds, and it is what the drift check can run against today.

| Superpower | TEAL | The definition as TEAL states it |
|---|---|---|
| **Alchemist** | `:14236` | "carries the rare ability to transform raw emotional charge into usable power. Where others recoil from grief, anger, or despair, the Alchemist listens for the signal inside the storm." |
| **Strategist** | `:5528` | "carry the superpower of clarity in complexity. They are the cartographers of chaos, mapping patterns where others see only noise. Their gift is not just seeing what is, but intuiting what will be." |
| **Connector** | `:7156` | "gift is a living network, a weave of threads, bridges, and gathering spaces. Through their presence, strangers become acquaintances, acquaintances become friends, and friends become co-conspirators." |
| **Disruptor** | `:11992` | "Some powers arrive quietly, slipping into the room like intuition. The Disruptor does not. This superpower is the sound of glass breaking, of silence cracking open, of a truth too jagged to leave unspoken." |
| **Escape Artist** | `:9188` | "honors the wisdom of fear… Their gift is movement, not just toward, but away, aside, beneath, beyond. They are the ones who know that retreat, well-timed and intentional, can be as powerful as a charge." |
| **Storyteller** | `:16788` | "gift is poignance, the art of feeling the weight of loss and weaving it into meaning. Where others see only fragments, the Storyteller threads them into coherence." |

### What TEAL settles, and it is the important thing

**In TEAL, superpower and Face are two axes that cross. In the book they are one axis.**

The Strategist chapter walks all six Faces by name and hyphenates them: *the Shaman-Strategist*,
*the Challenger-Strategist*, *the Regent-Strategist*, *the Diplomat-Strategist*, *the
Sage-Strategist* (`:6472`–`:6552`). The Escape Artist section names Faces 63 times. So the source
model is a **6 × 6**: any superpower can be played through any Face.

The book collapsed that to a **1:1** — each Face chapter names one superpower — which is a
book-era design decision layered on the source rather than something the source says.

**This is why `ch9:664` had to be corrected**, and it turns out to be righter than the reasoning
that produced it. The page diagnoses superpowers; the book's sheet line derives one from her Face.
On the TEAL model those are independent axes, so the two answers *routinely* differ, and the
sentence now in the book —

> Its answer does not have to match the superpower your Face came with.

— is not a hedge about two instruments disagreeing at the margin. It is the source model stated
plainly.

**Two smaller findings:**

- **Coach appears 8 times in TEAL**, against 117–155 for each of the six. The Sage's
  *Escape Artist + Coach* compound at `ch8:639` is book-era, not source. A page built from TEAL
  will almost certainly carry **Escape Artist alone**, which is drift test 2 firing before anyone
  has looked at the page.
- **TEAL's Storyteller is Water** — *"poignance… the weight of loss"*. The book gives the
  Storyteller to the **Regent**, whose material is inheritance and stewardship, and puts
  poignance/Water on the Regent's Optimizer-equivalent instead. Same name, adjacent but not
  identical claim. Worth a look when the page arrives.

---

## The reader's own superpower, which is a different object

`ch2:334` defines the personal superpower, and the `ch9:664` pointer could plausibly be read as
routing to either instrument:

> Your superpower is the reliable capacity you built to survive your wounds, once that capacity is
> made conscious, ethical, and usable in service of others.
>
> Formula: **adaptation under pressure → conscious integration → intentional contribution**.

**ANSWERED 2026-08-04, by Wendell: the page diagnoses the superpowers, not the Faces.** So the page
answers *this* question — the wound-derived one — and not the Face-derived one the six sections above
carry.

**That distinction is load-bearing and the book nearly lost it.** `ch2:334`'s superpower is built from
what happened to her. The six at `ch3`–`ch8` are built from a Face. They share a word and they are not
the same object, and a reader who runs both instruments can get two different answers with nothing
telling her that is expected. The first version of the `ch9:664` pointer called the page *a longer
version of this*, which read the two as one thing. Corrected the same day:

> (The one you built out of your own history is a different question, and the page at
> masteringallyship.com answers it. Its answer does not have to match the superpower your Face came
> with.)

The sheet line above it still routes through her Face, which is what keeps it answerable with the book
shut. The page is the second instrument, named as a second instrument.

---

## The drift check

Run by eye whenever the page changes or the book's superpower sites change:

1. **All six names present on the page**, spelled as above.
2. **The Sage is a compound**, not a single name.
3. **Storyteller and Strategist appear at all** — both were named 2026-08-04 and any page built
   before that date predates them.
4. **No seventh superpower.** Face-attachment is *not* a drift test: the page diagnoses superpowers
   directly and may not organise by Face at all. What would be a defect is the page implying a reader's
   superpower follows from her Face, since `ch2:334` derives it from her history instead, and `ch9:664`
   now says in the book that the two answers need not match.
5. **The page does not explain the six as a set in a way the book contradicts.** The book teaches
   each at its own altitude and never as a table; the page may table them, and that is fine as
   long as no definition disagrees with the quotes above.
6. **The page still exists at masteringallyship.com** and the book's parenthetical still describes
   what it does. `ch9:664` and `ch1:83` are the two sites that point out; DL-20's rule is that a
   printed pointer cannot be patched.

---

## Checking the pages

**Two pointers leave the book**, and neither is checkable from this repo:

| Site | Points at | What the book claims about it | Verified? |
|---|---|---|---|
| `ch9:664` | the superpower page | it answers the superpower you built out of your own history, and its answer need not match your Face's | **no** |
| `ch1:83` | the Myths Read | it marks which of the ten myths are yours **and takes each one apart** | **no** |

`ch1:83`'s claim is the sharper one, because it was narrowed to make it true. It previously read
*hands each one back with the page that takes it apart*, which on one reading promised the **book**
took apart all ten, and A3 records that only 9 of 10 do. The fix moved the job to the site, which is
correct only if the site actually does it for all ten, **including *helping the less powerful***, the
one the book leaves alone. **That is the single most important thing to check on either page.**

**Why this stays manual, and when it stops.** Both pages sit outside every instrument here, and this
environment's network policy blocks masteringallyship.com, so no automated check is possible today.
**Wendell, 2026-08-04: this gets easy once the manuscript is added to the bars-engine repo** — with
book and pages under one roof, both claims become greppable and the drift check below becomes a
script rather than a reading. Until then it is a reading, and this file is where it is recorded.
