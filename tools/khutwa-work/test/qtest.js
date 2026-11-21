// usage: node qtest.js sk [sk...]  — needs server on :8765 serving src/site
const { chromium } = require(process.env.PW || 'playwright');
(async()=>{ const sks=process.argv.slice(2); const b=await chromium.launch(); const p=await b.newPage(); const errs=[];
 p.on('pageerror',e=>errs.push(String(e))); p.on('console',m=>{ if(m.type()==='error') errs.push(m.text()); });
 await p.goto('http://localhost:8765/app/index.html',{waitUntil:'networkidle'});
 const r=await p.evaluate(async(sks)=>{ const idx=await (await fetch('quiz/index.json')).json(); const out={};
  for(const sk of sks){ const L=[]; CURR[sk].parts.forEach(pp=>pp[1].forEach(u=>u[1].split('|').forEach(l=>L.push(l))));
   const q=await (await fetch('quiz/'+sk+'.json')).json(); const bad=[]; let n=0;
   for(const [k,qs] of Object.entries(q.by)){ for(const x of qs){ n++; if(x.o.length!==4||!(x.a>=0&&x.a<4)||!x.q||!x.e) bad.push(k);} }
   out[sk]={lessons:L.length, inIndex:L.filter(l=>(idx[sk]||[]).includes(l)).length, quizLessons:Object.keys(q.by).length, questions:n, bad:bad.length, name:CURR[sk].name}; }
  return out; }, sks);
 console.log(JSON.stringify(r)); console.log('errs',JSON.stringify(errs)); await b.close(); })();
