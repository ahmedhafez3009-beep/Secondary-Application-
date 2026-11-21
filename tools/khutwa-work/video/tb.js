const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1296,height:900}});const errs=[];
p.on('pageerror',e=>errs.push(String(e)));
await p.goto('file:///home/claude/out/khutwa_hist_board_A.html');await p.waitForTimeout(1500);
const r=await p.evaluate(()=>{const K=window.__K;K.seek(K.END);const bad=[];K.IT.filter(i=>i.k=='w').forEach(i=>{const b=i.e.getBBox();if(b.x<i.cx+8||b.x+b.width>i.cx+K.CW-8||b.y+b.height>i.cy+530)bad.push([i.txt,Math.round(b.x-i.cx),Math.round(b.x+b.width-i.cx),Math.round(b.y+b.height-i.cy)])});
 // overlaps between texts
 const ws=K.IT.filter(i=>i.k=='w').map(i=>({t:i.txt,b:i.e.getBBox()}));const ov=[];for(let a=0;a<ws.length;a++)for(let c=a+1;c<ws.length;c++){const A=ws[a].b,B=ws[c].b;if(A.x<B.x+B.width-4&&B.x<A.x+A.width-4&&A.y+6<B.y+B.height-6&&B.y+6<A.y+A.height-6)ov.push([ws[a].t,ws[c].t])}
 return {end:K.END,lines:K.LINES.length,sl:K.SL.map(s=>[Math.round(s.t),s.name]),bad,ov,times:K.LINES.map(l=>[l.id,Math.round(l.t+l.d-0.1)])}});
console.log(JSON.stringify(r));
const want=['A1.1','A1.2','A1.3','A2.1','A2.4','A2.5','A2.7','A2.10','A3.1','A3.5','A3.11','A3.13','A3.15'];
for(const [id,t] of r.times){if(!want.includes(id))continue;await p.evaluate(t=>window.__K.seek(t),t);await p.waitForTimeout(120);await (await p.$('#stage')).screenshot({path:'f_'+id+'.png'})}
await p.evaluate(()=>window.__K.seek(window.__K.END));await (await p.$('#stage')).screenshot({path:'f_end.png'});
console.log('errs',errs);await b.close()})();
