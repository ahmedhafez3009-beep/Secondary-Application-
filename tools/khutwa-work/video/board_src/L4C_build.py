import re,json,sys
V='/home/claude/secondary-application-/tools/khutwa-work/video/'
md=open(V+'hist_l4_script_v1.md',encoding='utf-8').read()
sec=md.split('## BOARD L4C')[1].split('### كروت الحفظ — L4C')[0]
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
for l in sec.splitlines():
    c=[x.strip() for x in l.split('|')]
    if len(c)>4 and re.match(r'^4C\.\d+$',c[1]): S[c[1]]=c[2];SRC[c[1]]=src(c[4])
for l in rc.splitlines():
    c=[x.strip() for x in l.split('|')]
    if len(c)>3 and re.match(r'^RC\d+$',c[1]): S[c[1]]=c[2];SRC[c[1]]='مراجعة'
assert len(S)==71,len(S)
if len(sys.argv)>1:
    for k,t in S.items(): print(k,'|',SRC[k],'|',t)
    sys.exit()
NP=6
t=open(V+'board_template.html',encoding='utf-8').read()
import glob
body=''.join(open(f,encoding='utf-8').read()+'\n' for f in sorted(glob.glob('/home/claude/out/tools/L4C_p[0-9].js')))
a=t.index('/*__CONTENT_START__');b=t.index('/*__CONTENT_END__*/')+len('/*__CONTENT_END__*/')
t=t[:a]+'/*__CONTENT_START__*/\nconst S='+json.dumps(S,ensure_ascii=False)+',SRC='+json.dumps(SRC,ensure_ascii=False)+';\n'+body+'\n/*__CONTENT_END__*/'+t[b:]
t,n1=re.subn(r'<title>.*?</title>','<title>خُطوة · تاريخ · الدرس ٤ · السبورة L4C (الفصل ٣ · العقل والمكانة، ولمّة الوحدة الأولى والختام)</title>',t)
t,n2=re.subn(r'<p id="note">نسخة v7 · الافتتاحية A0 \+ الشرايح A1–A3 \(السكريبت v3 \+ تبسيط v4\)\.','<p id="note">نسخة v1 · السبورة L4C (الدرس ٤ · الفصل ٣ · العقل والمكانة، وتدريبات الدرس، ولمّة الوحدة الأولى وتقييمها الختامي، ودقيقة المراجعة RC والختام).',t)
H=15600
t,n3=re.subn(r'<rect y="-1800" width="3200" height="3600"','<rect y="-1800" width="3200" height="%d"'%H,t)
assert (n1,n2,n3)==(1,1,2),(n1,n2,n3)
t,n4=re.subn(r"if\(l!==curL\)\{curL=l;","if(l!==curL){curL=l;$('#sub').style.fontSize=l&&l.tk.length>27?'.74em':l&&l.tk.length>21?'.88em':'';",t)
assert n4==1
# patch: مقاسات النص ثابتة مهما كان الزووم (علشان الزووم الأخير على ٢٠ صف ما يغيّرش عرض الكلمات)
t,n5=re.subn(r"#world text\{font-family:Lalezar,Cairo,Tahoma,sans-serif\}","#world text{font-family:Lalezar,Cairo,Tahoma,sans-serif;text-rendering:geometricPrecision}",t)
assert n5==1
open('/home/claude/out/khutwa_hist_board_L4C.html','w',encoding='utf-8').write(t)
print('built',len(S))
