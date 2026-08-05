# -*- coding: utf-8 -*-
"""ch2_s1_rewrite.py — the rest of the ch2 Section 1 rewrite.

Ruled by Wendell 2026-08-02: "apply the rest of the Section 1 rewrite."

The agency pass. Wendell on the opening, 2026-08-02: *"The world is not fine. What is the
IT that is being referred to… Who is the hidden agent behind all of this. Hums are
arriving? Who sent them?"* Eleven paragraphs, one human agent, three different unnamed
referents for `It`, and a meeting that goes sideways with nobody in it.

And on the second half: *"we've set up the village here before defining what we mean by it.
We've also created this we that feels a bit unearned. This might be stronger in the 3rd
person so set up the ontological map."* `village` appears **zero times in ch1** and first
lands here inside a bolded thesis line, as established vocabulary. Appendix C defines
*Distortion* and *Exile* by reference to the village and never defines the village.

Five edits.

E1  The five opening paragraphs. Every abstraction that was doing a human verb now has a
    person behind it. The specificity is loaded into what happens rather than into invented
    particulars — the legal form is `ch1:22`, an open menu with generic actors, because the
    house rule (`MANUSCRIPT_FILE_CANON:154`) is never to narrate the reader's unnamed
    history back to her as fact. An earlier draft broke that rule with a headcount and was
    correctly rejected.

E2  The flaw named as structural, and pointed at the map rather than at "the whole thing."

E3  The thesis line into third person. A claim about the field's method has no business
    being a confession, and the unearned `we` is what let the passage claim co-membership.

E4  **The village defined at first use**, then the two halves of the diagnosis: all the
    tools in the village, and no curriculum at all for the other half. Ordered so that
    "somebody else's field" hands straight into the testimony's "I believed the knowledge
    belonged to somebody else."

E5  The confession into third person, turning to `you` for the last beat, which is where
    the reader has to be standing when `That feeling is the Shadow` arrives.

Anchors are exact and unique. A missed or duplicated anchor aborts with nothing written.
"""
import io, sys

P = "manuscript/ch2.md"

E = []

E.append((
    "It shows up closer in than the headlines: the meeting that goes sideways, the "
    "community built to hold and doesn't, the low hum of something wrong that arrives "
    "ahead of any language for it.\n"
    "\n"
    "It usually starts small. A conversation that goes wrong. A relationship that "
    "fractures over something that shouldn't have been able to break it. A moment when "
    "showing up to help turns out to have made it worse.\n"
    "\n"
    "Nothing gives it a name at first. Just the feeling, the one that shows up late at "
    "night, or early in the morning, or in the middle of a conversation that's going fine "
    "on the surface and completely wrong underneath.\n"
    "\n"
    "The feeling is this: *this isn't working.*\n"
    "\n"
    "*This isn't working* is a verdict on the work, not on you. Your effort is real. Your "
    "intentions are real. Something else is failing.\n"
    "\n"
    "That hum doesn't go away when you put down the phone. It lives in the body before it "
    "reaches the mind, and it doesn't resolve with the next action item.",

    "You do not learn that from the news. You learn it in a meeting, or a group chat, or "
    "a Sunday dinner, when somebody finally says the thing that has been sitting there for "
    "months and everybody at the table starts picking their words. Somebody gets talked "
    "over and nobody names it. Somebody names it and pays for it all week. Two people who "
    "agree with each other end up arguing about a word, while the person everybody is "
    "talking around says nothing at all.\n"
    "\n"
    "Nobody can say afterwards what broke. Everybody leaves knowing something did.\n"
    "\n"
    "Most of it starts smaller. You say the sentence you rehearsed and your friend agrees "
    "with you and never brings it up again. You call to check on the person who took the "
    "worst of it and you can hear them managing you. You defend somebody in public and "
    "they spend the next week repairing what your defense cost them.\n"
    "\n"
    "Nobody names any of it at the time. You just get the feeling, at 2am, or in the "
    "middle of a conversation going fine on the surface and wrong underneath.\n"
    "\n"
    "The feeling is this: *this isn't working.*\n"
    "\n"
    "*This isn't working* is a verdict on the method, not on you. Your effort is real. "
    "Your intentions are real. Something else is failing.\n"
    "\n"
    "You put the phone down and carry it anyway. It sits in your body before your mind "
    "finds a word for it, and no action item takes it out."))

E.append((
    "The whole thing has a structural flaw:",
    "The failure is structural. It starts with a map that covers half the ground:"))

E.append((
    "**We keep trying to fix the village without knowing what's in us.**",
    "**People keep trying to fix the village without knowing what they carry into it.**"))

E.append((
    "We see a problem. We respond. We post, we protest, we speak up, we show up. Then we "
    "wonder why three months later the problem still sits there, or worse, has grown, or "
    "has transformed into something that our original response can't touch.",

    "The village is every place with an audience: the workplace, the coalition, the family "
    "table, the group chat, anywhere other people can see what you did and adjust their "
    "read on you. Harm happens in the village, and repair has to land there, so the "
    "village is a reasonable place to have put all the tools. Allyship put all of them "
    "there.\n"
    "\n"
    "So the practice runs one direction. See a problem, respond. Post, protest, speak up, "
    "show up. Three months later the problem sits where it sat, or has grown, or has "
    "become something the response cannot reach, and the person who responded has nothing "
    "left.\n"
    "\n"
    "Nobody equipped the other half. No curriculum covers the reflex that fires before you "
    "decide anything, or the read you set aside, or the part of you that took the wheel "
    "during those forty minutes. Most training files that under private, or therapy, or "
    "somebody else's field."))

E.append((
    "If we're honest with ourselves, we've also been the one who couldn't hold it. Who "
    "froze. Who said the wrong thing. Who meant well and made it worse. Who showed up "
    "wanting to help and left feeling like the problem was us.",

    "Everybody in this work has also been the one who could not hold it. The one who "
    "froze. Who said the thing. Who meant it and made it worse. Who came to help and left "
    "certain the problem was them.\n"
    "\n"
    "You know which time was yours. You know the feeling that came with it."))


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
