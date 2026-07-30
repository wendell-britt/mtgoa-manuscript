# -*- coding: utf-8 -*-
"""
Run a command against marginalia-stripped body text, then always put the frame back.

Written 2026-07-29 after leaving the repo dirty three times in one session. Any
measurement that needs body text without the margin has to strip all nine chapters
first, and a bare `compile.py --strip` looks exactly like eight files of abandoned
edits to anyone reading `git status` — including the stop hook.

The frame is restored in a finally block, so it comes back even if the command
fails or raises.

    python3 instruments/on_body.py 'grep -c "Transmute" manuscript/ch3.md'
    python3 instruments/on_body.py 'python3 instruments/emdash.py -v'
"""
import os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
COMPILE = [sys.executable, os.path.join(HERE, os.pardir, "marginalia", "compile.py")]


def main():
    if len(sys.argv) < 2:
        print(__doc__.strip())
        return 2
    subprocess.run(COMPILE + ["--strip"], stdout=subprocess.DEVNULL, check=True)
    try:
        return subprocess.run(" ".join(sys.argv[1:]), shell=True).returncode
    finally:
        subprocess.run(COMPILE + ["--apply"], stdout=subprocess.DEVNULL, check=True)


if __name__ == "__main__":
    sys.exit(main())
