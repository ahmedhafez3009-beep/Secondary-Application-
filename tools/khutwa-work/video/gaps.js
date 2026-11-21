// usage: node gaps.js [maxGap=3.2] [file]  — per spoken line: how long the board sits with nothing NEW starting
const { chromium } = require('playwright');
(async()=>{const mg=+(process.argv[2]||3.2),f=process.argv[3]||'/home/claude/out/khutwa_hist_board_A.html';const b=await chromium.launch();const p=await b.newPage();const errs=[];p.on('pageerror',e=>errs.push(String(e)));
await p.goto('file://'+f);await p.waitForTimeout(800);
const r=await p.evaluate(mg=>{const K=window.__K;const st=K.IT.map(i=>i.t).concat(K.CAM.filter((c,i)=>i%2==1).map(c=>c[0])).sort((a,b)=>a-b);const bad=[];
 for(const l of K.LINES){if(!l.txt)continue;const a=l.t,z=l.t+l.d;const pts=[a-0.001].concat(st.filter(t=>t>=a-0.3&&t<z),[z]);let g=0,at=0;for(let i=1;i<pts.length;i++)if(pts[i]-pts[i-1]>g){g=pts[i]-pts[i-1];at=pts[i-1]}
  const n=pts.length-2;if(g>mg||n==0)bad.push(`${l.id} dur ${l.d.toFixed(1)}s beats ${n} longest-still ${g.toFixed(1)}s (from +${Math.max(0,at-a).toFixed(1)}s) | ${l.txt.slice(0,50)}`)}
 return {end:K.END,items:K.IT.length,lines:K.LINES.filter(l=>l.txt).length,bad}},mg);
console.log('END',r.end.toFixed(0)+'s','items',r.items,'lines',r.lines,'| lines still >'+mg+'s:',r.bad.length);r.bad.forEach(x=>console.log(' '+x));console.log('errs',errs);await b.close()})();
