const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch({args:['--autoplay-policy=no-user-gesture-required']});const p=await b.newPage({viewport:{width:1296,height:950}});const errs=[];p.on('pageerror',e=>errs.push(String(e)));
await p.goto('file:///home/claude/out/khutwa_hist_board_A.html');await p.waitForTimeout(800);
// karaoke
await p.click('#play');await p.waitForTimeout(2500);const k=await p.evaluate(()=>({on:document.querySelectorAll('#sub .on').length,cur:document.querySelectorAll('#sub .cur').length,n:document.querySelectorAll('#sub span').length}));await (await p.$('#stage')).screenshot({path:'k1.png'});await p.click('#play');
// record countdown
await p.click('#rec');await p.waitForTimeout(1200);const cd=await p.textContent('#cd');await p.waitForTimeout(3500);const rT=await p.evaluate(()=>window.__K.T);await p.evaluate(()=>window.__K.stop());
// sync with a silent 12s wav
const r=await p.evaluate(async()=>{const K=window.__K;const sr=8000,n=sr*12,buf=new ArrayBuffer(44+n),v=new DataView(buf);const W=(o,s)=>[...s].forEach((c,i)=>v.setUint8(o+i,c.charCodeAt(0)));W(0,'RIFF');v.setUint32(4,36+n,true);W(8,'WAVEfmt ');v.setUint32(16,16,true);v.setUint16(20,1,true);v.setUint16(22,1,true);v.setUint32(24,sr,true);v.setUint32(28,sr,true);v.setUint16(32,1,true);v.setUint16(34,8,true);W(36,'data');v.setUint32(40,n,true);for(let i=0;i<n;i++)v.setUint8(44+i,128);
 K.seek(0);K.AU[0]={a:new Audio(URL.createObjectURL(new Blob([buf],{type:'audio/wav'}))),taps:null};K.startSync();const w=ms=>new Promise(r=>setTimeout(r,ms));await w(1000);K.tap();await w(2000);K.tap();await w(2000);K.tap();await w(300);
 const taps=K.AU[0].taps,code=K.code;K.stop();await w(100);K.play();await w(2000);const T1=K.T;await w(2000);const T2=K.T;K.stop();return {taps,code,T1,T2,L:K.sLines(0).map(l=>l.t)}});
console.log(JSON.stringify({k,cd,rT,r}),'errs',errs);await b.close()})();
