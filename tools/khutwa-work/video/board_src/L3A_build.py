import re,json,sys
V='/home/claude/secondary-application-/tools/khutwa-work/video/'
md=open(V+'hist_l3_script_v1.md',encoding='utf-8').read()
sec=md.split('## BOARD L3A')[1].split('### كروت الحفظ — L3A')[0]
ra=md.split('### دقيقة المراجعة RA')[1].split('\n---')[0]
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
    if len(c)>4 and re.match(r'^3A\.\d+$',c[1]): S[c[1]]=c[2];SRC[c[1]]=src(c[4])
for l in ra.splitlines():
    c=[x.strip() for x in l.split('|')]
    if len(c)>3 and re.match(r'^RA\d+$',c[1]): S[c[1]]=c[2];SRC[c[1]]='مراجعة'
assert len(S)==66,len(S)
import os
if os.environ.get('ONLY'):
    pass
if len(sys.argv)>1:
    for k,t in S.items(): print(k,'|',SRC[k],'|',t)
    sys.exit()
NP=5
t=open(V+'board_template.html',encoding='utf-8').read()
body=''.join(open('/home/claude/out/tools/L3A_p%d.js'%i,encoding='utf-8').read()+'\n' for i in range(NP))
a=t.index('/*__CONTENT_START__');b=t.index('/*__CONTENT_END__*/')+len('/*__CONTENT_END__*/')
t=t[:a]+'/*__CONTENT_START__*/\nconst S='+json.dumps(S,ensure_ascii=False)+',SRC='+json.dumps(SRC,ensure_ascii=False)+';\n'+body+'\n/*__CONTENT_END__*/'+t[b:]
t,n1=re.subn(r'<title>.*?</title>','<title>خُطوة · تاريخ · الدرس ٣ · السبورة L3A (الفصل ١ · من ولاية لمركز قيادي: التحول السياسي والاجتماعي)</title>',t)
t,n2=re.subn(r'<p id="note">نسخة v7 · الافتتاحية A0 \+ الشرايح A1–A3 \(السكريبت v3 \+ تبسيط v4\)\.','<p id="note">نسخة v1 · السبورة L3A (الدرس ٣ · الفصل ١ · التحول السياسي والاجتماعي، ودقيقة المراجعة RA).',t)
H=10200
t,n3=re.subn(r'<rect y="-1800" width="3200" height="3600"','<rect y="-1800" width="3200" height="%d"'%H,t)
assert (n1,n2,n3)==(1,1,2),(n1,n2,n3)
t,n4=re.subn(r"if\(l!==curL\)\{curL=l;","if(l!==curL){curL=l;$('#sub').style.fontSize=l&&l.tk.length>27?'.74em':l&&l.tk.length>21?'.88em':'';",t)
assert n4==1
open('/home/claude/out/khutwa_hist_board_L3A.html','w',encoding='utf-8').write(t)
print('built',len(S))
