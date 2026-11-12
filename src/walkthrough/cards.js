const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const P=JSON.parse(fs.readFileSync('plan.json'));const b=await chromium.launch();const p=await b.newPage({viewport:{width:1920,height:1080}});
await p.goto('file://'+process.cwd()+'/card.html');await p.evaluate(()=>document.fonts.ready);
const secs=[];P.forEach(x=>{if(!secs.includes(x.sec)&&x.sec!=='خُطوة')secs.push(x.sec)});
for(const x of P){const ci=secs.indexOf(x.sec);const seen=new Set(P.filter(y=>y.i<x.i).map(y=>y.sec));const chips=secs.map((s,j)=>[s,j==ci?'on':(seen.has(s)||x.sc==='outro'?'d':'')]);
 const n=x.sc==='landing'||x.sc==='outro'?'':'';
 await p.evaluate(d=>set(d),{sec:x.sec,n,ar:x.ar,en:x.en,chips,end:x.sc==='outro'});await p.screenshot({path:'cards/c'+String(x.i).padStart(2,'0')+'.png'});}
const f=await b.newPage({viewport:{width:1920,height:1080}});await f.goto('file://'+process.cwd()+'/frame.html');await f.screenshot({path:'cards/frame.png',omitBackground:true});
await b.close()})();
