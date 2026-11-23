# بناء السبورة A45 (v8): v5 + مراجعة الحبكة v6 (A4.1a جديد، A4.4، A4.4a، A4.11a، A4.16)
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
# v6
V6={
 'A4.1a':'الملعب ده زي أرض الدولة: الخطوط هي حدودها، والصفّارة هي قرارها، ماشي جوّه الخطوط بس.',
 'A4.4':'اليابس، والمياه الإقليمية، والمجال الجوي. [[0.5]] تخيّل نفسك واقف على شط إسكندرية: تحت رجلك أرض، قدامك بحر، وفوقك سما.',
 'A4.4a':'وخد بالك، مفيش دولة من غير حدود محددة معترف بيها. يعني الدول التانية مقرّة بيها. زي سور بيتكم: الجيران عارفينه وما بيتعدّوهوش.',
 'A4.11a':'والميل البحري مقياس لمسافات البحر، وبنبدأ نعدّ من خط الأساس، يعني من عند الشط. [[0.5]] يعني شريط بحر، زي الرصيف قدام بيتكم.',
 'A4.16':'ونفس الفكرة في قناة السويس: الدولة بتحميها وبتراقب السفن العابرة. القناة جوّه حيزها، والمراقبة دي سيادة.',
}
assert S['A4.4'].startswith('اليابس') and S['A4.4a'].startswith('وخد بالك') and S['A4.11a'].startswith('والميل') and S['A4.16'].startswith('ونفس')
S.update(V6)
t=open('/home/claude/out/board_template.html',encoding='utf-8').read()
body=open('/home/claude/out/tools/A45_v8_content.js',encoding='utf-8').read()
a=t.index('/*__CONTENT_START__');b=t.index('/*__CONTENT_END__*/')+len('/*__CONTENT_END__*/')
t=t[:a]+'/*__CONTENT_START__*/\nconst S='+json.dumps(S,ensure_ascii=False)+';\n'+body+'\n/*__CONTENT_END__*/'+t[b:]
t,n1=re.subn(r'<title>.*?</title>','<title>خُطوة · تاريخ · نسخة v8 · السبورة A45 (الشرايح A4–A5)</title>',t)
t,n2=re.subn(r'<p id="note">نسخة v7 · الافتتاحية A0 \+ الشرايح A1–A3 \(السكريبت v3 \+ تبسيط v4\)\.','<p id="note">نسخة v8 · السبورة A45 (الشرايح A4–A5 + مراجعة الحبكة v6: الملعب = أرض الدولة، شط إسكندرية، سور البيت، خط الأساس، القناة حيز وسيادة).',t)
assert (n1,n2)==(1,1),(n1,n2)
t,n4=re.subn(r"if\(l!==curL\)\{curL=l;","if(l!==curL){curL=l;$('#sub').style.fontSize=l&&l.tk.length>27?'.74em':l&&l.tk.length>21?'.88em':'';",t)
t,n5=re.subn(r"#world text\{font-family:Lalezar,Cairo,Tahoma,sans-serif\}","#world text{font-family:Lalezar,Cairo,Tahoma,sans-serif;text-rendering:geometricPrecision}",t)
assert (n4,n5)==(1,1)
open('/home/claude/out/khutwa_hist_board_A45.html','w',encoding='utf-8').write(t)
print('built A45 v8',len(S))
