const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1296,height:900}});
await p.goto('file://'+process.env.BOARD);await p.waitForTimeout(1500);
const r=await p.evaluate(()=>{const K=window.__K;K.seek(K.END);const out=[];K.IT.forEach((i,n)=>{if(i.k=='w'&&['واختار','قبل الإجابة','قرار','من غير خضوع'].includes(i.txt)){const b=i.e.getBBox();out.push([n,i.txt,i.e.getAttribute('x'),b.x,b.x+b.width,i.bb&&i.bb.x,i.af&&i.af.bb&&i.af.bb.x,i.gp,K.IT.indexOf(i.af)])}});return [out,[...document.fonts].map(f=>f.family+':'+f.status)]});
console.log(JSON.stringify(r,null,0));await b.close()})();
