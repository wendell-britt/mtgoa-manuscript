# -*- coding: utf-8 -*-
"""
kdp_keywords.py — check the seven fields against the rules, then print the links that test them.

    python3 instruments/kdp_keywords.py                      # check, and the demand pass
    python3 instruments/kdp_keywords.py --index B0XXXXXXXX   # the indexing pass, after publishing
    python3 instruments/kdp_keywords.py --write FILE         # a clickable checklist

## Why this exists

`ANALYSIS_KDP_DESCRIPTION_2026-08-27.md` §5a: *"the model proposes, the autocomplete
disposes."* A language model has no Amazon search-volume data, so every phrase it suggests
is ideation until a real search box confirms a real person types it.

**This session cannot reach Amazon** — `kdp.amazon.com` and most publishing sites are denied
at the egress proxy — so the disposing has to happen in Wendell's browser. This file does
the half that can be automated: the mechanical rules, and the exact URLs to click.

## The four mechanical rules, all checkable without Amazon

**50 bytes per field, and it is a byte limit.** A smart quote or an em dash costs two or
three, and an overflowing field can be ignored whole. So the check is on `len(f.encode())`
and on `isascii()`, not on character count.

**Spaces, not commas.** Commas are indexed as content and waste 10-15% of capacity.

**Nothing already in the title, subtitle or author name.** Amazon indexes those separately.

**No word twice across the seven fields.** Amazon concatenates all seven into one index, so
a repeat buys nothing. Word order inside a field does not matter either.

## The prohibited-terms tier is different, and it is the one that carries risk

Subjective claims (*bestseller*, *award-winning*, *#1*), competitor author names and titles,
Amazon brand terms (*Kindle Unlimited*, *Prime Reading*), time-sensitive phrases (*new
release*), and misleading category claims are **against KDP's terms**, not merely wasteful.
The rest of this file finds inefficiency; this tier finds a compliance problem.

**Sourced from publishing-industry write-ups rather than from KDP's own help pages**, which
are unreachable from here. Treat the list as a prompt to check the live terms rather than as
the terms themselves.
"""
import io, os, re, sys, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)

# The book's own metadata. Amazon indexes these separately, so a keyword field repeating any
# of it is spending bytes on coverage the listing already has.
TITLE = "Mastering the Game of Allyship A Field Guide Wendell Britt"

FIELDS = [
    "compassion fatigue helper burnout recovery",
    "emotional labor exhaustion at work",
    "setting boundaries with someone you love",
    "how to help without losing yourself",
    "people pleasing overfunctioning saying no",
    "anger sadness fear joy self regulation",
    "dei inclusion facilitation group dynamics",
]

# Against KDP's terms rather than merely wasteful. See the docstring on sourcing.
PROHIBITED = re.compile(
    r"\b(bestsell\w*|best sell\w*|#1|number one|award[- ]winning|top[- ]rated|must[- ]read"
    r"|kindle unlimited|kdp select|amazon|prime reading|new release|available now"
    r"|brand new|coming soon|free)\b", re.I)

BOOKS = "https://www.amazon.com/s?i=stripbooks&k=%s"


def check(fields, title=TITLE):
    """[(field, [problem, ...])] — every rule, in the order they cost you."""
    words, first = {}, {}
    tw = {w.lower() for w in title.split()}
    out = []
    for i, f in enumerate(fields, 1):
        bad = []
        n = len(f.encode("utf-8"))
        if n > 50:
            bad.append("OVER 50 BYTES (%d) — the whole field may be ignored" % n)
        if not f.isascii():
            bad.append("non-ASCII: %s" % "".join(sorted({c for c in f if not c.isascii()})))
        if "," in f:
            bad.append("comma — use spaces")
        m = PROHIBITED.search(f)
        if m:
            bad.append("PROHIBITED TERM: %s — against KDP's terms, not just wasteful"
                       % m.group(0))
        for w in f.split():
            lw = w.lower()
            if lw in tw:
                bad.append("already in title/author: %s" % w)
            if lw in words:
                bad.append("repeat of field %d: %s" % (first[lw], w))
            words.setdefault(lw, True)
            first.setdefault(lw, i)
        out.append((f, bad))
    return out


def demand_links(fields):
    """The pass that answers: does a real person type this. Run before publishing."""
    rows = []
    for f in fields:
        seed = " ".join(f.split()[:3])
        rows.append((f, seed, BOOKS % urllib.parse.quote_plus(seed)))
    return rows


def index_links(fields, asin):
    """The pass that answers: has Amazon associated the book with this. Run after.

    Search the phrase and the ASIN together. A listing that comes back is indexed for the
    phrase; an empty result means it is not, and a book cannot rank on a phrase it is not
    indexed for. Reported by seller-side sources rather than by Amazon, so a null result is
    a prompt to look again after the indexing window rather than proof of anything.
    """
    return [(f, BOOKS % urllib.parse.quote_plus("%s %s" % (f, asin))) for f in fields]


def main():
    asin = None
    if "--index" in sys.argv:
        i = sys.argv.index("--index")
        asin = sys.argv[i + 1] if i + 1 < len(sys.argv) else None
        if not asin:
            sys.exit("--index needs the book's ASIN")
    out = None
    if "--write" in sys.argv:
        i = sys.argv.index("--write")
        out = sys.argv[i + 1] if i + 1 < len(sys.argv) else os.path.join(
            ROOT, "marketing", "KEYWORD_CHECKLIST.md")

    L = ["# The seven fields — checked, and the links that test them", "",
         "Generated by `instruments/kdp_keywords.py`. The rules are mechanical and run here;",
         "the demand and indexing passes need a browser, because this session cannot reach",
         "Amazon.", "",
         "## The rules", "",
         "| # | field | bytes | |", "|---|---|---|---|"]
    bad = 0
    for i, (f, problems) in enumerate(check(FIELDS), 1):
        L.append("| %d | `%s` | %d | %s |"
                 % (i, f, len(f.encode()), "ok" if not problems else "**" +
                    "**; **".join(problems) + "**"))
        bad += len(problems)
    L += ["", "**%d field(s), %d bytes of 350, %s.**"
          % (len(FIELDS), sum(len(f.encode()) for f in FIELDS),
             "every rule passes" if not bad else "%d problem(s)" % bad), ""]

    L += ["## Pass 1 — does anybody type this", "",
          "Type the seed into Amazon's search box and **read the dropdown before pressing",
          "enter**. The dropdown is the demand signal; the results page is the competition.",
          "Keep the phrase only if Amazon completes it or something close to it.", "",
          "| field | seed to type | results page |", "|---|---|---|"]
    for f, seed, url in demand_links(FIELDS):
        L.append("| `%s` | **%s** | [search](%s) |" % (f, seed, url))
    L += ["", "**Then the alphabet pass on any seed worth more:** type the seed, a space, and",
          "each letter in turn — *helper burnout a*, *helper burnout b* — and harvest what",
          "Amazon completes. Free, and it is the same endpoint the paid tools resell.", ""]

    if asin:
        L += ["## Pass 2 — is the book indexed for it", "",
              "Run this **after** the book is live and the indexing window has passed: 24-72",
              "hours from publishing, and 24 hours to two weeks after a keyword change.",
              "Search the phrase together with the ASIN. The book comes back, or it is not",
              "indexed for that phrase and cannot rank on it.", "",
              "| field | check |", "|---|---|"]
        for f, url in index_links(FIELDS, asin):
            L.append("| `%s` | [search + %s](%s) |" % (f, asin, url))
        L.append("")

    text = "\n".join(L) + "\n"
    if out:
        os.makedirs(os.path.dirname(out), exist_ok=True)
        io.open(out, "w", encoding="utf-8").write(text)
        print("wrote %s — %d problem(s)" % (os.path.relpath(out, ROOT), bad))
    else:
        sys.stdout.write(text)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
