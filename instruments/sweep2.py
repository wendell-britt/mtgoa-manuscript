# -*- coding: utf-8 -*-
import os as _os
MS = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), _os.pardir, 'manuscript') + _os.sep
import io
path=MS+'ch9.md'
t=io.open(path,encoding='utf-8').read()
reps=[
("That's the only definition that matters. Not what you believe about allyship. Not what you intend to do when you're calm. What you do when you're activated",
 "That's the only definition that matters. What you believe about allyship is a separate question. What you intend to do when you're calm is a separate question. This one is what you do when you're activated"),
("Like any moves, they require practice. Not theory. Practice.",
 "Like any moves, they require practice — the doing kind, repeated, which is a different thing from having read about them."),
]
for a,b in reps:
    assert a in t and t.count(a)==1, a[:80]
    t=t.replace(a,b,1)
io.open(path,'w',encoding='utf-8').write(t)
print('ok')
