# -*- coding: utf-8 -*-
import json,io,re
pages=json.load(io.open('ij_pages.json',encoding='utf-8'))
OVR=[('zip the situation','flip the situation'),('frustration, zip','frustration, flip'),
     ('in order to yt into','in order to fit into'),('both feet zat on','both feet flat on'),
     ('pressyeld','Pressfield')]
BUL={'\x89':1,'\x8a':2,'\x8b':3,'\x8c':4,'\x8d':5,'\x8e':6,'\x8f':7}
out=[];prev=None
md=[]
for pno,pg in enumerate(pages,1):
    for ln in pg:
        t=ln['t']
        for a,b in OVR: t=t.replace(a,b)
        t=t.replace('\xa0',' ').replace('\xad','')
        m=re.match(r'^[\x89-\x8f]¯\x9d',t)
        bullet=bool(m)
        t=re.sub(r'[\x89-\x8f]¯\x9d','',t).replace('¯','').replace('\x9d','')
        t=re.sub(r'\s+',' ',t).strip()
        if not t: continue
        sz=ln['size']
        if sz<11: continue                       # running header / page number
        if abs(ln['y']-29.5)<2: continue          # top running header
        if re.match(r"^Igniting Joy: Transforming Anger's Fire",t): continue
        kind='title' if sz>=28 else ('head' if sz>=20 else 'body')
        out.append({'p':pno,'y':ln['y'],'x':ln['x'],'k':kind,'b':bullet,'t':t})
# assemble
blocks=[];cur=None
for i,l in enumerate(out):
    newpar = (cur is None or cur['k']!=l['k'] or l['b'] or
              (cur['p']==l['p'] and l['y']-cur['y']>22) or
              (cur['p']!=l['p'] and l['k']=='body' and cur['end_par']))
    if cur is not None and cur['k']==l['k'] and l['k']!='body' and cur['p']==l['p'] and l['y']-cur['y']<=40:
        newpar=False
    if newpar:
        if cur: blocks.append(cur)
        cur={'k':l['k'],'p':l['p'],'y':l['y'],'t':[l['t']],'b':l['b'],'end_par':False}
    else:
        cur['t'].append(l['t']); cur['y']=l['y']; cur['p']=l['p']
    cur['end_par']=bool(re.search(r'[.!?][”’")]?$',l['t'])) and len(l['t'])<60
if cur: blocks.append(cur)
md=[]
for b in blocks:
    t=re.sub(r'\s+',' ',' '.join(b['t'])).strip()
    if b['k']=='title': md.append('\n\n# '+t)
    elif b['k']=='head': md.append('\n\n## '+t)
    elif b['b']: md.append('- '+t)
    else: md.append(t)
doc='\n\n'.join(md)
doc=re.sub(r'\n{3,}','\n\n',doc)
io.open('igniting_joy.md','w',encoding='utf-8').write(doc)
w=len([x for x in doc.split() if not x.startswith('#')])
print('blocks',len(blocks),'words',w)
