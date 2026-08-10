# Voice kit — the book's editorial system, portable

**Built 2026-08-10 from `wendell-britt/mtgoa-manuscript` at the final proof.**
For dropping into `johnair01/bars-engine`, or any repo with customer-facing copy.

The manuscript repo carries 196 instruments and ~100 specs. **Almost none of it ports**,
because almost all of it is about a book: a typeset spine, marginalia membranes, chapter
registers, a 313-entry outline. Copying it whole would ship a system that mostly reports
about files that do not exist.

This is the portion that is about English, plus the two rules that survived contact with a
reader. It is small on purpose.

```
agents-skills/
  no-ai-slop/        SKILL.md · eval.md · LICENSE     ← MIT, Peter Yang. Verbatim.
  house-voice/       SKILL.md · reference.md          ← new, adapted for product copy
tools/
  voice_lint.py                                       ← self-contained, stdlib only
```

---

## Install

```bash
# from the bars-engine repo root
cp -r voice-kit/agents-skills/no-ai-slop  .agents/skills/
cp -r voice-kit/agents-skills/house-voice .agents/skills/
mkdir -p tools && cp voice-kit/tools/voice_lint.py tools/

python3 tools/voice_lint.py "src/app/**/*.tsx"
```

`.agents/skills/` is where bars-engine already keeps its twelve skills, and both of these
carry the same frontmatter shape (`name`, `description`) as `narrative-quality` and
`deftness-development`, so they register the same way.

**`no-ai-slop` is MIT-licensed to Peter Yang and the `LICENSE` file must travel with it.**
That is the entire condition of the license; do not copy `SKILL.md` on its own.

---

## What each piece is for

**`no-ai-slop`** — unchanged from the book repo, at your request. It is a reading rather
than a measurement, so no instrument can replace it. Run it against its own `eval.md`, not
only the pattern list in `SKILL.md`: the pattern list finds bad sentences, `eval.md` finds
*invented* ones, which is the failure that reaches customers.

**`house-voice`** — the new one. The order of operations (ELI5 → lint → slop → stance),
the always-on constraints, the fourteen colors, and the portable rows of the style sheet.
It says explicitly what it is *not* for, so it does not collide with the existing
`narrative-quality` skill: that one trains on admin feedback for AI-generated quest prose;
this one is for copy a person wrote and a customer will read.

**`voice_lint.py`** — the counters from `gate.py`, `prose_diet.py` and `empty_head.py`,
copied **verbatim** so the site and the book cannot drift into disagreeing about what a
defect is. Standard library only. When the book's counters change, re-copy them rather
than re-deriving them.

It reads `.tsx` by extracting only customer-visible strings — JSX text nodes and prose-like
literals — because linting the code produces noise, and a board that is mostly noise trains
you to skim it. Every report prints a coverage line saying how much it actually scanned, so
a clean board on forty characters is visibly a clean board on forty characters.

---

## The board on your site right now

Run against the four customer-facing surfaces, unmodified, on 2026-08-10:

```
src/app/launch/page.tsx                         119w    HARD  1
src/app/mastering-allyship/chapter-1/page.tsx   686w    HARD  2
src/app/mastering-allyship/page.tsx            2786w    HARD 49
src/lib/launch/offers.ts                        734w    HARD  1
                                                        ── 53
```

Most of the 49 is `things` and `quiet` on the long sales letter, which is what you would
expect from a page written before the ban existed. **This is a starting board, not a
verdict.** Nothing here is a reason to rewrite a page that is converting; it is a list to
work through the next time each surface is touched.

---

## Three honest notes

**The kit's own docs run heavy on two soft counters.** `zombie` at 1.95, `waste` at 1.29 on
`reference.md`. That is real and it is correct: documentation about editing is full of
`the sentence`, `the definition`, `the concealment`, and prose about prose legitimately
sits in a different register than a landing page. The book repo has a `REGISTERS` table for
exactly this. **The hard board is 0** on both files, and the hard board is the tier that is not a
matter of register.

**The seven Heads did not come with this.** Maera Voss and the other headmasters are
in-world authors of in-world documents, and a product surface speaking as a fictional
headmaster is a category error — the customer has not opted into the fiction yet. What
ports is Wendell's own register. If you later want the Heads for something inside the
experience (a quest, an oracle reading), those specs live at
`marginalia/specs/SEVEN_VOICES.md` and `HEAD_VOICE_DIAL.md` in the book repo and want their
own handoff, because they are 490 lines and every rule in them is about in-world genre.

**The concealment rule is scoped to the book, and `house-voice` says so.** The book never
names the six Faces as integral altitudes; bars-engine names Spiral Dynamics and Integral
Theory openly in `/wiki/glossary`, `/wiki/values-and-polarities` and the emotional first
aid guide, and that is correct. The skill carries the distinction explicitly so nobody
"fixes" the wiki to match the book.

---

## What was deliberately left in the book repo

| | why |
|---|---|
| `instruments/review.py` and the other 195 | twelve steps against `manuscript/ch*.md`; none of that layout exists here |
| `marginalia/review.py` | the voice linter, keyed to marginalia membranes and chapter registers |
| `SEVEN_VOICES.md`, `HEAD_VOICE_DIAL.md`, `HEAD_REGISTERS.md` | in-world genre specs for fictional authors — see above |
| `specs/STYLE_SHEET.md` in full | the portable rows are in `reference.md` §4; the rest is about hyphenating compound modifiers in body prose |
| `EDITORIAL_OPERATING_SYSTEM.md` | about finishing a manuscript with a decision log, not about shipping copy |

If a product surface ever needs one of these, take it deliberately and adapt it, the way
`house-voice` adapts `mtgoa-review`. **Copying a book instrument into a product repo
unchanged is how you get a tool nobody runs.**

---

## Running the kit on itself

```
README.md                  clean
house-voice/SKILL.md       0 hard
house-voice/reference.md   0 hard
no-ai-slop/SKILL.md       12 hard
no-ai-slop/eval.md         3 hard
```

`no-ai-slop` does not pass this house's gate, and it is left exactly as it is. It is
somebody else's MIT-licensed work, its examples of bad writing necessarily contain the
words this house bans, and rewriting a third-party skill to satisfy a linter that was
pointed at it afterwards would be the same evasion as swapping `quiet` for `careful`.
**Exclude it, do not edit it:**

```bash
python3 tools/voice_lint.py "src/**/*.tsx" ".agents/skills/house-voice/*.md" --strict
```
