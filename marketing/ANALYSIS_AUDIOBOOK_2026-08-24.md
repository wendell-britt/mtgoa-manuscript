---
type: analysis
title: "The audiobook — two paths, priced"
aliases:
  - audiobook pricing
  - the audiobook
tags:
  - marketing
  - mtgoa
  - fulfilment
  - audiobook
created: 2026-08-24
review: 2026-08-31
source:
  - marketing/ANALYSIS_BACKER_OBLIGATIONS_2026-08-24.md
---

# The audiobook — two paths, priced

**Wendell, 2026-08-24:** *"I'm thinking of either doing my own audiobook or having an AI do the
audiobook for me using my voice. We'd need to price out that later option."*

**Sixteen backers paid for an audiobook in 2021.** Nothing in this repository has ever referred
to one.

## The size of the thing

Measured off the shipping manuscript, comments and tables stripped:

| | words | characters | runtime at 150 wpm |
|---|---|---|---|
| Nine chapters | 114,449 | 641,788 | **12.7 h** |
| Eight appendices | 12,793 | 75,384 | 1.4 h |
| **Both** | **127,242** | **717,172** | **14.1 h** |

**The appendices are the first decision and it is nearly free.** Appendix F is a polarity map,
Appendix H is a character sheet, and `ON_THE_SHOULDERS_OF` is a bibliography. **Three of the eight
are unreadable aloud in any useful sense.** Narrating the chapters alone saves 1.4 hours and about
75,000 characters, and loses nothing a listener wanted.

## Path A — the AI voice clone

**Roughly $100–$250 in vendor cost, and two to eight weeks of your attention.**

ElevenLabs is the realistic vendor. Professional Voice Cloning starts on the **Creator** plan at
**$22/month** (100,000 characters), with **Pro at $99/month** (500,000). Metered another way, the
effective rate runs about **$0.20 per generated minute**, with overage nearer **$0.30**.

| approach | vendor cost | calendar |
|---|---|---|
| Pro, two months, chapters only | **~$198** | 2 months of quota |
| Creator, spread across quota | **~$176** | 8 months — too slow |
| Per-minute framing, 762 min | **$152–$228** | — |

**Call it $200 in credits for the chapters.** That is not the real cost.

**The real cost is proofing.** A 12.7-hour synthetic read has to be listened to, because
misreadings do not announce themselves — a wrong stress on *Regent*, a mispronounced *Maera Voss*,
a treatise read in the narrator's default register. **Budget listening time at roughly 1.5× the
runtime**, so about **19 hours**, plus regeneration and stitching. **That is the line item, and it
is the same line item whichever path you take.**

**The book also has a structural problem for synthetic voice.** It carries marginalia in
`> ` blocks, six treatise voices with distinct registers, admissions pages, and a Headmaster's
letter. **These are characters, not the author** — that rule is enforced through the whole
manuscript. A single cloned voice reading everything flattens the apparatus the book spends nine
chapters building. Options: a second cloned voice for margin hands, a tonal shift per treatise, or
an explicit spoken label. **Undecided, and it should be decided before generation rather than
after.**

## Path B — record it yourself

**Roughly 45–65 hours of your time, and near-zero vendor cost if you already have a decent mic.**

Rule of thumb for a self-narrating author is **3–4 hours of work per finished hour** — reading,
retakes, editing, mastering. At 12.7 finished hours that is **38–51 hours**, plus setup.

**What it buys that Path A cannot.** Chapter 9 is a first-person account of burning out at the
bottom of a depression well. **A cloned voice reading that passage is a synthetic performance of
somebody's worst year**, and the one thing the book's own argument cannot survive is a mechanical
delivery of its most personal claim. The failure story is the most persuasive asset in every piece
of collateral you have; it is worth hearing in the voice it happened to.

## The distribution fork, which is where the real cost hides

**This is the decision that changes the price by an order of magnitude, and it is not a technical
one.**

**For sixteen people, you do not need a retailer.** You need 12.7 hours of audio files and a
delivery link. Path A at ~$200 discharges the obligation completely.

**For a retail product on Audible, AI narration is the harder road.** As of April 2026 ACX
requires human narration unless separately authorized; unauthorized text-to-speech and AI
recordings are prohibited on direct submission. AI-narrated audio reaches Audible through
aggregators or Amazon's own Virtual Voice programme instead, **at roughly 25% net royalty against
ACX exclusive's 40%**. ACX is piloting an authorized Voice Replica route where the narrator's own
replica is used under their review, which is the path a self-narrated clone would eventually want.

**So the two paths are not competing on quality. They are competing on what the audiobook is for.**

| if the audiobook is… | the path |
|---|---|
| **a debt to 16 people** | **Path A. ~$200, no retailer, done in weeks** |
| a product you intend to sell | **Path B**, or Path A through the authorized replica route, and the royalty and eligibility questions come first |

## Ruled 2026-08-24

**One voice throughout, no announcement, and a test chapter first.** Wendell: *"I'm not going to
announce it or do chapter 9 myself it would be weirder to have own chapter sound different. I will
try in a chapter and see if I like the output."*

**The Chapter 9 argument was better than the one it overruled.** A single chapter in a different
voice makes a listener hear the seam rather than the sincerity, and tonal consistency across
twelve hours outranks the authenticity of one passage. Recorded because the earlier recommendation
here said the opposite.

**On disclosure, one fact rather than a re-argument.** Not announcing is unconstrained for direct
delivery to sixteen people. It becomes a compliance question only on the retail path: Amazon
requires AI-narration disclosure on Virtual Voice, and ACX requires human narration outright.
**Direct delivery touches neither**, so the ruling and the retail question do not collide unless
and until the audiobook goes on sale.

## The scripts exist now — `instruments/build_narration.py`

**Raw markdown fed to a synthesis engine reads the asterisks.** So the fourth build target now
exists beside `build_pdf` and `build_epub`, and it produces exactly what a voice can read.

```
python3 instruments/build_narration.py --chapter 1
python3 instruments/build_narration.py --all
```

| | words | characters | at 150 wpm |
|---|---|---|---|
| **ch1 — the test chapter** | **9,100** | **48,536** | **1h 00m** |
| All nine chapters | 107,058 | **600,933** | **11h 53m** |

**Three judgements are built in, and each one is counted rather than silent.** Tables are dropped
(a polarity map read aloud is a list of nouns with no grammar) — 55 lines across the book.
Marginalia, treatises and signatures are **extracted to sidecar files** rather than narrated,
because they are other hands and one voice reading both collapses the membrane `SPEC_TWO_HANDS`
exists to hold — 59 blocks. Headings are **kept and spoken**, because a listener with no page has
no other signpost. Chapter titles are un-capsed, since a synthesis engine reads caps as shouting.

**The apparatus decision stays open on purpose.** Sidecars are written per chapter, so a second
cloned voice, a tonal shift, or omission are all still available without re-running anything.

## What the test costs

**ch1 is 48,536 characters, which fits inside one ElevenLabs Creator month — $22.** That is the
whole price of finding out whether the clone is good enough, and it is small enough that the
answer should be bought rather than argued about.

**If it passes, the full nine chapters are 600,933 characters** — two months of Pro at $99, so
**about $200**, matching the earlier estimate now that tables and apparatus are out.

## Before committing

- [ ] **Confirm the sixteen.** The count comes from a 2023 export, not the dashboard
- [ ] Rule on **appendices in or out** — three of eight do not read aloud
- [ ] Rule on **the apparatus voices** — marginalia and treatises, one voice or several
- [ ] Get a **sample generated and listen to Chapter 9's depression-well passage** before buying
      any quota. That passage is the test; if it fails there, Path A is decided against on the
      merits rather than on price
- [ ] Check ElevenLabs' **current** commercial terms and PVC tier directly — pricing here is from
      2026 secondary sources, and `elevenlabs.io` was not reachable from this session

## What I could not check

- **ElevenLabs' live pricing page.** Figures above are from 2026 secondary sources; treat them as
  an order of magnitude, not a quote.
- **Whether any audiobook work already exists** outside this repo. `The Library/` is unreachable
  from here.
- **Your existing recording setup**, which decides whether Path B has a hardware cost at all.

---

## Sources

- [ElevenLabs Pricing (2026): Plans, Credits, Commercial Rights, and API Costs](https://bigvu.tv/blog/elevenlabs-pricing-2026-plans-credits-commercial-rights-api-costs/)
- [ElevenLabs Pricing (2026): Plans, Voice Cloning Costs, and Alternatives](https://magichour.ai/blog/elevenlabs-pricing)
- [ElevenLabs Pricing for Creators & Businesses](https://elevenlabs.io/pricing)
- [Does ACX Allow AI-Narrated Audiobooks? (Current 2026 Policy)](https://www.audie.ai/does-acx-allow-ai-narrated-audiobooks-current-2026-policy)
- [Are AI Audiobooks Accepted on Audible in 2026? The Current Rules](https://storyvox.app/blog/are-ai-audiobooks-accepted-on-audible-2026-rules)
- [ACX Testing AI Program to Replicate Narrators Voices](https://www.publishersweekly.com/pw/by-topic/industry-news/audio-books/article/95904-acx-testing-ai-program-to-replicate-narrators-voices.html)
