# Exam-style review of b2math2_checked.json -> b2math2_exam.json  (89 lessons x 6, target ~2R/2U/2A)
# Every new/changed question carries a plain-Python check: 4 booleans (truth of each option),
# exactly one True and it must be option "a". No sympy: calculus/trig/logs are checked numerically.
import json, copy, math
from collections import Counter
from fractions import Fraction as F
SRC='/home/claude/khutwa/quiz/b2math2_checked.json'; OUT='/home/claude/khutwa/quiz/b2math2_exam.json'
by=copy.deepcopy(json.load(open(SRC))['by']); K=list(by)
BEFORE="""RRUUAA RRUUAA RRUAAA RUAAAA RUUAAA URUAAA RRUUAA RRRUAA RRRRUU UURARA
RRUUAA URUAAA RRAAAA RUUAAA RUAAAA RUUAAA RUAAAA RRUAAA RRUAAA RUUAAA
RRUAAA URUAAA RRUAAA RUAAAA RUAAAA RRUUAA RUUAAA RUUAAA UUURAA RRRUUA
RRRAUU RUAAAA RUUAAA RUUAAA RRRUUA URRUAA RUUAAA RURAAA RUAAAA UUAAAA
RRRRUA RRUUAA RUUAAA RUUAAA URUAAA RUUAAA RRUAAA RUUAAA RRUAAA RUUAAA
RRUAAA RURAAA RUUAAA RRAUAA RUAAAA RRUAAA RUAAAA RUAAAA RRUAAA RUUAAA
RUUAAA RUAAAA URUAAA RRAAAA RURAAA RUUAAA RUUAAA RRUAAA RRUUAA URAAAU
RUUAAA RRUAAA RUAAAA RUAAAA RURAAA RUAAAA RUAAAA RRUUAA RRRAAA RRUAAA
RRUAAA RUUAAA RRUAAU UUAAAA RUUAAA RUUAAA RURUAA RUAUAA RRRUUA""".split()
assert len(BEFORE)==89==len(K)
AFTER=list(BEFORE); NCHG=0
pi=math.pi; sin=math.sin; cos=math.cos; tan=math.tan; sq=math.sqrt
def eq(a,b,t=1e-9): return abs(a-b)<t
TH=[0.1+0.37*k for k in range(-9,18)]                       # sample angles
XS=[-3,-2.5,-1.3,-0.7,0.4,1.1,1.9,2.6,3.4]                  # sample reals
def simpson(f,a,b,n=2000):
    h=(b-a)/n; return h/3*(f(a)+f(b)+4*sum(f(a+(2*k-1)*h) for k in range(1,n//2+1))+2*sum(f(a+2*k*h) for k in range(1,n//2)))
def dnum(f,x,h=1e-5): return (f(x+h)-f(x-h))/(2*h)

def setq(i,name,j,lvl,q,o,a,e,chk):
    global NCHG
    assert name in K[i], (i,K[i])
    assert len(o)==4==len(set(o)), (i,j)
    chk=[bool(c) for c in chk]
    assert len(chk)==4 and chk.count(True)==1 and chk[a], (i,j,chk)
    L=[len(x) for x in o]
    assert L[a]<=max(l for t,l in enumerate(L) if t!=a), ('correct is longest',i,j,L)
    assert len(e.split())<=25, ('e too long',i,j,len(e.split()))
    assert by[K[i]][j]['a']==a, ('position drift',i,j)         # keep the original spread of "a"
    by[K[i]][j]={"q":q,"o":o,"a":a,"e":e,"chg":True}
    s=list(AFTER[i]); s[j]=lvl; AFTER[i]=''.join(s); NCHG+=1

# ---- 2 قيم الدوال المثلثية
v=[-1,sq(3)/2,0,1.5]
setq(2,"قيم الدوال",5,'U',"أى القيم الآتية لا يمكن أن تكون قيمة لـ جا θ ؟",["-1","sqrt(3)/2","0","3/2"],3,
 "على دائرة الوحدة -1 ≤ جا θ ≤ 1، والعدد 3/2 أكبر من 1 فلا يمكن أن يكون قيمة للجيب.",
 [not(-1<=x<=1) for x in v])

# ---- 3 line y = 2 vs unit circle: x^2 = 1 - 4
disc=1-2**2
setq(3,"إيجاد قياس",5,'U',"علل: المعادلة جا θ = 2 ليس لها حل.",
 ["لأن الدالة جا θ غير معرّفة عند بعض الزوايا","لأن المستقيم ص = 2 يمس دائرة الوحدة فى نقطة","لأن المستقيم ص = 2 لا يقطع دائرة الوحدة","لأن الضلع النهائى لا يدور أكثر من دورة"],2,
 "حلول جا θ = ك هى نقاط تقاطع المستقيم ص = ك مع دائرة الوحدة، و ص = 2 يقع خارجها.",
 [False, disc==0, disc<0 and all(sin(t)<2 for t in TH), False])

# ---- 7 sin(pi - t) = sin t : symmetry about the y-axis
P=lambda t:(cos(t),sin(t))
symy=all(eq(P(pi-t)[0],-P(t)[0]) and eq(P(pi-t)[1],P(t)[1]) for t in TH)
symx=all(eq(P(pi-t)[0],P(t)[0]) and eq(P(pi-t)[1],-P(t)[1]) for t in TH)
symo=all(eq(P(pi-t)[0],-P(t)[0]) and eq(P(pi-t)[1],-P(t)[1]) for t in TH)
same=all(eq(P(pi-t)[0],P(t)[0]) and eq(P(pi-t)[1],P(t)[1]) for t in TH)
setq(7,"خواص",2,'U',"علل: جا(pi - θ) = جا θ.",
 ["لأن نقطتى الزاويتين متماثلتان حول محور السينات","لأن نقطتى الزاويتين متماثلتان حول نقطة الأصل","لأن الزاويتين لهما الضلع النهائى نفسه دائمًا","لأن نقطتى الزاويتين متماثلتان حول محور الصادات"],3,
 "نقطتا θ و pi - θ على دائرة الوحدة متماثلتان حول محور الصادات، فلهما الإحداثى الصادى نفسه.",
 [symx,symo,same,symy])

# ---- 8 intersections of sin and cos on [0,2pi)
sol=sorted(k*pi/12 for k in range(24) if eq(sin(k*pi/12),cos(k*pi/12)))
cand=[[pi/4,5*pi/4],[pi/4,3*pi/4],[pi/2,3*pi/2],[3*pi/4,7*pi/4]]
assert len(sol)==2 and sum(1 for k in range(2400) if abs(sin(k*pi/1200)-cos(k*pi/1200))<1e-9)==2
setq(8,"البيانى للدوال المثلثية (1)",0,'A',"فى الفترة 0 ≤ θ < 2pi يتقاطع المنحنيان ص = جا θ و ص = جتا θ عند θ =",
 ["pi/4 أو 5pi/4","pi/4 أو 3pi/4","pi/2 أو 3pi/2","3pi/4 أو 7pi/4"],0,
 "يتساوى الجيب وجيب التمام عندما ظا θ = 1، أى عند pi/4 فى الربع الأول و 5pi/4 فى الربع الثالث.",
 [all(eq(a,b) for a,b in zip(sorted(c),sol)) for c in cand])

# ---- 12 المعادلات المثلثية
v=[7*pi/6,pi/6,5*pi/6,13*pi/6]
setq(12,"المعادلات المثلثية",2,'U',"أى مما يأتى ليس حلًّا للمعادلة جا θ = 1/2 ؟",["7pi/6","pi/6","5pi/6","13pi/6"],0,
 "جا(7pi/6) = -1/2 لأنها فى الربع الثالث، أما 13pi/6 فهى pi/6 + 2pi وتحقق المعادلة.",
 [not eq(sin(x),0.5) for x in v])
per=lambda p:all(eq(tan(t+p),tan(t),1e-6) for t in TH)
minper=min(p for p in (pi/2,pi,2*pi) if per(p))
setq(12,"المعادلات المثلثية",3,'U',"علل: فى الحل العام لمعادلة فى ظا θ نضيف pi × ن وليس 2pi × ن.",
 ["لأن دورة ظا θ تساوى 2pi","لأن ظا θ موجبة فى كل الأرباع","لأن مدى ظا θ من -1 إلى 1","لأن دورة ظا θ تساوى pi"],3,
 "قيم ظا θ تتكرر كل pi، فكل الحلول تنتج من حل واحد بإضافة مضاعفات pi.",
 [eq(minper,2*pi), all(tan(t)>0 for t in (1,2,4,5.5)), all(abs(tan(t))<=1 for t in TH), eq(minper,pi)])

# ---- 14 substitution cos^2 = 1 - sin^2
orig=lambda s:2*(1-s*s)+s-1
cs=[(2,1,-1),(2,-1,1),(2,-1,-1),(2,1,-3)]
S=[F(n,7) for n in range(-7,8)]
setq(14,"المعادلات والمتباينات المثلثية (1)",3,'U',"عند حل 2 جتا^2 θ + جا θ - 1 = 0 بالتعويض جتا^2 θ = 1 - جا^2 θ تصير المعادلة:",
 ["2 جا^2 θ + جا θ - 1 = 0","2 جا^2 θ - جا θ + 1 = 0","2 جا^2 θ - جا θ - 1 = 0","2 جا^2 θ + جا θ - 3 = 0"],2,
 "بالتعويض: 2(1 - جا^2 θ) + جا θ - 1 = 0، وبالتبسيط والضرب فى -1 ينتج المطلوب.",
 [all(orig(s)==-(a*s*s+b*s+c) for s in S) or all(orig(s)==(a*s*s+b*s+c) for s in S) for a,b,c in cs])

# ---- 16 vertex outside the range of t
g=lambda t:t*t-4*t; T=[F(n,50) for n in range(-50,51)]
mn=min(g(t) for t in T)
setq(16,"القيمتان العظمى والصغرى للدوال المثلثية (1)",5,'U',"علل: لا تبلغ الدالة ص = جا^2 θ - 4 جا θ قيمتها الصغرى عند رأس القطع المكافئ ت = 2 (حيث ت = جا θ).",
 ["لأن ت = 2 خارج المدى -1 ≤ ت ≤ 1","لأن معامل ت^2 فى الدالة عدد سالب","لأن الدالة ليست تربيعية فى المتغيّر ت","لأن ت = 2 تعطى القيمة العظمى للدالة"],0,
 "ت = جا θ محصورة بين -1 و 1، فالرأس ت = 2 غير متاح، والصغرى عند الطرف ت = 1 وتساوى -3.",
 [not(-1<=2<=1) and mn==g(F(1))==-3, 1<0, False, g(2)>g(1)])

# ---- 17 counter-example to sin(a+b)=sin a+sin b
pr=[(pi/2,pi/2),(2*pi,3*pi/2),(pi,0),(0,0)]
setq(17,"نظريات جمع",4,'U',"كتب طالب: جا(α + β) = جا α + جا β. أى زوج من القيم يبيّن خطأ هذه المساواة؟",
 ["α = pi/2 ، β = pi/2","α = 2pi ، β = 3pi/2","α = pi ، β = 0","α = 0 ، β = 0"],0,
 "جا(pi/2 + pi/2) = جا pi = 0 بينما جا(pi/2) + جا(pi/2) = 2؛ أما الأزواج الأخرى فتتساوى عندها القيمتان مصادفة.",
 [not eq(sin(a+b),sin(a)+sin(b)) for a,b in pr])

# ---- 18 perpendicular lines
M=[F(1,2),2,-3,F(5,3)]
den0=all(1+m*(-1/F(m))==0 for m in M); num0=any(m-(-1/F(m))==0 for m in M)
setq(18,"الزاوية بين مستقيمين",5,'U',"ماذا يحدث عند تطبيق صيغة ظا(α - β) على مستقيمين حاصل ضرب ميليهما -1 ؟",
 ["يساوى البسط صفرًا فالمستقيمان متوازيان","تساوى ظا الزاوية 1 فالزاوية بينهما pi/4","يساوى المقام 2 فالزاوية بينهما حادّة","يساوى المقام صفرًا فالمستقيمان متعامدان"],3,
 "المقام 1 + ظا α ظا β = 1 + (-1) = 0، فالظل غير معرّف والزاوية بين المستقيمين pi/2.",
 [num0, False, any(1+m*(-1/F(m))==2 for m in M), den0])

# ---- 20 sign of the root
a1,a2=pi/4,5*pi/4
setq(20,"لنصف الزاوية",1,'U',"علل: عند حساب جا(θ/2) من قيمة جا^2(θ/2) يجب معرفة الربع الذى تقع فيه θ/2.",
 ["لحساب قيمة جتا θ أولًا","لتحديد إشارة الجذر التربيعى","لتحويل الزاوية إلى الراديان","لمعرفة دورة الدالة جا(θ/2)"],1,
 "جا^2(θ/2) يعطى قيمتين متعاكستين فى الإشارة، والربع الذى تقع فيه θ/2 يحدد أيهما نأخذ.",
 [False, eq(sin(a1)**2,sin(a2)**2) and sin(a1)>0>sin(a2), False, False])

# ---- 22 r is the distance from the origin
a,b=3,4; r=5
ident=all(eq(a*sin(t)+b*cos(t), r*sin(t+math.atan2(b,a))) for t in TH)
setq(22,"الصورة التوافقية",5,'U',"علل: عند كتابة 3 جا θ + 4 جتا θ فى الصورة ر جا(θ + α) تكون ر = 5.",
 ["لأن ر مجموع إحداثيى النقطة (3 ، 4)","لأن ر بُعد النقطة (3 ، 4) عن نقطة الأصل","لأن ر ميل المستقيم المار بالنقطة (3 ، 4)","لأن ر حاصل ضرب إحداثيى النقطة (3 ، 4)"],1,
 "ر = sqrt(3^2 + 4^2) = 5 وهو بُعد النقطة (3 ، 4) عن نقطة الأصل، لا مجموع الإحداثيين 7.",
 [a+b==r, ident and eq(math.hypot(a,b),r), eq(b/a,r), a*b==r])

# ---- 23 no solution because of the amplitude
f=lambda t:sin(t)+sq(3)*cos(t)
idk=lambda k:all(eq(f(t),k*sin(t+pi/3)) for t in TH)
mx=max(f(k*pi/600) for k in range(1200))
setq(23,"بالصورة التوافقية",4,'U',"علل: المعادلة جا θ + sqrt(3) جتا θ = 3 ليس لها حل.",
 ["لأن المقدار يساوى 2 جا(θ + pi/3) ≥ 3 دائمًا","لأن المقدار يساوى 2 جا(θ + pi/3) ≤ 2 دائمًا","لأن المقدار يساوى جا(θ + pi/3) ≤ 1 دائمًا","لأن المقدار يساوى 4 جا(θ + pi/3) ≤ 4 دائمًا"],1,
 "المقدار = 2 جا(θ + pi/3) وأكبر قيمة له 2، فلا يمكن أن يساوى 3.",
 [idk(2) and all(f(t)>=3 for t in TH), idk(2) and eq(mx,2,1e-4) and mx<3, idk(1), idk(4)])

# ---- 24 doubling both coefficients
m1=max(3*sin(k*pi/3600)+4*cos(k*pi/3600) for k in range(7200)); m2=max(6*sin(k*pi/3600)+8*cos(k*pi/3600) for k in range(7200))
assert eq(m1,5,1e-5)
setq(24,"القيمتان العظمى والصغرى للدوال المثلثية (2)",3,'U',"القيمة العظمى للدالة ص = 3 جا θ + 4 جتا θ تساوى 5. ماذا يحدث لها إذا ضوعف المعاملان فصارت ص = 6 جا θ + 8 جتا θ ؟",
 ["تبقى 5 كما هى","تصير 10","تصير 14","تصير 25"],1,
 "القيمة العظمى = sqrt(6^2 + 8^2) = 10، أى ضعف 5، لأن ر تتضاعف بمضاعفة أ و ب معًا.",
 [eq(m2,x,1e-4) for x in (5,10,14,25)])

# ---- 31 base between 0 and 1 flips the inequality
xs=[F(n,4) for n in range(-12,20)]
true_set=[x for x in xs if (1/3)**float(x)<(1/3)**2-1e-12]
setq(31,"المعادلات والمتباينات الأسّية (1)",2,'U',"حلّ طالب المتباينة (1/3)^س < (1/3)^2 فكتب س < 2. ما خطؤه؟",
 ["أخطأ فى توحيد الأساس","أهمل شرط أن يكون س موجبًا","عكس علامة المتباينة دون سبب","لم يعكس علامة المتباينة"],3,
 "الأساس 1/3 بين 0 و 1 فالدالة متناقصة، فتنعكس العلامة ويكون الحل س > 2.",
 [False, any(x<=0 for x in true_set), False, true_set==[x for x in xs if x>2]])

# ---- 37 reciprocal logs
PB=[(2,3),(5,0.5),(0.3,7),(10,4)]
lg=lambda a,b:math.log(b)/math.log(a)
setq(37,"تغيير الأساس (1)",2,'U',"علل: لو_أ(ب) × لو_ب(أ) = 1 (أ ، ب موجبان ولا يساوى أىٌّ منهما 1).",
 ["لأن لو_ب(أ) = 1 ÷ لو_أ(ب)","لأن لو_ب(أ) = -لو_أ(ب)","لأن لو_ب(أ) = لو_أ(ب)","لأن لو_ب(أ) = 1 - لو_أ(ب)"],0,
 "بتغيير الأساس إلى أ: لو_ب(أ) = لو_أ(أ) ÷ لو_أ(ب) = 1 ÷ لو_أ(ب)، فحاصل الضرب 1.",
 [all(eq(lg(b,a),1/lg(a,b)) for a,b in PB), all(eq(lg(b,a),-lg(a,b)) for a,b in PB), all(eq(lg(b,a),lg(a,b)) for a,b in PB), all(eq(lg(b,a),1-lg(a,b)) for a,b in PB)])

# ---- 38 log_4 9 = log_2 3
L=lg(4,9); l9=lg(2,9); l4=lg(2,4)
assert eq(L,lg(2,3))
setq(38,"تغيير الأساس (2)",4,'U',"علل: لو_4(9) = لو_2(3).",
 ["لأن لو_4(9) = لو_2(9) - لو_2(4)","لأن لو_4(9) = لو_2(9) × لو_2(4)","لأن لو_4(9) = لو_2(9) ÷ لو_2(4)","لأن لو_4(9) = لو_2(9) + لو_2(4)"],2,
 "لو_2(9) ÷ لو_2(4) = 2 لو_2(3) ÷ 2 = لو_2(3) بقانون تغيير الأساس.",
 [eq(L,l9-l4),eq(L,l9*l4),eq(L,l9/l4) and eq(l9/l4,2*lg(2,3)/2),eq(L,l9+l4)])

# ---- 39 method (recall)
A_,B_=math.log10(2),math.log10(3)
ok=eq(math.log10(12),2*A_+B_) and eq(math.log10(18),A_+2*B_) and eq(math.log10(5),1-A_) and 12==2**2*3 and 18==2*3**2
setq(39,"التعبير عن لوغاريتم",5,'R',"للتعبير عن لو_10(م) بدلالة لو_10(2) و لو_10(3) نكتب العدد م أولًا فى صورة:",
 ["حاصل ضرب قوى للأعداد 2 ، 3 ، 10","مجموع مضاعفات للأعداد 2 ، 3 ، 10","فرق بين مربّعين كاملين","كسر عشرى دورى"],0,
 "مثل 12 = 2^2 × 3 و 5 = 10 ÷ 2؛ فقوانين اللوغاريتمات تحوّل الضرب والقوى إلى جمع ومضاعفات.",
 [ok, eq(math.log10(2+3),A_+B_), False, False])

# ---- 40 no y-intercept
def defined(x):
    try: math.log(x); return True
    except ValueError: return False
setq(40,"الدوال اللوغاريتمية",1,'U',"علل: منحنى ص = لو_أ(س) لا يقطع محور الصادات.",
 ["لأن المنحنى يمر بالنقطة (0 ، 1)","لأن الدالة متزايدة دائمًا","لأن مدى الدالة ص > 0 فقط","لأن س = 0 ليست فى مجال الدالة"],3,
 "مجال الدالة اللوغاريتمية س > 0 فقط، فلا توجد نقطة على المنحنى إحداثيها السينى صفر.",
 [defined(0), all(lg(a,3)>lg(a,2) for a in (0.5,2)), all(lg(2,x)>0 for x in (0.5,2)), not defined(0)])

# ---- 46 multiplying by 10
N=list(range(1,3000,7))
dg=lambda n:len(str(n))
setq(46,"اللوغاريتمات المعتادة",4,'U',"ماذا يحدث لعدد أرقام عدد صحيح موجب عند ضربه فى 10 ؟",
 ["يتضاعف","يزيد 10","يزيد 1","لا يتغيّر"],2,
 "لو_10(10س) = لو_10(س) + 1، فيزيد الجزء الصحيح للوغاريتم واحدًا ويزيد عدد الأرقام رقمًا واحدًا.",
 [all(dg(10*n)==2*dg(n) for n in N), all(dg(10*n)==dg(n)+10 for n in N), all(dg(10*n)==dg(n)+1 for n in N), all(dg(10*n)==dg(n) for n in N)])

# ---- 48 cancelling in a limit
near=[2+d for d in (1e-3,-1e-3,1e-5,-1e-5)]
canc=all(eq((x*x-4)/(x-2),x+2,1e-6) for x in near)
setq(48,"قيمة النهاية",4,'U',"علل: عند حساب نها (س → 2) للمقدار (س^2 - 4) ÷ (س - 2) يجوز اختصار العامل (س - 2).",
 ["لأن البسط لا ينعدم عند س = 2","لأن س تقترب من 2 ولا تساويها","لأن المقام عدد موجب دائمًا","لأن النهاية تساوى صفرًا دائمًا"],1,
 "س تقترب من 2 دون أن تساويها، فالعامل س - 2 لا يساوى صفرًا ويجوز اختصاره، والنهاية 4.",
 [2*2-4!=0, canc and all(x!=2 for x in near), all(x-2>0 for x in near), eq((near[2]**2-4)/(near[2]-2),0,1e-3)])

# ---- 50 h -> 0
x0=1.7
setq(50,"تعريف المشتقة",1,'U',"عند اشتقاق د(س) = س^2 بالتعريف يُختصر المقدار إلى 2س + هـ. لماذا تكون المشتقة 2س ؟",
 ["لأن هـ عدد سالب دائمًا","لأن س تقترب من الصفر","لأن هـ تقترب من الصفر","لأن هـ تساوى س فى النهاية"],2,
 "المشتقة هى نهاية المقدار عندما هـ → 0، فيقترب 2س + هـ من 2س.",
 [False, False, all(eq(((x0+h)**2-x0**2)/h,2*x0+h,1e-6) for h in (1e-2,1e-4)) and eq(dnum(lambda x:x*x,x0),2*x0,1e-6), eq(2*x0+x0,2*x0)])

# ---- 51 product is not differentiated factor by factor
fs=[lambda x:6*x**5, lambda x:5*x**4, lambda x:5*x**6, lambda x:6*x**4]
setq(51,"الاشتقاق باستخدام القوانين",2,'U',"كتب طالب أن مشتقة د(س) = س^2 × س^3 هى 2س × 3س^2. المشتقة الصحيحة هى:",
 ["6س^5","5س^4","5س^6","6س^4"],1,
 "د(س) = س^5 فمشتقتها 5س^4؛ ومشتقة حاصل الضرب لا تساوى حاصل ضرب المشتقتين.",
 [all(eq(dnum(lambda x:x**2*x**3,x),g(x),1e-4) for x in XS) for g in fs])

# ---- 53 zero derivative
f=lambda x:x*x-6*x; a0=3; sl=dnum(f,a0)
setq(53,"المماس (1)",2,'U',"ماذا يعنى أن دَ(أ) = 0 بالنسبة إلى مماس منحنى ص = د(س) عند س = أ ؟",
 ["المماس أفقى","المماس رأسى","المماس يمر بنقطة الأصل","المماس غير موجود"],0,
 "دَ(أ) هو ميل المماس عند س = أ، والميل صفر يعنى أن المماس أفقى.",
 [eq(sl,0,1e-6), False, eq(sl,0,1e-6) and eq(f(a0),0), False])

# ---- 54 no tangent through an interior point
T=[n/100 for n in range(-500,501)]
setq(54,"المماس (2)",2,'U',"علل: لا يمكن رسم مماس لمنحنى ص = س^2 يمر بالنقطة (0 ، 1).",
 ["لأن النقطة (0 ، 1) تقع على المنحنى","لأن ميل المماس عند س = 0 يساوى 1","لأن المنحنى لا يقطع محور الصادات","لأن شرط التماس ت^2 = -1 بلا حل"],3,
 "المماس عند س = ت معادلته ص = 2ت س - ت^2، ومروره بالنقطة (0 ، 1) يتطلب -ت^2 = 1 وهذا مستحيل.",
 [0**2==1, eq(dnum(lambda x:x*x,0),1), False, all(not eq(2*t*0-t*t,1) for t in T)])

# ---- 55 sign table in words
f=lambda x:x**3/3-x**2/2-2*x                                   # f' = (x+1)(x-2)
fp=lambda x:(x+1)*(x-2)
assert fp(-2)>0 and fp(0)<0 and fp(3)>0
lmax=lambda c:f(c)>f(c-1e-3) and f(c)>f(c+1e-3); lmin=lambda c:f(c)<f(c-1e-3) and f(c)<f(c+1e-3)
setq(55,"منحنى الدوال التكعيبية",4,'U',"إشارة دَ(س) لدالة د: موجبة عندما س < -1، سالبة عندما -1 < س < 2، موجبة عندما س > 2. أى العبارات الآتية صحيحة؟",
 ["للدالة قيمة صغرى محلية عند س = -1","للدالة قيمة عظمى محلية عند س = -1","الدالة متزايدة فى الفترة -1 < س < 2","للدالة قيمة عظمى محلية عند س = 2"],1,
 "عند س = -1 تتغير إشارة المشتقة من موجبة إلى سالبة فتكون القيمة عظمى محلية، وعند س = 2 صغرى محلية.",
 [lmin(-1), lmax(-1), f(1.5)>f(0), lmax(2)])

# ---- 56 endpoint beats the local maximum
f=lambda x:x**3-3*x**2+2
gmax=max(f(-2+6*k/6000) for k in range(6001))
setq(56,"القيم العظمى والصغرى للدوال التكعيبية",2,'U',"علل: القيمة العظمى للدالة د(س) = س^3 - 3س^2 + 2 فى الفترة -2 ≤ س ≤ 4 هى 18 وليست قيمتها العظمى المحلية 2.",
 ["لأن دَ(س) موجبة فى الفترة كلها","لأن الدالة ليس لها قيم قصوى محلية","لأن د(4) = 18 أكبر من د(0) = 2","لأن د(-2) = 18 أكبر من د(0) = 2"],2,
 "قيمة الدالة عند الطرف س = 4 تساوى 18 وهى أكبر من القيمة العظمى المحلية د(0) = 2.",
 [dnum(f,1)>0, False, f(4)==18>f(0)==2 and eq(gmax,18), f(-2)==18])

# ---- 57 derivative from the positions of the extrema
a,b=-6,9
f=lambda x:x**3+a*x*x+b*x
d1=lambda x:dnum(f,x)
setq(57,"تعيين الدالة من قيمها العظمى",3,'U',"إذا كان للدالة د(س) = س^3 + أ س^2 + ب س قيمتان قصويان عند س = 1 و س = 3، فلماذا تكون دَ(س) = 3(س - 1)(س - 3) ؟",
 ["لأن 1 و 3 جذرا د(س) = 0 ومعامل س^3 يساوى 3","لأن 1 و 3 جذرا دَ(س) = 0 ومعامل س^2 فيها 3","لأن 1 و 3 جذرا دَ(س) = 0 ومعامل س^2 فيها 1","لأن د(1) = د(3) = 0 ومعامل س فى د يساوى 3"],1,
 "دَ(س) = 3س^2 + 2أ س + ب تربيعية معامل س^2 فيها 3، وتنعدم عند القيم القصوى س = 1 و س = 3.",
 [f(1)==0 and f(3)==0, all(eq(d1(x),3*(x-1)*(x-3),1e-4) for x in XS), all(eq(d1(x),(x-1)*(x-3),1e-4) for x in XS), f(1)==0==f(3)])

# ---- 58 number of extrema as k changes
def next_(k):
    fp=lambda x:3*x*x-6*x+k
    xs=[-5+10*i/20000 for i in range(20001)]
    return sum(1 for u,w in zip(xs,xs[1:]) if fp(u)*fp(w)<0)
n2,n4=next_(2),next_(4)
setq(58,"الدوال التكعيبية والمميِّز (1)",1,'U',"ماذا يحدث لعدد القيم القصوى للدالة د(س) = س^3 - 3س^2 + ك س عندما تتغيّر ك من 2 إلى 4 ؟",
 ["يزيد من 0 إلى 2","يبقى 2","ينقص من 2 إلى 0","يبقى 0"],2,
 "مميِّز دَ(س) = 3س^2 - 6س + ك هو 36 - 12ك: موجب عند ك = 2 (قيمتان) وسالب عند ك = 4 (لا قيم).",
 [(n2,n4)==(0,2),(n2,n4)==(2,2),(n2,n4)==(2,0) and 36-12*2>0>36-12*4,(n2,n4)==(0,0)])

# ---- 61 tangency at the local maximum
g=lambda x:x**3-3*x
roots=sorted({round(x,6) for x in [n/1000 for n in range(-4000,4001)] if eq(g(x),2)})
setq(61,"الدوال التكعيبية والمعادلات التكعيبية (2)",4,'U',"علل: عند ك = 2 يكون للمعادلة س^3 - 3س = ك جذران حقيقيان مختلفان فقط.",
 ["لأن المستقيم ص = 2 لا يقطع المنحنى إطلاقًا","لأن المستقيم ص = 2 يقطع المنحنى فى ثلاث نقاط مختلفة","لأن المستقيم ص = 2 يمس المنحنى ويقطعه فى نقطة","لأن المستقيم ص = 2 يمر بنقطة الأصل وبالقمة"],2,
 "ص = 2 يمس المنحنى عند القمة العظمى (-1 ، 2) ويقطعه عند س = 2، فالجذور -1 (مكرر) و 2.",
 [len(roots)==0, len(roots)==3, roots==[-1,2] and eq(dnum(g,-1),0,1e-6) and not eq(dnum(g,2),0), False])

# ---- 63 quartics
f=lambda x:x**4-2*x**2
setq(63,"الدرجة الرابعة",0,'U',"علل: منحنى د(س) = س^4 - 2س^2 متماثل حول محور الصادات.",
 ["لأن د(-س) = د(س)","لأن د(-س) = -د(س)","لأن د(س) ≥ 0 دائمًا","لأن دَ(س) > 0 دائمًا"],0,
 "كل قوى س زوجية فيكون د(-س) = د(س)، أى أن النقطتين (س ، ص) و (-س ، ص) على المنحنى معًا.",
 [all(eq(f(-x),f(x)) for x in XS), all(eq(f(-x),-f(x)) for x in XS), all(f(x)>=0 for x in XS+[1]), all(dnum(f,x)>0 for x in XS)])
f=lambda x:x**4-4*x**3; fp=lambda x:4*x**3-12*x*x
assert all(eq(dnum(f,x),fp(x),1e-3) for x in XS)
setq(63,"الدرجة الرابعة",5,'U',"للدالة د(س) = س^4 - 4س^3 يكون دَ(0) = 0، ومع ذلك ليس لها قيمة قصوى عند س = 0 لأن:",
 ["إشارة دَ(س) لا تتغيّر حول س = 0","الدالة غير معرّفة عند س = 0","دَ(س) موجبة لكل قيم س ما عدا الصفر","المنحنى لا يمر بنقطة الأصل"],0,
 "دَ(س) = 4س^2(س - 3) سالبة قبل الصفر وبعده، فلا تتغير الإشارة؛ والقيمة القصوى الوحيدة عند س = 3.",
 [fp(0)==0 and fp(-0.1)<0 and fp(0.1)<0, False, all(fp(x)>0 for x in XS), f(0)!=0])

# ---- 64 antiderivatives of 2x
fs=[lambda x:x*x+5, lambda x:2*x*x, lambda x:x*x-3, lambda x:x*x]
setq(64,"التكامل غير المحدد",3,'U',"أى الدوال الآتية ليست تكاملًا غير محدد للدالة 2س ؟",
 ["س^2 + 5","2س^2","س^2 - 3","س^2"],1,
 "مشتقة 2س^2 هى 4س لا 2س؛ أما البقية فمشتقة كل منها 2س لأنها تختلف بثابت فقط.",
 [not all(eq(dnum(g,x),2*x,1e-5) for x in XS) for g in fs])

# ---- 67 equal limits
Fq=lambda x:x**3; fq=lambda x:3*x*x; a0=2
setq(67,"التكامل المحدّد (1)",1,'U',"علل: إذا تساوى حدّا التكامل المحدّد (من أ إلى أ) فإن قيمته صفر.",
 ["لأن الدالة تنعدم عند هذا الحد","لأن ق(أ) - ق(أ) = 0","لأن ثابت التكامل يساوى صفرًا","لأن ق(أ) + ق(أ) = 0"],1,
 "التكامل المحدّد = ق(ب) - ق(أ)، وعند ب = أ يصير ق(أ) - ق(أ) = 0 مهما كانت الدالة.",
 [fq(a0)==0, Fq(a0)-Fq(a0)==0 and eq(simpson(fq,a0,a0+0),0), False, Fq(a0)+Fq(a0)==0])

# ---- 71 incorrect statement about area and integral
I=simpson(lambda x:x*x-2*x,0,2); area=simpson(lambda x:abs(x*x-2*x),0,2)
assert eq(I,-4/3,1e-9) and eq(area,4/3,1e-6)
setq(71,"مساحات المناطق (1)",1,'U',"أى العبارات الآتية غير صحيحة؟",
 ["المساحة لا تكون عددًا سالبًا","التكامل المحدّد قد يكون عددًا سالبًا","إذا كانت د(س) ≤ 0 فالمساحة = سالب التكامل","التكامل المحدّد يساوى المساحة دائمًا"],3,
 "إذا وقع المنحنى تحت محور السينات كان التكامل سالبًا والمساحة موجبة، فلا يتساويان دائمًا.",
 [not(area>=0), not(I<0), not eq(area,-I,1e-6), not eq(I,area)])

# ---- 72 wrong order of subtraction
I=simpson(lambda x:x*x-2*x,0,2)
inter=[x for x in (0,2) if x*x==2*x]
setq(72,"مساحات المناطق (2)",4,'U',"لحساب المساحة المحصورة بين ص = س^2 و ص = 2س كامَل طالب المقدار (س^2 - 2س) من 0 إلى 2 فحصل على -4/3. ما خطؤه؟",
 ["أخطأ فى تعيين حدّى التكامل الأدنى والأعلى","طرح المنحنى الأعلى من الأسفل","نسى إضافة ثابت التكامل","كامَل حاصل ضرب الدالتين"],1,
 "فى الفترة من 0 إلى 2 المستقيم ص = 2س هو الأعلى، فالصواب تكامل (2س - س^2) والمساحة 4/3.",
 [inter!=[0,2], eq(I,-4/3) and all(2*x>x*x for x in (0.5,1,1.5)), False, False])

# ---- 73 set-up of the area for a cubic
f=lambda x:x**3-4*x
A1=simpson(f,-2,0); A2=simpson(f,0,2); area=simpson(lambda x:abs(f(x)),-2,2)
vals=[simpson(f,-2,2),A1-A2,A1+A2,A2-A1]
setq(73,"مساحات المناطق (3)",3,'U',"لحساب مساحة المنطقة المحصورة بين المنحنى ص = س^3 - 4س ومحور السينات نحسب للدالة س^3 - 4س:",
 ["التكامل من -2 إلى 2 مباشرة","(التكامل من -2 إلى 0) - (التكامل من 0 إلى 2)","(التكامل من -2 إلى 0) + (التكامل من 0 إلى 2)","(التكامل من 0 إلى 2) - (التكامل من -2 إلى 0)"],1,
 "المنحنى فوق المحور من -2 إلى 0 وتحته من 0 إلى 2، فنطرح التكامل الثانى: 4 - (-4) = 8.",
 [eq(v,area,1e-5) and eq(area,8,1e-5) for v in vals])

# ---- 74 removing the absolute value
I=[F(n,10) for n in range(0,21)]
fs=[lambda x:2-x, lambda x:x-2, lambda x:x+2, lambda x:-x-2]
setq(74,"القيمة المطلقة",4,'U',"عند حساب التكامل المحدّد للدالة |س - 2| من 0 إلى 5، يُكتب |س - 2| فى الفترة 0 ≤ س ≤ 2 فى الصورة:",
 ["2 - س","س - 2","س + 2","-س - 2"],0,
 "فى هذه الفترة س - 2 ≤ 0، فتكون |س - 2| = -(س - 2) = 2 - س.",
 [all(abs(x-2)==g(x) for x in I) for g in fs])

# ---- 75 symmetric tangents
t1=lambda x:2*x-1; t2=lambda x:-2*x-1
assert eq(dnum(lambda x:x*x,1),2) and t1(1)==1 and eq(dnum(lambda x:x*x,-1),-2) and t2(-1)==1
setq(75,"المماسّات والمساحة",2,'U',"علل: مماسّا القطع المكافئ ص = س^2 عند س = -1 و س = 1 يتقاطعان على محور الصادات.",
 ["لأنهما يمران معًا بنقطة الأصل (0 ، 0)","لأنهما متماثلان حول محور الصادات","لأنهما متماثلان حول محور السينات","لأنهما متعامدان وميلاهما 1 و -1"],1,
 "القطع متماثل حول محور الصادات، فالمماسان ص = 2س - 1 و ص = -2س - 1 متماثلان حوله ويلتقيان عليه عند (0 ، -1).",
 [t1(0)==0==t2(0), all(t1(-x)==t2(x) for x in XS) and t1(0)==t2(0), all(-t1(x)==t2(x) for x in XS), 2*-2==-1])

# ---- 76 تنصيف المساحة
ar=lambda m:simpson(lambda x:m*x-x*x,0,m)                      # between y = x^2 and y = m x
ratio=ar(4)/ar(2)
setq(76,"تنصيف المساحة",4,'U',"ماذا يحدث للمساحة المحصورة بين قطع مكافئ ومستقيم يقطعه فى نقطتين إذا تضاعف الفرق بين الإحداثيين السينيين لنقطتى التقاطع مع ثبات معامل س^2 ؟",
 ["تتضاعف","تصير 4 أمثالها","تصير 6 أمثالها","تصير 8 أمثالها"],3,
 "المساحة تتناسب مع مكعّب الفرق (β - α)^3، فمضاعفة الفرق تضرب المساحة فى 2^3 = 8.",
 [eq(ratio,x,1e-6) for x in (2,4,6,8)])
tot=simpson(lambda x:3*x-x*x,0,3); assert eq(tot,4.5,1e-9)
def part(m): return simpson(lambda x:3*x-x*x-m*x,0,3-m)
ms=[3-2**(1/3),1.5,3-3/2**(1/3),3-3/4**(1/3)]
setq(76,"تنصيف المساحة",5,'A',"إذا كان المستقيم ص = م س ينصّف مساحة المنطقة المحصورة بين القطع المكافئ ص = 3س - س^2 ومحور السينات فإن م =",
 ["3 - 2^(1/3)","3/2","3 - 3/2^(1/3)","3 - 3/4^(1/3)"],2,
 "المساحة الكلية 9/2 والمساحة بين القطع والمستقيم (3 - م)^3/6 = 9/4، فيكون (3 - م)^3 = 27/2.",
 [0<m<3 and eq(part(m),tot/2,1e-7) for m in ms])

# ---- 78 expectation
die=[F(k) for k in range(1,7)]; Ed=sum(die)/6
setq(78,"توقّع المتغيّرات العشوائية",1,'U',"توقّع العدد الظاهر عند إلقاء حجر نرد منتظم يساوى 7/2. ماذا نستنتج من ذلك؟",
 ["التوقّع قد لا يكون إحدى قيم المتغيّر","التوقّع يساوى دائمًا أكبر قيم المتغيّر","حجر النرد لا بدّ أن يكون غير منتظم","العدد 7/2 أكثر قيم المتغيّر احتمالًا"],0,
 "7/2 ليس وجهًا من أوجه النرد؛ فالتوقّع متوسّط مرجّح للقيم وليس بالضرورة واحدًا منها.",
 [Ed==F(7,2) and Ed not in die, Ed==max(die), False, Ed in die])
vals=[2,4,9]; E=sum(F(x,3) for x in vals)
setq(78,"توقّع المتغيّرات العشوائية",2,'U',"يأخذ المتغيّر س القيم 2 ، 4 ، 9 باحتمالات متساوية. توقّعه فى هذه الحالة هو:",
 ["أكبر القيم وهو 9","مجموع القيم وهو 15","القيمة الوسطى وهى 4","متوسّط القيم وهو 5"],3,
 "كل احتمال 1/3، فالتوقّع = (2 + 4 + 9) ÷ 3 = 5، أى الوسط الحسابى للقيم عند تساوى الاحتمالات.",
 [E==9, E==15, E==4, E==5==F(sum(vals),3)])

# ---- 79 E(X^2) vs (E X)^2
EX=F(1,2)*1+F(1,2)*(-1); EX2=F(1,2)*1+F(1,2)*1
setq(79,"خواصّ التوقّع",4,'U',"يأخذ المتغيّر س القيمتين 1 و -1 باحتمالين متساويين. أى العبارات الآتية صحيحة؟",
 ["توقّع س^2 = (توقّع س)^2 = 1","توقّع س = 0 و توقّع س^2 = 1","توقّع س = 0 و توقّع س^2 = 0","توقّع س = 1 و توقّع س^2 = 1"],1,
 "توقّع س = 1/2 - 1/2 = 0 و توقّع س^2 = 1/2 + 1/2 = 1؛ فتوقّع س^2 لا يساوى مربّع توقّع س.",
 [EX2==EX**2==1, EX==0 and EX2==1, EX==0 and EX2==0, EX==1 and EX2==1])

# ---- 80 variance of a constant
var=1*F(5)**2-(1*F(5))**2
setq(80,"تباين المتغيّرات العشوائية",3,'U',"متغيّر عشوائى يأخذ القيمة 5 فقط باحتمال 1. تباينه يساوى:",
 ["5","0","25","1"],1,
 "توقّعه 5 وكل انحراف عن التوقّع صفر، فالتباين = 25 - 5^2 = 0 لأن القيم لا تتشتّت.",
 [var==x for x in (5,0,25,1)])

# ---- 83 rule for a linear transform (recall)
xs=[0,1,2]; ps=[F(1,4),F(1,2),F(1,4)]
def stats(vs): 
    m=sum(v*p for v,p in zip(vs,ps)); return m, sq(sum(v*v*p for v,p in zip(vs,ps))-m*m)
m,s=stats(xs)
def test(fE,fS): return all(eq(stats([a*x+b for x in xs])[0],fE(a,b)) and eq(stats([a*x+b for x in xs])[1],fS(a,b)) for a,b in ((10,-5),(F(1,2),3),(3,7)))
setq(83,"تحويل المتغيّرات العشوائية (2)",5,'R',"توقّع س يساوى م وانحرافه المعيارى ع. إذا كان ص = أ س + ب (أ > 0) فإن توقّع ص وانحرافه المعيارى على الترتيب:",
 ["أ م ، أ ع + ب","أ م + ب ، أ ع + ب","أ م + ب ، أ ع","أ م + ب ، أ^2 ع"],2,
 "الثابت ب يزيح التوقّع فقط، والضرب فى أ يضرب التوقّع والانحراف المعيارى فى أ.",
 [test(lambda a,b:a*m,lambda a,b:a*s+b), test(lambda a,b:a*m+b,lambda a,b:a*s+b), test(lambda a,b:a*m+b,lambda a,b:a*s), test(lambda a,b:a*m+b,lambda a,b:a*a*s)])

# ================= validation & output =================
pos=Counter(); bad=[]
for i,k in enumerate(K):
    qs=by[k]; assert len(qs)==6,(i,len(qs))
    c=Counter(q['a'] for q in qs)
    if max(c.values())>2 or len(c)<4: bad.append((i,dict(c)))
    for j,q in enumerate(qs):
        assert set(q)-{'chg'}=={'q','o','a','e'} and len(q['o'])==4==len(set(q['o'])) and q['a'] in range(4)
        L=[len(x) for x in q['o']]
        if L[q['a']]>max(l for t,l in enumerate(L) if t!=q['a']): print('NOTE longest correct (untouched input)',i,j) if not q.get('chg') else exit('longest')
        assert 'السؤال السابق' not in q['q'], (i,j)
        pos[q['a']]+=1
    assert len({q['q'] for q in qs})==6,(i,'dup')
assert not bad, bad
def tot(S): c=Counter(''.join(S)); return (c['R'],c['U'],c['A'])
ex=lambda S:sum(1 for s in S if sorted(Counter(s).get(x,0) for x in 'RUA')==[2,2,2])
weak=lambda S:[i for i,s in enumerate(S) if s.count('U')<2 or s.count('A')<1 or s.count('R')<1 or max(Counter(s).values())>3]
json.dump({"by":by},open(OUT,'w'),ensure_ascii=False,indent=1)
d=json.load(open(OUT)); assert len(d['by'])==89 and list(d['by'])==K
print('lessons',len(d['by']),'questions',sum(len(v) for v in d['by'].values()))
print('mix R/U/A before',tot(BEFORE),'after',tot(AFTER))
print('lessons exactly 2/2/2: before',ex(BEFORE),'after',ex(AFTER),'| outside tolerance: before',len(weak(BEFORE)),'after',weak(AFTER))
print('changed',NCHG,'chg flags',sum(1 for v in d['by'].values() for q in v if q.get('chg')),'positions',dict(pos))
