const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1296,height:900}});const errs=[];p.on('pageerror',e=>errs.push(String(e)));
await p.goto('file:///home/claude/out/khutwa_hist_all.html');await p.waitForTimeout(800);
const goes=await p.$$eval('#home .go',a=>a.length);const out=[];
for(let n=1;n<=3;n++){await p.click('#menuBtn');await p.waitForTimeout(200);const bs=await p.$$('.les:not([disabled])');await bs[n-1].click();await p.waitForTimeout(400);
 const ks=await p.$$eval('#boards button',a=>a.map(x=>x.dataset.k));
 for(const k of ks){await p.click(`#boards button[data-k="${k}"]`);await p.waitForTimeout(1500);
  const fr=p.frames().find(f=>f!==p.mainFrame()&&f.name()===''&&!f.isDetached()&&f.url().startsWith('about:srcdoc')&&true);
  const h=await p.$(`iframe[title="${k}"]`);const f=await h.contentFrame();
  const r=await f.evaluate(()=>({lines:document.querySelectorAll('#lines option,.ln').length,sub:(document.getElementById('sub')||{}).textContent?.slice(0,20)}));out.push(k+':'+JSON.stringify(r));}}
await p.screenshot({path:'/tmp/all.png'});console.log('home buttons',goes);console.log(out.join('\n'));console.log('errs',JSON.stringify(errs));await b.close()})();
