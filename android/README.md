# «خُطوة» على جوجل بلاي (Trusted Web Activity)

الدليل الكامل للمطوّر: https://claude.ai/artifact/A6qbt5ZZa9sAvvZ1PmjS6a

- `twa-manifest.json` إعدادات Bubblewrap (packageId com.addvalue.khutwa). ارفع targetSdk لـ 36 في app/build.gradle بعد `bubblewrap init`.
- `assetlinks.json` قالب: حط بصمة SHA-256 لشهادة Play App Signing وبصمة مفتاح الرفع، وانشره على https://ahmedhafez3009-beep.github.io/.well-known/assetlinks.json (ريبو ahmedhafez3009-beep.github.io + ملف .nojekyll).
- `privacy.html` مسودة سياسة الخصوصية (ناقص الإيميل والتاريخ).
- `store/` أيقونة 512، صورة الغلاف 1024×500، و4 لقطات 9:16 من آخر نسخة.

ملف مفتاح التوقيع (.keystore) ما يترفعش هنا أبدًا.
