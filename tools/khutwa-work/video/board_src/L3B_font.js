const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1296,height:900}});
const t0=Date.now();p.on('requestfailed',r=>console.log('FAIL',Date.now()-t0,r.url().slice(0,80)));p.on('requestfinished',r=>console.log('OK',Date.now()-t0,r.url().slice(0,80)));
await p.goto('file://'+process.env.BOARD);console.log('loaded',Date.now()-t0);
for(const w of [200,1500,3000]){await p.waitForTimeout(w);console.log(Date.now()-t0,await p.evaluate(()=>{const K=window.__K;const i=K.IT.find(i=>i.k=='w'&&i.txt=='عمرو');return [document.fonts.size,document.fonts.status,[...document.fonts].map(f=>f.family+':'+f.status).join(','),i.e.getBBox().width,i.bb&&i.bb.width].join(' | ')}))}
await b.close()})();
