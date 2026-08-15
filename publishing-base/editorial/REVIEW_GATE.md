# Portable Editorial Review Gate

> Publishing Base version: 0.1

This is the house sequence. Each book supplies its own rules, vocabulary, thresholds, and voice references.

## 0. Plain-language truth test

Before styling a passage, say what it means in ordinary language.

If the plain version is unclear, stop. The idea is not ready for prose polish.

The plain version is not the target register. It is the control sample used to reveal what the styled version adds.

## 1. Claim integrity

Check that the proposal preserves the author's actual point and does not add unsupported particulars.

Fail the passage if it invents:

- author history;
- reader history;
- bodily or somatic experience;
- examples or scenes;
- quotations;
- statistics;
- factual claims;
- motives, diagnoses, or pathologies;
- certainty the source material did not contain.

When specificity is needed, make the event or mechanism concrete instead of inventing a biography for the reader.

## 2. Hard local gate

Run the book's deterministic rules:

- placeholders/tokens;
- banned production syntax;
- prohibited terms;
- required heading or metadata forms;
- known mechanical defects;
- broken references.

A hard-gate hit is fixed before canon. The book-local rule file owns the list.

Do not route around a rule with a meaningless synonym. If the banned construction is what the sentence naturally wants, rebuild the sentence.

## 3. Prose-drift diagnostics

Measure patterns that are hard to see one sentence at a time, such as:

- excessive copulas or weak sentence frames;
- expletive openers;
- empty pronouns;
- nominalizations;
- empty head nouns;
- passives;
- repeated sentence length/rhythm;
- hedge density;
- em-dash dependence;
- repeated phrases across chapters.

Compare against two references where available:

1. author baseline;
2. current book's approved register.

Metrics are diagnostic. A threshold that rewards a worse sentence is a broken diagnostic, not a command to keep editing.

## 4. AI-slop reading

Read the whole proposal, not just pattern counts.

Look for:

- generic throat clearing;
- fake insight setups;
- binary "not X but Y" scaffolds;
- dramatic fragments;
- colon reveals;
- robotic symmetry;
- faux-profound kickers;
- synonym cycling;
- invented examples;
- polished abstractions where the author used a concrete noun;
- smoothing away humor, edge, uncertainty, or oddness that belongs to the writer.

The goal is not to make prose maximally tidy. The goal is to remove generated habits while leaving the human sentence alive.

## 5. Repair check

After any repair, rerun the relevant diagnostics.

Assume a repair pass can create a new defect. Common failure shapes include:

- reducing pronouns by inventing a definite noun phrase;
- replacing an abstraction by falsely making the reader the actor;
- eliminating a copula by giving an inanimate subject a fake action;
- avoiding a banned word with a weaker synonym;
- compressing repetition until the author's cadence disappears.

## 6. Author visibility and approval

For canonical prose changes, Wendell sees the actual proposed wording before it lands unless he explicitly delegates that class of change.

A summary, score, counter, or file path is not a substitute for showing prose.

## 7. Canon insertion

After approval:

- apply the approved text;
- commit it;
- run manuscript-wide checks;
- verify the changed file can be read back from the durable repository state.

If later tooling changes wording, that later wording is a new proposal unless the transformation was explicitly declared mechanical.

## Review result

Use one of four outcomes:

- **PASS — eligible for approval/canon**
- **REVISE — prose problem identified**
- **BLOCK — unsupported claim, hard gate, or structural defect**
- **RULING — the tooling cannot decide; Wendell must choose**

Do not convert a RULING into an automatic fix.
