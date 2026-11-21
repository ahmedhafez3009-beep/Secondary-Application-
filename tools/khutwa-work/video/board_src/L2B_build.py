import re,json,sys
md=open('/home/claude/khutwa/video/hist_l2_script_v1.md',encoding='utf-8').read()
sec=md.split('## BOARD L2B')[1].split('### كروت الحفظ — L2B')[0]
rb=md.split('### دقيقة المراجعة RB')[1].split('\n---')[0]
S={};SRC={}
AR=str.maketrans('0123456789','٠١٢٣٤٥٦٧٨٩')
def src(x):
    m=re.search(r'ص[\d–]+',x)
    r='الكتاب '+m.group(0).translate(AR) if m else ''
    if 'درس 1' in x: r+=' + الدرس ١'
    return r or 'الكتاب'
for l in sec.splitlines():
    c=[x.strip() for x in l.split('|')]
    if len(c)>4 and re.match(r'^2B\.\d+$',c[1]): S[c[1]]=c[2];SRC[c[1]]=src(c[4])
for l in rb.splitlines():
    c=[x.strip() for x in l.split('|')]
    if len(c)>3 and re.match(r'^RB\d$',c[1]): S[c[1]]=c[2];SRC[c[1]]='مراجعة'
assert len(S)==50,len(S)
if len(sys.argv)>1:
    for k,t in S.items(): print(k,'|',SRC[k],'|',t)
    sys.exit()
t=open('/home/claude/out/board_template.html',encoding='utf-8').read()
body=''.join(open('/home/claude/out/tools/L2B_p%d.js'%i,encoding='utf-8').read()+'\n' for i in range(5))
a=t.index('/*__CONTENT_START__');b=t.index('/*__CONTENT_END__*/')+len('/*__CONTENT_END__*/')
t=t[:a]+'/*__CONTENT_START__*/\nconst S='+json.dumps(S,ensure_ascii=False)+',SRC='+json.dumps(SRC,ensure_ascii=False)+';\n'+body+'\n/*__CONTENT_END__*/'+t[b:]
t,n1=re.subn(r'<title>.*?</title>','<title>خُطوة · تاريخ · الدرس ٢ · السبورة L2B (الفصل ٢ · الفرس والإسكندر والبطالمة)</title>',t)
t,n2=re.subn(r'<p id="note">نسخة v7 · الافتتاحية A0 \+ الشرايح A1–A3 \(السكريبت v3 \+ تبسيط v4\)\.','<p id="note">نسخة v1 · السبورة L2B (الدرس ٢ · الفصل ٢ · الفرس والإسكندر والبطالمة).',t)
H=8300
t,n3=re.subn(r'<rect y="-1800" width="3200" height="3600"','<rect y="-1800" width="3200" height="%d"'%H,t)
assert (n1,n2,n3)==(1,1,2),(n1,n2,n3)
t,n4=re.subn(r"if\(l!==curL\)\{curL=l;","if(l!==curL){curL=l;$('#sub').style.fontSize=l&&l.tk.length>27?'.74em':l&&l.tk.length>21?'.88em':'';",t)
assert n4==1
open('/home/claude/out/khutwa_hist_board_L2B.html','w',encoding='utf-8').write(t)
print('built',len(S))
