# I2 — DRAFT FOR APPROVAL, v2

**Date:** 2026-08-04
**File:** `manuscript/ch2.md`, section *What the Old Allyship Got Wrong*
**Base:** `master` @ `3d441f2`
**Supersedes:** `DRAFT_I2_CH2_TRANSFER_GAP_20260804.md` (v1, the Lakoff pass)
**Status:** proposal. Nothing enters `manuscript/` until you approve this text.

**What v2 changes.** v1 has the right idea and would have failed the review pass. It was
written without one: four gate hits and two heavy counters, measured below. v2 keeps the
transfer gap intact and rebuilds the prose for Jordan. The insert is `gate clean`, every
diet counter in band, and `marginalia/review.py` clean.

**Note on the governing ruling.** `claude_SAGE_RULING_JORDAN_LAKOFF_SPLITS_2026-08-04.md`
is not in the repo, so I could not read it. §6 checks v2 against the rulings *as v1 states
them*, plus `EDITING_PLAN.md` (Jordan), `specs/SPEC_JORDAN_METAPHOR_ARC_CH1_CH3_2026-08-02.md`,
and the review skill. If the ruling says something v1 did not quote, §6 is unverified.

---

## 1 · What was wrong with v1, measured

`python3 instruments/review.py` on v1's 248 new words, then on v2's 250:

| | gate | be | copula | waste | zombie | expletive | passive | empty |
|---|---|---|---|---|---|---|---|---|
| v1 insert | **4 hits** | 1.17 | 1.25 | 1.18 | 0.98 | **3.79** | 0.00 | **2.89** |
| v2 insert | clean | 0.80 | 0.90 | 0.71 | 1.07 | 0.00 | 0.00 | 0.29 |
| ch2.md, for scale | clean | 0.63 | 0.59 | 1.02 | 0.71 | 0.44 | 0.82 | 0.97 |

**The four gate hits.** `And in the half-second something older gets there first` —
sentence-initial *And*. `most people in the room` and `in the room, while your face is
still doing` — banned since 2026-07-29. `carrying some version of that quietly` — banned
since 2026-07-31. Any one of these is a hard fail.

**The two heavy counters are the readability complaint.** Expletive at 3.79 is *It is also
the wrong half* and *It is a description of a method with a missing step*: the two sentences
carrying the acquittal both open on a pronoun with no noun behind it, so the most important
claim in the passage is the one with nothing in its subject. Empty at 2.89 is the abstraction
tax — *something you have*, *something you run*, *a thing you have*, *a thing you run*, *the
wrong half*, *some version of that*. Nine empty nouns doing the work of nine real ones.

The sentence that shows it whole is v1's:

> Those are different possessions and the difference is not one of degree.

Grammatical. Nobody is in it, nothing happens in it, and *possessions* is a word the book
has never used. Jordan skims theory; that is the sentence she skims.

## 2 · The ELI5, written first

Step 0 of the review pass, and the reason v2 exists:

> The old way has three steps: learn it, care about it, do it. All three hand you an idea.
> None of them puts the idea in your hands, where you could use it while somebody is looking
> at you and waiting. So the hard moment comes, and you know exactly what to do, and you do
> the old thing instead. Afterward you can explain what happened perfectly. Explaining is
> the part you got good at. Then you decide the problem is you. It is not. You learned half
> of a two-part skill, and nobody mentioned there was a second half.

Scored: `empty 2.86`, heavy, exactly as expected — it says *thing*, *part*, *half* because
that is what makes it land. The split-the-difference rule applies: the register version keeps
every move the ELI5 makes, and pays for its own abstractions one at a time.

## 3 · Proposed text

Everything before the insert is **unchanged, including the body paragraph in full**. v1 cut
that paragraph's last two sentences; v2 keeps them, because *It assumes the person executing
the right actions has the body to do it* is the handoff into the new material rather than a
duplicate of it.

> ### What the Old Allyship Got Wrong
>
> The old allyship's fatal flaw was mistaking information for transformation. It had a theory
> of change. It went like this:
>
> *Learn. Feel. Act.*
>
> This theory is incomplete rather than wrong. The old allyship produced real wins: doors that
> opened, conversations that happened, power that shifted in small amounts, temporarily, in
> specific places. It also produced a generation of exhausted practitioners who kept burning
> out on good intentions. Both of these things are true.
>
> You bring a body to every one of those actions. Sometimes that body runs on three hours of
> sleep. Sometimes it has been braced since the morning meeting. The old allyship does not ask
> about that. It assumes the person executing the right actions has the body to do it.
>
> **[NEW]** Look at the three steps again, and watch what each one hands you. *Learn* hands you
> a concept. *Feel* gives it weight. *Act* sends it out. All three work on what you know. None
> of them reaches the half-second where you actually move.
>
> **[NEW]** Holding a concept and running one are different skills. What you hold, you can turn
> over, weigh, and choose between. What you run fires before any of that arrives: the jaw sets,
> the voice goes even, the sentence leaves your mouth already shaped. You can hold an idea
> accurately for ten years and never once run it. The holding does not become the running on
> its own.
>
> **[NEW]** The years hand you one and not the other. You have the analysis, faster and sharper
> than most people at the table. Then the half-second comes, an older pattern moves first, and
> afterward you can name exactly what happened. Naming it is the skill that just failed.
>
> **[NEW]** The gap comes with an explanation attached, and the explanation is wrong. It says
> the problem is you: not committed enough, not brave enough, still too attached to being
> comfortable. You have carried some form of that for a while now, and it gets heavier with
> every book you finish.
>
> **[NEW]** The accurate explanation is duller. What you built is real, and it is half of a
> two-part skill. More of the first half was never going to turn into the second. The method
> has a missing step. You are not the missing step.
>
> *[P5 deleted — see §4.]*
>
> The old allyship produces moments of brilliance and long stretches of exhaustion. It produces
> people who care enormously and accomplish less than they could because they keep hitting the
> same wall. The wall that's not in the world, it's in them.
>
> [P7 through P9 unchanged.]

## 4 · Every edit, before and after

One deletion and one insertion. The deletion, whole sentences:

| | text |
|---|---|
| **before** | The old allyship tells you what to do. It doesn't tell you how to be the kind of person who can do it sustainably. Who can show up in the hardest moments without freezing. Who can hold complexity without collapsing. Who can take feedback without disappearing. Who can stay in the conversation when it gets hard. |
| **after** | *(deleted)* |

Why: this is the passage the new material replaces. *Doesn't tell you how to be the kind of
person who can do it sustainably* is the stamina framing of the same claim, and leaving both
in makes the chapter say it twice, the second time weaker.

The insertion is 250 new words and touches no existing sentence. **Nothing shipped is
rewritten** — v1 rewrote three paragraphs to make room; v2 rewrites none.

Line-level, what changed from v1 to v2 and why:

| v1 | v2 | reason |
|---|---|---|
| Those are different possessions and the difference is not one of degree. | Holding a concept and running one are different skills. | *possessions*, *difference*, *degree* — three abstractions, no person. Verbs instead. |
| A thing you have sits in the part of you that considers, weighs, and chooses. | What you hold, you can turn over, weigh, and choose between. | *a thing*, *the part of you* → the reader does the verbs. |
| in the half-second, in the room, while your face is still doing whatever your face does | the jaw sets, the voice goes even, the sentence leaves your mouth already shaped | gate: *room*. Also three named body events instead of one joke about a face. |
| You have it faster and better than most people in the room. And in the half-second something older gets there first | You have the analysis, faster and sharper than most people at the table. Then the half-second comes, an older pattern moves first | gate: *room*, sentence-initial *And*. *pattern* is the chapter's own word and pre-seeds Section 6. |
| You have probably been carrying some version of that quietly for a while | You have carried some form of that for a while now | gate: *quietly*. *version* is an empty noun. |
| Here is the accurate one. What you built is real. It is also the wrong half, and no amount of more of it was ever going to turn into the other half. | The accurate explanation is duller. What you built is real, and it is half of a two-part skill. More of the first half was never going to turn into the second. | two expletive openers removed. *the wrong half* / *the other half* named once as *a two-part skill*, so the reader knows what the halves are. |
| That is not a verdict on you. It is a description of a method with a missing step. | The method has a missing step. You are not the missing step. | the acquittal was carried by two pronoun subjects. Now the noun is in the subject both times, and the two sentences turn on the same word. |

Also run: `/no-ai-slop`, which took out one throat-clearing opener (*Try the accurate one
instead* → *The accurate explanation is duller*) and one *Which is* fragment tail flagged by
`marginalia/review.py`. Diet re-run after both, per the skill.

## 5 · Accounting

| Change | Words |
|---|---|
| New: the transfer gap (5 paragraphs) | **+250** |
| Cut P5 entirely | −56 |
| **Net** | **+194** |

Section goes 379 → 578 words. v1 was +159 but bought it by cutting into three shipped
paragraphs; v2 buys nothing and cuts only the paragraph it supersedes.

**Optional further cut, not taken:** P7 (76 words, the broken-map paragraph) now makes the
wrong-direction claim a second time and in weaker terms. Cutting it brings the net to
**+118**. I did not take it, for v1's reason and it is a good one: P7 is the on-ramp to the
sadness paragraph, and that is Water material under the Shaman's protection. Your call.

**Section-level diet, before and after the insert:** `passive` reads 2.55 on the section as
shipped and 1.67 with the insert in place. Both are over 1.30 and neither is mine — the
passives are in P8 (*The terms were set wrong from the beginning*), which is deliberate and
which the insert dilutes. Flagging it so it is not read as new drift.

## 6 · Why each ruling is satisfied

**Shaman — body paragraph intact, in position, now whole.** All five sentences survive
verbatim, including the two v1 cut. Its first appearance in the book is untouched and it
still arrives before the argument that depends on it.

**Jordan — method acquittal, not map acquittal.** *What you built is real, and it is half of
a two-part skill. … The method has a missing step. You are not the missing step.* Blames
neither her nor the map. The map acquittal stays in P8's grief, doing grief work.

**Jordan — the two stories, refused by name.** *Not committed enough, not brave enough, still
too attached to being comfortable* names the doing-well story and the performing story in one
breath, offers neither, argues with neither, and the accurate account arrives in the next
paragraph.

**Sage/Diplomat — no Orange premise.** No appeal to effectiveness, results, or strategic
self-interest. The argument runs on Jordan's own half-second.

**Register spec — no collision.** *Hold* and *run* are plain verbs. *Run* is already the
chapter's verb for a pattern that plays on its own (`ch2.md:102`, *What pattern do I run when
pressure rises?*), so the insert borrows the chapter's vocabulary rather than importing new
vocabulary. No term is introduced or defined, and the word *register* does not appear.

**Metaphor arc spec — Ch2 gives Jordan forest, joystick, pattern, protector.** *An older
pattern moves first* is that vocabulary, arriving in Section 1 where the chapter names it in
Section 2 and puts a joystick in it in Section 6. Nothing here promises a prerequisite ladder.

**Half-second is book vocabulary, not a new coinage.** `ch7.md:553` and `ch8.md:586` both run
BARs on *the half-second before you spoke*. Ch2 seeding it makes those two prompts land on a
phrase the reader already owns.

## 7 · Two seam defects in v1, fixed

Both would have shipped as broken reference.

1. **Orphaned pronoun.** v1 cut P6's first sentence and left the next one opening *It produces
people who care enormously…*, with the last-named subject four paragraphs upstream. v2 keeps
P6 whole, so *It* keeps its noun.
2. **Stranded demonstrative.** v1 put five new paragraphs between *Both of these things are
true* and *You bring a body to every one of those actions* — *those actions* then points across
250 words of new material. v2 leaves the body paragraph where it is and inserts after it.

## 8 · Gate 1: Appendix G — clear, re-verified

v1 filed a canon conflict and then withdrew it. Checked again on `3d441f2`, and the
withdrawal is correct:

- **Appendix G is *On the Shoulders Of*.** Four reader-facing citations: `front_matter/copyright.md`
  ×2, `ch6.md:238` (Meadows), `ch8.md:295` (Genpo Roshi, Wilber, Laloux). All mean the lineage
  appendix.
- **The belief-to-superpower map is not an appendix.** `SPEC_6_SABOTAGING_BELIEFS.md` and
  `SOURCES/SELF_SABOTAGING_BELIEFS.md` — production instruments.
- **Appendix C is not doubled.** `APPENDIX_C_KEY_TERMS.md` records its own retirement under
  your ruling of 2026-07-30; C is *The Five Channels in Practice*, which is what `ch3.md:451`
  cites.

A–G clean and singly assigned. **I6 lands in G with no renumbering.**

## 9 · Next

Say yes to this text, or mark it, and I'll take I1 — the one with the guard on it, and the
harder draft — then Ch4.

**One open question for you:** the P7 cut in §5. Taking it makes the net +118 and removes a
claim the new material now makes better; leaving it protects the on-ramp to the sadness
paragraph. I would leave it, and I would rather you rule than have me guess.
