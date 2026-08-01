# -*- coding: utf-8 -*-
"""Own It -> Be It, everywhere the 3-2-1 is named. Ruled by Wendell 2026-08-01.

"We actually do need to change the appendix if it is still saying own it. The appendix
should say be it ... then remove any instances of own it in the language relating to the
three two ones."

Four sites. The appendix has been teaching "Don't report about it -- *be* it" in its own
body under a label that said Own It since it was written; the label was the only thing out
of step, which is why nothing ever caught it.

ch3's recap also carried a cross-reference that this branch made false two commits ago:
"with its first practice in Chapter 4". The practice is in Chapter 3 now. The Polarity Map
clause in the same sentence stays as it is -- ch3 still has no polarity draw until step 4
of SPEC_321_PER_CHAPTER section 9, so "first drawn in Chapter 4" remains true today.

Aborts on any missed or duplicated anchor.
"""
import io, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, os.pardir)

E = [
    ("appendices/APPENDIX_E_321_SHADOW_PROCESS.md",
     "You move from observing it, to talking with it, to owning it — and the energy",
     "You move from observing it, to talking with it, to being it — and the energy"),

    ("appendices/APPENDIX_E_321_SHADOW_PROCESS.md",
     "### Step 1 — Own It (First Person)",
     "### Step 1 — Be It (First Person)"),

    ("appendices/APPENDIX_E_321_SHADOW_PROCESS.md",
     "3. **1 — Own it:** First-person statement from the part.",
     "3. **1 — Be it:** First-person statement from the part."),

    # The appendix header still routes the reader to ch4 for the first practice.
    ("appendices/APPENDIX_E_321_SHADOW_PROCESS.md",
     "**Book body:** Phase 1 catalog in Chapter 3; **first practice in Chapter 4** (Challenger / oppressor projection).",
     "**Book body:** Taught and first practised in Chapter 3; run again in every chapter after it."),

    ("manuscript/ch3.md",
     "3-2-1 is here by name (Face it, Talk to it, Own it) with its first practice in Chapter 4",
     "3-2-1 is here by name and in practice (Face it, Talk to it, Be it), and it runs again in every chapter after this one"),
]

for i, (rel, old, new) in enumerate(E, 1):
    p = os.path.join(ROOT, rel)
    t = io.open(p, encoding='utf-8').read()
    n = t.count(old)
    if n == 0:
        raise SystemExit('MISS #%d in %s: %r' % (i, rel, old[:70]))
    if n > 1:
        raise SystemExit('DUPE %d #%d in %s: %r' % (n, i, rel, old[:70]))
    io.open(p, 'w', encoding='utf-8').write(t.replace(old, new, 1))

print('applied %d' % len(E))
