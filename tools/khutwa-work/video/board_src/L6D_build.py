# السبورة L6D: آخر الدرس ٦ = ركن التدريبات (6C.37z–6C.45d-ج) + الكروت ٢٦–٢٨ + دقيقة المراجعة RC + الختام وتنويه التطبيق والتوقيع
import re,json,sys,glob
V='/home/claude/secondary-application-/tools/khutwa-work/video/'
md=open(V+'hist_l6_script_v1.md',encoding='utf-8').read()
sec=md.split('## BOARD L6C')[1].split('### كروت الحفظ — L6C')[0]
rc=md.split('### دقيقة المراجعة RC')[1].split('\n---')[0]
S={};SRC={}
AR=str.maketrans('0123456789','٠١٢٣٤٥٦٧٨٩')
def src(x):
    x=x.strip()
    if x in ('—',''): return ''
    out=[]
    for p in x.replace('(','').replace(')','').split('+'):
        p=p.strip()
        p=re.sub(r'درس (\d)',r'الدرس \1',p)
        p=re.sub(r'(?<![؀-ۿ])ص(\d)',r'الكتاب ص\1',p)
        out.append(p)
    r=' + '.join(out)
    i=r.find('الكتاب ')
    if i>=0: r=r[:i+7]+r[i+7:].replace('الكتاب ','')
    return r.translate(AR)
on=False
for l in sec.splitlines():
    c=[x.strip() for x in l.split('|')]
    if len(c)>4 and re.match(r'^(6C\.\d+[a-z]?(-[سحجك])?|APP)$',c[1]):
        if c[1]=='6C.37z': on=True
        if on: S[c[1]]=c[2];SRC[c[1]]=src(c[4])
for l in rc.splitlines():
    c=[x.strip() for x in l.split('|')]
    if len(c)>3 and re.match(r'^RC\d+$',c[1]): S[c[1]]=c[2];SRC[c[1]]='مراجعة'
for k in S:
    if k.endswith('-ح'): SRC[k]='طريقة الحل'
assert len(S)==58,len(S)
if len(sys.argv)>1:
    for k,t in S.items(): print(k,'|',SRC[k],'|',t)
    sys.exit()
t=open(V+'board_template.html',encoding='utf-8').read()
body=''.join(open(f,encoding='utf-8').read()+'\n' for f in sorted(glob.glob('/home/claude/out/tools/L6D_p[0-9].js')))+open('/home/claude/out/tools/APP_card.js',encoding='utf-8').read()+'\n'
a=t.index('/*__CONTENT_START__');b=t.index('/*__CONTENT_END__*/')+len('/*__CONTENT_END__*/')
t=t[:a]+'/*__CONTENT_START__*/\nconst S='+json.dumps(S,ensure_ascii=False)+',SRC='+json.dumps(SRC,ensure_ascii=False)+';\n'+body+'\n/*__CONTENT_END__*/'+t[b:]
t,n1=re.subn(r'<title>.*?</title>','<title>خُطوة · تاريخ · الدرس ٦ · السبورة L6D (ركن التدريبات + المراجعة + الختام)</title>',t)
t,n2=re.subn(r'<p id="note">نسخة v7 · الافتتاحية A0 \+ الشرايح A1–A3 \(السكريبت v3 \+ تبسيط v4\)\.','<p id="note">نسخة v1 · السبورة L6D (الدرس ٦ · ركن التدريبات ص٧١–٧٢ على «قالب ركن الامتحان»: السؤال ← طريقة الحل ← الإجابة، والكروت ٢٦–٢٨، ودقيقة المراجعة RC، والختام وتنويه تطبيق خُطوة والتوقيع).',t)
H=9000
t,n3=re.subn(r'<rect y="-1800" width="3200" height="3600"','<rect y="-1800" width="3200" height="%d"'%H,t)
assert (n1,n2,n3)==(1,1,2),(n1,n2,n3)
t,n4=re.subn(r"if\(l!==curL\)\{curL=l;","if(l!==curL){curL=l;$('#sub').style.fontSize=l&&l.tk.length>48?'.56em':l&&l.tk.length>36?'.64em':l&&l.tk.length>27?'.74em':l&&l.tk.length>21?'.88em':'';",t)
t,n5=re.subn(r"#world text\{font-family:Lalezar,Cairo,Tahoma,sans-serif\}","#world text{font-family:Lalezar,Cairo,Tahoma,sans-serif;text-rendering:geometricPrecision}",t)
# باتش التعليم (من D_v8): عنصر نص عليه hl بيتلوّن (وبيتخط تحته/بيتشطب) من لحظة hl
t,n6=re.subn(r"(if\(it\.off!=null\)it\.e\.setAttribute\('opacity',1-sm\(\(T-it\.off\)/\.4\)\);)(it\.r\.setAttribute\('y',b\.y-6\))",
    r"\1if(it.hl!=null){const on=T>=it.hl;it.e.setAttribute('fill',on?it.hc:it.col);it.e.setAttribute('text-decoration',on&&it.hd?it.hd:'none')}\2",t)
assert (n4,n5,n6)==(1,1,1),(n4,n5,n6)
open('/home/claude/out/khutwa_hist_board_L6D.html','w',encoding='utf-8').write(t)
print('built',len(S))
