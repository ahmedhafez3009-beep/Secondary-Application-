const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1296,height:900}});const errs=[];p.on('pageerror',e=>errs.push(String(e)));
await p.goto('file:///home/claude/out/khutwa_hist_lesson2_all.html');await p.waitForTimeout(1500);const out=[];
for(const k of (process.argv.slice(2).length?process.argv.slice(2):['A','A45','B'])){await p.click('#t_'+k);await p.waitForTimeout(1200);const fr=p.frames().find(f=>f.parentFrame()&&f.name()==''&&true&&f!==p.mainFrame()&&f.url().startsWith('about:srcdoc'));
 const h=await p.$('iframe[title="'+k+'"]');const f=await h.contentFrame();const r=await f.evaluate(async()=>{const K=window.__K;document.getElementById('play').click();await new Promise(r=>setTimeout(r,1500));const T=K.T;document.getElementById('play').click();return {lines:K.LINES.length,sl:K.SL.length,T:+T.toFixed(1),sub:document.getElementById('sub').textContent.slice(0,30)}});out.push(k+':'+JSON.stringify(r))}
await p.screenshot({path:'all.png'});console.log(out.join('\n'));console.log('disabled tabs',await p.$$eval('nav button:disabled',x=>x.map(b=>b.id)),'errs',errs);await b.close()})();
