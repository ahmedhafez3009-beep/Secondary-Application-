const { chromium } = require('playwright');
(async()=>{const ids=process.argv.slice(2);const b=await chromium.launch();const p=await b.newPage({viewport:{width:1296,height:900}});const errs=[];p.on('pageerror',e=>errs.push(String(e)));
await p.goto('file://'+(process.env.BOARD||'/home/claude/out/khutwa_hist_board_A.html'));await p.waitForTimeout(1000);
for(const id of ids){const t=await p.evaluate(id=>{const l=window.__K.LINES.find(x=>x.id==id);const t=l.t+l.d*0.93;window.__K.seek(t);return t},id);await p.waitForTimeout(120);await (await p.$('#stage')).screenshot({path:'g_'+(process.env.TAG||'')+id+'.png'})}
console.log('errs',errs);await b.close()})();
