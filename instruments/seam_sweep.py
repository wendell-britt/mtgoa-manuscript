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

Run through on_body.py so the marginalia frame is stripped and restored:

    python3 instruments/on_body.py 'python3 instruments/seam_sweep.py'
    python3 instruments/on_body.py 'python3 instruments/seam_sweep.py --quiet'
"""
import io, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")
CHAPTERS = [3, 4, 5, 6, 7, 8]
HEAD = {3: "Maera Voss", 4: "Corin Ash", 5: "Sera Quill",
        6: "Irix Vale", 7: "Elian Cross", 8: "Thalen Orr"}

T1 = ("BOOK", re.compile(
    r"\bthis book\b|\bthe book\b|\bChapter\s+\d|\bChapters\s+\d|\bthis chapter\b"
    r"|\bthe (?:next|last|previous|coming) chapter\b|\bAppendi(?:x|ces)\b"
    r"|\bearlier in\b|\blater in\b|\bthe rest of the chapter\b|\bthis section\b"
    r"|\bpart (?:one|two|three) of\b|\bwhat follows\b|\bby the end of the book\b", re.I))

T2 = ("AUTHOR", re.compile(
    r"bars-engine|Igniting Joy|\bI wrote\b|\bmy book\b|\bthis manuscript\b"
    r"|\bI threw out\b|\bwhen I started building\b", re.I))

# Real-world names and systems. Every one of these is checked against the repo's own
# source appendix rather than guessed at.
T3 = ("CREDIT", re.compile(
    r"wu xing|五行|Chinese|Kaptchuk|Wilber|\bIntegral\b|Spiral Dynamics|\bGraves\b|\bBeck\b"
    r"|\bEgan\b|Maslach|Meadows|Barry Johnson|Gorski|Yu-kai|\bChou\b|Octalysis"
    r"|Alan Watts|\bCarse\b|Robin Rice|Wilberian", re.I))

# Reported, never flagged: the Earth-world texture the 2026-07-30 ruling permits.
EARTH = re.compile(r"\bmeeting\b|\bemail\b|\bSlack\b|\boffice\b|\bmanager\b|\bteam\b"
                   r"|\btherapy\b|\bHR\b|\bcalendar\b|\bproject\b", re.I)

SENT = re.compile(r'(?<=[.!?])["”’\')]?\s+(?=[A-Z"“\'(*])')


def sections_1_to_3(text):
    """Section 1 up to Section 4, minus any `## A Note Before …` block.

    Those Notes are Wendell stepping in under his own heading, which is the
    convention this spec was reaching for and which the book already runs in ch6
    and ch8. They are not membrane breaches, so counting them as such would
    overstate the problem by about a third.
    """
    lines = text.split("\n")
    i = next((k for k, l in enumerate(lines) if l.startswith("## Section 1")), None)
    j = next((k for k, l in enumerate(lines) if l.startswith("## Section 4")), None)
    if i is None or j is None:
        raise SystemExit("could not bracket Sections 1-3")
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
        hits, earth = [], 0
        for k, line in enumerate(lines):
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
                        hits.append((offset + k, tier, m.group(0), sent))
                        totals[tier] += 1
                        break
        per_ch[n] = (hits, earth, len(lines))
        if not quiet and hits:
            print("\n%s ch%d  ·  %s  %s" % ("=" * 4, n, HEAD[n], "=" * 40))
            for ln, tier, tok, sent in hits:
                body = sent if len(sent) <= 175 else sent[:172] + "..."
                print("  %-6s L%-5d [%s]  %s" % (tier, ln, tok, body))

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
