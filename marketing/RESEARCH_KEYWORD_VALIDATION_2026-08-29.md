---
type: research
title: "Validating KDP keywords — the two passes, and what each one can prove"
aliases:
  - keyword validation
  - kdp keyword research
  - keyword indexing
tags:
  - marketing
  - mtgoa
  - kdp
  - amazon
created: 2026-08-29
review: 2026-09-12
source:
  - marketing/ANALYSIS_KDP_DESCRIPTION_2026-08-27.md
  - marketing/KDP_LISTING_2026-08-29.md
  - instruments/kdp_keywords.py
---

# Validating KDP keywords — the two passes, and what each one can prove

**Wendell, 2026-08-29:** *"do research on validating keywords for KDP."*

**The finding that reorganises everything else: validation is two different questions asked
at two different times**, and almost every guide runs them together.

| | before publishing | after publishing |
|---|---|---|
| the question | **does anybody type this** | **has Amazon associated the book with it** |
| the instrument | Amazon's autocomplete dropdown | a search for the phrase and the ASIN together |
| what a failure means | nobody searches it, so replace the phrase | the book cannot rank on it, whoever searches |
| when you can run it | now | 24–72 hours after Live |

**Neither one answers the other.** A phrase can have real demand and no index, and a phrase
can index perfectly while nobody on earth types it. **Both are free.**

---

## 1 · Pass one — does anybody type this

**The dropdown is the demand signal and the results page is not.** Type the first two or
three words of a candidate into Amazon's search box and read what Amazon offers to complete
before pressing enter. Those completions are aggregated real queries. If Amazon does not
suggest your phrase or something adjacent, that is the finding.

**The alphabet pass is the same endpoint, worked harder.** Type the seed, a space, then each
letter in turn — *helper burnout a*, *helper burnout b* — and harvest what comes back. Indie
authors have run this since roughly 2015, and **it is the endpoint the paid tools resell**.
The interface is what costs $97, not the data.

**Then judge the competition from the results page, not from the number of results.** The
useful reading is the shape of page one rather than its length: a phrase with 20,000 results
and weak leaders is easier than one with 5,000 dominated by imprints. The reported target is
**page one carrying books with 50–200 reviews and sales ranks between roughly 20,000 and
100,000** — books at your weight class. Page one full of five-thousand-review titles from
major publishers means the phrase is real and not yours.

## 2 · Pass two — is the book indexed for it

**Search the phrase and the ASIN together in one query.** If the book comes back, Amazon has
associated it with that phrase. If the result is empty, it has not, and **a book cannot rank
on a phrase it is not indexed for.**

**This is a seller-side technique applied to books**, reported consistently across
seller-tool documentation and repeated in author guides. It is not something Amazon
publishes, and it is the least well-sourced claim in this document.

**Timing, and it matters more than the technique.** Reported windows:

- **24–48 hours** from clicking Publish to the book appearing in the catalogue.
- **Up to 72 hours** after Live for search visibility across marketplaces.
- **About 24 hours** for a keyword change to register, but **two to four weeks** for the
  algorithm to fully reflect it.
- **Five to seven days minimum** before judging whether a change did anything, because sales
  rank moves on weekly cycles and same-day movement is noise.

**So a keyword that fails the index check on day one has not failed.** It has not been asked
yet. That is the single most useful line in this research, because the temptation on day two
is to start swapping fields.

## 3 · The rules that are mechanical, and one tier that is not

**Four rules cost you efficiency**, and `instruments/kdp_keywords.py` now checks all four
without needing Amazon:

- **50 bytes per field, and it is bytes.** A smart quote or an em dash costs two or three,
  and **an overflowing field can be ignored entirely** rather than truncated.
- **Spaces, not commas.** A comma is indexed as content and buys nothing.
- **Nothing already in the title, subtitle or author name.** Those are indexed separately.
- **No word twice across the seven fields.** **Amazon concatenates all seven into one
  index**, so a repeat in field three of a word from field one accomplishes nothing. Word
  order inside a field does not matter either — the phrase is indexed in every arrangement.

**One tier is a compliance problem rather than an inefficiency**, and it is worth separating
because the consequence differs:

| prohibited | why |
|---|---|
| *bestseller*, *#1*, *award-winning*, *top-rated*, *must-read* | subjective claims |
| other authors' names, other book titles | competitor targeting, explicitly banned |
| *Kindle Unlimited*, *KDP Select*, *Prime Reading* | Amazon brand terms, and they do not help |
| *available now*, *brand new*, *coming soon* | time-sensitive |
| a category the book is not in | misrepresentation |

**None of the seven fields for this book trips any of it**, checked. The instrument now
flags this tier separately from the waste tier, because *wasteful* and *against the terms*
should not print the same way.

## 4 · Free tooling, updated from `ANALYSIS_KDP_DESCRIPTION` §5a

**The §5a finding holds and has one confirmation.** `KDP Scout` — the open-source
command-line tool that mines Amazon autocomplete — is real, was released in **March 2026**,
and exists specifically because commercial tools wrap the same free endpoint.

**Three more free options worth knowing:**

| tool | cost | what it adds |
|---|---|---|
| **Amazon's own search box** | free | the actual signal, and the input every other tool resells |
| **KDP Scout** | free, open source | the alphabet pass automated into hundreds of long-tail variants |
| **Sonar** (Helium 10) | free | a keyword database, no account needed for basic use |
| **Keyword Tool Dominator** | free tier | the alphabet pass in a browser, **2 searches per day** |
| **Publisher Rocket** | ~$97 one-off | estimated competition and volume figures on top of the same base |

**The division of labour is unchanged: the model proposes, the autocomplete disposes.** The
seven fields in `KDP_LISTING_2026-08-29.md` are reasoned from the reader and are worth
nothing until the dropdown confirms them.

## 5 · What I could not verify, and it is a real limit

**Amazon and most publishing sites are blocked from this session.** `kdp.amazon.com` returns
403 at the egress proxy, and so do `kindlepreneur.com`, `vappingo.com`,
`searchenginejournal.com` and `sellershorts.com` — every page I tried to read directly.

**So this document is built from search-result extracts rather than from primary pages**, and
none of it is read off KDP's own help. The mechanics in §3 are consistent across many
independent write-ups, which is the best evidence available from here and is not the same as
a source. **Two claims are worth confirming against the live KDP help page before relying on
them:** the 50-byte behaviour on overflow, and the prohibited-terms list in full.

**This is the same correction shape as 2026-08-27**, when *"every byte spent re-typing a
title word is wasted"* turned out to be a recommendation rather than a mechanism. Watch the
stated certainty rather than the advice, because the whole genre is written by people
selling tools.

## 6 · The order to run it

1. **Publish with the current seven.** They pass every mechanical rule and nothing gates the
   proof on them. Keywords are editable at any time.
2. **Run pass one now** — `python3 instruments/kdp_keywords.py` prints the seeds and the
   search links. An hour, no money. Replace anything the dropdown does not complete.
3. **Order the proof.** It is in the post while the rest of this happens.
4. **Wait 72 hours after Live**, then run pass two —
   `python3 instruments/kdp_keywords.py --index <ASIN>` prints the seven index checks.
5. **Change at most two fields at a time**, and wait five to seven days before reading the
   result. Changing all seven teaches you nothing about any of them.

**Sources.** [Kindlepreneur on choosing Kindle
keywords](https://kindlepreneur.com/how-to-choose-kindle-keywords/) ·
[Kindlepreneur on the seven boxes](https://kindlepreneur.com/7-kindle-keywords/) ·
[Search Engine Journal on Amazon indexing](https://www.searchenginejournal.com/amazon-indexing/289093/) ·
[Vappingo's KDP search diagnostic](https://www.vappingo.com/word-blog/why-is-my-kdp-book-not-showing-up-in-amazon-search-a-diagnostic-guide-that-works/) ·
[Vappingo on prohibited KDP keywords](https://www.vappingo.com/word-blog/prohibited-kdp-keywords/) ·
[ManuscriptReport on the seven slots](https://manuscriptreport.com/blog/amazon-kdp-keywords) ·
[BookBeam on picking Amazon keywords](https://bookbeam.io/blog/how-to-pick-amazon-keywords/) ·
[KDP Scout, open-sourced](https://medium.com/@randypellegrini/i-built-a-free-keyword-research-tool-for-self-published-authors-and-open-sourced-it-d53c1adb9033) ·
[Keyword Tool Dominator](https://www.keywordtooldominator.com/amazon-keyword-tool) ·
[Reedsy on Amazon keywords](https://reedsy.com/blog/guide/kdp/amazon-keywords/)
