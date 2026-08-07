# Agency Ledger — Chapter 9: The Player

## Summary

- **Sites examined (close read + recall-net diff):** ~55 candidate subject+verb pairs on non-Grade-1 subjects.
- **Sites flagged as findings:** 33 total — **16 Tier 3**, **7 Tier 2**, **10 Tier 1** (Tier 1 reported as two consolidated cluster entries covering 10 instances, per "log at Tier 1, do not agonize"). The map-cluster (9 instances) is filed as one Tier 3 entry; the extended village-cluster remainder (~23 further instances beyond the 6 given individual entries) is filed as one REGISTRY-GAP entry.
- **R-op distribution (individually-opped sites, n=17 fixes):** R4 = 6 · R1 = 5 · R6 = 4 · R2 = 1 · R3 = 1 · R5 = 0.
- **R3-per-daemon:** Protector = 1 (line 380). No daemon over the 2-per-chapter threshold.
- **R1 guard:** 5 uses, one over the soft cap of 4. Constructions used, to show they don't drumbeat: (1) reflexive imperative — "ask yourself what you can learn"; (2) modal imperative — "ask what you are willing to become"; (3) negation-led — "Nobody tells you this"; (4) declarative, agent-fronted — "You already learned this by running the WAVE"; (5) plain narrative substitution — "People heard the six Faces and thought." No two share a grammatical shape.
- **Counts:** W-1-PENDING = 1 · W-2-PENDING = 1 · AMBIGUOUS-REFERENT = 4 · HANDBOOK-REGISTER = 0 (no HANDBOOK/SIGNATURE blocks in this file) · CHARACTER-VOICE = 0 (EPIGRAPH-BYLINE and POSTCARD blocks present but out of scope per instructions, not scanned).
- **REGISTRY-GAP:** "the village" is not enumerated in any grade in `agency_registry.yaml`, despite being the single heaviest agency-bearing subject in this chapter (~29 subject+verb instances). It is not "the ship" (Grade 5, has its own entry for the same reason — frame-fiction personification) and it is not quite "the culture" (Grade 6, abstract pattern) — it is a collective standing for a community of actual, if unnamed, people inside an origin fable. I have graded it by strongest structural analogy to Grade 6 (same shape as "the team," "the family," already enumerated there) for the purpose of scoring individual sites, but the grade itself needs Wendell's ruling, the same way `DAEMON_CANON.md`'s absence is already flagged in the registry's own header. **This is the single highest-leverage open item in this ledger** — a ruling on "village" would resolve roughly two-thirds of this chapter's findings at once, and it likely recurs in every other chapter (Sections 1–2 of this book use the same Exile/Distortion fable structure in each Face's chapter).
- **The chapter's characteristic failure:** Chapter 9 opens with a two-section origin myth ("The Exile," "The Distortion") that hands the entire founding action of the book's whole argument — teaching, forgetting, hearing, asking, needing — to "the village," never to a named teacher, student, or generation. The failure is not random; it is concentrated at the front of the chapter, in the story explaining how the six-Face model got distorted in the first place. Everywhere else, the chapter is unusually disciplined about testimony (heavy first-person "I" register in Sections 4–6) — the fable is the one place the chapter's own machinery reaches for an abstraction instead of a person.
- **Thesis-contradiction sites** (ranked, cost more than their tier suggests):
  1. **Line 43** — "The village taught that the six Faces named a destination." Opens the chapter's account of its own central distortion by having a pattern do the teaching, in the chapter whose entire argument is that you hold the joystick.
  2. **Line 51** — "The village forgot that the Faces were a map, not a menu." Same fable, "forgot" is a perception-class verb — the highest-value catch in the whole taxonomy — attributed to a collective with no one in it who remembers or fails to.
  3. **Line 370** — "Grow up: ask what the failure is actually telling you." This sits inside the chapter's own restatement of the WAVE, addressed directly to the reader as the practice they are meant to run themselves. Having the failure do the telling, in the WAVE's own explanation, undercuts the move it is teaching.
  4. **Line 384** — "Grow up: ask what this moment asks you to become." Same passage, same shape, 14 lines later — a moment issuing a demand instead of the reader deciding.
  5. **Line 640** ("Five." in The Last Rep) — two unnamed organizations perceive, speak, and defend themselves with no person in either one ever on the page, inside the chapter's own diagnostic drill for catching exactly this error in real situations.
- **B6 check: clean.** No "the game can tell the difference" or variant survives. Grepped for `tell the difference`, `can tell`, `the game (can|knows|tells|sees|senses|recognizes)`, and for any literal Grade-4 machine noun (app/cabinet/scoreboard/tokens/tickets/joystick) taking a perception verb — zero hits. The chapter's arcade-conceit machinery ("the deck," BAR cards) stays cleanly mechanical throughout (runs, deals, outlasts) and is licensed.

---

## Sites

### [T3] line 43 — `The village` (Grade 6, by analogy — REGISTRY-GAP) + `taught` [social-causal]
**Current:** > The village taught that the six Faces named a destination.
**Reading:** No mechanism for how a village teaches. Social-causal verbs are explicitly illegal at Grade 6 — patterns don't teach, people do, and the pattern is what their teaching leaves behind. No specific teacher is named or nameable in this fable register, which rules out R1 (false precision) and points to R6. **Thesis-contradiction, ranked #1** — see Summary.
**Op:** R6
**Proposed:** > Whoever taught the six Faces first taught them as a destination, and every teacher after repeated the mistake.
**Disposition:** fix
**Flags:** REGISTRY-GAP, THESIS-CONTRADICTION

### [T3] line 51 — `The village` (Grade 6, by analogy — REGISTRY-GAP) + `forgot` [perception]
**Current:** > The village forgot that the Faces were a map, not a menu.
**Reading:** "Forget" is a listed perception lemma — the class the Registry names the highest-value catch. A village has no single memory to lose; a chain of individuals stopped repeating the second half of the lesson. **Thesis-contradiction, ranked #2.**
**Op:** R6
**Proposed:** > Teacher after teacher dropped the second half of the lesson, until nobody in the village remembered the Faces were a map, not a menu.
**Disposition:** fix
**Flags:** REGISTRY-GAP, THESIS-CONTRADICTION

### [T3] line 25 — `the village` (Grade 6, by analogy) + `could teach` [social-causal]
**Current:** > They left because they had learned everything the village could teach them and they wanted to build something specific that required going further out than the village extended.
**Reading:** Same fable, same gap. "Teach" is social-causal, illegal at Grade 6. No individual teacher is nameable here either.
**Op:** R6
**Proposed:** > They left because everyone in the village who had something to teach had already taught it to them, and they wanted to build something specific that required going further out than the village's reach.
**Disposition:** fix
**Flags:** REGISTRY-GAP

### [T3] line 49 — `The village` (Grade 6, by analogy) + `heard` / `thought` [perception]
**Current:** > The village heard the six Faces and thought: *these are the types.*
**Reading:** Two perception verbs stacked on one collective sentence. Unlike the two above, this one has a natural real-persons substitute sitting right there — "people," not a fabricated name, but a real referent — so R1 fits instead of R6.
**Op:** R1
**Proposed:** > People heard the six Faces and thought: *these are the types.*
**Disposition:** fix
**Flags:** REGISTRY-GAP

### [T3] line 87 — `The book` (Grade 0) + `has been preparing` [intention]
**Current:** > The book has been preparing you for this. Not to consume the six Faces. To design your own.
**Reading:** Books don't intend. A person sequenced nine chapters on purpose. The knowing/planning happened in Wendell's head — R4's exact trigger.
**Op:** R4
**Proposed:** > I built this book to prepare you for this moment. Not to consume the six Faces. To design your own.
**Disposition:** fix

### [T3] line 224 — `the work` (Grade 0) + `needs` [intention]
**Current:** > I'll redesign the same mechanic six times, and every redesign dodges the one thing the work actually needs: putting it in front of someone and seeing what happens.
**Reading:** First person is already running this sentence ("I'll redesign"); the abstraction only takes over for the verb that names the actual failure to act.
**Op:** R4
**Proposed:** > I'll redesign the same mechanic six times, and every redesign dodges the one thing I actually need to do: put it in front of someone and see what happens.
**Disposition:** fix

### [T3] line 258 — `the culture` (Grade 6) + `taught` [social-causal]
**Current:** > Then I did what the culture taught me to do: I looked outward for the solution.
**Reading:** Textbook Grade 6 violation — social-causal verb, no license. It sits inside an already-open first-person testimony passage ("Here's what I've noticed about my own arrival at this work..."), so R4 is available directly rather than reaching for R1's "people did X to me" shape.
**Op:** R4
**Proposed:** > Then I did what every teacher, workshop, and well-meaning friend had told me to do: I looked outward for the solution.
**Disposition:** fix

### [T3] line 272 — `the structure` (Grade 6) + `lets` [intention]
**Current:** > ...how to create the structure that lets the next person act.
**Reading:** "Let/permit" is an explicit intention lemma, illegal at Grade 6. A structure doesn't grant permission; it removes an obstacle. This is the house's proven move.
**Op:** R2
**Proposed:** > ...how to build the structure that clears the next person's path.
**Disposition:** fix

### [T3] lines 294–304 — `The map` (Grade 0) + `shows` / `does not show` [perception] — cluster, 9 instances
**Current (representative, of 9):**
> The map shows you where the gates stand. It does not show you how long it takes to walk through them.
> The map does not show you what failure looks like. ... The map shows the path. The map doesn't show the rain.
> The map also doesn't show you what success looks like from the inside.
> The map doesn't show you that the walk takes as long as it takes.
**Reading:** "Show/reveal" is explicitly named a perception-class verb "even when aimed outward." Nine instances across an eleven-line passage, symmetrically built ("The map [does/doesn't] show you X"), reads as a deliberate, self-aware extended metaphor (the passage opens by naming its own device: "The map is honest about the terrain. It is not honest about the weather.") — closer in spirit to the protected liturgical register than to a slip, but "map" carries no Registry license the way the five channels do, and this is not Grade 3. Per C3 I cannot rule this a keep myself.
**Op:** if fixed, R4 — the book, not the map, is the thing with an honesty policy.
**Proposed (illustrative only, not proposed for shipping):** > I can be honest with you about the terrain. I can't be honest about the weather.
**Disposition:** keep-candidate
**Flags:** likely deliberate device — queue to read-aloud pass

### [T3] line 360 — `The book` (Grade 0) + `refused` [intention]
**Current:** > The book refused to come clear. The shape kept changing.
**Reading:** "Refuse" is an explicit intention lemma. A person sat down and failed to get chapters to cohere; the surrounding paragraph is already first-person testimony ("I sat in front of chapters I could not write"), which makes this the one sentence in the passage that ducks into the abstraction.
**Op:** R4
**Proposed:** > I could not get it to come clear. The shape kept changing on me.
**Disposition:** fix

### [T3] line 370 — `the failure` (Grade 0) + `is ... telling` [perception]
**Current:** > Grow up: ask what the failure is actually telling you.
**Reading:** "Tell" is a listed perception lemma. This sits inside the chapter's own restatement of the WAVE, in second person, addressed to the reader as a move they run themselves. Structurally it rhymes with the banned B6 shape (an event doing the telling instead of a person doing the perceiving) even though the subject here is "failure," not a machine, so it does not itself trip B6. **Thesis-contradiction, ranked #3** — the WAVE is presented everywhere else as something the reader runs, not something that runs on the reader.
**Op:** R1
**Proposed:** > Grow up: ask yourself what you can learn from the failure.
**Disposition:** fix
**Flags:** THESIS-CONTRADICTION

### [T3] line 328 — `the book` (Grade 0) + `would fail you` [social-causal, nearest lemma: abandon/betray]
**Current:** > Let me tell you honestly what the walk actually looks like, because the book would fail you if it ended with a rousing speech about your potential and left you to figure out the rest alone.
**Reading:** "Let me tell you honestly" is first person, one clause away — the sentence opens the author's chair and then hands the verb to the book anyway. Only a person can fail someone this way.
**Op:** R4
**Proposed:** > Let me tell you honestly what the walk actually looks like, because I would be failing you if I ended this with a rousing speech about your potential and left you to figure out the rest alone.
**Disposition:** fix

### [T3] line 408 — `the book` (Grade 0) + `would cheat you` / `pretended` [social-causal / intention]
**Current:** > I want to name that directly, because the book would cheat you if it pretended everyone leaves Chapter 9 with a fully-formed game.
**Reading:** Same shape as line 328 — "I want to name that directly" opens the chair in the same sentence, then hands the cheat/pretend verbs to the book.
**Op:** R4
**Proposed:** > I want to name that directly, because I would be cheating you if I pretended everyone leaves Chapter 9 with a fully-formed game.
**Disposition:** fix
**Flags:** AMBIGUOUS-REFERENT ("a fully-formed game" — arcade/RPG-companion sense unclear; not resolved, noted only)

### [T3] line 430 — `The culture` (Grade 6) + `tells` [perception]
**Current:** > The culture never tells you this: the Founder move probably already sits somewhere in your history.
**Reading:** Explicit Grade 6 perception violation. Structurally identical to the banned B6 shape (abstraction doing the telling) though the subject is "culture," not a machine, so B6 itself is not tripped. What's actually missing is a person who never said this to you.
**Op:** R1
**Proposed:** > Nobody tells you this: the Founder move probably already sits somewhere in your history.
**Disposition:** fix

### [T3] line 640 — `One` [organization, Grade 6] + `watched` [perception]
**Current:** > One did most of the work on a campaign and watched the other take the press.
**Reading:** "Organizations" is explicitly enumerated at Grade 6 — only pattern-residue verbs are licensed there. This is ordinary business idiom, which is exactly the shape the Registry warns about: no spokesperson, no staffer, nobody inside either organization is ever on the page. This sentence sits inside the chapter's own diagnostic drill ("The Last Rep") for training the reader to catch this move in real situations. **Thesis-contradiction, ranked #5.**
**Op:** R6 — naming individuals inside two unnamed coalition orgs would be false precision the scenario doesn't support.
**Proposed:** > One org did most of the work and its people watched the credit go to the other.
**Disposition:** fix
**Flags:** THESIS-CONTRADICTION

---

### [T2] line 29 — `the village` (Grade 6, by analogy) + `asked` [speech, quoted]
**Current:** > When the village asked *what now?* the Player said: *I'm going to build something.*
**Reading:** Direct quotation in a collective's mouth. No single speaker; a diffuse question from many.
**Op:** R6
**Proposed:** > When enough of the village asked, in enough different ways, *what now?* the Player said: *I'm going to build something.*
**Disposition:** fix
**Flags:** REGISTRY-GAP

### [T2] line 298 — `the village` (Grade 6, by analogy) + `says` [speech, quoted]
**Current:** > ...and the village says *we don't want this.*
**Reading:** Same shape as line 29 — a literal quotation placed in a collective's mouth, inside the "What the Map Doesn't Show You" passage.
**Op:** R6
**Proposed:** > ...and enough of the village says, in enough different words, *we don't want this.*
**Disposition:** fix
**Flags:** REGISTRY-GAP

### [T2] line 370 — `The WAVE` (Grade 0, by analogy to "the method"/"the process") + `taught` [social-causal]
**Current:** > The WAVE already taught you how to do this.
**Reading:** Social-causal on an unlicensed subject. The reader did the learning by running the practice; the WAVE is the name of the practice, not the teacher.
**Op:** R1
**Proposed:** > You already learned this by running the WAVE.
**Disposition:** fix

### [T2] line 380 — `The fear` (Grade 3) + `does not say` / `says` [speech, quoted]
**Current:** > The fear does not say *don't do this.* The fear says *this matters enough to be afraid of.*
**Reading:** Grade 3 licenses only directional and perception, with intention pending W-1. Speech is not licensed and is not part of the open question — it is a plain violation, and a heavier one than intention since it puts literal reported dialogue in the current's mouth. This is distinct from the protected liturgical register two sentences later in the same paragraph ("the fear shows me what I care about," which is perception-class and stays exactly as written). The Protector is the daemon on the page elsewhere in this chapter (line 476) whose canonical job is exactly this kind of threat-rehearsal.
**Op:** R3 → Protector
**Proposed:** > My Protector doesn't say *don't do this.* It says *this matters enough to be afraid of.*
**Disposition:** fix
**Flags:** R3→Protector (count: 1 this chapter)

**Same paragraph, not fixed:**
- "it rehearses" (referring to fear) — intention verb on a Grade 3 subject. **Tag W-1-PENDING. Not resolved.**
- "The fear will run the entire scenario" — "run" is a licensed directional lemma. Cleared, not a finding.
- "the fear shows me what I care about ... it shows me what I'm trying to build" — liturgical register, perception-class, protected. Cleared, not a finding.

### [T2] line 384 — `this moment` (Grade 0) + `asks` [speech]
**Current:** > Grow up: ask what this moment asks you to become.
**Reading:** Same passage as line 370's "failure is telling you," 14 lines later, same construction — an abstraction issuing a demand instead of the reader deciding. Two instances of "abstraction + tells/asks you" in one restatement of the WAVE is a real pattern, not a singleton. **Thesis-contradiction, ranked #4.**
**Op:** R1
**Proposed:** > Grow up: ask what you are willing to become because of this.
**Disposition:** fix
**Flags:** THESIS-CONTRADICTION

### [T2] line 640 — `The other` [organization, Grade 6] + `says` [speech]
**Current:** > The other says it was offered the interview, stole nothing, and is now under attack.
**Reading:** Same organization-personification as the "watched" clause in the same sentence (filed above at T3), scored separately because speech, not perception, is the verb class here.
**Op:** R6
**Proposed:** > Someone on the other side says they were offered the interview, took nothing that wasn't offered, and now they're the ones fielding the blame.
**Disposition:** fix

### [T2] line 502 — `These five moves` (Grade 0) + `name` / (implicit) `measure` — discourse/methodology self-reference
**Current:** > These five moves do something else: they name what you do when another person sits across from you and the thing you made lies on the table between you.
**Reading:** Reads as the book's own apparatus describing itself, the same shape as "this chapter asks" / "the book returns to."
**Op:** none — W-2 governs this class of site.
**Proposed:** none.
**Disposition:** parked
**Flags:** W-2-PENDING

---

### [T1] Dead-metaphor clusters — mechanical/directional on unlicensed subjects, per instructions logged briefly and not agonized over
- **"The walk" as subject** (Grade 0, by analogy to "the process"): lines 220 ("does the work move toward contact"), 222 ("the work goes somewhere"), 330 ("the walk begins before you're ready"), 374 ("the walk will not do for you: it will not eliminate fear"), 390 ("the walk also means"), 416 ("the walk will produce the game"), 440 ("the walk includes failure"), 448 ("the walk ends the way all walks end"), 552 ("a total rebuild resets the clock"). ~9 instances, directional/mechanical, dead metaphor.
- **"The pull is toward [Face]"** — six instances, one per moment in "The reads" (lines 648, 650, 652, 654, 656, 658). Directional, formulaic by design (it's a drill with a fixed answer key format), dead metaphor.
**Disposition:** parked (both clusters)

### [Ambiguous] `game`-subject and `game`-token sites — routed to human triage per standing instruction, not adjudicated
- **Line 300** — "you realize the game did that." `game` is grammatical subject of a causal-bare verb.
- **Line 354** — "A game can fail to be fun, and fun on its own can fail to make a great game." `game` is grammatical subject (first clause).
- **Line 463** — "Before you step into the game: a gate scan." `game` is object of "step into," reference sense still undetermined.
- **Line 647** — "...is information about the game rather than about the argument." `game` is object of "about," reference sense still undetermined.
**Disposition:** parked (all four)
**Flags:** AMBIGUOUS-REFERENT

### [REGISTRY-GAP] `the village` — remaining ~23 subject+verb instances not given individual entries
Beyond the six sites above (lines 25, 29, 43, 49, 51, 298), "the village" takes an agentive verb roughly 23 more times in this chapter: `was glad` / `needed` (33), `needed` (85), `actually needs` (256), `needs you` (312), `needs ... needs` (320, ×2), `doesn't receive` (376), `wasn't ready` / `often resists` (442), `doesn't need` / `needs` (456, ×2), `needs played` (618), `is waiting` (690), plus several more object-position and locative uses. All share the same missing-mechanism problem as the six logged individually. I have not written 23 individual rewrites — that would be manufacturing ledger bulk rather than reporting findings — but the count is real and the fix, once "village" has a ruled grade, is mechanical to apply using the same R6/R1 pattern shown above.
**Disposition:** parked
**Flags:** REGISTRY-GAP — needs Wendell's grade ruling before further remediation on this entity proceeds, chapter-wide and likely book-wide.

---

## Cleared

Sites the recall net raised, or that a pattern-match would flag, that are NOT defects:

- **Line 268, `fear` + "reaching for the plan."** Grammatical subject of "reaching" is the implied "you" (the Shaman), not fear — fear is the object of the preceding preposition. Net false positive.
- **Line 356, `guilt`/`shame` + "allied with."** Guilt and shame are objects of "allied with," not verb subjects — the subject is "They" (Grade 1, the people who finished the course). Shame does nothing here; it is acted upon.
- **Line 384, `the channel` + "let it run."** "Let" belongs to the imperative "[you] let it run," not to the channel. The channel itself only takes "run," which is a licensed directional lemma for Grade 3.
- **Line 396, `the book` + "want."** Grammatical subject of "want" is "people who want to do inner work," not the book. Net misattribution.
- **Line 524, `this chapter` + "tell."** "Earlier in this chapter" is a locative phrase, not a subject-verb agency claim; there is no verb with "this chapter" as subject in the sentence.
- **The five modes** (Cartographer, Designer, Founder, Elder, Outlaw) taking perception/intention/speech throughout Section 4 (e.g., "The Cartographer doesn't judge the map. It just draws it," "The Founder says..."). Mechanism is explicitly on the page at line 109: "The five modes work as roles, not personalities: you move through them as you design your practice." These are the reader wearing a role-name — Grade 1 by canon, not a bare-grade violation.
- **"The fear shows me what I care about... it shows me what I'm trying to build"** (line 380) and all other "[channel] shows/points to X" constructions in the chapter. Liturgical register, Grade 3 at full power, explicitly protected — never flagged.
- **"The fear will run the entire scenario"** (line 380). "Run" is a licensed directional lemma for Grade 3.
- **"The deck runs underneath all five of them," "deals you the card," "outlasts any single trip"** (lines 189, 171, 196) and similar deck/BAR-deck mechanical language throughout. Grade 4 machine-analog, mechanical verbs only — model citizen, matches the "pays out nothing for" pattern the house has already ruled licensed.
- **All uses of "The Shaman," "The Challenger," "The Regent," "The Architect," "The Diplomat," "The Sage," "The Player" as agentive subjects throughout the chapter.** Grade 1 by canon — these are the reader in a given mode, established since the book's opening chapters.
- **"You know how the Shaman feels what's true... before reaching for the plan"** (line 268) and the parallel six-paragraph "You know how the X..." passage (lines 268–278). All subjects are Grade 1 "you" or the licensed Face-identities; no bare abstraction takes a verb here.
