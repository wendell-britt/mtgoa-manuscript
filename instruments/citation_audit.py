# -*- coding: utf-8 -*-
"""
The citation audit — every named source in the book, checked against Appendix G.

`AUDIT_GAME_LOOP_CONFORMANCE` §4 names this the first thing a hostile reviewer opens
with, and it is also the cheapest integrity a synthesis book can buy. Appendix G opens by
promising *"where an idea here is load-bearing, it has a lineage."* This measures whether
that promise is kept, in both directions.

Three findings, and they need different fixes:

  UNCREDITED   a person, work or term appears in the book and Appendix G does not
               carry them. This is the one with real downside.

  DEAD         Appendix G credits a source the book never uses. Not dishonest, but it
               pads the lineage and the promise above says the opposite.

  BORROWED     a term of art that belongs to a specific thinker appears in the book
               without that thinker anywhere near it. A grep cannot see an unattributed
               idea, so this list is hand-built from the sources Appendix G already
               names, plus the ones a reader would recognise. It is the only part of
               this instrument that is judgement rather than measurement, and it is
               marked so.

Surfaces: the nine chapters, the seven appendices, front and back matter. Marginalia is
stripped first -- an in-world character citing Ted Kaptchuk is a separate problem, and
`seam_sweep.py` is the instrument for that one.

    python3 instruments/citation_audit.py
    python3 instruments/citation_audit.py --quiet
"""
import io, os, re, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)
sys.path.insert(0, os.path.join(ROOT, "marginalia"))
from compile import strip_marginalia

APPENDIX_G = os.path.join(ROOT, "appendices", "ON_THE_SHOULDERS_OF.md")

# Terms of art with an owner. Left column is what to grep for; right is who it belongs to
# and must therefore appear near it, or in Appendix G at minimum.
BORROWED = [
    (r"felt sense", "Gendlin"),
    (r"polyvagal|ventral vagal|dorsal vagal", "Porges"),
    (r"somatic experiencing", "Levine"),
    (r"wu ?xing|five[- ]phase", "Kaptchuk"),
    (r"transcend and include", "Wilber"),
    (r"pre/?trans fallacy", "Wilber"),
    (r"evolutionary purpose|\bTeal\b", "Laloux"),
    (r"skilled helper", "Egan"),
    # RESTORED 2026-07-31, an hour after I removed it, and the removal was my error.
    # I read two of eighteen hits and generalised from them. ch6:122 does mock the phrase
    # as jargon, and it is the only hit that does: ch6:261 asks "where is the actual
    # leverage point", ch6:349 says "you will have a leverage point before you have a
    # channel", ch6:512 sets "the leverage point instead of the brute-force push". That is
    # Meadows's concept carrying weight, and Appendix G was right that it "runs through
    # the Architect chapter as a term of art".
    (r"leverage points?", "Meadows"),
    (r"polarity map|both/and", "Johnson"),
    # ADDED 2026-08-03 with the Maslach reversal at ch1:34. The pronoun figures are
    # the Trevor Project's and the book names them inline, which is house style for
    # an empirical citation -- ch1:32 does the same for Maslach and Gorski.
    (r"pronouns most people|attempt suicide|Trevor Project", "Trevor"),
    # ADDED 2026-08-03, ruled by Wendell. ch1:135 states the ABI model outright --
    # "Capability, integrity and benevolence, if you want the words for them" -- and
    # the audit reported 0 uncredited because it had never been told whose model it
    # is. Their word is `ability`; the book says `capability`, so both are matched.
    (r"integrity and benevolence|benevolence", "Mayer"),
    (r"big mind", "Merzel|Genpo"),   # he is credited by his teaching name in ch8
    (r"genius demon ally", "Rice"),
    (r"existential kink", "Elliott"),
    (r"finite (?:and infinite )?game|infinite game", "Carse"),
    (r"octalysis|core drives?", "Chou"),
    (r"striving play|agency as art", "Nguyen"),
    (r"identity fusion", "Gorski"),
    (r"depersonalization|inefficacy", "Maslach"),
    # Watts removed from Appendix G 2026-07-31 by Wendell's ruling, after the audit found
    # him credited as the philosophical ground of the game frame and absent from all
    # 92,000 words. Nothing to check for now, and this comment is the record.
    # Adler by way of Kishimi and Koga. The book's one non-negotiable rule -- you make the
    # move, what they do with it stays theirs -- is the separation of tasks.
    (r"separation of tasks|whose task", "Adler"),
]

# Credited in Appendix G, absent by surname, and NOT a dead credit. Each one is
# hand-checked and the reason is recorded, which is `gate.py`'s convention for a finding
# that has been measured and then judged. Anything not on this list is reported.
EXEMPT_DEAD = {
    "Kishimi": "ch3:264 quotes the book by title rather than by author, which is a "
               "citation. Added to Appendix G 2026-07-31.",
    "Koga":    "co-author of the above.",
}

# Names the audit should not report: characters, places, and the author.
# Capitalised and not people. Added 2026-08-05 after `the Sunday call` was reported as an
# uncredited source: the name pattern reads `[a-z] Sunday call` as Sunday *calling*
# something, because `calls?` matches the noun too. March, Friday and Tuesday were already
# in the book and escaped only because no cue verb happened to follow them, so this was a
# latent false positive rather than a new one.
CALENDAR = set("""Monday Tuesday Wednesday Thursday Friday Saturday Sunday
January February March April May June July August September October November December
Spring Summer Autumn Winter""".split())

FICTION = set("""Voss Ash Quill Vale Cross Orr Maera Corin Sera Irix Elian Thalen Tull Bram
Merrow Calrunia Halvane Veyra Sol Sim Orrel Jordan Wendell Britt Shaman Challenger Regent
Architect Diplomat Sage Player Forest Village Horizon Oath Bridge Pattern Line Body
Controller Protector Skeptic Victim Fixer Healer Elder Damaged Self Face Gather Resources
Skillful Organizing Direct Action Raise Awareness Vulnerable Child""".split())


def surfaces():
    """Only what ships. `appendices/` also holds retired files and dated backups, and
    auditing those reports problems in pages no reader will ever see."""
    sys.path.insert(0, HERE)
    from build_book import SPINE
    out = []
    for _, _, rel, _ in [s for s in SPINE if s[2]]:
        p = os.path.join(ROOT, rel)
        if not os.path.exists(p) or os.path.abspath(p) == os.path.abspath(APPENDIX_G):
            continue
        out.append((rel, strip_marginalia(io.open(p, encoding="utf-8").read())))
    return out


def credited():
    """Every surname Appendix G names, in bold or in prose."""
    g = io.open(APPENDIX_G, encoding="utf-8").read()
    names = set()
    for m in re.finditer(r"\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\b", g):
        for part in m.group(1).split():
            names.add(part)
    return names, g


def main():
    quiet = "--quiet" in sys.argv
    names, g = credited()
    docs = surfaces()

    uncredited, borrowed = {}, {}
    for rel, text in docs:
        # Two shapes, both requiring evidence that this is a person rather than a
        # capitalised noun at the head of a sentence.
        #
        #   1. a full name, First Last, anywhere
        #   2. a lone surname MID-SENTENCE next to a claim verb, which is how the
        #      chapters cite on second reference
        #
        # The first version of this check allowed sentence-initial matches and reported
        # forty capitalised common nouns -- Accuracy, Nobody, Each, Opening.
        hits = []
        # `\s+` used to match newlines, so a heading's last word ran into the next
        # paragraph's first: "## Which Game Are You Playing" above "Somebody found me..."
        # was read as a person called Playing Somebody who *found* something. Names do not
        # span line breaks, and the manuscript does not wrap inside a paragraph, so the
        # separators are now horizontal whitespace only. Fixed 2026-08-05.
        for m in re.finditer(r"\b([A-Z][a-z]{2,}[^\S\n]+(?:[A-Z]\.[^\S\n]+)?[A-Z][a-z]{2,})(?:'s)?[^\S\n]+"
                             r"(?:calls?|names?|argues?|writes?|showed?|shows?|found|"
                             r"separates?|explains?|puts? it|research|work|finding|term|"
                             r"insight|distinction|makes? the)\b", text):
            hits.append((m.group(1), m.group(0)))
        for m in re.finditer(r"[a-z,][^\S\n]+([A-Z][a-z]{3,})(?:'s)?[^\S\n]+"
                             r"(?:calls?|names?|argues?|writes?|showed?|shows?|found|"
                             r"separates?|explains?|puts? it|research|finding|"
                             r"insight|distinction)\b", text):
            hits.append((m.group(1), m.group(0)))
        # Italicised book titles. This is the check that would have caught *The Courage
        # to Be Disliked*, which the name pass cannot see: ch3 quotes a specific claim
        # from it and Appendix G has no entry, so the title is the only evidence.
        #
        # A title alone is not enough, because the book italicises its own Move names and
        # chapter subtitles in exactly the same way. The discriminator is a citation cue
        # within a clause of it -- somebody quoting, attributing, or reporting a claim.
        # These are kept out of `hits` because the person-name filter below would eat
        # them: `names` holds every capitalised token in Appendix G, "The" included.
        for m in re.finditer(r"(?<!\*)\*((?:The |A |An )[A-Z][A-Za-z]+"
                             r"(?:\s+(?:of|to|the|a|an|and|in|no|that|has|your|"
                             r"[A-Z][A-Za-z]+)){2,})\*(?!\*)"
                             r"(?P<after>.{0,70})", text, re.S):
            title = m.group(1)
            if re.search(re.escape(title), g, re.I):
                continue
            if not re.search(r"\bhas a line\b|\bwrites?\b|\bargues?\b|\bcalls? it\b|"
                             r"\bputs? it\b|\bby [A-Z]|\bsays?\b|\bnames?\b|"
                             r"\bthere is a\b|\bquot", m.group("after")):
                continue
            uncredited.setdefault(title, []).append(
                (rel, " ".join((m.group(1) + m.group("after")).split())[:90]))

        for full, ctx in hits:
            parts = [w for w in full.split() if not w.endswith(".")]
            if (any(w in FICTION for w in parts) or any(w in names for w in parts)
                    or any(w in CALENDAR for w in parts)):
                continue
            uncredited.setdefault(full, []).append((rel, " ".join(ctx.split())))

    for rel, text in docs:
        for pat, owner in BORROWED:
            for m in re.finditer(pat, text, re.I):
                a, b = max(0, m.start() - 400), m.end() + 400
                if re.search(r"\b%s\b" % owner, text[a:b]):
                    continue
                borrowed.setdefault((owner, m.group(0).lower()), []).append(rel)

    # DEAD means the book uses NEITHER the person's name NOR their term of art NOR their
    # title. The first version checked the surname alone and reported six, four of them
    # wrongly: Appendix G exists precisely to credit sources the chapters do not name, and
    # it says so in its own opening. Gendlin is credited and "felt sense" is used eight
    # times; Johnson is credited and the polarity map runs through four files; Kishimi is
    # credited and ch3 quotes the book by title. None of those is a dead credit.
    dead = []
    body = "\n".join(t for _, t in docs)
    owned = {}
    for pat, owner in BORROWED:
        owned.setdefault(owner, []).append(pat)
    for m in re.finditer(r"\*\*([A-Z][a-z]+(?:\s+[A-Z]\.?)?(?:\s+[A-Z][a-z]+)+?)"
                         r"(?:'s)?\*?\*?\s*(?:\(|—|\*|is|and)", g):
        full = m.group(1)
        surname = full.split()[-1]
        if re.search(r"\b%s\b" % surname, body):
            continue
        if any(re.search(pat, body, re.I) for pat in owned.get(surname, [])):
            continue
        if surname in EXEMPT_DEAD:
            continue
        dead.append((full, surname))

    print("=" * 78)
    print("UNCREDITED — named in the book, absent from Appendix G")
    print("=" * 78)
    if not uncredited:
        print("  none")
    for n in sorted(uncredited):
        print("\n  %s" % n)
        for rel, ctx in uncredited[n][:4]:
            print("      %-28s %s" % (rel, ctx))

    print("\n" + "=" * 78)
    print("BORROWED — a term of art with no owner within 400 characters (judgement)")
    print("=" * 78)
    if not borrowed:
        print("  none")
    for (owner, term) in sorted(borrowed):
        where = borrowed[(owner, term)]
        print("  %-12s %-24s %d hit(s)  %s"
              % (owner, term, len(where), ", ".join(sorted(set(where))[:4])))

    print("\n" + "=" * 78)
    print("DEAD — credited in Appendix G, never used in the book")
    print("=" * 78)
    print("  none" if not dead else "")
    for full, surname in dead:
        print("  %s" % full)

    total = len(uncredited) + len(borrowed) + len(dead)
    print("\n%d finding(s): %d uncredited, %d borrowed, %d dead."
          % (total, len(uncredited), len(borrowed), len(dead)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
