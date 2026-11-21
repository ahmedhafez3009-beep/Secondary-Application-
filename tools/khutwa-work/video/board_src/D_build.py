import re,json,sys
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
for l in sec.splitlines():
    c=[x.strip() for x in l.split('|')]
    if len(c)>3 and re.match(r'^D\d\.\d+[a-d]?$',c[1]): S[c[1]]=c[2];SRC[c[1]]=src(c[4])
m=open('/home/claude/khutwa/video/hist_memory_v2.md',encoding='utf-8').read().split('## BOARD D')[1]
MEM=[('**أدلة سؤال التفسير','D2.6m'),('**العلاقات الأربعة','D5.8m'),('**الإجابة الكاملة','D7.2m')]
for l in m.splitlines():
    c=[x.strip() for x in l.split('|')]
    if len(c)>3 and re.match(r'^RD\d$',c[1]): S[c[1]]=c[2];SRC[c[1]]='مراجعة'
    if len(c)>6:
        for k,i in MEM:
            if c[1].startswith(k):
                assert c[5]!='مرسوم بس',c[1]; S[i]=c[5];SRC[i]='رابط حفظ'
    if len(c)>4 and c[1].startswith('☐'): S.setdefault('PLAN',[]).append([c[1].replace('☐','').strip(),c[2],c[3]])
assert len(S)==58+9+3+1,len(S)
if len(sys.argv)>1:
    for k,t in S.items(): print(k,'|',SRC.get(k),'|',t)
    sys.exit()
t=open('/home/claude/out/board_template.html',encoding='utf-8').read()
body=''.join(open('/home/claude/out/tools/D_p%d.js'%i,encoding='utf-8').read()+'\n' for i in range(3))
a=t.index('/*__CONTENT_START__');b=t.index('/*__CONTENT_END__*/')+len('/*__CONTENT_END__*/')
PLAN=S.pop('PLAN')
t=t[:a]+'/*__CONTENT_START__*/\nconst SP='+json.dumps(S,ensure_ascii=False)+',SRC='+json.dumps(SRC,ensure_ascii=False)+',PLAN='+json.dumps(PLAN,ensure_ascii=False)+';\n'+body+'\n/*__CONTENT_END__*/'+t[b:]
t,n1=re.subn(r'<title>.*?</title>','<title>خُطوة · تاريخ · نسخة v1 · السبورة D (الفصل الرابع · الشرايح D1–D7)</title>',t)
t,n2=re.subn(r'<p id="note">نسخة v7 · الافتتاحية A0 \+ الشرايح A1–A3 \(السكريبت v3 \+ تبسيط v4\)\.','<p id="note">نسخة v1 · السبورة D (الفصل الرابع · الشرايح D1–D7).',t)
t,n3=re.subn(r'<rect y="-1800" width="3200" height="3600"','<rect y="-1800" width="3200" height="8300"',t)
assert (n1,n2,n3)==(1,1,2),(n1,n2,n3)
open('/home/claude/out/khutwa_hist_board_D.html','w',encoding='utf-8').write(t)
print('built',len(S))
