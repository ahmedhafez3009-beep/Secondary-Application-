import re,json,sys
v=open('/home/claude/khutwa/video/hist_final_v5.md',encoding='utf-8').read()
sec=v.split('## BOARD C')[1].split('## BOARD D')[0]
S={};SRC={}
AR=str.maketrans('0123456789','٠١٢٣٤٥٦٧٨٩')
def src(x):
    x=x.replace('(','').replace(')','').replace('—','').strip()
    x=re.sub(r'قرار 4 في v3','',x).strip()
    x=re.sub(r'ص(\d)',r'ص\1',x)
    if 'ص' in x: x='الكتاب '+x
    return x.translate(AR)
for l in sec.splitlines():
    c=[x.strip() for x in l.split('|')]
    if len(c)>3 and re.match(r'^C\d\.\d+a?$',c[1]): S[c[1]]=c[2];SRC[c[1]]=src(c[4])
m=open('/home/claude/khutwa/video/hist_memory_v2.md',encoding='utf-8').read().split('## BOARD C')[1].split('## BOARD D')[0]
MEM=[('**16.','C4.2m'),('**اقتباس حمدان (1)','C2.7m'),('**قَسَم كتاب الموتى','C2.17m'),('**20.','C3.8m'),('**21.','C3.12m'),('**22ب.','C3.19m'),('**23.','C3.23m')]
for l in m.splitlines():
    c=[x.strip() for x in l.split('|')]
    if len(c)>3 and re.match(r'^RC\d$',c[1]): S[c[1]]=c[2]
    if len(c)>6:
        for k,i in MEM:
            if c[1].startswith(k):
                assert c[5]!='مرسوم بس',c[1]; S[i]=c[5]
print(len(S),file=sys.stderr)
if len(sys.argv)>1:
    for k,t in S.items(): print(k,'|',SRC.get(k),'|',t)
    sys.exit()
t=open('/home/claude/out/board_template.html',encoding='utf-8').read()
body=open('/home/claude/out/tools/C_content.js',encoding='utf-8').read()
a=t.index('/*__CONTENT_START__');b=t.index('/*__CONTENT_END__*/')+len('/*__CONTENT_END__*/')
t=t[:a]+'/*__CONTENT_START__*/\nconst S='+json.dumps(S,ensure_ascii=False)+',SRC='+json.dumps(SRC,ensure_ascii=False)+';\n'+body+'\n/*__CONTENT_END__*/'+t[b:]
t,n1=re.subn(r'<title>.*?</title>','<title>خُطوة · تاريخ · نسخة v1 · السبورة C (الفصل الثالث · الشرايح C1–C4)</title>',t)
t,n2=re.subn(r'<p id="note">نسخة v7 · الافتتاحية A0 \+ الشرايح A1–A3 \(السكريبت v3 \+ تبسيط v4\)\.','<p id="note">نسخة v1 · السبورة C (الفصل الثالث · الشرايح C1–C4).',t)
H=7300
t,n3=re.subn(r'<rect y="-1800" width="3200" height="3600"','<rect y="-1800" width="3200" height="%d"'%H,t)
assert (n1,n2,n3)==(1,1,2),(n1,n2,n3)
open('/home/claude/out/khutwa_hist_board_C.html','w',encoding='utf-8').write(t)
print('built',len(S))
