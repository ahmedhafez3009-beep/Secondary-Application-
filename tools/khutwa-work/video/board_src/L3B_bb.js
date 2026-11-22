const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1296,height:900}});
await p.goto('file://'+process.env.BOARD);await p.waitForTimeout(1500);
const want=process.argv.slice(2);
const r=await p.evaluate(want=>{const K=window.__K;K.seek(K.END);return K.IT.filter(i=>i.k=='w'&&want.includes(i.txt)).map(i=>{const b=i.e.getBBox();return [i.txt,Math.round(b.x-i.cx),Math.round(b.x+b.width-i.cx),Math.round(b.y-i.cy),Math.round(b.y+b.height-i.cy),i.sz]})},want);
r.forEach(x=>console.log(x.join(' ')));await b.close()})();
