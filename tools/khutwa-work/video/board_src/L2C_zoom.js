const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1296,height:900}});
await p.goto('file://'+process.env.BOARD);await p.waitForTimeout(1000);
const t=await p.evaluate(()=>{const K=window.__K;const l=K.LINES.find(x=>x.id=='2C.57');K.seek(l.t-0.05);return l.t});await p.waitForTimeout(200);
await (await p.$('#stage')).screenshot({path:'g_C_zoom.png'});console.log(t);await b.close()})();
