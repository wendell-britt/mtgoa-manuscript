# -*- coding: utf-8 -*-
"""
Assemble the print deliverable and report what is missing from it.

Nothing in this repository built a whole book before 2026-07-29. `compiled/` holds
one stale 2026-05-29 artifact and `compiled/build_compile.py` reads the retired
`chapters/` tree, so neither reflects canon. This reads canon.

The build is deliberately unforgiving about gaps. A missing half-title is not a
warning to be scrolled past — it exits non-zero, the same as a missing chapter,
because a book cannot be typeset without one. Run it to see the true distance to
a printable file:

    python3 instruments/build_book.py            # report only, no write
    python3 instruments/build_book.py --write    # emit build/MTGOA_PRINT_<date>.md
    python3 instruments/build_book.py --toc      # print the generated TOC alone

The marginalia frame must be applied when you build; the frame is part of the
printed page. `compile.py --strip` before measuring, `--apply` before building.
"""
import re, io, os, sys, glob, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)
MS = os.path.join(ROOT, "manuscript")
APX = os.path.join(ROOT, "appendices")
FRONT = os.path.join(ROOT, "front_matter")
BUILD = os.path.join(ROOT, "build")

# The book, in printed order.
#
#   kind    front | chapter | appendix | back
#   path    relative to repo root, or None where the component is generated
#   level   BLOCKER | GAP | OPTIONAL
#
# Three levels, not two, because the two-level version lied. Acknowledgements, the
# author's note, and the enrollment page were all marked "not required" so that the
# spine would report complete, and it did — while three components Wendell counts as
# necessary were missing. A reader notices their absence; the builder did not.
#
#   BLOCKER   there is no book without it. --write refuses.
#   GAP       the book assembles and the reader will notice. --write emits, and
#             stamps a banner naming what shipped incomplete.
#   OPTIONAL  a book is allowed not to have one.
#
# GAP exists because the deliverable is an ebook that gets updated after release.
# Refusing to build over a missing acknowledgements page would be the instrument
# substituting its judgment for a shipping decision that is Wendell's to make. Its
# job is to make the gap impossible to forget, not impossible to ship.
BLOCKER, GAP, OPTIONAL = "BLOCKER", "GAP", "OPTIONAL"

SPINE = [
    ("front",    "Half title",              "front_matter/half_title.md",        BLOCKER),
    ("front",    "Title page",              "front_matter/title_page.md",        BLOCKER),
    ("front",    "Copyright page",          "front_matter/copyright.md",         BLOCKER),
    ("front",    "Dedication",              "front_matter/dedication.md",        OPTIONAL),
    ("front",    "Table of contents",       None,                                BLOCKER),  # generated
    # The author's note is where the edition states what it is and is not. On a
    # book that ships deliberately incomplete, that page is the integrity.
    ("front",    "Author's note",           "front_matter/authors_note.md",      GAP),

    ("chapter",  "Chapter 1",               "manuscript/ch1.md",                 BLOCKER),
    ("chapter",  "Chapter 2",               "manuscript/ch2.md",                 BLOCKER),

    # The Headmaster's letter stands at the door of the six schools, so it sits here
    # rather than at the front of the book. It is stored under front_matter/ because
    # that directory holds standalone documents carrying no marginalia frame, and
    # because gate.py's matter surface already sweeps it; position in this spine is
    # what places a page, not the directory it lives in.
    ("front",    "A Letter to the Reader",  "front_matter/headmasters_letter.md", BLOCKER),

    ("chapter",  "Chapter 3",               "manuscript/ch3.md",                 BLOCKER),
    ("chapter",  "Chapter 4",               "manuscript/ch4.md",                 BLOCKER),
    ("chapter",  "Chapter 5",               "manuscript/ch5.md",                 BLOCKER),
    ("chapter",  "Chapter 6",               "manuscript/ch6.md",                 BLOCKER),
    ("chapter",  "Chapter 7",               "manuscript/ch7.md",                 BLOCKER),
    ("chapter",  "Chapter 8",               "manuscript/ch8.md",                 BLOCKER),
    ("chapter",  "Chapter 9",               "manuscript/ch9.md",                 BLOCKER),

    # Appendix C went to The Five Channels in Practice on 2026-07-30, by Wendell's
    # ruling. It was never a close call once the neighbours were read: Appendix B
    # already said "before Appendix C (The Five Channels in Practice)" and Appendix
    # D already named "the toolkit cluster (C Five Channels / D Emotional Alchemy /
    # E 3-2-1 Shadow)". The Key Terms glossary is not a toolkit and no chapter ever
    # pointed at it. The file stays on disk, marked retired, and off the spine.
    ("appendix", "Appendix A",  "appendices/APPENDIX_A_FOUR_ALLYSHIP_DOMAINS.md",     BLOCKER),
    ("appendix", "Appendix B",  "appendices/APPENDIX_B_QUESTS_CAMPAIGNS.md",          BLOCKER),
    ("appendix", "Appendix C",  "appendices/APPENDIX_C_FIVE_CHANNELS.md",             BLOCKER),
    ("appendix", "Appendix D",  "appendices/APPENDIX_D_EMOTIONAL_ALCHEMY_PRACTICES.md", BLOCKER),
    ("appendix", "Appendix E",  "appendices/APPENDIX_E_321_SHADOW_PROCESS.md",        BLOCKER),
    ("appendix", "Appendix F",  "appendices/APPENDIX_F_POLARITY_MAP.md",              BLOCKER),
    ("appendix", "Appendix G",  "appendices/ON_THE_SHOULDERS_OF.md",                  BLOCKER),

    ("back",     "Acknowledgements",        "back_matter/acknowledgements.md",   GAP),
    # The acknowledgements say "their names are on the page that follows", so this
    # is a live forward reference and has to sit immediately after them. Alphabetical
    # by Wendell's ruling 2026-07-30, no tiers. It stays a GAP rather than a BLOCKER
    # because only the backer list is missing, and holding the whole build hostage to
    # a list that arrives from Kickstarter would stop the book for a data export.
    ("back",     "Kickstarter backers",     "back_matter/kickstarter_backers.md", GAP),
    ("back",     "About the author",        "back_matter/about_the_author.md",   BLOCKER),
    # The enrollment page is the only place the book can hand a reader the app
    # deliberately. Twelve mentions of bars-engine and no address is a dead end.
    ("back",     "Enrollment page",         "back_matter/enrollment.md",         GAP),
]

# Live cross-references in canon that name an appendix by title rather than by
# letter. Each has to resolve to a lettered file in the spine before print, or a
# reader follows a pointer to nothing.
NAMED_REFERENCES = {
    "The Five Channels in Practice": "appendices/APPENDIX_C_FIVE_CHANNELS.md",
    "3-2-1 Shadow Process":          "appendices/APPENDIX_E_321_SHADOW_PROCESS.md",
    "Polarity Map":                  "appendices/APPENDIX_F_POLARITY_MAP.md",
}

MARGINALIA = re.compile(
    r"<!-- (MARGINALIA|EPIGRAPH-BYLINE|POSTCARD) -->\n(.*?)\n<!-- /\1 -->", re.S)


# Provenance headers. Every appendix carries a block of editorial metadata under
# its H1 — Status, Authority, Location in book, Timing dependency — and it is
# genuinely useful in the repository: it is how anybody knows Appendix D was
# checked line-by-line against the *Igniting Joy* source and approved.
#
# Until 2026-07-31 this builder copied it straight into the deliverable. Fifteen
# lines reached build/MTGOA_PRINT_2026-07-31.md across six shipping appendices,
# including internal file paths (docs/plans/..., GATE_GIFTS_ALLYSHIP_MOVES.md),
# "approved by Wendell", a **Status: Draft** flag on an appendix that was
# shipping, and "Coordinate before press" — an instruction addressed to the
# production team, printed for the reader.
#
# gate.py passed the whole time. It scores banned words; this is not one.
# build_book.py passed. It scores missing files; these files were present.
#
# Stripped only inside the header block — above the first `---` rule — so a
# legitimate bolded label in body prose is never touched.
META_KEY = re.compile(
    r"^\*\*(Status|Authority|Location in book|Timing dependency|Depends on|"
    r"Blocked by|Revised|Ported|Type|Source|Created):\*\*.*$", re.M)


def strip_provenance(text):
    """Remove editorial metadata from a component's header block."""
    parts = text.split("\n---\n", 1)
    if len(parts) == 1:
        return text
    head, rest = parts
    head = META_KEY.sub("", head)
    head = re.sub(r"\n{3,}", "\n\n", head).rstrip() + "\n"
    return head + "\n---\n" + rest


def read(rel):
    path = os.path.join(ROOT, rel)
    if not os.path.exists(path):
        return None
    return strip_provenance(io.open(path, encoding="utf-8").read())


def words(text):
    """Whitespace split, the measure MANIFEST.md and every planning doc quote."""
    return len(text.split())


# The nine chapters used to open in four different heading styles, and this comment
# used to list them. They were fixed at source on 2026-08-01 (CA-3, CA-4): every H1 now
# reads "CHAPTER N: THE FACE — clause". The normalizing stays, because a contents page
# is not a manuscript file and wants neither the caps nor a second em-dash:
#
#   in the file   # CHAPTER 1: THE INFINITE ARCADE — What You Spend, and What Comes Back
#   in the TOC    **Chapter 1** — The Infinite Arcade: What You Spend, and What Comes Back
#
# Two em-dashes in one contents line is the reason. The first one separates the label
# from the title and is the page's own punctuation; the second belongs to the title and
# collides with it. A colon holds the clause without competing. The Face name drops to
# title case so the chapter block and the appendix block below it read as one list.
# `--headings` still reports the raw forms.
HEADING = re.compile(r"^#\s*(?:CHAPTER|Chapter)\s*\d+\s*[—:-]?\s*(.*)$", re.M)
SUBTITLE = re.compile(r"^##\s*\*(.+?)\*\s*$", re.M)


def title_of(text, fallback):
    """The chapter or appendix name, with its own label prefix removed."""
    m = HEADING.search(text)
    if m and m.group(1).strip():
        return m.group(1).strip()
    m = re.search(r"^#+\s*(.+)$", text, re.M)
    if not m:
        return fallback
    # "Appendix F: The Polarity Map" -> "The Polarity Map"
    return re.sub(r"^Appendix\s+[A-G]\s*[—:-]\s*", "", m.group(1).strip())


def toc_title(title):
    """Render one title for a contents page: title-case the name, colon the clause.

    Splits on the em-dash the H1 uses to hold its clause. Appendix titles carry no
    clause and pass through untouched; a chapter name in caps comes down to title case,
    because SHOUTING is a manuscript-file convention and a contents page is not one.
    """
    name, sep, clause = title.partition(" — ")
    if name.isupper():
        name = name.title()
    return "%s: %s" % (name, clause) if sep else name


def subtitle_of(text):
    m = SUBTITLE.search(text)
    return m.group(1).strip() if m else None


def build_toc(entries):
    """Generate the contents from the headings that actually exist.

    Lists only what follows the contents page. The half title, title page, and
    copyright sit ahead of it and are never listed in one.
    """
    lines = ["# Contents", ""]
    section = None
    for kind, label, title, subtitle in entries:
        if kind != section:
            if section is not None:
                lines.append("")
            section = kind
        if kind in ("chapter", "appendix"):
            lines.append("**%s** — %s" % (label, toc_title(title)))
            if subtitle:
                lines.append("  *%s*" % subtitle)
        else:
            lines.append("%s" % title)
    return "\n".join(lines) + "\n"


def main():
    write = "--write" in sys.argv
    toc_only = "--toc" in sys.argv

    present, missing, entries, parts = [], [], [], []
    frame_blocks = 0
    toc_slot = toc_entry = None

    for kind, label, rel, level in SPINE:
        if rel is None:                       # generated, not authored
            toc_entry = len(entries)
            present.append((label, 0, "generated"))
            toc_slot = len(parts)             # filled once the entries are known
            parts.append(None)
            continue
        text = read(rel)
        if text is None:
            missing.append((label, rel, level))
            continue
        frame_blocks += len(MARGINALIA.findall(text))
        entries.append((kind, label, title_of(text, label), subtitle_of(text)))
        present.append((label, words(text), rel))
        parts.append(text)

    if "--headings" in sys.argv:
        print("%-12s %s" % ("component", "raw first heading"))
        print("-" * 78)
        for kind, label, rel, _ in SPINE:
            text = read(rel) if rel else None
            if text is None:
                continue
            first = re.search(r"^#+\s*.+$", text, re.M)
            print("%-12s %s" % (label, first.group(0) if first else "(none)"))
        return 0

    toc = build_toc(entries[toc_entry:] if toc_entry is not None else entries)
    if toc_slot is not None:
        parts[toc_slot] = toc
    if toc_only:
        sys.stdout.write(toc)
        return 0

    print("%-22s %8s  %s" % ("component", "words", "source"))
    print("-" * 78)
    for label, n, src in present:
        print("%-22s %8s  %s" % (label, n or "—", src))
    print("-" * 78)
    total = sum(n for _, n, _ in present)
    print("%-22s %8d  (%d marginalia blocks applied)" % ("TOTAL", total, frame_blocks))

    if frame_blocks == 0:
        print("\nWARNING: no marginalia blocks found. The frame is stripped. "
              "Run `python3 marginalia/compile.py --apply` before building.")

    if missing:
        print("\nMISSING — %d component(s):" % len(missing))
        order = {BLOCKER: 0, GAP: 1, OPTIONAL: 2}
        for label, rel, level in sorted(missing, key=lambda m: order[m[2]]):
            print("  %-9s %-22s %s" % (level, label, rel))

    unresolved = [(name, rel) for name, rel in NAMED_REFERENCES.items()
                  if read(rel) is None or not rel.startswith("appendices/")]
    if unresolved:
        print("\nUNPLACED — canon points at these by name and they are not in the "
              "appendix spine:")
        for name, rel in unresolved:
            state = "written, unlettered" if read(rel) is not None else "not written"
            print("  %-34s %-38s %s" % (name, rel, state))

    # Compare against the level, not its truthiness. Every level is a non-empty
    # string, so `if m[2]` was true for GAP and OPTIONAL alike and would have made
    # a missing dedication refuse the build.
    blockers = [m for m in missing if m[2] == BLOCKER]
    gaps = [m for m in missing if m[2] == GAP]

    if write:
        if blockers:
            print("\nRefusing to write: %d BLOCKER(s) missing." % len(blockers))
            return 1
        os.makedirs(BUILD, exist_ok=True)
        stamp = datetime.date.today().isoformat()
        out = os.path.join(BUILD, "MTGOA_PRINT_%s.md" % stamp)
        body = "\n\n\\newpage\n\n".join(p for p in parts if p is not None)
        io.open(out, "w", encoding="utf-8").write(body)
        print("\nWrote %s (%d words)" % (out, total))
        if gaps:
            # Loud, and after the success line, because the success line is the
            # part that gets read. This edition ships without these.
            print("\n" + "!" * 62)
            print("SHIPPING WITH %d GAP(S) — the reader will notice each one:" % len(gaps))
            for label, rel, _ in gaps:
                print("  %-22s %s" % (label, rel))
            print("!" * 62)
        return 0

    if blockers:
        print("\n%d BLOCKER(s) between here and a book." % len(blockers))
        return 1
    if gaps:
        print("\nSpine assembles, with %d gap(s): %s."
              % (len(gaps), ", ".join(m[0] for m in gaps)))
        return 0
    print("\nSpine complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
