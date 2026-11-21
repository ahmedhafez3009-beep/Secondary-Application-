// usage: node D_fr.js ID[@frac] ... | t=SECONDS  -> g_D_<id>[_frac].png
const { chromium } = require('playwright');
(async()=>{const ids=process.argv.slice(2);const b=await chromium.launch();const p=await b.newPage({viewport:{width:1296,height:900}});const errs=[];p.on('pageerror',e=>errs.push(String(e)));
await p.goto('file://'+process.env.BOARD);await p.waitForTimeout(1000);
for(const a of ids){let name=a.replace(/[@=.]/g,'_');const ok=await p.evaluate(a=>{const K=window.__K;if(a.startsWith('t=')){K.seek(a=='t=END'?K.END:+a.slice(2));return 1}const [id,f]=a.split('@');const l=K.LINES.find(x=>x.id==id);if(!l)return 0;K.seek(l.t+l.d*(f?+f:0.97));return 1},a);if(!ok){console.log('no',a);continue}
 await p.waitForTimeout(120);await (await p.$('#stage')).screenshot({path:'/home/claude/out/g_D_'+name+'.png'})}
console.log('errs',errs);await b.close()})();
