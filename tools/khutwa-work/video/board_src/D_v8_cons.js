const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();p.on('console',m=>console.log('CON',m.text()));p.on('pageerror',e=>console.log('PAGEERR',String(e).slice(0,300)));
await p.goto('file://'+process.env.BOARD);await p.waitForTimeout(600);await b.close()})();
