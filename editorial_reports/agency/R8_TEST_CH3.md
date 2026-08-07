# R8 stress test — Chapter 3

## Verdict

**Break rate: 2 clean BREAKS of 23 village-subject sites found (8.7%), plus 1 SHOULD-NOT-CHANGE
keep-candidate (13% combined).** 20 of 23 sites (87%) either HOLD outright or HOLD WITH TOUCH — a
pronoun (`it→they`), a possessive apostrophe (`village's→villagers'`), or a present-tense verb
agreement fix (`trains→train`, `manages→manage`). Past-tense verbs, which dominate this chapter's
village clauses, need no touch at all — English doesn't inflect the past tense for number, so most
of the ledger's existing R1 rewrites turn out to have been solving a problem the grammar didn't
actually have.

R8 is safe to adopt for Chapter 3, with two named exceptions and one flagged judgment call. Both
exceptions are instructive: line 316 is the exact "trains everyone" shape GAP_VOICE_ANCHOR already
predicted (villagers cannot train everyone, because they are everyone — a group acting on a set
coextensive with itself). Line 152 is a new, subtler failure mode the GAP doc did not anticipate: a
**semantic break that is not grammatically nonsense**. "The village never saw itself doing this"
encodes emergent, systemic blindness — the whole point is that no *individual* vantage could see
the aggregate pattern. "The villagers never saw themselves doing this" is perfectly grammatical and
quietly asserts a different, weaker claim (many individuals each missed their own participation).
R8's own worked examples only warn about nonsense; they don't warn about this. Any adoption of R8
needs a check for reflexive pronouns (`itself`, `by itself`) on the village subject, not just for
possessives (`its`) — reflexives are the same failure shape wearing different grammar.

The bigger finding is upstream of R8's success rate: **the ledger significantly undercounted village
sites.** It logged 14 lines; the chapter actually carries at least 23 — a 39% miss rate — including
a fourth Section 3 "callback echo" (line 161) the ledger's own summary said didn't exist ("three
faint callback echoes," when there are at least four, plus several standalone village-subject
clauses inside the Section 2 run that the ledger's excerpts quoted as context but never rowed
individually, e.g. "trusted," "had to act," "never thought to look," "did... on purpose," "solved…
moved… changed," "shrinks," "lost"). None of the missed sites turn out to be additional breaks —
all 9 new sites HOLD or HOLD WITH TOUCH — but a stress test that only checks the sites someone
already flagged isn't testing the rule, it's testing the ledger. Applying R8 mechanically across the
chapter (find "village," check number, check for possession/reflexivity) surfaces sites human
adjudication missed twice in a row.

One more finding worth flagging on its own: at three sites (134, 138, 142) the ledger's *existing*
R1 proposals quietly drop the paragraph's closing beat — "The village became brittle. Reactive.
Defended," "unable to actually grieve what it had lost," the whole appearing/becoming fragment run
— while R8's plural swap preserves all three unchanged. Where the two ops are both viable, R8 is not
just cheaper, it is measurably safer for the voice anchor's own "closing move is the register" test.

---

## Sites

### line 79 — HOLDS WITH TOUCH
**Current:** > The village trusted this once. It built rituals around it. Coming-of-age ceremonies that made space for sadness. Councils that opened with a moment to feel the ground underneath.
**R8:** > The villagers trusted this once. They built rituals around it. Coming-of-age ceremonies that made space for sadness. Councils that opened with a moment to feel the ground underneath.
**Turn:** "your body knows before your mind catches up. Listen to it." → unchanged, outside the touched span.
**Rhythm:** village (2) → villagers (3), +1 syllable; "It" (1) → "They" (1), no change.
**Humor:** n/a.
**Note:** Ledger's row for this line only tagged "built" (causal-bare, parked, low severity); "trusted" — a belief/attitude verb, same family as the flagged "needed" (line 89) — was never itemized as its own verb. R8 handles both cleanly with one touch (the pronoun).

### line 87 — HOLDS
**Current:** > There was a problem. The village had to act. *Now.*
**R8:** > There was a problem. The villagers had to act. *Now.*
**Turn:** the one-word fragment "*Now.*" → unchanged; lands the same.
**Rhythm:** village (2) → villagers (3), +1 syllable. Negligible against a three-sentence, three-beat run.
**Humor:** n/a.
**Note:** Not in the ledger at all. Clean plural, no touch needed (no pronoun or present-tense verb to fix).

### line 89 — HOLDS
**Current:** > At first, this seemed right. There were problems that needed solving. The village needed someone who could draw a line in the sand. Someone who could say "this is unacceptable" without softening it.
**R8:** > At first, this seemed right. There were problems that needed solving. The villagers needed someone who could draw a line in the sand. Someone who could say "this is unacceptable" without softening it.
**Turn:** "Someone who could move while others still gathered information" → unchanged.
**Rhythm:** village (2) → villagers (3), +1 syllable.
**Humor:** n/a.
**Note:** Ledger ruled R1 here and rewrote to "People wanted someone who could draw a line in the sand" — which drops "needed" for "wanted" and loses the parallel with "problems that needed solving" one clause earlier. R8's plain swap keeps that echo intact and is a smaller edit. Point in favor of R8 over the existing ledger proposal.

### line 91 — HOLDS
**Current:** > It worked. The cost landed somewhere the village never thought to look.
**R8:** > It worked. The cost landed somewhere the villagers never thought to look.
**Turn:** "somewhere the village never thought to look" *is* the turn — the whole sentence's point is the blind spot. Survives: "somewhere the villagers never thought to look" lands the same way.
**Rhythm:** village (2) → villagers (3), +1 syllable, on the last beat of the sentence — the one place a syllable landing badly would hurt most. It doesn't; the stress pattern absorbs it fine.
**Humor:** n/a.
**Note:** Not in the ledger. "Thought" is squarely a cognition verb, the same class as the flagged "learned"/"saw"/"forgot" elsewhere in this chapter — this is a clean miss, not a borderline call.

### line 115 — HOLDS
**Current:** > When the village started following the Challenger's lead, valuing speed over discernment, action over feeling, certainty over the wisdom that comes from sitting with complexity, the Shaman became less necessary.
**R8:** > When the villagers started following the Challenger's lead, valuing speed over discernment, action over feeling, certainty over the wisdom that comes from sitting with complexity, the Shaman became less necessary.
**Turn:** "the Shaman became less necessary. Even confusing." → unchanged.
**Rhythm:** village (2) → villagers (3), +1 syllable, buried in a long subordinate clause; unnoticeable.
**Humor:** n/a.
**Note:** Not in the ledger. Low severity, same causal-bare register as the lines the ledger did flag and park (79/146).

### line 123 — SHOULD NOT CHANGE
**Current:** > The village never meant for that to happen. It never said "go." It just stopped listening. Which, it turns out, amounts to exile.
**R8:** > The villagers never meant for that to happen. They never said "go." They just stopped listening. Which, it turns out, amounts to exile.
**Turn:** "Which, it turns out, amounts to exile" → survives verbatim; grammatically this site HOLDS WITH TOUCH (it→they, twice).
**Rhythm:** village (2) → villagers (3), +1 syllable.
**Humor:** n/a.
**Note:** Flagging this as a keep-candidate independent of the ledger's own R1-era keep-candidate ruling, because the *reason* is R8-specific and different. "The village never meant" describes emergent, no-one-decided drift — the whole passage's argument is that exile happened without any single mind intending it, which is why the very next clause redescribes it behaviorally ("it just stopped listening") instead of psychologically. "The villagers never meant" reads as many individual people, each not intending it — which is still true, but it nudges the sentence from "this was a structural non-decision" toward "these particular people didn't mean to," a subtly different and more individually-exculpatory claim. Not nonsense, not clearly wrong, but the kind of change that should go to Wendell rather than be waved through on a suffix rule. I am not ruling this a keep; I am saying what would be lost if it changed without a look.

### line 130 — HOLDS WITH TOUCH
**Current:** > Here's what happened after the Shaman left: the village didn't stop feeling. It just stopped *knowing what to do with feelings.*
**R8:** > Here's what happened after the Shaman left: the villagers didn't stop feeling. They just stopped *knowing what to do with feelings.*
**Turn:** "It just stopped *knowing what to do with feelings*" → "They just stopped *knowing what to do with feelings*" — the italicized punch phrase is untouched, turn survives.
**Rhythm:** village (2) → villagers (3), +1 syllable; It (1) → They (1), no change.
**Humor:** n/a.
**Note:** Not in the ledger at all, despite governing "feeling" and "knowing" — both squarely cognition/perception verbs, the exact category the registry targets, and this is the header sentence that sets up the four-paragraph fear/anger/sadness/joy run the ledger did catch. A genuinely surprising miss given how central this sentence is structurally.

### line 134 — HOLDS
**Current:** > The village still experienced fear. […] The village learned to not-feel the fear, which meant the village also missed the intelligence fear kept trying to deliver. The village became brittle. Reactive. Defended.
**R8:** > The villagers still experienced fear. […] The villagers learned to not-feel the fear, which meant the villagers also missed the intelligence fear kept trying to deliver. The villagers became brittle. Reactive. Defended.
**Turn:** "The village became brittle. Reactive. Defended." → "The villagers became brittle. Reactive. Defended." — the three-fragment landing survives completely.
**Rhythm:** village (2) → villagers (3) at each of 4 instances, +1 syllable each, +4 total across the paragraph. The fragment cadence ("brittle. Reactive. Defended.") is untouched since none of those three words change.
**Humor:** n/a.
**Note:** The ledger's own R1 proposal for this site — "Parents taught their children not to feel the fear, and so their children missed the intelligence fear kept trying to deliver" — silently drops "The village became brittle. Reactive. Defended" entirely. R8 keeps it. Repeating "the villagers" four times in one paragraph is mildly clunky; a light touch (swap instances 2–3 for a pronoun) would help but nothing breaks without it. Called HOLDS rather than HOLDS WITH TOUCH because no touch is grammatically required — the repetition is a taste question, not a defect.

### line 136 — HOLDS WITH TOUCH
**Current:** > The village learned to redirect anger *outward* at the systems, the bad people, the ones who weren't as woke. It forgot that anger could also point inward, showing you where your own boundaries got crossed, what you actually cared about beneath the performance.
**R8:** > The villagers learned to redirect anger *outward* at the systems, the bad people, the ones who weren't as woke. They forgot that anger could also point inward, showing you where your own boundaries got crossed, what you actually cared about beneath the performance.
**Turn:** "what you actually cared about beneath the performance" → unchanged.
**Rhythm:** village (2) → villagers (3), +1; It (1) → They (1), no change.
**Humor:** n/a.
**Note:** Ledger's R1 proposal merges the two sentences into one with "and" and keeps the full closing clause, so no loss there — this one was already handled comparably well by R1. R8 is simply the cheaper edit.

### line 138 — HOLDS WITH TOUCH
**Current:** > The village learned to skip over sadness, to move quickly past it into "lessons learned" and action items. It forgot how to let sadness teach. So it kept hitting the same losses over and over, unable to actually grieve what it had lost.
**R8:** > The villagers learned to skip over sadness, to move quickly past it into "lessons learned" and action items. They forgot how to let sadness teach. So they kept hitting the same losses over and over, unable to actually grieve what they had lost.
**Turn:** "unable to actually grieve what it had lost" → "unable to actually grieve what they had lost" — turn survives, and this is the strongest closing beat in the paragraph.
**Rhythm:** village (2) → villagers (3), +1; three instances of "it" → "they," no syllable change.
**Humor:** n/a.
**Note:** The ledger's R1 proposal for this site drops the entire "So it kept hitting the same losses over and over, unable to actually grieve what it had lost" sentence — the paragraph's real turn — and closes instead on "nobody remembered how to let sadness teach," a flatter, earlier beat. R8 preserves the stronger original ending untouched. This is the clearest case in the chapter where R8 beats the existing R1 proposal on the voice anchor's own test.

### line 140 — HOLDS
**Current:** > the village learned to celebrate *doing the work* instead of celebrating *becoming the kind of person who can do the work sustainably.* So joy became tied to output. To productivity. The village forgot that joy was also information, a signal that something true was happening, something aligned.
**R8:** > the villagers learned to celebrate *doing the work* instead of celebrating *becoming the kind of person who can do the work sustainably.* So joy became tied to output. To productivity. The villagers forgot that joy was also information, a signal that something true was happening, something aligned.
**Turn:** "a signal that something true was happening, something aligned" → unchanged.
**Rhythm:** village (2) → villagers (3) at each of 2 instances, +1 syllable each.
**Humor:** n/a.
**Note:** Clean swap, no pronoun issues in this one (no "it" governing village).

### line 142 — HOLDS
**Current:** > Without the Shaman, the village became very busy managing emotions instead of listening to them. Very skilled at pushing through discomfort, very poor at learning from it. Very good at *appearing* evolved, very bad at *actually becoming* evolved.
**R8:** > Without the Shaman, the villagers became very busy managing emotions instead of listening to them. Very skilled at pushing through discomfort, very poor at learning from it. Very good at *appearing* evolved, very bad at *actually becoming* evolved.
**Turn:** "very bad at *actually becoming* evolved" → unchanged; this parallel-fragment run is the closing turn of the whole four-emotion sequence and it lands identically.
**Rhythm:** village (2) → villagers (3), +1 syllable, in the lead-in clause only; the fragment run itself (the part carrying the rhythm) is entirely untouched.
**Humor:** mild irony present ("appearing evolved" vs "actually becoming evolved") — mocks a practice (performative growth-signaling), not a person. Untouched by the swap since the target of the joke was never "the village" grammatically, it's the appearing/becoming contrast. Humor survives.
**Note:** Ledger's R1 proposal here invents new content ("Nobody around them ever asked what it was trying to teach") to bridge the elliptical fragment run — a real addition to the text, not present in the original. R8 needs no addition at all and preserves the delicate list rhythm exactly. Clear win for R8.

### line 144 — HOLDS
**Current:** > The village did all of this on purpose. Because the Challenger was right: *something had to be done.*
**R8:** > The villagers did all of this on purpose. Because the Challenger was right: *something had to be done.*
**Turn:** "*something had to be done*" → unchanged (italicized callback to the Challenger's earlier line).
**Rhythm:** village (2) → villagers (3), +1 syllable.
**Humor:** n/a.
**Note:** Not in the ledger. "Did… on purpose" is an explicit intention ascription to the collective — arguably should have been Tier 3 in its own right, same class as "needed" (89) and "meant" (123), and the ledger missed it entirely. R8 handles it without incident: distributed deliberate action across many people reads naturally.

### line 146 — HOLDS
**Current:** > So the village made a choice: efficiency over wisdom. Output over presence. Action over discernment.
**R8:** > So the villagers made a choice: efficiency over wisdom. Output over presence. Action over discernment.
**Turn:** the three two-word fragments → unchanged, and they're the whole point of the sentence.
**Rhythm:** village (2) → villagers (3), +1 syllable.
**Humor:** n/a.
**Note:** "Made a choice" (singular "a choice" for a plural subject) is idiomatic English for a shared/joint decision ("the committee made a choice," "the jury reached a verdict") — no touch needed despite the number mismatch between subject and object.

### line 148 — HOLDS WITH TOUCH
**Current:** > It *worked.* The village solved some problems. It moved some mountains. It changed some systems, temporarily, in specific places. All while running on fumes. All while the people doing the work got more and more depleted, more and more cut off from the very source of energy that would have sustained them.
**R8:** > It *worked.* The villagers solved some problems. They moved some mountains. They changed some systems, temporarily, in specific places. All while running on fumes. All while the people doing the work got more and more depleted, more and more cut off from the very source of energy that would have sustained them.
**Turn:** "more and more cut off from the very source of energy that would have sustained them" → unchanged.
**Rhythm:** village (2) → villagers (3), +1; two instances of "It" → "They," no change.
**Humor:** the "moved some mountains" idiom carries mild irony (undercut by "running on fumes" two clauses later) — target is the practice/pattern, not persons. Survives.
**Note:** Not in the ledger — this is three additional causal-bare verbs (solved, moved, changed) the ledger's Tier-2 causal-bare cluster never counted (it logged only lines 79 and 146). Worth a flag: once "the village" becomes "the villagers" here, the sentence two clauses later — "the people doing the work got more and more depleted" — reads as a second, seemingly distinct group, when it's clearly meant to be the same population under a different description. Mild redundancy, not a break, but the kind of thing a copyedit pass should catch once R8 is applied mechanically at scale.

### line 150 — HOLDS WITH TOUCH
**Current:** > This is what the village does with emotional alchemy when the Shaman is gone: it transforms it into *performance management.* Into *emotional labor that must be optimized.*
**R8:** > This is what the villagers do with emotional alchemy when the Shaman is gone: they transform it into *performance management.* Into *emotional labor that must be optimized.*
**Turn:** the closing list ("Where fear answers to imposter syndrome and takes a mindfulness app. Where anger gets channeled into 'righteous action' but never, ever examined…") → unchanged; those clauses take "fear," "sadness," "anger" as their own subjects, not "the village," so R8 never touches them.
**Rhythm:** village (2) → villagers (3), +1; "does" (1) → "do" (1), no change; "it transforms" (3) → "they transform" (3, "trans-form" 2 + "they" 1), no net change.
**Humor:** satire aimed squarely at institutional wellness-culture practices (imposter syndrome, mindfulness apps, "righteous action"), never at persons — untouched by the swap since none of the joke's subordinate clauses take "the village" as their grammatical subject. Humor survives.
**Note:** Not in the ledger. Requires two touches (present-tense verb agreement, and the pronoun on the first "it" only — the second "it" refers to "emotional alchemy," not the village, and stays as-is).

### line 152 — BREAKS
**Current:** > The village never saw itself doing this. It called the pattern efficiency, and the pattern starved it.
**R8:** > The villagers never saw themselves doing this. They called the pattern efficiency, and the pattern starved them.
**Turn:** "and the pattern starved it" → "and the pattern starved them" — this half survives fine on its own.
**Rhythm:** village (2) → villagers (3), +1; itself (2) → themselves (3), +1; it (1) → them (1), no change.
**Humor:** n/a.
**Note:** **This is a genuine break, and not the shape R8's own worked examples warn about.** The reflexive "saw itself" is doing real conceptual work: it's asserting that *no vantage point inside the system* could see the aggregate pattern — that's precisely why it's a systemic failure rather than a series of individual failures. "The villagers never saw themselves doing this" is fully grammatical and asserts something different and weaker: that each villager, individually, missed their own participation. That's a plausible claim but not the same claim, and it quietly undercuts the sentence's actual argument (systemic blindness, not many instances of personal blindness). This is not nonsense — it reads fine on the page — which is exactly what makes it dangerous: a mechanical R8 pass would wave it through. R8's stated failure mode (possession → group acting on itself) doesn't cover this; **reflexive pronouns on the village subject need the same scrutiny as possessives.** The ledger's own R1 proposal for this line — "No one who did it saw it happening" — actually gets the systemic-blindness claim right, better than R8 does. This site needs R1, not R8.

### line 161 — HOLDS WITH TOUCH
**Current:** > The village shrinks alchemy into processing: *identify* the emotion, *understand* where it came from, *release* it, and then *move on.*
**R8:** > The villagers shrink alchemy into processing: *identify* the emotion, *understand* where it came from, *release* it, and then *move on.*
**Turn:** the four-verb imperative list ("identify… understand… release… move on") → unchanged; it's the whole point of the sentence and none of those verbs take "village" as their subject.
**Rhythm:** village (2) → villagers (3), +1; shrinks (1) → shrink (1), no change.
**Humor:** dry, not quite a joke — the clipped four-verb inventory mocks a process (corporate emotional processing), not a person. Survives.
**Note:** **Not in the ledger, and not counted among the ledger's "three faint callback echoes" (359, 572, 564) either** — this is a fourth Section 3 recurrence of the village construction that the chapter's own summary claimed didn't exist beyond three instances. It sits two sentences after the Maera Voss signature block, opening the new section, which may be why it read as "new material" rather than a callback on a first pass. It is textually the same device.

### line 213 — HOLDS
**Current:** > That is the Shaman's superpower. That is what the village lost when the Shaman left.
**R8:** > That is the Shaman's superpower. That is what the villagers lost when the Shaman left.
**Turn:** "when the Shaman left" → unchanged; this is the closing line of Section 3's frame-setting and lands the same.
**Rhythm:** village (2) → villagers (3), +1 syllable.
**Humor:** n/a.
**Note:** Not in the ledger. "Lost" is the same cognitive/possessive-loss verb class as the flagged "forgot" (line 572) — a near-parallel construction 359 lines apart, one caught, one missed.

### line 316 — BREAKS
**Current:** > The village trains everyone to turn feeling down. It hands you a dial in childhood and teaches one direction: lower it.
**R8 (naive):** > The villagers train everyone to turn feeling down. They hand you a dial in childhood and teach one direction: lower it.
**Turn:** "and teaches one direction: lower it" → survives verbatim, but the sentence in front of it doesn't.
**Rhythm:** village (2) → villagers (3), +1; trains (1) → train (1), no change.
**Humor:** n/a.
**Note:** **Confirms GAP_VOICE_ANCHOR's own flagged hard case exactly.** "The villagers train everyone" is nonsense on inspection: the villagers cannot train everyone, because in this fable they *are* everyone — subject and object are the same set. This is the coextensive-population failure shape, a variant of the "group acting on itself" problem the GAP doc names (there it's possession — "it taught its people" — here it's identity: subject population = object population). Naive R8 does not carry this site.
**Proposed instead (compression, matching GAP's own fix):** > The villagers hand you a dial in childhood and teach one direction: lower it.
Dropping the abstract first sentence and keeping the concrete second one preserves the turn intact, shortens the paragraph, and removes the coextensive-set problem entirely, since "hand you a dial" and "teach one direction" both plausibly describe specific adults (parents, teachers) acting on children, not villagers acting on villagers-in-general. This needs compression, not a straight R8 swap.

### line 359 — HOLDS WITH TOUCH
**Current:** > This is the first difference between the Shaman's practice and the village's distortion: the village tries to speed past this stage. The Shaman lingers here long enough to actually get the teaching.
**R8:** > This is the first difference between the Shaman's practice and the villagers' distortion: the villagers try to speed past this stage. The Shaman lingers here long enough to actually get the teaching.
**Turn:** "The Shaman lingers here long enough to actually get the teaching" → unchanged; the Shaman/village contrast (singular vs. now-plural) actually sharpens the antithesis rather than weakening it.
**Rhythm:** village's (3) → villagers' (4), +1; village (2) → villagers (3), +1; tries (1) → try (1), no change.
**Humor:** n/a.
**Note:** Two touches required: the possessive apostrophe moves (village's → villagers'), and the present-tense verb needs agreement (tries → try). Both mechanical, neither risky.

### line 564 — HOLDS WITH TOUCH
**Current:** > Without the Shaman, the village manages emotions instead of learning from them. The WAVE-Spiral is how you learn instead of manage.
**R8:** > Without the Shaman, the villagers manage emotions instead of learning from them. The WAVE-Spiral is how you learn instead of manage.
**Turn:** "The WAVE-Spiral is how you learn instead of manage" → unchanged, and the manage/learn echo between the two sentences survives.
**Rhythm:** village (2) → villagers (3), +1; manages (3) → manage (2), -1. Net rhythm change across the span: zero.
**Humor:** n/a.
**Note:** **This is the site where R8 outperforms the ledger's own ruling.** The ledger routed this to R6 (dissolve to transmission → "performance reviews reward managing emotions over learning from them"), reasoning that naming a specific human actor would be false precision. But R8 doesn't name a specific actor — it names the population, distributively — so the false-precision objection that blocked R1 here never applies to R8. "The villagers manage emotions instead of learning from them" is a true, licensed, Grade-1 claim about a population's aggregate habit, no institution-naming required. Worth flagging to whoever adjudicates R6-routed village sites: check whether R8 was tried first.

### line 572 — HOLDS
**Current:** > The village took a thousand years to forget this. The Shaman's practice is how you remember, in five stages, as many times as you need, until it becomes who you are.
**R8:** > The villagers took a thousand years to forget this. The Shaman's practice is how you remember, in five stages, as many times as you need, until it becomes who you are.
**Turn:** "until it becomes who you are" → unchanged.
**Rhythm:** village (2) → villagers (3), +1 syllable.
**Humor:** n/a.
**Note:** The ledger's own R1 proposal for this line — "It took a thousand years of nobody saying it out loud for the village to forget this" — is longer, adds an invented cause ("nobody saying it out loud"), and, oddly, still leaves "the village" in the sentence as the grammatical subject of the infinitive "to forget." It doesn't actually clear the Grade-6 subject it set out to fix. R8's plain swap is shorter, truer to the original, and actually resolves the agency question the R1 rewrite didn't.

---

## Where R8 breaks

Two shapes, one predicted by the proposal and one it missed:

1. **Coextensive population (predicted).** Line 316: "the village trains everyone" — subject and object are the same set, so pluralizing produces "the villagers train everyone," which is the villagers training themselves. This is the possession-failure shape from the GAP doc (ch4:127, "it taught its people") wearing an identity relation instead of a possessive one. Needs compression or a real rewrite naming the actual transmitting adults, not R8.

2. **Reflexive self-perception (not predicted — new finding).** Line 152: "the village never saw itself doing this." Grammatically, "the villagers never saw themselves doing this" is fine — that's what makes it dangerous. It quietly swaps a claim about *systemic, no-vantage-point blindness* for a claim about *many individual instances of personal blindness*. R8's own documentation only names nonsense (a group acting on itself) as the failure condition; it does not name meaning-drift through a reflexive pronoun as a risk. Any team adopting R8 at scale should add "check for reflexives (itself, by itself, on its own)" to the pre-flight, not just "check for possessives (its)."

Both failures share a root: they occur where "the village" is being used to make a claim about the *shape of the collective as a whole* (a trained-in norm everyone shares; a blind spot no one inside the system could see) rather than as shorthand for *the people in it, considered severally*. R8 works precisely when "the village" is doing the second job. It is the wrong tool the moment it's doing the first.

## Sites the previous ledger missed

Nine village-subject constructions not rowed in `LEDGER_CH3.md`, none of them a break under R8:

| line | construction | R8 result |
|---:|---|---|
| 87 | "The village had to act." | HOLDS |
| 91 | "the cost landed somewhere the village never thought to look" | HOLDS |
| 115 | "the village started following the Challenger's lead, valuing…" | HOLDS |
| 130 | "the village didn't stop feeling. It just stopped knowing…" | HOLDS WITH TOUCH |
| 144 | "The village did all of this on purpose." | HOLDS |
| 148 | "The village solved some problems. It moved some mountains. It changed some systems…" | HOLDS WITH TOUCH |
| 150 | "This is what the village does… it transforms it into performance management." | HOLDS WITH TOUCH |
| 161 | "The village shrinks alchemy into processing…" | HOLDS WITH TOUCH |
| 213 | "That is what the village lost when the Shaman left." | HOLDS |

Additionally, line 79's existing ledger row tagged only "built" (causal-bare); it missed "trusted" as a
second, distinct verb on the same subject in the same sentence, from the same cognitive/intention
family as the flagged "needed" (89) and "meant" (123).

Line 161 is the most structurally significant miss: the ledger's own summary states the village
construction appears "almost entirely confined to those two sections [1–2]... with three faint
callback echoes later in the chapter," naming 359, 572, and 564. Line 161, in Section 3, is a fourth
callback the summary's own count excludes. The chapter's self-diagnosis undercounted its own
recurring device by 25%.
