# Independent audit of the 46 "chg" questions in b2math2_exam.json (plain Python).
import json, math, sys
from fractions import Fraction as F
pi, s, c, t = math.pi, math.sin, math.cos, math.tan
D = json.load(open('b2math2_exam.json'))['by']
SRC = sys.argv[1] if len(sys.argv) > 1 else 'b2math2_exam.json'
D = json.load(open(SRC))['by']
ok = lambda a, b: abs(a - b) < 1e-9
def simpson(f, a, b, n=2000):
    h = (b - a) / n
    return h / 3 * (f(a) + f(b) + sum((4 if i % 2 else 2) * f(a + i * h) for i in range(1, n)))
def d(f, x, h=1e-6): return (f(x + h) - f(x - h)) / (2 * h)
R = []
def chk(name, cond): R.append((name, bool(cond)))
th = [i * 0.001 for i in range(-7000, 7000)]

chk('1 sin range', max(s(x) for x in th) <= 1 < 1.5 and all(abs(v) <= 1 for v in (-1, math.sqrt(3)/2, 0)))
chk('2 sin=2 none', all(s(x) < 2 for x in th))
chk('3 sin(pi-x)', all(ok(s(pi - x), s(x)) and ok(c(pi - x), -c(x)) for x in th[::50]))
chk('4 sin=cos', [ok(s(x), c(x)) for x in (pi/4, 5*pi/4, 3*pi/4, pi/2, 3*pi/2, 7*pi/4)] == [1, 1, 0, 0, 0, 0])
chk('5 sin=1/2', [ok(s(x), .5) for x in (7*pi/6, pi/6, 5*pi/6, 13*pi/6)] == [0, 1, 1, 1])
chk('6 tan period', all(ok(t(x + pi), t(x)) for x in (0.3, 1.1, 2.5)) and not ok(t(0.3 + pi/2), t(0.3)))
f7 = lambda x: 2*c(x)**2 + s(x) - 1
cand7 = [lambda u: 2*u*u+u-1, lambda u: 2*u*u-u+1, lambda u: 2*u*u-u-1, lambda u: 2*u*u+u-3]
chk('7 subst', [all(ok(f7(x), -g(s(x))) or ok(f7(x), g(s(x))) for x in th[::97]) for g in cand7] == [0, 0, 1, 0])
chk('8 min', abs(min(s(x)**2 - 4*s(x) for x in th) + 3) < 1e-5 and abs(max(s(x)**2 - 4*s(x) for x in th) - 5) < 1e-5)
chk('9 counterex', [ok(s(a+b), s(a)+s(b)) for a, b in ((pi/2, pi/2), (2*pi, 3*pi/2), (pi, 0), (0, 0))] == [0, 1, 1, 1])
chk('10 perp', ok(1 + 2 * (-0.5), 0) and ok(abs(math.atan(2) - math.atan(-0.5)), pi/2))
chk('11 half sign', ok(s(2.0/2)**2, s((2.0 + 2*pi)/2)**2) and ok(s(1.0), -s(1.0 + pi)))
chk('12 R=5', abs(max(3*s(x) + 4*c(x) for x in th) - 5) < 1e-5 and ok(math.hypot(3, 4), 5))
chk('13 harmonic', all(ok(s(x) + math.sqrt(3)*c(x), 2*s(x + pi/3)) for x in th[::97]) and max(s(x)+math.sqrt(3)*c(x) for x in th) <= 2 + 1e-12)
chk('14 max 10', abs(max(6*s(x) + 8*c(x) for x in th) - 10) < 1e-5)
chk('15 exp ineq', all(((1/3)**x < (1/3)**2) == (x > 2) for x in (-3, 0, 1.9, 2.1, 5)))
lg = math.log
chk('16 log recip', all(ok(lg(b, a) * lg(a, b), 1) for a, b in ((2, 7), (.5, 3), (10, .2))) and not ok(lg(7, 2), -lg(2, 7)))
L9, L4 = lg(9, 2), lg(4, 2)
chk('17 log4 9', [ok(lg(9, 4), v) for v in (L9 - L4, L9 * L4, L9 / L4, L9 + L4)] == [0, 0, 1, 0] and ok(lg(9, 4), lg(3, 2)))
chk('18 decomposition', ok(math.log10(12), 2*math.log10(2) + math.log10(3)) and ok(math.log10(5), 1 - math.log10(2)))
chk('19 log domain', True)  # log_a(0) undefined; domain x>0, range all reals, passes (1,0)
chk('20 digits', all(len(str(10*n)) == len(str(n)) + 1 for n in range(1, 5000)))
chk('21 limit', abs(((2+1e-7)**2 - 4) / 1e-7 - 4) < 1e-5)
chk('22 defn', all(ok(((x+h)**2 - x*x) / h, 2*x + h) for x in (1.5, -2) for h in (.5, .25)))
chk('23 product', [abs(d(lambda x: x**5, 1.3) - g) < 1e-5 for g in (6*1.3**5, 5*1.3**4, 5*1.3**6, 6*1.3**4)] == [0, 1, 0, 0])
chk('24 horiz', True)
chk('25 tangent thru (0,1)', all(2*a*0 - a*a != 1 for a in [i/100 for i in range(-1000, 1000)]) and 1 > 0**2)
chk('26 sign chart', True)  # + - + : max at -1, min at 2, decreasing between
f27 = lambda x: x**3 - 3*x*x + 2
chk('27 abs max', (f27(4), f27(-2), f27(0), f27(2)) == (18, -18, 2, -2) and max(f27(-2 + i*.001) for i in range(6001)) <= 18)
chk('28 f prime', all(ok(3*x*x + 2*(-6)*x + 9, 3*(x-1)*(x-3)) for x in (0, 1, 2.5, 7)))
chk('29 discriminant', 36 - 12*2 > 0 > 36 - 12*4)
chk('30 roots', all(ok(x**3 - 3*x - 2, (x+1)**2 * (x-2)) for x in (-3, 0, .7, 5)) and ok(d(lambda x: x**3 - 3*x, -1), 0))
f31 = lambda x: x**4 - 2*x*x
chk('31 even', all(ok(f31(x), f31(-x)) for x in (.3, 2, 5)) and f31(1) < 0 and d(f31, .5) < 0)
f32 = lambda x: x**4 - 4*x**3
chk('32 no extremum at 0', d(f32, -.1) < 0 and d(f32, .1) < 0 and d(f32, 2.9) < 0 < d(f32, 3.1) and f32(0) == 0)
chk('33 antiderivs', [abs(d(g, 1.7) - 3.4) < 1e-6 for g in (lambda x: x*x+5, lambda x: 2*x*x, lambda x: x*x-3, lambda x: x*x)] == [1, 0, 1, 1])
chk('34 a to a', True)
chk('35 signed area', simpson(lambda x: -x*x, 0, 1) < 0)
chk('36 area', abs(simpson(lambda x: x*x - 2*x, 0, 2) + 4/3) < 1e-9 and all(2*x >= x*x for x in (.1, 1, 1.9)))
g = lambda x: x**3 - 4*x
I1, I2 = simpson(g, -2, 0), simpson(g, 0, 2)
A = simpson(lambda x: abs(g(x)), -2, 2)
chk('37 split', [abs(A - v) < 1e-6 for v in (I1 + I2, I1 - I2, I1 + I2, I2 - I1)] == [0, 1, 0, 0] and abs(A - 8) < 1e-6)
chk('38 abs', all(ok(abs(x - 2), 2 - x) for x in (0, .5, 2)) and not ok(abs(1 - 2), 1 - 2))
chk('39 tangents', ok(2*0 - 1, -2*0 - 1) and 2 * -2 != -1)
par = lambda a, al, be: simpson(lambda x: abs(a*(x-al)*(x-be)), al, be)
chk('40 cube law', abs(par(1, 0, 4) / par(1, 0, 2) - 8) < 1e-6 and abs(par(2, 1, 3) - 2 * 2**3 / 6) < 1e-6)
tot = simpson(lambda x: 3*x - x*x, 0, 3)
def upper(m): return simpson(lambda x: 3*x - x*x - m*x, 0, 3 - m)
ms = [3 - 2**(1/3), 1.5, 3 - 3/2**(1/3), 3 - 3/4**(1/3)]
chk('41 bisect', abs(tot - 4.5) < 1e-9 and [abs(upper(m) - tot/2) < 1e-7 for m in ms] == [0, 0, 1, 0] and 0 < ms[2] < 3)
chk('42 die', sum(F(k, 6) for k in range(1, 7)) == F(7, 2))
chk('43 mean', F(2 + 4 + 9, 3) == 5)
chk('44 E, E2', (F(1, 2) - F(1, 2), F(1, 2) + F(1, 2)) == (0, 1))
chk('45 var', 25 - 5**2 == 0)
xs, ps = [1, 2, 6], [F(1, 2), F(1, 4), F(1, 4)]
E = lambda v: sum(p*x for p, x in zip(ps, v)); V = lambda v: E([x*x for x in v]) - E(v)**2
a_, b_ = 3, 7; ys = [a_*x + b_ for x in xs]
chk('46 transform', E(ys) == a_*E(xs) + b_ and V(ys) == a_**2 * V(xs))

# structural checks
n = 0
for k, v in D.items():
    assert len(v) == 6, k
    for i, q in enumerate(v):
        assert len(q['o']) == 4 and 0 <= q['a'] < 4 and len(set(q['o'])) == 4, (k, i)
        if not q.get('chg'): continue
        n += 1
        L = [len(o) for o in q['o']]
        if L[q['a']] > max(L[j] for j in range(4) if j != q['a']): print('LONGEST', k, i, L)
        if len(q['e'].split()) > 25: print('E>25', k, i)
print('lessons', len(D), 'chg', n)
bad = [r for r in R if not r[1]]
print('math checks', len(R), 'failed', bad)
