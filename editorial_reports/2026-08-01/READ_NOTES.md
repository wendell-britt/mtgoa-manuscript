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
