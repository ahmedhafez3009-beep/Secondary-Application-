# builds b2math2_quiz.json and b2math2_curr.json from chapter sources (ch5..ch8)
import json, importlib.util, os
from collections import Counter
D='/home/claude/khutwa/quiz/src_b2math2'
UNITS={5:"الفصل 5: الدوال المثلثية",6:"الفصل 6: الأسس واللوغاريتمات",7:"الفصل 7: التفاضل والتكامل",8:"الفصل 8: المتغيّرات العشوائية"}
def load(n):
    p=f'{D}/ch{n}.py'
    if not os.path.exists(p): return None
    s=importlib.util.spec_from_file_location(f'ch{n}',p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m.CH
by={}; curr=[]; k=0; warn=0
for n in range(5,9):
    CH=load(n)
    if CH is None: continue
    curr.append([UNITS[n],"|".join(name for name,_ in CH)])
    for name,qs in CH:
        assert '|' not in name and name not in by,name
        if len(qs)!=6: print('COUNT',name,len(qs))
        out=[]
        for t in qs:
            q,e,c,opts=t[0],t[1],t[2],list(t[3:])
            assert len(opts)==4,(name,q)
            pos=(k*3+(k//4))%4; k+=1
            cor=opts[0]; rest=opts[1:]
            o=rest[:pos]+[cor]+rest[pos:]
            if len(cor)>max(len(x) for x in rest):
                warn+=1; print('LONGEST',name,'|',q[:50],'|',cor)
            if len(set(x.strip() for x in o))<4: print('DUP',name,q[:40])
            if len(e.split())>25: print('LONG-E',name,q[:40])
            out.append({"q":q,"o":o,"a":pos,"e":e})
        by[name]=out
json.dump({"by":by},open('/home/claude/khutwa/quiz/b2math2_quiz.json','w'),ensure_ascii=False,indent=1)
json.dump({"parts":[["الجزء الثاني",curr]]},open('/home/claude/khutwa/quiz/b2math2_curr.json','w'),ensure_ascii=False)
print('lessons',len(by),'qs',sum(map(len,by.values())),'a-dist',sorted(Counter(x['a'] for v in by.values() for x in v).items()),'longest-warn',warn)
