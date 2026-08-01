# APPROVED — remove certification from the book

**Ruled by Wendell 2026-08-01:** *"certification isn't real yet. Let's remove
from the book."*

Certification is promised on four shipping surfaces and appears nowhere in
`MTGOA_Backend_Offer_Stack__Dojo_and_Cohort.md`. The book cannot promise a
product that does not exist.

**Scope, measured:** `grep -rn "certif" manuscript/ appendices/ front_matter/
back_matter/` returns exactly four hits. Three are in ch9 and are **held by
DL-18** — they go to the swmp78 queue. The fourth is back matter and is applied
on this branch.

**What survives every cut:** the succession itself. Wendell wanting to hand the
method off is a real position and the clearest Teal beat in the book. What goes
is the credential, which is a product. The edits below keep the first and remove
the second.

---

## 1 · `back_matter/about_the_author.md` — APPLIED on this branch

Not a chapter, so DL-18 does not hold it. This edit also takes the bars-engine
line, which was already approved for cutting in
`drafts/APPROVED_remove_app_v1.md`.

**BEFORE**

> **Wendell Britt** builds practices for people who want to be useful to each
> other and keep finding that the work costs more than it should. He is the
> author of *Igniting Joy*, whose emotional-body practices appear in Appendix D,
> and the builder of bars-engine, the app this book routes to. He coaches the six
> Faces one-on-one and certifies others to run them.

**AFTER**

> **Wendell Britt** builds practices for people who want to be useful to each
> other and keep finding that the work costs more than it should. He is the
> author of *Igniting Joy*, whose emotional-body practices appear in Appendix D.
> He coaches the six Faces one-on-one and runs the Allyship Dojo.

Two cuts, one addition. The Dojo replaces the app as the thing he runs, which is
true and is the offer stack's actual recurring container.

## 2 · `ch9:159` — QUEUED for swmp78

**BEFORE**

> If you want the method itself — to run it for other people, not just for the
> thing you're building — that's the succession this whole book has been pointing
> at, and it's the work I most want to hand off. Reach out:
> wendell@masteringallyship.com. I am looking for people to carry this and
> eventually get certified to teach it.

**AFTER**

> If you want the method itself — to run it for other people, not just for the
> thing you're building — that's the succession this whole book has been pointing
> at, and it's the work I most want to hand off. Reach out:
> wendell@masteringallyship.com. I am looking for people to carry this.

One sentence loses its second clause. The succession survives intact.

## 3 · `ch9:192` — QUEUED for swmp78

**BEFORE**

> - **Founder** → if you have a specific thing to build and you know you need
>   support getting it out, the fastest path is working through it with me,
>   one-on-one. If you want to learn the method itself, deeply enough to run it
>   for others, reach out about certification (wendell@masteringallyship.com).
>   That is the succession this book is for.

**AFTER**

> - **Founder** → if you have a specific thing to build and you know you need
>   support getting it out, the fastest path is working through it with me,
>   one-on-one. If you want to learn the method itself, deeply enough to run it
>   for others, say so (wendell@masteringallyship.com). That is the succession
>   this book is for.

*reach out about certification* → *say so*. The route stays open and names no
product.

## 4 · `ch9:698` — QUEUED for swmp78

This paragraph is already being rewritten under the app removal, since the
three-offer list it belongs to has bars-engine as its middle entry. The
certification cut is folded in rather than run as a separate edit.

**BEFORE**

> **The coaching, and the certification behind it.** The most expensive of the
> three, in every sense of the word. If you have a Founder move and you already
> know it has to be you, working it through with me one-on-one is the fastest
> path I know. If what you want is the method itself — to run these six Faces for
> other people, not just for the thing you're building — that is the succession
> this whole book was written to make possible, and it is the work I most want to
> hand off. wendell@masteringallyship.com.

**AFTER**

> **The coaching.** The most expensive of the three, in every sense of the word.
> If you have a Founder move and you already know it has to be you, working it
> through with me one-on-one is the fastest path I know. If what you want is the
> method itself — to run these six Faces for other people, not just for the thing
> you're building — that is the succession I wrote this book to make possible,
> and it is the work I most want to hand off. wendell@masteringallyship.com.

Heading loses four words. *was written to make possible* → *I wrote this book to
make possible* removes a passive with a hidden doer, the same fix the enrollment
page needed.

---

## Verification after application

    grep -rn "certif" manuscript/ appendices/ front_matter/ back_matter/

Must return **0**. Then `gate.py` on the body and matter surfaces.

## One related naming finding, not part of this ruling

`appendices/ON_THE_SHOULDERS_OF.md:80` calls them *"the oracle cards — which live
in the companion deck and the app rather than in these pages."* Two problems on a
shipping surface: it names the app, which the v1 removal cuts, and it calls the
cards *oracle cards* where Wendell's ruling of 2026-08-01 makes the official term
**the Allyship Deck**. The manuscript itself is already consistent — every one of
its fifteen references says *the deck* and none says *oracle*. **Wendell's call**,
filed with the enrollment spec.
