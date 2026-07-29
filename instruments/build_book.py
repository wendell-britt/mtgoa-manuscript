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

# The book, in printed order. `required` means the build fails without it.
#
#   kind   front | chapter | appendix | back
#   path   relative to repo root, or None where nothing has been written yet
#
# Front and back matter carry path=None until somebody writes them. That is the
# point: the gap is enforced by the builder rather than asserted in a planning
# document, because the planning documents have been wrong about exactly this.
SPINE = [
    ("front",    "Half title",              "front_matter/half_title.md",        True),
    ("front",    "Title page",              "front_matter/title_page.md",        True),
    ("front",    "Copyright page",          "front_matter/copyright.md",         True),
    ("front",    "Dedication",              "front_matter/dedication.md",        False),
    ("front",    "Table of contents",       None,                                True),  # generated
    ("front",    "Author's note",           "front_matter/authors_note.md",      False),

    ("chapter",  "Chapter 1",               "manuscript/ch1.md",                 True),
    ("chapter",  "Chapter 2",               "manuscript/ch2.md",                 True),
    ("chapter",  "Chapter 3",               "manuscript/ch3.md",                 True),
    ("chapter",  "Chapter 4",               "manuscript/ch4.md",                 True),
    ("chapter",  "Chapter 5",               "manuscript/ch5.md",                 True),
    ("chapter",  "Chapter 6",               "manuscript/ch6.md",                 True),
    ("chapter",  "Chapter 7",               "manuscript/ch7.md",                 True),
    ("chapter",  "Chapter 8",               "manuscript/ch8.md",                 True),
    ("chapter",  "Chapter 9",               "manuscript/ch9.md",                 True),

    ("appendix", "Appendix A",  "appendices/APPENDIX_A_FOUR_ALLYSHIP_DOMAINS.md",     True),
    ("appendix", "Appendix B",  "appendices/APPENDIX_B_QUESTS_CAMPAIGNS.md",          True),
    ("appendix", "Appendix C",  "appendices/APPENDIX_C_KEY_TERMS.md",                 True),
    ("appendix", "Appendix D",  "appendices/APPENDIX_D_EMOTIONAL_ALCHEMY_PRACTICES.md", True),
    ("appendix", "Appendix E",  "appendices/APPENDIX_E_321_SHADOW_PROCESS.md",        True),
    ("appendix", "Appendix F",  "appendices/APPENDIX_F_POLARITY_MAP.md",              True),
    ("appendix", "Appendix G",  "appendices/ON_THE_SHOULDERS_OF.md",                  True),

    ("back",     "Acknowledgements",        "back_matter/acknowledgements.md",   False),
    ("back",     "About the author",        "back_matter/about_the_author.md",   True),
    ("back",     "Enrollment page",         "back_matter/enrollment.md",         False),
]

# Live cross-references in canon that name an appendix by title rather than by
# letter. Each has to resolve to a real file before print, or a reader follows a
# pointer to nothing. The Five Channels appendix is the open case: ch3 sends the
# reader to it, it is written, and it has no letter and sits in drafts/.
NAMED_REFERENCES = {
    "The Five Channels in Practice": "drafts/appendix_channels.md",
    "3-2-1 Shadow Process":          "appendices/APPENDIX_E_321_SHADOW_PROCESS.md",
    "Polarity Map":                  "appendices/APPENDIX_F_POLARITY_MAP.md",
}

MARGINALIA = re.compile(
    r"<!-- (MARGINALIA|EPIGRAPH-BYLINE|POSTCARD) -->\n(.*?)\n<!-- /\1 -->", re.S)


def read(rel):
    path = os.path.join(ROOT, rel)
    if not os.path.exists(path):
        return None
    return io.open(path, encoding="utf-8").read()


def words(text):
    """Whitespace split, the measure MANIFEST.md and every planning doc quote."""
    return len(text.split())


# The nine chapters open in four different heading styles — "Chapter 1 — The
# Infinite Arcade", "CHAPTER 2: THE FOREST — subtitle", "CHAPTER 7 — THE
# DIPLOMAT", and ch9 with no Face name at all. A typesetter needs one form, so
# the TOC normalizes rather than reproducing the inconsistency. `--headings`
# reports the raw forms so they can be fixed at source.
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


def subtitle_of(text):
    m = SUBTITLE.search(text)
    return m.group(1).strip() if m else None


def build_toc(entries):
    """Generate the table of contents from the headings that actually exist."""
    lines = ["# Contents", ""]
    section = None
    for kind, label, title, subtitle in entries:
        if kind != section:
            if section is not None:
                lines.append("")
            section = kind
        if kind in ("chapter", "appendix"):
            lines.append("**%s** — %s" % (label, title))
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

    for kind, label, rel, required in SPINE:
        if rel is None:                       # generated, not authored
            entries.append((kind, label, "Contents", None))
            present.append((label, 0, "generated"))
            continue
        text = read(rel)
        if text is None:
            missing.append((label, rel, required))
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

    toc = build_toc(entries)
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
        for label, rel, required in missing:
            print("  %-8s %-22s %s" % ("BLOCKER" if required else "optional", label, rel))

    unresolved = [(name, rel) for name, rel in NAMED_REFERENCES.items()
                  if read(rel) is None or not rel.startswith("appendices/")]
    if unresolved:
        print("\nUNPLACED — canon points at these by name and they are not in the "
              "appendix spine:")
        for name, rel in unresolved:
            state = "written, unlettered" if read(rel) is not None else "not written"
            print("  %-34s %-38s %s" % (name, rel, state))

    blockers = [m for m in missing if m[2]]
    if write:
        if blockers:
            print("\nRefusing to write: %d required component(s) missing." % len(blockers))
            return 1
        os.makedirs(BUILD, exist_ok=True)
        stamp = datetime.date.today().isoformat()
        out = os.path.join(BUILD, "MTGOA_PRINT_%s.md" % stamp)
        io.open(out, "w", encoding="utf-8").write("\n\n\\newpage\n\n".join(parts))
        print("\nWrote %s (%d words)" % (out, total))
        return 0

    if blockers:
        print("\n%d blocker(s) between here and a printable file." % len(blockers))
        return 1
    print("\nSpine complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
