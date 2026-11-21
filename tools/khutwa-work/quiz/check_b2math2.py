# Verifies every computational question of b2math2_quiz.json.
# 3rd field of each tuple in src_b2math2/chN.py is an independent solve (numeric: finite differences,
# Simpson integration, grid search, enumeration of outcomes). EXACTLY ONE option must equal it, and it must be "a".
# kinds:  expr -> number / list (unordered set, options joined by " أو ") / tuple (ordered, " ، ")
#   F:expr   function of x,t,a,b,n,h compared at sample points (options may start with "ص = " / end with "+ ث")
#   I:lo,hi:pred   inequality options compared with predicate pred(v) on a grid of [lo,hi]
#   G:f:count  general solution in n: every value must satisfy f(t)=0 and give `count` distinct angles mod 2pi
#   U   -> the option saying "غير معرّفة"
import json, re, math, importlib.util, os, itertools, sys
from math import comb, factorial, sqrt, pi, sin, cos, tan, log, atan, exp
from fractions import Fraction as Fr
D='/home/claude/khutwa/quiz/src_b2math2'
quiz=json.load(open('/home/claude/khutwa/quiz/b2math2_quiz.json'))['by']
# ---------- helpers for the independent solves ----------
def LOG(b,x): return log(x)/log(b)
def Dx(f,x,h=1e-5): return (f(x+h)-f(x-h))/(2*h)
def D2(f,x,h=1e-4): return (f(x+h)-2*f(x)+f(x-h))/(h*h)
def INT(f,a,b,n=2000):
    h=(b-a)/n; s=f(a)+f(b)
    for i in range(1,n): s+=(4 if i%2 else 2)*f(a+i*h)
    return s*h/3
def SOL(f,lo=0,hi=2*pi,step=pi/12,inc_hi=False):
    r=[]; k=0
    while lo+k*step<hi-1e-9 or (inc_hi and abs(lo+k*step-hi)<1e-9):
        t=lo+k*step
        try:
            if abs(f(t))<1e-9: r.append(t)
        except Exception: pass
        k+=1
    return r
def ROOTS(f,lo,hi,n=20000):
    r=[]; h=(hi-lo)/n; p=f(lo)
    if abs(p)<1e-12: r.append(lo)
    for i in range(1,n+1):
        x=lo+i*h; q=f(x)
        if abs(q)<1e-12: r.append(x)
        elif abs(p)>=1e-12 and p*q<0:
            a,b=x-h,x
            for _ in range(60):
                m=(a+b)/2
                if f(a)*f(m)<=0: b=m
                else: a=m
            r.append((a+b)/2)
        p=q
    return r
def GRID(lo,hi,n=24000): return [lo+(hi-lo)*i/n for i in range(n+1)]
def MAX(f,lo=0,hi=2*pi): return max(f(x) for x in GRID(lo,hi))
def MIN(f,lo=0,hi=2*pi): return min(f(x) for x in GRID(lo,hi))
def ARGMAX(f,lo=0,hi=2*pi,closed=False):
    G=GRID(lo,hi); x=max(G if closed else G[:-1],key=f); h=(hi-lo)/24000
    a,b=max(lo,x-h),min(hi,x+h)
    for _ in range(200):          # ternary refinement around the best grid point
        m1,m2=a+(b-a)/3,b-(b-a)/3
        if f(m1)<f(m2): a=m1
        else: b=m2
    return (a+b)/2
def ARGMIN(f,lo=0,hi=2*pi,closed=False): return ARGMAX(lambda x:-f(x),lo,hi,closed)
def PER(f):
    for k in range(1,65):
        p=k*pi/8
        if all(abs(f(t+p)-f(t))<1e-9 for t in (0.123,0.77,1.9,2.6,4.4)): return p
R=range(-30,31)
def SC(f,lo,hi,n=900):            # number of sign changes on an offset grid
    xs=[lo+(hi-lo)*(i+0.3819)/n for i in range(n)]; v=[f(x) for x in xs]
    return sum(1 for i in range(n-1) if v[i]*v[i+1]<0)
def NEXT(f,lo=-10,hi=10,n=700): return SC(lambda x: Dx(f,x),lo,hi,n)     # number of local extrema
def nreal(f,lo=-12,hi=12):         # distinct real roots: crossings + tangency points
    crit=ROOTS(lambda x: Dx(f,x),lo,hi,4000)
    touch=[c for c in crit if abs(f(c))<1e-6]
    cross=[r for r in ROOTS(f,lo+0.000123,hi,4000) if all(abs(r-c)>1e-3 for c in touch)]
    return len(cross)+len(touch)
# distributions: dict value -> Fraction probability
def dist(pairs):
    d={}
    for v,p in pairs: d[v]=d.get(v,0)+Fr(p)
    assert sum(d.values())==1,d
    return d
def coins(n): return dist((sum(c),Fr(1,2**n)) for c in itertools.product((0,1),repeat=n))
def die(): return dist((v,Fr(1,6)) for v in range(1,7))
def draw(red,other,n):   # number of red among n drawn without replacement
    items=[1]*red+[0]*other; cs=list(itertools.combinations(range(len(items)),n))
    return dist((sum(items[i] for i in c),Fr(1,len(cs))) for c in cs)
def E(d,g=lambda v:v): return sum(g(v)*p for v,p in d.items())
def V(d,g=lambda v:v): return E(d,lambda v:g(v)**2)-E(d,g)**2
def SD(d,g=lambda v:v): return sqrt(V(d,g))
def joint(d1,d2,g): return dist((g(u,v),p*q) for u,p in d1.items() for v,q in d2.items())
# ---------- option parser ----------
FUN={'sin','cos','tan','sqrt','LOG','abs'}
PTS=[dict(x=1.3,t=0.7,a=0.4,b=1.1,n=3,h=0.37,y=2.3,A=1.7,B=0.6,K=2.2,M=0.9),
     dict(x=-0.6,t=2.2,a=1.7,b=3.4,n=4,h=1.21,y=0.9,A=2.9,B=1.4,K=0.7,M=1.6),
     dict(x=2.7,t=3.85,a=-1.2,b=0.8,n=7,h=-0.52,y=1.6,A=0.8,B=2.1,K=3.1,M=2.4)]
def norm(s):
    s=s.strip().replace('−','-').replace('–','-').replace('×','*').replace('÷','/').replace('^','**').replace('°','')
    s=s.replace('≤','<=').replace('≥','>=')
    s=re.sub(r'\+\s*ث\s*$','',s)
    s=s.replace('جتا','cos').replace('جا','sin').replace('ظا','tan')
    for u,v in [('هـ','h'),('س','x'),('ص','y'),('θ','t'),('α','a'),('β','b'),('ن','n'),('أ','A'),('ب','B'),('ك','K'),('م','M'),('ت','t')]: s=s.replace(u,v)
    s=re.sub(r'لو_([0-9A-Za-z./]+)\s*\(',r'LOG(\1,',s); s=s.replace('لو(','LOG(10,')
    s=re.sub(r'(sin|cos|tan)\*\*(\d)\s*(\d*)\s*([tab])\b',lambda m:f'({m.group(1)}({m.group(3)+"*" if m.group(3) else ""}{m.group(4)}))**{m.group(2)}',s)
    s=re.sub(r'(sin|cos|tan)\s+(\d*)\s*([tab])\b',lambda m:f'{m.group(1)}({m.group(2)+"*" if m.group(2) else ""}{m.group(3)})',s)
    if re.search(r'[؀-ۿ]',s): raise ValueError('arabic left: '+s)
    tk=re.findall(r'\d+\.\d+|\d+|[A-Za-z_]+|\*\*|<=|>=|[-+*/(),<>=]',s)
    if ''.join(tk)!=re.sub(r'\s+','',s): raise ValueError('tokens: '+s)
    out=[]
    for i,x in enumerate(tk):
        if i:
            p=tk[i-1]
            L=p==')' or p[0].isdigit() or (p[0].isalpha() and p not in FUN)
            R=x=='(' or x[0].isdigit() or x[0].isalpha()
            if L and R: out.append('*')
        out.append(x)
    return ''.join(out)
def env(pt): 
    e=dict(sin=sin,cos=cos,tan=tan,sqrt=sqrt,LOG=LOG,abs=abs,pi=pi); e.update(pt); return e
def ev(o,pt=PTS[0]):
    o=o.strip()
    if ' أو ' in o: return [ev(p,pt) for p in o.split(' أو ')]
    if ' ، ' in o:
        if o.startswith('(') and o.endswith(')'): o=o[1:-1]
        return tuple(ev(p,pt) for p in o.split(' ، '))
    m=re.match(r'^[سصθتنأبكم]\s*=\s*(.+)$',o)
    if m: o=m.group(1)
    try:
        z=norm(o)
        if re.search(r'(?<![<>=])=(?!=)',z):      # an equation: value = |LHS - RHS| (0 when true)
            L,R=re.split(r'(?<![<>=])=(?!=)',z,maxsplit=1); return abs(eval(L,env(pt))-eval(R,env(pt)))
        return eval(z,env(pt))
    except Exception:
        m=re.match(r'^(-?\d+(?:\.\d+)?(?:/\d+)?)\s*(pi)?\s+[؀-ۿ]',o)
        if m: return eval(m.group(1))*(pi if m.group(2) else 1)
        raise
def close(a,b):
    try:
        if isinstance(a,list) or isinstance(b,list):
            if not(isinstance(a,list) and isinstance(b,list)) or len(a)!=len(b): return False
            b=list(b)
            for u in a:
                j=next((j for j,v in enumerate(b) if close(u,v)),None)
                if j is None: return False
                b.pop(j)
            return True
        if isinstance(a,tuple) or isinstance(b,tuple):
            return isinstance(a,tuple) and isinstance(b,tuple) and len(a)==len(b) and all(close(u,v) for u,v in zip(a,b))
        return abs(float(a)-float(b))<1e-6*max(1,abs(float(b)))
    except Exception: return False
def pred(o):
    o=o.strip()
    if 'جميع الأعداد' in o: return lambda v: True
    if 'لا يوجد' in o or 'لا توجد' in o: return lambda v: False
    parts=[norm(p) for p in o.split(' أو ')]
    def f(v):
        e=env(dict(x=v,t=v,y=v,K=v,A=v,M=v,n=v))
        return any(eval(p,e) for p in parts)
    return f
_CACHE={}
def match(o,c):
    try:
        if c=='U': return 'غير معر' in o
        if c.startswith('F:'):
            vals=[]
            for pt in PTS:
                if not close(ev(o,pt),eval(c[2:],dict(globals(),**pt))): return False
            return True
        if c.startswith('W:'):      # W:A=..;B=..:expr   options evaluated with these values of the letters
            asg,expr=c[2:].split(':',1); pt=dict(PTS[0])
            for z in asg.split(';'):
                k,v=z.split('='); pt[k]=eval(v)
            return close(ev(o,pt),eval(expr))
        if c.startswith('I:') or c.startswith('IB:'):   # IB also tests the half-integer boundary points
            B=c.startswith('IB:'); rng,p=c[(3 if B else 2):].split(':',1); lo,hi=[eval(z) for z in rng.split(',')]
            g0=eval('lambda v: '+p); f=pred(o)
            def g(v):
                try: return bool(g0(v))
                except (ValueError,ZeroDivisionError): return False
            pts=[lo+(hi-lo)*(i+0.4142)/3001 for i in range(3001)]
            if B: pts+=[k/2 for k in range(int(2*lo),int(2*hi)+1)]
            return all(bool(f(v))==g(v) for v in pts)
        if c.startswith('G:'):
            _,fs,cnt=c.split(':'); f=eval('lambda t: '+fs); vals=[]
            for n in range(-3,4):
                r=ev(o,dict(PTS[0],n=n))
                vals+= r if isinstance(r,list) else [r]
            if any(abs(f(v))>1e-9 for v in vals): return False
            S={round(v%(2*pi),5) for v in vals}; S={0.0 if abs(z-2*pi)<1e-4 else z for z in S}; return len(S)==int(cnt)
        if c not in _CACHE: _CACHE[c]=eval(c)
        return close(ev(o),_CACHE[c])
    except Exception as ex:
        return False
if __name__=='__main__':
    bad=0; n=0; tot=0
    for f in sorted(os.listdir(D)):
        if not re.match(r'ch\d\.py$',f): continue
        s=importlib.util.spec_from_file_location(f[:-3],f'{D}/{f}'); m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
        cn=0
        for name,qs in m.CH:
            for j,t in enumerate(qs):
                tot+=1
                if not t[2]: continue
                n+=1; cn+=1; q=quiz[name][j]
                assert q['q']==t[0]
                try: ev(q['o'][q['a']]) if not t[2][:2] in ('I:','IB','U') and t[2]!='U' else None
                except Exception as ex: print('PARSE-CORRECT',name,j,q['o'][q['a']],ex)
                hits=[i for i,o in enumerate(q['o']) if match(o,t[2])]
                if hits!=[q['a']]:
                    bad+=1; print('BAD',name,j,'|',q['q'][:70],'| chk=',t[2],'| opts=',q['o'],'a=',q['a'],'hits=',hits)
        print(f,'computational checked',cn)
    print('total',tot,'checked',n,'bad',bad)
