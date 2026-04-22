#!/usr/bin/env python3
"""Normalize Chapter 6 section headers to spec format."""

import re

src = "/home/workspace/manuscripts/chapters/ch6-diplomat/CHAPTER6_DIPLOMAT_FULL_DRAFT_MASTER.md"

with open(src, "r") as f:
    content = f.read()

original = content

# Section header replacements
content = re.sub(r'^# SECTION 1 — THE DIPLOMAT'S THESIS', '## Section 1: The Exile — The Diplomat\'s Thesis', content, flags=re.MULTILINE)
content = re.sub(r'^# SECTION 2 — WHAT IT IS', '## Section 2: The Distortion — What It Is', content, flags=re.MULTILINE)
content = re.sub(r'^# SECTION 3 — THE FIVE CHANNELS \(PRACTICE\)', '## Section 3: The Concept — The Five Channels', content, flags=re.MULTILINE)
content = re.sub(r'^# SECTION 4$', '## Section 4: The Practice —', content, flags=re.MULTILINE)
content = re.sub(r'^# SECTION 5$', '## Section 5: The Journey —', content, flags=re.MULTILINE)
content = re.sub(r'^# SECTION 6$', '## Section 6: The Game —', content, flags=re.MULTILINE)
content = re.sub(r'^# SECTION 7 — RECAP AND TRANSITION', '## Section 7: The Recap — Recap and Transition', content, flags=re.MULTILINE)

# Channel header replacements
content = re.sub(r'^## CHANNEL 1 — BRIDGE-BUILDER', '### Channel 1: The Bridge-Builder', content, flags=re.MULTILINE)
content = re.sub(r'^## CHANNEL 2 —', '### Channel 2: The', content, flags=re.MULTILINE)
content = re.sub(r'^## CHANNEL 3 —', '### Channel 3: The', content, flags=re.MULTILINE)
content = re.sub(r'^## CHANNEL 4 — REPAIRER', '### Channel 4: The Repairer', content, flags=re.MULTILINE)
content = re.sub(r'^## CHANNEL 5 —', '### Channel 5: The', content, flags=re.MULTILINE)

# Strip trailing whitespace
content = re.sub(r'[ \t]+\n', '\n', content)

with open(src, "w") as f:
    f.write(content)

changed_lines = []
for orig_line, new_line in zip(original.splitlines(), content.splitlines()):
    if orig_line != new_line:
        changed_lines.append((orig_line, new_line))

print(f"Total lines checked: {len(original.splitlines())}")
print(f"Lines changed: {len(changed_lines)}")
for o, n in changed_lines:
    print(f"  OLD: {o!r}")
    print(f"  NEW: {n!r}")
    print()
