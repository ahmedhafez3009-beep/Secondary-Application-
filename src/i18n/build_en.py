import re,json,glob,importlib,sys,os
here=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,here)
P=[];PFX=[]
for f in sorted(glob.glob(here+'/en_pairs_*.py')):
    m=importlib.import_module(os.path.basename(f)[:-3]); P+=m.P; PFX+=getattr(m,'PFX',[])
MON="يناير فبراير مارس أبريل مايو يونيو يوليو أغسطس سبتمبر أكتوبر نوفمبر ديسمبر".split()
MON_EN="Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
DAY="الأحد الاثنين الثلاثاء الأربعاء الخميس الجمعة السبت".split()
DAY_EN="Sun Mon Tue Wed Thu Fri Sat".split()
TOK=dict(zip(MON,MON_EN)); TOK.update(dict(zip(DAY,DAY_EN))); TOK.update({"إبريل":"Apr","الاتنين":"Mon","التلات":"Tue","الأربع":"Wed"})
NAMES=["مريم","يوسف","سارة","سلمى","نور","x"]
tre=re.compile(r'(?<![؀-ۿ])('+'|'.join(sorted(TOK,key=len,reverse=True))+r')(?![؀-ۿ])')
def key(s):
    s=s.strip()
    for n in NAMES: s=re.sub(r'(?<![؀-ۿa-z])'+n+r'(?![؀-ۿa-z])','{N}',s)
    s=s.replace('بطلتنا','{N}').replace('بطلنا','{N}')
    s=re.sub(r'[0-9٠-٩]+(?:[.,][0-9٠-٩]+)?','#',s)
    return tre.sub('@',s)
import itertools
def expand(s):
    parts=re.split(r'(\[[^\]|]*\|[^\]]*\]|<[^>|]*\|[^>]*>)',s); opts=[]
    for x in parts:
        if re.fullmatch(r'\[[^\]|]*\|[^\]]*\]|<[^>|]*\|[^>]*>',x): opts.append(x[1:-1].split('|'))
        else: opts.append([x])
    return {''.join(c) for c in itertools.product(*opts)}
D={}
for a0,e in P:
  for a in expand(a0):
    k=key(a)
    if k in D and D[k]!=e: print('dup',k,'|',D[k],'|',e,file=sys.stderr)
    D[k]=e
Q=json.load(open(here+'/quotes_en.json',encoding='utf8')) if os.path.exists(here+'/quotes_en.json') else {}
out="var I18N_EN = "+json.dumps(D,ensure_ascii=False)+";\nvar I18N_PFX = "+json.dumps(PFX,ensure_ascii=False)+";\nvar I18N_TOK = "+json.dumps(TOK,ensure_ascii=False)+";\nvar I18N_Q = "+json.dumps(Q,ensure_ascii=False)+";\n"
open(os.path.join(here,'..','i18n_en.js'),'w',encoding='utf8').write(out)
print(len(D),'keys')
