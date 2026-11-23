const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();p.on('pageerror',e=>console.log('PAGEERR',String(e).slice(0,400)));p.on('console',m=>{if(m.type()=='warning')console.log('WARN',m.text())});
await p.goto('file://'+process.env.BOARD);await p.waitForTimeout(700);console.log('K',await p.evaluate(()=>!!window.__K));await b.close()})();
