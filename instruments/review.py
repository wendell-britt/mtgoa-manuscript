# -*- coding: utf-8 -*-
"""
review.py — the repeatable pass. Run this on anything before it lands.

**Wendell 2026-07-31: "this is doing a lot of the things with the definite article and too
many 'is' and such. Do we have a repeatable review process that should be being applied
after we generate text?"**

The instruments existed. The sequence did not, so they were being run by memory and by mood,
and the one that measures exactly what he caught -- `prose_diet.py` -- **was not run once on
any prose generated in this session.** Measured after he asked:

    the book's chapters      be 0.63 to 0.82   copula 0.56 to 0.96
    ch3 Examples draft       be 1.06           copula 1.17
    the Headmaster's letter  be 1.16           copula 1.18   expletive 1.44 HEAVY
    the ch5 register         be 1.40 HEAVY                   expletive 1.89 HEAVY

The register is already in the manuscript. That is the cost of an undefined sequence, and
this file is the fix.

## The order, and why it is this order

0. **voice** -- `marginalia/review.py`, the voice linter that has been in this repo since
   2026-07-28 and whose own docstring reads *"Run BEFORE any draft is shown to Wendell."*
   It finds AI shapes, say-the-noun failures, hedges and per-Head genre markers, and it
   exits 1 on a BLOCK finding. **I did not know it existed when I wrote this file**, which
   is how the repo ended up with two `review.py`s doing adjacent jobs. This one now calls
   it rather than competing with it: `marginalia/review.py` adjudicates voice, everything
   below counts things.
1. **gate** -- banned words, sentence-initial And/But, glued em-dashes, stacks, live tokens.
   Hard fail, cheapest, and it is the only one that can catch a token reaching the
   typesetter. First because a gate failure makes everything after it moot.
2. **diet** -- be-verbs, copula openings, waste words, zombie nouns, expletives, against the
   book's own baseline. This is the one that catches heaviness, and heaviness is invisible
   one sentence at a time, which is why it needs a number.
3. **em-dash budget** -- manuscript only. Ratchets down and never up.
4. **seam** -- membrane, for anything landing above a signature.
5. **citations** -- sources, for anything naming a person or a work.
6. **round-trip** -- `compile.py --verify`, for anything touching a chapter file.
7. **the slop pass** -- `/no-ai-slop`, which is a reading rather than a measurement and
   therefore last. It is the only step this file cannot run for you.

Steps 3 to 6 are book-wide and only meaningful once the prose has landed. Steps 1, 2 and 7
apply to a draft, which is the point: **run them before it lands, not after.**

    python3 instruments/review.py FILE [FILE...]   # a draft, steps 1, 2 and a reminder
    python3 instruments/review.py                  # the whole book, all six measurable steps

**Invoked by `.claude/skills/mtgoa-review/`**, which is what makes this run after every
generation rather than when somebody remembers. The skill carries the fixes that work per
finding and the rule on registers; this file carries the sequence.
"""
import io, os, re, sys, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)
sys.path.insert(0, HERE)
from gate import COUNTERS


def run(cmd):
    p = subprocess.run([sys.executable] + cmd, cwd=ROOT,
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return p.returncode, p.stdout.decode("utf-8", "replace")


def draft(paths):
    bad = 0
    for path in paths:
        text = io.open(path, encoding="utf-8").read()
        # Drafts under marginalia/new_prose/ carry a commentary header and the prose below
        # the last horizontal rule, which is the convention ch5_memoir_move.py and
        # handbook_seat.py already read by. Scoring the header reports my own notes as
        # findings: the first run of this file flagged "quietly" and a sentence-initial
        # "And" that were both in the notes about the prose rather than in the prose.
        if "new_prose" in path and "\n---\n" in text:
            text = text.rsplit("\n---\n", 1)[1]
        print("\n%s %s" % ("=" * 4, path))

        # STEP 0 WAS MISSING FROM THIS FUNCTION UNTIL 2026-08-02, and it is the step this
        # file's own docstring lists first.
        #
        # `marginalia/review.py` owns say-the-noun, AI shapes and hedges, and its docstring
        # reads "Run BEFORE any draft is shown to Wendell." `book()` called it. `draft()`
        # never did — so the only check that catches a withheld noun ran exclusively AFTER
        # the prose had already landed in the manuscript.
        #
        # Wendell 2026-08-02, on `Froze. Said the thing.` reaching him in a draft that had
        # been reported clean: "I swear to god. We HAVE to stop using this phrasing. WE have
        # rules against this. Did you run any of the reviews? ... What do I need to do to
        # stop having to make this correction?"
        #
        # Nothing, is the answer. The rule existed, the linter fired on that exact sentence,
        # and the draft path did not call it. `MANUSCRIPT_FILE_CANON:240` records that
        # `the thing` appears 132 times in this manuscript and is the same defect
        # `review.py` reports as say-the-noun.
        #
        # A BLOCK counts here, unlike in `book()`. Book-wide it is a candidate to
        # adjudicate against prose already ruled; on a draft it means fix it before showing
        # anyone, which is what the linter's own legend says.
        code, out = run(["marginalia/review.py", path])
        nblock = len([l for l in out.split("\n") if l.strip().startswith("[BLOCK]")])
        print("  0 voice   %s" % ("clean" if not nblock else "%d BLOCK" % nblock))
        for l in out.split("\n"):
            if l.strip().startswith("say the noun:") or l.strip().startswith("hedge:") \
                    or l.strip().startswith("ai shape:"):
                print("        %s" % l.strip()[:96])
        bad += nblock

        hits = []
        for name, pat, flags in COUNTERS:
            for m in re.finditer(pat, text, flags):
                hits.append((name, " ".join(m.group(0).split())[:60]))
        if hits:
            bad += len(hits)
            print("  1 gate    %d hit(s)" % len(hits))
            for name, s in hits[:12]:
                print("        %-8s %s" % (name, s))
        else:
            print("  1 gate    clean")

        tmp = os.path.join(ROOT, ".review_body.md")
        io.open(tmp, "w", encoding="utf-8").write(text)
        code, out = run([os.path.join(HERE, "prose_diet.py"), tmp])
        out = out.replace(".review_body.md", os.path.basename(path))
        os.remove(tmp)
        row = [l for l in out.split("\n") if os.path.basename(path)[:14] in l]
        print("  2 diet    %s" % (row[0].strip() if row else "no score"))
        # Keyed on the marker prose_diet prints, not on its wording. The first version
        # matched the literal "heavy (>1.30)"; renaming that heading to "heavy:" when the
        # register ceilings landed made this silently stop firing, and review.py then
        # reported ch6's Examples clean with zombie at 1.34 and passive at 1.44.
        if "\nheavy:" in out:
            for l in out.split("\nheavy:")[1].split("\n"):
                if l.strip():
                    print("            HEAVY %s" % l.strip())
                    bad += 1
        # STEP 7 on a draft, added 2026-08-03, and it belongs here more than book-wide.
        # `specs/MANUSCRIPT_FILE_CANON.md:240` logged "`the thing` appears 132 times in this
        # manuscript" and ruled it "a candidate finder, never a gate." Wendell overruled
        # that: "we've got to solve this definite article issue once and for all. It's the
        # new AI slop issue that our passes are creating faster than we can get rid of
        # them." A finder nobody gates on is how a count sits in canon for weeks.
        code, out = run([os.path.join(HERE, "empty_head.py"), path])
        row = [l for l in out.split("\n") if os.path.basename(path)[:14] in l]
        print("  7 head    %s" % (row[0].strip() if row else "no score"))
        print("  8 slop    run /no-ai-slop by hand, then re-run this")
    return bad


def book():
    steps = [
        ("0 voice     ", ["marginalia/review.py"], None),
        ("1 gate      ", ["instruments/gate.py"], "GATE PASS"),
        ("2 diet      ", ["instruments/prose_diet.py"], None),
        ("3 em-dash   ", ["instruments/emdash.py"], "within budget"),
        ("4 seam      ", ["instruments/seam_sweep.py", "--quiet"], None),
        ("5 citations ", ["instruments/citation_audit.py"], None),
        ("6 round-trip", ["marginalia/compile.py", "--verify"], "byte-identical"),
        # Added 2026-08-03. Wendell: "we've got to solve this definite article issue once
        # and for all. It's the new AI slop issue that our passes are creating faster than
        # we can get rid of them." Reports rather than gates while the standing 266 sites
        # are worked; `empty_head.py --strict` is the promotion path.
        ("7 empty head", ["instruments/empty_head.py"], "reporting only"),
    ]
    bad = 0
    for label, cmd, want in steps:
        code, out = run(cmd)
        tail = [l for l in out.strip().split("\n") if l.strip()][-1][:66]
        # marginalia/review.py exits 1 on a BLOCK finding, which is a candidate to
        # adjudicate rather than a build failure, so it reports rather than fails.
        ok = (want in out) if want else (code == 0 or "review.py" in cmd[0])
        # DIET IS A SPECIAL CASE, and it was silently broken until 2026-08-02.
        #
        # prose_diet.py exits 0 whatever it finds — heaviness is a candidate, not a build
        # failure — so this loop marked it `ok`, and `tail` printed **only the last line of
        # the heavy block** as if that line were the summary. On the day this was found the
        # book had three heavy counters and the step reported one of them, over the word ok.
        #
        # Exactly the failure the comment forty lines up describes, in the other half of the
        # same file: `draft()` was taught to parse the heavy block and `book()` never was.
        # A step that cannot fail reads the same as a step that passed.
        if "diet" in label:
            heavy = ([l.strip() for l in out.split("\nheavy:")[1].split("\n") if l.strip()]
                     if "\nheavy:" in out else [])
            ok = not heavy
            bad += len(heavy)
            print("  %s %-4s %s" % (label, "ok" if ok else "LOOK",
                                    "%d heavy" % len(heavy) if heavy else "all counters "
                                    "within baseline"))
            for l in heavy:
                print("               HEAVY %s" % l)
            continue
        bad += 0 if ok else 1
        print("  %s %-4s %s" % (label, "ok" if ok else "LOOK", tail))
    print("\n  8 slop       run /no-ai-slop on anything written today")
    return bad


def main():
    paths = [a for a in sys.argv[1:] if not a.startswith("-")]
    print("review — %s" % ("draft" if paths else "book-wide"))
    bad = draft(paths) if paths else book()
    print("\n%s" % ("clean" if not bad else "%d thing(s) to look at" % bad))
    return 0


if __name__ == "__main__":
    sys.exit(main())
