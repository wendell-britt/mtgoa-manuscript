# -*- coding: utf-8 -*-
"""
Band 1 of the editorial working list: the claim errors, where a stated fact is wrong.

Band 1 held 26 findings. This applies the ones where the manuscript settles the answer
by itself -- a heading that names the stage, a chapter count that can be subtracted, a
sentence that contradicts the one before it. Where fixing the error requires a decision
about the book's system rather than a correction to it, the finding is NOT touched here
and is listed in the report instead.

Two of the 26 were closed earlier tonight and are asserted rather than re-fixed:

  CH2 C1  'Chapter 1 put the joystick in your hands' -- ch1 now contains joystick twice,
          closed by Fix 2 of the approved unearned-recall set.
  CH9 C6  'the altar' used twice as recall and defined nowhere -- closed by R4, which cut
          the term from the book.
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")

E = [
    # CH3 C1 -- the heading four lines above reads '#### Stage 4: Grow'.
    ("ch3.md",
     "Now you understand what the feeling shows you. The third stage lets that "
     "understanding actually *change* you.",
     "Now you understand what the feeling shows you. The fourth stage lets that "
     "understanding actually *change* you."),

    # CH3 C2 -- the tool table sends the Polarity Map to Chapter 5. Thirty-two lines
    # later the same chapter states 'First draw: Chapter 4. First field practice:
    # Chapter 7', and ch4 does carry a Polarity Encounter. The table is the wrong one.
    ("ch3.md",
     "| Stuck between two *rights* | Polarity Map (Chapter 5 → Chapter 7) |",
     "| Stuck between two *rights* | Polarity Map (Chapter 4 → Chapter 7) |"),

    # CH3 C3 -- five channels cannot be one per domain when the same sentence goes on to
    # say 'all four of those cards'. The domains are four; the channels are five; the
    # claim of a one-to-one mapping is the part that is wrong.
    ("ch3.md",
     "Clean Up holds the five channels, one per domain, which is why all four of those "
     "cards begin with the same verb",
     "Clean Up holds the five channels, which is why all four of those "
     "cards begin with the same verb"),

    # CH4 C1 -- the Diplomat is Chapter 7 and this is Chapter 4.
    ("ch4.md",
     "The Diplomat has a stage called Hold, five chapters from here",
     "The Diplomat has a stage called Hold, three chapters from here"),

    # CH4 C2 -- 'five stages' collides with this chapter's own five stages, Charge, Aim,
    # Act, Stand, Exit. The five being pointed at are the Shaman's WAVE stages, so they
    # get their name.
    ("ch4.md",
     "They are the same five stages you ran with the Shaman",
     "They are the same five WAVE stages you ran with the Shaman"),

    # CH5 C3 -- 'the Storyteller' is named once in the manuscript and never defined. ch4
    # names the Disruptor and defines it again at ch4:763; ch7 names the Connector and
    # glosses it in the same sentence. The definition ch5 needs is already the last line
    # of its own paragraph, so the name moves to sit on it.
    ("ch5.md",
     "That lays the Storyteller's foundation. The Regent's superpower puts",
     "That lays the foundation of the Regent's superpower, which puts"),
    ("ch5.md",
     "Not by being held. By being told, in full, to someone who can pick it up.",
     "Not by being held. By being told, in full, to someone who can pick it up. "
     "That is the Storyteller."),

    # CH6 C1 -- 'strategic design' appears once in the manuscript, here. The chapter's
    # term, used throughout, is structural design.
    ("ch6.md",
     "You've learned what strategic design is",
     "You've learned what structural design is"),

    # CH7 C2 -- the sentence in front of it says ninety seconds, which is what ch4, ch6
    # and ch8 also say. ch5 is the only one that differs, and it is longer, not shorter.
    # So the Diplomat's version is not the shortest in the book; the rest of the claim
    # is true and stands.
    ("ch7.md",
     "The Diplomat's version is the shortest in the book and the one most likely to get "
     "interrupted by a balance.",
     "The Diplomat's version is the one most likely to get interrupted by a balance."),

    # CH9 C4 -- ch1 promises the BAR deck and defines a BAR as the card. ch9 hands the
    # deck over and never uses the word, so the thread ch1 opened does not close.
    ("ch9.md",
     "**The deck.** A hundred and twenty cards: Wake Up",
     "**The deck.** A hundred and twenty BARs: Wake Up"),
]

# Closed earlier tonight. Asserted so that reverting those commits surfaces here.
CLOSED = [("ch1.md", "joystick", 2), ("ch9.md", "altar", 0)]


def main():
    for name, term, want in CLOSED:
        t = io.open(os.path.join(MS, name), encoding="utf-8").read()
        if t.count(term) != want:
            print("ABORTED — %s: %r appears %d times, expected %d"
                  % (name, term, t.count(term), want))
            return 1

    files, bad = {}, []
    for i, (name, old, new) in enumerate(E, 1):
        files.setdefault(name, io.open(os.path.join(MS, name), encoding="utf-8").read())
        n = files[name].count(old)
        if n != 1:
            bad.append("#%d %s matched %d times: %r" % (i, name, n, old[:56]))
            continue
        files[name] = files[name].replace(old, new, 1)
    if bad:
        print("ABORTED, nothing written:")
        for b in bad:
            print("  " + b)
        return 1
    if "--dry" not in sys.argv:
        for name, t in files.items():
            io.open(os.path.join(MS, name), "w", encoding="utf-8").write(t)
    print("%d edit(s) %s across %d file(s)"
          % (len(E), "checked" if "--dry" in sys.argv else "applied", len(files)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
