# -*- coding: utf-8 -*-
"""
Move Wendell's memoir out of Quill's treatise, and put a register in its place.

The rule stands from 2026-07-30: **above the signature, only the Head. Below it, only
Wendell.** ch3 and ch8 were cleared by lifting the memoir. ch5 could not be cleared the same
way, because the 330 words at the tail of Section 1 were the only evidence in that half of the
chapter that a body without governance drifts. Lift them and the section asserts it.

Wendell ruled a fourth option: *"move it below the seam and replace it with structures that
are generic that quill has seen across the cosmos. Gives a parallel structure and sets up the
biographical experience."*

So this is a swap rather than a lift.

**Out:** the memoir. Martial arts, the church, academia, the collective with no governance,
the crown worn under the hood, three crises, and the floor he never learned to offer before
the crisis. It lands at the head of Section 4, where the section's opening question --
*what did you inherit?* -- is the question the memoir answers.

**In:** clauses four through six of Quill's charter, with notes, covering the same eight beats
as the general case. Written to `HEAD_VOICE_DIAL.md` §2a (third impersonal, no *you*, fact and
record) and to her ruled tic, which is that the note is where she says the true thing. Prose
and the beat-for-beat table at `marginalia/new_prose/CH5_REGISTER.md`.

**Why the swap is clean.** The block sits alone between two horizontal rules, at the slot
every section in this chapter reserves for the turn away from the village. Both rules stay.
The section keeps its shape and changes its speaker.

    python3 instruments/ch5_memoir_move.py --dry
    python3 instruments/ch5_memoir_move.py
"""
import io, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CH5 = os.path.join(HERE, os.pardir, "manuscript", "ch5.md")
DRAFT = os.path.join(HERE, os.pardir, "marginalia", "new_prose", "CH5_REGISTER.md")

START = "I came up in traditions."
END = ("By then, the invitation to receive it has a very different shape than I wanted it "
       "to have.")
SECTION4 = "## Section 4: The Practice\n### *The Cycle of Inheritance -- How Loyalty Actually Works*"
SECTION4 = SECTION4.replace("--", "—")


def register():
    """Read the passage back out of the drafts file, below its final rule, so the script and
    the file cannot drift apart. The file is the source; this is the applicator."""
    text = io.open(DRAFT, encoding="utf-8").read()
    return text.rsplit("\n---\n", 1)[1].strip()


def main():
    dry = "--dry" in sys.argv
    t = io.open(CH5, encoding="utf-8").read()
    new = register()

    for name, s in (("START", START), ("END", END), ("SECTION4", SECTION4)):
        if t.count(s) != 1:
            raise SystemExit("%s anchor matched %d times, expected 1" % (name, t.count(s)))
    if "Clause four." in t:
        raise SystemExit("the register is already seated")

    i = t.find(START)
    j = t.find(END) + len(END)
    memoir = t[i:j].strip()

    for kind in ("<!-- MARGINALIA", "<!-- SIGNATURE", "<!-- EPIGRAPH"):
        if kind in memoir:
            raise SystemExit("a frame block sits inside the memoir; strip first")

    swapped = t[:i] + new + t[j:]
    k = swapped.find(SECTION4) + len(SECTION4)
    out = swapped[:k] + "\n\n" + memoir + swapped[k:]

    if dry:
        print("out: %3d words, %d paragraphs -- %s"
              % (len(memoir.split()), memoir.count("\n\n") + 1, memoir.split("\n")[0][:52]))
        print("in:  %3d words, %d paragraphs -- %s"
              % (len(new.split()), new.count("\n\n") + 1, new.split("\n")[0][:52]))
        print("em-dashes  out %d, in %d" % (memoir.count("—"), new.count("—")))
        print("second person in the register: %d"
              % len(re.findall(r"\byou(?:r|rs|rself)?\b", new, re.I)))
        print("numbered labels: %d" % len(re.findall(r"\*\*Clause \w+\.\*\*", new)))
        print("\nthe seam the swap leaves behind:")
        print("  ...%s" % " ".join(swapped[max(0, i - 120):i].split()))
        print("  >>> %s" % " ".join(new.split())[:100])
        print("\nwhere the memoir lands:")
        n = out.find(SECTION4)
        print("  %s" % " ".join(out[n:n + 300].split()))
        return 0

    io.open(CH5, "w", encoding="utf-8").write(out)
    print("swapped %d words of memoir for %d words of register; memoir seated in Section 4"
          % (len(memoir.split()), len(new.split())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
