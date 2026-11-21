import re,json,sys
V='/home/claude/secondary-application-/tools/khutwa-work/video/'
md=open(V+'hist_l2_script_v1.md',encoding='utf-8').read()
sec=md.split('## BOARD L2C')[1].split('### كروت الحفظ — L2C')[0]
rc=md.split('### دقيقة المراجعة RC')[1].split('\n---')[0]
S={};SRC={}
AR=str.maketrans('0123456789','٠١٢٣٤٥٦٧٨٩')
def src(x):
    x=x.strip()
    if x in ('—',''): return ''
    x=x.replace('(','').replace(')','').replace('درس 1','الدرس ١').replace('المنهج + ص31','المنهج + الكتاب ص31')
    if 'ص' in x and not x.startswith('المنهج'): x='الكتاب '+x
    return x.translate(AR)
for l in sec.splitlines():
    c=[x.strip() for x in l.split('|')]
    if len(c)>4 and re.match(r'^2C\.\d+$',c[1]): S[c[1]]=c[2];SRC[c[1]]=src(c[4])
for l in rc.splitlines():
    c=[x.strip() for x in l.split('|')]
    if len(c)>3 and re.match(r'^RC\d+$',c[1]): S[c[1]]=c[2];SRC[c[1]]='مراجعة'
assert len(S)==67,len(S)
if len(sys.argv)>1:
    for k,t in S.items(): print(k,'|',SRC[k],'|',t)
    sys.exit()
t=open(V+'board_template.html',encoding='utf-8').read()
body=''.join(open('/home/claude/out/tools/L2C_p%d.js'%i,encoding='utf-8').read()+'\n' for i in range(5))
a=t.index('/*__CONTENT_START__');b=t.index('/*__CONTENT_END__*/')+len('/*__CONTENT_END__*/')
t=t[:a]+'/*__CONTENT_START__*/\nconst S='+json.dumps(S,ensure_ascii=False)+',SRC='+json.dumps(SRC,ensure_ascii=False)+';\n'+body+'\n/*__CONTENT_END__*/'+t[b:]
t,n1=re.subn(r'<title>.*?</title>','<title>خُطوة · تاريخ · الدرس ٢ · السبورة L2C (الفصل ٣ · الرومان والمقاومة ودرس الدرس والختام)</title>',t)
t,n2=re.subn(r'<p id="note">نسخة v7 · الافتتاحية A0 \+ الشرايح A1–A3 \(السكريبت v3 \+ تبسيط v4\)\.','<p id="note">نسخة v1 · السبورة L2C (الدرس ٢ · الفصل ٣ · الرومان والمقاومة، ودرس الدرس، والمراجعة والختام).',t)
H=11400
t,n3=re.subn(r'<rect y="-1800" width="3200" height="3600"','<rect y="-1800" width="3200" height="%d"'%H,t)
assert (n1,n2,n3)==(1,1,2),(n1,n2,n3)
t,n4=re.subn(r"if\(l!==curL\)\{curL=l;","if(l!==curL){curL=l;$('#sub').style.fontSize=l&&l.tk.length>27?'.74em':l&&l.tk.length>21?'.88em':'';",t)
assert n4==1
open('/home/claude/out/khutwa_hist_board_L2C.html','w',encoding='utf-8').write(t)
print('built',len(S))
