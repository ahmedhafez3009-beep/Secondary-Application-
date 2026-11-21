# ذاكرة مشروع «خُطوة» — اقرأ ده الأول بدل الشات كله
آخر تحديث: 2026-11-21 ~07:00 UTC

## المشروع
- تطبيق مذاكرة PWA مجاني لطلاب مصر. الريبو: /home/claude/secondary-application- ، المصدر في src/ ، البناء `python3 build.py` → src/site/.
- النشر: انسخ src/site/app/{index.html,sw.js,curriculum.json,curriculum2.json,version.json} → app/ ، و src/site/app/quiz/*.json → app/quiz/ ، و src/site/{index,report,story}.html → الجذر. ثم `git add -A && git commit` (نهاية الرسالة: سطرين Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com> و Claude-Session: https://claude.ai/code/session_01WsJEfRvCHVV1FWo1tmrmyE) ثم `git push -q origin main main:gh-pages`. src/site في .gitignore.
- الموقع: https://ahmedhafez3009-beep.github.io/Secondary-Application-/
- المستخدم: أحمد (Ahmed.Alalfy). الرد عليه بالعامية المصرية. إيميله خاص. قال «ارفع» = مسموح نرفع الجاهز من غير ما نسأل.

## قواعد ثابتة
- تقدم الطلاب ما يتكسرش أبدًا: لو أماكن الدروس اتغيرت → CURR_MIG + CURR_VERSION (حاليًا 12). تغيير الاسم في نفس المكان آمن.
- مفاتيح الكويز = أسماء الدروس بالظبط. data.js سطر 6 = `var CURR = {...};` (JSON).
- لا أرقام/شهادات مزيفة. حياد سياسي وبنص الكتاب.
- خطوات كل مادة: كاتب (BACC_TASK.md) → مراجع مستقل (CHECK.md) → مراجعة شكل الامتحان (EXAM_REVIEW.md، 2 حفظ/2 فهم/2 تطبيق) → مراجع مستقل على الأسئلة chg بس → integrate → build → اختبار → رفع. فرنساوي/ألماني + مراجع لغة (LANG_REVIEW.md).
- الملفات في /home/claude/khutwa/quiz/: SPEC_GEN.md SPEC_MATH.md CHECK.md BACC_TASK.md EXAM_REVIEW.md LANG_REVIEW.md exam_style.md integrate.py (بيشيل chg).
- الدمج: `cd /home/claude/khutwa/quiz && python3 integrate.py <sk> "<المصدر>" <file>.json`. أسماء الدروس من <sk>_curr.json تتحط في data.js بسكريبت يتأكد إن العدد والترتيب ثابت.
- اختبار: سيرفر `cd src/site && python3 -m http.server 8765 &` ثم سكريبتات playwright في /tmp (b2l2t.js, b2en.js, b2hi.js, b2ph.js — بتفتح الشعبة وأول كويز وتطبع errs []). ممكن تكون اتمسحت بعد restart.

## قراية كتب البكالوريا (المتصفح المدمج على جهاز أحمد)
- تاب "seed" على https://egyptianbaccalaureate.blob.core.windows.net/egyptianbaccalaureate/x404 (صفحة XML: السكربتات بتتحمل بـ fetch + eval، والـ canvas من HD=document.implementation.createHTMLDocument، وdisableFontFace:true، وintent:'print').
- دوال: openDoc, render, ocrOne, processBook (OCR دايمًا), runAll(BOOKS), gzsave(k) → نص GZB64 بيتحفظ في /tmp/claude-tool-results/... ونفكه بـ `python3 /home/claude/khutwa/ocr/dec.py <file> <out>`. tlBook(k,file) = طبقة نص الـPDF (أرقامها سليمة، حروفها بايظة) → gzsave('tl_'+k).
- مهم: OCR الحروف سليمة والأرقام بتبوظ؛ طبقة النص العكس. المواد الحسابية لازم الاتنين. صور الصفحات (toDataURL) أدق مصدر للتحقق.
- لو المتصفح اتقفل الحالة بتضيع ولازم أبنيها من جديد (الكود فوق).
- الحالة: اتقرا hi1 hi2 ph1 ph2 ch1 ch2 (+ textlayer لـ hi/ph/ch). كان شغال على ma1 (59/206). الطابور بعده: ma2 pr1 pr2 ac1 ac2 bz1 bz2 ps1 ps2 sar sen.
- أسماء الملفات: /home/claude/khutwa/ocr/b2<sub><1|2>.txt (+ _textlayer.txt). ma→b2math, pr→b2prog, ac→b2acc, bz→b2biz, ps→b2psy, sar→b2arstory, sen→b2enstory.
- أدوات جهاز أحمد (remote-devices) مش متاحة دلوقتي في الجلسة؛ لازم أحمد يفتح الشات من تطبيق الديسكتوب علشان ترجع.

## حالة كويزات البكالوريا تانية (مرفوع آخر commit 78bb66d)
| مادة | الحالة |
|---|---|
| b2ar عربي 156 | مرفوع (+امتحان) — دروس القصة لسه |
| b2en إنجليزي 270 | مرفوع — 5 دروس «The Story & Review» فاضية لحد قراية كتاب القصة |
| b2hi تاريخ 144 | مرفوع من النص النضيف |
| b2phys فيزياء 270 | مرفوع |
| b2fr فرنساوي 144 / b2de ألماني 76 | مرفوع (+لغة +امتحان)؛ شعب جديدة fr/de، والشعبة l2 = «إيطالي أو إسباني أو غيرهم» |
| b2chem كيميا | الكاتب وقف بسبب حد الاستخدام (agent a9d83eeb1b44eb8e3) — فيه b2chem_curr.json وb2chem_quiz.json جزئيين؛ كمّله بـ SendMessage |
| b2math, b2prog, b2acc, b2biz, b2psy | الكتب لسه ما اتقريتش |

## فيديو شرح التاريخ (درس تجريبي)
- الدرس: «بناء الدولة المصرية واستمرارها عبر التاريخ» (تانية بكالوريا، و1 د1، ص6–20 جزء 1).
- القرار: فيديو يوتيوب واحد ~24 دقيقة، 4 فصول، كل فصل على سبورة (أسلوب الأخضر)، أحمد بيسجل بصوته فويس نوت لكل شريحة (22 شريحة). اللينك هيتحط في التطبيق (زرار «▶ شرح الدرس» + زراير فصول بـ t=) — لسه ما اتعملش في التطبيق.
- الملفات: /home/claude/khutwa/video/ : HIST_VIDEO_SPEC.md، hist_u1l1_script_v3.md (الأخير)، review_*_v2.md، pages/p9,p11–p20.jpg (صور صفحات الكتاب)، hires_pages.txt، script_v3.html.
- صفحة المراجعة والتلقين: https://claude.ai/artifact/NGfmwsHJXBkreWsgjAGdmN (slug ac3ff6dd-02cc-443b-8a55-ef3590e82905).
- مستني من أحمد: موافقة على السكريبت + 4 قرارات (الطول 24 ولا 23¼، جمل الصياغة، الأردن/السعودية على الخريطة، إجابات بدون مفتاح). بعدها يسجّل الفصل 1 (A1–A5) الأول.
- عدة فيديو السبورة القديمة مش موجودة (لا هنا ولا على جهازه) → لازم تتبني من جديد (Python/PIL + ffmpeg) على قواعد سكيل addvalue-akhdar-sheet-video بهوية «خُطوة». الخريطة الذهنية بأسلوب بوزان بعد الفيديو.
- فريق الفيديو: كاتب، حارس أدلة، مراجع امتحان، لهجة قاهرية، محامي شيطان، مخرج بصري، مصمم خريطة ذهنية، مراجع جودة فيديو.

## مؤجل
- كتب الترم التاني، أسماء دروس إنجليزي الإعدادي، مواد X الإنجليزي بدون كويزات.
