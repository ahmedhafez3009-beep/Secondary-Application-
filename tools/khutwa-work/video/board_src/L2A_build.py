import re,json,sys
V='/home/claude/secondary-application-/tools/khutwa-work/video/'
v=open(V+'hist_l2_script_v1.md',encoding='utf-8').read()
sec=v.split('## BOARD L2A')[1].split('### كروت الحفظ — L2A')[0]
ra=v.split('### دقيقة المراجعة RA')[1].split('## BOARD L2B')[0]
S={};SRC={}
AR=str.maketrans('0123456789','٠١٢٣٤٥٦٧٨٩')
def src(x):
    x=x.replace('(','').replace(')','').replace('—','–').strip()
    x=x.replace('(تشبيه) لـ ص22','تشبيه توضيحي · ص22').replace('درس 1','الدرس الأول')
    if 'ص' in x: x='الكتاب '+x
    return x.translate(AR)
for l in sec.splitlines():
    c=[x.strip() for x in l.split('|')]
    if len(c)>5 and re.match(r'^2A\.\d+$',c[1]): S[c[1]]=c[2];SRC[c[1]]=src(c[4])
for l in ra.splitlines():
    c=[x.strip() for x in l.split('|')]
    if len(c)>4 and re.match(r'^RA\d$',c[1]): S[c[1]]=c[2]
if len(sys.argv)>1:
    for k,t in S.items(): print(k,'|',SRC.get(k),'|',t)
    sys.exit()
print(len(S),file=sys.stderr)
t=open(V+'board_template.html',encoding='utf-8').read()
body=open(V+'board_src/L2A_content.js',encoding='utf-8').read()
a=t.index('/*__CONTENT_START__');b=t.index('/*__CONTENT_END__*/')+len('/*__CONTENT_END__*/')
t=t[:a]+'/*__CONTENT_START__*/\nconst S='+json.dumps(S,ensure_ascii=False)+',SRC='+json.dumps(SRC,ensure_ascii=False)+';\n'+body+'\n/*__CONTENT_END__*/'+t[b:]
t,n1=re.subn(r'<title>.*?</title>','<title>خُطوة · تاريخ · الدرس ٢ · السبورة L2A (الفصل الأول · ص٢١–٢٤)</title>',t)
t,n2=re.subn(r'<p id="note">نسخة v7 · الافتتاحية A0 \+ الشرايح A1–A3 \(السكريبت v3 \+ تبسيط v4\)\.','<p id="note">نسخة v1 · السبورة L2A (الدرس ٢ · الفصل الأول · ص٢١–٢٤).',t)
H=8400
t,n3=re.subn(r'<rect y="-1800" width="3200" height="3600"','<rect y="-1800" width="3200" height="%d"'%H,t)
assert (n1,n2,n3)==(1,1,2),(n1,n2,n3)
open('/home/claude/out/khutwa_hist_board_L2A.html','w',encoding='utf-8').write(t)
print('built',len(S))
