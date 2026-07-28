import re, glob
NEG = re.compile(r'^(Not|No|Never|Nor|Neither|Don\'t|Doesn\'t|Nothing)\b')
FILES = sorted(glob.glob('/home/claude/ch[1-9].md'))
grand=0
for f in FILES:
    lines = open(f).read().split('\n')
    runs=[]
    for ln,line in enumerate(lines,1):
        if line.startswith('#') or line.startswith('|'): continue
        parts=[p.strip() for p in re.split(r'(?<=[.!?])\s+', line)]
        run=[]
        for p in parts:
            c=re.sub(r'[*_`]','',p).strip()
            if NEG.match(c): run.append(c)
            else:
                if len(run)>=2: runs.append((ln,run))
                run=[]
        if len(run)>=2: runs.append((ln,run))
    if runs:
        print('='*70); print(f, len(runs),'stacks')
        for ln,r in runs:
            print(f'  L{ln}: '+' || '.join(x[:70] for x in r))
        grand+=len(runs)
print('\nTOTAL STACKS', grand)
