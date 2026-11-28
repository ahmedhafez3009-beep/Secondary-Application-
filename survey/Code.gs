/**
 * «خُطوة» — استقبال الاستبيان الأسبوعي في Google Sheet
 * 1) مشروع Apps Script (script.google.com) مربوط بالجدول عن طريق SHEET_ID تحت.
 * 2) Deploy ← New deployment ← Web app: Execute as = Me، Who has access = Anyone.
 * 3) انسخ رابط الـ Web app (بينتهي بـ /exec) وحطه في src/sv.txt وابني التطبيق.
 * 4) باسوورد لوحة الإدارة: Project Settings ← Script properties ← Add: الاسم ADMIN_KEY والقيمة الباسوورد.
 *    (الباسوورد بيتحفظ هنا بس، مش في كود التطبيق ولا الريبو.) بعد أي تعديل في الكود: Deploy ← Manage deployments ← Edit ← New version.
 */
const SHEET = 'الردود';
const SHEET_ID = '1aBXhuyjYM6E54zqDslhnAxN5vvoobJvMewlhW9o5MLA'; // جدول «خُطوة · ردود الاستبيان»
const HEAD = ['التاريخ','الأسبوع','رقم المستخدم','السن','الاسم','التقييم','المشاكل','مشكلة أخرى','المرحلة','الشعبة','المستخدم','خطوات الأسبوع','كويزات الأسبوع','حضور الأسبوع %','دروس خلصت','نسخة المناهج'];
const AGE = {u10:'أقل من 10 سنين','10':'من 10 لـ 12','13':'من 13 لـ 15','16':'من 16 لـ 18','18':'أكبر من 18'};
const PROB = {time:'مافيش وقت',hard:'مادة صعبة',focus:'تركيز',lessons:'أسماء الدروس',quiz:'الكويز',app:'التطبيق',other:'أخرى'};
const WHO = {self:'طالب',parent:'ولي أمر'};

function sheet_() {
  const ss = SpreadsheetApp.openById(SHEET_ID);
  let sh = ss.getSheetByName(SHEET);
  if (!sh) { sh = ss.insertSheet(SHEET); sh.appendRow(HEAD); sh.setFrozenRows(1); sh.setRightToLeft(true); }
  return sh;
}
const clip = (v, n) => String(v == null ? '' : v).replace(/[=+\-@]/, m => "'" + m).slice(0, n); // يمنع الصيغ في الخلايا

function doPost(e) {
  try {
    const d = JSON.parse(e.postData.contents);
    if (d.action === 'stats') return json_(stats_(d.key, d));
    if (d.action === 'news') return json_({ items: news_() });
    if (d.action === 'boot') return json_({ items: news_(), cfg: cfg_() });
    if (d.action === 'setcfg') return json_(setcfg_(d));
    if (d.action === 'announce') return json_(announce_(d));
    if (d.action === 'unannounce') return json_(unannounce_(d));
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

function json_(o) { return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }

/* لوحة الإدارة: بترجع ملخص بس لو الباسوورد صح؛ 8 محاولات غلط في 15 دقيقة = قفل 15 دقيقة */
function stats_(key, q) {
  const bad = auth_(key); if (bad) return bad;
  q = q || {};
  const span = [4, 12, 52].indexOf(+q.weeks) >= 0 ? +q.weeks : 4;
  const stF = /^[a-z]\d$/.test(q.stage || '') ? q.stage : '';
  const all = sheet_().getDataRange().getValues().slice(1).filter(r => r[2]);
  const rows = stF ? all.filter(r => r[8] === stF) : all;
  const wk = d => { const x = new Date(d); x.setHours(0,0,0,0); x.setDate(x.getDate() - ((x.getDay() + 1) % 7)); return Utilities.formatDate(x, 'Africa/Cairo', 'yyyy-MM-dd'); }; // الأسبوع بيبدأ السبت
  const avg = a => a.length ? a.reduce((s, v) => s + v, 0) / a.length : null;
  const now = new Date(), thisW = wk(now), prevW = wk(new Date(now - 7 * 864e5)), from4 = new Date(now - span * 7 * 864e5);
  const byW = {}; rows.forEach(r => { const w = wk(r[0]); (byW[w] = byW[w] || []).push(r); });
  const weeks = Object.keys(byW).sort().slice(-Math.max(span, 4)).map(w => ({ week: w, n: byW[w].length, rating: avg(byW[w].map(r => +r[5])), steps: avg(byW[w].map(r => +r[11])), att: avg(byW[w].filter(r => r[13] !== '').map(r => +r[13])) }));
  const tw = byW[thisW] || [], pw = byW[prevW] || [];
  const recent = rows.filter(r => new Date(r[0]) >= from4);
  // مين بيتحسن: آخر ردّين لكل مستخدم
  const byU = {}; rows.forEach(r => (byU[r[2]] = byU[r[2]] || []).push(r));
  let better = 0, worse = 0; Object.values(byU).forEach(a => { if (a.length > 1) { const d = +a[a.length - 1][5] - +a[a.length - 2][5]; if (d > 0) better++; else if (d < 0) worse++; } });
  const count = (arr, f) => { const c = {}; arr.forEach(r => f(r).forEach(k => { if (k) c[k] = (c[k] || 0) + 1; })); return Object.keys(c).map(k => ({ label: k, n: c[k] })).sort((a, b) => b.n - a.n); };
  const problems = count(recent, r => String(r[6] || '').split('، '));
  const stageR = {}; recent.forEach(r => { const s = r[8] || '؟'; (stageR[s] = stageR[s] || []).push(+r[5]); });
  const stages = Object.keys(stageR).map(s => ({ label: s, n: stageR[s].length, rating: avg(stageR[s]) })).sort((a, b) => b.n - a.n);
  const ages = count(recent, r => [r[3]]);
  const att = avg(recent.filter(r => r[13] !== '').map(r => +r[13])), steps = avg(recent.map(r => +r[11]));
  const comments = rows.filter(r => r[7]).slice(-30).reverse().map(r => ({ text: r[7], name: r[4] || '', age: r[3] || '', stage: r[8] || '', rating: r[5], week: wk(r[0]) }));
  // نقط الشغل: قواعد بسيطة وواضحة
  const focus = [];
  if (recent.length) problems.slice(0, 3).forEach(p => { const pct = Math.round(100 * p.n / recent.length); if (pct >= 15) focus.push('«' + p.label + '» اتقالت في ' + pct + '% من ردود آخر ' + span + ' أسبوع.'); });
  stages.filter(s => s.n >= 5 && s.rating < 3).forEach(s => focus.push('المرحلة ' + s.label + ' تقييمها ' + s.rating.toFixed(1) + ' من 5 (' + s.n + ' رد).'));
  if (weeks.length >= 3) { const a = weeks.slice(-3).map(w => w.rating); if (a[2] < a[1] && a[1] < a[0]) focus.push('متوسط التقييم نازل 3 أسابيع ورا بعض.'); }
  if (att != null && att < 70) focus.push('متوسط الحضور ' + Math.round(att) + '%، أقل من 70%.');
  if (steps != null && steps < 3) focus.push('متوسط خطوات المذاكرة في الأسبوع ' + steps.toFixed(1) + ' بس.');
  if (worse > better && worse >= 3) focus.push(worse + ' مستخدم تقييمهم نزل عن الرد اللي قبله (مقابل ' + better + ' طلع).');
  return {
    at: Utilities.formatDate(now, 'Africa/Cairo', 'yyyy-MM-dd HH:mm'),
    kpi: { total: rows.length, users: Object.keys(byU).length, thisWeek: tw.length, ratingThis: avg(tw.map(r => +r[5])), ratingPrev: avg(pw.map(r => +r[5])), better, worse, att: att == null ? null : Math.round(att), steps: steps == null ? null : +steps.toFixed(1) },
    weeks, problems, stages, ages, comments, focus, news: news_(true), span, stage: stF,
    dist: [1, 2, 3, 4, 5].map(v => recent.filter(r => +r[5] === v).length),
    stageOpts: Object.keys(all.reduce((o, r) => (r[8] && (o[r[8]] = 1), o), {})),
    stageMetrics: Object.keys(stageR).map(s => { const a = recent.filter(r => (r[8] || '؟') === s); return { label: s, n: a.length, rating: avg(a.map(r => +r[5])), steps: avg(a.map(r => +r[11])), att: avg(a.filter(r => r[13] !== '').map(r => +r[13])) }; }),
    responses: rows.slice(-60).reverse().map(r => ({ at: Utilities.formatDate(new Date(r[0]), 'Africa/Cairo', 'yyyy-MM-dd'), id: String(r[2]).slice(0, 6), age: r[3], name: r[4], rating: r[5], problems: r[6], other: r[7], stage: r[8], who: r[10], steps: r[11], quiz: r[12], att: r[13] })),
    cfg: cfg_(), sheetUrl: 'https://docs.google.com/spreadsheets/d/' + SHEET_ID + '/edit'
  };
}

function auth_(key) {
  const cache = CacheService.getScriptCache();
  const fails = +(cache.get('fails') || 0);
  if (fails >= 8) return { error: 'locked' };
  const real = PropertiesService.getScriptProperties().getProperty('ADMIN_KEY') || '';
  if (!real || String(key || '') !== real) { cache.put('fails', String(fails + 1), 900); Utilities.sleep(800); return { error: 'auth' }; }
  cache.remove('fails'); return null;
}

/* الإعلانات: آخر 5 إعلانات، كل واحد ليه رقم؛ الطالب بيشوف اللي ما شافهوش أول ما يفتح التطبيق */
function news_(all) {
  let a = []; try { a = JSON.parse(PropertiesService.getScriptProperties().getProperty('NEWS') || '[]'); } catch (e) {}
  return all ? a : a.map(x => ({ id: x.id, t: x.t, b: x.b, u: x.u, st: x.st, at: x.at }));
}
function saveNews_(a) { PropertiesService.getScriptProperties().setProperty('NEWS', JSON.stringify(a.slice(-5))); }
function announce_(d) {
  const bad = auth_(d.key); if (bad) return bad;
  const t = String(d.t || '').trim().slice(0, 60), b = String(d.b || '').trim().slice(0, 400);
  const u = /^https:\/\/[^\s"<>]{4,300}$/.test(d.u || '') ? d.u : '';
  const st = /^[a-z]\d$/.test(d.st || '') ? d.st : '';
  if (!t) return { error: 'empty' };
  const a = news_(true); a.push({ id: Date.now().toString(36), t, b, u, st, at: Utilities.formatDate(new Date(), 'Africa/Cairo', 'yyyy-MM-dd') });
  saveNews_(a); return { ok: true, news: news_(true) };
}
function unannounce_(d) {
  const bad = auth_(d.key); if (bad) return bad;
  saveNews_(news_(true).filter(x => x.id !== d.id)); return { ok: true, news: news_(true) };
}

/* شغّلها مرة واحدة من المحرر: بتسمّي الجدول وبتعمل صفحة الردود وبتطلب الصلاحيات */
function setup() { const ss = SpreadsheetApp.openById(SHEET_ID); ss.rename('خُطوة · ردود الاستبيان'); sheet_(); }

/* إعدادات الاستبيان من لوحة الإدارة */
const CFG_DEF = { on: true, every: 7, firstAfter: 3, askName: true };
function cfg_() { let c = {}; try { c = JSON.parse(PropertiesService.getScriptProperties().getProperty('CFG') || '{}'); } catch (e) {} return Object.assign({}, CFG_DEF, c); }
function setcfg_(d) {
  const bad = auth_(d.key); if (bad) return bad;
  const c = d.cfg || {};
  const v = { on: c.on !== false, every: [7, 14, 30].indexOf(+c.every) >= 0 ? +c.every : 7, firstAfter: [1, 3, 7].indexOf(+c.firstAfter) >= 0 ? +c.firstAfter : 3, askName: c.askName !== false };
  PropertiesService.getScriptProperties().setProperty('CFG', JSON.stringify(v)); return { ok: true, cfg: v };
}
