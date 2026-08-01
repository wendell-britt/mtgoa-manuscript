# -*- coding: utf-8 -*-
"""
Find a line from the printed page back in canon, and file it as a note.

Wendell reads the PDF and pastes the lines that do not work. A pasted line has no
file and no line number, and it has been through a typesetter on the way — curly
quotes, an em-dash with no spaces, a hyphen where the source has none, a line
broken across a page. Searching for it literally fails on all four.

    python3 instruments/find_line.py "the sentence you pasted"
    python3 instruments/find_line.py -              # a blob on stdin, one per line
    python3 instruments/find_line.py - --file NOTES.md   # and append them as rows

## What it searches

Exactly what prints: the components in `build_book.py`'s spine, in spine order.
A line found in `drafts/` or `chapters/` would be a line the reader never saw.

It reports the surface too — **body** or **margin** — because they are different
voices with different rules, and a note about the annotator's hand is not a note
about Wendell's.

## Matching

Three passes, stopping at the first that hits:

  exact       after normalising quotes, dashes, and runs of whitespace
  fragment    the longest run of words that appears exactly once in the book,
              which is what catches a line the typesetter broke or hyphenated
  nearest     difflib against every sentence, reported with a score so a bad
              match announces itself rather than being quietly accepted

A line that matches in more than one place is reported with all of them and left
for a person. That is a real signal — `dupes.py` exists because sentences have
been duplicated across chapters before.
"""
import io, os, re, sys, glob, difflib, datetime, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)

DEFAULT_NOTES = os.path.join(ROOT, "editorial_reports",
                             datetime.date.today().isoformat(), "READ_NOTES.md")


def _load_build_book():
    spec = importlib.util.spec_from_file_location(
        "build_book", os.path.join(HERE, "build_book.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


bb = _load_build_book()

# What a typesetter does to a line on the way to the page, undone.
FOLD = {
    "‘": "'", "’": "'", "“": '"', "”": '"',
    "—": "-", "–": "-", "−": "-", "‐": "-", "­": "",
    "…": "...", " ": " ", "​": "",
}

FRAME_OPEN = re.compile(r"<!-- (MARGINALIA|EPIGRAPH-BYLINE|HANDBOOK|SIGNATURE|POSTCARD) -->")
FRAME_CLOSE = re.compile(r"<!-- /(MARGINALIA|EPIGRAPH-BYLINE|HANDBOOK|SIGNATURE|POSTCARD) -->")


def fold(text):
    for a, b in FOLD.items():
        text = text.replace(a, b)
    # Markdown emphasis is invisible on the page, so a pasted line never has it.
    text = re.sub(r"\*{1,3}|_{1,3}|`", "", text)
    return re.sub(r"\s+", " ", text).strip().lower()


def surfaces():
    """Every printed line, with where it is and which voice it is in."""
    out = []
    for kind, label, rel, level in bb.SPINE:
        if rel is None:
            continue
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            continue
        depth = 0
        for n, raw in enumerate(io.open(path, encoding="utf-8"), 1):
            line = raw.rstrip("\n")
            if FRAME_OPEN.search(line):
                depth += 1
                continue
            if FRAME_CLOSE.search(line):
                depth = max(0, depth - 1)
                continue
            if not line.strip():
                continue
            out.append({"label": label, "rel": rel, "line": n,
                        "surface": "margin" if depth else "body",
                        "text": line, "key": fold(line)})
    return out


def words(s):
    return [w for w in fold(s).split(" ") if w]


def find(query, lines):
    """(how, [hits]) — exact, then longest unique fragment, then nearest."""
    key = fold(query)
    if not key:
        return "empty", []

    hits = [l for l in lines if key and key in l["key"]]
    if hits:
        return "exact", hits

    # A line the typesetter broke arrives as two halves, or with a hyphen the
    # source never had. The longest run of its words that appears exactly once is
    # what survives that, and it is far more reliable than a similarity score.
    ws = words(query)
    for span in range(len(ws), 3, -1):
        for start in range(0, len(ws) - span + 1):
            frag = " ".join(ws[start:start + span])
            found = [l for l in lines if frag in l["key"]]
            if len(found) == 1:
                return "fragment(%d words)" % span, found
            if len(found) > 1:
                return "fragment(%d words, %d places)" % (span, len(found)), found

    scored = sorted(lines, key=lambda l: difflib.SequenceMatcher(
        None, key, l["key"]).ratio(), reverse=True)[:3]
    best = difflib.SequenceMatcher(None, key, scored[0]["key"]).ratio() if scored else 0
    return "nearest(%.0f%%)" % (best * 100), scored[:1] if best > 0.55 else []


def row(note_id, query, how, hit):
    where = "%s:%d" % (hit["rel"], hit["line"]) if hit else "—"
    label = "%s · %s" % (hit["label"], hit["surface"]) if hit else "NOT FOUND"
    quoted = (hit["text"] if hit else query).replace("|", "\\|").strip()
    return "| %s | %s | %s | %s | | | open |" % (note_id, label, where, quoted)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    notes = None
    for a in sys.argv[1:]:
        if a.startswith("--file"):
            notes = a.split("=", 1)[1] if "=" in a else DEFAULT_NOTES
    if "--file" in sys.argv:
        i = sys.argv.index("--file")
        notes = sys.argv[i + 1] if i + 1 < len(sys.argv) else DEFAULT_NOTES

    if not args:
        sys.stderr.write(__doc__.split("## What it searches")[0])
        return 1

    if args[0] == "-":
        blob = sys.stdin.read()
        # One note per line, but a pasted paragraph is one note. Blank lines split.
        queries = [q.strip() for q in re.split(r"\n\s*\n", blob) if q.strip()]
        queries = [re.sub(r"\s+", " ", q) for q in queries]
    else:
        queries = args

    lines = surfaces()
    print("searching %d printed lines across %d components\n"
          % (len(lines), len({l["label"] for l in lines})))

    rows, misses = [], 0
    for i, q in enumerate(queries, 1):
        how, hits = find(q, lines)
        nid = "N%02d" % i
        print("%s  %s" % (nid, q[:96] + ("…" if len(q) > 96 else "")))
        if not hits:
            misses += 1
            print("     NOT FOUND (%s) — check the paste, or it may be front matter "
                  "the spine does not carry\n" % how)
            rows.append(row(nid, q, how, None))
            continue
        for h in hits[:4]:
            print("     %-9s %-28s %-6s %s" % (
                how, "%s:%d" % (h["rel"], h["line"]), h["surface"],
                h["text"][:80] + ("…" if len(h["text"]) > 80 else "")))
        if len(hits) > 1:
            print("     %d places — a person has to pick, and a real duplicate is a "
                  "finding in itself" % len(hits))
        print()
        rows.append(row(nid, q, how, hits[0]))

    if notes:
        os.makedirs(os.path.dirname(notes), exist_ok=True)
        new = not os.path.exists(notes)
        with io.open(notes, "a", encoding="utf-8") as fh:
            if new:
                fh.write("# Read-through notes\n\n"
                         "Filed by `instruments/find_line.py`. One row per line "
                         "Wendell flagged.\n\n"
                         "| ID | Component · surface | Location | Line as it stands |"
                         " Why it does not work | Replacement | Status |\n"
                         "|---|---|---|---|---|---|---|\n")
            fh.write("\n".join(rows) + "\n")
        print("filed %d row(s) -> %s" % (len(rows), os.path.relpath(notes, ROOT)))

    if misses:
        print("\n%d of %d not found." % (misses, len(queries)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
