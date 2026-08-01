# -*- coding: utf-8 -*-
"""
DL-22, corrected and applied — the three provenance leaks the existing strip misses.

**The correction first, because I reported this wrong.** I told Wendell that six shipping
appendices print their internal metadata and that a reader opening Appendix B meets
*"Status: Draft"* and a repo path before a word of the book. That was false.
`build_book.py` grew `strip_provenance()` on 2026-07-31 and it works: every
`**Status:**`, `**Authority:**` and `**Location in book:**` line is removed at assembly,
and `placeholders.py` imports the same function so it does not report them either. The
15-line leak the app spec measured was real when measured and has been closed since.
DL-22 as first logged described a fixed defect.

**What is actually still leaking is three lines, and they leak because the strip is keyed
on a shape rather than on a meaning.** `META_KEY` matches `**Known-Label:**` at the start
of a line inside the header block. Anything internal wearing a different costume walks
straight through.

  1. `APPENDIX_D`, the no-somatic note. A blockquote, so no `**Label:**` to match. It is
     addressed to whoever edits the file, not to the reader -- *"Keep it framed that way,
     invitation and lineage, never prescription mid-argument."* The reasoning is worth
     keeping and belongs in the repo: Appendix D is the book's one deliberate exception to
     the rule that its prose never narrates the reader's interior, and it earns the
     exception by sourcing three named, opt-in practices from a prior published book. That
     rationale is preserved here and in the commit; what comes out of the appendix is the
     instruction to the editor.

  2. `APPENDIX_E`, the `**Book body:**` line. The label is not in `META_KEY`, so it prints
     whole, carrying a repo path (`ch3.md:545`) and an editing note (*"Renumbered
     2026-07-29 -- the old figures were 0-indexed"*). Half of it is genuinely useful to a
     reader, though: where the catalogue is and where the first practice is. So the line is
     rewritten to the cross-reference form Appendix C already uses, rather than stripped.

  3. `ON_THE_SHOULDERS_OF`, two words. The paragraph is reader-facing and good; it opens
     *"Back matter."*, which is a production label sitting in front of it.

**Both scanners gain `Book body`** so the label class cannot return by a route the shape
rule misses. `APPENDIX_D:60`'s `*Source:*` line is deliberately left alone: it is reader
attribution, not provenance -- *"this page is here so you can run them without the
original in hand."*
"""
import io, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)

NOTE = (
    "> **Note on the no-somatic directive.** The book's prose never narrates the "
    "reader's interior — that reads as manipulation, and it's barred everywhere in the "
    "body of the book. This appendix is the one deliberate exception, and it earns the "
    "exception the same way the book earns its other body claims: by sourcing them. "
    "These are three named, opt-in practices from a prior, published book of mine. The "
    "reader chooses to open this page and run them. That's a toolkit you reach for, not "
    "a felt-sense I assert about you. Keep it framed that way — invitation and lineage, "
    "never prescription mid-argument.\n\n"
)

BOOKBODY = (
    "**Book body:** Phase 1 catalog in Chapter 3; **first practice in Chapter 4** "
    "(Challenger / oppressor projection). Renumbered 2026-07-29 — the old figures were "
    "0-indexed and disagreed with `ch3.md:545`."
)

E = [
    ("appendices/APPENDIX_D_EMOTIONAL_ALCHEMY_PRACTICES.md", NOTE, ""),
    ("appendices/APPENDIX_E_321_SHADOW_PROCESS.md", BOOKBODY,
     "*Concept and catalogue: Chapter 3. First practice: Chapter 4.*"),
    ("appendices/ON_THE_SHOULDERS_OF.md",
     "*Back matter. This book is a synthesis, not an invention.",
     "*This book is a synthesis, not an invention."),

    # Both scanners: cover the label class, not just the labels that happened to exist.
    ("instruments/build_book.py",
     r'r"^\*\*(Status|Authority|Location in book|Timing dependency|Depends on|"',
     r'r"^\*\*(Status|Authority|Location in book|Book body|Timing dependency|Depends on|"'),
    ("instruments/placeholders.py",
     r"r'^\*\*(Status|Authority|Location in book|Timing dependency|Depends on|'",
     r"r'^\*\*(Status|Authority|Location in book|Book body|Timing dependency|Depends on|'"),
]


def main():
    files, bad = {}, []
    for path, old, new in E:
        files.setdefault(path, io.open(os.path.join(ROOT, path), encoding="utf-8").read())
        n = files[path].count(old)
        if n != 1:
            bad.append("%s: matched %d times — %r" % (path, n, old[:56]))
            continue
        files[path] = files[path].replace(old, new, 1)
    if bad:
        print("ABORTED, nothing written:")
        for b in bad:
            print("  " + b)
        return 1
    # Collapse the blank run the blockquote left behind, header block only.
    k = "appendices/APPENDIX_D_EMOTIONAL_ALCHEMY_PRACTICES.md"
    head, sep, rest = files[k].partition("\n---\n")
    files[k] = re.sub(r"\n{3,}", "\n\n", head).rstrip() + "\n" + sep + rest
    if "--dry" not in sys.argv:
        for path, t in files.items():
            io.open(os.path.join(ROOT, path), "w", encoding="utf-8").write(t)
    print("%d edit(s) %s" % (len(E), "checked" if "--dry" in sys.argv else "applied"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
