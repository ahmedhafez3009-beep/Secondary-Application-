const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1296,height:950}});const errs=[];p.on('pageerror',e=>errs.push(String(e)));
await p.goto('file:///home/claude/out/khutwa_hist_board_A.html');await p.waitForTimeout(800);
await p.click('#mode');const pr=await p.getAttribute('#mode','aria-pressed');
const r=await p.evaluate(async()=>{const K=window.__K,w=ms=>new Promise(r=>setTimeout(r,ms));const s1=K.SL[1].t;K.seek(s1-1.5);K.play();await w(2500);return {s1,T:K.T,msg:document.getElementById('msg').textContent,btn:document.getElementById('play').textContent}});
console.log(pr,JSON.stringify(r));
await p.click('#play');await p.waitForTimeout(1500);console.log('after play again',await p.evaluate(()=>window.__K.T));await p.click('#play');
await p.evaluate(()=>{const K=window.__K;K.seek(K.SL[1].t-1);K.play()});await p.waitForTimeout(1800);await p.click('#rec');await p.waitForTimeout(4300);console.log('after rec',await p.evaluate(()=>[window.__K.T,document.getElementById('msg').textContent]),errs);await b.close()})();
