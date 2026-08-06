# -*- coding: utf-8 -*-
"""
glossary_check.py -- keeps `back_matter/glossary.md` answerable to the book.

Wendell 2026-08-05: *"let's do the glossary."* The book has not had one since DL-8
retired `APPENDIX_C_KEY_TERMS.md` on 2026-07-30, and that retirement is the whole reason
this file exists. The old glossary was not badly written. It was **written once, against
a spec, and never checked again**, so it went on defining a book that had stopped
existing: the wrong six for *The Face*, *Gate* as one of eight threshold moments, a
Vulnerable Child that had left ch2's roster, chapter tags 0-indexed against a Ch0 that
is now Chapter 1, and fifty-one references to trigrams and hexagrams the manuscript no
longer contains.

A glossary is the one back-matter component that rots silently. The index points at
locations and a moved section breaks it loudly; a definition keeps reading fine forever
while the chapter underneath it changes.

Three checks. The third is the one that matters.

  1. **Every headword appears in the book.** An entry for a term the manuscript does not
     use is the retired glossary's failure in miniature.

  2. **Every cited locator holds its term.** Same rule as `index_build.py`: if a section
     moved, the pointer is wrong and the build says so rather than shipping it.

  3. **Every coined term in the index has an entry.** This is the reverse direction, and
     it is the check the old glossary had no version of.
     `AUDIT_GAME_LOOP_CONFORMANCE_2026-07-30.md:77` reports *"there is no BAR entry in
     the shipping glossary"* and its recommendation 2 says to add one -- a live
     instruction with no target for the ten months since. Nothing in the repo could see
     the gap, because a missing entry looks exactly like a glossary that is finished.

Sources are exempt from check 3. Appendix G credits them at length and a glossary that
also defined Gendlin would be a second, shorter, drifting copy of it. Game moves are
exempt too: the roster is in ch3 through ch8 by name, each one is a sentence in the
imperative, and a definition would restate the name.

    python3 instruments/glossary_check.py
    python3 instruments/glossary_check.py --quiet
"""
import io, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, os.pardir))
sys.path.insert(0, HERE)

GLOSSARY = os.path.join(ROOT, "back_matter", "glossary.md")

# Index groups whose terms must each have a glossary entry. See the docstring for why
# `Sources` and `Game moves` are not here.
REQUIRED_GROUPS = ["The six Faces", "The daemons", "The five channels", "Practices",
                   "The world", "The four domains", "Concepts"]

# An index term whose glossary entry is a different headword, or which is deliberately
# covered by a collective entry. Each one is a judgement and carries its reason.
COVERED = {
    "Metal / fear": "Channels, the five", "Water / sadness": "Channels, the five",
    "Wood / joy": "Channels, the five", "Fire / anger": "Channels, the five",
    "Earth / neutrality": "Channels, the five",
    "wonder (fear completed)": "Completed states, the five",
    "poignance (sadness completed)": "Completed states, the five",
    "triumph (anger completed)": "Completed states, the five",
    "bliss (joy completed)": "Completed states, the five",
    "peace (neutrality completed)": "Completed states, the five",
    "Wake Up": "WAVE-Spiral, the", "Open Up": "WAVE-Spiral, the",
    "Clean Up": "WAVE-Spiral, the", "Grow Up": "WAVE-Spiral, the",
    "Show Up": "WAVE-Spiral, the",
    "School of the Body": "Schools, the six", "School of the Line": "Schools, the six",
    "School of the Oath": "Schools, the six", "School of the Pattern": "Schools, the six",
    "School of the Bridge": "Schools, the six", "School of the Horizon": "Schools, the six",
    "Gather Resources": "Allyship domains, the four",
    "Raise Awareness": "Allyship domains, the four",
    "Direct Action": "Allyship domains, the four",
    "Skillful Organizing": "Allyship domains, the four",
    "Shaman": "Shaman, the", "Challenger": "Challenger, the", "Regent": "Regent, the",
    "Architect": "Architect, the", "Diplomat": "Diplomat, the", "Sage": "Sage, the",
    "Protector": "Protector, the", "Controller": "Controller, the",
    "Skeptic": "Skeptic, the", "Fixer/Healer": "Fixer/Healer, the",
    "Emotional Body": "Emotional Body, the", "Victim": "Victim, the",
    "Damaged Self": "Damaged Self, the",
    # Borrowed terms the book runs on. Appendix G owns the lineage; the glossary carries
    # the two that are equipment a reader picks up and uses.
    "felt sense": None, "existential kink": None, "leverage point": None,
    "evolutionary purpose": None, "pre/trans fallacy": None,
    "transcend and include": None, "separation of tasks": None,
    "renewable fuel": None,
}


def entries():
    """Headword -> the locators cited in its trailing italic."""
    out = {}
    for m in re.finditer(r"^\*\*(.+?)\*\* — (.+?)(?=\n\n|\Z)", io.open(GLOSSARY, encoding="utf-8").read(), re.S | re.M):
        head, body = m.group(1), " ".join(m.group(2).split())
        cite = re.search(r"\*([^*]+)\*\s*$", body)
        locs = re.findall(r"(?:Ch|App) [0-9A-G](?: §\d+)?", cite.group(1)) if cite else []
        out[head] = locs
    return out


def main():
    quiet = "--quiet" in sys.argv
    from index_build import TERMS, surfaces, locator, order
    glos = entries()
    docs = surfaces()
    missing_term, bad_loc, missing_entry = [], [], []

    # Resolve each headword to the index's own regex for that term. The first draft
    # searched the headword string itself and reported three false locator failures --
    # a glossary cites where a CONCEPT is taught, and the chapter teaching it often
    # never uses the glossary's phrasing. `Allyship domains, the four` is taught at
    # Ch 2 §10 by naming all four, and the phrase itself appears only in Appendix A.
    heads = {h.split(",")[0].strip().lower(): h for h in glos}
    pat_for, inv = {}, {}
    for g, rows in TERMS.items():
        for display, pat in rows:
            inv.setdefault(COVERED.get(display) or display, []).append(pat)
    for head in glos:
        pats = inv.get(head) or inv.get(head.split(",")[0].strip()) or []
        if pats:
            pat_for[head] = "|".join("(?:%s)" % p for p in pats)
    for head, locs in glos.items():
        rx = pat_for.get(head) or re.escape(head.split(",")[0].split("(")[0].strip())
        found = {}
        for label, rel, text in docs:
            if rel.startswith("back_matter/glossary"):
                continue
            for m in re.finditer(rx, text, re.I):
                found.setdefault(locator(label, rel, text, m.start()), 0)
                found[locator(label, rel, text, m.start())] += 1
        if not found:
            missing_term.append(head)
            continue
        for loc in locs:
            if loc not in found:
                # Book order, not alphabetical. The first draft showed sorted(found)[:4],
                # which put App A through App G in front of every chapter and read as
                # "found in the appendices only" for a term that is in seven chapters.
                # A truncation that hides the relevant half is worse than a long line.
                ordered = sorted(found, key=order)
                shown = ", ".join(ordered[:6])
                if len(ordered) > 6:
                    shown += " (+%d more)" % (len(ordered) - 6)
                bad_loc.append((head, loc, shown))

    for group in REQUIRED_GROUPS:
        for display, _pat in TERMS.get(group, []):
            if display in COVERED:
                continue
            stem = display.split(",")[0].split("(")[0].strip()
            if stem.lower() not in heads and display not in glos:
                missing_entry.append("%s (%s)" % (display, group))

    n = len(missing_term) + len(bad_loc) + len(missing_entry)
    if not quiet or n:
        print("=" * 78)
        print("glossary — %d entries" % len(glos))
        print("=" * 78)
        for label, rows in (("HEADWORD NOT IN THE BOOK", missing_term),
                            ("MISSING ENTRY — a coined term the index carries", missing_entry)):
            print("\n%s\n%s" % (label, "-" * len(label)))
            print("\n".join("  %s" % r for r in rows) if rows else "  none")
        print("\nCITED LOCATOR DOES NOT HOLD THE TERM\n" + "-" * 35)
        print("\n".join("  %-28s cites %-10s found in %s" % b for b in bad_loc) if bad_loc else "  none")
        print("\n%d finding(s)." % n)
    return 1 if n else 0


if __name__ == "__main__":
    sys.exit(main())
