# Independent re-solve of the b2math2 quiz (grade-2 baccalaureate maths, part 2).
# Plain Python only. Usage: python3 recheck_b2math2.py [quiz.json]
import json, re, sys, math, random, itertools
from fractions import Fraction as Fr
from math import sin, cos, tan, sqrt, pi, log, asin, acos, atan

PATH = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/khutwa/quiz/b2math2_checked.json'
Q = json.load(open(PATH))['by']
KEYS = list(Q)
random.seed(7)

# ---------------------------------------------------------------- parser
VAR = {'س': 'x', 'ص': 'y', 'أ': 'a', 'ب': 'b', 'ج': 'c', 'ك': 'k', 'م': 'm', 'ن': 'n', 'ل': 'l',
       'ت': 't', 'ث': 'C', 'ع': 'z', 'θ': 'th', 'α': 'al', 'β': 'be'}
TRIG = [('جتا', 'cos'), ('جا', 'sin'), ('ظا', 'tan')]
PHR = [('الانحراف المعيارى لـ س', ' SX '), ('توقّع س', ' EX '), ('توقّع ص', ' EY '),
       ('تباين س', ' VX '), ('تباين ص', ' VY ')]
ORD = {'الثالث': 3, 'الرابع': 4, 'الخامس': 5, 'السادس': 6}


class PErr(Exception):
    pass


def tokens(s):
    for a, b in PHR:
        s = s.replace(a, b)
    s = re.sub(r'الجذر (\S+) للعدد (-?\d+)', lambda m: '((%s)^(1/%d))' % (m.group(2), ORD[m.group(1)]) if int(m.group(2)) > 0
               else '(-((%d)^(1/%d)))' % (-int(m.group(2)), ORD[m.group(1)]), s)
    s = s.replace('هـ', ' h ').replace('×', '*').replace('÷', '/').replace('°', '').replace('−', '-')
    s = re.sub(r'\|([^|]+)\|', r'abs(\1)', s)
    out = []
    i = 0
    while i < len(s):
        c = s[i]
        if c.isspace():
            i += 1
            continue
        m = re.match(r'لو_(\(([^()]*)\)|(\d+/\d+)|(\d+)|([أ-ي]))\(', s[i:])
        if m:
            base = m.group(2) or m.group(3) or m.group(4) or m.group(5)
            out.append(('log', translate(base)))
            i += m.end() - 1
            continue
        for ar, fn in TRIG:
            if s.startswith(ar, i):
                out.append(('trig', fn))
                i += len(ar)
                break
        else:
            m = re.match(r'\d+(\.\d+)?', s[i:])
            if m:
                out.append(('num', m.group(0)))
                i += m.end()
                continue
            m = re.match(r'(pi|sqrt|abs|EX|EY|VX|VY|SX|h)(?![A-Za-z])', s[i:])
            if m:
                out.append(('fn' if m.group(1) in ('sqrt', 'abs') else 'id', m.group(1)))
                i += m.end()
                continue
            if c in VAR:
                out.append(('id', VAR[c]))
                i += 1
                continue
            if c in '+-*/^()':
                out.append(('op', c))
                i += 1
                continue
            m = re.match(r'(<=|>=|≤|≥|<|>|=)', s[i:])
            if m:
                out.append(('rel', {'≤': '<=', '≥': '>=', '=': '=='}.get(m.group(1), m.group(1))))
                i += m.end()
                continue
            raise PErr(s)
    return out


def translate(s):
    tk = tokens(s)
    return build(tk)


def group(tk, i):
    # tk[i] is '(' ; return (inner tokens, index after ')')
    d = 0
    for j in range(i, len(tk)):
        if tk[j] == ('op', '('):
            d += 1
        elif tk[j] == ('op', ')'):
            d -= 1
            if d == 0:
                return tk[i + 1:j], j + 1
    raise PErr('paren')


def build(tk):
    parts = []  # (kind, text) kind in atom/op/rel/fn
    i = 0
    while i < len(tk):
        k, v = tk[i]
        if k == 'trig':
            i += 1
            p = None
            if i < len(tk) and tk[i] == ('op', '^'):
                p = tk[i + 1][1]
                i += 2
            if i < len(tk) and tk[i] == ('op', '('):
                inner, i = group(tk, i)
                arg = build(inner)
            else:
                arg = ''
                if i < len(tk) and tk[i][0] == 'num':
                    arg = tk[i][1] + '*'
                    i += 1
                if i < len(tk) and tk[i][0] == 'id':
                    arg += tk[i][1]
                    i += 1
                else:
                    raise PErr('trig arg')
            parts.append(('atom', '(%s(%s))' % (v, arg) + ('**%s' % p if p else '')))
            if p:
                parts[-1] = ('atom', '(' + parts[-1][1] + ')')
            continue
        if k == 'log':
            inner, i = group(tk, i + 1)
            parts.append(('atom', '(log(%s)/log(%s))' % (build(inner), v)))
            continue
        if k == 'fn':
            inner, i = group(tk, i + 1)
            parts.append(('atom', '%s(%s)' % (v, build(inner))))
            continue
        if k == 'op' and v == '(':
            inner, i = group(tk, i)
            parts.append(('atom', '(' + build(inner) + ')'))
            continue
        if k in ('num', 'id'):
            parts.append(('atom', v))
        elif k == 'op':
            parts.append(('op', '**' if v == '^' else v))
        elif k == 'rel':
            parts.append(('rel', v))
        i += 1
    s = ''
    prev = None
    for k, v in parts:
        if k == 'atom' and prev == 'atom':
            s += '*'
        s += ' ' + v + ' ' if k == 'rel' else v
        prev = k
    return s


BASE = dict(sin=sin, cos=cos, tan=tan, sqrt=sqrt, pi=pi, log=log, abs=abs)


def ev(s, env=None):
    """numeric value of an option string, or None"""
    try:
        e = dict(BASE)
        e.update(env or {})
        v = eval(translate(s), {'__builtins__': {}}, e)
        return v
    except Exception:
        return None


def strip_lhs(s):
    return re.sub(r'^\s*(س|ص|θ|ك|د\(س\))\s*=\s*', '', s.strip())


def close(a, b):
    return a is not None and b is not None and not isinstance(a, bool) and abs(a - b) <= 1e-7 * max(1, abs(a), abs(b))


def pset(s, env=None):
    parts = re.split(r'\s+أو\s+|\s*،\s*', s.strip())
    vals = [ev(strip_lhs(p), env) for p in parts]
    return None if any(v is None for v in vals) else vals


def ppair(s):
    m = re.match(r'^\((.+)،(.+)\)$', s.strip())
    if not m:
        return None
    return (ev(m.group(1)), ev(m.group(2)))


def pineq(s, env):
    s = s.strip()
    if 'جميع الأعداد الحقيقية' in s:
        return True
    try:
        e = dict(BASE)
        e.update(env)
        return any(bool(eval(translate(p), {'__builtins__': {}}, e)) for p in re.split(r'\s+أو\s+', s))
    except Exception:
        return None


# ---------------------------------------------------------------- numeric helpers
def nd(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)


def simp(f, a, b, n=2000):
    if a == b:
        return 0.0
    h = (b - a) / n
    return (f(a) + f(b) + 4 * sum(f(a + (2 * i - 1) * h) for i in range(1, n // 2 + 1))
            + 2 * sum(f(a + 2 * i * h) for i in range(1, n // 2))) * h / 3


def r9(v):
    return round(v, 9)


G12 = [k * pi / 12 for k in range(24)]            # theta grid on [0, 2pi)


def troots(f, lo=0, hi=24):
    return [k * pi / 12 for k in range(lo, hi) if abs(f(k * pi / 12)) < 1e-9]


FINE = [k * pi / 360 for k in range(720)]


def fmax(f, grid=FINE):
    return max(f(t) for t in grid)


def fmin(f, grid=FINE):
    return min(f(t) for t in grid)


def argmax(f, grid=FINE):
    m = fmax(f, grid)
    r = [t for t in grid if abs(f(t) - m) < 1e-9]
    assert len(r) == 1, r
    return r[0]


def argmin(f, grid):
    m = fmin(f, grid)
    r = [t for t in grid if abs(f(t) - m) < 1e-9]
    assert len(r) == 1, r
    return r[0]


def period(f):
    xs = [0.3, 1.1, 2.9, 4.4, 5.3]
    for k in range(1, 300):
        T = k * pi / 24
        if all(abs(f(x + T) - f(x)) < 1e-9 for x in xs):
            return T


def lin(lo, hi, step):
    n = int(round((hi - lo) / step))
    return [lo + i * step for i in range(n + 1)]


def bisect(f, a, b):
    fa = f(a)
    for _ in range(200):
        m = (a + b) / 2
        fm = f(m)
        if (fa < 0) == (fm < 0):
            a, fa = m, fm
        else:
            b = m
    return (a + b) / 2


XG = [Fr(i, 100) for i in range(-600, 601)]


def extrema(f, grid=XG):
    """local maxima / minima (x, f(x)) of a polynomial with nice critical points (exact Fractions)"""
    mx, mn = [], []
    for i in range(1, len(grid) - 1):
        a, b, c = f(grid[i - 1]), f(grid[i]), f(grid[i + 1])
        if b > a and b > c:
            mx.append((grid[i], b))
        if b < a and b < c:
            mn.append((grid[i], b))
    return mx, mn


def nroots(f, grid=XG):
    """number of distinct real roots; exact zeros on the grid, sign changes elsewhere"""
    n = 0
    prev = None
    for x in grid:
        v = f(x)
        if v == 0:
            n += 1
            prev = None
            continue
        if prev is not None and (prev < 0) != (v < 0):
            n += 1
        prev = v
    return n


def dist_stats(vals, probs):
    E = sum(v * p for v, p in zip(vals, probs))
    V = sum((v - E) ** 2 * p for v, p in zip(vals, probs))
    return E, V


def joint(*ds):
    """independent joint distribution: list of (tuple of values, prob)"""
    out = []
    for combo in itertools.product(*[list(zip(*d)) for d in ds]):
        p = 1
        for _, q in combo:
            p *= q
        out.append((tuple(v for v, _ in combo), p))
    return out


def E(j, g):
    return sum(g(*v) * p for v, p in j)


def Var(j, g):
    m = E(j, g)
    return sum((g(*v) - m) ** 2 * p for v, p in j)


COIN = ([0, 1], [Fr(1, 2)] * 2)
COINS2 = ([0, 1, 2], [Fr(1, 4), Fr(1, 2), Fr(1, 4)])
DIE = ([1, 2, 3, 4, 5, 6], [Fr(1, 6)] * 6)

# ---------------------------------------------------------------- truth table
T = {}


def N(v, env=None):
    return ('num', float(v), env)


def S(vs, env=None):
    return ('set', sorted(float(v) for v in vs), env)


def F(f, samples=None):
    return ('fn', f, samples)


def FNOT(f, samples=None):
    return ('fnot', f, samples)


def P(pred):
    return ('pred', pred)          # predicate on parsed numeric value


def PT(pred):
    return ('pt', pred)            # predicate on parsed (x, y) pair


def PL(pred):
    return ('plist', pred)         # predicate on parsed list


def FP(pred):
    return ('fpred', pred)         # predicate on option as function of x (or theta)


def I(pred, var, grid):
    return ('ineq', pred, var, grid)


def ID(samples, want=True):
    return ('ident', samples, want)


def REL(samples):
    return ('rel', samples)


def GEN(roots):
    return ('gen', roots)


def AD(f, samples=None):
    return ('antider', f, samples)


def EXT(kind):
    return ('ext', kind)


def rs(names, lo=0.5, hi=2.5, n=6):
    return [{v: random.uniform(lo, hi) for v in names} for _ in range(n)]


TH = rs(['th'], 0.2, 1.3)
TG = [k / 2 for k in range(0, 48)]          # theta grid in units where pi == 12 (step pi/24)
QG = [k / 4 for k in range(-80, 81)]         # quarter grid for algebraic inequalities


def th_pred(p):
    """truth predicate on theta given in units pi=12"""
    return lambda u: p(u * pi / 12)


L = 0   # الزاوية فى الوضع القياسى
T[L, 3] = P(lambda v: (v - 140) % 360 == 0)
T[L, 4] = N(435 % 360)
T[L, 5] = N(-855 % 360)
L = 1
T[L, 0] = N(pi / 180); T[L, 1] = N(2 * pi / 2); T[L, 2] = N(630 * pi / 180); T[L, 3] = N(-7 * pi / 4 * 180 / pi)
T[L, 4] = N(6 * (2 * pi / 3)); T[L, 5] = N(0.5 * 6 ** 2 * (pi / 3))
L = 2
T[L, 3] = N(cos(5 * pi / 6)); T[L, 4] = N(tan(2 * pi / 3)); T[L, 5] = N(sin(-pi / 6))
L = 3
T[L, 1] = N(len(troots(lambda t: cos(t) - sqrt(3) / 2)))
T[L, 2] = S(troots(lambda t: sin(t) - .5)); T[L, 3] = S(troots(lambda t: cos(t) + .5))
T[L, 4] = S(troots(lambda t: sin(t) - cos(t))); T[L, 5] = S(troots(lambda t: cos(t) + 1))
L = 4
T[L, 0] = ID(TH); T[L, 3] = N(cos(pi + asin(3 / 5))); T[L, 4] = N(sin(-acos(5 / 13))); T[L, 5] = N(cos(pi + atan(2)))
L = 5
T[L, 0] = F(lambda e: (sin(e['th']) + cos(e['th'])) ** 2, TH)
T[L, 1] = F(lambda e: (sin(e['th']) ** 3 + cos(e['th']) ** 3) / (sin(e['th']) + cos(e['th'])), TH)
_th = bisect(lambda t: sin(t) + cos(t) - .5, pi / 2, pi)        # second-quadrant angle with s + c = 1/2
T[L, 3] = N(sin(_th) * cos(_th)); T[L, 4] = N(sin(_th) ** 3 + cos(_th) ** 3); T[L, 5] = N(sin(_th) - cos(_th))
L = 6
T[L, 2] = ID(TH, False); T[L, 3] = F(lambda e: tan(e['th']) * cos(e['th']), TH)
T[L, 4] = F(lambda e: (sin(e['th']) + cos(e['th'])) ** 2 + (sin(e['th']) - cos(e['th'])) ** 2, TH)
T[L, 5] = F(lambda e: 1 / cos(e['th']) ** 2 - tan(e['th']) ** 2, TH)
L = 7
T[L, 0] = F(lambda e: sin(pi + e['th']), TH); T[L, 1] = F(lambda e: cos(pi / 2 - e['th']), TH)
T[L, 2] = F(lambda e: sin(pi / 2 + e['th']), TH); T[L, 3] = ID(TH, False)
T[L, 4] = N(sin(8 * pi / 9)); T[L, 5] = N(sin(13 * pi / 6))
L = 8
T[L, 0] = N(period(sin)); T[L, 1] = N(period(tan))
T[L, 2] = I(lambda y: fmin(cos) <= y <= fmax(cos), 'y', QG)
T[L, 3] = P(lambda v: abs(cos(v)) < 1e-9)
T[L, 4] = FP(lambda f: abs(f(0)) > 1e-9)
T[L, 5] = N(argmax(sin))
L = 9
T[L, 1] = FP(lambda f: close(period(f), 2 * pi)); T[L, 2] = N(period(lambda t: sin(2 * t)))
T[L, 3] = N(period(lambda t: cos(t / 2)))
T[L, 4] = I(lambda y: r9(fmin(lambda t: 2 * cos(t))) <= y <= r9(fmax(lambda t: 2 * cos(t))), 'y', QG)
T[L, 5] = N(period(lambda t: tan(2 * t)))
L = 10
T[L, 2] = N(period(lambda t: cos(t + pi / 4)))
T[L, 3] = FP(lambda f: all(close(f(t), cos(t)) for t in (0.3, 1.7, 4.1)))
T[L, 4] = P(lambda v: abs(sin(v - pi / 3)) < 1e-9)
T[L, 5] = N(argmax(lambda t: cos(t - pi / 4)))
L = 11
T[L, 0] = FP(lambda f: all(close(f(t), sin(2 * t - pi / 3)) for t in (0.3, 1.7, 4.1)))
T[L, 3] = N(period(lambda t: 2 * sin(2 * t - pi / 3)))
_lo11, _hi11 = r9(fmin(lambda t: 3 * cos(2 * t + pi / 2))), r9(fmax(lambda t: 3 * cos(2 * t + pi / 2)))
T[L, 4] = I(lambda y: _lo11 <= y <= _hi11, 'y', QG)
T[L, 5] = N(period(lambda t: cos(t / 2 + pi / 4)))
L = 12
T[L, 2] = S(troots(lambda t: 2 * cos(t) - sqrt(3))); T[L, 3] = S(troots(lambda t: sqrt(2) * sin(t) + 1))
T[L, 4] = GEN(troots(lambda t: sin(t) - sqrt(3) * cos(t), 0, 48))
T[L, 5] = GEN(troots(lambda t: cos(t) - .5, 0, 48))
L = 13
T[L, 3] = I(th_pred(lambda t: r9(sin(t)) > .5), 'th', TG)
T[L, 4] = I(th_pred(lambda t: r9(cos(t)) <= .5), 'th', TG)
T[L, 5] = I(th_pred(lambda t: abs(cos(t)) > 1e-9 and r9(tan(t)) > 1), 'th', TG)
L = 14
T[L, 2] = S(troots(lambda t: 2 * cos(t) ** 2 + sin(t) - 1)); T[L, 3] = N(len(troots(lambda t: 2 * sin(t) ** 2 - sin(t))))
T[L, 4] = S(troots(lambda t: 2 * cos(t) ** 2 - 3 * cos(t) + 1))
T[L, 5] = I(th_pred(lambda t: r9(2 * sin(t) ** 2 - sin(t)) < 0), 'th', TG)
L = 15
T[L, 1] = I(lambda t: 0 <= t / 2 < 24, 't', [k / 2 for k in range(-30, 130)])           # t = 2 theta, pi = 12
T[L, 2] = I(lambda t: 0 <= t - 4 < 24, 't', [k / 2 for k in range(-30, 130)])           # t = theta + pi/3
T[L, 3] = N(len(troots(lambda t: sin(2 * t) - .5))); T[L, 4] = S(troots(lambda t: cos(t + pi / 6) - .5))
T[L, 5] = I(th_pred(lambda t: r9(sin(2 * t)) > 0), 'th', TG)
L = 16
T[L, 1] = I(lambda t: r9(fmin(sin)) <= t <= r9(fmax(sin)), 't', QG)
_f = lambda t: sin(t) ** 2 - 2 * sin(t)
T[L, 2] = N(fmax(_f)); T[L, 3] = N(argmax(_f)); T[L, 4] = N(fmin(lambda t: cos(t) ** 2 + cos(t)))
T[L, 5] = N(fmax(lambda t: -sin(t) ** 2 + sin(t) + 1))
L = 17
AB = rs(['al', 'be'], 0.2, 1.2)
T[L, 0] = F(lambda e: sin(e['al'] + e['be']), AB); T[L, 1] = F(lambda e: cos(e['al'] + e['be']), AB)
T[L, 3] = N(sin(math.radians(75))); T[L, 4] = N(tan(math.radians(15)))
T[L, 5] = N(sin((pi - asin(3 / 5)) + (pi + acos(5 / 13))))
L = 18
T[L, 0] = F(lambda e: tan(e['al'] - e['be']), AB)
T[L, 3] = N(abs(atan(3) - atan(.5))); T[L, 4] = N(abs(atan(sqrt(3)) - atan(sqrt(3) / 3))); T[L, 5] = N(tan(atan(2) + atan(3)))
L = 19
T[L, 0] = F(lambda e: sin(2 * e['th']), TH); T[L, 1] = FNOT(lambda e: cos(2 * e['th']), TH)
T[L, 3] = N(sin(2 * (pi - asin(3 / 5)))); T[L, 4] = N(cos(2 * acos(1 / 3))); T[L, 5] = N(tan(2 * atan(.5)))
L = 20
T[L, 0] = F(lambda e: sin(e['th'] / 2) ** 2, TH)
T[L, 3] = N(sin(acos(1 / 3) / 2)); T[L, 4] = N(cos(acos(-7 / 25) / 2)); T[L, 5] = N(sin(pi / 8) ** 2)
L = 21
T[L, 3] = N(len(troots(lambda t: sin(2 * t) - cos(t)))); T[L, 4] = S(troots(lambda t: cos(2 * t) - cos(t)))
T[L, 5] = I(th_pred(lambda t: r9(cos(2 * t) - sin(t)) < 0), 'th', TG)
L = 22
T[L, 0] = F(lambda e: fmax(lambda t: e['a'] * sin(t) + e['b'] * cos(t), [k * pi / 20000 for k in range(40000)]),
            [{'a': 3, 'b': 4}, {'a': 5, 'b': 12}, {'a': 1, 'b': 1}])
T[L, 3] = F(lambda e: sin(e['th']) + sqrt(3) * cos(e['th']), TH); T[L, 4] = F(lambda e: sin(e['th']) - cos(e['th']), TH)
T[L, 5] = N(fmax(lambda t: 3 * sin(t) + 4 * cos(t), [k * pi / 200000 for k in range(100000)]))
L = 23
T[L, 1] = I(lambda t: 0 <= t - 4 < 24, 't', [k / 2 for k in range(-30, 130)])
T[L, 2] = S(troots(lambda t: sin(t) + sqrt(3) * cos(t) - 1)); T[L, 3] = S(troots(lambda t: sin(t) - cos(t) - 1))
T[L, 4] = S(troots(lambda t: sqrt(3) * sin(t) + cos(t) - 2))
T[L, 5] = I(th_pred(lambda t: r9(sin(t) + cos(t)) > 1), 'th', TG)
L = 24
T[L, 0] = T[22, 0]
T[L, 2] = N(fmin(lambda t: 3 * sin(t) + 4 * cos(t), [k * pi / 200000 for k in range(400000)]))
_f = lambda t: sin(t) + sqrt(3) * cos(t)
T[L, 3] = N(fmax(_f)); T[L, 4] = N(argmax(_f)); T[L, 5] = N(fmax(lambda t: cos(2 * t) + 2 * sin(t)))

# ---- chapter 6
L = 25
T[L, 0] = F(lambda e: e['a'] ** 0, rs(['a']))
T[L, 1] = F(lambda e: 1 / e['a'] ** e['n'], [{'a': 1.7, 'n': 3}, {'a': 0.6, 'n': 2}, {'a': 2.2, 'n': 5}])
T[L, 2] = ID(rs(['a', 'b', 'm', 'n']), False)
T[L, 3] = N(Fr(1, 2 ** 3)); T[L, 4] = N(Fr((2 ** 3) ** 2, 2 ** 4))
T[L, 5] = F(lambda e: e['a'] ** 5 * e['a'] ** -2 / e['a'] ** 4, rs(['a']))
L = 26
T[L, 3] = P(lambda v: close(v ** 3, -8)); T[L, 4] = P(lambda v: v > 0 and close(v ** 4, 81))
T[L, 5] = N(round((4 * 2) ** (1 / 3), 9))
L = 27
T[L, 1] = F(lambda e: (e['a'] ** 2) ** (1 / 3), rs(['a'])); T[L, 2] = F(lambda e: 1 / sqrt(e['a']), rs(['a']))
T[L, 3] = N(round((8 ** 2) ** (1 / 3), 9)); T[L, 4] = N(1 / 27 ** (1 / 3)); T[L, 5] = N(round((16 ** 3) ** .25, 9))
L = 28
T[L, 0] = F(lambda e: sqrt(e['a']) * e['a'] ** (1 / 3), rs(['a'])); T[L, 1] = F(lambda e: (e['a'] ** 1.5) ** (4 / 3), rs(['a']))
T[L, 2] = F(lambda e: e['a'] ** (5 / 6) / e['a'] ** (1 / 3), rs(['a']))
T[L, 4] = N(sqrt(4) ** 3 / 2); T[L, 5] = N(sqrt(sqrt(9)) * sqrt(3))
L = 29
T[L, 0] = PT(lambda p: all(close(a ** p[0], p[1]) for a in (0.5, 2, 3.3)))
T[L, 3] = I(lambda y: y > 0, 'y', QG)
T[L, 4] = FP(lambda f: f(1) < f(0) < f(-1))
T[L, 5] = N(Fr(1, 9))
L = 30
T[L, 0] = REL([{'a': 1.5, 'm': -1, 'n': 2}, {'a': 3, 'm': 0.5, 'n': 0.7}, {'a': 1.1, 'm': -3, 'n': -2}])
T[L, 1] = REL([{'a': 0.5, 'm': -1, 'n': 2}, {'a': 0.9, 'm': 0.5, 'n': 0.7}, {'a': 0.2, 'm': -3, 'n': -2}])
T[L, 3] = EXT('max'); T[L, 4] = REL([{}]); T[L, 5] = EXT('min')
L = 31
T[L, 2] = N(bisect(lambda x: 4 ** x - 8, 0, 5)); T[L, 3] = N(bisect(lambda x: x * log(9) - (x - 1) * log(27), -10, 10))
T[L, 4] = I(lambda x: Fr(1, 2) ** Fr(x).numerator > Fr(1, 8) ** Fr(x).denominator if Fr(x).denominator > 1 else Fr(1, 2) ** int(x) > Fr(1, 8), 'x', QG)
T[L, 5] = I(lambda x: (2 * x - 1) >= 3, 'x', QG)      # 3^u >= 27 = 3^3, increasing base
L = 32
_t = lambda x: 2.0 ** x
T[L, 1] = F(lambda e: 4 ** (log(e['t']) / log(2)), rs(['t']))
HG = [k / 2 for k in range(-20, 21)]
T[L, 3] = S([x for x in HG if abs(4 ** x - 5 * 2 ** x + 4) < 1e-9]); T[L, 4] = S([x for x in HG if abs(9 ** x - 8 * 3 ** x - 9) < 1e-9])
T[L, 5] = I(lambda x: r9(4 ** x - 2 ** x - 2) > 0, 'x', QG)
L = 33
T[L, 1] = I(lambda t: 2 ** -1 <= t <= 2 ** 2, 't', QG)
XS = lin(-1, 2, 1 / 1000)
_f = lambda x: 4 ** x - 2 ** (x + 1) + 3
T[L, 3] = N(r9(fmin(_f, XS))); T[L, 4] = N(fmax(_f, XS)); T[L, 5] = N(r9(argmin(lambda x: r9(_f(x)), XS)))
L = 34
_s = [{'a': 2, 'l': 3, 'm': 8}, {'a': 1.5, 'l': -2, 'm': 1.5 ** -2}, {'a': 0.3, 'l': 0.5, 'm': 0.3 ** 0.5}]
T[L, 0] = ID(_s); T[L, 3] = ID([{}]); T[L, 4] = ID([{}]); T[L, 5] = N(2 ** 3)
L = 35
T[L, 0] = P(lambda v: abs(v) < 1e-12)
T[L, 1] = F(lambda e: log(e['a'] ** e['l']) / log(e['a']), rs(['a', 'l'], 1.2, 3))
T[L, 2] = F(lambda e: log(e['a']) / log(e['a']), rs(['a'], 1.2, 3))
T[L, 3] = N(log(16, 2)); T[L, 4] = N(log(1 / 5, 5)); T[L, 5] = N(log(sqrt(27), 3))
L = 36
T[L, 0] = F(lambda e: log(e['m'] * e['n']) / log(e['a']), rs(['a', 'm', 'n'], 1.2, 3))
T[L, 1] = ID(rs(['a', 'm', 'n', 'k'], 1.2, 3), False)
T[L, 2] = N(2 * log(5, 3)); T[L, 3] = N(log(4, 6) + log(9, 6)); T[L, 4] = N(log(24, 2) - log(3, 2)); T[L, 5] = N(2 * log(5, 10) + log(4, 10))
L = 37
T[L, 0] = F(lambda e: log(e['b']) / log(e['a']), rs(['a', 'b', 'c'], 1.2, 3))
T[L, 2] = F(lambda e: log(e['b'], e['a']) * log(e['a'], e['b']), rs(['a', 'b'], 1.2, 3))
T[L, 3] = N(log(4, 8)); T[L, 4] = N(log(27, 9)); T[L, 5] = N(log(1 / 8, 4))
L = 38
T[L, 1] = N(log(9, 4)); T[L, 2] = N(log(3, 2) * log(8, 3)); T[L, 3] = N(log(5, 3) * log(9, 5))
T[L, 4] = N(r9(log(9, 4) - log(3, 2))); T[L, 5] = N(log(3, 2) * log(5, 3) * log(2, 5))
L = 39
AB10 = {'a': math.log10(2), 'b': math.log10(3)}
T[L, 0] = ('expr5', None)
T[L, 1] = N(math.log10(6), AB10); T[L, 2] = N(math.log10(5), AB10); T[L, 3] = N(math.log10(12), AB10)
T[L, 4] = N(log(3, 2), AB10); T[L, 5] = N(math.log10(18), AB10)
L = 40
T[L, 0] = PT(lambda p: p[0] > 0 and all(close(log(p[0], a), p[1]) for a in (0.5, 2, 3.3)))
T[L, 4] = I(lambda x: x - 2 > 0, 'x', QG)
T[L, 5] = N(sqrt(9))
L = 41
T[L, 0] = REL([{'a': 1.5, 'm': 1, 'n': 2}, {'a': 3, 'm': 0.5, 'n': 0.7}, {'a': 1.1, 'm': 3, 'n': 300}])
T[L, 1] = REL([{'a': 0.5, 'm': 1, 'n': 2}, {'a': 0.9, 'm': 0.5, 'n': 0.7}, {'a': 0.2, 'm': 3, 'n': 300}])
T[L, 2] = P(lambda v: close(v, 2)); T[L, 3] = REL([{}]); T[L, 4] = EXT('max'); T[L, 5] = EXT('min')
L = 42
T[L, 1] = I(lambda x: x - 3 > 0, 'x', QG)
T[L, 3] = N(bisect(lambda x: log(x - 1, 2) - 3, 1.001, 100))
T[L, 4] = S([x for x in QG if x > 2 and abs(log(x, 2) + log(x - 2, 2) - 3) < 1e-9])
T[L, 5] = N(bisect(lambda x: log(2 * x + 1, 3) - log(x + 4, 3), 0, 100))
L = 43
T[L, 3] = I(lambda x: x > 0 and r9(log(x, 2)) < 3, 'x', QG)
T[L, 4] = I(lambda x: x > 0 and r9(log(x, .5)) > 2, 'x', QG)
T[L, 5] = I(lambda x: x - 1 > 0 and r9(log(x - 1, 3)) >= 1, 'x', QG)
L = 44


def quad(a, b, c):
    d = sqrt(b * b - 4 * a * c)
    return [(-b - d) / (2 * a), (-b + d) / (2 * a)]


T[L, 3] = S([2 ** t for t in quad(1, -3, 2)]); T[L, 4] = S([3 ** t for t in quad(1, -1, -2)])
T[L, 5] = I(lambda x: x > 0 and r9(log(x, 2) ** 2 - 3 * log(x, 2) + 2) < 0, 'x', QG)
L = 45
T[L, 2] = I(lambda t: r9(log(1, 2)) <= t <= r9(log(8, 2)), 't', QG)
XS = lin(1, 8, 1 / 1000)
_g = lambda x: r9(-log(x, 2) ** 2 + 4 * log(x, 2))
T[L, 3] = N(fmax(_g, XS)); T[L, 4] = N(r9(argmax(_g, XS))); T[L, 5] = N(fmin(_g, XS))
L = 46
T[L, 1] = F(lambda e: len(str(int(10 ** (e['n'] - 0.5)))), [{'n': 3}, {'n': 5}, {'n': 8}])
T[L, 2] = N(len(str(int(10 ** 3.2)))); T[L, 3] = N(len(str(2 ** 50))); T[L, 4] = N(len(str(3 ** 20)))
T[L, 5] = N(min(k for k in range(1, 40) if Fr(10 ** k, 2 ** 20) >= 1))

# ---- chapter 7
L = 47
avg = lambda f, a, b: (f(b) - f(a)) / (b - a)
T[L, 2] = N(avg(lambda x: 3 * x + 1, -1.3, 4.1)); T[L, 3] = N(avg(lambda x: x * x, 1, 3)); T[L, 4] = N(avg(lambda x: 2 * x * x - 1, -1, 2))
T[L, 5] = F(lambda e: avg(lambda x: x * x + 2 * x, 1, 1 + e['h']), rs(['h'], 0.1, 2))
L = 48
T[L, 2] = N(2 ** 2 + 3 * 2); T[L, 3] = N(round(((1 + 1e-7) ** 2 - 1) / 1e-7, 5))
T[L, 4] = N(round(((3 + 1e-7) ** 2 - (3 + 1e-7) - 6) / 1e-7, 5)); T[L, 5] = N(round((6e-7 + 1e-14) / 1e-7, 5))
L = 49
T[L, 3] = F(lambda e: ((1 + e['h']) ** 2 - 1) / e['h'], rs(['h'], 0.1, 2))
T[L, 4] = N(round(nd(lambda x: x * x, 3), 6)); T[L, 5] = N(round(nd(lambda x: x * x - 4 * x, 2), 6))
L = 50
XH = rs(['x', 'h'], 0.3, 2)
T[L, 3] = F(lambda e: (e['x'] + e['h']) ** 2 - e['x'] ** 2, XH)
T[L, 4] = F(lambda e: nd(lambda x: x * x, e['x']), XH); T[L, 5] = F(lambda e: nd(lambda x: 3 * x + 2, e['x']), XH)
L = 51
T[L, 0] = F(lambda e: nd(lambda x: x ** e['n'], e['x']), [{'x': 1.3, 'n': 2}, {'x': 0.7, 'n': 3}, {'x': 1.9, 'n': 5}])
T[L, 2] = F(lambda e: round(nd(lambda x: 5, e['x']), 6), rs(['x']))
T[L, 3] = F(lambda e: nd(lambda x: 2 * x ** 3 - 4 * x ** 2 + 5 * x - 7, e['x']), rs(['x']))
T[L, 4] = F(lambda e: nd(lambda x: (2 * x - 1) ** 2, e['x']), rs(['x']))
T[L, 5] = N(round(nd(lambda x: x ** 3 - 3 * x, 2), 5))
L = 52
T[L, 0] = F(lambda e: nd(lambda x: e['a'] * x * x + e['b'] * x + e['c'], e['x']), rs(['a', 'b', 'c', 'x']))
_c52 = 1; _b52 = -2; _a52 = (4 - _b52) / 2            # d(0)=1, d'(0)=b=-2, d'(1)=2a+b=4
T[L, 3] = F(lambda e: _a52 * e['x'] ** 2 + _b52 * e['x'] + _c52, rs(['x']))
T[L, 4] = N(4 / 2)                              # 2a = 4
T[L, 5] = N(2 - (4 / 2) * 1 - (-3) * 1)         # c = d(1) - a - b
L = 53
T[L, 2] = N(bisect(lambda x: nd(lambda u: u * u - 6 * u, x), -10, 10)); T[L, 3] = N(round(nd(lambda x: x * x - 4 * x + 1, 3), 5))
tangent = lambda f, a: (lambda x: f(a) + nd(f, a) * (x - a))
T[L, 4] = F(lambda e: tangent(lambda x: x * x, 1)(e['x']), rs(['x'])); T[L, 5] = F(lambda e: tangent(lambda x: x ** 3 - 2 * x, 2)(e['x']), rs(['x']))
L = 54
T[L, 2] = F(lambda e: tangent(lambda x: x * x, bisect(lambda u: nd(lambda x: x * x, u) - 4, -10, 10))(e['x']), rs(['x']))
T[L, 3] = PT(lambda p: close(nd(lambda x: x * x + 2 * x, p[0]), -2) and close(p[0] ** 2 + 2 * p[0], p[1]))
T[L, 4] = S([t for t in HG if abs(tangent(lambda x: x * x, t)(0) + 1) < 1e-6])
T[L, 5] = FP(lambda f: close(f(0), -1) and close((f(1) - f(0)) ** 2 + 4 * f(0), 0))
L = 55
_f = lambda x: x ** 3 - 3 * x
T[L, 3] = N(extrema(_f)[0][0][1]); T[L, 4] = N(extrema(_f)[1][0][0])
T[L, 5] = I(lambda x: r9(nd(lambda u: u ** 3 - 3 * u, x)) < 0, 'x', QG)
L = 56
_f = lambda x: x ** 3 - 3 * x ** 2 + 2
T[L, 2] = N(fmax(_f, lin(-2, 4, 1 / 500))); T[L, 3] = N(fmin(_f, lin(-2, 4, 1 / 500))); T[L, 4] = N(fmin(_f, lin(0, 3, 1 / 500)))
T[L, 5] = N(argmax(lambda x: r9(-x ** 3 + 3 * x), lin(0, 2, 1 / 500)))
L = 57
# 3 + 2a + b = 0 and 27 + 6a + b = 0
_a = Fr(-(27 - 3), 6 - 2); _b = -3 - 2 * _a
assert len(extrema(lambda x: x ** 3 + _a * x ** 2 + _b * x)[0]) == 1
T[L, 2] = N(_a); T[L, 3] = N(_b)
_c = 5 - extrema(lambda x: x ** 3 - 3 * x)[0][0][1]
T[L, 4] = N(_c); T[L, 5] = N(extrema(lambda x: x ** 3 - 3 * x)[1][0][1] + _c)
L = 58
nx = lambda f: sum(map(len, extrema(f)))
T[L, 3] = N(nx(lambda x: x ** 3 + 3 * x ** 2 + 3 * x + 1))
T[L, 4] = I(lambda k: (2 * k) ** 2 - 4 * 3 * 12 <= 0, 'k', QG)
T[L, 5] = I(lambda k: (-6) ** 2 - 4 * 3 * k > 0, 'k', QG)
L = 59
T[L, 2] = FP(lambda f: all(f(x + .01) > f(x) for x in lin(-5, 5, .01)))
T[L, 3] = I(lambda k: (2 * k) ** 2 - 4 * 3 * 3 <= 0, 'k', QG)
T[L, 4] = I(lambda k: (-6) ** 2 - 4 * 3 * k <= 0, 'k', QG)
T[L, 5] = I(lambda k: max(-3 * x * x + k for x in lin(-5, 5, .25)) <= 0, 'k', QG)
L = 60
T[L, 3] = N(nroots(lambda x: x ** 3 - 3 * x + 1)); T[L, 4] = N(nroots(lambda x: x ** 3 - 3 * x + 2)); T[L, 5] = N(nroots(lambda x: x ** 3 + 3 * x + 5))
L = 61
KG = [Fr(k, 4) for k in range(-40, 41)]
_n1 = {float(k): nroots(lambda x: x ** 3 - 3 * x - k) for k in KG}
_n2 = {float(k): nroots(lambda x: x ** 3 - 3 * x ** 2 - k) for k in KG}
FKG = [float(k) for k in KG]
T[L, 2] = I(lambda k: _n1[k] == 3, 'k', FKG); T[L, 3] = I(lambda k: _n1[k] == 1, 'k', FKG)
T[L, 4] = S([k for k in FKG if _n1[k] == 2]); T[L, 5] = I(lambda k: _n2[k] == 3, 'k', FKG)
L = 62
T[L, 2] = F(lambda e: (e['x'] ** 3 + 2) - 3 * e['x'], rs(['x']))
XP = [Fr(i, 100) for i in range(0, 1001)]
_f = lambda x: x ** 3 - 3 * x + 2
T[L, 3] = N(min(_f(x) for x in XP)); T[L, 4] = S([x for x in XP if x ** 3 + 2 == 3 * x])
T[L, 5] = N(argmin(lambda x: x ** 3 - 3 * x ** 2 + 4, XP))
L = 63
T[L, 2] = F(lambda e: nd(lambda x: x ** 4 - 2 * x ** 2, e['x']), rs(['x']))
_e = extrema(lambda x: x ** 4 - 2 * x ** 2)
assert len({v for _, v in _e[1]}) == 1 and len(_e[0]) == 1
T[L, 3] = N(_e[1][0][1]); T[L, 4] = N(_e[0][0][0]); T[L, 5] = N(nx(lambda x: x ** 4 - 4 * x ** 3))
L = 64
T[L, 2] = AD(lambda e: e['x'] ** e['n'], [{'x': 1.3, 'n': 2}, {'x': 0.7, 'n': 3}, {'x': 1.9, 'n': 4}])
T[L, 3] = AD(lambda e: 4 * e['x'] ** 3); T[L, 4] = AD(lambda e: 6 * e['x'] ** 2 - 4 * e['x'] + 1)
T[L, 5] = AD(lambda e: (e['x'] + 1) * (e['x'] - 1))
L = 65
T[L, 3] = F(lambda e: 1 + simp(lambda x: 2 * x + 3, 0, e['x']), rs(['x']))
T[L, 4] = N(2 - simp(lambda x: 3 * x * x - 4 * x, 0, 1)); T[L, 5] = N(4 + simp(lambda x: 6 * x - 2, 1, 2))
L = 66
T[L, 3] = F(lambda e: 2 + simp(lambda x: 2 * x - 1, 1, e['x']), rs(['x']))
T[L, 4] = N(3 + simp(lambda x: 3 * x * x, 0, 2)); T[L, 5] = N(1 + simp(lambda x: 4 * x - 3, 2, 0))
L = 67
T[L, 3] = N(simp(lambda x: 3 * x * x, 0, 2)); T[L, 4] = N(simp(lambda x: 2 * x + 1, 1, 3)); T[L, 5] = N(r9(simp(lambda x: x * x - 1, -1, 2)))
L = 68
T[L, 2] = N(-6); T[L, 3] = N(10 - 3)
T[L, 4] = N(simp(lambda x: x * x + 2 * x, 0, 1) + simp(lambda x: x * x + 2 * x, 1, 3))
T[L, 5] = N(simp(lambda x: x * x + 3 * x, 0, 2) + simp(lambda x: 2 * x * x - 3 * x, 0, 2))
L = 69
_k = bisect(lambda k: simp(lambda t: 2 * t + k, 0, 2) - k, -100, 100)
T[L, 2] = N(_k); T[L, 3] = N(2 * 1 + _k)
_k2 = bisect(lambda k: simp(lambda t: 6 * t * t - k, 0, 1) - k, -100, 100)
T[L, 4] = F(lambda e: 6 * e['x'] ** 2 - _k2, rs(['x']))
L = 70
T[L, 3] = F(lambda e: nd(lambda x: x * x + 2 * x - 3, e['x']), rs(['x']))
T[L, 4] = N(bisect(lambda a: a * a - 4, 0, 100))
T[L, 5] = F(lambda e: nd(lambda x: simp(lambda t: t * t + 1, 2, x, 200), e['x']), rs(['x']))
L = 71
area = lambda f, a, b: simp(lambda x: abs(f(x)), a, b)
T[L, 3] = N(area(lambda x: x * x, 0, 3)); T[L, 4] = N(area(lambda x: 4 - x * x, -2, 2)); T[L, 5] = N(area(lambda x: x * x - 2 * x, 0, 2))
L = 72
T[L, 2] = S([x for x in HG if x * x == x + 2])
T[L, 3] = N(area(lambda x: x + 2 - x * x, -1, 2)); T[L, 4] = N(area(lambda x: 2 * x - x * x, 0, 2)); T[L, 5] = N(area(lambda x: 2 - 2 * x * x, -1, 1))
L = 73
T[L, 2] = S([x for x in HG if x ** 3 - 4 * x == 0])
T[L, 3] = N(area(lambda x: x ** 3 - 4 * x, -2, 0) + area(lambda x: x ** 3 - 4 * x, 0, 2))
T[L, 4] = N(area(lambda x: x ** 3 - 3 * x * x, 0, 3))
T[L, 5] = N(area(lambda x: x ** 3 - 3 * x * x + 2 * x, 0, 1) + area(lambda x: x ** 3 - 3 * x * x + 2 * x, 1, 2))
L = 74
T[L, 3] = N(simp(lambda x: abs(x - 1), 0, 1) + simp(lambda x: abs(x - 1), 1, 3))
T[L, 4] = N(simp(abs, -1, 0) + simp(abs, 0, 3))
T[L, 5] = N(simp(lambda x: abs(x * x - 4), 0, 2) + simp(lambda x: abs(x * x - 4), 2, 3))
L = 75
_t1 = tangent(lambda x: x * x, -1); _t2 = tangent(lambda x: x * x, 1)
_xi = bisect(lambda x: _t1(x) - _t2(x), -5, 5)
T[L, 2] = N(r9(_xi))
T[L, 3] = N(simp(lambda x: x * x - _t1(x), -1, _xi) + simp(lambda x: x * x - _t2(x), _xi, 1))
T[L, 4] = N(simp(lambda x: x * x - _t2(x), 0, 1))
_t3 = tangent(lambda x: x ** 3, 1)
T[L, 5] = S([float(x) for x in XG if x != 1 and abs(float(x) ** 3 - _t3(float(x))) < 1e-6])
L = 76
T[L, 0] = F(lambda e: area(lambda x: e['a'] * (x - e['al']) * (x - e['be']), e['al'], e['be']),
            [{'a': 2, 'al': 1, 'be': 3}, {'a': -1.5, 'al': -1, 'be': 2}, {'a': 1, 'al': 0.5, 'be': 4}])
T[L, 2] = N(area(lambda x: 2 * x - x * x, 0, 2)); T[L, 3] = N(area(lambda x: 4 - x * x, -2, 2))
T[L, 4] = F(lambda e: bisect(lambda x: 2 * x - x * x - e['m'] * x, 1e-6 + 0.0, 5) if True else 0, rs(['m'], 0.2, 1.8))
T[L, 5] = N(bisect(lambda m: simp(lambda x: 2 * x - x * x - m * x, 0, 2 - m) - area(lambda x: 2 * x - x * x, 0, 2) / 2, 0, 2))

# ---- chapter 8
L = 77
T[L, 2] = PL(lambda v: sum(Fr(x).limit_denominator(1000) for x in v) != 1)
_two = [(a, b) for a in 'HT' for b in 'HT']
T[L, 3] = S(sorted({o.count('H') for o in _two})); T[L, 4] = N(Fr(sum(o.count('H') == 1 for o in _two), 4)); T[L, 5] = N(1 - 0.2 - 0.5)
L = 78
T[L, 3] = N(Fr(sum(o.count('H') for o in _two), 4)); T[L, 4] = N(dist_stats([1, 2, 4], [Fr(1, 2), Fr(1, 4), Fr(1, 4)])[0])
_dr = list(itertools.combinations('RRRWW', 2))
T[L, 5] = N(Fr(sum(c.count('R') for c in _dr), len(_dr)))
L = 79
J1 = joint(([1, 2, 6], [Fr(1, 2), Fr(1, 4), Fr(1, 4)]))
_EX = E(J1, lambda x: x)
T[L, 0] = F(lambda e: E(J1, lambda x: e['a'] * x + e['b']), [{'a': 2, 'b': 3, 'EX': _EX}, {'a': -1.5, 'b': 0.5, 'EX': _EX}])
T[L, 3] = N(E(joint(([1, 5], [Fr(1, 2)] * 2)), lambda x: 2 * x + 5))       # E = 3
T[L, 4] = N(E(joint(([3, 5], [Fr(1, 2)] * 2)), lambda x: 10 - 3 * x))      # E = 4
T[L, 5] = N(E(joint(COINS2), lambda x: x * x))
L = 80
_d = joint(([1, 3], [Fr(1, 2)] * 2)); assert E(_d, lambda x: x) == 2 and E(_d, lambda x: x * x) == 5
T[L, 3] = N(Var(_d, lambda x: x)); T[L, 4] = N(Var(joint(COINS2), lambda x: x)); T[L, 5] = N(Var(joint(DIE), lambda x: x))
L = 81
T[L, 3] = N(sqrt(9))
_d = joint(([1, 5], [Fr(1, 2)] * 2)); assert E(_d, lambda x: x) == 3 and E(_d, lambda x: x * x) == 13
T[L, 4] = N(sqrt(Var(_d, lambda x: x))); T[L, 5] = N(sqrt(Var(joint(COINS2), lambda x: x)))
L = 82
_VX = float(Var(J1, lambda x: x))
T[L, 0] = F(lambda e: float(Var(J1, lambda x: Fr(e['a']) * x + Fr(e['b']))), [{'a': 2, 'b': 3, 'VX': _VX}, {'a': -1.5, 'b': 0.5, 'VX': _VX}])
T[L, 1] = F(lambda e: sqrt(Var(J1, lambda x: Fr(e['a']) * x + Fr(e['b']))),
            [{'a': 2, 'b': 3, 'SX': sqrt(_VX)}, {'a': -1.5, 'b': 0.5, 'SX': sqrt(_VX)}, {'a': -3, 'b': -2, 'SX': sqrt(_VX)}])
_d = joint(([-2, 2], [Fr(1, 2)] * 2)); assert Var(_d, lambda x: x) == 4
T[L, 3] = N(Var(_d, lambda x: 3 * x + 2)); T[L, 4] = N(sqrt(Var(_d, lambda x: -3 * x + 1)))
_d5 = [((-sqrt(5),), .5), ((sqrt(5),), .5)]
T[L, 5] = N(Var(_d5, lambda x: x + 7))
L = 83
T[L, 0] = F(lambda e: 10 * e['x'] - 5, rs(['x']))
T[L, 2] = N(E(joint(COINS2), lambda x: 10 * x - 5)); T[L, 3] = N(sqrt(Var(joint(COINS2), lambda x: 10 * x - 5)))
T[L, 4] = N(1 / 2)                 # |a| * 2 = 1, a > 0
T[L, 5] = N(-5 * (1 / 2))          # 5a + b = 0
_d = joint(([3, 7], [Fr(1, 2)] * 2)); assert E(_d, lambda x: x) == 5 and Var(_d, lambda x: x) == 4
assert E(_d, lambda x: x / 2 - Fr(5, 2)) == 0 and Var(_d, lambda x: x / 2 - Fr(5, 2)) == 1
L = 84
T[L, 2] = N(2.5 + 4); T[L, 3] = N(E(joint(DIE, DIE), lambda x, y: x + y)); T[L, 4] = N(E(joint(COIN, DIE), lambda x, y: x + y))
T[L, 5] = N(E(joint(DIE, DIE, DIE), lambda x, y, z: x + y + z))
L = 85
JD = [((1, 2), Fr(1, 2)), ((3, 3), Fr(1, 4)), ((5, 1), Fr(1, 4))]        # dependent pair
_ex, _ey = float(E(JD, lambda x, y: x)), float(E(JD, lambda x, y: y))
T[L, 0] = F(lambda e: float(E(JD, lambda x, y: Fr(e['a']) * x + Fr(e['b']) * y)),
            [{'a': 2, 'b': 3, 'EX': _ex, 'EY': _ey}, {'a': -1.5, 'b': 0.5, 'EX': _ex, 'EY': _ey}])
T[L, 2] = N(3 * 2 + 2 * 3); T[L, 3] = N(2 * 4 - 3 * 1)
T[L, 4] = N(E(joint(DIE, DIE), lambda x, y: x - y)); T[L, 5] = N(E(joint(COINS2, DIE), lambda x, y: 4 * x + 2 * y))
L = 86
JI = joint(([1, 2, 6], [Fr(1, 2), Fr(1, 4), Fr(1, 4)]), ([2, 5], [Fr(1, 3), Fr(2, 3)]))
T[L, 0] = F(lambda e: float(E(JI, lambda x, y: x * y)), [{'EX': float(E(JI, lambda x, y: x)), 'EY': float(E(JI, lambda x, y: y))}])
_d = joint(([1, 5], [Fr(1, 2)] * 2), ([4, 6], [Fr(1, 2)] * 2))
T[L, 3] = N(E(_d, lambda x, y: x * y)); T[L, 4] = N(E(joint(DIE, DIE), lambda x, y: x * y)); T[L, 5] = N(E(joint(COIN, DIE), lambda x, y: x * y))
L = 87
T[L, 0] = F(lambda e: float(Var(JI, lambda x, y: x + y)), [{'VX': float(Var(JI, lambda x, y: x)), 'VY': float(Var(JI, lambda x, y: y))}])


def two(v1, v2):
    return [((sx * sqrt(v1), sy * sqrt(v2)), .25) for sx in (-1, 1) for sy in (-1, 1)]


T[L, 2] = N(sqrt(Var(two(3, 4), lambda x, y: x + y))); T[L, 3] = N(Var(two(5, 3), lambda x, y: x - y))
T[L, 4] = N(Var(two(2, 1), lambda x, y: 3 * x + 2 * y)); T[L, 5] = N(Var(joint(DIE, DIE), lambda x, y: x + y))
L = 88
T[L, 3] = N(2 + 3 + 4)
_d = joint(([1, 3], [Fr(1, 2)] * 2), ([2, 4], [Fr(1, 2)] * 2), ([3, 5], [Fr(1, 2)] * 2))
T[L, 4] = N(E(_d, lambda x, y, z: x * y * z)); T[L, 5] = N(Var(joint(DIE, DIE, DIE), lambda x, y, z: x + y + z))

# ---------------------------------------------------------------- run
bad = 0
done = 0


def fail(k, j, msg):
    global bad
    bad += 1
    print('FAIL [%d] %s q%d: %s | %s' % (KEYS.index(k), k, j, msg, Q[k][j]['q'][:50]))


def hits_for(spec, opts):
    kind = spec[0]
    if kind == 'num':
        vals = [ev(strip_lhs(o), spec[2]) for o in opts]
        num = [v for v in vals if v is not None]
        dup = any(close(a, b) for a, b in itertools.combinations(num, 2))
        return [close(v, spec[1]) for v in vals], dup
    if kind == 'set':
        vs = [pset(o, spec[2]) for o in opts]
        ok = [v is not None and len(v) == len(spec[1]) and all(close(a, b) for a, b in zip(sorted(v), spec[1])) for v in vs]
        dup = any(a is not None and b is not None and len(a) == len(b) and all(close(x, y) for x, y in zip(sorted(a), sorted(b)))
                  for a, b in itertools.combinations(vs, 2))
        return ok, dup
    if kind in ('fn', 'fnot'):
        samples = spec[2] or rs(['x'])
        rows = [[ev(strip_lhs(o), e) for e in samples] for o in opts]
        truth = [spec[1](e) for e in samples]
        eq = [all(close(v, t) for v, t in zip(r, truth)) for r in rows]
        dup = any(all(close(x, y) for x, y in zip(a, b)) for a, b in itertools.combinations(rows, 2))
        if kind == 'fnot':
            return [not x for x in eq], any(None in r for r in rows)
        return eq, dup
    if kind == 'pred':
        vals = [ev(strip_lhs(o)) for o in opts]
        return [v is not None and bool(spec[1](v)) for v in vals], False
    if kind == 'pt':
        vals = [ppair(o) for o in opts]
        return [v is not None and None not in v and bool(spec[1](v)) for v in vals], False
    if kind == 'plist':
        vals = [pset(o) for o in opts]
        return [v is not None and bool(spec[1](v)) for v in vals], False
    if kind == 'fpred':
        def mk(o):
            src = strip_lhs(o)
            if ev(src, {'x': 0.37, 'th': 0.37}) is None:
                return None
            return lambda u: ev(src, {'x': u, 'th': u})
        fs = [mk(o) for o in opts]
        return [f is not None and bool(spec[1](f)) for f in fs], False
    if kind == 'ineq':
        _, pred, var, grid = spec
        truth = [bool(pred(g)) for g in grid]
        rows = []
        for o in opts:
            env = {'pi': 12.0} if var in ('th', 't') else {}
            row = []
            for g in grid:
                env[var] = g
                row.append(pineq(o, env))
            rows.append(row)
        dup = any(a == b for a, b in itertools.combinations(rows, 2))
        return [r == truth for r in rows], dup
    if kind == 'ident':
        res = []
        for o in opts:
            if o.count('=') != 1:
                res.append(None)
                continue
            l, r = re.sub(r'\s(لأى|حيث)\s.*$', '', o).split('=')
            try:
                translate(l), translate(r)
            except Exception:
                res.append(None)
                continue
            vals = [(ev(l, e), ev(r, e)) for e in spec[1]]
            res.append(all(close(a, b) for a, b in vals))
        if None in res:
            return [False] * 4, True
        return [x == spec[2] for x in res], False
    if kind == 'rel':
        res = []
        for o in opts:
            vals = [pineq(o, dict(e)) for e in spec[1]]
            res.append(None if None in vals else all(vals))
        if None in res:
            return [False] * 4, True
        return [bool(x) for x in res], False
    if kind == 'gen':
        true = sorted(r9(v) for v in spec[1])            # roots in [0, 4pi)
        res = []
        for o in opts:
            got = set()
            for part in re.split(r'\s+أو\s+', o):
                b0, b1 = ev(part, {'n': 0}), ev(part, {'n': 1})
                if b0 is None:
                    got = None
                    break
                for n in range(-8, 9):
                    v = b0 + n * (b1 - b0)
                    if -1e-9 <= v < 4 * pi - 1e-9:
                        got.add(r9(v))
            res.append(got is not None and sorted(got) == true)
        return res, False
    if kind == 'antider':
        samples = spec[2] or rs(['x'])
        res = []
        for o in opts:
            src = re.sub(r'\s*\+\s*ث\s*$', '', o)
            assert src != o, 'no constant of integration'
            ok = True
            for e in samples:
                d = nd(lambda u: ev(src, dict(e, x=u)) or float('nan'), e['x'])
                ok = ok and close(round(d, 6), round(spec[1](e), 6))
            res.append(ok)
        return res, False
    if kind == 'ext':
        vals = [ev(o) for o in opts]
        if None in vals:
            return [False] * 4, True
        m = max(vals) if spec[1] == 'max' else min(vals)
        return [close(v, m) for v in vals], len({r9(v) for v in vals}) < 4
    if kind == 'expr5':
        # L39 q0: only an expression built from 10 and 2 alone that equals 5 is acceptable
        vals = [ev(o) for o in opts]
        return [close(v, 5) and set(re.findall(r'\d+', o)) <= {'10', '2'} for v, o in zip(vals, opts)], \
            any(not close(v, 5) for v in vals)
    raise ValueError(kind)


for (li, j), spec in sorted(T.items()):
    k = KEYS[li]
    if j >= len(Q[k]):
        continue
    q = Q[k][j]
    if q.get('_new'):
        continue
    try:
        hits, dup = hits_for(spec, q['o'])
    except Exception as ex:
        fail(k, j, 'error %r' % ex)
        continue
    done += 1
    if sum(hits) != 1:
        fail(k, j, 'matches=%s' % hits)
    elif not hits[q['a']]:
        fail(k, j, 'key %d but computed option %d' % (q['a'], hits.index(True)))
    elif dup:
        fail(k, j, 'two options equivalent')

# generic structural pass over every question
for k, qs in Q.items():
    if not 5 <= len(qs) <= 6:
        fail(k, 0, 'count %d' % len(qs))
    stems = [q['q'] for q in qs]
    if len(set(stems)) != len(stems):
        fail(k, 0, 'duplicate stem')
    for j, q in enumerate(qs):
        o, a = q['o'], q['a']
        if len(o) != 4 or len(set(x.strip() for x in o)) != 4 or not 0 <= a <= 3:
            fail(k, j, 'options')
            continue
        if len(o[a]) > max(len(x) for i, x in enumerate(o) if i != a):
            fail(k, j, 'correct option strictly longest')
        if len(q['e'].split()) > 25:
            fail(k, j, 'e > 25 words')
        vals = [ev(strip_lhs(x)) for x in o]
        for x, y in itertools.combinations(range(4), 2):
            if vals[x] is not None and vals[y] is not None and not re.search(r'[<>≤≥،]| أو ', o[x] + o[y]) \
                    and not isinstance(vals[x], bool) and close(vals[x], vals[y]) and (KEYS.index(k), j) not in ((39, 0), (17, 2)) and 'غير معرّف' not in q['q']:
                fail(k, j, 'numerically equal options %s | %s' % (o[x], o[y]))
        txt = q['q'] + ' ' + q['e'] + ' ' + ' '.join(o)
        if re.search(r'لو_\d+/\d+\(|\$|\\frac|السؤال السابق|كهذه|أعلاه', txt):
            fail(k, j, 'notation/standalone')
        if re.search(r'(?<![\w])(في|التي|الذي|إلي)(?![\w\u064B-\u0652])', txt):
            fail(k, j, 'spelling style differs from the book convention (فى/التى/الذى)')

from collections import Counter
tot = sum(map(len, Q.values()))
print('file', PATH)
print('lessons', len(Q), 'questions', tot, 'key distribution', sorted(Counter(q['a'] for v in Q.values() for q in v).items()))
print('re-solved numerically', done, '| failures', bad)
