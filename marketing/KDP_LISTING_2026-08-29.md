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

**439 words, about 2,400 characters.** Well under the 4,000 ceiling, because a description is read
standing up.

You started this work for a reason. It's just gotten hard to hear that reason over all the noise of doing the work.

You are the one who notices. The meeting where somebody gets talked over. The decision that lands on whoever can least afford it. The group chat where everybody stops typing for four hours and then carries on. You move, because you can see it and you cannot leave it alone, and it is costing you more than you have told anyone.

You have read the books that explain what is wrong. Every one of them points at the problem. Not one of them hands you a move.

This is a field guide. It tells you what you are looking at.

Six roles a group runs on. One person cracks the joke that lets everybody breathe. One says the rule out loud. One rebuilds the process so it cannot happen again. Those are three of the six, and under strain everybody reaches for the same one every time.

Five channels a feeling travels: anger, fear, sadness, joy, and the flat calm that is none of them. Each is reporting something different about what the situation needs next, and the book teaches you to read which one is running before it starts driving.

One form, five moves: Wake Up, Open Up, Clean Up, Grow Up, Show Up. Form in the martial artist's sense, a fixed order you run until your body has it. Ninety seconds in a hallway, or a year with one person.

Thirty moves in all. Each of the six roles teaches that same form and then teaches its own changes to it, which is why the sixth role is not six times the work.

A hundred and twenty prompts, crossing those moves against the four domains where allyship leaves your head: gathering resources, raising awareness, direct action, and skillful organizing.

Burnout here is a design flaw that looks exactly like a character flaw: the yes that costs a weekend, the favor that becomes a standing arrangement, the meeting where the same person absorbs it again. You can change a design.

Wendell Britt built a course on this material in 2020. Under ten percent of the people who started it finished. He spent the years after that finding out why, and rebuilt the method around the answer. This book is what came out.

For the person still showing up and running out of road. It will not tell you to care more. You already do. It teaches the moves instead, which is the training nobody gets.

Not for you if you are looking for a script.

## The same thing with KDP's HTML

**KDP accepts a small tag set and strips everything else.** Bold and lists survive, so the five
specifics become scannable, which is the whole reason to use markup at all — **a browser reads
bolded fragments, not sentences.**

```html
<p><b>You started this work for a reason. It's just gotten hard to hear that reason over all the noise of doing the work.</b></p>
<p>You are the one who notices. The meeting where somebody gets talked over. The decision that lands on whoever can least afford it. The group chat where everybody stops typing for four hours and then carries on. You move, because you can see it and you cannot leave it alone, and it is costing you more than you have told anyone.</p>
<p>You have read the books that explain what is wrong. Every one of them points at the problem. Not one of them hands you a move.</p>
<p><b>This is a field guide. It tells you what you are looking at.</b></p>
<ul>
<li><b>Six roles a group runs on.</b> One person cracks the joke that lets everybody breathe. One says the rule out loud. One rebuilds the process so it cannot happen again. Those are three of the six, and under strain everybody reaches for the same one every time.</li>
<li><b>Five channels a feeling travels: anger, fear, sadness, joy, and the flat calm that is none of them.</b> Each is reporting something different about what the situation needs next, and the book teaches you to read which one is running before it starts driving.</li>
<li><b>One form, five moves: Wake Up, Open Up, Clean Up, Grow Up, Show Up.</b> Form in the martial artist's sense, a fixed order you run until your body has it. Ninety seconds in a hallway, or a year with one person.</li>
<li><b>Thirty moves in all.</b> Each of the six roles teaches that same form and then teaches its own changes to it, which is why the sixth role is not six times the work.</li>
<li><b>A hundred and twenty prompts, crossing those moves against the four domains where allyship leaves your head: gathering resources, raising awareness, direct action, and skillful organizing.</b></li>
</ul>
<p>Burnout here is a design flaw that looks exactly like a character flaw: the yes that costs a weekend, the favor that becomes a standing arrangement, the meeting where the same person absorbs it again. You can change a design.</p>
<p>Wendell Britt built a course on this material in 2020. <b>Under ten percent of the people who started it finished.</b> He spent the years after that finding out why, and rebuilt the method around the answer. This book is what came out.</p>
<p>For the person still showing up and running out of road. It will not tell you to care more. You already do. It teaches the moves instead, which is the training nobody gets.</p>
<p><i>Not for you if you are looking for a script.</i></p>
```

**About 2,900 characters with the tags.** Still half the ceiling.

## Keywords — provisional, and that is fine

**These are ideation, not measurement**, per `ANALYSIS_KDP_DESCRIPTION` §5a — a language model has
no Amazon search-volume data. **Put them in to publish, then spend the free hour with Amazon's
autocomplete and replace whatever does not complete.** Spaces, not commas. Nothing already in the
title.

```
1  compassion fatigue helper burnout
2  boundaries for people who care too much
3  emotional labor exhaustion recovery
4  activist burnout sustainable practice
5  how to help without burning out
6  shadow work self awareness practice
7  workplace inclusion practical guide
```

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

**4 · ISBN.** KDP's free ISBN works and costs nothing, and it names Amazon as publisher and cannot
be used elsewhere. **A bought ISBN is the one to use if the book is ever going into bookstores or
to another printer.** Given a print run is already planned for the 247 backers, **buy the ISBN** —
the free one will not carry across.

**5 · The back cover copy and jacket bio are done.**
`marketing/BACK_COVER_2026-08-27.md` and `marketing/AUTHOR_BIO_2026-08-27.md`, both through the
full pass. They go in the wrap, not in KDP's fields.

## The review pass

**Step 0 · ELI5 first.** *You keep helping people and it keeps wearing you out. This book says the
problem is not that you care wrong, it is that nobody taught you the moves. It names six ways of
helping, shows which one you reach for under pressure, and gives you thirty things to actually do.*
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

**Final:** `voice` clean · `gate` clean · `expletive` **0.00** · `passive` **0.00** · `empty`
**0.00** · `inchoative` **0.00** · `be` 0.76 · `copula` 0.79 · `waste` 1.23, inside range ·
`head` 0 hard, 0 clause, 4 soft.

### Correction — I claimed step 3 and did a fraction of it

**Wendell, 2026-08-29:** *"did you do the /no-ai-slop or /creative-writing skills?"* **No.** I ran
`eval.md`'s fabrication check and labelled it *"Step 3 · slop, by hand"*. That check is one item of
one file inside a step that is a whole reading. **Naming a fraction after the whole is the same
move as calling `gate` plus `diet` "the pass"**, which is the failure this project already has a
standing rule about. Run properly, `/no-ai-slop` found three things.

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
| *"burnout is a design flaw"* | *"the yes that costs a weekend, the favor that becomes a standing arrangement, the meeting where the same person absorbs it again"* |

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

## The order for this week

1. **Buy the ISBN**, since a print run is coming and the free one will not travel.
2. **Run KDP's Cover Template Generator** at 6×9, 387 pages, your paper choice.
3. **Build the wrap** on that template, using the back cover copy and jacket bio already written.
4. **Upload `MTGOA_2026-08-29_trade.pdf`** and run the Print Previewer. Let it find the margins.
5. **Paste the description and the seven keywords**, pick categories for the ICA, set the price.
6. **Order the proof.**
7. **Then** spend the free hour with Amazon's autocomplete and revise the keywords. The proof will
   still be in the post.
