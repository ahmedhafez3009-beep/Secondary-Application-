/**
 * «خُطوة» — استقبال الاستبيان الأسبوعي في Google Sheet
 * 1) افتح Google Sheet جديد ← Extensions ← Apps Script ← الصق الكود ده مكان أي كود.
 * 2) Deploy ← New deployment ← Web app: Execute as = Me، Who has access = Anyone.
 * 3) انسخ رابط الـ Web app (بينتهي بـ /exec) وحطه في src/sv.txt وابني التطبيق.
 */
const SHEET = 'الردود';
const HEAD = ['التاريخ','الأسبوع','رقم المستخدم','السن','الاسم','التقييم','المشاكل','مشكلة أخرى','المرحلة','الشعبة','المستخدم','خطوات الأسبوع','كويزات الأسبوع','حضور الأسبوع %','دروس خلصت','نسخة المناهج'];
const AGE = {u10:'أقل من 10','10':'10–12','13':'13–15','16':'16–18','18':'أكبر من 18'};
const PROB = {time:'مافيش وقت',hard:'مادة صعبة',focus:'تركيز',lessons:'أسماء الدروس',quiz:'الكويز',app:'التطبيق',other:'أخرى'};
const WHO = {self:'طالب',parent:'ولي أمر'};

function sheet_() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sh = ss.getSheetByName(SHEET);
  if (!sh) { sh = ss.insertSheet(SHEET); sh.appendRow(HEAD); sh.setFrozenRows(1); sh.setRightToLeft(true); }
  return sh;
}
const clip = (v, n) => String(v == null ? '' : v).replace(/[=+\-@]/, m => "'" + m).slice(0, n); // يمنع الصيغ في الخلايا

function doPost(e) {
  try {
    const d = JSON.parse(e.postData.contents);
    const r = Number(d.rating);
    if (!(r >= 1 && r <= 5) || !/^[a-z0-9]{8,24}$/.test(d.id || '')) return out_('bad');
    const m = d.m || {};
    const lock = LockService.getScriptLock(); lock.waitLock(5000);
    sheet_().appendRow([
      new Date(), clip(d.week, 10), d.id, AGE[d.age] || '', clip(d.name, 20), r,
      (d.problems || []).map(p => PROB[p] || '').filter(String).join('، '), clip(d.other, 200),
      clip(m.stage, 6), clip(m.track, 10), WHO[m.who] || '', +m.steps7 || 0, +m.quiz7 || 0,
      (+m.att7 >= 0 ? +m.att7 : ''), +m.lessonsDone || 0, clip(d.app, 8)
    ]);
    lock.releaseLock();
    return out_('ok');
  } catch (err) { return out_('err'); }
}
function out_(s) { return ContentService.createTextOutput(s); }
