// node render.js <board.html> <out_prefix> [fps] [maxFrames]
const { chromium } = require('playwright');const fs=require('fs');const {spawn}=require('child_process');
(async()=>{const [,,file,out,fpsA,maxA]=process.argv;const fps=+(fpsA||25);
const b=await chromium.launch();const p=await b.newPage({viewport:{width:1280,height:720},deviceScaleFactor:1});
await p.goto('file://'+file);await p.addStyleTag({content:fs.readFileSync(__dirname+'/fonts_inline.css','utf8')});
await p.waitForFunction(()=>window.__LR&&Object.keys(__LR.LA).length>0,null,{timeout:60000});await p.waitForTimeout(1500);
await p.addScriptTag({content:"window.__setT=t=>{T=t;render()};"});
const tl=await p.evaluate(async()=>{await document.fonts.ready;IT.forEach(it=>it.bb=null);document.body.classList.add('rec');document.getElementById('lr').style.display='none';render();
 const LA=__LR.LA,segs=[];let w=0;for(let i=0;i<LINES.length;i++){const l=LINES[i];const k=Object.keys(LA).find(x=>x.endsWith('|'+l.id+'#'+i));const R=l.txt&&k?LA[k]:null;
  if(R){segs.push({w,dur:R.end-R.start,t:l.t,d:l.d,A:R.A,start:R.start,key:l.id+'#'+i});w+=R.end-R.start}else{segs.push({w,dur:l.d,t:l.t,d:l.d});w+=l.d}}
 return {segs,total:w,END,SFX}});
fs.writeFileSync(out+'_tl.json',JSON.stringify(tl));
const mapT=w=>{let s=tl.segs[0];for(const x of tl.segs)if(w>=x.w)s=x;const u=w-s.w;if(!s.A)return s.t+Math.min(u,s.d);const ta=s.start+u,A=s.A;if(ta<=A[0][0])return s.t;for(let i=1;i<A.length;i++)if(ta<A[i][0]){const a=A[i-1],c=A[i];return s.t+a[1]+(c[1]-a[1])*(ta-a[0])/(c[0]-a[0])}return s.t+s.d};
const N=Math.min(Math.ceil(tl.total*fps),+(maxA||1e9));
const ff=spawn('ffmpeg',['-v','error','-y','-f','image2pipe','-framerate',String(fps),'-i','-','-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p',out+'_v.mp4']);
const st=await p.$('#stage');let prev=-1;const ev=[];const t0=Date.now();
for(let f=0;f<N;f++){const w=f/fps,T=Math.min(mapT(w),tl.END);for(const e of tl.SFX)if(e.t>prev&&e.t<=T)ev.push({w,k:e.k});prev=T;
 await p.evaluate(t=>__setT(t),T);const buf=await st.screenshot({type:'jpeg',quality:88});if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r));
 if(f%500==0)console.error('frame',f,'/',N,((Date.now()-t0)/1000).toFixed(0)+'s')}
ff.stdin.end();await new Promise(r=>ff.on('close',r));fs.writeFileSync(out+'_sfx.json',JSON.stringify(ev));console.log('done',N,'frames',((Date.now()-t0)/1000).toFixed(0)+'s');await b.close()})();
