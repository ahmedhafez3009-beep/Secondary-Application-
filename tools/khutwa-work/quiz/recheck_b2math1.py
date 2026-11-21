#!/usr/bin/env python3
# Independent re-solve of b2math1 quiz (fresh script; does not use check_b2math1.py).
import json, sys, re, math, cmath, random, itertools
from fractions import Fraction as F
random.seed(7)
SRC = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/khutwa/quiz/b2math1_checked.json'
C = json.load(open('/home/claude/khutwa/quiz/b2math1_curr.json'))
D = json.load(open(SRC))['by']
LS = [l for p in C['parts'] for ch in p[1] for l in ch[1].split('|')]
ERR = []; SEEN = set()
def Q(i, j): return D[LS[i]][j]
def err(i, j, msg): ERR.append(f'L{i} q{j}: {msg} :: {Q(i,j)["q"][:50]}')

# ---------- notation converter ----------
AR = {'س':'x','ص':'y','ع':'z','أ':'a','ب':'b','ج':'c','د':'d','ن':'n','ك':'k','ر':'r','م':'m','ل':'l','ف':'p','ق':'q','ت':'I','ي':'j'}
TOK = re.compile(r"\s*(\d+\.\d+|\d+|sqrt|abs|pi|نق|[سصعأبجدنكرملفقتيαβω](?:\d|')?|[-+*/^(),|×÷−])")
def conv(s):
    s = re.sub(r'\|([^|]+)\|', r'abs(\1)', s.strip()); out = []; pos = 0; prev = None
    while pos < len(s):
        mt = TOK.match(s, pos)
        if not mt:
            if s[pos:].strip() == '': break
            raise ValueError('tok:' + s[pos:])
        t = mt.group(1); pos = mt.end()
        if t[0].isdigit(): kind, v = 'num', t
        elif t in ('sqrt', 'abs'): kind, v = 'fn', t
        elif t == 'pi': kind, v = 'var', 'pi'
        elif t == 'نق': kind, v = 'var', 'R'
        elif t[0] in AR: kind, v = 'var', AR[t[0]] + (t[1:].replace("'", 'p'))
        elif t[0] in 'αβω': kind, v = 'var', {'α':'al','β':'be','ω':'W'}[t[0]]
        elif t == '(': kind, v = '(', '('
        elif t == ')': kind, v = ')', ')'
        else: kind, v = 'op', {'^':'**','×':'*','÷':'/','−':'-'}.get(t, t)
        if prev in ('num', 'var', ')') and kind in ('num', 'var', '(', 'fn'): out.append('*')
        out.append(v); prev = kind
    return ''.join(out)
def csqrt(v):
    if isinstance(v, complex) or v < 0: return cmath.sqrt(v)
    return math.sqrt(v)
BASE = {'sqrt': csqrt, 'abs': abs, 'pi': math.pi, 'I': 1j, 'W': cmath.exp(2j*math.pi/3), '__builtins__': {}}
def ev(s, env=None):
    e = dict(BASE); e.update(env or {})
    return eval(conv(s), e)
def close(a, b):
    if isinstance(a, (tuple, list)) or isinstance(b, (tuple, list)):
        return isinstance(a, (tuple, list)) and isinstance(b, (tuple, list)) and len(a) == len(b) and all(close(u, v) for u, v in zip(a, b))
    return abs(a - b) <= 1e-7 * max(1, abs(a), abs(b))
def uniq(i, j, vals, exp_match):
    q = Q(i, j); SEEN.add((i, j))
    hits = [k for k in range(4) if exp_match(vals[k])]
    if hits != [q['a']]: err(i, j, f'expected-match {hits} vs marked {q["a"]}')
    for u, v in itertools.combinations(range(4), 2):
        if vals[u] is not None and vals[v] is not None and vals[u][0] == vals[v][0] and all(close(s, t) for s, t in zip(vals[u][1], vals[v][1])):
            err(i, j, f'options {u},{v} equivalent')
UNIT = re.compile(r'\s*(سم\^2|سم|وحدة مربعة|وحدات|فقط)\s*$')
def NUM(i, j, expected):
    vals = []
    for o in Q(i, j)['o']:
        try: vals.append(('n', [ev(UNIT.sub('', o))]))
        except Exception as ex: vals.append(None); err(i, j, f'unparsable option {o}: {ex}')
    uniq(i, j, vals, lambda v: v is not None and close(v[1][0], expected))
def pts(vars, n=6, ints=False, lo=1.3, hi=3.9):
    r = []
    for t in range(n):
        r.append({v: (random.randint(1, 9) if ints else random.uniform(lo, hi)) for v in vars.split()})
    return r
def FN(i, j, f, vars='x', ints=False, P=None, strip=None):
    """f: my independently derived function of latin-named vars; options evaluated at same points"""
    P = P or pts(vars, ints=ints)
    exp = [f(**{k: p[k] for k in vars.split()}) for p in P]
    vals = []
    for o in Q(i, j)['o']:
        if strip: o = re.sub(strip, '', o)
        try: vals.append(('f', [ev(o, p) for p in P]))
        except Exception as ex: vals.append(None); err(i, j, f'unparsable option {o}: {ex}')
    uniq(i, j, vals, lambda v: v is not None and all(close(s, t) for s, t in zip(v[1], exp)))
def parse_set(o):
    o = re.sub(r'\s*فقط\s*$', '', o.strip())
    parts = re.split(r'\s*(?:،|أو)\s*', o)
    items = []
    for p in parts:
        v = ev(p)
        items.append(tuple(v) if isinstance(v, tuple) else v)
    return items
def same_set(A, B):
    return len(A) == len(B) and all(any(close(a, b) for b in B) for a in A) and all(any(close(a, b) for a in A) for b in B)
def SET(i, j, expected):
    q = Q(i, j); SEEN.add((i, j)); sets = []
    for o in q['o']:
        try: sets.append(parse_set(o))
        except Exception as ex: sets.append(None); err(i, j, f'unparsable option {o}: {ex}')
    hits = [k for k in range(4) if sets[k] is not None and same_set(sets[k], list(expected))]
    if hits != [q['a']]: err(i, j, f'expected-match {hits} vs marked {q["a"]}')
    for u, v in itertools.combinations(range(4), 2):
        if sets[u] and sets[v] and same_set(sets[u], sets[v]): err(i, j, f'options {u},{v} equivalent')
def PT(i, j, p): SET(i, j, [tuple(p)])
def eqf(o, P):
    o = o.strip()
    l, r = o.split('=')
    return [ev(l, p) - ev(r, p) for p in P]
def prop(u, v):
    # u, v lists of values; proportional by nonzero constant?
    k = None
    for s, t in zip(u, v):
        if abs(t) < 1e-9 or abs(s) < 1e-9:
            if abs(t) < 1e-9 and abs(s) < 1e-9: continue
            return False
        if k is None: k = s / t
        elif not close(s / t, k): return False
    return True
def EQ(i, j, f, vars='x y', lo=-3.0, hi=4.0):
    """options are equations; my f(vars)=0 is the expected locus; equality up to nonzero factor"""
    q = Q(i, j); SEEN.add((i, j))
    P = pts(vars, n=7, lo=lo, hi=hi)
    exp = [f(**p) for p in P]; vals = []
    for o in q['o']:
        try: vals.append(eqf(o, P))
        except Exception as ex: vals.append(None); err(i, j, f'unparsable option {o}: {ex}')
    hits = [k for k in range(4) if vals[k] is not None and prop(vals[k], exp)]
    if hits != [q['a']]: err(i, j, f'expected-match {hits} vs marked {q["a"]}')
    for u, v in itertools.combinations(range(4), 2):
        if vals[u] and vals[v] and prop(vals[u], vals[v]): err(i, j, f'options {u},{v} equivalent')
def TXT(i, j, idx, why=''):
    SEEN.add((i, j))
    if Q(i, j)['a'] != idx: err(i, j, f'manual answer {idx} vs marked {Q(i,j)["a"]} {why}')
def TRUE1(i, j, truth):
    """truth: list of 4 booleans computed independently; exactly the marked one must be True"""
    SEEN.add((i, j))
    hits = [k for k in range(4) if truth[k]]
    if hits != [Q(i, j)['a']]: err(i, j, f'truth pattern {truth} vs marked {Q(i,j)["a"]}')
def FALSE1(i, j, truth): TRUE1(i, j, [not t for t in truth])

# ---------- small algebra helpers ----------
def pmul(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): r[i + j] += x * y
    return r
def ppow(a, n):
    r = [1]
    for _ in range(n): r = pmul(r, a)
    return r
def pdiv(a, b):  # coefficient lists high->low ; returns (q, r)
    a = [F(x) for x in a]; q = []
    while len(a) >= len(b):
        c = a[0] / b[0]; q.append(c)
        for k in range(len(b)): a[k] -= c * b[k]
        a.pop(0)
    return q, a
def pv(c, x):  # high->low
    r = 0
    for k in c: r = r * x + k
    return r
def pvl(c, x): return sum(k * x ** e for e, k in enumerate(c))  # low->high
def mexp(terms, n):
    """expand (sum coef*var)^n ; terms: list of (coef, varindex); returns dict exps->coef"""
    nv = len(terms); res = {tuple([0] * nv): 1}
    for _ in range(n):
        new = {}
        for e, c in res.items():
            for k, (cf, _) in enumerate(terms):
                e2 = list(e); e2[k] += 1; e2 = tuple(e2)
                new[e2] = new.get(e2, 0) + c * cf
        res = new
    return res
def quad_roots(a, b, c):
    d = cmath.sqrt(b * b - 4 * a * c); return [(-b + d) / (2 * a), (-b - d) / (2 * a)]
INTS = lambda v: [{v: t} for t in range(1, 8)]

# =================== Chapter 1 ===================
i = 0
FN(i, 0, lambda n: len(ppow([1, 1], n)), 'n', P=INTS('n'))
TXT(i, 1, 3); TXT(i, 2, 2)
NUM(i, 3, math.comb(5, 3))
NUM(i, 4, ppow([2, 1], 5)[3])          # low->high: (2 + x)^5
NUM(i, 5, ppow([-1, 2], 4)[2])
i = 1
TXT(i, 0, 3); TXT(i, 1, 2)
TXT(i, 2, 2, 'x^4 z^2 has degree 6')
NUM(i, 3, mexp([(1, 0), (1, 1), (1, 2)], 4)[(2, 1, 1)])
NUM(i, 4, mexp([(1, 0), (1, 1), (1, 2)], 6)[(2, 2, 2)])
NUM(i, 5, mexp([(1, 0), (-2, 1), (1, 2)], 4)[(2, 1, 1)])
i = 2
TXT(i, 0, 3)
FN(i, 1, lambda n: sum((-1) ** k * math.comb(n, k) for k in range(n + 1)), 'n', P=INTS('n'))
TXT(i, 2, 1)
NUM(i, 3, sum(math.comb(6, k) for k in range(7)))
NUM(i, 4, sum(ppow([-1, 2], 5)))
NUM(i, 5, math.comb(5, 0) + math.comb(5, 2) + math.comb(5, 4))
i = 3
TXT(i, 0, 2); TXT(i, 1, 1); TXT(i, 2, 1)
q_, r_ = pdiv([1, 5, 6], [1, 2]); assert all(v == 0 for v in r_)
FN(i, 3, lambda x: pv(q_, x))
q2, r2 = pdiv([2, -3, 0, 4], [1, -1, -1])
FN(i, 4, lambda x: pv(q2, x)); FN(i, 5, lambda x: pv(r2, x))
i = 4
TXT(i, 0, 2); TXT(i, 1, 1); TXT(i, 2, 0); NUM(i, 3, 5 - 2)
FN(i, 4, lambda x: (x * x + 1) * (x - 2) + 3 * x + 1)
q3, r3 = pdiv([2, 3, -4 - 1, 2 - 5], [2, 1]); assert all(v == 0 for v in r3)
FN(i, 5, lambda x: pv(q3, x))
i = 5
TXT(i, 0, 1); TXT(i, 1, 0)
P_ = pts('x'); tr = []
for o in Q(i, 2)['o']:
    l, r = o.split(' = '); tr.append(all(close(ev(l, p), ev(r, p)) for p in P_))
FALSE1(i, 2, tr)
FN(i, 3, lambda x: (x * x - 9) / (x * x + 3 * x))
FN(i, 4, lambda x: (x + 1) / (x - 2) * (x * x - 4) / (x * x - 1))
FN(i, 5, lambda x: (2 * x) / (x + 3) / ((4 * x * x) / (x * x - 9)))
i = 6
TXT(i, 0, 1); TXT(i, 1, 0); TXT(i, 2, 3)
FN(i, 3, lambda x: 1 / (x + 1) + 1 / (x - 1))
FN(i, 4, lambda x: 3 / (x - 2) - 2 / (x + 1))
FN(i, 5, lambda x: 2 / (x * x - 1) + 1 / (x + 1))
i = 7
TXT(i, 0, 0); TXT(i, 1, 3); TXT(i, 2, 3)
FN(i, 3, lambda x: (1 + 1 / x) / (1 - 1 / x))
FN(i, 4, lambda x, y: (1 / x - 1 / y) / (1 / x + 1 / y), 'x y')
FN(i, 5, lambda x: (x - 1 / x) / (1 + 1 / x))
i = 8
TXT(i, 0, 0); TXT(i, 1, 3); TXT(i, 2, 2)
NUM(i, 3, (3 * (-1) + 5))                       # x=-1 kills a(x+1)
a_ = F(4, 2); NUM(i, 4, 1 - a_ * a_)
NUM(i, 5, F(2 * (-2) + 1, (-2) + 1))            # cover-up at x=-2
i = 9
TXT(i, 0, 3); TXT(i, 1, 2)
FN(i, 2, lambda x, y: (x + y) ** 2 - (x - y) ** 2, 'x y')
FN(i, 3, lambda x: (x + 1) ** 3 - (x - 1) ** 3)
FN(i, 4, lambda x, y: (x ** 3 - y ** 3) / (x - y), 'x y')
FN(i, 5, lambda a, b, c, d: (a * a + b * b) * (c * c + d * d) - (a * c - b * d) ** 2, 'a b c d')
i = 10
TXT(i, 0, 3); TXT(i, 1, 2)
Pabc = [dict(a=u, b=v, c=-u - v) for u, v in [(1.3, 2.1), (-0.7, 3.3), (2.2, -5.1), (0.4, 0.9)]]
FN(i, 2, lambda a, b, c: a ** 3 + b ** 3 + c ** 3, 'a b c', P=Pabc)
NUM(i, 3, 2 ** 2 - 2 * (-3))
for a0 in (0.3, 2.7, -1.9): assert close(a0 ** 3 + (1 - a0) ** 3 + 3 * a0 * (1 - a0), 1)
NUM(i, 4, 1)
FN(i, 5, lambda a, b, c: (a + b) * (b + c) * (c + a), 'a b c', P=Pabc)
i = 11
TXT(i, 0, 2); TXT(i, 1, 1)
Pk = [dict(a=b * k, b=b, c=d * k, d=d) for b, d, k in [(1.5, 2.5, 0.7), (2.0, 3.1, -1.3), (0.6, 1.9, 2.2)]]
FN(i, 2, lambda a, b, c, d: a / b, 'a b c d', P=Pk)
NUM(i, 3, F(2 * 3 + 4, 3 + 4)); NUM(i, 4, F(1 + 2 + 3, 3 - 1)); NUM(i, 5, F(4 + 1, 2))
i = 12
TXT(i, 0, 2); TXT(i, 1, 1)
S = [(a, b) for a in (0.5, 2, 7.5) for b in (0.2, 1, 3) if a > b]
TRUE1(i, 2, [all(a * a > b * b for a, b in S), all(1 / a > 1 / b for a, b in S), all(-a > -b for a, b in S), all(a - b < 0 for a, b in S)])
TXT(i, 3, 3)
FN(i, 4, lambda x: x * x - x)
FN(i, 5, lambda a, b: a / b - (a + 1) / (b + 1), 'a b')
i = 13
TXT(i, 0, 1); TXT(i, 1, 0); TXT(i, 2, 0)
FN(i, 3, lambda a, b: a * a + 4 * b * b - 4 * a * b, 'a b')
NUM(i, 4, min(x * x - 6 * x + 10 for x in [k / 1000 for k in range(-10000, 10000)]))
TXT(i, 5, 1)
i = 14
TXT(i, 0, 1); TXT(i, 1, 0)
NUM(i, 2, (math.sqrt(2) + math.sqrt(3)) ** 2)
l_, r_ = math.sqrt(3) + math.sqrt(5), math.sqrt(2) + math.sqrt(6)
TRUE1(i, 3, [l_ < r_, close(l_, r_), l_ > r_, close(l_, math.sqrt(8))])
FN(i, 4, lambda a, b: (math.sqrt(a) + math.sqrt(b)) ** 2 - (a + b), 'a b')
TXT(i, 5, 1)
i = 15
TXT(i, 0, 0); TXT(i, 1, 3); TXT(i, 2, 3)
NUM(i, 3, min(x + 9 / x for x in [k / 1000 for k in range(1, 20000)]))
NUM(i, 4, max(w * (10 - w) for w in [k / 1000 for k in range(1, 10000)]))
NUM(i, 5, min((a + b) * (1 / a + 1 / b) for a in [k / 20 for k in range(1, 100)] for b in [k / 20 for k in range(1, 100)]))
#CH1END

# =================== Chapter 2 ===================
def seqP(k): return [{'n': t} for t in range(1, k + 1)]
def terms(lst): return lambda n: lst[n - 1]
def iterate(a1, step, k):
    r = [a1]
    for t in range(1, k): r.append(step(r[-1], t))   # a_{t+1} = step(a_t, t)
    return r
i = 16
TXT(i, 0, 0); TXT(i, 1, 3); NUM(i, 2, 2 * 3 ** 2 - 1)
FN(i, 3, terms([-1, 2, -3, 4]), 'n', P=seqP(4))
FN(i, 4, terms([F(1, 3), F(2, 5), F(3, 7)]), 'n', P=seqP(3))
FN(i, 5, terms([3, 9, 27, 81]), 'n', P=seqP(4))
i = 17
TXT(i, 0, 3)
Padn = [dict(a=1.5, d=0.7, n=5), dict(a=-2.0, d=1.3, n=8), dict(a=4.0, d=-0.6, n=3)]
FN(i, 1, lambda a, d, n: iterate(a, lambda u, t: u + d, n)[-1], 'a d n', P=Padn)
def is_ar(o):
    v = parse_set(o); return all(close(v[k + 1] - v[k], v[1] - v[0]) for k in range(len(v) - 1))
def is_ge(o):
    v = parse_set(o); return all(close(v[k + 1] / v[k], v[1] / v[0]) for k in range(len(v) - 1))
TRUE1(i, 2, [is_ar(o) for o in Q(i, 2)['o']])
NUM(i, 3, 4 - 7)
NUM(i, 4, iterate(3, lambda u, t: u + 4, 20)[-1])
FN(i, 5, terms([5, 8, 11, 14, 17]), 'n', P=seqP(5))
i = 18
TXT(i, 0, 3); TXT(i, 1, 2)
d_ = F(30 - 10, 8 - 3); a1 = 10 - 2 * d_
FN(i, 2, lambda n: a1 + (n - 1) * d_, 'n', P=seqP(8))
NUM(i, 3, [n for n in range(1, 500) if 5 + 3 * (n - 1) == 101][0])
NUM(i, 4, [x for x in range(-50, 50) if (2 * x + 1) - x == 11 - (2 * x + 1)][0])
NUM(i, 5, [n for n in range(1, 500) if 7 + 4 * (n - 1) > 100][0])
i = 19
FN(i, 0, lambda a, l, n: sum(a + k * (l - a) / (n - 1) for k in range(n)), 'a l n', P=[dict(a=1.5, l=7.5, n=5), dict(a=-2.0, l=3.0, n=8), dict(a=4.0, l=1.0, n=3)])
FN(i, 1, lambda a, d, n: sum(iterate(a, lambda u, t: u + d, n)), 'a d n', P=Padn)
TXT(i, 2, 1)
NUM(i, 3, sum(8 + k * F(32 - 8, 6) for k in range(7)))
NUM(i, 4, sum(iterate(10, lambda u, t: u - 5, 10)))
NUM(i, 5, sum(range(2, 48, 3)))
i = 20
FN(i, 0, lambda n: sum(range(1, n + 1)), 'n', P=seqP(7))
NUM(i, 1, sum(range(1, 101))); NUM(i, 2, len(range(50, 101))); NUM(i, 3, sum(range(101, 201)))
NUM(i, 4, sum(k for k in range(1, 101) if k % 3 == 0))
FN(i, 5, lambda n: sum(2 * k - 1 for k in range(1, n + 1)), 'n', P=seqP(7))
i = 21
TXT(i, 0, 1); TXT(i, 1, 0); TXT(i, 2, 0)
ps = lambda a, d, n: sum(a + k * d for k in range(n))
NUM(i, 3, [n for n in range(1, 200) if ps(4, 5, n) == 172][0])
best = max(range(1, 60), key=lambda n: ps(25, -4, n))
assert [n for n in range(1, 60) if ps(25, -4, n) == ps(25, -4, best)] == [best]
NUM(i, 4, best); NUM(i, 5, ps(25, -4, best))
i = 22
TXT(i, 0, 1)
Parn = [dict(a=1.5, r=0.7, n=5), dict(a=-2.0, r=1.3, n=6), dict(a=4.0, r=-0.6, n=3)]
FN(i, 1, lambda a, r, n: iterate(a, lambda u, t: u * r, n)[-1], 'a r n', P=Parn)
TRUE1(i, 2, [is_ge(o) for o in Q(i, 2)['o']])
NUM(i, 3, F(-6, 3)); NUM(i, 4, iterate(2, lambda u, t: u * 3, 5)[-1])
FN(i, 5, terms([5, 10, 20, 40, 80]), 'n', P=seqP(5))
i = 23
TXT(i, 0, 0); TXT(i, 1, 3)
SET(i, 2, [x for x in range(-20, 21) if x * x == 2 * 8])
r_ = round((96 / 12) ** (1 / 3)); assert r_ ** 3 * 12 == 96; a1 = F(12, r_ ** 2)
FN(i, 3, lambda n: a1 * r_ ** (n - 1), 'n', P=seqP(6))
r4 = math.sqrt(96 / 24); NUM(i, 4, 24 / r4 ** 3)
NUM(i, 5, [n for n in range(1, 60) if 2 * 3 ** (n - 1) > 1000][0])
i = 24
gs = lambda a, r, n: sum(a * r ** k for k in range(n))
FN(i, 0, gs, 'a r n', P=Parn)
TXT(i, 1, 3)
FN(i, 2, gs, 'a r n', P=[dict(a=1.5, r=0.7, n=5), dict(a=-2.0, r=0.3, n=6), dict(a=4.0, r=-0.6, n=3)])
NUM(i, 3, gs(4, 3, 5)); NUM(i, 4, sum(2 ** k for k in range(10))); NUM(i, 5, gs(8, F(1, 2), 4))
i = 25
FN(i, 0, lambda a, r: a * r ** 2 + a * r ** 3 + a * r ** 4, 'a r')
TXT(i, 1, 2)
sol = [(a, r) for r in range(-10, 11) if r not in (0, 1) for a in [F(7, 1 + r + r * r)] if gs(a, r, 6) == 63]
assert len(sol) == 1
NUM(i, 2, sol[0][1]); NUM(i, 3, sol[0][0])
NUM(i, 4, sum(2 ** (k - 1) for k in range(4, 7)))
NUM(i, 5, [n for n in range(1, 40) if gs(3, 2, n) == 381][0])
i = 26
TXT(i, 0, 3)
assert sum(2 * k for k in range(1, 21)) == sum(range(2, 41, 2)) and list(range(2, 41, 2))[-1] == 40
TXT(i, 1, 2)
NUM(i, 2, len(range(3, 11))); NUM(i, 3, sum(2 * k + 1 for k in range(1, 5))); NUM(i, 4, sum(3 for k in range(1, 6))); NUM(i, 5, sum(2 ** k for k in range(1, 6)))
i = 27
FN(i, 0, lambda n: sum(k * k for k in range(1, n + 1)), 'n', P=seqP(7))
FN(i, 1, lambda n: sum(k ** 3 for k in range(1, n + 1)), 'n', P=seqP(7))
TXT(i, 2, 1)
NUM(i, 3, sum(k * k for k in range(1, 11))); NUM(i, 4, sum(2 * k + 3 for k in range(1, 11)))
FN(i, 5, lambda n: sum(6 * k for k in range(1, n + 1)), 'n', P=seqP(7))
i = 28
FN(i, 0, gs, 'a r n', P=Parn)
t_ = [2 ** (2 * n - 1) for n in range(1, 6)]; assert t_[0] == 2 and all(t_[k + 1] == 4 * t_[k] for k in range(4))
TXT(i, 1, 1); TXT(i, 2, 0)
NUM(i, 3, sum(3 ** (k - 1) for k in range(1, 6)))
FN(i, 4, lambda n: sum(2 ** k for k in range(1, n + 1)), 'n', P=seqP(7))
NUM(i, 5, sum(F(1, 2) ** (k - 1) for k in range(1, 7)))
i = 29
TXT(i, 0, 1)
FN(i, 1, lambda k: 1 / (k * (k + 1)), 'k')
TXT(i, 2, 0)
FN(i, 3, lambda n: sum(F(1, k * (k + 1)) for k in range(1, n + 1)), 'n', P=seqP(7))
NUM(i, 4, sum(F(1, k * (k + 2)) for k in range(1, 20, 2)))
NUM(i, 5, sum(1 / (math.sqrt(k + 1) + math.sqrt(k)) for k in range(1, 9)))
i = 30
TXT(i, 0, 1); TXT(i, 1, 0)
for n in (3, 5):
    M = sum(k * 2 ** (k - 1) for k in range(1, n + 1)); assert M - 2 * M == sum(2 ** k for k in range(n)) - n * 2 ** n
TXT(i, 2, 3)
NUM(i, 3, sum(k * 2 ** (k - 1) for k in range(1, 6)))
FN(i, 4, lambda n: sum(k * 2 ** (k - 1) for k in range(1, n + 1)), 'n', P=seqP(7))
NUM(i, 5, sum(k * 3 ** (k - 1) for k in range(1, 5)))
i = 31
TXT(i, 0, 0)
FN(i, 1, lambda k: sum(range(1, k + 1)), 'k', P=[{'k': t} for t in range(1, 7)])
FN(i, 2, lambda k: sum(2 * t for t in range(1, k + 1)), 'k', P=[{'k': t} for t in range(1, 7)])
NUM(i, 3, sum(2 * t - 1 for t in range(1, 6)))
NUM(i, 4, sum(sum(range(1, k + 1)) for k in range(1, 5)))
FN(i, 5, lambda n: sum(sum(range(1, k + 1)) for k in range(1, n + 1)), 'n', P=seqP(7))
i = 32
TXT(i, 0, 0); TXT(i, 1, 3); TXT(i, 2, 2)
S_ = lambda n: n * n + 2 * n
FN(i, 3, lambda n: S_(n) - S_(n - 1) if n > 1 else S_(1), 'n', P=seqP(7))
NUM(i, 4, (2 ** 5 - 1) - (2 ** 4 - 1)); NUM(i, 5, 1 ** 2 + 1)
i = 33
TXT(i, 0, 3); TXT(i, 1, 2)
FN(i, 2, lambda n: sum(range(1, n)), 'n', P=seqP(7))
s_ = [1, 2, 4, 7, 11]; df = [s_[k + 1] - s_[k] for k in range(4)]; assert df == [1, 2, 3, 4]
NUM(i, 3, s_[-1] + df[-1] + 1)
FN(i, 4, terms([2, 5, 10, 17, 26]), 'n', P=seqP(5))
FN(i, 5, terms([1, 3, 7, 15, 31]), 'n', P=seqP(5))
i = 34
TXT(i, 0, 3)
def groups(src, k):
    it = iter(src); return [[next(it) for _ in range(g)] for g in range(1, k + 1)]
G = groups(itertools.count(1), 12)
NUM(i, 1, G[9][0]); NUM(i, 2, sum(G[4])); NUM(i, 3, [g + 1 for g in range(12) if 50 in G[g]][0])
FN(i, 4, lambda n: G[n - 1][-1], 'n', P=seqP(8))
NUM(i, 5, groups(itertools.count(1, 2), 5)[3][0])
i = 35
TXT(i, 0, 2); TXT(i, 1, 1)
FN(i, 2, terms(iterate(3, lambda u, t: 2 * u, 7)), 'n', P=seqP(7))
NUM(i, 3, iterate(1, lambda u, t: 2 * u + 1, 4)[-1]); NUM(i, 4, iterate(2, lambda u, t: u * u - 1, 3)[-1])
FN(i, 5, terms(iterate(5, lambda u, t: u - 4, 7)), 'n', P=seqP(7))
i = 36
TXT(i, 0, 2); TXT(i, 1, 1)
NUM(i, 2, iterate(1, lambda u, t: u + t, 5)[-1])
FN(i, 3, terms(iterate(1, lambda u, t: u + 2 * t, 7)), 'n', P=seqP(7))
FN(i, 4, terms(iterate(2, lambda u, t: u + 3 ** t, 7)), 'n', P=seqP(7))
TXT(i, 5, 2)
i = 37
TXT(i, 0, 1); TXT(i, 1, 0)
NUM(i, 2, F(2, 1 - 3))
FN(i, 3, terms(iterate(1, lambda u, t: 3 * u + 2, 7)), 'n', P=seqP(7))
FN(i, 4, terms(iterate(F(5), lambda u, t: u / 2 + 1, 7)), 'n', P=seqP(7))
NUM(i, 5, iterate(4, lambda u, t: 2 * u - 3, 3)[-1])
i = 38
TXT(i, 0, 1); TXT(i, 1, 0); TXT(i, 2, 3); TXT(i, 3, 2)
FN(i, 4, lambda k: F(sum(r * r for r in range(1, k + 2))), 'k', P=[{'k': t} for t in range(1, 7)])
NUM(i, 5, 1 * 2); assert 1 * 2 * 3 / 3 == 2
i = 39
TXT(i, 0, 0); TXT(i, 1, 3)
ok = lambda n: 2 ** n > n * n
NUM(i, 2, [n0 for n0 in range(1, 30) if all(ok(n) for n in range(n0, 200))][0])
TXT(i, 3, 2)
FN(i, 4, lambda k: 4 * k - 2 * (k + 1), 'k')
assert math.factorial(4) == 24 and 2 ** 4 == 16
TXT(i, 5, 0)
i = 40
TXT(i, 0, 0); NUM(i, 1, 4 ** 1 - 1)
# with 4^k = 3m+1 :  4^(k+1)-1 = 4(3m+1)-1
FN(i, 2, lambda m: 4 * (3 * m + 1) - 1, 'm'); FN(i, 3, lambda m: 5 * (4 * m + 1) - 1, 'm')
TRUE1(i, 4, [all((n ** 3 + 2 * n) % int(o) == 0 for n in range(1, 200)) for o in Q(i, 4)['o']])
TRUE1(i, 5, [all((7 ** n - 1) % int(o) == 0 for n in range(1, 60)) for o in Q(i, 5)['o']])
i = 41
TXT(i, 0, 3); TXT(i, 1, 2)
FN(i, 2, terms(iterate(1, lambda u, t: u + 2 * t + 1, 7)), 'n', P=seqP(7))
FN(i, 3, lambda k: k * k + 2 * k + 1, 'k')
FN(i, 4, terms(iterate(2, lambda u, t: 2 * u - 1, 7)), 'n', P=seqP(7))
FN(i, 5, terms(iterate(F(1), lambda u, t: u / (u + 1), 7)), 'n', P=seqP(7))
#CH2END

# =================== Chapter 3 ===================
def dk(co):  # roots of polynomial, coefficients high->low (Durand-Kerner)
    co = [complex(c) / co[0] for c in co]; n = len(co) - 1
    z = [(0.4 + 0.9j) ** k for k in range(n)]
    for _ in range(600):
        nz = []
        for k in range(n):
            den = 1
            for m in range(n):
                if m != k: den *= (z[k] - z[m])
            nz.append(z[k] - pv(co, z[k]) / den)
        z = nz
    return z
def cl6(a, b): return abs(a - b) < 1e-4
def same_roots(A, B): return len(A) == len(B) and all(any(cl6(a, b) for b in B) for a in A) and all(any(cl6(a, b) for a in A) for b in B)
def ROOTS(i, j, co):
    q = Q(i, j); SEEN.add((i, j)); exp = dk(co); sets = [parse_set(o) for o in q['o']]
    hits = [k for k in range(4) if same_roots(sets[k], exp)]
    if hits != [q['a']]: err(i, j, f'roots {exp} match {hits} vs marked {q["a"]}')
i = 42
TXT(i, 0, 3); TXT(i, 1, 2)
TRUE1(i, 2, [abs(complex(ev(o)).real) < 1e-12 and abs(complex(ev(o)).imag) > 0 for o in Q(i, 2)['o']])
NUM(i, 3, (3 - 5j).imag); NUM(i, 4, (4j).real)
NUM(i, 5, F(6 + 2, 2))
i = 43
TXT(i, 0, 2); NUM(i, 1, 1j ** 3); NUM(i, 2, (3 + 2j) + (1 - 5j)); NUM(i, 3, (2 + 3j) * (1 - 1j)); NUM(i, 4, 1j ** 10); NUM(i, 5, (1 + 1j) ** 2)
i = 44
FN(i, 0, lambda a, b: complex(a, b).conjugate(), 'a b'); TXT(i, 1, 1); TXT(i, 2, 0)
NUM(i, 3, (3 + 4j) * (3 - 4j)); NUM(i, 4, 5 / (2 - 1j)); NUM(i, 5, (1 + 1j) / (1 - 1j))
i = 45
FN(i, 0, lambda a: cmath.sqrt(-a), 'a')
tr = []
for o in Q(i, 1)['o']:
    l, r = o.split(' = '); tr.append(close(ev(l), ev(r)))
TRUE1(i, 1, tr); TXT(i, 2, 0)
NUM(i, 3, cmath.sqrt(-4) * cmath.sqrt(-9)); NUM(i, 4, cmath.sqrt(-16) + cmath.sqrt(-25)); NUM(i, 5, cmath.sqrt(-12) / cmath.sqrt(-3))
i = 46
TXT(i, 0, 1); TXT(i, 1, 0)
ROOTS(i, 2, [1, 0, 9])
EQ(i, 3, lambda x: x * x + 6 * x + 13, 'x')
ROOTS(i, 4, pmul([1, -2], [1, -2])[:2] + [8])      # (x-2)^2 + 4
ROOTS(i, 5, [1, -2, 5])
i = 47
Pq = [dict(a=1.5, b=-2.5, c=0.7), dict(a=-2.0, b=3.1, c=1.3), dict(a=0.6, b=1.9, c=-2.2)]
def disc_from_roots(a, b, c):
    r1, r2 = quad_roots(a, b, c); return a * a * (r1 - r2) ** 2
FN(i, 0, disc_from_roots, 'a b c', P=Pq)
TXT(i, 1, 3); TXT(i, 2, 3)
NUM(i, 3, disc_from_roots(2, -3, 5).real)
r1, r2 = quad_roots(1, -6, 9); assert cl6(r1, r2) and abs(r1.imag) < 1e-9
TXT(i, 4, 1)
SET(i, 5, [k for k in range(-40, 41) if cl6(*quad_roots(1, k, 9))])
i = 48
FN(i, 0, lambda a, b, c: sum(quad_roots(a, b, c)), 'a b c', P=Pq)
FN(i, 1, lambda a, b, c: quad_roots(a, b, c)[0] * quad_roots(a, b, c)[1], 'a b c', P=Pq)
r1, r2 = quad_roots(2, -6, 3); NUM(i, 2, r1 + r2); NUM(i, 3, r1 * r2)
r1, r2 = quad_roots(1, -4, 1); NUM(i, 4, r1 ** 2 + r2 ** 2); NUM(i, 5, 1 / r1 + 1 / r2)
i = 49
TXT(i, 0, 3); TXT(i, 1, 2); TXT(i, 2, 2)
ks = [k for k in range(-100, 101) for r in [quad_roots(1, -9, k)] if cl6(r[0], 2 * r[1]) or cl6(r[1], 2 * r[0])]
assert len(ks) == 1; NUM(i, 3, ks[0])
NUM(i, 4, F(-(2 * 2 + 6), 2))
ks = [k for k in range(1, 101) for r in [quad_roots(1, -k, 6)] if cl6(abs(r[0] - r[1]), 1)]
assert len(ks) == 1; NUM(i, 5, ks[0])
i = 50
FN(i, 0, lambda a, al, be, x: a * (x * x - (al + be) * x + al * be), 'a al be x')
TXT(i, 1, 2)
FN(i, 2, lambda x: x * x + 4); FN(i, 3, lambda x: x * x + 3); FN(i, 4, lambda x: x * x - 2 * x + 2); FN(i, 5, lambda x: 2 * x * x - 4 * x + 4)
i = 51
EQ(i, 0, lambda x, al, be: (x - al) * (x - be), 'x al be')
EQ(i, 1, lambda x: (x - 2) * (x + 5), 'x'); EQ(i, 2, lambda x: (x - (1 + 1j)) * (x - (1 - 1j)), 'x'); EQ(i, 3, lambda x: (x - 0.5) * (x - 3), 'x')
ROOTS(i, 4, [1, -4, 13])
r1, r2 = quad_roots(1, -3, 1); EQ(i, 5, lambda x: (x - (r1 + 1)) * (x - (r2 + 1)), 'x')
i = 52
TXT(i, 0, 2); TXT(i, 1, 1); TXT(i, 2, 0)
def qc(o):
    g = lambda x: eqf(o, [{'x': x}])[0]; c = g(0); a = (g(1) + g(-1)) / 2 - c; b = (g(1) - g(-1)) / 2; return a, b, c
def twopos(a, b, c):
    r = quad_roots(a, b, c); return all(abs(t.imag) < 1e-9 and t.real > 0 for t in r) and not cl6(*r)
def twoneg(a, b, c):
    r = quad_roots(a, b, c); return all(abs(t.imag) < 1e-9 and t.real < 0 for t in r) and not cl6(*r)
def opp(a, b, c):
    r = quad_roots(a, b, c); return all(abs(t.imag) < 1e-9 for t in r) and r[0].real * r[1].real < 0
TRUE1(i, 3, [twopos(*qc(o)) for o in Q(i, 3)['o']])
grid = [k / 8 for k in range(-80, 81)]
conds4 = [lambda m: m > 0, lambda m: m < 25 / 4, lambda m: 0 < m < 25 / 4, lambda m: m < 0]
TRUE1(i, 4, [all(opp(1, -5, m) == cnd(m) for m in grid if m != 0) for cnd in conds4])
conds5 = [lambda m: m < 4, lambda m: m > 0, lambda m: 0 < m < 4, lambda m: -4 < m < 0]
TRUE1(i, 5, [all(twoneg(1, 4, m) == cnd(m) for m in grid if m not in (0, 4)) for cnd in conds5])
i = 53
TXT(i, 0, 1); TXT(i, 1, 0)
NUM(i, 2, pdiv([1, -2, 0, 4], [1, -3])[1][0]); NUM(i, 3, pdiv([2, 0, 1, -5], [1, 1])[1][0]); NUM(i, 4, pdiv([4, -2, 1], [2, -1])[1][0])
av = [a for a in range(-20, 21) if pdiv([1, a, 2, 1], [1, 2])[1][0] == -3]; assert len(av) == 1; NUM(i, 5, av[0])
i = 54
TXT(i, 0, 1); TXT(i, 1, 0)
def line2(p, q): return lambda x: p[1] + (q[1] - p[1]) / (q[0] - p[0]) * (x - p[0])
FN(i, 2, line2((1, 3), (-2, -3)))
FN(i, 3, lambda x: pv(pdiv([1, 0, 0, 0, 0], [1, 0, -1])[1], x))
FN(i, 4, lambda x: pv(pdiv([1, 0, 0, 0], [1, -1, 0])[1], x))
FN(i, 5, lambda x: pv(pdiv([1, 0, 0, 2], pmul([1, -1], [1, -2]))[1], x))
i = 55
TXT(i, 0, 0); TXT(i, 1, 3)
NUM(i, 2, 2 * 1 + 3); NUM(i, 3, 2 * (-1) + 3)
assert pv([1, 1, -2], -2) == 0; NUM(i, 4, -2 + 4)
FN(i, 5, line2((2, 3 * 2 - 1), (3, 11)))
i = 56
TXT(i, 0, 0); NUM(i, 1, -2); TXT(i, 2, 2)
qq, rr = pdiv([1, -2, 0, 3], [1, -1]); FN(i, 3, lambda x: pv(qq, x)); NUM(i, 4, rr[0])
NUM(i, 5, pdiv([2, 0, -5, 1], [1, 2])[1][0])
i = 57
TXT(i, 0, 3); TXT(i, 1, 2)
TRUE1(i, 2, [pv([1, -3, 0, 4], -ev(o, {'x': 0})) == 0 for o in Q(i, 2)['o']])
kv = [k for k in range(-20, 21) if pv([1, k, 0, -4], 1) == 0]; assert len(kv) == 1; NUM(i, 3, kv[0])
FN(i, 4, lambda x: x ** 3 - 7 * x + 6)
av = [a for a in range(-20, 21) if pv([1, a, -1, -2], -1) == 0]; assert len(av) == 1; NUM(i, 5, av[0])
i = 58
TXT(i, 0, 3)
FN(i, 1, lambda x, a: x ** 3 + a ** 3, 'x a'); TXT(i, 2, 1)
ROOTS(i, 3, [1, 0, -5, 0, 4]); ROOTS(i, 4, [1, 0, 0, 0, -16]); ROOTS(i, 5, [1, 0, 0, -8])
i = 59
NUM(i, 0, (2 + 1j).conjugate()); TXT(i, 1, 1)
EQ(i, 2, lambda x: (x - 1) * (x - 2) * (x - 3), 'x'); EQ(i, 3, lambda x: (x - 1) * (x - 1j) * (x + 1j), 'x')
# x^3+ax^2+bx+5 with roots 2+i, 2-i, r : -(2+i)(2-i) r = 5
rr_ = -5 / ((2 + 1j) * (2 - 1j)); NUM(i, 4, rr_)
assert pmul([1, -4, 5], [1, 1])[3] == 5 and close(pv([1, -4, 5], 2 + 1j), 0)
NUM(i, 5, pmul([1, -4, 5], [1, 1])[1])
i = 60
W_ = BASE['W']; assert close(W_ ** 3, 1)
TXT(i, 0, 2)
tr = []
for o in Q(i, 1)['o']:
    l, r = o.split(' = '); tr.append(close(ev(l), ev(r)))
TRUE1(i, 1, tr); TXT(i, 2, 0)
NUM(i, 3, W_ ** 10); NUM(i, 4, (1 + W_) ** 3); NUM(i, 5, (1 - W_ + W_ ** 2) * (1 + W_ - W_ ** 2))
i = 61
TXT(i, 0, 1); TXT(i, 1, 0)
def rep(co):
    z = dk(co); return [z[u] for u in range(len(z)) for v in range(u) if abs(z[u] - z[v]) < 1e-3]
NUM(i, 2, rep([1, -3, 0, 4])[0])
SET(i, 3, [k for k in range(-30, 31) if rep(pmul([1, -1], [1, 2, k]))])
NUM(i, 4, rep(pmul([1, -3], [1, -2, 1]))[0]); NUM(i, 5, rep(pmul([1, -3], [1, -2, -3]))[0])
#CH3END

# =================== Chapter 4 ===================
def dist(p, q): return math.hypot(p[0] - q[0], p[1] - q[1])
def refl_line(p, a, b, c):  # reflect p across ax+by+c=0
    t = (a * p[0] + b * p[1] + c) / (a * a + b * b); return (p[0] - 2 * a * t, p[1] - 2 * b * t)
def dline(p, a, b, c): return abs(a * p[0] + b * p[1] + c) / math.hypot(a, b)
def area(A, B, Cc): return abs((B[0] - A[0]) * (Cc[1] - A[1]) - (B[1] - A[1]) * (Cc[0] - A[0])) / 2
def inter(l1, l2):
    (a, b, c), (d, e, f) = l1, l2; det = a * e - b * d
    return ((b * f - c * e) / det, (c * d - a * f) / det)
def divide(A, B, m, n):  # internal m:n ; external use n negative
    return tuple((n * a + m * b) / (m + n) for a, b in zip(A, B))
i = 62
FN(i, 0, lambda x1, x2: max(x1, x2) - min(x1, x2), 'x1 x2', P=[dict(x1=1.5, x2=4.0), dict(x1=3.0, x2=-2.5), dict(x1=-1.0, x2=-4.5)])
def indiv(m, n, x1, x2):
    p = x1 + (x2 - x1) * m / (m + n); assert close((p - x1) * n, (x2 - p) * m); return p
FN(i, 1, indiv, 'm n x1 x2', P=[dict(m=2.0, n=3.0, x1=1.5, x2=4.0), dict(m=1.0, n=4.0, x1=3.0, x2=-2.5), dict(m=5.0, n=2.0, x1=-1.0, x2=-4.5)])
TXT(i, 2, 3); NUM(i, 3, abs(8 - (-4))); NUM(i, 4, indiv(1, 3, -4, 8))
pe = [p for p in [k / 4 for k in range(-400, 401)] if p not in (-4, 8) and not (-4 < p < 8) and abs(p + 4) == 3 * abs(p - 8)]
assert len(pe) == 1; NUM(i, 5, pe[0])
i = 63
TXT(i, 0, 0); TXT(i, 1, 3); TXT(i, 2, 3)
PT(i, 3, refl_line((3, -2), 0, 1, 0)); PT(i, 4, refl_line((3, -2), 1, 0, 0)); PT(i, 5, (-3, 2))
i = 64
P4 = [dict(x1=1.5, y1=-2.0, x2=4.0, y2=3.5), dict(x1=3.0, y1=2.0, x2=-2.5, y2=-1.0), dict(x1=-1.0, y1=5.0, x2=-4.5, y2=0.5)]
FN(i, 0, lambda x1, y1, x2, y2: dist((x1, y1), (x2, y2)), 'x1 y1 x2 y2', P=P4)
TXT(i, 1, 3)
NUM(i, 2, dist((1, 2), (4, 6))); NUM(i, 3, dist((-2, 3), (4, -5))); NUM(i, 4, dist((5, -12), (0, 0)))
SET(i, 5, [k for k in range(-50, 51) if close(dist((1, k), (4, 5)), 5)])
i = 65
TXT(i, 0, 3); TXT(i, 1, 2); TXT(i, 2, 2)
def equi(param, A, B):  # param t -> point ; solve dist^2 equal (linear in t) by secant on two samples
    g = lambda t: dist(param(t), A) ** 2 - dist(param(t), B) ** 2
    t = -g(0) / (g(1) - g(0)); assert abs(g(t)) < 1e-9; return param(t)
PT(i, 3, equi(lambda t: (t, 0), (-1, 2), (3, 4))); PT(i, 4, equi(lambda t: (0, t), (2, 0), (0, 4))); PT(i, 5, equi(lambda t: (t, t), (1, 0), (0, 3)))
i = 66
P6 = [dict(m=2.0, n=3.0, **p) for p in P4]
FN(i, 0, lambda m, n, x1, y1, x2, y2: divide((x1, y1), (x2, y2), m, n), 'm n x1 y1 x2 y2', P=P6)
FN(i, 1, lambda x1, y1, x2, y2: divide((x1, y1), (x2, y2), 1, 1), 'x1 y1 x2 y2', P=P4)
PT(i, 2, divide((-2, 5), (6, -1), 1, 1)); PT(i, 3, divide((1, 2), (7, 8), 1, 2)); PT(i, 4, divide((1, 2), (4, 5), 2, -1)); TXT(i, 5, 3)
i = 67
TXT(i, 0, 2); TXT(i, 1, 1)
sym = lambda A, Pp: (2 * Pp[0] - A[0], 2 * Pp[1] - A[1])
PT(i, 2, sym((3, 4), (1, 6))); PT(i, 3, sym((5, 1), (2, -1))); PT(i, 4, divide((1, 2), (5, 8), 1, 1)); PT(i, 5, sym((2, -3), (0, 0)))
i = 68
TXT(i, 0, 2); TXT(i, 1, 1); TXT(i, 2, 0)
def kind(A, B, Cc):
    s = sorted([dist(A, B) ** 2, dist(B, Cc) ** 2, dist(A, Cc) ** 2])
    return (close(s[0] + s[1], s[2]), close(s[0], s[1]) or close(s[1], s[2]), close(s[0], s[2]))  # right, isosceles, equilateral
assert kind((0, 0), (4, 0), (0, 3)) == (True, False, False); TXT(i, 3, 3)
assert kind((1, 1), (4, 1), (1, 4)) == (True, True, False); TXT(i, 4, 3)
assert kind((0, 0), (2, 0), (1, math.sqrt(3))) == (False, True, True); TXT(i, 5, 2)
i = 69
TXT(i, 0, 1)
EQ(i, 1, lambda x, y, x1, y1, m: y - y1 - m * (x - x1), 'x y x1 y1 m')
NUM(i, 2, F(8 - 2, 3 - 1))
def thru(A, B): return lambda x, y: (B[1] - A[1]) * (x - A[0]) - (B[0] - A[0]) * (y - A[1])
def ptslope(A, m): return lambda x, y: y - A[1] - m * (x - A[0])
EQ(i, 3, ptslope((2, -1), 3)); EQ(i, 4, thru((1, 2), (3, 6))); EQ(i, 5, lambda x, y: x - 5)
i = 70
TXT(i, 0, 1); TXT(i, 1, 0)
NUM(i, 2, F(2, 3)); assert 2 * 3 - 3 * (2 + F(2, 3) * 3) + 6 == 0   # (0,2),(3,4) on the line
NUM(i, 3, F(6, 3))
tv = [t for t in range(-50, 51) if area((1, 1), (3, 5), (t, 9)) == 0]; assert len(tv) == 1; NUM(i, 4, tv[0])
EQ(i, 5, thru((0, 0), inter((1, 1, -3), (1, -1, -1))))
i = 71
TXT(i, 0, 0); TXT(i, 1, 3)
NUM(i, 2, F(-1, 2)); EQ(i, 3, ptslope((1, 2), 3)); EQ(i, 4, ptslope((2, 3), 2))
assert close(-1 / (-1 / 2), 2)
NUM(i, 5, [k for k in range(-20, 21) if k * (-1) - 2 * 3 == 0][0])    # k x + 2y  ||  3x - y : k*(-1) - 2*3 = 0
i = 72
TXT(i, 0, 0); TXT(i, 1, 3)
EQ(i, 2, lambda x, y: dist((x, y), (1, 1)) ** 2 - dist((x, y), (5, 3)) ** 2)
PT(i, 3, refl_line((3, 1), 1, -1, 0)); PT(i, 4, refl_line((2, 5), 0, 1, -2)); PT(i, 5, refl_line((4, 0), 1, 1, 0))
i = 73
P5 = [dict(a=1.5, b=-2.0, c=4.0, x1=3.5, y1=1.0), dict(a=3.0, b=2.0, c=-2.5, x1=-1.0, y1=-3.0), dict(a=-1.0, b=5.0, c=-4.5, x1=0.5, y1=2.0)]
FN(i, 0, lambda a, b, c, x1, y1: dline((x1, y1), a, b, c), 'a b c x1 y1', P=P5)
TXT(i, 1, 2)
NUM(i, 2, dline((1, 2), 3, 4, -1)); NUM(i, 3, dline((0, 0), 5, -12, 39)); NUM(i, 4, dline((F(2, 3), 0), 3, 4, -12))
NUM(i, 5, [k for k in range(1, 100) if close(dline((0, 0), 3, 4, k), 2)][0])
i = 74
TXT(i, 0, 3); TXT(i, 1, 2)
NUM(i, 2, area((0, 0), (4, 0), (0, 3))); NUM(i, 3, area((1, 0), (5, 0), (2, 6))); NUM(i, 4, area((1, 1), (3, 7), (-3, -1)))
NUM(i, 5, 0.5 * 2 * math.sqrt(5) * math.sqrt(5))
i = 75
TXT(i, 0, 2); TXT(i, 1, 1)
def fixed(L):  # L(k) -> (a,b,c)
    p = inter(L(0), L(1)); a, b, c = L(2.5); assert abs(a * p[0] + b * p[1] + c) < 1e-9; return p
PT(i, 2, fixed(lambda k: (k, -1, 2 - 3 * k)))
PT(i, 3, fixed(lambda k: (k + 1, k - 1, -3 * k - 1)))
PT(i, 4, fixed(lambda k: (k + 1, k - 1, -2 * k)))
PT(i, 5, fixed(lambda k: (2 * k + 1, -(k - 2), k + 3)))
i = 76
TXT(i, 0, 2); TXT(i, 1, 1); TXT(i, 2, 0)
L1, L2 = (1, -1, 1), (2, 1, -4); L3 = lambda k: (k, 1, -3)
par = lambda u, v: abs(u[0] * v[1] - u[1] * v[0]) < 1e-12
p0 = inter(L1, L2)
conc = [k for k in range(-20, 21) if abs(k * p0[0] + p0[1] - 3) < 1e-9]; assert len(conc) == 1; NUM(i, 3, conc[0])
p1 = [k for k in range(-20, 21) if par(L3(k), L1)]; assert len(p1) == 1; NUM(i, 4, p1[0])
SET(i, 5, [k for k in range(-20, 21) if par(L3(k), L1) or par(L3(k), L2) or abs(k * p0[0] + p0[1] - 3) < 1e-9])
i = 77
circ = lambda cx, cy, r2: (lambda x, y: (x - cx) ** 2 + (y - cy) ** 2 - r2)
EQ(i, 0, lambda x, y, a, b, R: (x - a) ** 2 + (y - b) ** 2 - R * R, 'x y a b R')
def gen2std(l, m, n):  # x^2+y^2+lx+my+n=0
    return (-l / 2, -m / 2), math.sqrt(l * l / 4 + m * m / 4 - n)
PT(i, 1, (-3, 1)); EQ(i, 2, circ(-3, 1, 4)); EQ(i, 3, circ(0, 0, 25))
c_, r_ = gen2std(-4, 6, 4); SET(i, 4, [c_, r_]); NUM(i, 5, gen2std(-6, 8, 0)[1])
i = 78
TXT(i, 0, 1); TXT(i, 1, 0); TXT(i, 2, 3)
EQ(i, 3, circ(2, 3, dist((2, 3), (5, 7)) ** 2))
mid = divide((1, 2), (5, -4), 1, 1); EQ(i, 4, circ(mid[0], mid[1], dist(mid, (1, 2)) ** 2))
cc = inter((2 * 4, 0, -16), (0, 2 * 6, -36))   # perpendicular bisectors of (0,0)-(4,0), (0,0)-(0,6)
assert close(dist(cc, (4, 0)), dist(cc, (0, 6))) and close(dist(cc, (0, 0)), dist(cc, (0, 6)))
EQ(i, 5, circ(cc[0], cc[1], dist(cc, (0, 0)) ** 2))
i = 79
FN(i, 0, lambda a, b: dline((a, b), 0, 1, 0), 'a b', P=[dict(a=2.0, b=-3.0), dict(a=-1.5, b=4.0), dict(a=5.0, b=0.5)])
TXT(i, 1, 3)
EQ(i, 2, circ(4, -2, dline((4, -2), 0, 1, 0) ** 2)); EQ(i, 3, circ(-3, 5, dline((-3, 5), 1, 0, 0) ** 2)); EQ(i, 4, circ(-2, 2, 4))
c5 = inter((1, 0, -2), (1, -1, 0)); EQ(i, 5, circ(c5[0], c5[1], dist(c5, (0, 0)) ** 2))
i = 80
TXT(i, 0, 0); TXT(i, 1, 3)
r2 = lambda l, m, n: l * l / 4 + m * m / 4 - n
assert r2(2, 0, 5) < 0 and r2(-2, 4, 1) > 0; TXT(i, 2, 2)
gk = [k / 4 for k in range(-80, 81)]
TRUE1(i, 3, [all((r2(4, -2, k) > 0) == c(k) for k in gk) for c in [lambda k: k > 5, lambda k: k < 5, lambda k: k < -5, lambda k: k > -5]])
TRUE1(i, 4, [all((r2(-2 * k, 0, 4) > 0) == c(k) for k in gk) for c in [lambda k: -2 < k < 2, lambda k: k < -2 or k > 2, lambda k: k > 4 or k < -4, lambda k: k < 4]])
assert r2(-6, 2, 10) == 0; TXT(i, 5, 0)
i = 81
TXT(i, 0, 3); TXT(i, 1, 2); TXT(i, 2, 2)
def cl_int(r2_, m, c):  # x^2+y^2=r2 with y=mx+c
    A, B, Cq = 1 + m * m, 2 * m * c, c * c - r2_; dsc = B * B - 4 * A * Cq
    if dsc < -1e-9: return []
    xs = {round((-B + s * math.sqrt(max(dsc, 0))) / (2 * A), 9) for s in (1, -1)}
    return [(x, m * x + c) for x in xs]
SET(i, 3, cl_int(10, 1, 2)); NUM(i, 4, len(cl_int(5, 2, 5))); NUM(i, 5, len(cl_int(4, 1, 5)))
i = 82
TXT(i, 0, 3); TXT(i, 1, 2)
SET(i, 2, [k for k in range(-30, 31) if len(cl_int(8, 1, k)) == 1])
d3 = dline((1, 2), 3, 4, -1); assert 0 < d3 < 3; TXT(i, 3, 0)
assert dline((2, 0), 1, 0, -5) == 3; TXT(i, 4, 0)
TRUE1(i, 5, [all((len(cl_int(9, 0, k)) == 2) == c(k) for k in [t / 4 for t in range(-60, 61)]) for c in [lambda k: k > 3, lambda k: abs(k) == 3, lambda k: -9 < k < 9, lambda k: -3 < k < 3]])
i = 83
TXT(i, 0, 2)
FN(i, 1, lambda R, d: 2 * math.sqrt(R * R - d * d), 'R d', P=[dict(R=5.0, d=3.0), dict(R=2.5, d=1.0), dict(R=7.0, d=6.5)])
chord = lambda c, r2_, a, b, cc_: 2 * math.sqrt(r2_ - dline(c, a, b, cc_) ** 2)
NUM(i, 2, chord((0, 0), 25, 0, 1, -3)); NUM(i, 3, chord((0, 0), 4, 1, 1, -2)); NUM(i, 4, chord((1, -1), 13, 1, 0, -3))
SET(i, 5, [k for k in range(-3, 4) if close(chord((0, 0), 10, 0, 1, -k), 6)])
i = 84
EQ(i, 0, lambda x, y, a, b, R: a * x + b * y - R * R, 'x y a b R'); TXT(i, 1, 1)
def tang(p, r2_):
    assert close(p[0] ** 2 + p[1] ** 2, r2_); return lambda x, y: p[0] * (x - p[0]) + p[1] * (y - p[1])  # radius ⟂ tangent
EQ(i, 2, tang((3, 4), 25)); EQ(i, 3, tang((1, -3), 10))
tp = [(a, b) for a in range(-3, 4) for b in range(-3, 4) if a * a + b * b == 5 and a * (3 - a) + b * (1 - b) == 0]
SET(i, 4, tp); TXT(i, 5, 2)
i = 85
def rel(c1, r1, c2, r2_):
    d = dist(c1, c2)
    if close(d, r1 + r2_): return 'ext-tangent'
    if close(d, abs(r1 - r2_)): return 'int-tangent'
    if d > r1 + r2_: return 'outside'
    if d < abs(r1 - r2_): return 'inside'
    return 'two'
TXT(i, 0, 1); TXT(i, 1, 0); TXT(i, 2, 0)
assert rel((0, 0), 2, (3, 0), 1) == 'ext-tangent'; TXT(i, 3, 3)
assert rel((0, 0), 5, (1, 0), 3) == 'inside'; TXT(i, 4, 2)
assert rel((0, 0), 3, (4, 3), 2) == 'ext-tangent'; TXT(i, 5, 1)
i = 86
TXT(i, 0, 1); TXT(i, 1, 0)
def cc_int(g1, g2):  # circles as (l,m,n); returns radical line and intersection points (integer grid search + check)
    a, b, c = g1[0] - g2[0], g1[1] - g2[1], g1[2] - g2[2]
    ptsx = []
    for t in [k / 1000 for k in range(-8000, 8001)]:
        for (x, y) in ([(t, -(a * t + c) / b)] if b else [(-c / a, t)]):
            if abs(x * x + y * y + g1[0] * x + g1[1] * y + g1[2]) < 1e-9: ptsx.append((x, y))
    return (a, b, c), ptsx
ln, ip = cc_int((0, 0, -4), (-4, -4, 4))
EQ(i, 2, lambda x, y: ln[0] * x + ln[1] * y + ln[2]); SET(i, 3, ip)
ln2, ip2 = cc_int((0, 0, -13), (-2, 0, -9))
EQ(i, 4, lambda x, y: ln2[0] * x + ln2[1] * y + ln2[2]); SET(i, 5, ip2)
i = 87
TXT(i, 0, 0); TXT(i, 1, 3); TXT(i, 2, 3)
g1 = lambda x, y: x * x + y * y - 4; g2 = lambda x, y: x * x + y * y - 2 * x
k3 = F(-g2(0, 1), g1(0, 1)); NUM(i, 3, k3)
EQ(i, 4, lambda x, y: float(k3) * g1(x, y) + g2(x, y))
h1 = lambda x, y: x * x + y * y - 9; h2 = lambda x, y: x * x + y * y - 4 * y
k5 = F(-h2(3, 3), h1(3, 3))
EQ(i, 5, lambda x, y: float(k5) * h1(x, y) + h2(x, y))
#CH4END

# =================== report ===================
miss = [(i, j) for i in range(len(LS)) for j in range(len(D[LS[i]])) if (i, j) not in SEEN]
print('lessons', len(LS), 'questions', sum(len(v) for v in D.values()), 'checked', len(SEEN), 'unchecked', len(miss))
if miss: print('UNCHECKED', miss[:40])
# structural checks
for i, l in enumerate(LS):
    for j, q in enumerate(D[l]):
        if len(q['o']) != 4 or len(set(o.strip() for o in q['o'])) != 4: ERR.append(f'L{i} q{j}: options structure')
        if len(q['e'].split()) > 25: ERR.append(f'L{i} q{j}: e has {len(q["e"].split())} words')
        ln = [len(o) for o in q['o']]
        if ln[q['a']] == max(ln) and ln.count(max(ln)) == 1: ERR.append(f'L{i} q{j}: correct option strictly longest')
print('ERRORS', len(ERR))
for e in ERR: print(' ', e)
