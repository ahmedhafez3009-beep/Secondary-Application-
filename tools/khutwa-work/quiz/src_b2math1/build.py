# builds b2math1_quiz.json and b2math1_curr.json from chapter sources
import json, importlib.util, sys, os
D='/home/claude/khutwa/quiz/src_b2math1'
UNITS=["الفصل 1: البراهين الجبرية","الفصل 2: المتتابعات","الفصل 3: الأعداد المركبة والمعادلات","الفصل 4: الهندسة والمعادلات"]
def load(n):
    p=f'{D}/ch{n}.py'
    if not os.path.exists(p): return None
    s=importlib.util.spec_from_file_location(f'ch{n}',p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m.CH
by={}; curr=[]; k=0; warn=0
for n in range(1,5):
    CH=load(n)
    if CH is None: continue
    curr.append([UNITS[n-1],"|".join(name for name,_ in CH)])
    for name,qs in CH:
        out=[]
        for t in qs:
            q,e,c,opts=t[0],t[1],t[2],list(t[3:])
            assert len(opts)==4,(name,q)
            pos=(k*3+ (k//4))%4; k+=1
            cor=opts[0]; rest=opts[1:]
            o=rest[:pos]+[cor]+rest[pos:]
            if len(cor)>max(len(x) for x in rest):
                warn+=1; print('LONGEST',name,'|',q[:50],'|',cor)
            if len(set(o))<4: print('DUP',name,q[:40])
            out.append({"q":q,"o":o,"a":pos,"e":e})
        by[name]=out
json.dump({"by":by},open('/home/claude/khutwa/quiz/b2math1_quiz.json','w'),ensure_ascii=False,indent=1)
json.dump({"parts":[["الجزء الأول",curr]]},open('/home/claude/khutwa/quiz/b2math1_curr.json','w'),ensure_ascii=False)
from collections import Counter
print('lessons',len(by),'qs',sum(map(len,by.values())),'a-dist',Counter(x['a'] for v in by.values() for x in v),'longest-warn',warn)
