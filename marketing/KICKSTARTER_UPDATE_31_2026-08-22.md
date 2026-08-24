---
type: copy
title: "Kickstarter update #31 — the short version"
aliases:
  - update 31
  - the speaking update
tags:
  - marketing
  - mtgoa
  - kickstarter
  - speaking
created: 2026-08-22
review: 2026-08-25
source:
  - marketing/OUTREACH_PACK_2026-08-11.md
  - marketing/KICKSTARTER_UPDATE_2026-08-11.md
  - bars-engine src/app/speaking/page.tsx
---

# Kickstarter update #31 — the short version

**The debt this pays.** #29 promised: *"I'm also putting together something shorter, for people
who'd rather not read 388 pages before deciding. That's coming in the next update."*

**Everything it needs is already live and verified**, `bars-engine` at `db4ee33`:

| | |
|---|---|
| `/speaking` | built, fees on the page rather than behind an enquiry |
| `public/speaking/Wendell_Britt_Speaker_One_Sheet.pdf` | **present**, 322 KB |
| `public/speaking/Wendell_Britt_Field_Staff_Training.pdf` | **present**, 384 KB |
| the fees | talk **$2,500** · half-day **$4,500** · outdoor **$95/seat sliding to $75** |

**Both PDFs were confirmed on disk before this copy quoted them.** That check is here because the
last update promised a code that had no box to go in.

## Timing — hold this until after the 48-hour check

**#30 went out today and its job is to get 364 people a book they already paid for. #31 asks them
for a favour.** Landing an ask on the heels of *"there was no box"* spends goodwill that is
currently being repaired, and it steps on the one measurement that tells us whether the checkout
was ever the problem.

**Send it after the redemption number is read.** If redemptions moved, #31 goes to an audience
holding the book. If they did not, #31 is not the next move at all — the delivery problem is, and
another update is not how it gets solved.

---

**Title:** The short version, for the person you'd send me to.

---

Last update I said I was putting together something shorter, for people who would rather not read
388 pages before deciding. Here it is.

**masteringallyship.com/speaking**

Two one-sheets on that page. One covers conferences and companies, the other covers outdoor
programs and field staff. Download whichever fits the person you have in mind and send it on.

The fees sit on the page too. A page that hides its number costs somebody a whole conversation
before they find out they cannot afford it.

A talk, **$2,500**. A half-day, where people leave having run a move rather than having agreed
with one, **$4,500**. Outdoor and experiential work, **$95 a seat and sliding to $75**, so a small
program pays a small number.

**Now the part that saves you the writing.**

Warm introductions rarely fail on willingness. They fail because nobody knows what to say. So here
is a paragraph you can paste into an email and change however you like.

> I backed a book called *Mastering the Game of Allyship*. It came out this year, and it is the
> first one I have read on the subject that is about what to do rather than what to believe. The
> author, Wendell Britt, speaks and runs workshops on it. The short version of his pitch is that
> most training on this does not stick, and he can prove it, because his own course had under a
> ten percent completion rate before he rebuilt the method around that failure. He is at
> wendell@masteringallyship.com.

Cut whatever does not fit. If you have not read the book yet, say so plainly. *"I backed this one
and I hear it is good"* still works, and it beats a recommendation you have to manufacture.

If writing to them is more than you want to take on, reply with a name and I will handle it from
there.

Three or four bookings covers the print run and every copy still owed.

— Wendell

---

## Why it is built this way

**It leads with the tool, not the request.** `OUTREACH_PACK` §5 is explicit that update #1 asks
for names and update #2 arms the people who send them. An update that repeats the ask has no
reason to exist; one that hands over a finished instrument does.

**The blurb is written as the backer, not as Wendell — and it is deliberately left un-dieted.**
`prose_diet` was run on the body only. Polishing the blurb to the book's ratios would make it
sound like the person being recommended wrote it, **which is the one thing it cannot sound like**
or nobody forwards it. `OUTREACH_PACK` §5: *"A recommendation that sounds like it was written by
the person being recommended does not get forwarded."*

**The permission to admit they have not read it is the line I would fight for.** Seven of 371 had
the book when this was drafted. Most backers being asked to recommend it have not opened it, and
a blurb that assumes otherwise asks them to lie in writing to a colleague. *"I backed this one and
I hear it is good"* is a real sentence a real person sends, and it costs the pitch almost nothing.

**The fee is stated rather than hinted.** It saves the backer the worst part of an introduction —
not knowing whether their friend is about to be asked for money.

**No new accountability beat.** #29 spent that budget and #30 spent what was left. The print run
gets one closing line, connecting the ask to the debt, and then it stops.

**Measured.** Body: `gate` all 0 · `prose_diet` every counter under 1.00, **expletive 0.00,
passive 0.00**, waste 0.85 against a ~0.5 floor. 231 words. The first draft ran 337 words with
four counters heavy — expletive 1.98, copula 1.80 — from a stack of *it is* and *X is $Y*
constructions that rewrote out cleanly.

## Before posting

- [ ] The 48-hour redemption number read, and #30 judged
- [ ] `masteringallyship.com/speaking` loads, and **both one-sheet PDFs download** from it
- [ ] The one-sheets have had Wendell's voice pass — `OPSBACKLOG` A6 had this open, and the page
      shipped since, so confirm rather than assume
- [ ] Fees on the page still match the three numbers quoted here
