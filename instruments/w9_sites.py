# -*- coding: utf-8 -*-
"""
List every prose em-dash as a decision to make, one sentence at a time.

SPEC_EMDASH_AND_DENSITY 1.4: *"For every dash, ask what decision the dash
avoided, then make it."* This prints the sentence around each dash so the
question can be asked, and nothing else. It proposes no replacement, because a
mechanical conversion is the thing 1.4 rules out -- the ch3 and ch7 pass went
site by site and that is why it held its short-sentence share.

    python3 instruments/w9_sites.py ch1          # every site in ch1
    python3 instruments/w9_sites.py ch1 --wide   # with the whole paragraph
"""
import io, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, os.pardir, "manuscript")
sys.path.insert(0, HERE)
import emdash

SPLIT = re.compile(r"(?<=[.!?])\s+")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    wide = "--wide" in sys.argv
    if not args:
        print(__doc__)
        return 1
    ch = args[0].replace(".md", "")
    text = io.open(os.path.join(MS, ch + ".md"), encoding="utf-8").read()

    n = 0
    for ln, line in emdash.prose_lines(text):
        if "—" not in line:
            continue
        if wide:
            n += line.count("—")
            print("\n%s ~L%d  (%d dash)\n%s" % (ch, ln, line.count("—"), line.strip()))
            continue
        for sent in SPLIT.split(line.strip()):
            if "—" not in sent:
                continue
            for m in re.finditer("—", sent):
                n += 1
                print("\n%3d  [%s]" % (n, emdash.shape(sent, m.start())))
                print("     %s" % sent.strip())
                break  # one print per sentence; the shape line names each
    print("\n%s: %d dash-bearing site(s)" % (ch, n))
    return 0


if __name__ == "__main__":
    sys.exit(main())
