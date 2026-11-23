// usage: FR=0.999 node D_v8_fr.js id...   (زي fr.js بس بنسبة من السطر)
const { chromium } = require('playwright');
(async()=>{const ids=process.argv.slice(2),fr=+(process.env.FR||.999);const b=await chromium.launch();const p=await b.newPage({viewport:{width:1296,height:900}});
await p.goto('file://'+process.env.BOARD);await p.waitForTimeout(900);
for(const id of ids){await p.evaluate(([id,fr])=>{const l=window.__K.LINES.find(x=>x.id==id);window.__K.seek(l.t+l.d*fr)},[id,fr]);await p.waitForTimeout(120);await (await p.$('#stage')).screenshot({path:'h_'+(process.env.TAG||'')+id+'.png'})}
await b.close()})();
