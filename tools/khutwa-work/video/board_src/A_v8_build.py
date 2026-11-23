# بناء السبورة A (v8): القالب (محرك A الأصلي v7 من غير المحتوى) + المحتوى A_v8_p0..p5.js
# الاستعمال: python3 A_v8_build.py   ← بيكتب /home/claude/out/khutwa_hist_board_A.html
#            وبعدها: python3 .../video/inject_lrec.py <الملف>  (A_v8_make.sh بيعمل الاتنين)
import re,glob
T='/home/claude/out/tools/'
t=open(T+'A_v8_template.html',encoding='utf-8').read()
body=''.join(open(f,encoding='utf-8').read()+'\n' for f in sorted(glob.glob(T+'A_v8_p[0-9].js')))
a=t.index('/*__CONTENT_START__*/');b=t.index('/*__CONTENT_END__*/')+len('/*__CONTENT_END__*/')
t=t[:a]+'/*__CONTENT_START__*/\n'+body+'\n/*__CONTENT_END__*/'+t[b:]
t,n1=re.subn(r'<title>.*?</title>','<title>خُطوة · تاريخ · السبورة A (v8: خريطة البيت + مصر زي مين)</title>',t)
t,n2=re.subn(r'<p id="note">نسخة v7 · الافتتاحية A0 \+ الشرايح A1–A3 \(السكريبت v3 \+ تبسيط v4\)\.','<p id="note">نسخة v8 · الافتتاحية A0 + الشرايح A1–A3 (السكريبت v3 + تبسيط v4 + مراجعة الحبكة v6: خريطة البيت الكاملة، وكارت ٢أ «الأركان في مصر»، واللامثال).',t)
# الورقة اتوسعت: عمود جديد على الشمال (x<0) + توقيع تحت الشبكة
t,n3=re.subn(r'<rect y="-1800" width="3200" height="3600"','<rect x="-1400" y="-1800" width="4900" height="4400"',t)
assert (n1,n2,n3)==(1,1,2),(n1,n2,n3)
# patch: تصغير خط الترجمة للجمل الطويلة (زي L5C)
t,n4=re.subn(r"if\(l!==curL\)\{curL=l;","if(l!==curL){curL=l;$('#sub').style.fontSize=l&&l.tk.length>27?'.74em':l&&l.tk.length>21?'.88em':'';",t)
assert n4==1
# patch: مقاسات النص ثابتة مهما كان الزووم
t,n5=re.subn(r"#world text\{font-family:Lalezar,Cairo,Tahoma,sans-serif\}","#world text{font-family:Lalezar,Cairo,Tahoma,sans-serif;text-rendering:geometricPrecision}",t)
assert n5==1
open('/home/claude/out/khutwa_hist_board_A.html','w',encoding='utf-8').write(t)
print('built A v8')
