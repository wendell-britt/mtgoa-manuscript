# -*- coding: utf-8 -*-
"""
index_build.py -- the back-matter index, generated from the book rather than typed.

Wendell 2026-08-05: *"an index would be useful."* It is the last of the four back-matter
components the spine never listed, and the only one that cannot be written by hand
without going stale the first time a section moves.

------------------------------------------------------------------ what a locator is

A print index points at page numbers. This book has no pages yet -- it is markdown until
a typesetter touches it -- so the locator here is **chapter and section**, which is the
one address that survives typesetting. At print the compositor substitutes pages; in the
ebook the section reference is more useful than a page number would have been, because
an ebook reader has no fixed pages to point at.

    Ch 3 §4        chapter 3, Section 4
    Ch 1           a chapter with no section headings (ch1 has none)
    App F          an appendix
    Copyright      front or back matter, by its spine label

------------------------------------------------------------------ the term list

Curated, not extracted. An index built by frequency is a concordance, and a concordance
of a 123,000-word practice book is noise -- *the field* alone would run to three hundred
locators. What earns an entry here is vocabulary the book **coins or borrows and then
uses as equipment**: the Faces, the daemons, the channels and their completed states,
the named moves, the practices, the schools, the domains, and the sources whose terms of
art the book runs on.

Two rules keep it honest, and both abort the build rather than emitting something wrong:

  1. **No entry without a hit.** A term in this list that appears nowhere in the book is
     a fabricated index entry, which is worse than a missing one -- it sends a reader to
     a page that has nothing on it. The build fails and names the term.

  2. **No primary without a hit at that locator.** `PRIMARY` records where a term is
     taught, which is the one piece of judgement in this file. If a section moves and the
     recorded primary no longer holds the term, the build fails rather than pointing the
     reader at the wrong section.

Rule 1 caught `The Game So Far` on the first run, which `SPEC_REPETITION_AND_CUTS.md:140`
had already found absent from all nine chapters. A project glossary listed it as a
recurring element with seven instances. It has none, and an index would have been the
fourth document to assert it exists.

------------------------------------------------------------------------- saturation

A term in more than SATURATED surfaces gets its primary locator and the word *throughout*
rather than a list of nine chapters. `the field` is in every chapter; printing that fact
nine times is not a finding, and an index entry a reader cannot act on is shelf-weight.

    python3 instruments/index_build.py            # write back_matter/index.md
    python3 instruments/index_build.py --dry      # report only, write nothing
    python3 instruments/index_build.py --check    # exit 1 if the file on disk is stale
"""
import io, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, os.pardir))
sys.path.insert(0, os.path.join(ROOT, "marginalia"))
sys.path.insert(0, HERE)
from compile import strip_marginalia

OUT = os.path.join(ROOT, "back_matter", "index.md")
SATURATED = 8   # locators, not files -- see build()

# ---------------------------------------------------------------- the term list
# (display form, regex). The regex is what gets searched; the display form is what a
# reader sees. Case-insensitive throughout, because the book capitalises a Face at the
# head of a sentence and mid-sentence alike.
TERMS = {
    "The six Faces": [
        ("Shaman",     r"\bShamans?\b"),
        ("Challenger", r"\bChallengers?\b"),
        ("Regent",     r"\bRegents?\b"),
        ("Architect",  r"\bArchitects?\b"),
        ("Diplomat",   r"\bDiplomats?\b"),
        ("Sage",       r"\bSages?\b"),
        ("Player, the", r"\bthe Player\b"),
    ],
    "The daemons": [
        ("Protector",      r"\bProtector\b"),
        ("Controller",     r"\bController\b"),
        ("Skeptic",        r"\bSkeptic\b"),
        ("Fixer/Healer",   r"\bFixer\b|\bHealer\b"),
        ("Emotional Body", r"\bEmotional Body\b"),
        ("Victim",         r"\bVictim\b"),
        ("Damaged Self",   r"\bDamaged Self\b"),
        ("shadow, the",    r"\bthe shadow\b"),
        # Not an eighth daemon -- ch2:384 makes her the Player at the centre. Missing
        # from both index and glossary until 2026-08-05, which is why check 3 could not
        # see the gap: it can only require an entry for a term the index already knows.
        ("Vulnerable Child", r"Vulnerable Child"),
    ],
    "The five channels": [
        ("Metal / fear",        r"\bMetal\b"),
        ("Water / sadness",     r"\bWater\b"),
        ("Wood / joy",          r"\bWood\b"),
        ("Fire / anger",        r"\bFire\b"),
        ("Earth / neutrality",  r"\bEarth\b"),
        ("wonder (fear completed)",      r"\bwonder\b"),
        ("poignance (sadness completed)", r"\bpoignance\b"),
        ("triumph (anger completed)",    r"\btriumph\b"),
        ("bliss (joy completed)",        r"\bbliss\b"),
        ("peace (neutrality completed)", r"\bpeace\b"),
    ],
    "Practices": [
        ("Five-Move Form",      r"Five.Move Form"),
        # Case-sensitive, scoped: the build compiles every pattern with re.I, and `wave`
        # is an ordinary English verb. ch1:175 -- "makes serious people wave the whole
        # idea away" -- was indexed as the breath practice on the first run after the
        # rename. Rule 1 cannot see it: the term does have hits, they are the wrong word.
        ("WAVE",                r"(?-i:\bWAVE\b)"),
        ("Wake Up",             r"\bWake Up\b"),
        ("Open Up",             r"\bOpen Up\b"),
        ("Clean Up",            r"\bClean Up\b"),
        ("Grow Up",             r"\bGrow Up\b"),
        ("Show Up",             r"\bShow Up\b"),
        ("BAR",                 r"\bBARs?\b"),
        ("3-2-1 Shadow Process", r"3.?2.?1\b"),
        ("Polarity Map",        r"[Pp]olarity [Mm]ap"),
        ("quest",               r"\bquests?\b"),
        ("campaign",            r"\bcampaigns?\b"),
    ],
    "Game moves": [
        ("Catch It Before the Story",   r"Catch It Before the Story"),
        ("Turn the Dial Up",            r"Turn the Dial Up"),
        ("Name the Channel Out Loud",   r"Name the Channel Out Loud"),
        ("Say What You Can Do Now",     r"Say What You Can Do Now"),
        ("Say the Unsaid Charge", r"Say the [Uu]nsaid [Cc]harge"),
        ("Find What You Keep Defending", r"Find What You Keep Defending"),
        ("Name the Unnameable",         r"Name the Unnameable"),
        ("Draw the Line",               r"Draw the Line"),
        ("Take the Full Charge",        r"Take the Full Charge"),
        ("Confront Without Cruelty",    r"Confront Without Cruelty"),
        # ch5-ch8 owned twenty moves that no reader could look up. The list was
        # hard-coded at ten, all from ch3 and ch4, and ch9:662 sends the reader after
        # three of ch7's by name. Added 2026-08-11 after the nine-reader deep read.
        ("Name the Inheritance",        r"Name the Inheritance"),
        ("Honor What Still Serves",     r"Honor What Still Serves"),
        ("Keep the Vows",               r"Keep the Vows"),
        ("Reform Without Erasing",      r"Reform Without Erasing"),
        ("Entrust Without Clinging",    r"Entrust Without Clinging"),
        ("Find the Leverage Point",     r"Find the Leverage Point"),
        ("Name the Unstated Assumption", r"Name the Unstated Assumption"),
        ("Design for Handoff",          r"Design for Handoff"),
        ("Ship the Minimum",            r"Ship the Minimum"),
        ("Refactor Kindly",             r"Refactor Kindly"),
        ("Name the Field",              r"Name the Field"),
        ("Translate Across Camps",      r"Translate Across Camps"),
        ("Close with Honest Terms",     r"Close with Honest Terms"),
        ("Repair After Rupture",        r"Repair After Rupture"),
        ("Refuse False Equivalence",    r"Refuse False Equivalence"),
        ("Name the Game",               r"Name the Game"),
        ("Switch Games Deliberately",   r"Switch Games Deliberately"),
        ("Return Without Condescension", r"Return Without Condescension"),
        ("Put a Game Down",             r"Put a Game Down"),
        ("Hold the Meta Without Losing the Ground", r"Hold the Meta Without Losing the Ground"),
    ],
    "The world": [
        ("Infinite Arcade",  r"Infinite Arcade"),
        ("Forest, the",      r"\bthe Forest\b"),
        ("village, the",     r"\bthe villagers?\b|\bthe village\b"),
        ("School of the Body",    r"School of the Body"),
        ("School of the Line",    r"School of the Line"),
        ("School of the Oath",    r"School of the Oath"),
        ("School of the Pattern", r"School of the Pattern"),
        ("School of the Bridge",  r"School of the Bridge"),
        ("School of the Horizon", r"School of the Horizon"),
    ],
    "The four domains": [
        ("Gather Resources",   r"Gather(?:ing)? Resources"),
        ("Raise Awareness",    r"Rais(?:e|ing) Awareness"),
        ("Direct Action",      r"Direct Action"),
        ("Skillful Organizing", r"Skillful Organizing"),
    ],
    "Concepts": [
        ("altitude",             r"\baltitudes?\b"),
        ("charge, the",          r"\bthe charge\b"),
        # Coined in ch2 §7's second walk, ported 2026-08-05. Four uses, all there.
        ("clearance",            r"\bclearance\b"),
        ("field, the",           r"\bthe field\b"),
        ("felt sense",           r"felt sense"),
        ("existential kink",     r"existential kink"),
        ("leverage point",       r"leverage points?"),
        ("evolutionary purpose", r"evolutionary purpose"),
        ("pre/trans fallacy",    r"pre.?trans fallacy"),
        ("transcend and include", r"transcend.and.include"),
        ("renewable fuel",       r"renewable"),
        ("separation of tasks",  r"separation of tasks|whose task"),
    ],
    "Sources": [
        ("Adler, Alfred",       r"\bAdler\b"),
        ("Carse, James",        r"\bCarse\b"),
        ("Chou, Yu-kai",        r"\bChou\b"),
        ("Egan, Gerard",        r"\bEgan\b"),
        ("Elliott, Carolyn",    r"\bElliott\b"),
        ("Gendlin, Eugene",     r"\bGendlin\b"),
        ("Johnson, Barry",      r"\bJohnson\b"),
        ("Kaptchuk, Ted",       r"\bKaptchuk\b"),
        ("Laloux, Frederic",    r"\bLaloux\b"),
        ("Levine, Peter",       r"\bLevine\b"),
        ("Meadows, Donella",    r"\bMeadows\b"),
        ("Merzel, Dennis Genpo", r"\bMerzel\b|\bGenpo\b"),
        ("Nguyen, C. Thi",      r"\bNguyen\b"),
        ("Porges, Stephen",     r"\bPorges\b"),
        ("Rice, Robin",         r"\bRobin Rice\b"),
        ("Wilber, Ken",         r"\bWilber\b"),
    ],
}

# Where a term is TAUGHT, as opposed to used. The one piece of judgement in this file, so
# every entry is checked against the text at build time and a stale one fails the build.
PRIMARY = {
    # the Faces, each in its own chapter
    "Shaman": "Ch 3", "Challenger": "Ch 4", "Regent": "Ch 5",
    "Architect": "Ch 6", "Diplomat": "Ch 7", "Sage": "Ch 8",
    "Player, the": "Ch 2 §6",
    # the daemons, all seven introduced in one roster
    "Protector": "Ch 2 §6", "Controller": "Ch 2 §6", "Skeptic": "Ch 2 §6",
    "Fixer/Healer": "Ch 2 §6", "Emotional Body": "Ch 2 §6", "Victim": "Ch 2 §6",
    "Damaged Self": "Ch 2 §6", "shadow, the": "Ch 1",
    # the channels and the states they complete into
    "Metal / fear": "Ch 3 §4", "Water / sadness": "Ch 3 §4", "Wood / joy": "Ch 3 §4",
    "Fire / anger": "Ch 3 §4", "Earth / neutrality": "Ch 3 §4",
    "wonder (fear completed)": "Ch 3 §4", "poignance (sadness completed)": "Ch 3 §4",
    "triumph (anger completed)": "Ch 3 §4", "bliss (joy completed)": "Ch 3 §4",
    "peace (neutrality completed)": "Ch 3 §4",
    # practices
    "BAR": "Ch 2 §9", "Polarity Map": "Ch 3 §4",
    # Two practices, two names, ruled 2026-08-07 in SPEC_WAVE_RENAME. One regex used to
    # catch both and file them under `WAVE-Spiral`, which is how a half-finished rename
    # survived four chapters, an appendix, a glossary and this file.
    "Five-Move Form": "Ch 3 §4", "WAVE": "Ch 3 §4",
    "3-2-1 Shadow Process": "App E",
    # The five Ups are the MOVE names in §6, not the stage names in §4 -- §4 runs them
    # bare (Stage 1: Wake, Stage 2: Open). Recorded here because the first draft sent all
    # five to §4 and the build refused, which is the check doing its job on my judgement
    # rather than on the book.
    "Wake Up": "Ch 3 §6", "Open Up": "Ch 3 §6", "Clean Up": "Ch 3 §6",
    "Grow Up": "Ch 3 §6", "Show Up": "Ch 3 §6",
    "quest": "App B", "campaign": "App B",
    # the world
    "Infinite Arcade": "Ch 1", "Forest, the": "Ch 2 §3",
    "School of the Body": "Ch 3", "School of the Line": "Ch 4",
    "School of the Oath": "Ch 5", "School of the Pattern": "Ch 6",
    "School of the Bridge": "Ch 7", "School of the Horizon": "Ch 8",
    # domains
    "Gather Resources": "App A", "Raise Awareness": "App A",
    "Direct Action": "App A", "Skillful Organizing": "App A",
    # concepts
    "felt sense": "Ch 3 §4", "leverage point": "Ch 6 §4",
    "evolutionary purpose": "Ch 8 §4", "existential kink": "Ch 1",
    # Defined in the Second Walk -- "That distance is your clearance, and it is the only
    # currency on this side of the floor" -- then spent once per chapter after it.
    "clearance": "Ch 2 §7",
    "pre/trans fallacy": "Author's note",
}


def locator(label, rel, text, pos):
    """Chapter and section for an offset, or the spine label for matter with no sections."""
    m = re.match(r"Chapter (\d+)", label)
    stem = "Ch %s" % m.group(1) if m else None
    if not stem:
        m = re.match(r"Appendix ([A-G])", label)
        stem = "App %s" % m.group(1) if m else label
    sec = None
    for h in re.finditer(r"^## Section (\d+)", text, re.M):
        if h.start() > pos:
            break
        sec = h.group(1)
    return "%s §%s" % (stem, sec) if sec else stem


def order(loc):
    """Front matter, then chapters in number order, then appendices, then back."""
    m = re.match(r"Ch (\d+)(?: §(\d+))?", loc)
    if m:
        return (1, int(m.group(1)), int(m.group(2) or 0), "")
    m = re.match(r"App ([A-G])", loc)
    if m:
        return (2, 0, 0, m.group(1))
    return (0, 0, 0, loc)


def surfaces():
    """The printed page, marginalia INCLUDED.

    Every other instrument here strips marginalia first, because an in-world character
    citing Ted Kaptchuk is not the author citing him and an attribution audit has to know
    the difference. An index is the one instrument where that reasoning inverts: it points
    at what a reader can find, the margin notes are printed -- `build_book` applies 47
    blocks -- and a reader looking up a term does not care which voice said it.

    Stripping them first made the build abort on `School of the Line`, and the abort was
    right about the book and wrong about the index. All five mentions of the Challenger's
    school live in margin notes; the body text names it zero times, against Body 8,
    Pattern 4, Bridge 4, Horizon 3, Oath 1. That asymmetry is a real finding and it is
    recorded here, but it is a question about ch4's prose rather than a reason to leave a
    school out of the index of a book that prints its name five times.
    """
    from build_book import SPINE
    out = []
    for _kind, label, rel, _lvl in SPINE:
        if not rel:
            continue
        p = os.path.join(ROOT, rel)
        if not os.path.exists(p) or os.path.abspath(p) == os.path.abspath(OUT):
            continue
        # The index is a spine component, so the moment it went on the spine it became one
        # of its own surfaces -- every term in it matched itself, every entry gained an
        # "Index" locator, and `--check` reported STALE on a file it had just written,
        # because writing it changed the input. Excluded here.
        out.append((label, rel, io.open(p, encoding="utf-8").read()))
    return out


def build():
    docs = surfaces()
    entries, missing, bad_primary = [], [], []

    for group, terms in TERMS.items():
        rows = []
        for display, pat in terms:
            rx = re.compile(pat, re.I)
            locs, files = [], set()
            for label, rel, text in docs:
                found = False
                for m in rx.finditer(text):
                    loc = locator(label, rel, text, m.start())
                    if loc not in locs:
                        locs.append(loc)
                    found = True
                if found:
                    files.add(rel)
            if not locs:
                missing.append(display)
                continue

            primary = PRIMARY.get(display)
            if primary and primary not in locs:
                bad_primary.append((display, primary, ", ".join(sorted(set(locs))[:4])))
                continue

            locs = sorted(set(locs), key=order)
            if len(locs) > SATURATED:
                shown = "**%s**, and throughout" % primary if primary else "throughout"
            else:
                shown = ", ".join(("**%s**" % l if l == primary else l) for l in locs)
            rows.append((display, shown))
        entries.append((group, rows))

    if missing:
        sys.exit("ABORT: %d term(s) in TERMS appear nowhere in the book.\n  %s\n"
                 "An index entry pointing at nothing is worse than a missing one."
                 % (len(missing), "\n  ".join(missing)))
    if bad_primary:
        sys.exit("ABORT: %d PRIMARY locator(s) no longer hold their term.\n  %s\n"
                 "A section moved. Fix PRIMARY rather than the index."
                 % (len(bad_primary),
                    "\n  ".join("%s: recorded %s, found in %s" % b for b in bad_primary)))
    return entries


def render(entries):
    out = ["# Index", "",
           "Locators are chapter and section rather than page. **Bold** marks where a "
           "term is taught; the rest is where it gets used.", ""]
    for group, rows in entries:
        out.append("## %s" % group)
        out.append("")
        for display, shown in sorted(rows, key=lambda r: r[0].lower()):
            out.append("**%s** — %s" % (display, shown))
            out.append("")
    return "\n".join(out).rstrip() + "\n"


def main():
    text = render(build())
    n = sum(len(rows) for _g, rows in build())
    if "--check" in sys.argv:
        on_disk = io.open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
        if on_disk != text:
            sys.exit("STALE: back_matter/index.md does not match the book. Rebuild it.")
        print("index ok — %d entries, current" % n)
        return 0
    if "--dry" in sys.argv:
        print(text)
        print("--dry: %d entries, nothing written." % n)
        return 0
    io.open(OUT, "w", encoding="utf-8").write(text)
    print("wrote back_matter/index.md — %d entries." % n)
    return 0


if __name__ == "__main__":
    sys.exit(main())
