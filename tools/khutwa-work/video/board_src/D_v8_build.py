# بناء السبورة D (v8، قالب ركن الامتحان) — اتقسمت لملفين:
#   khutwa_hist_board_D.html  = D1 + أسئلة ص١٨–١٩ (D2–D4)
#   khutwa_hist_board_D2.html = الأسئلة المقالية ص٢٠ (D5) + لوحات الحفظ D6 + الختام D7 + الدرس في دقيقة + التوقيع
# المصادر: hist_final_v5.md (D1، D6، D7) + hist_memory_v2.md (RD، D7.2m، الخطة) + hist_l1_plot_v6.md (D2–D5 بالقالب، وD6.2)
import re,json,sys,os
V='/home/claude/secondary-application-/tools/khutwa-work/video/'
T='/home/claude/out/tools/'
v=open('/home/claude/khutwa/video/hist_final_v5.md',encoding='utf-8').read()
sec=v.split('## BOARD D')[1].split('\n## ')[0]
S={};SRC={}
AR=str.maketrans('0123456789','٠١٢٣٤٥٦٧٨٩')
def src(x):
    if 'العنوان' in x: return 'عنوان الدرس الجاي'
    x=re.sub(r'\(v4[^)]*\)','',x)
    x=x.replace('(','').replace(')','').replace('—','').strip()
    if 'ص' in x: x='الكتاب '+x
    return x.translate(AR)
KEEP=re.compile(r'^D(1\.\d|6\.\d|7\.\d+[a-d]?)$')
for l in sec.splitlines():
    c=[x.strip() for x in l.split('|')]
    if len(c)>3 and re.match(r'^D\d\.\d+[a-d]?$',c[1]) and KEEP.match(c[1]): S[c[1]]=c[2];SRC[c[1]]=src(c[4])
m=open('/home/claude/khutwa/video/hist_memory_v2.md',encoding='utf-8').read().split('## BOARD D')[1]
PLAN=[]
for l in m.splitlines():
    c=[x.strip() for x in l.split('|')]
    if len(c)>3 and re.match(r'^RD\d$',c[1]): S[c[1]]=c[2];SRC[c[1]]='مراجعة'
    if len(c)>6 and c[1].startswith('**الإجابة الكاملة'):
        assert c[5]!='مرسوم بس'; S['D7.2m']=c[5];SRC['D7.2m']='رابط حفظ'
    if len(c)>4 and c[1].startswith('☐'): PLAN.append([c[1].replace('☐','').strip(),c[2],c[3]])
# v6: قالب ركن الامتحان
md=open(V+'hist_l1_plot_v6.md',encoding='utf-8').read()
d6=md.split('### السبورة D (ركن')[1].split('## (ج)')[0]
PG={'D2':'ص١٨','D3':'ص١٩','D4':'ص١٩','D5':'ص٢٠'}
n6=0
for l in d6.splitlines():
    c=[x.strip() for x in l.split('|')]
    if len(c)>5 and re.match(r'^D\d\.\d+[a]?(-[سحج])?$',c[1]):
        k=c[1];t=c[3];assert t and t not in ('زي ما هو.','—'),k
        S[k]=t;n6+=1
        if k=='D6.2': continue
        if k.endswith('-ح'): SRC[k]='طريقة الحل'
        elif k.endswith('-ج'):
            pg=re.findall(r'ص(\d+)',c[4]); SRC[k]=('اجتهاد · الكتاب '+'، '.join('ص'+p for p in pg)).translate(AR)
        else: SRC[k]='الكتاب '+PG[k[:2]]
assert n6==73,n6
print('lines',len(S))
if len(sys.argv)>1:
    for k,t in S.items(): print(k,'|',SRC.get(k),'|',t)
    sys.exit()
# تنويه تطبيق خُطوة (نفس روح البرومو promo/script.md ص٥٠–٥١) — نص موحّد في آخر كل درس قبل التوقيع
APP='وعشان تعرف إنت وصلت لفين في المنهج، وتراجع الدرس ده في وقته: حمّل تطبيق خُطوة. [[0.3]] مجاني، واللينك تحت الفيديو. [[0.3]] الثانوية مش قفزة. [[0.3]] الثانوية سلّم. [[0.3]] ابدأ النهارده بخُطوة واحدة.'
tpl=open('/home/claude/out/board_template.html',encoding='utf-8').read()
def build(out,parts,title,note,H,extra=None):
    S2=dict(S);SRC2=dict(SRC)
    for k,v in (extra or {}).items(): S2[k]=v;SRC2[k]=''
    body=''.join(open(T+f,encoding='utf-8').read()+'\n' for f in parts)
    t=tpl
    a=t.index('/*__CONTENT_START__');b=t.index('/*__CONTENT_END__*/')+len('/*__CONTENT_END__*/')
    t=t[:a]+'/*__CONTENT_START__*/\nconst SP='+json.dumps(S2,ensure_ascii=False)+',SRC='+json.dumps(SRC2,ensure_ascii=False)+',PLAN='+json.dumps(PLAN,ensure_ascii=False)+';\n'+body+'\n/*__CONTENT_END__*/'+t[b:]
    t,n1=re.subn(r'<title>.*?</title>','<title>'+title+'</title>',t)
    t,n2=re.subn(r'<p id="note">نسخة v7 · الافتتاحية A0 \+ الشرايح A1–A3 \(السكريبت v3 \+ تبسيط v4\)\.','<p id="note">'+note,t)
    t,n3=re.subn(r'<rect y="-1800" width="3200" height="3600"','<rect y="-1800" width="3200" height="%d"'%H,t)
    assert (n1,n2,n3)==(1,1,2),(n1,n2,n3)
    t,n4=re.subn(r"if\(l!==curL\)\{curL=l;","if(l!==curL){curL=l;$('#sub').style.fontSize=l&&l.tk.length>48?'.56em':l&&l.tk.length>36?'.64em':l&&l.tk.length>27?'.74em':l&&l.tk.length>21?'.88em':'';",t)
    t,n5=re.subn(r"#world text\{font-family:Lalezar,Cairo,Tahoma,sans-serif\}","#world text{font-family:Lalezar,Cairo,Tahoma,sans-serif;text-rendering:geometricPrecision}",t)
    # باتش التعليم: عنصر نص عليه hl بيتلوّن (وبيتخط تحته/بيتشطب) من لحظة hl
    t,n6=re.subn(r"(if\(it\.off!=null\)it\.e\.setAttribute\('opacity',1-sm\(\(T-it\.off\)/\.4\)\);)(it\.r\.setAttribute\('y',b\.y-6\))",
        r"\1if(it.hl!=null){const on=T>=it.hl;it.e.setAttribute('fill',on?it.hc:it.col);it.e.setAttribute('text-decoration',on&&it.hd?it.hd:'none')}\2",t)
    assert (n4,n5,n6)==(1,1,1),(n4,n5,n6)
    open('/home/claude/out/'+out,'w',encoding='utf-8').write(t);print('built',out)
build('khutwa_hist_board_D.html',['D_v8_h.js','D_v8_d1.js'],'خُطوة · تاريخ · نسخة v8 · السبورة D (ركن الامتحان ١: D1 + أسئلة ص١٨–١٩)',
      'نسخة v8 · السبورة D (الفصل الرابع، الجزء ١): افتتاح الفصل D1 + أسئلة الدرس ص١٨–١٩ على «قالب ركن الامتحان»: السؤال بنصه ← طريقة الحل ← الإجابة النموذجية (مراجعة الحبكة v6). الجزء ٢ في khutwa_hist_board_D2.html.',5600)
if os.path.exists(T+'D_v8_d2.js'):
    build('khutwa_hist_board_D2.html',['D_v8_h.js','D_v8_d2.js','APP_card.js'],'خُطوة · تاريخ · نسخة v8 · السبورة D2 (ركن الامتحان ٢: المقال ص٢٠ + لوحات الحفظ + الختام)',
      'نسخة v8 · السبورة D2 (الفصل الرابع، الجزء ٢): الأسئلة المقالية ص٢٠ على «قالب ركن الامتحان» + لوحات «احفظ دي» التلاتة + إجابة سؤال الدرس + الدرس في دقيقة + الختام وتنويه تطبيق خُطوة والتوقيع.',7600,
      {'D5.0':'إنت هنا: كمّلنا ركن الامتحان. [[0.3]] فاضل أسئلة صفحة عشرين، ولوحات الحفظ، والختام. [[0.3]] جهّز ورقة وقلم، ونبدأ.',
       'APP':APP})
