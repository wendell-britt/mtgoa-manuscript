# Read-through notes — the PDF pass

Wendell reads `build/MTGOA_<date>_trade.pdf` and pastes the lines that do not
work. Each one lands here as a row, located back in canon, and then gets worked
line by line.

## Standing rule for this session

**Wendell, 2026-08-01: everything pasted into the session is a defect until he says
otherwise.** A line arriving without a stated reason is still work; the reason
comes later, or the line gets read again together. Nothing pasted is context.

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
| N05 | Author's note · body | front_matter/authors_note.md:25 | Here is the part worth sitting with. Allyship is already a game, and it is already gamified. Yu-kai Chou, who maps what actually drives people, separates the motivators that leave you feeling capable from the motivators that leave you anxious and compliant. Both get results. Scarcity, social pressure, and fear of losing your standing will absolutely make somebody act, and they will hollow that person out over about three years. Every drive currently powering allyship comes from that second set. The work is not the problem. The drives underneath it are. | Cut. Do not tell people what is worth sitting with. | | open |
| N06 | Author's note · body | front_matter/authors_note.md:27 | So this book moves the same work onto the other set, and it does that by being an actual game, with a world in it, six schools, and the six people who run them, who will argue with you in the margins. | What is *the other set*? Needs to be specific. | | open |
| N07 | Author's note · body | front_matter/authors_note.md:35 | One rule holds the whole practice up. You can make your move. You cannot make another person satisfied, and reaching for that is the exact place where helping curdles into something else. So you aim at one person, by name, you make the move cleanly, and what they do with it stays theirs. It has to stay theirs. Take that away and you are recruiting. | What is *something else*? Name it. | | open |
| N08 | Chapter 1 · body | manuscript/ch1.md:6 | I made a promise to readers who trusted me with their money and their hope, and then I couldn't deliver. The reason, when I finally let myself look at it clearly, was both embarrassing and fitting: I was writing a book about allyship, and it was making me a worse ally. Not to the people I was trying to serve. To myself, to the people closest to me, to the work itself. | Should be *made me feel like a worse ally*. | | open |
| N09 | Chapter 1 · body | manuscript/ch1.md:8 | I knew that helping people from a place of scarcity doesn't work. I'd built a whole framework around that idea. So I told myself I wasn't doing that. I was being responsible. I was staying in integrity. Every word of that was true, and every word of it left the guilt nowhere to go. It went underground. The work went with it. | Add a contraction here. | | open |
| N10 | Chapter 1 · body | manuscript/ch1.md:12 | Realizing this is what finally unlocked my ability to finish. I could see the pattern clearly, and I kept playing. It didn't have to disappear first. In fact, letting the charge of that awareness exist was what let me alchemize it into the book in your hands right now. | Flagged, reason not yet given. (Standing rule: everything pasted this session is a defect until Wendell says otherwise.) | | open |
| N11 | Chapter 1 · body | manuscript/ch1.md:14 | You're the person I made that promise to. This is me showing up: late, imperfect, and in the game. | What is *this*? | | open |
| N12 | Chapter 1 · body | manuscript/ch1.md:16 | You are a Game Master. You have been running your own allyship campaign for years, whether you named it or not. You decided which harm in a moment got named out loud and which one slid past. You set the stakes with a single sentence, or by saying nothing at all. You did almost none of it on purpose. The conscious you never called those moves. The part that runs on default did: inherited reflexes, old wounds, the face you reach for without checking whether it fits. Your unconscious has been the game master. It has run your allyship the whole time, and it plays by one rule: keep you safe. Helping the people you meant to serve was never its assignment. What changes now: you take the seat. This whole book builds toward that move, and that is why so much of it runs on shadow work. Your shadow is the game master. You cannot take the controls from a player you refuse to look at. | Cut, or explain what a Game Master is. | | open |
| N13 | Chapter 1 · body | manuscript/ch1.md:16 | You are a Game Master. You have been running your own allyship campaign for years, whether you named it or not. You decided which harm in a moment got named out loud and which one slid past. You set the stakes with a single sentence, or by saying nothing at all. You did almost none of it on purpose. The conscious you never called those moves. The part that runs on default did: inherited reflexes, old wounds, the face you reach for without checking whether it fits. Your unconscious has been the game master. It has run your allyship the whole time, and it plays by one rule: keep you safe. Helping the people you meant to serve was never its assignment. What changes now: you take the seat. This whole book builds toward that move, and that is why so much of it runs on shadow work. Your shadow is the game master. You cannot take the controls from a player you refuse to look at. | Flagged, reason not yet given. | | open |
| N14 | Chapter 1 · body | manuscript/ch1.md:16 | You are a Game Master. You have been running your own allyship campaign for years, whether you named it or not. You decided which harm in a moment got named out loud and which one slid past. You set the stakes with a single sentence, or by saying nothing at all. You did almost none of it on purpose. The conscious you never called those moves. The part that runs on default did: inherited reflexes, old wounds, the face you reach for without checking whether it fits. Your unconscious has been the game master. It has run your allyship the whole time, and it plays by one rule: keep you safe. Helping the people you meant to serve was never its assignment. What changes now: you take the seat. This whole book builds toward that move, and that is why so much of it runs on shadow work. Your shadow is the game master. You cannot take the controls from a player you refuse to look at. | Clunky and weird. | | open |
| N15 | Chapter 1 · body | manuscript/ch1.md:22 | You have done this before. You walk into a meeting or a dinner or a group chat and you catch something nobody else seems to catch: a game already running under the surface. Somebody gets talked over, or a decision lands on the person with the least power to absorb it, and the temperature drops while everyone keeps talking. You are the one who moves, changing who you look at and slowing the conversation down and saying the sentence that costs you something, even though nobody handed you that job. That pull, to step into a game no one invited you to play because you can see it and cannot leave it alone, is the call. You have been answering it since before you had a word for it. | Done what before? Hates all intros like this — vague and weird. | | open |
| N16 | Chapter 1 · body | manuscript/ch1.md:24 | Underneath it runs a feeling you have never fully worked through. It sits closest to worry, the low and steady kind that never switches all the way off. You can see how the systems you were born into wear people down by design, and you can see how little your moves seem to move the machine, and you keep playing anyway while the worry keeps running underneath the play. | Whole two-paragraph opening needs an ELI5. It assumes a secret competence, which is not the point of the book. Unconscious skills can be brought to bear, but what people actually experience is a pressure to do good that they cannot act on as consistently as they think they should. | | open |
