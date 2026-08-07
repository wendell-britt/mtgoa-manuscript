# -*- coding: utf-8 -*-
"""
The 74 em-dashes the arrow filter was hiding, brought back under cap.

emdash.py skipped any line containing an arrow, so every prose sentence using the
book's own channel notation (Fire/Anger → Triumph) was invisible to the counter.
Fixing the filter exposed 74 real em-dashes in 8 chapters. Raising the budget is
Wendell's call, so these come out instead.

Three uniform families do most of the work:

  ch7 Translate headers   "When a field is X — three adjectives — the Translate move…"
                          A textbook parenthetical. Takes parentheses, 18 sites.
  BAR exercise prompts    "*You named it out loud — or you watched yourself not…*"
                          Single tail before a lowercase clause. Takes a comma.
  chapter recap lines     long summary sentences using dashes as list brackets.
                          Handled individually; ch3's also names two retired Moves.

ch8's five `[DISSATISFACTION → SATISFACTION] X — **Y** → *Z*` labels are left alone
deliberately: they are bracket labels, and tracker A1 removes the brackets outright.
Fixing their punctuation now would be work thrown away.

    python3 instruments/emdash_hidden.py --dry
    python3 instruments/emdash_hidden.py
"""
import io, os, re, sys

MS = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "manuscript")

# --- family 1: ch7's Translate headers. "X — aaa, bbb, ccc — Y" -> "X (aaa, bbb, ccc) Y"
PAIR = re.compile(r" — ([a-z][^—\n]{4,60}?) — (?=the Translate move|the terms agreed)")

# --- family 2: single tail before a lowercase continuation, inside italic BAR prompts
TAIL = re.compile(r" — (?=[a-z])")

FAMILY1 = ["ch7.md"]
# lines where a bare single-tail -> comma is right, addressed by exact anchor
SINGLES = {
"ch3.md": [
 ("ruled a feeling out of order before you could act on it — a read you talked",
  "ruled a feeling out of order before you could act on it, a read you talked"),
 ("*Draw one card from your twenty — by hand, or let the app deal it.",
  "*Draw one card from your twenty, by hand or by letting the app deal it."),
],
"ch4.md": [
 ("Wood stuck is defiance with no future in it — the no that is only a no,",
  "Wood stuck is defiance with no future in it: the no that is only a no,"),
 ("The Refusal's opposing force is Earth gone flat — compliance that has stopped",
  "The Refusal's opposing force is Earth gone flat: compliance that has stopped"),
 ("Naming a cost requires the sadness underneath the anger — what it costs to watch",
  "Naming a cost requires the sadness underneath the anger, which is what it costs to watch"),
 ("The demand clarifies your own non-negotiables — the places where you will not move",
  "The demand clarifies your own non-negotiables, the places where you will not move"),
 ("The line you drew is not just stated — it is backed.",
  "The line you drew is stated and also backed."),
 ("It does not eliminate the charge — it stores it.",
  "It does not eliminate the charge. It stores it."),
 ("You express the charge, but for the audience — not the line.",
  "You express the charge for the audience rather than for the line."),
 ("*You drew a line in the Village — or you watched yourself not.",
  "*You drew a line in the Village, or you watched yourself not."),
 ("Anger, fear, sadness, joy, neutrality — one word, from your body,",
  "Anger, fear, sadness, joy, neutrality: one word, from your body,"),
 ("closed the case on a charge before you could aim it — a crossing you talked",
  "closed the case on a charge before you could aim it, a crossing you talked"),
 ("why the Skeptic is nearly impossible to catch standing on it — and why the chapter",
  "why the Skeptic is nearly impossible to catch standing on it, and why the chapter"),
],
"ch5.md": [
 ("Allegiance holds — because you chose it.", "Allegiance holds, because you chose it."),
 ("*You named an inheritance out loud — claimed it or reformed it — or you watched",
  "*You named an inheritance out loud, claimed it or reformed it, or you watched"),
 ("*Bring one inheritance you have been repairing instead of accepting — a role you keep",
  "*Bring one inheritance you have been repairing instead of accepting, a role you keep"),
],
"ch6.md": [
 ("*You named an assumption out loud in a real meeting — or you watched yourself swallow",
  "*You named an assumption out loud in a real meeting, or you watched yourself swallow"),
 ("*Bring one design you shipped fast — a fix, a process, a proposal",
  "*Bring one design you shipped fast: a fix, a process, a proposal"),
 ("why the Emotional Body is nearly impossible to catch standing on it — and why the chapter",
  "why the Emotional Body is nearly impossible to catch standing on it, and why the chapter"),
],
"ch7.md": [
 ("The fire doesn't go out — it becomes a fireplace instead of a wildfire.",
  "The fire doesn't go out. It becomes a fireplace instead of a wildfire."),
 # STALE 2026-08-04. Both halves of this pair now read "produced before you spoke": Wendell
 # ruled the half-second out of the two BAR prompts as needless precision, the sentence four
 # lines up having already named the unit. The migration ran on 2026-07-31 and the colon is in
 # the manuscript, so this is a record rather than a pending edit; re-running it is a no-op.
 ("Name what the ledger produced in the half-second before you spoke — the entry, not the feeling",
  "Name what the ledger produced in the half-second before you spoke: the entry, not the feeling"),
 ("*You named your terms in a real conversation — or you softened them",
  "*You named your terms in a real conversation, or you softened them"),
 ("that sounds aligned but isn't yet specific — the Translate move carries the structure",
  "that sounds aligned but isn't yet specific, the Translate move carries the structure"),
],
"ch8.md": [
 # STALE 2026-08-04, same ruling as the ch7 pair above.
 ("Name what the Damaged Self produced in the half-second before you spoke — the reading about yourself",
  "Name what the Damaged Self produced in the half-second before you spoke: the reading about yourself"),
 ("*You saw the thing — and you named it and stayed,",
  "*You saw the thing, and you named it and stayed,"),
],
"ch9.md": [
 ("reach out about certification (wendell@masteringallyship.com) — that's the succession",
  "reach out about certification (wendell@masteringallyship.com). That is the succession"),
 ("give other people the vocabulary — the deck is what you run the session from.",
  "give other people the vocabulary. The deck is what you run the session from."),
 ("a structure that needs to be challenged, broken, or rebuilt — that's also allyship work.",
  "a structure that needs to be challenged, broken, or rebuilt. That is also allyship work."),
 ("*The Protector showed up in your building. Not the old guardedness — something specific",
  "*The Protector showed up in your building, and not as the old guardedness. Something specific"),
 ("*The Controller showed up in your building — the standard for how it should look,",
  "*The Controller showed up in your building: the standard for how it should look,"),
 ("*The Skeptic showed up with a question about what you're building — whether it's real,",
  "*The Skeptic showed up with a question about what you're building: whether it's real,"),
 ("*The Fixer showed up in your building and pointed at something specific — an obstacle, a gap,",
  "*The Fixer showed up in your building and pointed at something specific: an obstacle, a gap,"),
 ("what's the thing that story is circling — what the Cauldron needs to transform?",
  "what's the thing that story is circling, the thing the Cauldron needs to transform?"),
 ("Set the work aside for a second — what's actually running in you,",
  "Set the work aside for a second. What is actually running in you,"),
 ("*The Damaged Self showed up in your building — what you know because of what you survived.",
  "*The Damaged Self showed up in your building: what you know because of what you survived."),
 ("Not the project — you.", "Not the project. You."),
],
}


def main():
    dry = "--dry" in sys.argv
    total = 0
    staged, bad = [], []
    for name in sorted(set(list(SINGLES) + FAMILY1)):
        p = os.path.join(MS, name)
        t = io.open(p, encoding="utf-8").read()
        n = 0
        if name in FAMILY1:
            t, k = PAIR.subn(r" (\1) ", t); n += k * 2
        for a, b in SINGLES.get(name, []):
            if t.count(a) != 1:
                bad.append((name, t.count(a), a[:55]))
            else:
                t = t.replace(a, b, 1); n += a.count("—")
        staged.append((p, t)); total += n
        if dry: print("%-9s %d em-dashes" % (name, n))
    if bad:
        print("ABORT — anchors not unique, nothing written:")
        for x in bad: print("  %s  %d matches: %r" % x)
        return 1
    if not dry:
        for p, t in staged: io.open(p, "w", encoding="utf-8").write(t)
    print("\n%s %d em-dashes" % ("would remove" if dry else "removed", total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
