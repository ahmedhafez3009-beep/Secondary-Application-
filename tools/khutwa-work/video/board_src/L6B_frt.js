// usage: node L3B_frt.js id:pauseIdx ...  → frame at 60% of the given pause (or id:@0.5 = fraction of the line)
const { chromium } = require('playwright');
(async()=>{const ids=process.argv.slice(2);const b=await chromium.launch();const p=await b.newPage({viewport:{width:1296,height:900}});
await p.goto('file://'+process.env.BOARD);await p.waitForTimeout(1000);
for(const a of ids){const [id,k]=a.split(':');await p.evaluate(([id,k])=>{const K=window.__K,l=K.LINES.find(x=>x.id==id);let t;if(k[0]=='@')t=l.t+l.d*+k.slice(1);else{const pz=l.tk.filter(x=>x.p)[+k];t=l.t+pz.s+(pz.e-pz.s)*.6}K.seek(t)},[id,k]);await p.waitForTimeout(120);await (await p.$('#stage')).screenshot({path:'h_'+a.replace(/[:@]/g,'_')+'.png'})}
await b.close()})();
