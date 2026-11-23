# يبني السبورة B (v8): python3 B_v8_build.py  [list = يطبع السطور]
import re,json,sys,glob
T='/home/claude/out/tools/'
J=json.load(open(T+'B_v8_text.json',encoding='utf-8'));SP=J['SP'];SRC=J['SRC']
if len(sys.argv)>1:
    for k,v in SP.items(): print(k,'|',SRC.get(k),'|',v)
    sys.exit()
t=open('/home/claude/out/board_template.html',encoding='utf-8').read()
body=''.join(open(f,encoding='utf-8').read() for f in sorted(glob.glob(T+'B_v8_p[0-9].js')))
a=t.index('/*__CONTENT_START__');b=t.index('/*__CONTENT_END__*/')
t=t[:a]+'/*__CONTENT_START__ (اكتب محتوى السبورة هنا: slide()/go()/line()...) */\nconst SP='+json.dumps(SP,ensure_ascii=False)+',SRC='+json.dumps(SRC,ensure_ascii=False)+';\n'+body+t[b:]
t,n1=re.subn(r'<title>.*?</title>','<title>خُطوة · تاريخ · نسخة v8 · السبورة B (الفصل الثاني · الشرايح B1–B6)</title>',t)
t,n2=re.subn(r'<p id="note">نسخة v7 · الافتتاحية A0 \+ الشرايح A1–A3 \(السكريبت v3 \+ تبسيط v4\)\.','<p id="note">نسخة v8 · السبورة B (الفصل الثاني · الشرايح B1–B6).',t)
t,n3=re.subn(r'<rect y="-1800" width="3200" height="3600"','<rect x="-2400" y="-1800" width="8000" height="6000"',t)
assert (n1,n2,n3)==(1,1,2),(n1,n2,n3)
t,n4=re.subn(r"if\(l!==curL\)\{curL=l;","if(l!==curL){curL=l;$('#sub').style.fontSize=l&&l.tk.length>27?'.74em':l&&l.tk.length>21?'.88em':'';",t)
t,n5=re.subn(r"#world text\{font-family:Lalezar,Cairo,Tahoma,sans-serif\}","#world text{font-family:Lalezar,Cairo,Tahoma,sans-serif;text-rendering:geometricPrecision}",t)
assert (n4,n5)==(1,1),(n4,n5)
open('/home/claude/out/khutwa_hist_board_B.html','w',encoding='utf-8').write(t)
print('built B',len(SP))
