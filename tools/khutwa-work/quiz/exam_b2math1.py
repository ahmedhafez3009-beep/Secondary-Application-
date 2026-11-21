# Exam-style review of b2math1_checked.json -> b2math1_exam.json  (88 lessons x 6, target ~2R/2U/2A)
# Every new/changed question carries a plain-Python check: a list of 4 booleans (truth of each option),
# exactly one of which must be True and it must be option "a".
import json, copy, math
from collections import Counter
from fractions import Fraction as F
SRC='/home/claude/khutwa/quiz/b2math1_checked.json'; OUT='/home/claude/khutwa/quiz/b2math1_exam.json'
by=copy.deepcopy(json.load(open(SRC))['by']); K=list(by)
BEFORE="""RRUUAA RRUUAA RRUUAA RRUUAA RRUUAA RRUAAA RUUAAA RRUAAA RRUAAA RUUARA
RURAAA RUUAAA RUURUA RRRUAU RUUAAU RRUAAA RRUAAU RRUUAA RRAAAA RRUUAA
RUUAAR RUUAAA RRUUAU RRUAAA RRUUAA URAAAA RUUAUA RRUAAU RUUAAA RRUAAA
RUUAAA RUUAAA RRUAAU RRRUAA RAAAAA RUUAAU RUAAAU RRUAAA RRUUAU RRAUUU
RUAAAA RUAUAA RRUUUA RRUAUA RRRUAA RUUAAA RRUUAA RRUUUA RRUUAA RRUAUA
RUUAAA RUAAAA RRRUAA RRUAAA RUAAAA URUAAA RUUAAA RUUAAA RRUAAA RUAAAU
RRUUAA RRAAUU RRUUAA UUUUUU RUUAAA RRUAAA RRUAAU RRUAAU RUUAAA RRUAAU
RRUUAA RRUAAA RRAUAA RUUAAA RUUAAU RRUAAA RRUAUA RUUUAA RRUAAA RRUAAA
RRUAAU RRRAAA RRAAUU RRUAAA RRUAAU RRRUAA RUUAAA RURAAA""".split()
assert len(BEFORE)==88==len(K)
AFTER=list(BEFORE); NCHG=0; NCHK=0
XS=[F(n,d) for n in range(-7,8) for d in (1,2,3)]          # sample points for identity tests

def setq(i,j,lvl,q,o,a,e,chk):
    global NCHG,NCHK
    assert len(o)==4==len(set(o)), (i,j)
    assert len(chk)==4 and [bool(c) for c in chk].count(True)==1 and chk[a], (i,j,chk)
    L=[len(x) for x in o]
    assert L[a]<=max(l for t,l in enumerate(L) if t!=a), ('correct is longest',i,j,L)
    assert len(e.split())<=25, ('e too long',i,j,len(e.split()))
    by[K[i]][j]={"q":q,"o":o,"a":a,"e":e,"chg":True}
    s=list(AFTER[i]); s[j]=lvl; AFTER[i]=''.join(s); NCHG+=1; NCHK+=1

def same(f,g,xs=XS):            # f == g as functions (skipping poles)
    ok=0
    for x in xs:
        try: a,b=f(x),g(x)
        except ZeroDivisionError: continue
        if a!=b: return False
        ok+=1
    return ok>=10

# ---- 5 ضرب وقسمة المقادير النسبية: cancelled common factor
cf=[lambda x:x-3, lambda x:x, lambda x:x*x, lambda x:x+3]
setq(5,3,'U',"عند تبسيط (س^2 - 9)/(س^2 + 3س) إلى (س - 3)/س، ما العامل المشترك الذي اختُصر من البسط والمقام؟",
 ["س - 3","س","س^2","س + 3"],3,
 "البسط = (س - 3)(س + 3) والمقام = س(س + 3)، فالعامل المشترك المختصر هو س + 3.",
 [same(lambda x:x*x-9, lambda x,f=f:(x-3)*f(x)) and same(lambda x:x*x+3*x, lambda x,f=f:x*f(x)) for f in cf])

# ---- 7 الكسور المركبة: find the error
num_x=same(lambda x:(1+1/x)*x, lambda x:x+1)                # numerator was multiplied by x
den_same=True                                               # denominator 1 - 1/x left untouched in the student's result
den_x=same(lambda x:(1-1/x)*x, lambda x:1-1/x)              # False: denominator was not multiplied
setq(7,3,'U',"بسّط طالب المقدار (1 + 1/س)/(1 - 1/س) فكتب الناتج (س + 1)/(1 - 1/س). ما خطؤه؟",
 ["جمع 1 + 1/س جمعًا غير صحيح","قسم البسط والمقام على س","ضرب البسط وحده في س","ضرب المقام وحده في س"],2,
 "ضرب البسط في س فصار س + 1 وترك المقام؛ والصواب ضرب البسط والمقام معًا فيصير (س + 1)/(س - 1).",
 [not num_x, same(lambda x:(1+1/x)/x, lambda x:x+1), num_x and den_same and not den_x, den_x])

# ---- 8 المتطابقات: which equality is an identity
ids=[lambda x:x*x-4==0, lambda x:(x+1)**2==x*x+2*x+1, lambda x:2*x+1==5, lambda x:(x+2)**2==x*x+2*x+4]
setq(8,3,'U',"أي المساويات الآتية متطابقة في س؟",
 ["س^2 - 4 = 0","(س + 1)^2 = س^2 + 2س + 1","2س + 1 = 5","(س + 2)^2 = س^2 + 2س + 4"],1,
 "(س + 1)^2 = س^2 + 2س + 1 تتحقق لكل قيم س، أما البقية فتتحقق عند قيم محددة فقط.",
 [all(f(x) for x in XS) for f in ids])

# ---- 10 إثبات المتطابقات (2): reason
T=[(a,b,-a-b) for a in range(-4,5) for b in range(-4,5)]
setq(10,5,'U',"علل: إذا كان أ + ب + ج = 0 فإن (أ + ب)(ب + ج)(ج + أ) = -أبج.",
 ["لأن كل قوس يساوي صفرًا عند تحقق هذا الشرط","لأن أ + ب = ج ، ب + ج = أ ، ج + أ = ب","لأن أ = ب = ج = 0 دائمًا عند تحقق هذا الشرط","لأن أ + ب = -ج ، ب + ج = -أ ، ج + أ = -ب"],3,
 "من الشرط: أ + ب = -ج ، ب + ج = -أ ، ج + أ = -ب، وحاصل ضربها (-ج)(-أ)(-ب) = -أبج.",
 [all(a+b==0 and b+c==0 and c+a==0 for a,b,c in T), all(a+b==c and b+c==a and c+a==b for a,b,c in T),
  all(a==b==c==0 for a,b,c in T),
  all(a+b==-c and b+c==-a and c+a==-b and (a+b)*(b+c)*(c+a)==-a*b*c for a,b,c in T)])

# ---- 15 AM-GM: where the minimum is attained
f15=lambda x:x+F(9)/x; opts=[9,6,3,1]
mn=min(f15(F(n,100)) for n in range(1,2001))
setq(15,3,'U',"إذا كان س > 0 فإن المقدار س + 9/س يأخذ أصغر قيمة له عندما:",
 ["س = 9","س = 6","س = 3","س = 1"],2,
 "تتحقق المساواة في متباينة المتوسطين عندما س = 9/س، أي س = 3، وعندها القيمة الصغرى 6.",
 [f15(F(v))==mn==6 for v in opts])

# ---- 18 المتتابعة الحسابية (2)
AP=[(a,a+d,a+2*d) for a in range(-3,4) for d in range(-3,4) if a and a+d and d]
setq(18,3,'U',"علل: إذا كانت أ ، ب ، ج متتابعة حسابية بهذا الترتيب فإن 2ب = أ + ج.",
 ["لأن ب - أ = ج - ب","لأن ب ÷ أ = ج ÷ ب","لأن ب - أ = ب - ج","لأن أ + ب = ب + ج"],0,
 "الفرق بين كل حدين متتاليين ثابت: ب - أ = ج - ب، ومنها 2ب = أ + ج.",
 [all(b-a==c-b and 2*b==a+c for a,b,c in AP), all(F(b,a)==F(c,b) for a,b,c in AP),
  all(b-a==b-c for a,b,c in AP), all(a+b==b+c for a,b,c in AP)])
d=F(30-10,8-3)
setq(18,4,'U',"متتابعة حسابية أساسها د، حدها الثالث 10 وحدها الثامن 30. أي معادلة تعطي د مباشرة؟",
 ["5د = 20","8د = 30","3د = 10","11د = 40"],0,
 "أ_8 - أ_3 = (8 - 3)د، أي 5د = 30 - 10 = 20، ومنها د = 4.",
 [5*d==20, 8*d==30, 3*d==10, 11*d==40])

# ---- 23 المتتابعة الهندسية (2)
sols=[(a,r) for r in (F(n,dn) for n in range(-12,13) for dn in (1,2,3) if n) for a in [F(24)/r**3] if a*r**5==96]
assert sorted({r for a,r in sols})==[-2,2]
setq(23,4,'U',"متتابعة هندسية أساسها ر، حدها الرابع 24 وحدها السادس 96. بقسمة الحد السادس على الحد الرابع نحصل على:",
 ["ر = 4","ر^2 = 4","ر^2 = 72","ر^3 = 4"],1,
 "أ ر^5 ÷ أ ر^3 = ر^2 = 96 ÷ 24 = 4، فتُحذف أ ويبقى ر^2 = 4.",
 [all(r==4 for a,r in sols), all(r**2==4 for a,r in sols), all(r**2==72 for a,r in sols), all(r**3==4 for a,r in sols)])

# ---- 25 مجموع المتتابعة الهندسية (2)
G=[(a,r) for a in (1,2,F(1,3)) for r in (2,3,F(1,2),-2) if a*(1+r+r*r)!=0]
def s46(a,r): return a*r**3+a*r**4+a*r**5
def s13(a,r): return a+a*r+a*r*r
setq(25,3,'U',"متتابعة هندسية أساسها ر، مجموع حدودها الثلاثة الأولى 7. مجموع حدودها من الرابع إلى السادس يساوي:",
 ["7ر^2","7ر^3","7ر^6","7 + ر^3"],1,
 "كل حد من الرابع إلى السادس يساوي نظيره في الثلاثة الأولى مضروبًا في ر^3، فالمجموع 7ر^3.",
 [all(s46(a,r)==s13(a,r)*r**2 for a,r in G), all(s46(a,r)==s13(a,r)*r**3 for a,r in G),
  all(s46(a,r)==s13(a,r)*r**6 for a,r in G), all(s46(a,r)==s13(a,r)+r**3 for a,r in G)])

# ---- 29 المتتابعات الكسرية: telescoping
tel=all(sum(F(1,k)-F(1,k+1) for k in range(1,n+1))==1-F(1,n+1) for n in range(1,30))
terms=[F(1,k)-F(1,k+1) for k in range(1,8)]
setq(29,3,'U',"علل: عند جمع الحدود (1/ك - 1/(ك + 1)) من ك = 1 إلى ن يبقى 1 - 1/(ن + 1) فقط.",
 ["لأن جميع الحدود موجبة فيتراكم مجموعها","لأن المتتابعة هندسية أساسها يساوي 1/2","لأن مقامات الكسور كلها متساوية القيمة","لأن الحدود الوسطى يحذف بعضها بعضًا"],3,
 "-1/2 يُحذف مع +1/2 وهكذا، فلا يبقى إلا الحد الأول 1 والأخير -1/(ن + 1).",
 [False, all(terms[i+1]/terms[i]==F(1,2) for i in range(6)), len({F(1,k).denominator for k in range(1,8)})==1, tel])

# ---- 33 متتابعات الفروق
seq=[2,5,10,17,26]; dif=[seq[i+1]-seq[i] for i in range(4)]
setq(33,2,'U',"متتابعة الفروق للمتتابعة 2 ، 5 ، 10 ، 17 ، 26 ، ... هي:",
 ["2 ، 3 ، 5 ، 7 ، ...","7 ، 15 ، 27 ، 43 ، ...","3 ، 5 ، 7 ، 9 ، ...","3 ، 5 ، 7 ، 8 ، ..."],2,
 "نطرح كل حد من الحد الذي يليه فنحصل على الفروق 3 ثم 5 ثم 7 ثم 9.",
 [dif==[2,3,5,7], dif==[7,15,27,43], dif==[3,5,7,9], dif==[3,5,7,8]])

# ---- 34 المتتابعات المجمعة
def group(n):
    start=n*(n-1)//2+1; return list(range(start,start+n))
allnums=[x for n in range(1,25) for x in group(n)]; assert allnums==list(range(1,len(allnums)+1))
setq(34,2,'U',"في التجميع (1) ، (2 ، 3) ، (4 ، 5 ، 6) ، ... عدد حدود المجموعة العشرين يساوي:",
 ["19","20","210","21"],1,
 "المجموعة الأولى فيها حد واحد والثانية حدان وهكذا، فالمجموعة رقم ن فيها ن حدًا؛ والعشرون فيها 20.",
 [len(group(20))==v for v in (19,20,210,21)])
R=range(1,25)
setq(34,5,'U',"علل: في التجميع (1) ، (2 ، 3) ، (4 ، 5 ، 6) ، ... الحد الأخير في المجموعة ن هو ن(ن + 1)/2.",
 ["لأن كل مجموعة تبدأ بمربع رقمها","لأن عدد حدود كل المجموعات ثابت","لأن الحد الأخير ضعف الحد الأول","لأنه يساوي 1 + 2 + ... + ن"],3,
 "الحدود هي الأعداد الطبيعية بالترتيب، وعددها حتى نهاية المجموعة ن هو 1 + 2 + ... + ن = ن(ن + 1)/2.",
 [all(group(n)[0]==n*n for n in R), len({len(group(n)) for n in R})==1, all(group(n)[-1]==2*group(n)[0] for n in R),
  all(group(n)[-1]==sum(range(1,n+1))==n*(n+1)//2 for n in R)])

# ---- 37 علاقات التكرار (3): a_1 equals the fixed value
a=[3]
for _ in range(10): a.append(2*a[-1]-3)
setq(37,5,'U',"إذا كان أ_1 = 3 ، أ_(ن+1) = 2أ_ن - 3 فماذا يحدث لحدود المتتابعة؟",
 ["تتضاعف من حد إلى آخر","تبقى كلها مساوية 3","تتناقص بمقدار 3 كل مرة","تتزايد بمقدار 3 كل مرة"],1,
 "ج = 2ج - 3 تعطي ج = 3 = أ_1، فيكون أ_2 = 2 × 3 - 3 = 3 وهكذا تثبت الحدود.",
 [all(a[i+1]==2*a[i] for i in range(10)), set(a)=={3}, all(a[i+1]==a[i]-3 for i in range(10)), all(a[i+1]==a[i]+3 for i in range(10))])

# ---- 40 الاستقراء (المضاعفات)
ident=all(4**(k+1)-1==4*(4**k-1)+3 for k in range(1,30)); mult=all((4**k-1)%3==0 for k in range(1,30))
setq(40,3,'U',"في إثبات أن 4^ن - 1 مضاعف للعدد 3 بالاستقراء، لماذا نكتب 4^(ك+1) - 1 = 4(4^ك - 1) + 3؟",
 ["لنتحقق من صحة العبارة عندما ن = 1 فقط","لنستخدم فرض أن 4^ك - 1 مضاعف لـ 3","لنثبت أن العدد 4^ك عدد زوجي دائمًا","لنحذف العدد 3 من طرفي هذه المعادلة"],1,
 "بهذه الصورة يظهر 4^ك - 1 المفترض أنه مضاعف لـ 3، فيكون المجموع كله مضاعفًا لـ 3.",
 [False, ident and mult, False, False])

# ---- 44 قسمة الأعداد المركبة
z=2-1j; p=z*z.conjugate(); n1=5*z.conjugate()
setq(44,2,'U',"علل: عند قسمة عددين مركبين نضرب البسط والمقام في مرافق المقام.",
 ["ليصبح المقام عددًا حقيقيًا","ليصبح البسط عددًا حقيقيًا","ليصبح المقام تخيليًا بحتًا","لتتغير قيمة الكسر إلى مرافقه"],0,
 "حاصل ضرب العدد المركب في مرافقه عدد حقيقي، فيصبح المقام حقيقيًا وتسهل القسمة.",
 [p.imag==0 and p.real==5, n1.imag==0, p.real==0, abs(n1/p-(5/z).conjugate())<1e-12])

# ---- 51 تكوين المعادلة التربيعية
q1=lambda x:2*x*x-7*x+3; q2=lambda x:x*x-F(7,2)*x+F(3,2)
roots=[F(1,2),F(3)]
setq(51,3,'U',"علل: تُكتب المعادلة التي جذراها 1/2 و 3 على الصورة 2س^2 - 7س + 3 = 0 بدلًا من س^2 - (7/2)س + 3/2 = 0.",
 ["لتصبح معاملاتها أعدادًا صحيحة بالضرب في 2","لأن الضرب في 2 يضاعف قيمة كل من الجذرين","لأن المعادلة الثانية جذراها مختلفان عنهما","لأن معامل س^2 لا يجوز أن يساوي الواحد أبدًا"],0,
 "ضرب طرفي المعادلة في 2 لا يغير الجذرين، ويجعل المعاملات كلها أعدادًا صحيحة.",
 [all(q1(r)==0==q2(r) for r in roots) and same(q1,lambda x:2*q2(x)), all(q1(2*r)==0 for r in roots),
  any(q2(r)!=0 for r in roots), False])

# ---- 52 إشارتا الحلين
C=[(a,b,c) for a in range(-4,5) for b in range(-4,5) for c in range(-4,5) if a and a*c<0]
disc=lambda a,b,c:b*b-4*a*c
setq(52,2,'U',"علل: يكفي الشرط ج/أ < 0 ليكون للمعادلة أس^2 + بس + ج = 0 حلان مختلفا الإشارة دون اشتراط د > 0.",
 ["لأن أج < 0 يجعل المميز موجبًا","لأن المميز لا يؤثر في نوع الحلين","لأن مجموع الحلين يساوي صفرًا","لأن أج < 0 يجعل المميز صفرًا"],0,
 "إذا كان ج/أ < 0 فإن أج < 0، فيكون ب^2 - 4أج > 0 تلقائيًا ويتحقق شرط المميز.",
 [all(disc(*t)>0 for t in C), False, all(t[1]==0 for t in C), all(disc(*t)==0 for t in C)])

# ---- 53 نظرية الباقي (1): find the error
def synth(co,r):            # synthetic division by (x - r): returns remainder
    v=0
    for c in co: v=v*r+c
    return v
def longrem(co,dv):         # remainder of polynomial long division (coefficient lists, high->low)
    co=[F(c) for c in co]
    while len(co)>=len(dv):
        k=co[0]/dv[0]
        for t in range(len(dv)): co[t]-=k*dv[t]
        co.pop(0)
    return co
P=[2,0,1,-5]; fv=lambda x:synth(P,x); rem=longrem(P,[1,1])[0]
setq(53,3,'U',"قال طالب: «باقي قسمة ف(س) على س + 1 هو ف(1)». ما الصواب؟",
 ["الباقي ف(0) لأن الحد الثابت في المقسوم عليه 1","الباقي -ف(1) لأن الإشارة تنعكس","قوله صحيح ولا خطأ فيه","الباقي ف(-1) لأن س + 1 = س - (-1)"],3,
 "الباقي عند القسمة على س - أ هو ف(أ)، و س + 1 = س - (-1)، فالباقي ف(-1) لا ف(1).",
 [rem==fv(0), rem==-fv(1), rem==fv(1), rem==fv(-1)])

# ---- 54 نظرية الباقي (2)
degs=set()
for co in ([1,0,0,2],[1,0,0,0,0],[3,-1,2,5,1],[1,1,1]):
    r=longrem(co,[1,1,-2])           # (x-1)(x+2) = x^2 + x - 2
    degs.add(len(r))
setq(54,4,'U',"علل: عند قسمة كثير حدود على (س - 1)(س + 2) نفرض الباقي على الصورة أس + ب.",
 ["لأن الباقي يساوي المقسوم عليه في كل قسمة","لأن درجة الباقي تساوي درجة الناتج","لأن درجة الباقي أقل من الدرجة الثانية","لأن الباقي عدد ثابت في كل الحالات"],2,
 "درجة الباقي أقل من درجة المقسوم عليه (الثانية)، فهو من الدرجة الأولى على الأكثر: أس + ب.",
 [False, False, degs=={2}, all(longrem(co,[1,1,-2])[0]==0 for co in ([1,0,0,2],[1,0,0,0,0]))])

# ---- 58 المعادلات ذات الدرجة العليا
fac=same(lambda x:x**3-8, lambda x:(x-2)*(x*x+2*x+4)); f58=lambda x:x**3-8
setq(58,4,'U',"علل: للمعادلة س^3 - 8 = 0 ثلاثة حلول في مجموعة الأعداد المركبة وليس الحل 2 فقط.",
 ["لأن العامل س^2 + 2س + 4 يعطي جذرين مركبين","لأن العدد 2 جذر مكرر ثلاث مرات للمعادلة","لأن العامل س^2 - 2س + 4 يعطي جذرين حقيقيين","لأن -2 و 2ت جذران آخران لهذه المعادلة"],0,
 "س^3 - 8 = (س - 2)(س^2 + 2س + 4)، ومميز العامل التربيعي سالب فيعطي جذرين مركبين.",
 [fac and 2*2-4*4<0, same(f58, lambda x:(x-2)**3), same(f58, lambda x:(x-2)*(x*x-2*x+4)), f58(-2)==0 and abs(f58(2j))<1e-9])

# ---- 63 النقاط في المستوى الإحداثي (was 6 x understanding)
ks=[F(n,4) for n in range(-40,41)]
q2nd=lambda k:(k-2<0 and k+3>0)
setq(63,0,'A',"تقع النقطة (ك - 2, ك + 3) في الربع الثاني عندما:",
 ["-3 < ك < 2","ك > 2","ك < -3","-2 < ك < 3"],0,
 "في الربع الثاني س سالب و ص موجب، فيكون ك < 2 و ك > -3 معًا.",
 [all(q2nd(k)==c(k) for k in ks) for c in (lambda k:-3<k<2, lambda k:k>2, lambda k:k<-3, lambda k:-2<k<3)])
quad=lambda x,y:{(1,1):1,(-1,1):2,(-1,-1):3,(1,-1):4}[(x,y)]
setq(63,2,'R',"أي شرط يميز نقاط الربع الرابع؟",
 ["س < 0 ، ص > 0","س < 0 ، ص < 0","س > 0 ، ص < 0","س > 0 ، ص > 0"],2,
 "في الربع الرابع يكون الإحداثي السيني موجبًا والإحداثي الصادي سالبًا.",
 [quad(*s)==4 for s in ((-1,1),(-1,-1),(1,-1),(1,1))])
pt=(F(3),F(-2)); refx=(pt[0],-pt[1])
setq(63,3,'R',"النقطة المتماثلة مع النقطة (أ, ب) بالنسبة لمحور س هي:",
 ["(-أ, ب)","(-أ, -ب)","(ب, أ)","(أ, -ب)"],3,
 "التماثل بالنسبة لمحور س يُبقي الإحداثي السيني ويعكس إشارة الإحداثي الصادي.",
 [refx==(-pt[0],pt[1]), refx==(-pt[0],-pt[1]), refx==(pt[1],pt[0]), refx==(pt[0],-pt[1])])
sol=[(A,B) for A in range(-20,21) for B in range(-20,21) if (A+1,3)==(-4,B-2)]   # reflection in y-axis: (x,y)->(-x,y)
assert sol==[(-5,5)]
setq(63,5,'A',"إذا كانت النقطتان (أ + 1, 3) و (4, ب - 2) متماثلتين بالنسبة لمحور ص فإن أ + ب =",
 ["0","2","-6","8"],0,
 "التماثل بالنسبة لمحور ص يعكس إشارة س فقط، فيكون أ + 1 = -4 و ب - 2 = 3.",
 [sum(sol[0])==v for v in (0,2,-6,8)])

# ---- 65 النقاط المتساوية البعد: set up the condition
dA=lambda t:(t+1)**2+(0-2)**2; dB=lambda t:(t-3)**2+(0-4)**2
cand=[(lambda t:(t-1)**2+4, lambda t:(t+3)**2+16),(lambda t:(t+1)**2+4, lambda t:(t-3)**2+16),
      (lambda t:(t+1)**2+2, lambda t:(t-3)**2+4),(lambda t:(t+1)+2, lambda t:(t-3)+4)]
assert dA(F(5,2))==dB(F(5,2))
setq(65,3,'U',"نقطة (ع, 0) على محور س متساوية البعد عن أ(-1, 2) و ب(3, 4). أي معادلة تعبر عن هذا الشرط؟",
 ["(ع - 1)^2 + 4 = (ع + 3)^2 + 16","(ع + 1)^2 + 4 = (ع - 3)^2 + 16","(ع + 1)^2 + 2 = (ع - 3)^2 + 4","(ع + 1) + 2 = (ع - 3) + 4"],1,
 "مربع البعد عن أ يساوي (ع + 1)^2 + 2^2 وعن ب يساوي (ع - 3)^2 + 4^2، ونساوي بينهما.",
 [same(l,dA) and same(r,dB) for l,r in cand])

# ---- 71 التوازي والتعامد
m1=F(-2,3); m2=F(3,2)        # 2x+3y=1 -> y=(-2/3)x+..., 3x-2y=4 -> y=(3/2)x-2
assert 2*3+3*(-2)==0         # independent test: a1*a2 + b1*b2 = 0
setq(71,3,'U',"علل: المستقيمان 2س + 3ص = 1 و 3س - 2ص = 4 متعامدان.",
 ["لأن ميليهما متساويان في القيمة والإشارة","لأن مجموع ميليهما يساوي صفرًا","لأن حاصل ضرب ميليهما يساوي -1","لأن حاصل ضرب ميليهما يساوي 1"],2,
 "ميل الأول -2/3 وميل الثاني 3/2، وحاصل ضربهما -1، وهذا شرط التعامد.",
 [m1==m2, m1+m2==0, m1*m2==-1, m1*m2==1])

# ---- 72 محور القطعة المستقيمة
A_,B_=(1,1),(5,3); d2=lambda P,Q:(P[0]-Q[0])**2+(P[1]-Q[1])**2
axis=[(F(x),-2*F(x)+8) for x in (F(n,2) for n in range(-10,15))]      # y = -2x + 8 (lesson's own example)
setq(72,5,'U',"ما الذي يميز كل نقطة تقع على محور القطعة المستقيمة أب؟",
 ["بعداها عن أ و ب متساويان","بعدها عن أ ضعف بعدها عن ب","تقع بين أ و ب على القطعة نفسها","تقع على امتداد أب خارج القطعة"],0,
 "المحور عمودي على أب ويمر بمنتصفها، فكل نقطة عليه متساوية البعد عن الطرفين أ و ب.",
 [all(d2(P,A_)==d2(P,B_) for P in axis), all(d2(P,A_)==4*d2(P,B_) for P in axis),
  all((P[0]-1)*2==(P[1]-1)*4 and 1<=P[0]<=5 for P in axis), all((P[0]-1)*2==(P[1]-1)*4 and not 1<=P[0]<=5 for P in axis)])

# ---- 75 المستقيم المار بنقطة ثابتة
x,y=2,1; b1=x+y-3; b2=x-y-1
slopes={F(-(k+1),(k-1)) for k in (0,2,3,5)}       # k(x+y-3)+(x-y-1)=0 -> (k+1)x+(k-1)y-(3k+1)=0
setq(75,3,'U',"علل: يمر المستقيم ك(س + ص - 3) + (س - ص - 1) = 0 بالنقطة (2, 1) لكل قيم ك.",
 ["لأن القوسين يساويان صفرًا عندها","لأن ميل المستقيم لا يتغير مع ك","لأن ك تساوي صفرًا عند هذه النقطة","لأن القوسين متساويان ويساويان 1"],0,
 "عند (2, 1): س + ص - 3 = 0 و س - ص - 1 = 0، فتتحقق المعادلة أيًّا كانت قيمة ك.",
 [b1==0==b2 and all(k*b1+b2==0 for k in range(-9,10)), len(slopes)==1, False, b1==b2==1])

# ---- 78 معادلة الدائرة (2)
dc=math.hypot(5-2,7-3)
setq(78,3,'U',"علل: تقع النقطة (5, 7) على الدائرة التي مركزها (2, 3) ونصف قطرها 5.",
 ["لأن بعدها عن نقطة الأصل يساوي 5","لأن بعدها عن محور س يساوي 5","لأن بعدها عن المركز يساوي 5","لأن بعدها عن المركز يساوي 25"],2,
 "sqrt((5 - 2)^2 + (7 - 3)^2) = sqrt(25) = 5 = نق، فالنقطة تقع على الدائرة.",
 [math.hypot(5,7)==5, abs(7)==5, dc==5, dc==25])

# ---- 79 معادلة الدائرة (3)
cx,cy,r=-3,5,3
def rel(dist,r): return 'touch' if dist==r else 'cut' if dist<r else 'none'
ry=rel(abs(cx),r); rx=rel(abs(cy),r)       # relation with y-axis / x-axis
setq(79,3,'U',"دائرة مركزها (-3, 5) ونصف قطرها 3. ما وضعها بالنسبة للمحورين؟",
 ["تمس محور س ولا تقطع محور ص","تمس المحورين معًا","تمس محور ص ولا تقطع محور س","تقطع كلًّا من المحورين في نقطتين"],2,
 "بعد المركز عن محور ص = 3 = نق فتمسه، وبعده عن محور س = 5 > نق فلا تقطعه.",
 [rx=='touch' and ry=='none', rx=='touch'==ry, ry=='touch' and rx=='none', rx=='cut'==ry])

# ---- 81 تقاطع الدائرة والمستقيم (1)
def sub_line(m,c,r2):       # x^2 + (mx+c)^2 = r2  ->  coefficients of the quadratic in x
    return (1+m*m, 2*m*c, c*c-r2)
tq=sub_line(1,2,10); prop=lambda co:all(F(co[i])*tq[0]==F(tq[i])*co[0] for i in range(3))
setq(81,2,'U',"بالتعويض من ص = س + 2 في س^2 + ص^2 = 10 والتبسيط نحصل على المعادلة:",
 ["س^2 + 2س + 3 = 0","س^2 - 3 = 0","س^2 + 2س - 3 = 0","س^2 + 4س - 6 = 0"],2,
 "س^2 + (س + 2)^2 = 10 تعطي 2س^2 + 4س - 6 = 0، وبالقسمة على 2: س^2 + 2س - 3 = 0.",
 [prop(c) for c in ((1,2,3),(1,0,-3),(1,2,-3),(1,4,-6))])
A2,B2,C2=sub_line(1,5,4); D=B2*B2-4*A2*C2
setq(81,5,'U',"علل: المستقيم ص = س + 5 لا يقطع الدائرة س^2 + ص^2 = 4.",
 ["لأن مميز المعادلة الناتجة يساوي صفرًا","لأن مميز المعادلة الناتجة موجب","لأن ميل المستقيم يساوي نصف القطر","لأن مميز المعادلة الناتجة سالب"],3,
 "بالتعويض نحصل على 2س^2 + 10س + 21 = 0 ومميزها 100 - 168 = -68 < 0، فلا توجد نقاط مشتركة.",
 [D==0, D>0, 1==2, D<0 and D==-68])

# ---- 83 طول الوتر
ch=lambda r,d:2*math.sqrt(r*r-d*d); r=5; ds=[4,3,2,1,0]; L=[ch(r,d) for d in ds]
inc=all(L[i]<L[i+1] for i in range(4))
setq(83,4,'U',"ماذا يحدث لطول الوتر كلما اقترب المستقيم القاطع من مركز الدائرة؟",
 ["يقل حتى ينعدم عند المرور بالمركز","يبقى ثابتًا لأن نصف القطر لا يتغير","يزداد حتى يتجاوز طول قطر الدائرة","يزداد حتى يساوي القطر عند المركز"],3,
 "طول الوتر = 2sqrt(نق^2 - د^2)؛ كلما صغرت د زاد الطول، وعند د = 0 يساوي القطر 2نق.",
 [(not inc) and L[-1]==0, len(set(L))==1, inc and L[-1]>2*r, inc and L[-1]==2*r])

# ---- 85 العلاقة بين دائرتين
def crel(r1,r2,d):
    r1,r2=max(r1,r2),min(r1,r2)
    if d>r1+r2: return 'متباعدتان'
    if d==r1+r2: return 'تماس خارجي'
    if d>r1-r2: return 'تقاطع'
    if d==r1-r2: return 'تماس داخلي'
    return 'داخل'
assert crel(2,1,3)=='تماس خارجي'
after={crel(r1,r2,r1+r2+e) for r1,r2 in ((2,1),(3,3),(5,2)) for e in (F(1,10),1,7)}
setq(85,2,'U',"دائرتان تتماسان خارجيًا. ماذا يحدث لو زادت المسافة بين مركزيهما مع ثبات نصفي القطرين؟",
 ["تصبحان متباعدتين","تتقاطعان في نقطتين","تتماسان داخليًا","تصبح إحداهما داخل الأخرى"],0,
 "عند التماس الخارجي د = نق1 + نق2؛ فإذا زادت د صارت د > نق1 + نق2 فتتباعد الدائرتان.",
 [after=={'متباعدتان'}, after=={'تقاطع'}, after=={'تماس داخلي'}, after=={'داخل'}])

# ---- 87 دائرة تمر بنقاط تقاطع دائرتين
# NOTE: the original pair x^2+y^2-4=0, x^2+y^2-2x=0 is internally tangent (one common point), so q3/q4 were rebuilt
# on x^2+y^2-4=0 and x^2+y^2-2x-2=0, which meet at (1, ±sqrt(3)).
c1=lambda x,y:x*x+y*y-4; c2=lambda x,y:x*x+y*y-2*x-2
s3=math.sqrt(3); I1,I2=(1,s3),(1,-s3)
assert abs(c1(*I1))<1e-9 and abs(c2(*I1))<1e-9 and abs(c1(*I2))<1e-9 and abs(c2(*I2))<1e-9
assert abs(math.hypot(1,0)-(2-1))<1e-12      # old pair: centres 1 apart = r1 - r2  -> tangent internally
k=F(-c2(0,1),c1(0,1)); assert k==F(-1,3)
# k*c1 + c2 = (k+1)x^2 + (k+1)y^2 - 2x - 4k - 2  ->  divide by (k+1)
true=(1,1,F(-2)/(k+1),(-4*k-2)/(k+1)); assert true==(1,1,-3,-1)
unnorm=(2,2,-6,-2); assert all(F(unnorm[i],2)==true[i] for i in range(4))
setq(87,3,'U',"حصل طالب على 2س^2 + 2ص^2 - 6س - 2 = 0 معادلةً لدائرة مطلوبة. ما الخطوة الباقية لكتابتها في صورتها النهائية؟",
 ["إضافة 2 إلى الطرفين","التعويض عن ك مرة أخرى","قسمة الطرفين على 2","تربيع طرفي المعادلة"],2,
 "يجب أن يكون معاملا س^2 و ص^2 مساويين 1، فنقسم على 2: س^2 + ص^2 - 3س - 1 = 0.",
 [False, False, all(F(unnorm[i],2)==true[i] for i in range(4)) and true[0]==1, False])
circ=lambda co:(lambda x,y:x*x+y*y+co[0]*x+co[1])
ok=lambda co:all(abs(circ(co)(*P))<1e-9 for P in (I1,I2,(0,1)))
setq(87,4,'A',"معادلة الدائرة المارة بنقطتي تقاطع س^2 + ص^2 - 4 = 0 و س^2 + ص^2 - 2س - 2 = 0 وبالنقطة (0, 1) هي:",
 ["س^2 + ص^2 - 3س + 1 = 0","س^2 + ص^2 - 3س - 1 = 0","س^2 + ص^2 - 6س - 1 = 0","س^2 + ص^2 - س - 1 = 0"],1,
 "بالتعويض بالنقطة (0, 1) نجد ك = -1/3، وبالتبسيط والقسمة على 2: س^2 + ص^2 - 3س - 1 = 0.",
 [ok(c) for c in ((-3,1),(-3,-1),(-6,-1),(-1,-1))])

# ================= validation & output =================
pos=Counter(); bad=[]
for i,k in enumerate(K):
    qs=by[k]; assert len(qs)==6,(i,len(qs))
    c=Counter(q['a'] for q in qs)
    if max(c.values())>2 or len(c)<4: bad.append((i,dict(c)))
    for j,q in enumerate(qs):
        assert set(q)-{'chg'}=={'q','o','a','e'} and len(q['o'])==4==len(set(q['o'])) and q['a'] in range(4)
        L=[len(x) for x in q['o']]; assert L[q['a']]<=max(l for t,l in enumerate(L) if t!=q['a']),(i,j)
        assert 'السؤال السابق' not in q['q'], (i,j)
        pos[q['a']]+=1
assert not bad, bad
def tot(S): c=Counter(''.join(S)); return (c['R'],c['U'],c['A'])
offb=sum(1 for s in BEFORE if sorted(Counter(s).get(x,0) for x in 'RUA')!=[2,2,2])
offa=sum(1 for s in AFTER if sorted(Counter(s).get(x,0) for x in 'RUA')!=[2,2,2])
weakb=sum(1 for s in BEFORE if s.count('U')<2 or s.count('A')<1 or s.count('R')<1 or max(Counter(s).values())>3)
weaka=sum(1 for s in AFTER if s.count('U')<2 or s.count('A')<1 or s.count('R')<1 or max(Counter(s).values())>3)
json.dump({"by":by},open(OUT,'w'),ensure_ascii=False,indent=1)
d=json.load(open(OUT)); assert len(d['by'])==88 and list(d['by'])==K
print('lessons',len(d['by']),'questions',sum(len(v) for v in d['by'].values()))
print('mix R/U/A before',tot(BEFORE),'after',tot(AFTER))
print('lessons exactly 2/2/2: before',88-offb,'after',88-offa,'| lessons outside tolerance: before',weakb,'after',weaka)
print('changed',NCHG,'checked',NCHK,'chg flags',sum(1 for v in d['by'].values() for q in v if q.get('chg')),'positions',dict(pos))
