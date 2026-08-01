# -*- coding: utf-8 -*-
"""
Remove the app from v1 — the ruled and drafted portion.

Source: `drafts/APPROVED_remove_app_v1.md` and `specs/SPEC_REMOVE_APP_V1_2026-07-31.md`,
merged from master this morning. Ruled by Wendell 2026-07-31.

**The approved draft's anchors were stale and are re-derived here.** That draft was
written against master. This branch ran the W9 em-dash sweep last night, which converted
the joints in four of the six B1 sentences from em-dashes to commas, so the quoted OLD
strings no longer matched the page. The *ruling* is untouched; only the anchor text moved.
Applying the draft verbatim would have aborted on four of six, which is spec_edit.py
working correctly rather than a problem, but it is worth recording that a draft anchored
on quoted text can still go stale when another branch edits the quote.

What is applied:

  B1, six sites. "The app keeps count" comes out as a promise with no paper equivalent.
      ch3 takes the deeper cut Wendell ruled, which removes the six-week threat with it,
      leaving the paragraph to end on "You practiced it."
  Pre-draw diagnostic, Appendix A, two edits. Not shipping.
  Job A, the `→ app` routing tag, every site in manuscript/. The spec: "Strip the tag.
      Jordan still knows exactly what to do. Nothing else changes."

What is NOT applied, and why:

  B2, "A card that ends in the app is a card you read", six sites. The spec reasons it
      through and the approved draft lists it as **not yet drafted**. One line of
      reasoning is not a ruling.
  Appendix B's thirteen tags. Open ruling 5: do quests end in a capture, full stop, or
      does the capture get a named home?
  about_the_author. Open ruling 4: biography line or routing line.
  The superpower quiz. Open ruling 3.
  ch3:843's App Layer heading, ch9's routing block, ch1's four. Job C, undrafted.
"""
import io, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)

B1 = [
    ("manuscript/ch3.md",
     " The app keeps count, and it will tell you when you have been feeling deeply for "
     "six weeks and calling it allyship.",
     ""),
    ("manuscript/ch4.md",
     "the only place the pattern shows, and the reason the app keeps count.",
     "the only place the pattern shows."),
    ("manuscript/ch5.md",
     "the pattern shows nowhere else, and that is why the app keeps count.",
     "the pattern shows nowhere else."),
    ("manuscript/ch6.md",
     "that is the only place the pattern shows, and it is why the app keeps count.",
     "that is the only place the pattern shows."),
    ("manuscript/ch7.md",
     "Look at the sequence, not the verdict. That is why the app keeps count.",
     "Look at the sequence, not the verdict."),
    ("manuscript/ch8.md",
     "Look at the sequence, not the verdict, that is why the app keeps count.",
     "Look at the sequence, not the verdict, that is where the pattern shows."),

    # Section 2 — the pre-draw domain diagnostic, ruled not shipping.
    ("appendices/APPENDIX_A_FOUR_ALLYSHIP_DOMAINS.md",
     "Before you draw a card, before you open the app: **which domain is actually alive "
     "for you right now?**",
     "Before you draw a card: **which domain is actually alive for you right now?**"),
    ("appendices/APPENDIX_A_FOUR_ALLYSHIP_DOMAINS.md",
     "If you don't know, open the bars-engine app. The pre-draw diagnostic will ask you.",
     ""),
]

# Job A. Mechanical, and scoped to manuscript/ only: Appendix B's thirteen wait on a
# ruling about where a quest's capture lives.
TAG = re.compile(r"\s*→ app")
CHAPTERS = ["manuscript/ch%d.md" % i for i in range(1, 10)]


def main():
    dry = "--dry" in sys.argv
    files, bad, tags = {}, [], 0

    for path, old, new in B1:
        files.setdefault(path, io.open(os.path.join(ROOT, path), encoding="utf-8").read())
        n = files[path].count(old)
        if n != 1:
            bad.append("%s: matched %d times — %r" % (path, n, old[:56]))
            continue
        files[path] = files[path].replace(old, new, 1)

    for path in CHAPTERS:
        files.setdefault(path, io.open(os.path.join(ROOT, path), encoding="utf-8").read())
        files[path], k = TAG.subn("", files[path])
        tags += k

    if bad:
        print("ABORTED, nothing written:")
        for b in bad:
            print("  " + b)
        return 1

    if not dry:
        for path, t in files.items():
            io.open(os.path.join(ROOT, path), "w", encoding="utf-8").write(t)
    print("%d anchored edit(s) + %d routing tag(s) %s"
          % (len(B1), tags, "checked" if dry else "applied"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
