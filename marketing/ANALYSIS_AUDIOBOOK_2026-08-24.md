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

## What I would do

**Discharge the debt with Path A and keep Path B as the product.** They are not exclusive. Sixteen
people are owed something now and have waited three years; ~$200 and a proofing pass ends that.
**A self-narrated retail edition can come later and be a better thing**, and having shipped the
first one is not an argument against the second.

**With one exception: narrate Chapter 9 yourself either way.** It is one chapter, about ninety
minutes finished, and it is the passage where a synthetic voice costs the most.

**Tell the sixteen which they are getting.** *"This is an AI reading in my voice, and here is why"*
is a sentence this audience will accept from this author, who has spent a book arguing that naming
the mechanism beats hiding it. Discovering it unannounced is the version that goes badly.

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
