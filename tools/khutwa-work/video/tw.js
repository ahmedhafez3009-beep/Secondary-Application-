// WebKit check: nothing may be visible before its time
const pw = require('playwright');
(async()=>{for(const eng of ['webkit','chromium']){let b;try{b=await pw[eng].launch()}catch(e){console.log(eng,'not available');continue}
const p=await b.newPage({viewport:{width:1296,height:900}});const errs=[];p.on('pageerror',e=>errs.push(String(e)));
await p.goto('file://'+(process.env.BOARD||'/home/claude/out/khutwa_hist_board_A.html'));await p.waitForTimeout(1000);
const r=await p.evaluate(()=>{const K=window.__K;K.seek(0.5);return K.IT.filter(i=>i.k=='w'&&i.t>1&&i.e.getAttribute('visibility')!='hidden').length});
await (await p.$('#stage')).screenshot({path:'w_'+eng+'_0.png'});await p.evaluate(()=>{const K=window.__K;const l=K.LINES.find(x=>x.id=='A0.3');K.seek(l.t+l.d*.5)});await p.waitForTimeout(150);await (await p.$('#stage')).screenshot({path:'w_'+eng+'_1.png'});
console.log(eng,'future texts not hidden at t=0.5:',r,'errs',errs);await b.close()}})();
