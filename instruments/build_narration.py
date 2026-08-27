# -*- coding: utf-8 -*-
"""
Narration scripts — the manuscript as something a voice can read.

Sixteen backers bought an audiobook in 2021 and nothing in this repository has
ever produced audio. This is the first step: a chapter as plain prose, with
every mark that exists for the eye removed and every mark that exists for the
ear kept.

The fourth build target, and the only one whose output a machine reads aloud:

    build_book.py     is it complete?
    typeset.py        can it be set?
    build_pdf.py      the page
    build_epub.py     the reflow
    build_narration.py the voice          <- here

WHAT GETS DROPPED, AND WHY EACH ONE IS A JUDGEMENT

  tables        A polarity map read aloud is a list of nouns with no grammar.
                Dropped, and counted, so the drop is visible rather than silent.
  marginalia    These are OTHER HANDS. SPEC_TWO_HANDS keeps the author's
                teaching voice and the fiction's voices on opposite sides of a
                membrane, and one cloned voice reading both collapses it.
                Extracted to a sidecar file so the decision stays open.
  headings      KEPT and spoken. A listener with no page needs to know where a
                section starts, and the heading is the only signpost audio has.
  emphasis      Markers stripped, words kept. Emphasis is a delivery choice; a
                narrator decides it, and asterisks read as asterisks.

    python3 instruments/build_narration.py --chapter 1
    python3 instruments/build_narration.py --all
"""
import re, io, os, sys, glob, argparse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)
MS = os.path.join(ROOT, "manuscript")
BUILD = os.path.join(ROOT, "build", "narration")

# The apparatus frames, from MANUSCRIPT_FILE_CANON. Each is a different hand.
FRAMES = ("MARGINALIA", "EPIGRAPH-BYLINE", "SIGNATURE", "HANDBOOK", "POSTCARD")


def extract_frames(text):
    """Pull every apparatus block out of the body. Returns (body, [(kind, text)])."""
    found = []

    def take(m):
        found.append((m.group(1), m.group(2).strip()))
        return "\n"

    for kind in FRAMES:
        pattern = re.compile(
            r"<!-- (%s) -->\n(.*?)\n<!-- /%s -->" % (re.escape(kind), re.escape(kind)),
            re.S,
        )
        text = pattern.sub(take, text)
    # Any stray comment that survived is still not for the ear.
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    return text, found


def strip_tables(text, tally):
    """Drop pipe tables. Counted, never silent — see the module docstring."""
    out, dropped = [], 0
    for line in text.split("\n"):
        if re.match(r"^\s*\|", line):
            dropped += 1
            continue
        out.append(line)
    tally["table lines dropped"] = dropped
    return "\n".join(out)


def uncaps(head):
    """
    THE INFINITE ARCADE -> The Infinite Arcade.

    Chapter titles are set in caps for the page. A synthesis engine reads caps
    as shouting or, on short runs, as an acronym to spell out. The caps are
    typography, so they come off before the voice sees them.

    A run is what gets tested, not the whole heading. "CHAPTER 1: THE INFINITE
    ARCADE — What You Spend" is majority lowercase overall, so a ratio taken
    across the line reads it as fine and leaves the shouting in.
    """
    small = {"a", "an", "and", "the", "of", "or", "to", "in", "on", "for", "at"}

    def fix(m):
        words = []
        for i, w in enumerate(m.group(0).split()):
            lw = w.lower()
            words.append(lw if (i and lw in small) else lw.capitalize())
        return " ".join(words)

    # Two or more consecutive words in caps, each at least two letters. Leaves
    # a lone acronym alone, which is the one case where caps carry meaning.
    head = re.sub(r"\b[A-Z][A-Z'’]{1,}(?:\s+[A-Z][A-Z'’]{1,}|\s+(?:a|an|and|the|of|or|to|in|on|for|at)\b)+",
                  fix, head)
    # A lone caps word before a numeral is the one that opens every chapter,
    # and it is the first thing a listener hears.
    return re.sub(r"^([A-Z]{2,})(?=\s+\d)", lambda m: m.group(1).capitalize(), head)


def spoken_headings(text, tally):
    """A heading becomes its own sentence. Audio has no other signpost."""
    out, n = [], 0
    for line in text.split("\n"):
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            head = uncaps(m.group(2).strip().rstrip("."))
            # "CHAPTER 1: THE INFINITE ARCADE — What You Spend" reads badly in
            # caps-lock and worse with the colon swallowed. Give it a stop.
            head = re.sub(r"\s*[—–-]\s*", ". ", head, count=1) if ":" in head else head
            head = head.replace(":", ".")
            out.append(head + ("." if not head.endswith((".", "?", "!")) else ""))
            n += 1
            continue
        out.append(line)
    tally["headings spoken"] = n
    return "\n".join(out)


def inline(text):
    """Marks for the eye, removed. Words kept."""
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)          # images
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)      # links -> label
    text = re.sub(r"`([^`]+)`", r"\1", text)                  # code spans
    text = re.sub(r"\*\*\*([^*]+)\*\*\*", r"\1", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    text = re.sub(r"_([^_]+)_", r"\1", text)
    text = re.sub(r"^\s*[-*+]\s+", "", text, flags=re.M)      # bullets -> sentences
    text = re.sub(r"^\s*\d+\.\s+", "", text, flags=re.M)
    text = re.sub(r"^\s*>\s?", "", text, flags=re.M)          # stray quote marks
    text = re.sub(r"^\s*(---+|\*\*\*+|___+)\s*$", "", text, flags=re.M)  # rules
    return text


def punctuation(text):
    """Marks the ear hears, normalised for a synthesis engine."""
    text = text.replace(u"‑", "-").replace(u"⁠", "")   # typeset artefacts
    text = re.sub(r"\s*[—–]\s*", ", ", text)   # em dash -> a comma's worth of pause
    text = text.replace(u"…", "...")
    text = text.replace(u"“", '"').replace(u"”", '"')
    text = text.replace(u"‘", "'").replace(u"’", "'")
    return text


def tidy(text):
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def narrate(path):
    raw = io.open(path, encoding="utf-8").read()
    tally = {}
    body, frames = extract_frames(raw)
    tally["apparatus blocks extracted"] = len(frames)
    body = strip_tables(body, tally)
    body = spoken_headings(body, tally)
    body = punctuation(inline(body))
    return tidy(body), frames, tally


def runtime(words, wpm=150):
    m = words / float(wpm)
    return "%dh %02dm" % (int(m // 60), int(m % 60))


def write(path, out_dir):
    label = os.path.splitext(os.path.basename(path))[0]
    text, frames, tally = narrate(path)
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    script = os.path.join(out_dir, "%s_narration.txt" % label)
    io.open(script, "w", encoding="utf-8").write(text)

    if frames:
        side = os.path.join(out_dir, "%s_apparatus.txt" % label)
        with io.open(side, "w", encoding="utf-8") as fh:
            for kind, block in frames:
                fh.write("[%s]\n%s\n\n" % (kind, block))

    words = len(text.split())
    print("  %-6s %7d words  %7d chars  %s  %s" % (
        label, words, len(text), runtime(words),
        " · ".join("%s %s" % (k, v) for k, v in sorted(tally.items()) if v)))
    return words, len(text)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chapter", help="a single chapter number, e.g. 1")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--out", default=BUILD)
    a = ap.parse_args()

    if a.chapter:
        paths = [os.path.join(MS, "ch%s.md" % a.chapter)]
    elif a.all:
        paths = sorted(glob.glob(os.path.join(MS, "ch*.md")),
                       key=lambda p: int(re.search(r"ch(\d+)", p).group(1)))
    else:
        ap.error("pass --chapter N or --all")

    print("narration scripts -> %s" % os.path.relpath(a.out, ROOT))
    w = c = 0
    for p in paths:
        if not os.path.exists(p):
            sys.exit("no such chapter: %s" % p)
        dw, dc = write(p, a.out)
        w += dw
        c += dc

    if len(paths) > 1:
        print("  %-6s %7d words  %7d chars  %s" % ("TOTAL", w, c, runtime(w)))
    print("\nNARRATION OK — %d characters. Tables are dropped and apparatus is" % c)
    print("sidecarred; both are counted above rather than removed quietly.")


if __name__ == "__main__":
    sys.exit(main())
