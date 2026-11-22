const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1296,height:900}});
await p.goto('file://'+process.env.BOARD);await p.waitForTimeout(1500);
const r=await p.evaluate(()=>{const K=window.__K;K.seek(K.END);const o=[];K.IT.forEach((i,n)=>{if(i.k=='w'&&i.af&&(i.txt=='بن'||i.txt=='الحاكم،')){const b=i.e.getBBox();o.push([i.txt,i.x-i.cx,i.gp,'bb',b.x-i.cx,b.width,'stored',i.bb.x-i.cx,i.bb.width,'af',i.af.txt,i.af.bb.x-i.cx,i.af.bb.width,i.e.getAttribute('x')-i.cx, n, K.IT.indexOf(i.af)].join(' '))}});return o});
r.forEach(x=>console.log(x));await b.close()})();
