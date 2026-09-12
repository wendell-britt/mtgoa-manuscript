# Every piece of launch collateral, and what it is actually for

**Wendell, 2026-08-13:** *"pull all versions of the kickstarter launch announcement.
Specifically any sales collateral that we've made. I want to launch to the kickstarter backers
and I know we've created content for this already."*

**It exists, all of it is from one week in June, and none of it is a delivery announcement.**
That is the finding this document is written around, because it changes what gets reused and
what gets thrown away.

---

## 0 · Correction, 2026-08-18 — the delivery announcement exists

**Wendell: *"there should be one that was in august."* He was right and this document was
wrong.**

**`KICKSTARTER_FINAL.md`, Google Drive, created 2026-08-11T23:00Z.** It is a complete delivery
announcement, it is titled *It's done. Here's your copy.*, and it has been finished for a week.
Two more from the same night: **`OUTREACH_PACK.md`** (23:08Z) and **`OPSBACKLOG.md`** (23:45Z).
The first two are now in this directory as `KICKSTARTER_UPDATE_2026-08-11.md` and
`OUTREACH_PACK_2026-08-11.md`.

**How this document got it wrong: I searched the repository and called the result the world.**
§5 below says *"There is no delivery announcement in this repo"* — which was true, and which I
then reported as *no delivery announcement exists*. **The repo is not the archive.** Three
launch documents were written outside it and nothing in it points at them.

**That is the same failure shape this project has already paid for twice** — the merge that
resolved to 23 production tags, and the seven blocking items reported closed that were still
live. Recorded there as *"a summary is not an audit."* The version of it here: **an inventory
of one location is not an inventory.**

**Both of §6's blockers were already ruled, on 2026-08-11:**

| §6 asked | the answer, in the August copy |
|---|---|
| the true backer number | **371.** *"The code works 420 times. There are 371 of you."* |
| the fulfilment mechanic | **Free.** Code `ARCADE371`, 100% off, capped at 420 |

**So the number in the Gumroad draft was the right one and the June collateral's "over 400" is
the stale figure** — §3 below has it backwards, and stays as written so the correction is legible.

### What is actually wrong with the August copy

**One defect, measured against today's build.** The update says **383 pages** in two places.
That figure came from `HANDOFF_ANNOUNCE_2026-08-10` §1, which was verified at commit `cc9185a`
— before ch7's exile and the ch1 gloss landed. Re-derived from the shipping build on
2026-08-18:

```
trade interior      387 pp        workbook interior    395 pp
trade PDF ebook     388 pp        workbook-9 interior  405 pp   ← the file a backer downloads
```

**The number to quote is 388.** It is the one claim in the update that 371 people can check by
opening the file, and it is wrong by five pages in the direction that undersells it.

**One thing to decide rather than fix — since ruled.** The last thing backers heard was
**update #28, 2026-08-01: *"🎶ITS THE FINAL COUNTDOWN🎶 (book launching in the next 48
hours)."*** The draft's *"You waited a long time"* is about the three years and did not touch
the two and a half weeks since a forty-eight-hour promise. **Wendell, 2026-08-18: *"add
something about how the final stretch took longer than I thought."*** A paragraph now sits
directly under that line, naming the forty-eight hours and what the extra two weeks bought.

**And `OPSBACKLOG.md` says the send is blocked on plumbing, not copy** — A3 reads *"Copy final,"*
blocked by **A1** (Kit list landing page) and **A2** (`ARCADE371` created, capped, tested to $0
with email captured). Nothing below is the thing standing between the backers and the book.

---

## 1 · The complete inventory — ten files, one session, 2026-06-18

Everything below came onto `master` on 2026-08-13 in PR #17, rescued from
`codex/book-eod-draft-2026-06-09`, a branch with unrelated history that nothing else pointed
at. **It had never been on master before.**

| file | what it is | reusable now? |
|---|---|---|
| `MTGOA_Copy_Strategy_Spec` | 39K. Seven story beats, six level-by-level strategies, voice directives, hard banned phrases | **Yes — the voice half** |
| `FUNDRAISER_COPY_SPEC` | 25K. Near-duplicate of the above with a Beat 4.5 the other lacks | Yes, same |
| `IDEAL_READER_MATRIX` | 17K. Six reader rows: Desire, Fear, Wall, **Crack**, Epiphany, what loses them | **Yes — the most valuable file here** |
| `MARKETING_STRATEGY_SPEC` | 15K. Channel plan, **§5a is a Kickstarter Backer Email brief**, a dated timeline | Partly — the brief yes, the timeline no |
| `MTGOA_Drafts_5Parallel` | 15K. **Five complete drafts, one per Face.** Draft 3 is the Regent/Amber one | **Draft 3 is the closest thing to what you want** |
| `MTGOA_Draft_Teal` | 13K. An eight-section integration draft | Structurally, yes |
| `MTGOA_Launch_Spec` | 12K. Tier table, **the Kickstarter self-report mechanic** | **The mechanic yes, the tiers need re-ruling** |
| `KOFI_OPENING_DRAFT` | 6K. The page's opening beats | Partly |
| `PARTIFUL_EVENT_PAGES` | 4K. Two event pages, July 18 and Portland | **No — the dates have passed** |
| `SOCIAL_POST_LAUNCH` | 1K. Day-one social post | No, same reason |
| `leads/MTGOA_LEADS` | 5K. Three circles of outreach; **Circle 3 is the Kickstarter backers** | Yes — it is a plan, not a list of names |

## 2 · What all of it was for, and why that matters

**Every one of these was written for a fundraiser to replace a car.**

> `MTGOA_Drafts_5Parallel:150` — *"the final obstacle between this work and the people who are
> waiting for it is that my car engine blew up… **The goal is $8,500.**"*

The structure underneath all ten files is: **the book is nearly done → here is the obstacle →
back me so I can finish and travel → July 18 launch → August 1 ship.** It is an appeal with an
accountability confession at its centre, and it is well built for that.

**None of that is true any more.** The book is finished, built, and downloadable. August 1 has
passed. July 18 has passed. **The emotional structure inverts completely:** what was *I owe you
this and here is why it is late* becomes *here it is*, and the ask stops being the point of the
message.

**So the June collateral cannot be edited into a delivery announcement.** The beats are in the
wrong order for the new situation. What survives is the raw material, not the arrangement.

## 3 · The number is wrong on the page you drafted

**Every one of the ten files says over 400. Your Gumroad draft says 371.**

> `MTGOA_Drafts_5Parallel:144` — *"In 2021, **400 people** backed Mastering the Game of Allyship
> on Kickstarter."*
> `KOFI_OPENING_DRAFT:22` · `MTGOA_Draft_Teal:127` · `SOCIAL_POST_LAUNCH:21` ·
> `MARKETING_STRATEGY_SPEC:85` · `IDEAL_READER_MATRIX:70` — all **"over 400"** / **"400+"**

**Neither number is verifiable in this repo.** `back_matter/kickstarter_backers.md` has never
existed on any branch — `FINAL_SHIPPING_DRAFTS:193` records it as *"absent from every checked
branch"*, and `build_book.py` still reports it as one of two OPTIONAL gaps. **DL-16 in the
decision log opened on exactly this: backers promised a credit who do not find one.**

**This has to come off the Kickstarter dashboard before anything ships.** It is the single
most-repeated claim in the collateral and the audience for it is the one group who can check.

## 4 · The three things worth taking, in order of value

### a · The self-report mechanic — take it exactly as written

> `MTGOA_Drafts_5Parallel:173` — *"**A note to Kickstarter backers:** If you already backed
> this on Kickstarter, you can self-report at the $15 tier and receive the digital Allyship
> Deck at no additional charge. **I trust you. That's how this works.**"*

**That last line is the best sentence in the entire collateral**, and it is doing something no
discount code can. It hands the backer the honour system as a gift, it costs nothing to run,
and it is the book's own thesis applied to commerce — the reader is the one with agency.

**For a delivery announcement it needs one change.** In June it was a reward for paying again.
Now the book is finished and these people already paid, three years ago. **The natural version
is that backers get the book free and the honour system covers the deck.**

### b · The Regent draft is the closest thing to what you want

`IDEAL_READER_MATRIX:74` is explicit: **Kickstarter backers ARE the Amber audience.** Draft 3
is the only one of the five written to them, and it earns its register — *"I believe in
honoring commitments"*, *"This is not a promise. This is a report on work completed"*, *"The
accountability is this page."*

**What survives:** the accountability posture, the four-artifacts proof list, the plain
inventory of what exists. **What has to go:** the engine photo, the $8,500, the tiers, both
event dates, and every future-tense verb about the book.

### c · The voice directives are still binding

`MTGOA_Copy_Strategy_Spec` §5 bans, by name: *"failing forward"*, *"silver lining"*, *"hard
times"*, *"grateful for the support"*, *"I need your help"*, *"this is about more than me"*,
*"wouldn't be possible without you"*, and **any sentence that sounds like an apology**.

**That last one is the one to watch in a delivery message to people who waited three years.**
The pull toward apology will be strong and the spec already ruled it out. The register it wants
instead: *"someone who figured something out and is choosing to tell you about it."*

## 5 · What does not exist and has to be written

**There is no delivery announcement in this repo.** No version of *the thing you backed is
finished, here is how to get it*. Every draft here was written while the book was still a
promise.

**Four things it needs that none of the June collateral has:**

1. **The artifact, described.** 387-page trade interior, 395-page workbook at a wider trim, a
   reflowing EPUB, nine chapters, eight appendices, a glossary and an index. The June files
   could only say *"in final editorial passes."*
2. **How a backer actually gets it.** In June the answer was a Ko-fi tier. Now it is a Gumroad
   link, and **the fulfilment question for people who already paid is unanswered anywhere in
   this repo.**
3. **The three years, named once and then dropped.** They waited. The spec bans the apology but
   the silence would be worse. One sentence, no flinching, then on to the book.
4. **What is still owed.** The deck, the RPG, the app, the print edition — `HANDOFF_ANNOUNCE`
   §1 records that print still says *ships after the print run*. **A delivery message that goes
   quiet on the rest of the promise re-opens the same wound it is closing.**

## 6 · What I would do next

**Superseded by §0 — items 1–3 were already answered on 2026-08-11.** Kept as written.

1. ~~**Get the backer number off the Kickstarter dashboard.** Everything else waits on it.~~
   **371.**
2. ~~**Decide the fulfilment mechanic** — free to backers, honour system, or a code.~~
   **A code, `ARCADE371`, 100% off, capped at 420.**
3. ~~**Then write the announcement.**~~ **Written 2026-08-11, not yet posted.**
4. **Only then the Gumroad page** — the backer email and the public page answer different
   questions, and `MARKETING_STRATEGY_SPEC:5a` is right that backers should hear from you
   **before** they see it anywhere else. **This one still stands**, and the August copy makes it
   load-bearing: the update's only link is the Gumroad page, so a backer redeeming `ARCADE371`
   reads that page on the way to the file they already paid for.

**The live order, as of 2026-08-18:**

1. ~~**Fix `383` → `388`** in the update, both places.~~ **Done**, with the final-stretch
   paragraph added and the 420-code line cut, on Wendell's instruction.
2. **Unblock the send** — `OPSBACKLOG` A1 and A2. Copy is not the constraint.
3. **Then the Gumroad page**, per `ANALYSIS_SALES_PAGE_2026-08-13.md` §5.

**Not to reuse:** the tier table, both event pages, the social post, the $8,500, and the
timeline. Those belong to a campaign that is over.
