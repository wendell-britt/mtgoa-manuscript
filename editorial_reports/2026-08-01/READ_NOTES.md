# Read-through notes — the PDF pass

Wendell reads `build/MTGOA_<date>_trade.pdf` and pastes the lines that do not
work. Each one lands here as a row, located back in canon, and then gets worked
line by line.

## The loop

**1 · Paste.** Any number of lines, blank line between them. Curly quotes,
em-dashes, and a line the typesetter broke across a page all come through fine —
`find_line.py` folds them back before it searches.

**2 · Locate.** They get filed here automatically, with the component, the
surface, and the file and line number:

```bash
pbpaste | python3 instruments/find_line.py - --file editorial_reports/2026-08-01/READ_NOTES.md
```

**3 · Rule, one at a time.** Wendell says why a line does not work; the
replacement goes in the console before it goes near `manuscript/`, per the
standing rule. Status moves `open` → `ruled` → `applied`.

**4 · Apply and re-measure.** Gate on four surfaces, `compile.py --check`,
rebuild.

## Two things the locator will tell you that are findings in themselves

**A line found in more than one place.** Sentences have been duplicated across
chapters in this book before, which is why `dupes.py` exists. If a flagged line
matches twice, that is worth knowing before deciding what to do with it.

**A line found on the `margin` surface.** The annotator is a character, not
Wendell, and the margin is scored separately (DL-6, DL-25). A note about the
annotator's hand is a different kind of note.

## The notes

| ID | Component · surface | Location | Line as it stands | Why it does not work | Replacement | Status |
|---|---|---|---|---|---|---|
| N01 | Author's note · body | front_matter/authors_note.md:3 | Everyone with a phone became a marketer. Nobody signed up for that, the training never arrived, and the standard kept rising anyway. The same thing has happened to helping. | Not EVERYONE with a phone became a marketer. A phone plus social media meant everyone became responsible for their own branding. Needs at least another line on that. | open |
| N02 | Author's note · body | front_matter/authors_note.md:9 | A system like that produces a predictable game, and the game seats three kinds of player. Some understand that visible allyship converts into standing, and spend accordingly. Some believe the stated mission, do the actual labor, and burn out inside three years. The rest are the people the apparatus is nominally for, who tend to get asked last. | *three kinds of players*, not *player*. | open |
| N03 | Author's note · body | front_matter/authors_note.md:17 | Ken Wilber named this confusion, and his name for it is the most useful thing I can hand you before chapter one. He calls it the pre/trans fallacy. Two very different positions sit on either side of the conventional middle: one that has not reached the rules yet, and one that has been through them and come out the far side. From inside the middle, the two look identical. | Hedging — go straight to what Ken says. And the pre/trans sentence is too baroque: the plain version is that from the conventional position, preconventional and postconventional are hard to tell apart. Wants a one-line example, ideally a jerk joke — harm reduction is where it is most poignant. Some cause harm because they are preconventionally unskilled; others know you sometimes have to cause discomfort to move somebody up, and challenging a paradigm is about the most uncomfortable thing you can do. | open |
