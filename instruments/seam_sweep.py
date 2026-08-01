# -*- coding: utf-8 -*-
"""
The seam sweep — find every sentence in a treatise that only Wendell could have written.

Under `specs/SPEC_TWO_HANDS_2026-07-30.md`, Sections 1-3 of ch3-ch8 are the Head's
treatise, signed at the close of Section 3. Sections 4-7 are Wendell Britt on allyship.
Nothing may cross the membrane. This finds what already does.

Three tiers, because they need different fixes:

  T1 BOOK   the Head cannot know they are inside a book. Chapter cross-references,
            appendix pointers, "this chapter", forward pointers. Impossible, not
            merely awkward -- no amount of worldbuilding fixes it.

  T2 AUTHOR the author's own life and work. bars-engine, his other titles, the
            writing of this book. Impossible for the same reason and worse.

  T3 CREDIT real-world attribution. Wendell ruled 2026-07-30 that traffic between
            the worlds is ordinary, so a Head *could* know these -- but credit
            belongs to the author rather than to a character. Ted Kaptchuk should
            be thanked by Wendell Britt, not by Maera Voss. So these move, on
            grounds of attribution rather than possibility.

What is deliberately NOT flagged: ordinary Earth-world vocabulary and scenes --
meetings, email, offices, therapy. Before the Earth-travel ruling those were
suspect. They are not any more, and the count of them is reported so the size of
what is being left alone is visible rather than assumed.

Line labels: `L` is a file line in Sections 1-3. `HB` is a line inside that school's
handbook, which lives in `marginalia/insertions.py` and has no stable file line until the
frame is applied.

**Why ch1, ch2 and ch9 are not in CHAPTERS.** They are Wendell's frame: `SPEC_DL19` ruled
that his real biography has exactly one legal home and this is it. A frame chapter has no
seam because it has no fictional author, so there is no membrane for a sentence to cross.

That was true of ch1 and ch9 from the start and became true of ch2 only on 2026-08-01.
Until then ch2 carried `set down by Bram Tull, Caretaker` at the top of the chapter -- the
last top-of-chapter byline in the book, in the configuration `SPEC_TWO_HANDS` condemned as
overclaiming -- while this sweep was hardcoded to skip it. Running these same three tiers
over ch2 that day returned **BOOK 28, AUTHOR 13, CREDIT 2**, against 2/37/0 for all six
cleaned treatises combined: the George Floyd origin story, the book naming itself at
ch2:241, and credits to Carolyn Elliott, Robin Rice and Gerard Egan, all under a fictional
caretaker's signature.

**None of those 43 sites was edited.** Bram was removed instead, and they became legal in
place. That is the shape of the fix to reach for when this sweep fires on a frame chapter:
ask who is signing, before asking what the sentence says. See
`specs/SPEC_CH2_FRAME_2026-08-01.md`.

One consequence worth knowing if you extend this: ch2 no longer round-trips through
`compile.py`, because it left `CHAPTERS` there too. Running this under `on_body.py` is
still correct -- ch2 simply has no frame to strip.

**The total moved 28 to 42 on 2026-07-30** when the six handbooks came under the sweep for
the first time. Nothing was added to the treatises; 2,027 words that had never been measured
started being measured. Twelve of the fourteen are AUTHOR hits on Heads narrating their own
lives in clause 6, which is what clause 6 is for and what this tier over-reports by design.
The two BOOK hits are both *what follows* pointing at the rest of the handbook rather than at
the rest of the book, which a bounded document is entitled to do.

Run through on_body.py so the marginalia frame is stripped and restored:

    python3 instruments/on_body.py 'python3 instruments/seam_sweep.py'
    python3 instruments/on_body.py 'python3 instruments/seam_sweep.py --quiet'
"""
import io, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")
sys.path.insert(0, os.path.join(HERE, os.pardir, "marginalia"))
# The handbooks are Head prose too, and they sit ABOVE Section 1, so the Section 1 to
# Section 4 bracket below never sees them -- SPEC_SCHOOL_HANDBOOKS §11 called this out
# before they were written. Reading them from `insertions` rather than from the page makes
# the sweep independent of whether the marginalia frame is currently applied, which matters
# because this runs both ways: directly, and under `on_body.py` on stripped text.
from insertions import HANDBOOK

# The six treatise chapters, and deliberately not ch1/ch2/ch9 -- see the docstring.
# Adding a frame chapter here reports the author's own frame as a breach.
CHAPTERS = [3, 4, 5, 6, 7, 8]
HEAD = {3: "Maera Voss", 4: "Corin Ash", 5: "Sera Quill",
        6: "Irix Vale", 7: "Elian Cross", 8: "Thalen Orr"}

T1 = ("BOOK", re.compile(
    # Widened 2026-07-30: the first version keyed on "this chapter" and missed
    # "the whole chapter", "the chapter", "the reader", "the ideal reader". Any
    # determiner in front of chapter/section/book is the same breach.
    r"\b(?:this|the|that|a|each|every|whole)\s+(?:whole\s+)?(?:book|chapter|section)\b"
    r"|\bChapters?\s+\d|\bAppendi(?:x|ces)\b|\bearlier in\b|\blater in\b"
    r"|\bthe (?:ideal )?reader\b|\bpart (?:one|two|three) of\b"
    r"|\bwhat follows\b|\bby the end of the book\b", re.I))

# WIDENED 2026-07-30 after Wendell asked whether I had read ch3 or only grepped it.
# I had only grepped it. The first version keyed on named artifacts -- bars-engine, the
# other title -- and so reported AUTHOR: 0 across all six chapters while ch3:91-107 sat
# there carrying Wendell's customer-service years, a real book he read, and a game he
# invented. A tier that only catches proper nouns cannot see a memoir.
#
# So this now catches the shape instead: first-person past-tense narration of a life.
# It over-reports by design, because a Head's own biography in clause 6 looks identical
# from the outside and the difference is a judgment only a reader can make.
T2 = ("AUTHOR", re.compile(
    r"bars-engine|Igniting Joy|\bthis manuscript\b"
    r"|\bI (?:used to|eventually|had to|kept|spent|quit|built|invented|wrote|threw out|"
    r"started|learned|remember|would|was|am|have been|took|converted|stayed|said)\b"
    r"|\bI'?d\b|\bI'?ve\b|\bI'?m\b|\bmy (?:book|chest|own|father|mother|life|career|phone)\b"
    r"|\bwhen I started building\b", re.I))

# Real-world names and systems. Every one of these is checked against the repo's own
# source appendix rather than guessed at.
T3 = ("CREDIT", re.compile(
    r"wu xing|五行|Chinese|Kaptchuk|Wilber|\bIntegral\b|Spiral Dynamics|\bGraves\b|\bBeck\b"
    r"|\bEgan\b|Maslach|Meadows|Barry Johnson|Gorski|Yu-kai|\bChou\b|Octalysis"
    r"|Alan Watts|\bCarse\b|Robin Rice|Wilberian|Courage to Be Disliked|Kishimi|Adler", re.I))

# Reported, never flagged: the Earth-world texture the 2026-07-30 ruling permits.
EARTH = re.compile(r"\bmeeting\b|\bemail\b|\bSlack\b|\boffice\b|\bmanager\b|\bteam\b"
                   r"|\btherapy\b|\bHR\b|\bcalendar\b|\bproject\b", re.I)

SENT = re.compile(r'(?<=[.!?])["”’\')]?\s+(?=[A-Z"“\'(*])')


def sections_1_to_3(text):
    """Section 1 up to the treatise signature, minus any `## A Note Before …` block.

    Those Notes are Wendell stepping in under his own heading, which is the
    convention this spec was reaching for and which the book already runs in ch6
    and ch8. They are not membrane breaches, so counting them as such would
    overstate the problem by about a third.
    """
    lines = text.split("\n")
    i = next((k for k, l in enumerate(lines) if l.startswith("## Section 1")), None)
    j = next((k for k, l in enumerate(lines) if l.startswith("## Section 4")), None)
    if i is None or j is None:
        raise SystemExit("could not bracket the treatise")
    # The treatise ends at its signature, and marginalia/compile.py puts that above
    # any trailing italic apparatus at the foot of Section 3. This sweep runs on
    # stripped body text, where the signature block does not exist, so it recomputes
    # the same boundary by the same rule. Both must agree or the sweep will report
    # lines that are already on the author's side of the seam.
    while j > i and (not lines[j - 1].strip()
                     or lines[j - 1].strip() in ("---",)
                     or (lines[j - 1].strip().startswith("*")
                         and lines[j - 1].strip().endswith("*")
                         and not lines[j - 1].strip().startswith("**"))):
        j -= 1
    out, keep = [], True
    for k in range(i, j):
        if lines[k].startswith("## "):
            keep = not lines[k].startswith("## A Note Before")
        out.append(lines[k] if keep else "")
    return out, i + 1


def main():
    quiet = "--quiet" in sys.argv
    totals = {"BOOK": 0, "AUTHOR": 0, "CREDIT": 0}
    per_ch = {}

    for n in CHAPTERS:
        path = os.path.join(MS, "ch%d.md" % n)
        lines, offset = sections_1_to_3(io.open(path, encoding="utf-8").read())
        # Two regions of Head prose, swept identically. The handbook is labelled HB
        # because it has no stable file line: it lives in insertions.py and lands on the
        # page only once the frame is applied.
        regions = [("HB", HANDBOOK[n].split("\n"), 1)] if n in HANDBOOK else []
        regions.append(("L", lines, offset))

        hits, earth, scanned = [], 0, 0
        for label, region, base in regions:
            scanned += len(region)
            for k, line in enumerate(region):
                s = line.strip()
                # Headings, rules, tables and the exercise prompts are apparatus, not
                # the Head's prose. A heading is the book's furniture in every book.
                if not s or s.startswith(("#", "|", "---", ">", "<!--", "*[")):
                    continue
                for sent in SENT.split(s):
                    sent = sent.strip()
                    if len(sent.split()) < 3:
                        continue
                    if EARTH.search(sent):
                        earth += 1
                    for tier, pat in (T1, T2, T3):
                        m = pat.search(sent)
                        if m:
                            hits.append(("%s%d" % (label, base + k),
                                         tier, m.group(0), sent))
                            totals[tier] += 1
                            break
        per_ch[n] = (hits, earth, scanned)
        if not quiet and hits:
            print("\n%s ch%d  ·  %s  %s" % ("=" * 4, n, HEAD[n], "=" * 40))
            for ln, tier, tok, sent in hits:
                body = sent if len(sent) <= 175 else sent[:172] + "..."
                print("  %-6s %-6s [%s]  %s" % (tier, ln, tok, body))

    print("\n" + "=" * 78)
    print("%-6s %-14s %6s %6s %6s %7s   %s" %
          ("ch", "Head", "BOOK", "AUTHOR", "CREDIT", "total", "Earth-texture (allowed)"))
    print("-" * 78)
    grand = 0
    for n in CHAPTERS:
        hits, earth, _ = per_ch[n]
        c = {"BOOK": 0, "AUTHOR": 0, "CREDIT": 0}
        for _, tier, _, _ in hits:
            c[tier] += 1
        grand += len(hits)
        print("%-6d %-14s %6d %6d %6d %7d   %d" %
              (n, HEAD[n], c["BOOK"], c["AUTHOR"], c["CREDIT"], len(hits), earth))
    print("-" * 78)
    print("%-21s %6d %6d %6d %7d" %
          ("TOTAL", totals["BOOK"], totals["AUTHOR"], totals["CREDIT"], grand))
    print("\nBOOK and AUTHOR are impossible for a Head and must move below the seam.")
    print("CREDIT is possible since the Earth-travel ruling, and moves anyway:")
    print("attribution belongs to the author, not to a character.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
