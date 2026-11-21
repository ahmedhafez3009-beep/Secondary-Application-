const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1296,height:950}});const errs=[];p.on('pageerror',e=>errs.push(String(e)));
await p.goto('file:///home/claude/out/khutwa_hist_board_A.html');await p.waitForTimeout(800);await p.click('#mode');
await p.evaluate(()=>{const K=window.__K;K.seek(K.SL[1].t-1);K.play()});await p.waitForTimeout(1800);
console.log('before rec',await p.evaluate(()=>[(window.__K.T-window.__K.SL[1].t).toFixed(2),document.getElementById('msg').textContent.slice(0,20)]));
await p.click('#rec');await p.waitForTimeout(500);console.log('0.5s',await p.evaluate(()=>[(window.__K.T-window.__K.SL[1].t).toFixed(2),document.getElementById('cd').hidden,document.getElementById('msg').textContent.slice(0,25)]));
for(let i=0;i<9;i++){await p.waitForTimeout(450);process.stdout.write(await p.evaluate(()=>(window.__K.T-window.__K.SL[1].t).toFixed(2)+document.getElementById("play").textContent[0]+" "))}console.log('4.5s',await p.evaluate(()=>[(window.__K.T-window.__K.SL[1].t).toFixed(2),document.getElementById('msg').textContent.slice(0,25)]),errs);await b.close()})();
