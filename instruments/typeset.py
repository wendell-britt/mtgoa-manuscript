# -*- coding: utf-8 -*-
"""
Turn the assembled book into a source a typesetter can style, without touching canon.

`build_book.py` answers *is the book complete*. This answers *can it be set*, and
they are different questions. The assembled markdown is correct and unstylable:
five different frame devices all arrive as the same blockquote, four chapters
announce themselves in four different heading styles, and 251 `---` rules mean two
unrelated things depending on what follows them. A designer handed that file has to
guess, and a converter has no way to guess at all.

This is the layer where the guessing gets done once, in code, with the reasoning
written down. Both `build_pdf.py` and `build_epub.py` read its output, so the two
editions cannot drift apart in how they treat a marginal note.

Nothing here edits `manuscript/`. Every transform runs on the assembled copy.

    python3 instruments/typeset.py             # report the transforms and the flags
    python3 instruments/typeset.py --write     # emit build/MTGOA_TYPESET_<date>.md
    python3 instruments/typeset.py --flags     # the flags alone, for a ruling pass

## The four transforms

**1 · The frame becomes five named devices.** The Calrunia frame is the book's
signature: each chapter is a document by one character annotated by another. On
disk all five kinds are HTML-commented blockquotes, which is right for the
repository — greppable, strippable, safe to hand anybody. Set as blockquotes they
collapse into one undifferentiated grey, and a postcard from Tull reads exactly
like an admissions handbook. Each kind becomes a div carrying its own class, and
the `> ` marks come off so the design owns the indent rather than inheriting it.

**2 · The chapter openers are read, not remembered.** Canon settled on one form on
2026-08-01, closing §6 of `SPEC_PRINT_READINESS_2026-07-29.md`:

    # CHAPTER 3: THE SHAMAN — What to Do With What You Feel
    ## *Emotional Alchemy as the Foundation of Real Allyship*

Until then this file carried a hand-written display title for each of the nine
chapters plus a frozen copy of the raw heading each was read off — eighteen
strings to keep in step with canon by hand. All eighteen are gone. One regex takes
the number for the label, the name for the title, and the em-dash tail for the
clause; a chapter that does not match the form is a BLOCKER.

**3 · The rules get read.** 188 of the 251 `---` sit immediately before a heading,
where the heading already supplies the break and a printed line is noise. 2 open a
component with nothing above them to separate. 61 fall mid-prose, where they are
the scene break and have to stay visible. Same character, three jobs. Only the
last group survives, as a marked break the design sets as an ornament.

**4 · The lists get their blank line.** Eleven places write a lead-in and then the
items directly under it, with no blank line between. Markdown wants one, and
without it the whole thing is a single paragraph — `This might look like: - A deep
breath - A shift in your thinking`, hyphens running inline like stray dashes.
Obsidian renders the list, which is why it survived: the vault shows the author
what the author meant. Five of the eleven are the five channel entries in Appendix
C, so that entire appendix was setting as run-on prose.
"""
import re, io, os, sys, glob, datetime, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)
BUILD = os.path.join(ROOT, "build")


def _load_build_book():
    """Import build_book as a module so the spine has exactly one definition."""
    spec = importlib.util.spec_from_file_location(
        "build_book", os.path.join(HERE, "build_book.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


bb = _load_build_book()


# ---------------------------------------------------------------- frame devices

# The five kinds, in the order a reader meets them. The class name is what both
# the Typst template and the EPUB stylesheet key off, so changing one of these
# strings means changing it in three files.
FRAME_KINDS = ("MARGINALIA", "EPIGRAPH-BYLINE", "HANDBOOK", "SIGNATURE", "POSTCARD")
FRAME_CLASS = {
    "MARGINALIA":      "marginalia",       # another hand, in the margin
    "EPIGRAPH-BYLINE": "epigraph",         # the voices before a chapter opens
    "HANDBOOK":        "handbook",         # a document inside the document
    "SIGNATURE":       "signature",        # who set the treatise down
    "POSTCARD":        "postcard",         # correspondence, not instruction
}

FRAME = re.compile(
    r"<!-- (%s) -->\n(.*?)\n<!-- /\1 -->" % "|".join(re.escape(k) for k in FRAME_KINDS),
    re.S)


def unquote(block):
    """Strip the `> ` marks. The device owns its indent; markdown should not."""
    out = []
    for line in block.split("\n"):
        out.append(re.sub(r"^>[ ]?", "", line))
    return "\n".join(out)


def frame_to_divs(text, tally):
    def sub(m):
        kind, body = m.group(1), m.group(2)
        tally[kind] = tally.get(kind, 0) + 1
        return "::: {.%s}\n%s\n:::" % (FRAME_CLASS[kind], unquote(body).strip())
    return FRAME.sub(sub, text)


# ------------------------------------------------------------- chapter openers

# Canon opens every chapter the same way as of 2026-08-01 (CA-3, CA-4):
#
#     # CHAPTER 3: THE SHAMAN — What to Do With What You Feel
#     ## *Emotional Alchemy as the Foundation of Real Allyship*
#
# That closes §6 of `specs/SPEC_PRINT_READINESS_2026-07-29.md`, open since July,
# and it replaces the table that used to live here — a hand-written display title
# for each of the nine chapters plus a frozen copy of the raw heading each was read
# off. Eighteen strings to keep in step with canon by hand, gone.
#
# **The clause is new and it is not the subtitle.** Every chapter now carries both:
# a plain clause in the H1, drafted against that chapter's own argument, and the
# italic subtitle it always had, which `d65ba78` ruled a feature. Three lines of
# display type on an opening page, and the design has to make them read as a
# descending hierarchy rather than as the same thing said three times.
#
# Two earlier answers to this were wrong and are worth naming. The first hand-wrote
# nine display titles. The second cherry-picked `6026b06` off
# `claude/book-print-readiness-august-ar95mo`, which normalised the form by
# *deleting* Chapter 2's clause — the exact opposite of the ruling that landed on
# master hours later, which gave the other eight a clause of their own. A branch
# that answers a question is not the same as the branch that answered it last.
CHAPTER_HEADING = re.compile(r"^CHAPTER\s+(\d+):\s+([^—]+?)(?:\s+—\s+(.+))?$")

# The slot id becomes the anchor in both editions and the filename stem in the
# EPUB, so it is stable and readable rather than generated from the title.
SLOT = {
    "Half title": "half-title", "Title page": "title-page",
    "Copyright page": "copyright", "Dedication": "dedication",
    "Table of contents": "contents", "Author's note": "authors-note",
    "A Letter to the Reader": "letter",
    "Acknowledgements": "acknowledgements", "Kickstarter backers": "backers",
    "About the author": "about-the-author", "Enrollment page": "enrollment",
}

H1 = re.compile(r"^#[ \t]+(.+?)[ \t]*$", re.M)
H2_SUBTITLE = re.compile(r"^##[ \t]*\*(.+?)\*[ \t]*$", re.M)
ITALIC_H3 = re.compile(r"^###[ \t]*(\*[^\n]+\*)[ \t]*$", re.M)


def split_opener(text, label):
    """Peel the H1 and the italic H2 subtitle off a component's body.

    Returns (title, subtitle, body). The heading pair is metadata about the
    component, not the first two lines of it — a chapter opener is a designed page
    and cannot be built from a heading that has already been set.
    """
    m = H1.search(text)
    raw_title = m.group(1).strip() if m else label
    body = text[:m.start()] + text[m.end():] if m else text

    subtitle = None
    m2 = H2_SUBTITLE.search(body)
    # Only if it leads the component. An italic H2 deep in a chapter is prose.
    if m2 and not body[:m2.start()].strip():
        subtitle = m2.group(1).strip()
        body = body[:m2.start()] + body[m2.end():]

    # A chapter names itself `CHAPTER 3: THE SHAMAN — What to Do With What You
    # Feel`. The number is the label, which the design sets above the rule; the
    # name is the title, and comes back mixed-case for the small caps to work on;
    # the clause is its own line.
    clause = None
    m3 = CHAPTER_HEADING.match(raw_title)
    if m3:
        title = m3.group(2).strip()
        if title.isupper():
            title = title.title()          # the same rule build_book.py's TOC uses
        clause = (m3.group(3) or "").strip() or None
    else:
        # Front, back, and appendix components keep their own heading, minus the
        # label the design sets separately: "Appendix F: The Polarity Map".
        title = re.sub(r"^Appendix\s+[A-Z]\s*[—:-]\s*", "", raw_title).strip()
    return title, clause, subtitle, body.lstrip("\n")


def demote_section_subtitles(text, tally):
    """An italic H3 directly under its H2 is that section's subtitle, not a head.

    `## Section 1: Urgency` / `### *"The World Didn't Get Safer..."*` is one
    two-line unit. Left as a heading it enters the contents and the EPUB nav as a
    peer of the section above it, and every navigation surface doubles in length
    with entries that are not places.
    """
    lines = text.split("\n")
    out, i = [], 0
    while i < len(lines):
        out.append(lines[i])
        if lines[i].startswith("## ") and not lines[i].startswith("###"):
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            m = ITALIC_H3.match(lines[j]) if j < len(lines) else None
            if m:
                out.append("")
                out.append("::: {.sectionsubtitle}")
                out.append(m.group(1))
                out.append(":::")
                tally["sectionsubtitle"] = tally.get("sectionsubtitle", 0) + 1
                i = j + 1
                continue
        i += 1
    return "\n".join(out)


# ------------------------------------------------------------------- the lists

LIST_ITEM = re.compile(r"^\s*([-*+]|\d+\.)\s+\S")


def open_lists(text, tally):
    """Give a list the blank line markdown needs before it will be a list.

    Eleven places in the shipping components write a lead-in and then the items
    directly under it:

        This might look like:
        - A deep breath where you actually feel your body relax slightly
        - A shift in your thinking from "why is this happening?" to ...

    Markdown wants a blank line after the lead-in. Without one the whole thing is
    a single paragraph, and it sets as `This might look like: - A deep breath
    where you actually feel your body relax slightly - A shift in your thinking`,
    with the hyphens running inline like stray dashes.

    Obsidian renders it as a list, which is why it survived: the vault shows the
    author what the author meant. Five of the eleven are the five channel entries
    in Appendix C, so the whole of that appendix was setting as run-on prose.

    Same class of thing as the rules — a mechanical gap between what markdown
    requires and what the file says, resolved by the layer that exists for it, and
    counted in the report so a new one gets noticed.
    """
    lines = text.split("\n")
    out = []
    for line in lines:
        if (out and out[-1].strip() and LIST_ITEM.match(line)
                and not LIST_ITEM.match(out[-1])
                and not out[-1].lstrip().startswith(("#", ">", "|", ":::"))):
            out.append("")
            tally["list_opened"] = tally.get("list_opened", 0) + 1
        out.append(line)
    return "\n".join(out)


# ------------------------------------------------------------------- the rules

def resolve_rules(text, tally):
    """Drop the rules a heading already makes; mark the ones that are scene breaks."""
    lines = text.split("\n")
    out, seen_content = [], False
    for i, line in enumerate(lines):
        if line.strip() != "---":
            if line.strip():
                seen_content = True
            out.append(line)
            continue
        j = i + 1
        while j < len(lines) and not lines[j].strip():
            j += 1
        if j < len(lines) and lines[j].lstrip().startswith("#"):
            tally["rule_dropped"] = tally.get("rule_dropped", 0) + 1
            continue                       # the heading is the break
        if not seen_content:
            # A rule with nothing above it separates nothing. Every appendix has
            # one: it closed the provenance header that `build_book.py` strips, so
            # it survived into the build as a scene break under the title, marking
            # a break between the chapter title and the appendix's first sentence.
            tally["rule_leading"] = tally.get("rule_leading", 0) + 1
            continue
        tally["rule_kept"] = tally.get("rule_kept", 0) + 1
        out.append("::: {.scenebreak}")
        out.append(":::")
    return "\n".join(out)


# ------------------------------------------------------------ hyphenation rulings
# `instruments/proofread.py` reads the built interior and reports a FRAGMENT: a
# paragraph whose last line is nothing but the back half of a hyphenated word.
# `book/mtgoa.typ` already carries `costs: (runt: 400%)` for this, which took the
# count from three to two on 2026-08-09. The two survivors do not answer to cost.
#
#   p126  "...a container for hurt feelings without a desti-  / nation."
#   p246  "...a failure of discernment disguised as open-     / mindedness."
#
# Measured 2026-08-13 before writing this. Raising `runt` to 600, 800 and 1200%
# changed nothing and did not move a single page, so the cost was never binding.
# Raising `costs.hyphenation` to 300% did clear `nation.` -- and cost two pages
# across the whole book, 387 to 389, while leaving `mindedness.` untouched,
# because that one breaks at a hyphen the author typed rather than one Typst
# inserted and `costs.hyphenation` does not govern those.
#
# So: two pages of repagination for half the job, against a per-word exception
# that moves nothing. A word list is what a house style actually keeps, and it is
# the same call `copyedit.py` made when it swapped a morphological guess for an
# explicit BRITISH dict.
#
# U+2011 NON-BREAKING HYPHEN holds an authored hyphen together. U+2060 WORD
# JOINER inside a word denies the hyphenator a break point without printing a
# glyph. Both survive pandoc into Typst and both are inert in the EPUB, where
# nothing has a measure to break against.
NOBREAK_HYPHEN = u"\u2011"
WORD_JOINER = u"\u2060"

# Each entry is a ruling, and each carries the page it was found on.
HYPHEN_RULINGS = [
    ("open-mindedness", "open" + NOBREAK_HYPHEN + "mindedness"),   # trade p246
    ("destination", "desti" + WORD_JOINER + "nation"),             # trade p126
]


def hyphen_rulings(text, tally):
    """Apply the per-word exceptions the proofread ruled. Nothing else."""
    for word, fixed in HYPHEN_RULINGS:
        n = len(re.findall(r"\b%s\b" % re.escape(word), text))
        if n:
            text = re.sub(r"\b%s\b" % re.escape(word), fixed, text)
            tally["hyphen: " + word] = n
    return text


# --------------------------------------------------------------------- assembly

# ------------------------------------------------------- the joined-lines ruling

BOLD_LINE = re.compile(r"^\*\*[^*].*\*\*$")


def joined_lines(body, label, flags):
    """Bold label lines the author put on their own line, which markdown joins.

    Markdown folds a single newline inside a paragraph into a space, so a label
    written on its own line sets run-in with the line under it. Obsidian renders
    the break, which is why nobody sees this until something is typeset.

    **Only where the author did not already ask for the break.** The first version
    of this check flagged thirteen sites and eight of them were correct on disk:
    Chapter 2's five moves and Chapter 4's three steps all end in the two trailing
    spaces that are markdown's hard line break, and they set on their own line in
    both editions. Reporting them as defects would have sent Wendell to fix eight
    lines that were already right.

    That leaves Chapter 8's five alchemy moves, which end at the `**` with nothing
    after it. The book's own convention — set twice, in two chapters, by the same
    hand — says what they should be.
    """
    lines = body.split("\n")
    for i, line in enumerate(lines[:-1]):
        nxt = lines[i + 1].strip()
        if not BOLD_LINE.match(line.strip()) or not nxt:
            continue
        if line.endswith("  ") or line.rstrip().endswith("\\"):
            continue                       # already a hard break; renders correctly
        if nxt.startswith(("#", "|", "-", ">", "*", "+", ":::")):
            continue
        flags.append(("RULING", label,
                      "two authored lines set as one, and no hard break: %s + %s"
                      % (line.strip()[:40], nxt[:34])))


def attr(**kw):
    """Pandoc attribute syntax, with quotes in a value escaped rather than eaten."""
    bits = []
    for k, v in kw.items():
        if v is None:
            continue
        bits.append('%s="%s"' % (k, str(v).replace('"', '\\"')))
    return " ".join(bits)


def components():
    """Every spine component that exists on disk, normalised and ready to set."""
    tally, flags, out = {}, [], []

    for kind, label, rel, level in bb.SPINE:
        if rel is None:                                  # the generated contents
            out.append({"kind": "contents", "label": label, "slot": SLOT[label],
                        "title": "Contents", "clause": None, "subtitle": None,
                        "toctitle": "Contents", "body": ""})
            continue

        text = bb.read(rel)
        if text is None:
            if level == bb.BLOCKER:
                flags.append(("BLOCKER", label, "missing: %s" % rel))
            elif level == bb.GAP:
                flags.append(("GAP", label, "missing: %s" % rel))
            continue

        # One heading form, enforced rather than remembered. This replaced a frozen
        # copy of all nine raw headings — which guarded the right thing and cost a
        # hand edit every time a chapter was retitled. The form is the guard now.
        if kind == "chapter":
            found = H1.search(text)
            found = found.group(1).strip() if found else "(no H1)"
            if not CHAPTER_HEADING.match(found):
                flags.append(("BLOCKER", label,
                              "heading is not the one canon form.\n"
                              "                   expected  # CHAPTER N: THE NAME\n"
                              "                   found     # %s" % found))

        title, clause, subtitle, body = split_opener(text, label)

        # The title page's byline is the one piece of body prose that belongs to
        # the page design rather than to the reading. It stays authored content —
        # dropping it into a template variable would take the author's name out of
        # the manuscript — so it is marked instead, and each edition centres it.
        if SLOT.get(label) == "title-page" and body.strip():
            body = "::: {.centered}\n%s\n:::\n" % body.strip()

        joined_lines(body, label, flags)
        body = frame_to_divs(body, tally)
        body = open_lists(body, tally)
        body = demote_section_subtitles(body, tally)
        body = resolve_rules(body, tally)
        body = hyphen_rulings(body, tally)
        body = re.sub(r"\n{3,}", "\n\n", body).strip() + "\n"

        # `toctitle` is how a contents line reads it: name, colon, clause. The rule
        # is build_book.py's, reused rather than restated, so the generated
        # contents in the PDF and the one build_book.py prints cannot disagree.
        out.append({"kind": kind, "label": label,
                    "slot": SLOT.get(label, re.sub(r"[^a-z0-9]+", "-", label.lower())),
                    "title": title, "clause": clause, "subtitle": subtitle,
                    "toctitle": bb.toc_title(
                        "%s — %s" % (title, clause) if clause else title),
                    "body": body})

    return out, tally, flags


def output_path():
    """The one definition of where `--write` puts the intermediate.

    Both builders used to re-derive this with `newest("MTGOA_TYPESET_*.md")`,
    which sorts a glob **by filename**, so any file matching that pattern and
    sorting later won permanently. On 2026-08-13 a reflow source named
    `MTGOA_TYPESET_REFLOW_<date>.md` did exactly that -- "R" sorts after "2" --
    and `build_pdf.py` silently set the book from it, dropping the hyphenation
    rulings. The PDF still built, still passed its own structural check, and the
    only thing that caught it was re-running the proofread.

    A builder that runs `typeset.py --write` already knows the answer; it does
    not need to guess. This function is that answer, and there is no pattern left
    to collide with.
    """
    return os.path.join(BUILD, "MTGOA_TYPESET_%s.md" % datetime.date.today())


def to_markdown(comps):
    """One file, every component announced by an H1 carrying its own metadata.

    The metadata rides on the heading rather than a wrapper div on purpose: pandoc
    splits an EPUB on headings, and a div around the heading takes the split with
    it — one 120,000-word XHTML file instead of twenty-four.
    """
    parts = []
    for c in comps:
        head = "# %s {%s}" % (c["title"], attr(
            **{"id": c["slot"], "class": c["kind"], "label": c["label"],
               "clause": c["clause"], "subtitle": c["subtitle"],
               "toctitle": c["toctitle"]}))
        # `class` is not a valid keyword name in the call above; rebuild it here so
        # the attribute reads `.chapter` the way pandoc expects a class to.
        head = head.replace('class="%s"' % c["kind"], ".%s" % c["kind"])
        parts.append(head + ("\n\n" + c["body"] if c["body"].strip() else "\n"))
    return "\n\n".join(parts)


def main():
    comps, tally, flags = components()

    print("%-24s %-9s %-14s %s" % ("component", "kind", "slot", "title"))
    print("-" * 78)
    for c in comps:
        print("%-24s %-9s %-14s %s%s%s" % (
            c["label"], c["kind"], c["slot"], c["title"],
            "  :  %s" % c["clause"] if c["clause"] else "",
            "  ·  %s" % c["subtitle"] if c["subtitle"] else ""))

    print("-" * 78)
    print("frame devices resolved")
    for kind in FRAME_KINDS:
        print("  %-16s %3d  -> .%s" % (kind, tally.get(kind, 0), FRAME_CLASS[kind]))
    print("  %-16s %3d  -> .sectionsubtitle" % ("italic H3 subtitle",
                                                tally.get("sectionsubtitle", 0)))
    print("lists")
    print("  %-16s %3d  blank line inserted so the items are a list"
          % ("run into prose", tally.get("list_opened", 0)))
    print("rules")
    print("  %-16s %3d  dropped — the heading after it is the break"
          % ("before a heading", tally.get("rule_dropped", 0)))
    print("  %-16s %3d  dropped — nothing above it to separate"
          % ("opening a body", tally.get("rule_leading", 0)))
    print("  %-16s %3d  kept    -> .scenebreak" % ("mid-prose",
                                                   tally.get("rule_kept", 0)))

    if "--flags" in sys.argv or flags:
        print("-" * 78)
        if not flags:
            print("No flags.")
        for level, label, note in flags:
            print("  %-8s %-16s %s" % (level, label, note))

    blockers = [f for f in flags if f[0] == "BLOCKER"]

    if "--write" in sys.argv:
        if blockers:
            print("\nRefusing to write: %d BLOCKER flag(s)." % len(blockers))
            return 1
        os.makedirs(BUILD, exist_ok=True)
        out = output_path()
        io.open(out, "w", encoding="utf-8").write(to_markdown(comps))
        print("\nWrote %s (%d components)" % (os.path.relpath(out, ROOT), len(comps)))
        return 0

    return 1 if blockers else 0


if __name__ == "__main__":
    sys.exit(main())
