# Agency Ledger — Chapter 3: The Shaman

Scope per SPEC_AGENCY_TRACEABILITY_AUDIT_20260802 / `instruments/agency_registry.yaml`. MARGINALIA, EPIGRAPH-BYLINE, and POSTCARD blocks stripped and out of scope this pass — not read for findings. HANDBOOK and SIGNATURE blocks are in scope, tagged `HANDBOOK-REGISTER`. Line numbers are against `manuscript/ch3.md` as it stands on disk (not the recall net's stripped-body numbering, which shifts once marginalia is removed).

## Summary

**Sites examined:** the full 16,428-word body was read directly (not sampled), with the recall net (`instruments/agency_grep.py`) run as a coverage check. ~45 candidate constructions were adjudicated by hand: every "village" clause with a cognition or social verb, every channel-subject clause across Sections 3–4, every chapter/book self-reference, every "game" subject, and the Controller/referee material in Section 5.

**Flagged, by tier:**
- Tier 3: **12** sites — all Grade 6 (`the village`), all perception, intention, or social-causal verbs.
- Tier 2: **2** sites — one Grade 6 speech cluster (`the council`), one Grade 6 causal-bare cluster (`the village built… made…`).
- Tier 1: none logged as individual rows (a few dead-metaphor directional/mechanical hits on Grade 0 subjects were noted and cleared, not rowed, per the "do not agonize" instruction).

**R-op distribution** (14 findings total; 2 keep-candidates, 1 parked, 11 fix):
- R1 (Restore human agent): **10** — all on the Grade 6 "village" cluster. This exceeds the >4 guard, so all ten are built on different grammatical strategies (simple subject swap, named-role + cause-effect, sentence-coordination merge, named-role + impersonal negative, named-role + passive idiom, fragment-rhythm preservation, indefinite-negative + pronoun continuation, compound named roles, indefinite collective modifier, cleft construction demoting "village" to an object). Detail is in each site's Op note; the variation list is repeated in full below the site table.
- R6 (Dissolve to transmission): **1** — the one village site where naming a specific human actor would have been false precision (institutional reward structures, not people, are the actual transmission path).
- R2, R3, R4, R5: **0** each.
- Keep-candidate (no op ruled): **2** — one negated village clause that already performs the demotion the registry wants; one Grade 6 speech cluster (`the council`) that is the parable's own deliberate dramatization of institutional language hiding an individual's avoidance — direct W-4 evidence, not a defect.
- Parked: **1** — a two-instance causal-bare cluster on `the village`, low severity, left for the author's pass rather than rewritten.

**R3-per-daemon counts:** **0 routings** to any daemon this chapter. The Controller/referee/judge material in Section 5 is extensive but is already-licensed Grade 2 daemon activity (its verbs — rules, judges, convenes, holds court — sit inside the Controller's canonical job as standard-setter, and the mechanism is the entire section), not abstraction routed to a part via R3. No daemon is over the >2 flag threshold because none were used.

**Pending/ambiguous/register tag counts:**
- `W-1-PENDING`: **6** sites (7 verb instances) — channel or "the feeling" as subject of an intention verb (*meant, trying, means*). Logged, not resolved, per the constraint.
- `W-2-PENDING`: **11** sites (~15 verb instances) — chapter/book/Chapter 1 as subject of a discourse verb (*runs, does, taught, teaches, handed, named, pointed, takes up, breaks, leaves*). This chapter is unusually self-referential (it opens by explaining its own length and structure, and closes with an extended recap), so this count runs high; that is evidence for the W-2 ruling, not a defect finding.
- `AMBIGUOUS-REFERENT`: **5** sites — every place "the game" is grammatical subject of a verb. Routed to triage, not disambiguated.
- `HANDBOOK-REGISTER`: **1** site — inside the Handbook block, a feeling-as-subject intention verb inside Maera's admissions prose.
- `CHARACTER-VOICE`: **0** — no in-body quoted dialogue commits an unearned-agency error; the register only exists in marginalia this chapter, which is out of scope.

**The chapter's characteristic failure.** This chapter is disciplined almost everywhere it could have gone wrong. The five-channel liturgical register — the chapter's signature device, used upward of thirty times — stays inside its license (directional and perception verbs only) with real consistency; the one place it strays into social-causal territory (*fear teaches you*) is explicitly protected and correctly so. The Controller/referee material, easily the densest daemon writing in the chapter, keeps every verb inside the daemon's established job and never inflates into another part. The one real, concentrated defect is the origin myth in Sections 1–2: "the village" is written as a single mind that *learns*, *forgets*, *sees*, *means*, *needs*, and once, explicitly, *trains* and *teaches* its members — precisely the Grade 6 category error the registry's own worked example warns against ("Culture does not train, reward, or punish. People do those things."). It is almost entirely confined to those two sections (eleven of the twelve Tier 3 sites), with three faint callback echoes later in the chapter. Outside that one recurring device, this chapter earns its keep.

## Sites

### [Tier 3] line 316 — `the village` (Grade 6) + `trains`, `teaches` [social-causal]
**Current:** > The village trains everyone to turn feeling down. It hands you a dial in childhood and teaches one direction: lower it.
**Reading:** This is the registry's own textbook case, verbatim: a Grade 6 subject taking the social-causal verbs the grade has no license for at all ("Culture does not train, reward, or punish. People do those things, and the pattern is the name for what their doing leaves behind."). No institution trains anyone; specific people — parents, teachers, whoever is in the room when a child is told to calm down — do the training, over years, one correction at a time. The dial metaphor that follows is genuinely earned (it is the mechanism for the *rest* of the paragraph), but the subject doing the training is never named.
**Op:** R1
**Proposed:** > Parents and teachers train children to turn feeling down. They hand you a dial in childhood and teach one direction: lower it.
**Disposition:** fix
**Flags:** none

### [Tier 3] line 134 — `the village` (Grade 6) + `learned` [perception]
**Current:** > The village still experienced fear. Fear of things going wrong. Fear of not being good enough. Fear of getting blamed if something in the allyship went sideways. Without the Shaman to say "fear is your compass, it's showing you where the real risk lives," fear became noise. A thing to be managed, suppressed, medicated away. The village learned to not-feel the fear, which meant the village also missed the intelligence fear kept trying to deliver. The village became brittle. Reactive. Defended.
**Reading:** "Learned" is a perception-class verb; villages do not learn, people teach children not to feel things and the children grow up and repeat it. The clause "fear kept trying to deliver" is a separate, W-1-pending construction (channel + intention) and is left untouched in the rewrite.
**Op:** R1
**Proposed:** > Parents taught their children not to feel the fear, and so their children missed the intelligence fear kept trying to deliver.
**Disposition:** fix
**Flags:** none

### [Tier 3] line 136 — `the village` (Grade 6) + `learned`, `forgot` [perception]
**Current:** > The village still experienced anger. […] The village learned to redirect anger *outward* at the systems, the bad people, the ones who weren't as woke. It forgot that anger could also point inward, showing you where your own boundaries got crossed, what you actually cared about beneath the performance.
**Reading:** Two perception verbs, one subject, one paragraph. The village does not learn a redirection habit or forget a fact; specific people picked up the habit of aiming anger outward and specific people stopped teaching the inward reading.
**Op:** R1
**Proposed:** > People learned to redirect anger *outward* at the systems, the bad people, the ones who weren't as woke, and forgot that anger could also point inward, showing you where your own boundaries got crossed, what you actually cared about beneath the performance.
**Disposition:** fix
**Flags:** none

### [Tier 3] line 138 — `the village` (Grade 6) + `learned`, `forgot` [perception]
**Current:** > The village still experienced sadness. […] The village learned to skip over sadness, to move quickly past it into "lessons learned" and action items. It forgot how to let sadness teach. So it kept hitting the same losses over and over, unable to actually grieve what it had lost.
**Reading:** Same defect, third instance in the same run. "Let sadness teach" is the protected liturgical construction and stays; the perception verbs governing it (*learned*, *forgot*) do not.
**Op:** R1
**Proposed:** > Managers learned to skip over sadness, to move quickly past it into "lessons learned" and action items, and nobody remembered how to let sadness teach.
**Disposition:** fix
**Flags:** none

### [Tier 3] line 140 — `the village` (Grade 6) + `learned`, `forgot` [perception]
**Current:** > The village still experienced joy. […] the village learned to celebrate *doing the work* instead of celebrating *becoming the kind of person who can do the work sustainably.* So joy became tied to output. To productivity. The village forgot that joy was also information, a signal that something true was happening, something aligned.
**Reading:** Fourth instance in the same run (fear/anger/sadness/joy each get the identical "village learned… village forgot…" treatment). The repetition across all four channels is itself the evidence this is a structural habit, not four separate accidents.
**Op:** R1
**Proposed:** > Teams learned to celebrate *doing the work* instead of celebrating *becoming the kind of person who can do the work sustainably*, and what got lost in the applause was that joy is also information, a signal that something true was happening, something aligned.
**Disposition:** fix
**Flags:** none

### [Tier 3] line 142 — `the village` (Grade 6, elliptical) + `learning` [perception]
**Current:** > Without the Shaman, the village became very busy managing emotions instead of listening to them. Very skilled at pushing through discomfort, very poor at learning from it. Very good at *appearing* evolved, very bad at *actually becoming* evolved.
**Reading:** The fragment run elides the subject, but it is still "the village" carrying "poor at learning." Restoring a human agent here has to work inside the sentence's own list rhythm or it flattens a real stylistic move.
**Op:** R1
**Proposed:** > Without the Shaman, people got very busy managing emotions instead of listening to them. Very skilled at pushing through discomfort. Nobody around them ever asked what it was trying to teach. Very good at *appearing* evolved, very bad at *actually becoming* evolved.
**Disposition:** fix
**Flags:** none

### [Tier 3] line 152 — `the village` (Grade 6) + `saw` [perception]
**Current:** > The village never saw itself doing this. It called the pattern efficiency, and the pattern starved it.
**Reading:** "Saw" is squarely on the perception lemma list. "The pattern starved it" is cleared separately (see Cleared) as licensed dead-metaphor Grade 6 pattern-verb usage, consistent with the fuel-economy register the chapter already runs.
**Op:** R1
**Proposed:** > No one who did it saw it happening. They called the pattern efficiency, and the pattern starved them.
**Disposition:** fix
**Flags:** none

### [Tier 3] line 89 — `the village` (Grade 6) + `needed` [intention]
**Current:** > At first, this seemed right. There were problems that needed solving. The village needed someone who could draw a line in the sand. Someone who could say "this is unacceptable" without softening it.
**Reading:** "Need" is on the intention lemma list. This is the earliest instance in the chapter and sets the pattern the Sections-1–2 run continues.
**Op:** R1
**Proposed:** > People wanted someone who could draw a line in the sand.
**Disposition:** fix
**Flags:** none

### [Tier 3] line 359 — `the village` (Grade 6) + `tries` [intention]
**Current:** > This is the first difference between the Shaman's practice and the village's distortion: the village tries to speed past this stage. The Shaman lingers here long enough to actually get the teaching.
**Reading:** A callback echo of the Sections 1–2 pattern, forty pages later. "Try" is on the intention list.
**Op:** R1
**Proposed:** > This is the first difference between the Shaman's practice and the village's distortion: everyone in a hurry tries to speed past this stage.
**Disposition:** fix
**Flags:** none

### [Tier 3] line 572 — `the village` (Grade 6) + `forget` [perception]
**Current:** > The village took a thousand years to forget this. The Shaman's practice is how you remember, in five stages, as many times as you need, until it becomes who you are.
**Reading:** Second callback echo. "Forget" is on the perception list.
**Op:** R1
**Proposed:** > It took a thousand years of nobody saying it out loud for the village to forget this.
**Disposition:** fix
**Flags:** none

### [Tier 3] line 123 — `the village` (Grade 6) + `meant` [intention, negated]
**Current:** > The village never meant for that to happen. It never said "go." It just stopped listening. Which, it turns out, amounts to exile.
**Reading:** "Meant" is technically on the intention lemma list, on a Grade 6 subject. But the whole sentence is a negation of that claim ("never meant"), and the two sentences after it already name the actual mechanism in behavioral terms ("it just stopped listening") rather than an interior mental state — which is exactly the demotion R1 would produce. Rewriting it risks manufacturing a fix for a sentence that is already doing the registry's own argument in grammar. This is a genuine site, mechanically, but a rewrite would be redundant with what the prose already does one clause later.
**Op:** none proposed
**Proposed:** *(none — see reading)*
**Disposition:** keep-candidate
**Flags:** none

### [Tier 3] line 435 — `the feeling` (Grade 3) + `means` [intention]
**Current:** > Every feeling you experience falls into one of five channels. Understanding which channel you're in helps you know what the feeling means to teach, and what move to make next.
**Reading:** "The feeling means to teach" reads as intention (the feeling intends something), not the licensed directional/perception classes, and not the liturgical construction either (that register is *X teaches you*, present, declarative — this is *the feeling means to teach*, an intention verb about the feeling's own aim). W-1 governs whether channels get intention verbs at all.
**Op:** none — W-1 unruled
**Proposed:** *(none — tag only, per constraint)*
**Disposition:** parked
**Flags:** W-1-PENDING

### [Tier 2] line 744 — `the council` (Grade 6) + `said`, `spoke` [speech]
**Current:** > So the council said its words. It spoke of resilience. It spoke of the hard seasons the ancestors had survived. It named the suffering of the lower families with real feeling, and it moved not one handful of earth.
**Reading:** Speech verbs on an institutional Grade 6 subject are technically unlicensed at any grade-severity combination. But this is not an accidental abstraction — it is the deliberate engine of the parable that follows. The passage is built to contrast this collective, correct, empty institutional voice against one woman's individual "true sentence" three paragraphs later ("she turned to the one at the head of the circle and said the true thing, to his face"). The story is dramatizing the exact claim the registry makes about Grade 6 language — that collective/systemic speech is residue, not agency, and that only a named person's actual sentence moves anything ("The water moved… because one sentence was true and said to the face that could change it"). Rewriting "the council said" into named individual speech would erase the contrast the whole story is built on. This is direct evidence for the W-4 ruling (systemic language as the place a confrontation gets avoided) rather than a defect to fix.
**Op:** none proposed
**Proposed:** *(none — see reading)*
**Disposition:** keep-candidate
**Flags:** W-4-relevant (placement evidence)

### [Tier 2] lines 79, 146 — `the village` / `it` (Grade 6) + `built`, `made` [causal-bare, cluster]
**Current:** > The village trusted this once. It built rituals around it. […] So the village made a choice: efficiency over wisdom. Output over presence. Action over discernment.
**Reading:** Two causal-bare instances on the same Grade 6 subject across the chapter — a thin cluster, correctly the most forgivable class in the severity ordering. Real, but low value next to the perception/intention sites above; a full rewrite would cost more than it returns.
**Op:** none proposed (low severity)
**Proposed:** *(none)*
**Disposition:** parked
**Flags:** none

### [Tier 2] line 564 — `the village` (Grade 6) + `manages`, `learning` [perception]
**Current:** > Without the Shaman, the village manages emotions instead of learning from them. The WAVE-Spiral is how you learn instead of manage.
**Reading:** Third callback echo of the Sections 1–2 pattern, and the last one in the chapter. Naming a specific human actor here would be false precision — this sentence is summarizing an aggregate workplace pattern already established in more detail elsewhere (see line 316's rewrite, which names parents and teachers for the childhood-conditioning version of the same claim). The institutional transmission path — what actually rewards managing over learning in adult workplaces — is reviews and promotion, not a person in the room.
**Op:** R6
**Proposed:** > Without the Shaman, performance reviews reward managing emotions over learning from them.
**Disposition:** fix
**Flags:** none

## W-1-PENDING — channel/feeling subjects taking intention verbs (logged, not resolved)

Six sites, seven verb instances. None proposed for fix; W-1 is unruled and these tag only.

| line | subject | verb | sentence |
|---:|---|---|---|
| 77 | fear / anger | meant | "The one who knew that fear meant something. That anger meant something." |
| 134 | fear | trying | "…the village also missed the intelligence fear kept trying to deliver." |
| 150 | anger (`it`) | trying (to tell) | "…anger gets channeled into 'righteous action' but never, ever examined for what it might be trying to tell you about yourself." |
| 341 | the feeling | means | "…fear of what the feeling means, guilt about the situation…" |
| 435 | the feeling | means (to teach) | "…helps you know what the feeling means to teach, and what move to make next." (full site above) |
| 473 | sadness | lets | "…sadness felt all the way through lets you sit with someone else's loss without collapsing into it." |

Also present, inside the Handbook block (tagged `HANDBOOK-REGISTER`, not counted above):
- Line 28–29: *"A student learns to name where a feeling landed in the body before naming what it means."* — feeling + means, intention, inside Maera's admissions prose. In-world Head document; characterization license may apply. Tag only.

## W-2-PENDING — chapter/book as subject of a discourse verb (logged, not resolved)

Eleven sites (~15 verb instances). This chapter is the most self-referential in the book (it opens by explaining its own length, closes with an extended index of its own contents, and cross-references Chapter 1 repeatedly for the fuel-economy callback), so this count is high by construction, not by defect.

| line | subject | verb(s) | sentence (abridged) |
|---:|---|---|---|
| 64 | This chapter | runs | "This chapter runs longest in the book…" |
| 68 | Chapter 3 / It | does, serves | "Chapter 3 does two jobs. It serves as the Shaman's chapter…" |
| 433 | Chapter 1 / the book | put, says | "Chapter 1 put my own fluency on the table… the back of the book says where to start." |
| 463 | The chapter | taught | "The chapter has taught you to feel each channel all the way through." |
| 467 | Chapter 1 | pointed | "…the renewable fuel Chapter 1 pointed you here to make." |
| 501 | Chapter 1 / this chapter | handed, named, teaches | "Chapter 1 handed to the Shaman to finish… Chapter 1 named the fuel; this chapter teaches you to make it." |
| 680 | this chapter | takes up | "The second half of this chapter takes up the part of you that decides…" |
| 701 | this chapter | taught | "Everything the first half of this chapter taught you runs on a feeling being allowed onto the field." |
| 754 | this chapter | breaks | "That is the myth this chapter breaks." |
| 779 | this chapter | can do | "The Controller developed does one thing nothing else in this chapter can do…" |
| 981 | The chapter | leaves | "The chapter leaves you holding a practice whose parts fit together." |

## AMBIGUOUS-REFERENT — every "game"-subject site

Per the registry, none of these are disambiguated. Routed to triage as-is.

| line | sentence |
|---:|---|
| 268 | "A game exists for exactly this, Tough Conversations." / "The game removes the option of solving." |
| 318 | "…with the dial down, the rest of the game has nothing to work with." |
| 465 | "A feeling can settle on its own sometimes… but the game does not wait on that." |
| 703 | "…keeping the game honest, which now includes letting you feel." |

## Cleared

Sites the recall net raised, or that a mechanical grade/verb-class check would flag, that are not defects.

- **Lines 199, 201, 203, 205, 347, 567, 830, 842, and ~10 more** — the liturgical five-channel register ("fear teaches you what you actually care about," "anger teaches you where you're willing to stand," "sadness teaches you what was real," "joy teaches you what's aligned," and the many restatements: *shows, points, detects, arrives*). Explicitly protected per task instructions; not flagged regardless of the mechanical social-causal classification some of these verbs (*teaches*) would otherwise carry. Full accounting in the Grade 3 census below.
- **Lines 233, 205 ("School of the Body teaches / argues")** and one more instance at the same passage — recall net flagged "the school" (Grade 6) taking social-causal *teaches*. Cleared via C1: this whole section (Section 3, "The Concept") is Maera Voss's first-person testimony, signed at line 246 ("the first treatise, submitted by Maera Voss… Head of the School of the Body"). The mechanism is fully on the page — she is the actual teacher, describing her own practice throughout in the first person ("I recorded contempt…," "I called it discipline…"). The abstraction "the School of the Body" here is shorthand for her own described teaching, not an unearned institutional mind.
- **Line 756** — recall net flagged "the joystick" (Grade 4) + "aimed" as intention. Misparse: the grammatical subject of "aimed" is the compound "The sensing, the WAVE, the Controller," not "the joystick" (the joystick is the object of "pried off" in the preceding clause). Controller is Grade 2 (licensed for intention); "the sensing" and "the WAVE" are Grade-0-adjacent but the construction is a summarizing metaphor with the mechanism (the whole chapter) fully established. Not a finding.
- **Line 136, 352** — recall net flagged "anger" + "needed"/"needs" as intention. Misparse both times: the grammatical subject of "needed" is "systems" ("systems that needed to change"), and of "needs" is "what obstacle"/"what boundary" ("what obstacle needs overcoming"), not "anger." Anger is a topic marker ("If it's anger:"), not the verb's subject.
- **Line 152** — "the pattern starved it." Grade 6 subject + a verb not on any lemma list literally, but functioning as the converse of the chapter's own established fuel/token economy metaphor (renewable vs. non-renewable tokens, spending, draining). Mechanism is on the page (the whole Energy Ecology section). Treated as licensed dead metaphor, consistent with the registry's own "Token/Ticket… pays out nothing" example. (The governing clause of the same sentence, "the village never saw itself," is flagged above — this is only the second clause.)
- **Line 985** — "The system did not give you your superpower." Causal-bare ("give") on Grade 6, but negated and isolated (a lone instance, not a cluster) — explicitly denying the system agency, which is the chapter's own correct claim ("Your specific survival shaped it"). Not worth a row per the causal-bare clustering rule.
- **Line 320** — "Opening trains you to hold sensation on purpose." Reads at first pass like the same defect as line 316 ("the village trains everyone"), but the sense of "train" here is athletic/practice ("running trains your legs"), not institutional social control, and the mechanism — repetition, described in the same sentence and the paragraph around it — is fully on the page. Distinguished deliberately from line 316, where "train" is the suppression-conditioning sense the registry's example targets.
- **Line 830, 942** — "the channel stops being weather and becomes an object on the table"; "It names the channel that has a sanctioned output." First is Grade 3 taking directional/state-transition verbs not on any severity-critical list (dead metaphor, licensed by extension of the directional class). Second has "It" = the Controller (Grade 2, licensed) as the actual subject; "the channel" is the object.
- **Lines throughout Section 5** ("rules," "judges," "convenes," "holds court," "verdict," "the judge already has every past ruling on file") — the Controller/referee/judge extended metaphor. Social-causal-class verbs (*judge*) technically sit outside Grade 2's bare licensed-class list [perception, intention, speech, somatic], but the Controller's canonical job, established explicitly across the whole section, *is* judging and standard-setting. C1's mechanism-on-page override applies squarely: the entire section is the mechanism. Not itemized individually — there are dozens of instances — because they are one consistent, well-earned daemon voice, not scattered category errors.

## Grade 3 census

Every channel/feeling-subject construction identified, grouped by license category. This is the evidence base for the W-1 ruling.

**Liturgical (protected — never flagged), representative sites:**
- Line 199: "fear teaches you what you actually care about… fear shows up… It shows you your real values"
- Line 201: "anger teaches you where you're willing to stand… Anger is the voice that says 'this is not acceptable.'"
- Line 203: "sadness teaches you what was real… Sadness says 'this was true…'… Sadness is the voice that says 'no. This mattered.'"
- Line 205: "joy teaches you what's aligned… Joy shows up… Joy is the feeling that says 'yes…'"
- Line 347: "Fear's job is to detect threat and risk… Sadness's job is to point you toward what you care about… Joy's job is to show you what's aligned…"
- Line 567: "fear shows you what matters"
- Line 842: "Fear that showed you what matters becomes a value you hold… Anger that showed you a line becomes a line you are allowed to have."
- Approximate total across the chapter: **15–18 instances**, concentrated in Section 3 ("The Concept") and its Grow-stage callbacks. This is the register named explicitly protected in the task brief and is the chapter's signature move.

**Directional (licensed outright):**
- Lines 331–339: "Fear arrives… Anger arrives… Sadness arrives… Joy arrives… Neutrality arrives."
- Lines 471–479: "Fear completes into wonder… opens into curiosity"; "Sadness completes into poignance… opens into poignance"; "Anger completes into triumph"; "Joy completes into bliss"; "Neutrality completes into peace."
- Line 347: "Sadness's job is to point you toward…"
- Approximate total: **~12 instances**, concentrated in the Satisfied States section (lines 461–481) and the Clean stage (331–339).

**Perception (licensed outright):**
- Lines 331–355: "what does fear actually detect?"; "If it's fear: what threat or risk does it detect?" (and parallel lines for anger/sadness/joy/neutrality)
- Line 364: "Now you understand what the feeling shows you."
- Line 981: "The five channels… tell you which teaching a given charge carries."
- Approximate total: **~10 instances**, concentrated in the Clean stage (Section 4).

**Intention — W-1-PENDING (tagged, not resolved):**
- 6 sites, 7 verb instances. Full table above. Concentrated at the seams of the chapter (the Section 1 origin frame, the Section 2 distortion, and two definitional moments in Sections 3–4) rather than inside the liturgical passages themselves — the liturgical register, notably, never once reaches for an intention verb on its own; it stays inside perception/directional with real discipline. The W-1 question in this chapter is not "does the signature device need intention" (it doesn't, and doesn't use it) but "do the chapter's connective-tissue sentences, written faster and less carefully than the liturgical set-pieces, drift into it" (they do, six times).
