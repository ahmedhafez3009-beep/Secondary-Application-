// written-vs-spoken check: every written word must be spoken in its own line, and not appear >0.35s before it is first said
const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();await p.goto('file://'+process.env.BOARD);await p.waitForTimeout(700);
const r=await p.evaluate(()=>{const K=window.__K;const nz=s=>s.replace(/[ً-ْـ]/g,'').replace(/[«».,،:؟?!؛=←…()\[\]0-9٠-٩\-]/g,'').replace(/[أإآ]/g,'ا').replace(/ى/g,'ي').replace(/ة/g,'ه');const core=s=>nz(s).replace(/^(وال|بال|لل|ال|و|ب|ل|ك|ف)/,'');
 const OKW=['بالبلدي:','رسم تخيّلي','ض'],un=[],early=[],labels=new Set();for(const it of K.IT){if(it.k!='w')continue;let l=null;for(const x of K.LINES)if(it.t>=x.t-0.35)l=x;if(!l||!l.txt)continue;
  if(/^اجتهاد · /.test(it.txt)||/^[أبجد]$/.test(it.txt)||OKW.includes(it.txt)||/^احفظ دي [٠-٩]+$/.test(it.txt)||/^ص[٠-٩]+$/.test(it.txt)||/^[٠-٩]+$/.test(it.txt)){labels.add(it.txt.replace(/[٠-٩]+/,'N'));continue}
  const toks=l.tk.filter(k=>!k.p);
  for(const w of it.txt.split(/\s+/)){const c=core(w);if(!c)continue;const hit=toks.filter(k=>{const a=nz(k.w),d=core(k.w);return a.includes(c)||(d.length>=3&&c.includes(d))});
   if(!hit.length){un.push(l.id+' | '+it.txt+' | '+w);continue}
   const lead=Math.min(...hit.map(k=>l.t+k.s-it.t));if(lead>0.36)early.push(l.id+' EARLY '+lead.toFixed(2)+'s | '+it.txt)}}
 return {un,early,labels:[...labels]}});
console.log('UNSPOKEN ('+r.un.length+')\n'+r.un.join('\n'));console.log('EARLY ('+r.early.length+')\n'+r.early.join('\n'));console.log('label kinds',r.labels.join(' , '));await b.close()})();
