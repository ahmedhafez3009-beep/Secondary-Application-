// scans final zoom widths: text metrics at tiny scale are quantised, so tb.js overlap results depend on the end zoom
const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1296,height:900}});
await p.goto('file://'+process.env.BOARD);await p.waitForTimeout(1500);
const r=await p.evaluate(()=>{const K=window.__K,out=[];const last=K.CAM[K.CAM.length-1];
 for(let w=14560;w<=16400;w+=40){const h=w*9/16;last[1]=1599-w/2;last[2]=-100;last[3]=w;last[4]=h;K.seek(K.END-1);K.seek(K.END);
  const ws=K.IT.filter(i=>i.k=='w').map(i=>({t:i.txt,b:i.e.getBBox(),i}));let ov=0,bad=0;
  for(const {b,i} of ws){if(i.cy<0?(b.x<20||b.x+b.width>3180||b.y+b.height>i.cy+1584):(b.x<i.cx+8||b.x+b.width>i.cx+K.CW-8||b.y+b.height>i.cy+530))bad++}
  for(let a=0;a<ws.length;a++)for(let c=a+1;c<ws.length;c++){const A=ws[a].b,B=ws[c].b;if(A.x<B.x+B.width-4&&B.x<A.x+A.width-4&&A.y+6<B.y+B.height-6&&B.y+6<A.y+A.height-6)ov++}
  out.push([w,ov,bad])}return out});
console.log(r.map(x=>x.join(':')).join(' '));await b.close()})();
