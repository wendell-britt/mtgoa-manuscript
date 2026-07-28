# -*- coding: utf-8 -*-
# Task 36: PRACTICE-EXAMPLE INVENTORY.
# What is Jordan actually handed to practice ON, and does every chapter hand her one?
import io, re, collections

L = {c: io.open('/home/claude/ch%d.md' % c, encoding='utf-8').read().split('\n') for c in range(1, 10)}

PAT = [
 ('do-it-now heading',  re.compile(r'^#{2,4}\s*(Try It Now|The One Rep|The Last Rep|Halfway|Your First BAR|Run the|Name One|In Practice|Before You)', re.I)),
 ('in-the-Village',     re.compile(r'in the Village', re.I)),
 ('quest block',        re.compile(r'^#{2,4}\s*From Card to Quest', re.I)),
 ('twenty cards',       re.compile(r'^#{2,4}\s*Your Twenty Cards', re.I)),
 ('shadow draw',        re.compile(r'^#{2,4}\s*Drawing Against the Shadow', re.I)),
 ('reflection prompts', re.compile(r'^#{2,4}\s*Reflection Prompts', re.I)),
 ('winning-when test',  re.compile(r"You're winning when|You are winning when", re.I)),
 ('BAR capture',        re.compile(r'capture it as a BAR|two minutes to capture', re.I)),
 ('polarity encounter', re.compile(r'^#{2,4}\s*Polarity Encounter', re.I)),
 ('scenario label',     re.compile(r'\*\*(Example|Scenario)\b|In practice:', re.I)),
]

print('=== PRACTICE SURFACE BY CHAPTER (counts) ===')
print('%-22s %s' % ('device', '  '.join('ch%d' % c for c in range(1, 10))))
grid = {}
for name, R in PAT:
    row = []
    for c in range(1, 10):
        n = sum(1 for l in L[c] if R.search(l))
        row.append(n); grid[(name, c)] = n
    print('%-22s %s' % (name, '  '.join('%3d' % n for n in row)))

print()
print('=== EVERY DO-IT-NOW / IN-THE-VILLAGE HEADING, IN READING ORDER ===')
HD = re.compile(r'^#{2,4}\s*(.*)')
for c in range(1, 10):
    for i, l in enumerate(L[c], 1):
        m = HD.match(l)
        if not m: continue
        t = m.group(1).strip()
        if re.search(r'Try It Now|One Rep|Halfway|Run the|Name One|In Practice|First BAR|Village|Before You|Put the Book', t, re.I):
            print('  ch%d:%-5d %s' % (c, i, t))

print()
print('=== THE TRANSFER TEST: is Jordan ever given a situation and asked to CHOOSE a face/move? ===')
CHOOSE = re.compile(r'which (face|move|game|card) (would|do) you|which one (does|do) (this|the) (moment|situation)'
                    r'|pick the (face|move|card)|choose the (face|move|card)|what would you (play|draw|reach for)'
                    r'|which face does this|which (face|move) the moment needs'
                    r'|write down .{0,40}which (face|move)', re.I)
hits = 0
for c in range(1, 10):
    for i, l in enumerate(L[c], 1):
        if CHOOSE.search(l):
            hits += 1; print('  ch%d:%-5d %s' % (c, i, l.strip()[:190]))
if not hits: print('  NONE FOUND across all nine chapters.')

print()
print('=== QUEST: how is the reader\'s own quest carried forward? ===')
Q = re.compile(r'\bquest\b', re.I)
for c in range(1, 10):
    ns = [(i, l.strip()) for i, l in enumerate(L[c], 1) if Q.search(l)]
    print('  ch%-2d  n=%d  %s' % (c, len(ns), ', '.join('%d' % i for i, _ in ns[:14])))
