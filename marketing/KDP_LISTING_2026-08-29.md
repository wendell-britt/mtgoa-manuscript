---
type: copy
title: "KDP listing — description, keywords, and what a proof needs"
aliases:
  - kdp listing
  - amazon description
tags:
  - marketing
  - mtgoa
  - kdp
  - print
created: 2026-08-29
review: 2026-09-15
source:
  - marketing/ANALYSIS_KDP_DESCRIPTION_2026-08-27.md
  - marketing/BACK_COVER_2026-08-27.md
---

# KDP listing — description, keywords, and what a proof needs

**Wendell, 2026-08-29:** *"a description that I can put on Amazon to setup KDP publishing for
Mastering Allyship so that I can get a proof of the book in the next week or so."*

**The goal is a proof, not a launch, and that changes what has to be right.** A KDP description is
**editable at any time**, so nothing here needs to wait on the keyword hour. **Publish with this,
order the proof, refine the listing while the proof is in the post.**

---

## The description — paste this

**475 words, 2,527 characters plain and 2,690 with the HTML.** Both well under the 4,000 ceiling,
because a description is read standing up.

You started this work for a reason. It's just gotten hard to hear that reason over all the noise of seeming like you're doing a good job.

You are the one who notices. You catch the meeting where somebody gets talked over, the decision that lands on whoever can least afford to absorb it, and the group chat where everybody stops typing for four hours and then carries on. You move, because you can see it and you cannot leave it alone, and moving costs you more than you have told anyone.

You have read the books that explain what is wrong. Every one of them points at the problem, and not one of them hands you a move.

This is a field guide, so it tells you what you are looking at.

A group runs on six roles. One person cracks the joke that lets everybody breathe, one says the rule out loud, and one rebuilds the process so it cannot happen again. Those are three of the six, and most people reach for the same one every time.

A feeling travels one of five channels: anger, fear, sadness, joy, or the flat calm that is none of them. Each one reports something different about what the situation needs next, and you learn to read which is running before it starts driving.

The same form runs under the roles and the channels alike, in five moves: Wake Up, Open Up, Clean Up, Grow Up, Show Up. Form here means what it means in a dojo, a fixed order you run until your body has it. It takes ninety seconds in a hallway or a year with one person.

Learn the form once and each role bends it a different way, which is where the thirty moves come from and why the sixth role is not six times the work.

A hundred and twenty prompts cross those moves against the four domains where allyship leaves your head: gathering resources, raising awareness, direct action, and skillful organizing.

Burnout here is a design flaw that looks exactly like a character flaw. It arrives as the yes that costs a weekend, the favor that turns into a standing arrangement, and the meeting that ends with the person who named the problem owning it. You can change a design.

Wendell Britt built a course on this material in 2020. Under ten percent of the people who started it finished. He spent the years since finding out why, and rebuilt the method around the answer. This book is what came out.

This is for the person still showing up and running out of road. It will not tell you to care more, because you already do. It teaches the moves instead, so that on Monday you can do more than notice.

Skip it if you are looking for a script.

## The same copy with KDP's HTML

**KDP accepts a small tag set and strips everything else.** Bold and lists survive, so the five
specifics become scannable, which is the whole reason to use markup at all — **a browser scanning
twenty listings reads the bolded sentence and moves on.**

**Each list item bolds its first complete sentence and nothing else.** No bold inside a sentence,
which is a formatting-slop pattern `no-ai-slop` names by itself, and no fragment used as a label.

```html
<p><b>You started this work for a reason. It's just gotten hard to hear that reason over all the noise of seeming like you're doing a good job.</b></p>
<p>You are the one who notices. You catch the meeting where somebody gets talked over, the decision that lands on whoever can least afford to absorb it, and the group chat where everybody stops typing for four hours and then carries on. You move, because you can see it and you cannot leave it alone, and moving costs you more than you have told anyone.</p>
<p>You have read the books that explain what is wrong. Every one of them points at the problem, and not one of them hands you a move.</p>
<p><b>This is a field guide, so it tells you what you are looking at.</b></p>
<ul>
<li><b>A group runs on six roles.</b> One person cracks the joke that lets everybody breathe, one says the rule out loud, and one rebuilds the process so it cannot happen again. Those are three of the six, and most people reach for the same one every time.</li>
<li><b>A feeling travels one of five channels: anger, fear, sadness, joy, or the flat calm that is none of them.</b> Each one reports something different about what the situation needs next, and you learn to read which is running before it starts driving.</li>
<li><b>The same form runs under the roles and the channels alike, in five moves: Wake Up, Open Up, Clean Up, Grow Up, Show Up.</b> Form here means what it means in a dojo, a fixed order you run until your body has it. It takes ninety seconds in a hallway or a year with one person.</li>
<li><b>Learn the form once and each role bends it a different way, which is where the thirty moves come from and why the sixth role is not six times the work.</b></li>
<li><b>A hundred and twenty prompts cross those moves against the four domains where allyship leaves your head: gathering resources, raising awareness, direct action, and skillful organizing.</b></li>
</ul>
<p>Burnout here is a design flaw that looks exactly like a character flaw. It arrives as the yes that costs a weekend, the favor that turns into a standing arrangement, and the meeting that ends with the person who named the problem owning it. You can change a design.</p>
<p>Wendell Britt built a course on this material in 2020. <b>Under ten percent of the people who started it finished.</b> He spent the years since finding out why, and rebuilt the method around the answer. This book is what came out.</p>
<p>This is for the person still showing up and running out of road. It will not tell you to care more, because you already do. It teaches the moves instead, so that on Monday you can do more than notice.</p>
<p><i>Skip it if you are looking for a script.</i></p>
```

**2,690 bytes with the tags, and every byte is ASCII** — no smart quotes, no em dashes, so the
count Amazon sees is the count above. **Stripped of tags it is byte-identical to the plain body
above**, checked rather than assumed, so there is only one text to keep true.

## Keywords — provisional, and that is fine

**These are ideation, not measurement**, per `ANALYSIS_KDP_DESCRIPTION` §5a — a language model has
no Amazon search-volume data. **Put them in to publish, then spend the free hour with Amazon's
autocomplete and replace whatever does not complete.** Spaces, not commas. Nothing already in the
title.

```
1  compassion fatigue helper burnout recovery
2  emotional labor exhaustion at work
3  setting boundaries with someone you love
4  how to help without losing yourself
5  rebuilding trust after conflict apology
6  anger sadness fear joy self regulation
7  dei inclusion facilitation group dynamics
```

**269 bytes of 350, every mechanical rule checked** by `instruments/kdp_keywords.py` — 50
bytes per field not 50 characters, ASCII only, no commas, nothing already in the title or
the author name, no word repeated across the seven, and no prohibited term.

**Field 5 was replaced after a delivery audit against the manuscript.** *"people pleasing
overfunctioning saying no"* named two concepts the book does not have: `people pleasing`
returns 4 incidental hits and `overfunctioning` returns 0, with no synonym behind it.
**A keyword may use the reader's vocabulary rather than the book's, but it has to name
something the book delivers** — and *compassion fatigue* (0 in the text, the whole premise
in substance) passes that test where *overfunctioning* does not. The replacement points at
ch7:726's named structure for repair: `repair` 84, `trust` 53, `conflict` 31, `apology` 19,
and nothing in the seven fields had been aimed at it.

**Validation is `marketing/RESEARCH_KEYWORD_VALIDATION_2026-08-29.md`.** Two passes at two
times, both free, neither runnable from this session — every Amazon host is 403 at the
egress proxy.

**Categories: pick for the exhausted helper, not the corporate buyer.** Same reasoning as §3 of the
analysis — the L&D buyer arrives through `/speaking`, which is built and priced for them.

## What actually gates the proof, and it is not the description

**1 · The interior was rebuilt today, 2026-08-29.** The subtitle ruling changed the title page and
the old build still carried *How to Build an Allyship Practice That Lasts*. **Upload
`build/MTGOA_2026-08-29_trade.pdf`** — 387 pages, 28 components, every opener on a recto, folio
continuous. **Not the 08-13 file**, which is now wrong on the title page.

**2 · The cover wrap does not exist yet.** A front cover exists; KDP print needs **front, spine and
back as one flat file**. Computed for 387 pages at 6×9:

| paper | spine | full wrap, with 0.125" bleed |
|---|---|---|
| white | **0.8715"** | 13.1215 × 9.25 in |
| cream | **0.9675"** | 13.2175 × 9.25 in |

**Do not build from those numbers.** Use **KDP's Cover Template Generator** — trim size, page
count, paper colour in, exact PNG and PDF template out, with the spine and barcode zones drawn.
**It is free and it is authoritative**, and it removes the one measurement most likely to send a
proof back.

**3 · Margins.** KDP requires a wider inside margin as page count grows, and 387 pages is in the
band where it matters. **The remedy is to stop guessing: upload and run KDP's Print Previewer**,
which flags margin and bleed problems before you pay for anything. **Free, immediate, and more
authoritative than any spec I could quote.**

**4 · ISBN — superseded 2026-08-29 by `DECISION_ISBN_2026-08-29.md`.** This section said *buy
the ISBN* before ordering the proof. **The proof does not depend on it.** You cannot change an
ISBN on a *published* KDP book, but you can change it freely while the book is in **Draft**, and
proof copies can be ordered from Draft and print marked *Not For Resale*. **So take the free KDP
ISBN today, order the proof, and buy Bowker's block of ten before you publish** — $295 at $29.50
each, against $125 for a single, with the paperback, the backer print run, the audiobook, the
workbook and *Allyship at Work* all needing one.

**5 · The back cover copy and jacket bio are done.**
`marketing/BACK_COVER_2026-08-27.md` and `marketing/AUTHOR_BIO_2026-08-27.md`, both through the
full pass. They go in the wrap, not in KDP's fields.

## The review pass

**Step 0 · ELI5 first.** *You keep helping people and it keeps wearing you out. This book says the
problem is not that you care wrong, it is that nobody taught you the moves. It names six ways of
helping, shows which one you reach for under pressure, and gives you thirty moves to actually make.*
The register version adds the specifics and the credential and nothing else.

**Three real defects, found and fixed.**

| step | found | fix |
|---|---|---|
| **1 · gate** | **HARD FAIL** — *"a list of things to say"*. `things` is a banned word | *"a script"*, which is sharper and shorter |
| **2 · diet** | `inchoative` **11.57**, a DEFECT — *"allyship stops being private and goes external"*, an abstraction wearing a verb of motion | Named the four domains outright. **Kills the defect and adds four concrete searchable nouns**, so the fix pays twice |
| **2 · diet** | `expletive` **1.60** — *"It is for the person still showing up"* | *"For the person still showing up"* |
| **canon** | **Factual error.** *"Thirty moves"* and *"a five-move form"* were listed as two features. `ch3:746-798` shows the Shaman's five moves **are** the Form, and `ch1:260` says every school after uses the same form and teaches its own changes | **The thirty moves are six roles × the Form.** Rewritten to show the relation, which is also the `LIKE WILBER` fix — one thing at two levels had been presented as two things |
| **1 · gate** | **HARD FAIL** on the rewrite — *"not a sixth thing to learn"* | *"not six times the work"* |

**The `goes external` one is worth noting.** That phrase is the book's own, at `ch3:876`. **New
marketing prose does not get to inherit a defect because the manuscript carries it** — and naming
the domains was better copy anyway.

**Measured at that point:** `voice` clean · `gate` clean · `expletive` **0.00** · `passive`
**0.00** · `empty` **0.00** · `inchoative` **0.00** · `be` 0.76 · `copula` 0.79 · `waste` 1.23 ·
`head` 0 hard, 0 clause, 4 soft. **Three more rulings came after it — see below.**

### Correction — I claimed step 3 and did a fraction of it

**Wendell, 2026-08-29:** *"did you do the /no-ai-slop or /creative-writing skills?"* **No.** I ran
`eval.md`'s fabrication check and labelled it *"Step 3 · slop, by hand"*. That check is one item of
one file inside a step that is a whole reading. **Naming a fraction after the whole is the same
move as calling `gate` plus `diet` "the pass"**, which is the failure this project already has a
standing rule about. Run properly, `/no-ai-slop` found three defects.

**1 · A reader-history assertion — fixed.** *"Nobody ever handed you the moves."*
`MANUSCRIPT_FILE_CANON:154` forbids narrating the reader's unnamed history back to her as fact, and
that sentence asserts something about her past that nothing has earned. It is the same defect class
as *"you know the loop."* **Now:** *"It teaches the moves instead, which is the training nobody
gets"* — the absence becomes a claim about the world rather than about her.

**2 · Stacked fragments — kept, and then the defence was overturned.**

**The first defence was:** *"they survive because they are the concrete images the whole
description rests on."* **Wendell, 2026-08-29:** *"then write more descriptive images throughout,
don't keep them out of scarcity."*

**He is right, and the error is in the shape of the argument rather than the verdict.** Defending
an element by pointing at the poverty of everything around it is an argument from scarcity. **The
answer to *this is the only concrete moment* is to write more concrete moments**, which removes
the need to defend anything.

**So the description was rewritten with images throughout** rather than rationed to one paragraph:

| was abstract | now |
|---|---|
| *"six roles a group runs on, and which one you reach for under strain"* | *"One person cracks the joke that lets everybody breathe. One says the rule out loud. One rebuilds the process so it cannot happen again."* |
| *"five channels a feeling travels"* | *"anger, fear, sadness, joy, and the flat calm that is none of them"* |
| *"you can run it in ten seconds or ten hours"* | *"Ninety seconds in a hallway, or a year with one person"* — and the ninety seconds is `ch3:904`'s own figure |
| *"burnout is a design flaw"* | *"the yes that costs a weekend, the favor that becomes a standing arrangement, the meeting where the same person absorbs it again"* — **the last clause superseded below; it was a handwave** |

**The fragments then stopped needing a defence.** They are now one set of images among five rather
than the only ones, which is what makes them read as texture instead of as a device.

**Two defects the rewrite introduced, both caught by the slop reading and not by any counter:**

- ***"The group chat that goes strange for four hours"*** — `go` plus an adjective on a subject
  that cannot act. **`inchoative` read 0.00** because the adjective was not in its list, which is
  the counter's known blind spot. Now *"where everybody stops typing"*, which names a doer and is
  a better image.
- **A second fragment triplet** echoing the opening one, which is the robotic-rhythm pattern.
  Folded into a single sentence behind a colon, so the shape varies.

**3 · A binary contrast — kept, and it is Wendell's own.** *"Every one of them points at the
problem. Not one of them hands you a move."* The banned shape is *this is not X, it's Y*, stated
for false drama. **This one ranks rather than denies** — it concedes the genre its real
achievement, which is exactly the constraint the book runs on — and `ANALYSIS_SALES_PAGE` §2 rated
it the sharpest line available. **Flagged so it is a decision rather than an oversight.**

**No em dashes in the body.** Zero, checked. The skill says use none in short copy.

**Fabrication check, `eval.md` item 1.** Every number is canon: six roles, five channels, the
five-move Form by its five names, thirty moves as six roles times that Form, 120 prompts, the four
domains under their canonical names, and the sub-ten-percent completion rate from Chapter 9.

**Step 3.5 · stance.** Person — address holds on *you* throughout, no first-person plural. Doer —
no get-passives. Back-pointer — no vague openers. Membrane — no fiction present.

### Ruling — fragments are out, because he does not speak in them

**Wendell, 2026-08-29:** *"fragments are bad. I speak in complete sentences."*

**That overturns the defence above and the verdict with it.** The previous section argued the
fragments could stay once there were images elsewhere. **The reason they go is not density, it is
that they are not his voice** — and a voice rule outranks a texture argument.

**So the three fragment triplets became three sentences with doers.** *"The meeting where somebody
gets talked over. The decision that lands on whoever can least afford it."* became **"You catch
the meeting where somebody gets talked over, the decision that lands on whoever can least afford
to absorb it, and the group chat where everybody stops typing."** The images all survive; they now
hang off a subject who is doing something.

**Two more went the same way.** *"Six roles a group runs on"* became *"A group runs on six roles"*,
and *"Five channels a feeling travels"* became *"A feeling travels one of five channels."* Both had
been inversions dressed as headlines. **The disqualifier changed for the same reason** — *"Not for
you if you are looking for a script"* became **"Skip it if you are looking for a script,"** which
is a complete sentence and an instruction rather than a label.

### Four handwaves he caught by eye, and every counter had passed them

**Each one is a noun phrase or a pronoun that names nothing a reader could point at.**

| his catch | the defect | now |
|---|---|---|
| *"the noise of doing the work"* | *the work* names nothing. Which work, done how, felt as what | *"the noise of seeming like you're doing a good job"* — the noise is now a specific performance |
| *"under strain everybody reaches for the same one"* | *everybody* and *under strain* are both unfalsifiable | *"most people reach for the same one every time"* — a claim about frequency, checkable against yourself |
| *"the meeting where the same person absorbs it again"* | **"what person? what is it? We're handwaving again."** Both the person and the *it* were introduced by the definite article and never named | *"the meeting that ends with the person who named the problem owning it"* — the person is identified by what they did, and *it* points at *the problem* two words back |
| *"which is the training nobody gets"* | Faux-insight flattery, the *what nobody tells you* shape, and a claim about the world nobody can check | *"so that on Monday you can do more than notice"* — concrete, dated, and it cashes *"You are the one who notices"* from the second paragraph |

**The last one is the one worth keeping.** A term coined early and paid off late is the `LIKE RAO`
test, and it arrived here as a slop fix rather than a stylistic move, which is the order that
tends to produce the good ones.

### The `waste` pass — fifteen instances of *it*, checked one at a time

**`waste` read 1.34, above the 1.30 ceiling**, and the honest fix was not to delete pronouns but to
find the ones with no arrow. Sword's rule is exact: use *it* only when you can state which noun it
refers to.

**Four had no arrow, and all four were rewritten rather than trimmed:**

- *"and it is costing you more than you have told anyone"* → **"and moving costs you more"**. The
  *it* was the act of moving, which is a verb, so the fix names it as one.
- *"One form runs through all of it, and it has five moves"* — **two pronouns in one clause, the
  first pointing at everything above it.** → **"The same form runs under the roles and the channels
  alike, in five moves."**
- *"teaches its own changes to it"* → **"each role bends it a different way,"** where *it* now sits
  four words from *the form*.
- *"He spent the years after that finding out why"* → **"the years since."**

**Result: `waste` 1.20**, inside range, with the pronoun count down by four and no sentence
shortened to get there.

**One voice block came out of that pass and is worth recording.** *"what a martial artist means by
the word"* tripped `say the noun` — the instrument's point being that *the word* is a placeholder
where a noun belongs. **Now:** *"what it means in a dojo."* Shorter, concrete, and the *it* points
at *Form* one word back.

**Final:** `voice` clean · `gate` clean · `head` 0 hard, 0 clause, 7 soft · `expletive`, `passive`
and `inchoative` all **0.00** · `be` 0.54 · `copula` 0.83 · `zombie` 0.42 · `empty` 0.30 · `waste`
**1.20**. **475 words.**

## The order for this week

1. **Take the free KDP ISBN** — reversible while the book is in Draft, and the proof prints
   *Not For Resale* either way. Buy Bowker's ten before you publish. See `DECISION_ISBN_2026-08-29.md`.
2. **Run KDP's Cover Template Generator** at 6×9, 387 pages, your paper choice.
3. **Build the wrap** on that template, using the back cover copy and jacket bio already written.
4. **Upload `MTGOA_2026-08-29_trade.pdf`** and run the Print Previewer. Let it find the margins.
5. **Paste the description and the seven keywords**, pick categories for the ICA, set the price.
6. **Order the proof.**
7. **Then** spend the free hour with Amazon's autocomplete and revise the keywords. The proof will
   still be in the post.
