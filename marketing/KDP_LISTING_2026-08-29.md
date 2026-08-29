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

**289 words, 1,550 characters.** Well under the 4,000 ceiling, because a description is read
standing up.

You started this work for a reason. It's just gotten hard to hear that reason over all the noise
of doing the work.

You are the one who notices. The meeting where somebody gets talked over. The decision that lands
on whoever can least afford it. You move, because you can see it and you cannot leave it alone,
and it is costing you more than you have told anyone.

You have read the books that explain what is wrong. Every one of them points at the problem. Not
one of them hands you a move.

This is a field guide. It tells you what you are looking at.

Six roles a group runs on, and which one you reach for under strain.

Five channels a feeling travels, and how to read which one is live before it drives.

Thirty moves, five per role, each with a test for whether it worked.

A five-move form you can run in ten seconds or ten hours.

A hundred and twenty prompts, crossing those moves against the four domains where allyship leaves
your head: gathering resources, raising awareness, direct action, and skillful organizing.

Burnout here is a design flaw that looks exactly like a character flaw. You can change a design.

Wendell Britt built a course on this material in 2020. Under ten percent of the people who started
it finished. He spent the years after that finding out why, and rebuilt the method around the
answer. This book is what came out.

For the person still showing up and running out of road. It will not tell you to care more. You
already do, and that was never what was missing.

Not for you if you are looking for a script.

## The same thing with KDP's HTML

**KDP accepts a small tag set and strips everything else.** Bold and lists survive, so the five
specifics become scannable, which is the whole reason to use markup at all — **a browser reads
bolded fragments, not sentences.**

```html
<p><b>You started this work for a reason. It's just gotten hard to hear that reason over all the noise of doing the work.</b></p>
<p>You are the one who notices. The meeting where somebody gets talked over. The decision that lands on whoever can least afford it. You move, because you can see it and you cannot leave it alone, and it is costing you more than you have told anyone.</p>
<p>You have read the books that explain what is wrong. Every one of them points at the problem. Not one of them hands you a move.</p>
<p><b>This is a field guide. It tells you what you are looking at.</b></p>
<ul>
<li><b>Six roles</b> a group runs on, and which one you reach for under strain.</li>
<li><b>Five channels</b> a feeling travels, and how to read which one is live before it drives.</li>
<li><b>Thirty moves</b>, five per role, each with a test for whether it worked.</li>
<li><b>A five-move form</b> you can run in ten seconds or ten hours.</li>
<li><b>A hundred and twenty prompts</b>, crossing those moves against the four domains where allyship leaves your head: gathering resources, raising awareness, direct action, and skillful organizing.</li>
</ul>
<p>Burnout here is a design flaw that looks exactly like a character flaw. You can change a design.</p>
<p>Wendell Britt built a course on this material in 2020. <b>Under ten percent of the people who started it finished.</b> He spent the years after that finding out why, and rebuilt the method around the answer. This book is what came out.</p>
<p>For the person still showing up and running out of road. It will not tell you to care more. You already do, and that was never what was missing.</p>
<p><i>Not for you if you are looking for a script.</i></p>
```

**About 2,100 characters with the tags.** Still half the ceiling.

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

**The `goes external` one is worth noting.** That phrase is the book's own, at `ch3:876`. **New
marketing prose does not get to inherit a defect because the manuscript carries it** — and naming
the domains was better copy anyway.

**Final:** `voice` clean · `gate` clean · `expletive` **0.00** · `passive` **0.00** · `empty`
**0.00** · `inchoative` **0.00** · `be` 0.76 · `copula` 0.79 · `waste` 1.23, inside range ·
`head` 0 hard, 0 clause, 4 soft.

**Step 3 · slop, against `eval.md` check 1.** Every number is canon: six roles, five channels,
thirty moves, the five-move form, 120 prompts, the four domains by their canonical names, and the
sub-ten-percent completion rate from Chapter 9. **No invented claims.**

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
