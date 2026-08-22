---
type: incident
title: "ARCADE371 could not be redeemed"
aliases:
  - the code incident
tags:
  - marketing
  - mtgoa
  - kickstarter
  - incident
created: 2026-08-22
review: 2026-08-23
source:
  - marketing/KICKSTARTER_UPDATE_2026-08-11.md
  - Kickstarter update #29 comments, 2026-08-18/19
---

# ARCADE371 could not be redeemed

**Open, four days old, affecting all 371 backers.**

Update #29 went out **2026-08-18 22:59 UTC**. Its first instruction is:

> *"**Your code:** ARCADE371 — enter it at checkout and the price goes to zero."*

**There is no field to enter it in.** Gumroad hides the discount input unless the setting is
switched on, and it was not.

## What the backers said

| when | who | |
|---|---|---|
| 08-18 23:20 | **Daniel Russo** | *"I didn't see a place to enter a code before pressing the 'Pay' button. Can you help me out?"* |
| 08-19 01:59 | **Jana Hoffmann** | *"I also can't see where to enter a code to grab a digital copy"* |
| 08-19 03:03 | **Natalie Metzger** | *"Yeah, joining the crowd on not seeing a code area in the checkout."* |
| 08-19 20:13 | **Kit Stubbs** | found the cause, quoted Gumroad's own docs, and posted the workaround |

**All four notifications are still unread.** Kit Stubbs has been running the support desk in the
comments for three days:

> *"it looks like direct coupon code entry isn't enabled on Wendell's shop, but it will work via
> URL… go to wendellbritt dot gumroad dot com slash l slash MTGOAbook slash ARCADE371 … In the
> 'Name a fair price' box, enter 0, then click 'Buy this'."*

## The fix

**1 · Switch the field on.** Gumroad → **Checkout form** tab → toggle **"Only if a discount is
available"**. Kit quoted this from Gumroad's support site:

> *"To show the discount code input box on the checkout page, toggle 'Only if a discount is
> available' in the Checkout form tab, otherwise, it will only be possible to apply a discount
> code by using a URL parameter."*

**2 · Use the URL form from now on**, in every surface that mentions the code:

```
https://wendellbritt.gumroad.com/l/MTGOAbook/ARCADE371
```

**The code belongs in the link, not in an instruction.** A code the buyer has to type depends on a
setting; a code carried in the URL does not. This is the change to make permanent regardless of
the toggle.

**3 · Reply on the update.** Draft below — gate clean, no apology sentence, and it credits Kit.

> Daniel, Jana, Natalie: you were right, there was no box to put it in. Kit, thank you for doing
> my support desk for me while I was asleep.
>
> The discount field was switched off in my checkout settings. It is on now.
>
> If you would rather not go back and fight with a checkout page, this link carries the code for
> you: https://wendellbritt.gumroad.com/l/MTGOAbook/ARCADE371 — put a 0 in the *name a fair price*
> field and it will take it.
>
> If it still gives you trouble, say so here or email me and I will send you the files directly.
> You paid for this once already and that is enough.

**Do not post the middle line until the toggle is actually flipped.** Saying it is on when it is
not is the same failure a second time, to the same people.

## What this cost, and the lesson

**The one claim 371 people could check immediately was the one that failed**, in the message whose
entire argument is that the promises are being kept now. Three of the four who spoke up are
visible to every other backer reading the comments; the ones who tried, failed and said nothing
are not counted anywhere.

**`marketing/KICKSTARTER_UPDATE_2026-08-11.md` carried the test and it was not run.** Its own
*Before you send* checklist reads:

> *"`ARCADE371` live, capped at 420, **tested to $0 in an incognito window**"*

It was reported live. **Live and redeemable are different facts**, and only the second one is the
promise. The check existed, was written down, and was skipped — the same shape as the production
tags, the seven blocking items, and the stale handoff base.

## Still open after this

- **Did anyone succeed?** Gumroad's sales list for `MTGOAbook` at $0 is the count. If it is near
  zero after four days, almost nobody got through and the reply above is not enough — that is a
  fresh update, not a comment.
- **Update #30 is owed.** #29 promised *"something shorter, for people who'd rather not read 388
  pages before deciding. That's coming in the next update."* Four days, not sent.
- **A Kickstarter Trust & Safety thread** was opened 2026-08-20 (request #2254545) and answered.
  Unrelated to this as far as the subject lines show, but it is open.
