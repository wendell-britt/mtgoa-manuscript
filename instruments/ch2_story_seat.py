# -*- coding: utf-8 -*-
"""ch2_story_seat.py — seat the Section 1 testimony, cut what it makes redundant.

Two edits, both ruled by Wendell 2026-08-02.

E1. The burnout paragraph out, the story in. `specs/CH1_CH2_BURNOUT_COLLISION_6FACE_2026-08-02.md`
    landed six Faces on cut for six reasons: ch1 runs the burnout argument seven times and
    names the cause three separate ways, then ch2:29 tells Jordan it "doesn't name the
    cause." The paragraph is ~70 words of theory at the exact point the section goes cold,
    in a section that had **no story in 1,782 words** — the one thing Jordan's profile says
    she never skips. Cutting it does not leave a hole, it opens the slot.

E2. The hypothetical setup at ch2:132 out. Wendell: "let's cut the hypothetical setup."
    It was E1's story told as *picture a meeting* about the reader — the same argument,
    flattened, carrying two of ch2's eight inchoatives (`goes cold`, `goes unused`) in one
    sentence pair. With the real version in Section 1 the chapter was making the argument
    twice, once in Wendell's voice and once as a hypothetical about hers. Its conclusion is
    kept and re-pointed at Section 1, which turns an orphan into a callback.

Anchors are exact and unique. A missed or duplicated anchor aborts with nothing written.
"""
import io, sys

P = "manuscript/ch2.md"

E = []

E.append((
    "We wonder why we're exhausted. Why we're burned out. Why the allyship feels like "
    "more than we can carry. (Some of us have been calling this burnout for five years. "
    "Burnout names the depletion. It doesn't name the cause.)",

    "I spent years refusing a capacity I already had.\n"
    "\n"
    "I was trained in shamanism, and I did not want to learn it. I had no affinity for "
    "the practices it draws on, and it did not feel like mine to pick up. People whose "
    "judgment I trusted had advised me never to trust the exact kind of spooky white lady "
    "now teaching me. I stayed because her chops were impeccable. That was the whole "
    "reason, and it held.\n"
    "\n"
    "She taught me to read a body. Mine first, then the bodies of everyone else. Most of "
    "what we were calling shamanism was presence, and we read the research next to the "
    "practice: the same moves keep surfacing in mainstream psychology under other names, "
    "because they work on a nervous system. Stephen Porges had already mapped why.\n"
    "\n"
    "I use it every time I teach now, in dance and in writing and in this. I can walk "
    "into a group and hold it steady, because I trust my body to read what moves in it "
    "before anybody says so.\n"
    "\n"
    "I could not do any of that while I believed the knowledge belonged to somebody else. "
    "The capacity sat in my body the whole time. Nobody was ever going to hand me "
    "permission to use it."))

E.append((
    "Picture a meeting that goes cold. The body knows exactly what is happening, maybe "
    "before anyone speaks, and the read gets set aside for the consensus, not for lack of "
    "capacity, but because body-knowing, in a certain framework, belongs to people closer "
    "to their roots, and claiming it can feel like appropriation. So the literacy gets "
    "built and the read goes unused.\n"
    "\n"
    "The body doing that reading never appropriated anything. It is yours.",

    "Your body was never appropriating anything. It is yours."))


def main():
    t = io.open(P, encoding="utf-8").read()
    for i, (a, _b) in enumerate(E, 1):
        n = t.count(a)
        if n != 1:
            sys.exit("E%d anchor matched %d times, expected 1: %r" % (i, n, a[:70]))
    for a, b in E:
        t = t.replace(a, b)
    io.open(P, "w", encoding="utf-8").write(t)
    print("ch2.md — %d edits applied" % len(E))
    return 0


if __name__ == "__main__":
    sys.exit(main())
