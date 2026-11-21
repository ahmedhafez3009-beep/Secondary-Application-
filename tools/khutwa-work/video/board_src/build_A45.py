import re,json
v=open('/home/claude/khutwa/video/hist_final_v5.md',encoding='utf-8').read()
sec=v.split('## BOARD A45')[1].split('## BOARD B')[0]
S={}
for l in sec.splitlines():
    c=[x.strip() for x in l.split('|')]
    if len(c)>3 and re.match(r'^A\d\.\d+a?$',c[1]): S[c[1]]=c[2]
m=open('/home/claude/khutwa/video/hist_memory_v1.md',encoding='utf-8').read().split('## 4. دقيقة المراجعة')[1]
for l in m.splitlines():
    c=[x.strip() for x in l.split('|')]
    if len(c)>3 and re.match(r'^R\d$',c[1]): S[c[1]]=c[2]
t=open('/home/claude/out/board_template.html',encoding='utf-8').read()
body=open('/home/claude/out/tools/A45_content.js',encoding='utf-8').read()
a=t.index('/*__CONTENT_START__');b=t.index('/*__CONTENT_END__*/')+len('/*__CONTENT_END__*/')
t=t[:a]+'/*__CONTENT_START__*/\nconst S='+json.dumps(S,ensure_ascii=False)+';\n'+body+'\n/*__CONTENT_END__*/'+t[b:]
t=re.sub(r'<title>.*?</title>','<title>خُطوة · تاريخ · نسخة v1 · السبورة A45 (الشرايح A4–A5)</title>',t)
t=re.sub(r'<p id="note">نسخة v7 · الافتتاحية A0 \+ الشرايح A1–A3 \(السكريبت v3 \+ تبسيط v4\)\.','<p id="note">نسخة v1 · السبورة A45 (الشرايح A4–A5).',t)
open('/home/claude/out/khutwa_hist_board_A45.html','w',encoding='utf-8').write(t)
print(len(S),list(S)[:40])
