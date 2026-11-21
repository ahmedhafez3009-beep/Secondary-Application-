# Independent audit of the 37 "chg" questions in b2math1 (plain Python).
# Each check returns a list of 4 booleans (option is true/correct); exactly one must be True, at index "a".
import json, sys, math, cmath, random
from fractions import Fraction as F
random.seed(7)
SRC = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/khutwa/quiz/b2math1_exam.json'
by = json.load(open(SRC, encoding='utf-8'))['by']
R = lambda: random.uniform(-5, 5)
def ident(f, g, n=40, nv=1):
    """numeric identity test of f == g over random points"""
    for _ in range(n):
        xs = [R() for _ in range(nv)]
        try:
            a, b = f(*xs), g(*xs)
        except ZeroDivisionError:
            continue
        if abs(a - b) > 1e-7 * (1 + abs(a)):
            return False
    return True
C = {}
def chk(lesson, idx):
    def d(fn): C[(lesson, idx)] = fn; return fn
    return d

@chk('ضرب وقسمة المقادير النسبية', 3)
def _():
    orig = lambda x: (x*x - 9) / (x*x + 3*x)
    assert ident(orig, lambda x: (x - 3) / x)
    # cancelled factor f: num/f = x-3 and den/f = x
    cands = [lambda x: x - 3, lambda x: x, lambda x: x*x, lambda x: x + 3]
    return [ident(lambda x: (x*x - 9) / f(x), lambda x: x - 3) and ident(lambda x: (x*x + 3*x) / f(x), lambda x: x) for f in cands]

@chk('الكسور المركبة', 3)
def _():
    student = lambda x: (x + 1) / (1 - 1/x)
    num_only = lambda x: ((1 + 1/x) * x) / (1 - 1/x)          # numerator alone times x
    den_only = lambda x: (1 + 1/x) / ((1 - 1/x) * x)
    both_div = lambda x: ((1 + 1/x) / x) / ((1 - 1/x) / x)
    both_mul = lambda x: ((1 + 1/x) * x) / ((1 - 1/x) * x)
    assert ident(student, num_only) and not ident(student, den_only)
    assert not ident(student, both_div) and not ident(student, both_mul)
    assert ident(both_mul, lambda x: (x + 1) / (x - 1))
    o = by['الكسور المركبة'][3]['o']
    res = []
    for t in o:
        if 'البسط وحده' in t: res.append(True)
        elif 'المقام وحده' in t or 'قسم' in t or 'والمقام معًا' in t: res.append(False)
        else: res.append(None)   # unverifiable / arguable wording -> flagged
    return res

@chk('المتطابقات', 3)
def _():
    return [ident(lambda x: x*x - 4, lambda x: 0), ident(lambda x: (x+1)**2, lambda x: x*x + 2*x + 1),
            ident(lambda x: 2*x + 1, lambda x: 5), ident(lambda x: (x+2)**2, lambda x: x*x + 2*x + 4)]

@chk('إثبات المتطابقات (2)', 5)
def _():
    ok = True; neg = True; pos = True
    for _ in range(50):
        a, b = R(), R(); c = -a - b
        ok &= abs((a+b)*(b+c)*(c+a) + a*b*c) < 1e-9
        neg &= abs(a+b+c_) < 1e-9 if False else (abs((a+b) + c) < 1e-9 and abs((b+c) + a) < 1e-9 and abs((c+a) + b) < 1e-9)
        pos &= abs((a+b) - c) < 1e-9
    assert ok
    each_zero = False   # brackets equal -c,-a,-b, not zero in general
    all_zero = False    # a=1,b=1,c=-2 satisfies the condition
    return [each_zero, pos, all_zero, neg]

@chk('إثبات المتباينات (4) (متباينة المتوسط الحسابي والمتوسط الهندسي)', 3)
def _():
    f = lambda x: x + 9/x
    xm = min((i/1000 for i in range(1, 20001)), key=f)
    assert abs(xm - 3) < 1e-9 and f(3) == 6
    return [abs(xm - v) < 1e-9 for v in (9, 6, 3, 1)]

@chk('المتتابعة الحسابية (2)', 3)
def _():
    r = [True, True, True, True]
    def holds(rel):  # relation true for every AP, and implies 2b=a+c
        t = True
        for _ in range(50):
            a, dd = R(), R() or 1.0
            try: t &= rel(a, a+dd, a+2*dd)
            except ZeroDivisionError: pass
        return t
    e = 1e-9
    return [holds(lambda a,b,c: abs((b-a)-(c-b)) < e), holds(lambda a,b,c: abs(b/a-c/b) < e),
            holds(lambda a,b,c: abs((b-a)-(b-c)) < e), holds(lambda a,b,c: abs((a+b)-(b+c)) < e)]

@chk('المتتابعة الحسابية (2)', 4)
def _():
    dd = F(30 - 10, 8 - 3); a = 10 - 2*dd
    assert dd == 4 and a + 7*dd == 30
    return [F(20,5) == dd, F(30,8) == dd, F(10,3) == dd, F(40,11) == dd]

@chk('المتتابعة الهندسية (2)', 4)
def _():
    sols = [(a, r) for r in (2, -2) for a in (F(24, r**3),) if a*r**5 == 96]
    assert len(sols) == 2
    return [all(r == 4 for a, r in sols), all(r*r == 4 for a, r in sols),
            all(r*r == 72 for a, r in sols), all(r**3 == 4 for a, r in sols)]

@chk('مجموع المتتابعة الهندسية (2)', 3)
def _():
    fs = [lambda r: 7*r**2, lambda r: 7*r**3, lambda r: 7*r**6, lambda r: 7 + r**3]
    out = []
    for f in fs:
        t = True
        for _ in range(30):
            r = R(); a = 7 / (1 + r + r*r)
            t &= abs(a*r**3 + a*r**4 + a*r**5 - f(r)) < 1e-7
        out.append(t)
    return out

@chk('مجموع المتتابعات الكسرية', 3)
def _():
    for n in range(1, 40):
        assert sum(F(1, k) - F(1, k+1) for k in range(1, n+1)) == 1 - F(1, n+1)
    terms = [F(1, k) - F(1, k+1) for k in range(1, 6)]
    geometric = len({terms[i+1] / terms[i] for i in range(4)}) == 1
    return [False, geometric, False, True]   # 0: positivity doesn't explain telescoping; 2: denominators differ

@chk('متتابعات الفروق', 2)
def _():
    s = [2, 5, 10, 17, 26]; dif = [s[i+1] - s[i] for i in range(4)]
    return [dif == o for o in ([2,3,5,7], [7,15,27,43], [3,5,7,9], [3,5,7,8])]

def groups(n):
    g, k = [], 1
    for i in range(1, n+1):
        g.append(list(range(k, k+i))); k += i
    return g

@chk('المتتابعات المجمعة', 2)
def _():
    return [len(groups(20)[19]) == v for v in (19, 20, 210, 21)]

@chk('المتتابعات المجمعة', 5)
def _():
    g = groups(30)
    assert all(g[n-1][-1] == n*(n+1)//2 == sum(range(1, n+1)) for n in range(1, 31))
    starts_sq = all(g[n-1][0] == n*n for n in range(1, 31))
    const = len({len(x) for x in g}) == 1
    dbl = all(x[-1] == 2*x[0] for x in g)
    return [starts_sq, const, dbl, True]

@chk('علاقات التكرار (3)', 5)
def _():
    a = [3]
    for _ in range(20): a.append(2*a[-1] - 3)
    return [all(a[i+1] == 2*a[i] for i in range(20)), all(x == 3 for x in a),
            all(a[i+1] == a[i] - 3 for i in range(20)), all(a[i+1] == a[i] + 3 for i in range(20))]

@chk('إثبات كون العدد مضاعفًا باستخدام الاستقراء الرياضي', 3)
def _():
    assert all(4**(k+1) - 1 == 4*(4**k - 1) + 3 and (4**k - 1) % 3 == 0 for k in range(1, 30))
    return [False, True, False, False]   # the rewriting exposes 4^k - 1 (induction hypothesis)

@chk('العمليات على الأعداد المركبة (2)', 2)
def _():
    den_real = num_real = den_imag = conj = True
    for _ in range(40):
        z, w = complex(R(), R()), complex(R(), R())
        nn, dn = z * w.conjugate(), w * w.conjugate()
        den_real &= abs(dn.imag) < 1e-9; num_real &= abs(nn.imag) < 1e-9
        den_imag &= abs(dn.real) < 1e-9; conj &= abs(nn/dn - (z/w).conjugate()) < 1e-9
        assert abs(nn/dn - z/w) < 1e-9
    return [den_real, num_real, den_imag, conj]

@chk('تكوين المعادلة التربيعية بمعلومية جذورها', 3)
def _():
    for x in (F(1, 2), F(3)):
        assert 2*x*x - 7*x + 3 == 0 and x*x - F(7, 2)*x + F(3, 2) == 0
    return [True, False, False, False]   # same roots; x2 only clears fractions; leading coeff 1 is allowed

@chk('إشارتا الحلين', 2)
def _():
    pos = True
    for _ in range(2000):
        a, b, c = R(), R(), R()
        if a and c / a < 0:
            D = b*b - 4*a*c; pos &= D > 0
            r1 = (-b + math.sqrt(D)) / (2*a); r2 = (-b - math.sqrt(D)) / (2*a)
            assert r1 * r2 < 0
    # x^2 - x - 2: sum = 1 != 0 ; D = 9 != 0
    return [pos, False, False, False]

@chk('نظرية الباقي (1)', 3)
def _():
    def rem(co, a):  # synthetic division by x - a
        r = 0
        for c in co: r = r*a + c
        return r
    ev = lambda co, x: rem(co, x)
    t = [True]*4
    for _ in range(30):
        co = [random.randint(-5, 5) for _ in range(5)]
        # true remainder on division by x+1 via long division
        q = []; r = 0
        for c in co: r = r*(-1) + c; q.append(r)
        true_rem = q[-1]
        t[0] &= true_rem == ev(co, 0); t[1] &= true_rem == -ev(co, 1)
        t[2] &= true_rem == ev(co, 1); t[3] &= true_rem == ev(co, -1)
    return t

@chk('نظرية الباقي (2)', 4)
def _():
    # divide random polys by (x-1)(x+2) = x^2 + x - 2 ; remainder degree <= 1
    for _ in range(30):
        p = [random.randint(-5, 5) for _ in range(6)]; p[0] = p[0] or 1
        r = p[:]
        for i in range(len(r) - 2):
            c = r[i]; r[i] = 0; r[i+1] -= c*1; r[i+2] -= c*(-2)
        assert all(v == 0 for v in r[:-2])
    return [False, False, True, False]   # x^3 / divisor: remainder 3x-2 (not const), deg quotient 1 only by accident

@chk('المعادلات ذات الدرجة العليا', 4)
def _():
    assert ident(lambda x: x**3 - 8, lambda x: (x - 2)*(x*x + 2*x + 4))
    r = [(-2 + cmath.sqrt(4 - 16)) / 2, (-2 - cmath.sqrt(4 - 16)) / 2]
    assert all(abs(z**3 - 8) < 1e-9 and abs(z.imag) > 1 for z in r)
    triple = ident(lambda x: x**3 - 8, lambda x: (x - 2)**3)
    other = ident(lambda x: x**3 - 8, lambda x: (x - 2)*(x*x - 2*x + 4))
    o3 = abs((-2)**3 - 8) < 1e-9 and abs((2j)**3 - 8) < 1e-9
    return [True, triple, other, o3]

@chk('النقاط في المستوى الإحداثي', 0)
def _():
    conds = [lambda k: -3 < k < 2, lambda k: k > 2, lambda k: k < -3, lambda k: -2 < k < 3]
    ks = [i/10 for i in range(-80, 81)]
    return [all(c(k) == (k - 2 < 0 and k + 3 > 0) for k in ks) for c in conds]

@chk('النقاط في المستوى الإحداثي', 2)
def _():
    q4 = lambda x, y: x > 0 and y < 0
    pts = [(1, -1), (-1, 1), (-1, -1), (1, 1)]
    cs = [lambda x, y: x < 0 and y > 0, lambda x, y: x < 0 and y < 0, lambda x, y: x > 0 and y < 0, lambda x, y: x > 0 and y > 0]
    return [all(c(*p) == q4(*p) for p in pts) for c in cs]

@chk('النقاط في المستوى الإحداثي', 3)
def _():
    a, b = 2.5, -1.5
    return [p == (a, -b) for p in ((-a, b), (-a, -b), (b, a), (a, -b))]

@chk('النقاط في المستوى الإحداثي', 5)
def _():
    a = -4 - 1; b = 3 + 2
    assert (-(a + 1), 3) == (4, b - 2)
    return [a + b == v for v in (0, 2, -6, 8)]

@chk('النقاط المتساوية البعد عن نقطتين', 3)
def _():
    cond = lambda t: (t + 1)**2 + 2**2 - ((t - 3)**2 + 4**2)
    os_ = [lambda t: (t-1)**2 + 4 - ((t+3)**2 + 16), lambda t: (t+1)**2 + 4 - ((t-3)**2 + 16),
           lambda t: (t+1)**2 + 2 - ((t-3)**2 + 4), lambda t: (t+1) + 2 - ((t-3) + 4)]
    assert cond(2.5) == 0
    return [ident(cond, f) for f in os_]

@chk('المستقيمات المتوازية والمتعامدة', 3)
def _():
    m1, m2 = F(-2, 3), F(3, 2)
    return [m1 == m2, m1 + m2 == 0, m1*m2 == -1, m1*m2 == 1]

@chk('محور القطعة المستقيمة والنقاط المتماثلة بالنسبة لمستقيم', 5)
def _():
    A, B = (1.0, 1.0), (5.0, 3.0); M = (3.0, 2.0); dirn = (-2.0, 4.0)
    eq = dbl = between = True
    for _ in range(30):
        t = R(); P = (M[0] + t*dirn[0], M[1] + t*dirn[1])
        pa, pb = math.dist(P, A), math.dist(P, B)
        eq &= abs(pa - pb) < 1e-9; dbl &= abs(pa - 2*pb) < 1e-9
        between &= abs(pa + pb - math.dist(A, B)) < 1e-9
    return [eq, dbl, between, False]

@chk('المستقيم المار بنقطة ثابتة', 3)
def _():
    x, y = 2, 1
    b1, b2 = x + y - 3, x - y - 1
    assert all(k*b1 + b2 == 0 for k in range(-9, 10))
    slopes = {F(-(k + 1), (k - 1)) for k in (0, 2, 3)}
    return [b1 == 0 and b2 == 0, len(slopes) == 1, False, b1 == b2 == 1]

@chk('معادلة الدائرة (2)', 3)
def _():
    P, Cn = (5, 7), (2, 3)
    dC = math.dist(P, Cn)
    return [math.dist(P, (0, 0)) == 5, abs(P[1]) == 5, dC == 5, dC == 25]

@chk('معادلة الدائرة (3)', 3)
def _():
    cx, cy, r = -3, 5, 3
    tx, ty = abs(cy) == r, abs(cx) == r          # tangent to x-axis / y-axis
    mx, my = abs(cy) < r, abs(cx) < r            # cuts x-axis / y-axis in 2 points
    nox, noy = abs(cy) > r, abs(cx) > r
    return [tx and noy, tx and ty, ty and nox, mx and my]

@chk('نقاط تقاطع الدائرة والمستقيم (1)', 2)
def _():
    sub = lambda x: (x*x + (x + 2)**2 - 10) / 2
    os_ = [lambda x: x*x + 2*x + 3, lambda x: x*x - 3, lambda x: x*x + 2*x - 3, lambda x: x*x + 4*x - 6]
    roots = lambda f: {x for x in range(-10, 11) if f(x) == 0}
    assert roots(sub) == {1, -3}
    return [ident(sub, f) for f in os_]

@chk('نقاط تقاطع الدائرة والمستقيم (1)', 5)
def _():
    # x^2 + (x+5)^2 = 4 -> 2x^2 + 10x + 21 = 0
    assert ident(lambda x: x*x + (x+5)**2 - 4, lambda x: 2*x*x + 10*x + 21)
    D = 100 - 4*2*21
    assert D == -68 and 5 / math.sqrt(2) > 2     # distance from centre > radius
    return [D == 0, D > 0, 1 == 2, D < 0]        # slope 1, radius 2

@chk('طول الوتر', 4)
def _():
    r = 5.0; L = lambda d: 2*math.sqrt(r*r - d*d)
    ds = [4.9 - 0.1*i for i in range(50)]
    inc = all(L(ds[i+1]) > L(ds[i]) for i in range(49))
    return [L(0) == 0, not inc and len({L(d) for d in ds}) == 1, max(L(d) for d in ds + [0]) > 2*r, inc and L(0) == 2*r]

@chk('العلاقة الوضعية بين دائرتين', 2)
def _():
    r1, r2 = 3.0, 2.0
    def rel(d):
        if d > r1 + r2: return 'apart'
        if d == r1 + r2: return 'ext'
        if abs(r1 - r2) < d: return 'two'
        if d == abs(r1 - r2): return 'int'
        return 'inside'
    assert rel(5.0) == 'ext'
    s = {rel(5.0 + e) for e in (0.01, 1, 10, 100)}
    return [s == {'apart'}, s == {'two'}, s == {'int'}, s == {'inside'}]

def family_circle():
    # k*(x^2+y^2-4) + (x^2+y^2-2x-2) = 0 through (0,1)
    k = F(-(0 + 1 - 0 - 2), (0 + 1 - 4))
    assert k == F(-1, 3)
    A = k + 1; co = [F(1), F(1), F(-2) / A, (-4*k - 2) / A]   # x^2, y^2, x, const (normalised)
    return k, co

@chk('دائرة تمر بنقاط تقاطع دائرتين', 3)
def _():
    k, co = family_circle()
    assert [2*c for c in co] == [2, 2, -6, -2]
    return [False, False, co == [1, 1, -3, -1], False]

@chk('دائرة تمر بنقاط تقاطع دائرتين', 4)
def _():
    k, co = family_circle()
    # the two circles really intersect: centres (0,0),(1,0), radii 2, sqrt3
    assert abs(2 - math.sqrt(3)) < 1 < 2 + math.sqrt(3)
    # intersection points: subtract -> 2x - 2 = 0 -> x = 1, y = +-sqrt3
    for y in (math.sqrt(3), -math.sqrt(3)):
        assert abs(1 + y*y - 3*1 - 1) < 1e-9
    assert 0 + 1 - 0 - 1 == 0
    return [co == [1, 1, c, d] for c, d in ((-3, 1), (-3, -1), (-6, -1), (-1, -1))]

# ---------------- run ----------------
bad = 0; n = 0
assert len(by) == 88 and all(len(v) == 6 for v in by.values())
for les, qs in by.items():
    for i, q in enumerate(qs):
        if not q.get('chg'): continue
        n += 1; notes = []
        fn = C.get((les, i))
        if fn is None: notes.append('NO CHECK')
        else:
            res = fn()
            if None in res: notes.append('arguable option(s) %s' % [j for j, v in enumerate(res) if v is None])
            if [j for j, v in enumerate(res) if v is True] != [q['a']]: notes.append('truth vector %s vs a=%d' % (res, q['a']))
        if len(q['o']) != 4 or len(set(q['o'])) != 4: notes.append('options')
        if len(q['e'].split()) > 25: notes.append('e too long')
        L = [len(o) for o in q['o']]
        if all(L[q['a']] > L[j] for j in range(4) if j != q['a']): notes.append('correct strictly longest')
        if notes: bad += 1; print('FAIL', les, i, notes)
print('audited', n, 'failing', bad)
