# -*- coding: utf-8 -*-
"""
ch7_invoice.py — split the invoice sentence, and fix the aphorism.

Wendell 2026-08-03, reading back the field pass: "split into two sentences.
These aren't causally linked. A person who doesn't send an invoice doesn't get
paid."

Two faults, and the first is mine. The field pass replaced "the field will let
you" with "nobody there will stop you" and left the `because` standing, so the
sentence now reads as though nobody stopping you were CAUSED by the invoice
principle. It is not. The principle is a separate observation that lights the
first clause up; joining them with `because` asserts a mechanism the sentence
does not have and cannot support. A full stop lets the aphorism land as an
aphorism instead of arriving as a subordinate reason.

Second, the aphorism was pointed at the wrong person. "A person who does not
send an invoice is a person nobody has to pay" makes the OTHERS the subject and
their obligation the content -- it takes a detour through everyone else to say
something about you. "Does not get paid" states the consequence where it lands.
Shorter, and the repeated `does not` gives it the balance an aphorism wants.

Contractions stay out: the clause already read "a person who does not send an
invoice", so the register was set inside the sentence being fixed.

    python3 instruments/ch7_invoice.py --dry
    python3 instruments/ch7_invoice.py
"""
import io, os, sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))
CH7 = "manuscript/ch7.md"

EDITS = [
    ("and nobody there will stop you, because a person who does not send an "
     "invoice is a person nobody has to pay.",
     "and nobody there will stop you. A person who does not send an invoice does "
     "not get paid."),
]


def main():
    dry = "--dry" in sys.argv
    full = os.path.join(ROOT, CH7)
    text = io.open(full, encoding="utf-8").read()

    for before, _a in EDITS:
        n = text.count(before)
        if n != 1:
            sys.exit("ABORT: anchor matched %d times, expected 1.\n  %s\nNothing written."
                     % (n, before[:96]))

    for before, after in EDITS:
        text = text.replace(before, after, 1)
        print("  --  %s" % before)
        print("  ++  %s" % after)

    if dry:
        print("\n--dry: %d edit verified, nothing written." % len(EDITS))
        return 0
    io.open(full, "w", encoding="utf-8").write(text)
    print("\nwrote %s, %d edit." % (CH7, len(EDITS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
