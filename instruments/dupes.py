import re, collections, glob
for f in sorted(glob.glob('/home/claude/ch[2-9].md')):
    t=open(f).read()
    s=[x.strip() for x in re.split(r'(?<=[.!?])\s+', t) if len(x.strip())>45]
    c=collections.Counter(s)
    d=[(n,x) for x,n in c.items() if n>1]
    if d:
        print(f)
        for n,x in d: print('  ',n,x[:110])
