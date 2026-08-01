# PASS 3 · LINE EDITOR — book-wide scan, 2026-08-01

**Role:** Line Editor, `specs/EDITORIAL_OPERATING_SYSTEM.md` §3 — readability only.
**Branch:** `claude/pass-3-line-editor-scan-09nc6f`. Apparatus only; **no file in
`manuscript/` is touched by this branch**, per DL-18.
**Doctrine:** diagnosis before revision. Nothing here is applied. Every flag is a
candidate for Wendell, and *leave as-is* is a first-class outcome.

Scanned against the merged manuscript at `ee18459` — the book as it stands after the
DL-19 and DL-20 work of 2026-08-01, not the `625aaab` snapshot the July reports analyse.

---

## 1 · What ran

| Instrument | Result |
|---|---|
| `instruments/gate.py` | GATE PASS — 0 on all four surfaces, before and after |
| `instruments/line_scan.py` | **new.** 186 candidates across six rules |
| `instruments/dupes.py` | 1 exactly repeated sentence (ch7) |
| `instruments/prose_diet.py` | heavy: ch7 passive 1.49, ch5 passive 1.35; everything else under 1.30 |
| `marginalia/review.py` | BLOCK 13 · WARN 106 · INFO 168 |
| `instruments/rescan.py` | 85 LIVE · 48 PARTIAL · 39 GONE **(corrected — see §2)** |
| `instruments/placeholders.py` | 1 — `ch1:269`, the deferred app CTA. Unchanged, still P0 |

`line_scan.py` is new and is the point of this pass. The Line Editor's brief names six
defects and this repo had an instrument for none of them: `gate.py` scores the canon
list, `prose_diet.py` scores register drift against *Igniting Joy*, `review.py`
adjudicates voice, `dupes.py` catches one exact repeat. None of them asks the Line
Editor's question, which is narrower: *where does a reader have to double back for
something the sentence should have handed her.*

```
file        orphan-ref      repeat     doubled        hard      notbut  banned-kin   total
ch1.md               2           2           0          12           0           0      16
ch2.md               0           2           0           5           0           0       7
ch3.md               2           6           0          20           0           1      29
ch4.md               0           8           0           9           1           0      18
ch5.md               2           7           0          11           0           2      22
ch6.md               0           8           0          11           0           2      21
ch7.md               0          16           0          13           1           3      33
ch8.md               0           3           0          14           0           0      17
ch9.md               0          11           0          10           0           2      23
TOTAL                6          63           0         105           2          10     186
```

**186 candidates became 33 flags.** That ratio is the instrument working as designed,
not failing: `repeat` cannot tell a refrain from an accident, and most of the 63 are
the book's own conventions — the BAR capture formula, the five-channel section
template, the Move recaps. Every rule's precision is recorded in §5 so the next pass
starts from measured behaviour rather than from the count.

`doubled` returns 0 book-wide. It found `the The Emotional Body` in the July reports'
quoted evidence and finds nothing on the page, which is the corroboration that the
defect was fixed and the rule works.

## 2 · An instrument correction — `rescan.py` was reporting fixed lines as LIVE

`rescan.py` decides whether a July finding still quotes text that is on the page. Its
test was `norm(quote)[:60] in corpus` — **the first sixty characters of the
quotation.** Sixty characters is about a clause, and a fixed defect almost always sits
later in the sentence than that. So:

| finding | July evidence | on the page 2026-08-01 | old verdict |
|---|---|---|---|
| ch1 L2 | "…never sees a point of it" | "never sees **a penny** of it" | LIVE |
| ch1 L4 | "…how to win **and succeed**" | the doublet is gone | LIVE |
| ch1 L6 | "…the same **quieter** thing" | the banned word is gone | LIVE |
| ch6 L1 | "the **The** Emotional Body" | the doubled article is gone | LIVE |

Four fixed lines sitting in a working list as actionable work. The prefix was not a
careless choice — the reports elide long evidence with `…`, and a full-string match
fails on every one of those. The fix splits each quotation on sentence ends **and on
the ellipsis**, then tests each piece, which also gives the honest verdict for a
two-sentence quote whose second sentence was rewritten: PARTIAL, not LIVE.

```
                     LIVE  PARTIAL  GONE
before (60-char)      102       31    39
after  (per piece)     85       48    39     41 verdicts change
```

No finding moves *into* work that was not already there. The LINE band drops from 29
to 28 and, more usefully, stops asserting that four demonstrably-fixed lines are live.
Recorded in the file's own docstring, in the repo's habit of writing the correction
next to the rule it corrects.

## 3 · Closed by edit since 2026-07-31 — verified gone, do not re-run

The July line findings the prose has already answered. Each verified by string search
against `manuscript/`, not by reading a status column.

| finding | what it flagged | evidence now |
|---|---|---|
| CH1 L1 | "the payoff" with no antecedent | reads "Look at what **that stash** really buys you", antecedent at ch1:147 |
| CH1 L2 | "never sees a point of it" | "a penny of it" — 0 hits for the old phrase |
| CH1 L4 | "win and succeed" doublet | 0 hits |
| CH1 L5 | Yu-kai Chou introduced twice | second mention is now a back-reference, "Chou's decade of mapping" (ch1:137) |
| CH1 L6 | "quieter" in the banned family | 0 hits; `gate.py` now matches `quiet(ly\|er\|est)` too |
| CH2 L5 | "When you see it as pattern … after that" | 0 hits |
| CH2 L6 | "nearer the center" twice | 1 hit, ch2:374 |
| CH3 L4 | "These five are what…" twice in a paragraph | 1 hit, ch3:728 |
| CH4 L5 | "Five modes, five channels, no overlap" | 0 hits |
| CH6 L1 | "the The Emotional Body" | 0 hits; `line_scan.py` `doubled` reads 0 book-wide |
| CH6 L5 | "showing up before and after itself" | 0 hits |
| CH6 L6 | the eighteen-months blueprint pair | 1 hit, ch6:415 |
| CH7 L1 | Field-Holder's two sentences printed twice | "collapse masquerading as calm" — 1 hit, ch7:349 |
| CH7 L4 | "one sentence' worth of time" | 0 hits |
| CH9 L3 | "A different journey" | 0 hits |
| CH9 L4 | "…just shows you what walking looks like" | rewritten to "is another stretch of the same road" (ch9:366) |

**CH7 L2 was a false flag and is withdrawn.** "You build a practice…" appears twice
because `**The structure of the X:**` is the chapter's template across all five channel
sections (ch7:335, 375, 413, 457, 467). A convention used five times is a convention.

## 4 · The flags — 33, chapter by chapter

Format is the Lean OS Line Editor's own: location · original · diagnosis · minimal
proposed edit · reader problem solved · risk to voice · leave-as-is rationale. Line
numbers are on-disk, in the files as they stand on this branch.

---

### Chapter 1 — 2 flags

**LE-1 · `ch1:44` · vague reference**
> Children receive care or not based on whether you actually understand something, and your theory of harm stays invisible to them.

- **Diagnosis:** *something* has no referent, and the two clauses joined by *and* do
  different jobs — one is a condition of care, the other a fact about visibility. It is
  the only abstraction in a list whose other two members are concrete.
- **Minimal edit:** "Children receive care or not based on whether you actually
  understand what they need, and your theory of harm is invisible to them either way."
- **Reader problem solved:** the paragraph proving that fluency earns nothing stops
  going abstract in its middle example.
- **Risk to voice:** low. The register here is already plain.
- **Leave as-is if:** the withholding is deliberate and the sentence is meant to enact
  the not-understanding it describes.

**LE-2 · `ch1:48` · say the noun**
> Fewer of us are willing to ask whether the vocabulary we have built does the same thing less visibly: a set of conditions to meet before the real help arrives.

- **Diagnosis:** *the same thing* is the say-the-noun defect at the chapter's sharpest
  analogy. The noun is one sentence back — missionaries requiring **conversion** before
  food — and never named here. Note this line already carried the July `quieter` fix;
  the edit removed the banned word and kept the empty noun.
- **Minimal edit:** "…whether the vocabulary we have built asks for the same
  conversion, less visibly: a set of conditions to meet before the real help arrives."
- **Reader problem solved:** the analogy lands as an argument instead of a gesture.
- **Risk to voice:** low; *conversion* is the paragraph's own word.
- **Leave as-is if:** naming it makes the charge too explicit for a paragraph that
  wants the reader to arrive at it herself.

### Chapter 2 — 3 flags

**LE-3 · `ch2:57` · antecedent across a marginalia block** *(carry-forward, CH2 L2)*
> The subject of that sentence is the work. Your effort is real.

- **Diagnosis:** *that sentence* is `ch2:44` — "The feeling is this: *this isn't
  working.*" — thirteen lines and a nine-line margin block back. The margin is a
  different voice, so the reader's eye has left the body and returned.
- **Minimal edit:** "The subject of *this isn't working* is the work."
- **Reader problem solved:** the chapter's first reframe stops depending on a pointer
  that crosses a voice change.
- **Risk to voice:** none — it quotes the book's own line.
- **Leave as-is if:** the margin is understood to be skippable and the pointer reads
  cleanly to someone who skipped it.

**LE-4 · `ch2:107` · parse failure** *(carry-forward, CH2 L1)*
> Most people turn back. The ones who don't push through instead of going through: they override the sensation, run on fumes, and eventually the body stops cooperating.

- **Diagnosis:** *the ones who don't* has to be read as *the ones who don't turn
  back*, but *push through* attaches to *don't* on first pass and delivers the exact
  opposite meaning. The July edit replaced an em-dash with a colon; the ambiguity is in
  *don't*, so the colon did not reach it.
- **Minimal edit:** "The ones who don't **often** push through instead of going
  through: they override the sensation…"
- **Reader problem solved:** the failure mode the chapter is built to name is legible
  on the first read.
- **Risk to voice:** low; one word.
- **Leave as-is if:** the stumble is wanted, since the sentence describes a stumble.

**LE-5 · `ch2:370` · unheralded first person** *(carry-forward, CH2 L3)*
> When the Protector holds the joystick, I walk into a conversation already armored, braced against something that has not happened, and the person across from me meets the hull before they meet me.

- **Diagnosis:** one sentence of *I* between two *you* paragraphs, with no testimony
  frame around it. DL-4 and DL-19 already ruled this shape; the DL-19 fix at `ch3:258`
  was exactly this move to second person.
- **Minimal edit:** "When the Protector holds the joystick, **you** walk into a
  conversation already armored, braced against something that has not happened, and the
  person across from **you** meets the hull before they meet **you**."
- **Reader problem solved:** one author per surface, which is the ruled state.
- **Risk to voice:** low, and it removes an unowned *I* rather than adding one.
- **Leave as-is if:** Wendell wants this as testimony, in which case it needs the frame
  the other testimonies get, not a pronoun swap.

### Chapter 3 — 5 flags

**LE-6 · `ch3:894` · pronoun with no antecedent** *(carry-forward, CH3 L1)*
> Quests come from the Show Up cards, and every card in it ends in an artifact, and an artifact is something another person can encounter.

- **Diagnosis:** *it* has no singular referent; the noun in front of it is plural
  (*cards*). This is a straight agreement error in the sentence that defines a quest.
- **Minimal edit:** "Quests come from the Show Up cards, and **every one of them** ends
  in an artifact…"
- **Reader problem solved:** the definition the appendix depends on parses.
- **Risk to voice:** none.
- **Leave as-is if:** *it* is meant to name the deck, in which case the deck has to be
  the subject of the clause.

**LE-7 · `ch3:896` · a card name arriving as known**  *(carry-forward, CH3 L2)*
> *Aim the Awareness* becomes: **I will tell Dana what I noticed in Tuesday's meeting and not soften it, before Friday, and it will cost me her thinking I am difficult.**

- **Diagnosis:** *Aim the Awareness* is used as an established card name and returns
  one hit in the whole chapter — this one. The reader is asked to recognise something
  she has not met.
- **Minimal edit:** "A Show Up card like *Aim the Awareness* becomes: …"
- **Reader problem solved:** the worked example stops implying a missed page.
- **Risk to voice:** low.
- **Leave as-is if:** the card names are seated elsewhere in the shipping deck and the
  chapter is deliberately gesturing at it.

**LE-8 · `ch3:311` · dangling modifier**  *(carry-forward, CH3 L3)*
> This stage can take five seconds or can run throughout, and you keep noticing the feeling across the whole experience.

- **Diagnosis:** *throughout* has no object. The clause after it supplies the meaning,
  which means the reader carries an unresolved word until she gets there.
- **Minimal edit:** "This stage can take five seconds or run the length of the
  encounter, and you keep noticing the feeling the whole way through."
- **Reader problem solved:** the WAVE's first stage states its own duration.
- **Risk to voice:** none.
- **Leave as-is if:** *throughout* is doing colloquial work the fuller phrasing loses.

**LE-9 · `ch3:691` · a modifier attached to the wrong place**  *(carry-forward, CH3 L6)*
> So take the move where it counts, out of the forest, where nothing costs you and no one is watching, and into the places allyship actually happens.

- **Diagnosis:** *where nothing costs you* is meant to modify *the forest* but follows
  *where it counts*, so the first reading is that the move counts where nothing costs
  you — the reverse of the chapter's argument, at its hinge.
- **Minimal edit:** "So take the move **out of the forest**, where nothing costs you and
  no one is watching, and into the places allyship actually happens."
- **Reader problem solved:** the Feeling-to-Function turn says what it means the first
  time.
- **Risk to voice:** none; it cuts three words.
- **Leave as-is if:** *where it counts* is load-bearing enough to keep and can be moved
  to the tail instead.

**LE-10 · `ch3:810` · the same thing called two incompatible things**  *(carry-forward, CH3 L5)*
> The read has four domains, and one cheap habit that is none of them. … that is the awareness trap, the domain that swallowed the others because you can run it from the chair.

- **Diagnosis:** inside one paragraph the awareness trap is *none of them* and then
  *the domain*. A reader tracking the taxonomy has to pick one and will pick wrong half
  the time.
- **Minimal edit:** "…that is the awareness trap, **the habit** that swallowed the
  others because you can run it from the chair."
- **Reader problem solved:** the four-domain count stays four.
- **Risk to voice:** none.
- **Leave as-is if:** the trap is genuinely a fifth domain, in which case the opening
  sentence is the one to change.

### Chapter 4 — 4 flags

**LE-11 · `ch4:163` · grammar**  *(carry-forward, CH4 L3)*
> The Challenger learned this the hard way, by watching boundaries dissolve, relationships violate, and lines get crossed because someone stated a preference instead of drawing a line.

- **Diagnosis:** *violate* is transitive; in this parallel series it reads as a typo
  the reader repairs mid-sentence, in the treatise's opening claim.
- **Minimal edit:** "…by watching boundaries dissolve, relationships **rupture**, and
  lines get crossed…"
- **Reader problem solved:** the series parses and the three verbs stay parallel.
- **Risk to voice:** none. Corin's register is blunt, not ungrammatical.
- **Leave as-is if:** the misuse is characterisation, in which case it should be one
  the reader can tell from an error.

**LE-12 · `ch4:171` · vague reference**  *(carry-forward, CH4 L1)*
> The Challenger's gift is meaning it. From outside it will look like fighting. Ignore that.

- **Diagnosis:** *that* has three candidates in ten words — the appearance, the outside
  view, the fighting — and the sentence is an instruction, so the ambiguity costs
  compliance rather than comprehension.
- **Minimal edit:** "From outside it will look like fighting. **Let it look like that.**"
- **Reader problem solved:** the instruction says what to do rather than what to ignore.
- **Risk to voice:** low; it keeps the three-beat rhythm.
- **Leave as-is if:** the clipped *Ignore that* is the Challenger's voice doing work no
  longer sentence can do.

**LE-13 · `ch4:434` · an unnamed manner and an unfindable pronoun**  *(carry-forward, CH4 L4)*
> Months of swallowed charge, wrong target, wrong register. Everything stopped in a particular way. They didn't come back after that.

- **Diagnosis:** *in a particular way* names nothing, and *they* has no antecedent —
  the nearest plural is *well-meaning people*, five sentences back and the wrong
  referent. This is the passage's emotional landing.
- **Minimal edit:** "Everything stopped. **The people on the other end of it** didn't
  come back."
- **Reader problem solved:** the consequence is attached to somebody.
- **Risk to voice:** low; the cut of *in a particular way* sharpens the beat.
- **Leave as-is if:** the vagueness is protecting a real person's identity, in which
  case say so in the sentence.

**LE-14 · `ch4:360` · an instruction written as a description**  *(carry-forward, CH4 L6)*
> You let the field settle. You do not retraumatize the other person by returning to the confrontation before the moment has passed.

- **Diagnosis:** the Rest stage's one rule arrives as a statement about what the reader
  does not do, in a paragraph already carrying two *you do not* constructions. A reader
  who does return to the confrontation is told, grammatically, that she did not.
- **Minimal edit:** "You let the field settle. **Do not return to the confrontation
  before the moment has passed.**"
- **Reader problem solved:** the stage's only rule is issuable.
- **Risk to voice:** low; the chapter already uses the imperative.
- **Leave as-is if:** the descriptive frame is deliberate, to avoid stacking commands.

### Chapter 5 — 6 flags

**LE-15 · `ch5:189` · the answer does not match the question**  *(carry-forward, CH5 L1)*
> Here's what it is: a question about what you built instead, and whether it lasted, and whether you can see the connection.

- **Diagnosis:** *it* is the School of the Oath. A School is not a question, so the
  sentence's own grammar says the wrong thing about the thing it is defining.
- **Minimal edit:** "Here's what it **asks**: what you built instead, whether it
  lasted, and whether you can see the connection."
- **Reader problem solved:** the School's definition is a School.
- **Risk to voice:** none.
- **Leave as-is if:** *it* refers to the objection rather than the School, in which
  case the previous sentence needs the pointer.

**LE-16 · `ch5:272` · two pronouns, two referents, one sentence**  *(carry-forward, CH5 L2)*
> That is the Regent's pair in active tension. It goes on record here because from the inside it reads as weakness, and keepers before you have filed the tension under that name.

- **Diagnosis:** the first *it* is the act of recording, the second is the tension.
  *Goes on record* is the Head's in-world register arriving mid-instruction, which is
  what makes the first *it* hard to place.
- **Minimal edit:** "That is the Regent's pair in active tension. It is **named** here
  because from the inside **the tension** reads as weakness, and keepers before you
  have filed it under that name."
- **Reader problem solved:** one referent per pronoun in a sentence that has to carry
  the pair.
- **Risk to voice:** *goes on record* is Sera's register; losing it costs a little
  colour. Recorded as a real trade.
- **Leave as-is if:** the register is worth the ambiguity here.

**LE-17 · `ch5:492` · accidental repetition, garden path**  *(carry-forward, CH5 L3)*
> That is the only reason anything inherited ever improves, and it will look like meddling to somebody. Somebody repaired every tradition still worth having, noticed it failing, and did something about it instead of calling the failure sacred.

- **Diagnosis:** *somebody* ends one sentence as an indefinite object and opens the
  next as an indefinite subject. The reader binds them to the same person and has to
  unbind them a clause later.
- **Minimal edit:** "…and it will look like meddling to somebody. **Every tradition
  still worth having was repaired by someone who noticed it failing** and did something
  about it instead of calling the failure sacred."
- **Reader problem solved:** the Fixer-Healer's defence lands on the first read.
- **Risk to voice:** low, and the rewrite puts the tradition in the subject where the
  argument is.
- **Leave as-is if:** the echo is deliberate rhetoric.

**LE-18 · `ch5:546` · a parenthesis between a definition and its object**  *(carry-forward, CH5 L5)*
> …which puts what you received into a form the next person can receive (endurance and loyalty are the entry requirements): the account of where this came from, what it cost, what broke, what still holds, and why any of it is worth their time.

- **Diagnosis:** requirements for what — the parenthesis introduces a second idea
  between the definition and the colon that completes it, and its own referent is
  unstated.
- **Minimal edit:** cut the parenthesis. "…into a form the next person can receive: the
  account of where this came from, what it cost, what broke, what still holds, and why
  any of it is worth their time."
- **Reader problem solved:** the superpower's definition arrives in one move.
- **Risk to voice:** none; it removes an aside.
- **Leave as-is if:** the entry-requirements point is load-bearing, in which case it
  wants its own sentence.

**LE-19 · `ch5:619` · pronoun with three candidates**  *(carry-forward, CH5 L6)*
> The Regent's Show Up cards are the only ones in the deck built entirely out of verbs for keeping: hold, keep, sustain, tend. Nothing in it is made.

- **Diagnosis:** *it* can be the deck, the Regent's cards, or the verb set. The
  sentence is the section's point, so a wrong bind costs the point.
- **Minimal edit:** "**Not one of them makes anything new.**"
- **Reader problem solved:** the contrast between keeping and building is stated
  against the right noun.
- **Risk to voice:** low.
- **Leave as-is if:** *it* is the deck and the claim is about the whole deck, which
  would be a different and larger claim.

**LE-20 · `ch5:520` · register break inside a spoken line**  *(carry-forward, CH5 L4)*
> *Tell me what is broken. All of it, in detail: that is the report I want, and I will act on it. Whether I commit is not in your remit. That was settled when I accepted this.*

- **Diagnosis:** *remit* is administrative English inside an address to a daemon that
  is otherwise plain and physical. The reader stops on the word rather than on the
  boundary being drawn.
- **Minimal edit:** "Whether I commit is **not yours to decide.**"
- **Reader problem solved:** the address to the Fixer-Healer stays in one register.
- **Risk to voice:** the Regent's register is formal by design; this is the one line
  where formality reads as jargon rather than as ceremony. Wendell's call.
- **Leave as-is if:** *remit* is the Regent's diction and the reader is meant to feel
  the officialdom.

### Chapter 6 — 3 flags

**LE-21 · `ch6:155` · empty noun doing load-bearing work**  *(carry-forward, CH6 L3)*
> Exiling that one makes sense. The discipline goes out with it, and the discipline alone addresses the thing above.

- **Diagnosis:** *the thing above* points at a paragraph rather than a noun, and it is
  the pivot of the exile argument.
- **Minimal edit:** "…and the discipline is the only thing that keeps a relational
  field from becoming a leverage point in the first place."
- **Reader problem solved:** the reason not to exile the Architect is stated instead of
  gestured at.
- **Risk to voice:** low; it reuses the paragraph's own terms.
- **Leave as-is if:** the referent is something other than the KPI move above it, in
  which case name that instead.

**LE-22 · `ch6:389` · "the other one" with no other one**  *(carry-forward, CH6 L2)*
> Six seconds is enough for the question that is actually being asked. It is not enough for the other one, and that shortfall is the point.

- **Diagnosis:** one question is named; the second is implied and never stated, so *the
  other one* asks the reader to supply the term the sentence is about.
- **Minimal edit:** "It is not enough for **the question underneath it**, and that
  shortfall is the point."
- **Reader problem solved:** the shortfall has two sides.
- **Risk to voice:** none.
- **Leave as-is if:** the second question is named in the lines above and the pointer
  is closer than it looks.

**LE-23 · `ch6:340` · 48 words, subject and verb twenty apart**
> The reason you can walk into an organization and know, before you have seen a single number, that something has gone wrong under the third floor of the org chart, comes down to this: the Emotional Body registered it and the rest of you is still catching up.

- **Diagnosis:** *the reason … comes down to this* is separated by twenty words of
  subordinate material. `line_scan.py` flags it at 48 words; the paragraph around it
  runs shorter, so the rhythm drops exactly where the claim is.
- **Minimal edit:** "You can walk into an organization and know something has gone
  wrong under the third floor of the org chart before you have seen a single number.
  The Emotional Body registered it; the rest of you is still catching up."
- **Reader problem solved:** the chapter's claim about the Emotional Body as sensor
  arrives in one breath.
- **Risk to voice:** low; the split is into two sentences the chapter already uses.
- **Leave as-is if:** the long build is deliberate and the payoff wants the delay. Note
  separately that the sentence asserts a capacity Jordan may not have yet — that is
  CH6 L4 and a structural question, not this one.

### Chapter 7 — 3 flags

**LE-24 · `ch7:77` · 56-word not/but, at the reader's first meeting with Hold**  *(carry-forward, CH7 L6)*
> **Hold** is the maintenance of enough safety that difficult conversation remains possible even when the field is charged, not the four seconds of Stand you learned from the Challenger, where one person declines to take back one line, but the sustained containment of a whole field over the length of a hard conversation, sometimes over months.

- **Diagnosis:** the reader holds a negation open across a clause and a half before the
  *but* resolves it. It is one of two `notbut` hits in the book, and it lands on a
  five-stage definition list where the other four stages are one sentence each.
- **Minimal edit:** "**Hold** is the maintenance of enough safety that difficult
  conversation remains possible even when the field is charged. It is not the four
  seconds of Stand you learned from the Challenger, where one person declines to take
  back one line; it is the sustained containment of a whole field over the length of a
  hard conversation, sometimes over months."
- **Reader problem solved:** the stage list stays parseable at the stage that carries
  the chapter.
- **Risk to voice:** low; nothing is cut.
- **Leave as-is if:** the long held negation is the felt experience of Hold and is
  wanted as enactment.

**LE-25 · `ch7:87` · the pronoun binds to the misunderstanding**  *(carry-forward, CH7 L5)*
> Niceness, conflict-avoidance dressed in the language of harmony, and the absence of judgment in the service of false peace all get mistaken for it. It is the altitude at which a person can hold multiple valid perspectives simultaneously.

- **Diagnosis:** the nearest antecedent for the second *It* is the mistaking, not the
  Diplomat's altitude. The sentence defining the altitude opens by pointing at the
  wrong thing.
- **Minimal edit:** "**The Diplomat's altitude is the one** at which a person can hold
  multiple valid perspectives simultaneously."
- **Reader problem solved:** the definition attaches to what is being defined.
- **Risk to voice:** none.
- **Leave as-is if:** the pronoun chain is read as obviously resuming the paragraph's
  subject.

**LE-26 · `ch7:185` and `ch7:529` · an identical sentence twice**  *(carry-forward, CH7 L3; confirmed by `dupes.py`)*
> Care without impact is attendance: warm, dependable, and doing nothing.

- **Diagnosis:** the only exactly-repeated sentence in ch2–ch9. In July the pair
  differed by one word (*dependable* / *reliable*); the edit since made them identical,
  which converts a near-repeat into a verbatim one 344 lines apart. The second sits in
  the Victim section as recall, where a pointer would do.
- **Minimal edit:** at `ch7:529`, "You know both failure states: attendance on one
  side, the Challenger's altitude imported on the other."
- **Reader problem solved:** the recall reads as recall instead of as a paragraph the
  reader has already read.
- **Risk to voice:** low; the memorable line keeps its one home at `ch7:185`.
- **Leave as-is if:** the verbatim return is the intended drumbeat, in which case it
  should be exact on purpose and probably marked as a return.

### Chapter 8 — 6 flags

**LE-27 · `ch8:71` · elliptical clause on the chapter's guardrail**  *(carry-forward, CH8 LN-1)*
> Inner work keeps the response clean enough to still work tomorrow. It looks like delay from outside, and from inside on a bad day.

- **Diagnosis:** the second clause drops its verb, so the guardrail — the one paragraph
  telling a reader when *not* to use this chapter — ends on a construction she has to
  rebuild.
- **Minimal edit:** "It looks like delay from outside, and on a bad day it looks like
  delay from inside too."
- **Reader problem solved:** the limit case closes on a complete sentence.
- **Risk to voice:** low; the compression is stylish but this is the wrong paragraph
  for it.
- **Leave as-is if:** the clipped tail is the Sage's register and the meaning survives
  a read-aloud.

**LE-28 · `ch8:174` · two *it*s, two referents**  *(carry-forward, CH8 LN-2)*
> The Sage who could name that dynamic chooses instead to hold space for it. To validate. To see. Holding space participates in it.

- **Diagnosis:** the first *it* is the dynamic; the second is the competition itself.
  The three fragments between them make the second bind harder, and the sentence is the
  section's indictment.
- **Minimal edit:** "Holding space participates in **the competition**."
- **Reader problem solved:** the charge names what the Sage is participating in.
- **Risk to voice:** none.
- **Leave as-is if:** the two *it*s are the same thing on a reading I have not found.

**LE-29 · `ch8:224` · "None of this" reaching across a first-person aside**  *(carry-forward, CH8 LN-3)*
> None of this describes the guru on the mountain who has risen above it all.

- **Diagnosis:** the six lines before it are the Head's in-world aside (*I am the
  oldest first-year at this school*), so *this* has to reach past a voice change to the
  material before it.
- **Minimal edit:** "**The Sage described here is not** the guru on the mountain who has
  risen above it all."
- **Reader problem solved:** the definition's most important negation stops depending
  on what the reader did with the digression.
- **Risk to voice:** low.
- **Leave as-is if:** the aside is meant to be part of *this*, which would make the
  pointer correct and the reading unusual.

**LE-30 · `ch8:511` · demonstrative plus an unattached frequency**  *(carry-forward, CH8 LN-4)*
> Something about how you process runs off-standard. That happens frequently, and at this altitude almost always, because panoramic vision is not the common configuration.

- **Diagnosis:** *That happens frequently* reads as a claim about an event rather than
  about a proportion of people, which is what it means.
- **Minimal edit:** "Something about how you process runs off-standard. **It does for a
  lot of people**, and at this altitude almost always, because panoramic vision is not
  the common configuration."
- **Reader problem solved:** the reassurance actually reassures.
- **Risk to voice:** none.
- **Leave as-is if:** the frequency claim is about occasions rather than people.

**LE-31 · `ch8:527` · a conjunction joining two incompatible predicates**  *(carry-forward, CH8 LN-5)*
> *Keep the reading. Something in me runs differently, and that is usually accurate and sometimes the whole instrument.*

- **Diagnosis:** the first *and* joins a claim about accuracy to a claim about
  identity; the second is not a completion of the first. This is the line the reader is
  asked to say to the daemon, so it has to hold on a spoken read.
- **Minimal edit:** "…and **that reading is usually accurate, and sometimes it is the
  whole instrument.**"
- **Reader problem solved:** the address is sayable.
- **Risk to voice:** low.
- **Leave as-is if:** the compression is the point and the line is meant to be said
  fast.

**LE-32 · `ch8:531` · a pivot with no transition**  *(carry-forward, CH8 LN-6)*
> They leave with reading. On the narrow jurisdiction, the same part returns the same accurate report and the answer changes.

- **Diagnosis:** *the narrow jurisdiction* is set more than twenty lines earlier and
  arrives here as a bare adverbial, at the chapter's key reversal.
- **Minimal edit:** "**Give that same part its narrow jurisdiction and** it returns the
  same accurate report — but the answer changes."
- **Reader problem solved:** the reversal is legible where it happens.
- **Risk to voice:** low.
- **Leave as-is if:** the term is fresh enough by this point to carry a bare pointer.

### Chapter 9 — 1 flag

**LE-33 · `ch9:157` · "in this mode" with no referent**  *(carry-forward, CH9 L5)*
> I built a method. Right now I'm essentially the only one running it in this mode. That's true today.

- **Diagnosis:** *this mode* names nothing on the page, and *mode* is a loaded word in
  ch9 — the chapter runs five of them (Review, Discern, Design, Build, Pass On), none
  of which is what this sentence means.
- **Minimal edit:** "Right now I'm essentially the only one **teaching it this way**."
- **Reader problem solved:** the chapter's most personal claim stops colliding with its
  own vocabulary.
- **Risk to voice:** none.
- **Leave as-is if:** *mode* is meant in the chapter's sense, which would be a
  continuity finding rather than a line one.

---

## 5 · Checked and clean — recorded so it is not re-run

- **`repeat`, 63 hits, ~5 real.** Most are the book's conventions and should stay:
  *two minutes to capture it as a BAR* (the standing practice close, ch2/ch4/ch5/ch6),
  the `**The structure of the X:**` template (five ch7 sections), the Move recaps in
  ch4–ch8, ch7's `Here is what its absence looks like` / `its distortion looks like`
  channel template, and ch9:284/676's WAVE roll-call. Precision on this rule is low by
  construction; its value is that it makes an accident findable at all.
- **`ch2:111` / `ch2:368`, "and just hums".** July flagged the pair. Keeping it: 368
  explains the symptom 111 introduced, in the same chapter, about the same daemon. A
  callback that names its own antecedent is doing work.
- **`ch9:51` / `ch9:618`, "any game the village needs played, whatever the moment
  requires".** A bookend — the chapter's opening diagnosis and its closing recap. The
  triple *The Player shows that…* at 618 is anaphora, not accident.
- **`orphan-ref`, 6 hits, 2 real.** `ch1:4` (*This book is three years late*) and
  `ch1:199` (*This is your character sheet*) are chapter and section openers where the
  demonstrative points forward. The rule cannot tell forward from backward reference;
  the two real ones are LE-3 and LE-29.
- **`banned-kin`, 10 hits, 0 flags.** Every one is *genuine* or *Genuine*. The canon
  bans *genuinely*; four of the ten are the ruled EA alchemy name **Genuine Inclusion**
  (`ch7:109`, `ch7:351`), which is canon, and the rest are ordinary adjectival use. Not
  a defect — logged as a question for Wendell in §7.
- **`ch9:366`, "The iteration is the walk."** July CH9 L4 called this a sentence that
  closes on itself. The second half has been rewritten since (*another stretch of the
  same road*), which fixes the circularity. No flag.
- **`prose_diet` passive: ch7 1.49, ch5 1.35.** Both over 1.30 and both already ruled
  in the 2026-08-01 passive pass (four sites with a hidden doer fixed; the rest named
  as register). Not re-opened here.

## 6 · What this pass did not do

- **It did not read the book aloud.** The OS is explicit that a human read-aloud pass
  and real readers come after AI line work, and neither is in this report.
- **It is not a full human line read of 106,614 words.** Coverage is: a mechanical
  sweep of all nine chapters on six rules, plus reader adjudication at every site those
  rules hit, plus every LINE-band and BLOCKED-band finding carried over from
  2026-07-31. A defect that no rule reaches and no earlier reader caught is not in here.
- **It did not touch structural or continuity findings.** One job at a time. Where a
  line flag is really a structural question it says so and stops (LE-23's second half,
  LE-33's alternative reading).
- **Ship window.** Today is delivery day and DL-20 is blocker one. **Nothing in this
  report is a print blocker**, and none of it should compete with the app removal for
  attention. `ch1:269`'s `[ URL / QR ]` remains the only print blocker on the line
  surface and it is P0, not a Pass 3 finding.

## 7 · Rulings needed

1. **Which flags become work.** Only items in `specs/DECISION_LOG.md` become editing
   work. Filed as **DL-22** with the 33 flags attached; Wendell picks.
2. **`genuine`.** The canon bans *genuinely*. Ten sites use *genuine*, four of them the
   ruled alchemy name. Ban, allow, or allow-except-adjectival.
3. **`ch5:520` `remit` and `ch5:272` `goes on record`.** Both are Sera's register.
   Ruling wanted on whether the Regent's formality outranks plain readability in an
   address the reader is asked to say out loud.
4. **`ch2:370`'s `I`.** DL-4 and DL-19 imply second person. Confirm, or frame it as
   testimony.

*Instruments: `instruments/line_scan.py` (new), `instruments/rescan.py` (corrected).
Nothing in `manuscript/` was modified on this branch.*
