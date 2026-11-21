# Verifies every computational question of b2math1_quiz.json:
# the check expression (3rd field in src_b2math1/chN.py, written as an independent solve)
# is evaluated here and EXACTLY ONE option must equal it, and that option must be "a".
import json, re, math, cmath, importlib.util, os
from math import comb, factorial, sqrt, gcd
from fractions import Fraction as F
D='/home/claude/khutwa/quiz/src_b2math1'
quiz=json.load(open('/home/claude/khutwa/quiz/b2math1_quiz.json'))['by']
I=1j
W=cmath.exp(2j*math.pi/3)
def nature(a,b,c):
    D=b*b-4*a*c
    return 'جذران حقيقيان مختلفان' if D>0 else 'جذر حقيقي مكرر' if D==0 else 'جذران مركبان غير حقيقيين'
def tri(P,Q,R):
    d=lambda u,v:(u[0]-v[0])**2+(u[1]-v[1])**2
    s=sorted([d(P,Q),d(Q,R),d(P,R)]); eq=lambda u,v:abs(u-v)<1e-9
    right=eq(s[0]+s[1],s[2]); iso=eq(s[0],s[1]) or eq(s[1],s[2])
    if eq(s[0],s[2]): return 'متطابق الأضلاع'
    if right and iso: return 'متطابق الساقين وقائم الزاوية'
    if right: return 'قائم الزاوية'
    return 'متطابق الساقين' if iso else 'مختلف الأضلاع'
def crel(r1,r2,d):
    r1,r2=max(r1,r2),min(r1,r2); eq=lambda u,v:abs(u-v)<1e-9
    if d>r1+r2+1e-9: return 'خارجيتان عن بعضهما'
    if eq(d,r1+r2): return 'تتماسان خارجيًا'
    if d>r1-r2+1e-9: return 'تتقاطعان في نقطتين'
    if eq(d,r1-r2): return 'تتماسان داخليًا'
    return 'إحداهما داخل الأخرى'
def lrel(r,d):
    return 'يتقاطعان في نقطتين' if d<r-1e-9 else 'يتماسان' if abs(d-r)<1e-9 else 'لا يتقاطعان'
def qroots(a,b,c):
    d=cmath.sqrt(b*b-4*a*c); return [(-b+d)/(2*a),(-b-d)/(2*a)]
def norm(s):
    s=s.strip().replace('−','-').replace('–','-').replace('×','*').replace('÷','/').replace('^','**')
    s=s.replace('sqrt','Q').replace('pi','P')
    for a,b in [('س','x'),('ص','y'),('ت','I'),('أ','A'),('ب','B'),('ج','C'),('ع','z'),('ن','N'),('ك','K'),('ω','W')]: s=s.replace(a,b)
    s=re.sub(r'(?<=[\dxyzIABCNKW)P])\s*(?=[xyzIABCNKW(QP])','*',s)
    s=re.sub(r'\)\s*(?=\d)',')*',s)
    return s.replace('Q','sqrt').replace('P','pi')
PTS=[(1.3,-0.7,0.4,1.1,2.3,0.6,3,2),(-0.6,2.2,1.7,3.4,0.9,1.9,4,5),(2.7,0.35,-1.2,0.8,1.6,2.8,7,3)]
def rec(a1,f,n):
    a=a1
    for k in range(1,n): a=f(a,k)
    return a
def envf(pt):
    x,y,z,A,B,C,N,K=pt
    return dict(x=x,y=y,z=z,A=A,B=B,C=C,N=N,K=K,comb=comb,factorial=factorial,rec=rec,W=cmath.exp(2j*math.pi/3),I=1j,sqrt=lambda v: cmath.sqrt(v) if (isinstance(v,complex) or v<0) else math.sqrt(v),pi=math.pi)
def ev(o,pt=PTS[0]):
    for sep in (' أو ',' ، '):
        if sep in o: return [ev(p,pt) for p in o.split(sep)]
    s=norm(o); env=envf(pt)
    if '=' in s and '==' not in s and '<' not in s and '>' not in s:
        L,R=s.split('=',1); return eval(f'({L})-({R})',env)
    return eval(s,env)
def close(a,b):
    try:
        if isinstance(a,list) or isinstance(b,list):
            a=list(a); b=list(b)
            if len(a)!=len(b): return False
            for u in a:
                j=next((j for j,v in enumerate(b) if close(u,v)),None)
                if j is None: return False
                b.pop(j)
            return True
        if isinstance(a,tuple) or isinstance(b,tuple):
            return isinstance(a,tuple) and isinstance(b,tuple) and len(a)==len(b) and all(close(u,v) for u,v in zip(a,b))
        return abs(complex(a)-complex(b))<1e-6*max(1,abs(complex(b)))
    except Exception: return False
def match(o,c):
    if isinstance(c,str):
        if c.startswith('EQ:'):   # equation equal up to a nonzero factor
            f=eval('lambda x,y: '+c[3:]); r=None
            try:
                for pt in PTS:
                    g=ev(o,pt); h=f(pt[0],pt[1])
                    if abs(h)<1e-9: 
                        if abs(g)>1e-9: return False
                        continue
                    if r is None: r=g/h
                    elif abs(g/h-r)>1e-6: return False
                return r is not None and abs(r)>1e-9
            except Exception: return False
        return o.strip()==c.strip()
    if isinstance(c,tuple) and c and c[0]=='F':
        try: return all(close(ev(o,pt),eval(c[1],envf(pt))) for pt in PTS)
        except Exception: return False
    if callable(c):
        try: return all(close(ev(o,pt),c(*pt[:2])) for pt in PTS)
        except Exception: return False
    try: return close(ev(o),c)
    except Exception:
        m=re.match(r'\s*(-?\d+(?:\.\d+)?(?:/\d+)?)\s+[\u0600-\u06FF]',o)
        return bool(m) and close(eval(m.group(1)),c)
bad=0; n=0
for f in sorted(os.listdir(D)):
    if not re.match(r'ch\d\.py$',f): continue
    s=importlib.util.spec_from_file_location(f[:-3],f'{D}/{f}'); m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
    for name,qs in m.CH:
        for j,t in enumerate(qs):
            if not t[2]: continue
            n+=1; c=(('F',t[2][2:]) if t[2].startswith('F:') else t[2][2:] if t[2].startswith('T:') else t[2] if t[2].startswith('EQ:') else eval(t[2]))
            q=quiz[name][j]
            hits=[i for i,o in enumerate(q['o']) if match(o,c)]
            if hits!=[q['a']]:
                bad+=1; print('BAD',name,j,'|',q['q'][:60],'| calc=',c if not callable(c) else 'fn','| opts=',q['o'],'a=',q['a'],'hits=',hits)
print('checked',n,'bad',bad)
