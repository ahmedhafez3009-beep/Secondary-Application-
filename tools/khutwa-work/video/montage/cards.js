const { chromium } = require('playwright');const fs=require('fs');
const FD='/home/claude/secondary-application-/tools/khutwa-work/video/fonts/';
const css=fs.readFileSync(FD+'fonts.css','utf8').replace(/url\(['"]?([^'")]+)['"]?\)/g,(m,u)=>'url(file://'+FD+u.split('/').pop()+')');
const [,,cfgf,dir]=process.argv;const C=JSON.parse(fs.readFileSync(cfgf));
const mmss=s=>{s=Math.floor(s);return String(Math.floor(s/60)).padStart(2,'0')+':'+String(s%60).padStart(2,'0')};
const ar=s=>s.replace(/\d/g,d=>'٠١٢٣٤٥٦٧٨٩'[d]);
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1280,height:720}});
const shot=async(html,path,omit)=>{fs.writeFileSync(dir+'/t.html',`<html dir="rtl"><style>${css}body{margin:0;width:1280px;height:720px;overflow:hidden;font-family:Cairo;${omit?'background:transparent':''}}</style><body>${html}</body></html>`);await p.goto('file://'+dir+'/t.html');await p.evaluate(()=>document.fonts.ready);await p.screenshot({path,omitBackground:!!omit});};
for(let i=0;i<C.pauses.length;i++){const P=C.pauses[i];const N=P.dur||6;
 for(let n=N;n>=1;n--){const el=N-n;await shot(`<img src="file://${dir}/bg${i}.jpg" style="position:absolute;inset:0;width:100%;height:100%;filter:blur(7px) brightness(.55)">
 <div style="position:absolute;left:150px;right:150px;top:70px;bottom:70px;background:#fbf8f1;border:5px solid #102a43;border-radius:22px;box-shadow:10px 10px 0 #102a43;padding:28px 46px">
  <div style="display:flex;justify-content:space-between;align-items:center"><div style="font:900 44px Cairo;color:#102a43">⏸ وقفة · <span style="color:#d63a2f">اللي فات</span></div>
  <div style="width:84px;height:84px;border-radius:50%;border:7px solid #1EA05F;display:flex;align-items:center;justify-content:center;font:900 46px Cairo;color:#1EA05F">${ar(String(n))}</div></div>
  <div style="font:800 30px Cairo;color:#1EA05F;margin:6px 0 14px">${P.head}</div>
  ${P.points.map((t,j)=>`<div style="font:700 26px Cairo;color:#102a43;margin:9px 0;line-height:1.45;padding-right:34px;position:relative;opacity:${el>=1+Math.floor(j*(N-4)/P.points.length)?1:0}"><span style="position:absolute;right:0;color:#f5b301">●</span>${t}</div>`).join('')}
  <div style="position:absolute;bottom:22px;right:46px;left:46px;display:flex;justify-content:space-between;font:800 27px Cairo;color:#555"><span>مش فاكر؟ ارجع لـ <b style="color:#d63a2f;direction:ltr;unicode-bidi:embed">${mmss(P.back_final)}</b></span><span>غمّض وقولها لنفسك</span></div>
 </div>`,`${dir}/p${i}_${N-n}.png`)}}
for(let i=0;i<C.sections.length;i++){const S=C.sections[i];
 await shot(`<div style="position:absolute;top:14px;left:192px;right:0;display:flex;justify-content:center"><div style="background:#102a43;color:#fff;border-radius:16px;padding:6px 40px;text-align:center;box-shadow:8px 8px 0 #f5b301">
 <div style="font:800 26px Cairo;color:#f5b301">${C.lesson} · الجزء ${ar(C.part)}</div><div style="font-family:Lalezar;font-size:52px;line-height:1.15">${S.title}</div></div></div>`,`${dir}/s${i}.png`,true)}

const ST=[];C.sections.forEach((S,i)=>{ST.push({t:S.title,at:S.at_final,k:'s'});});C.pauses.forEach((P,i)=>ST.push({t:'وقفة: '+P.head.split('·')[0].trim(),at:P.at_final,k:'p'}));ST.sort((a,b)=>a.at-b.at);C.ST=ST;
fs.writeFileSync(dir+'/st.json',JSON.stringify(ST));
for(let a=0;a<ST.length;a++){await shot(`<div style="position:absolute;left:0;top:0;width:192px;height:720px;background:#102a43;color:#fff;padding:16px 12px;box-sizing:border-box">
<div style="font:900 20px Cairo;color:#f5b301;text-align:center">المحطات</div><div style="font:700 14px Cairo;text-align:center;opacity:.8;margin-bottom:10px">${C.lesson.split('·')[0]}· ${ar(C.part)}</div>
${ST.map((x,i)=>`<div style="display:flex;align-items:flex-start;gap:8px;margin:7px 0;padding:7px 8px;border-radius:10px;${i==a?'background:#f5b301;color:#102a43;':''}${i>a?'opacity:.55;':''}font:${i==a?900:700} ${x.k=='p'?15:17}px Cairo;line-height:1.35">
<span style="flex:none;width:22px;height:22px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:13px;${i<a?'background:#1EA05F;color:#fff':i==a?'background:#102a43;color:#f5b301':'border:2px solid #fff'}">${i<a?'✓':x.k=='p'?'⏸':ar(String(ST.slice(0,i+1).filter(y=>y.k=='s').length))}</span><span>${x.t}${i==a?'<br><span style="font-size:12px">◀ إنت هنا</span>':''}</span></div>`).join('')}
</div>
<div style="position:absolute;left:192px;right:0;top:612px;height:108px;background:#fbf8f1;border-top:3px solid #102a43">
<div style="position:absolute;right:24px;top:12px;font:800 22px Cairo;color:#102a43">${C.lesson}</div>
<div style="position:absolute;left:24px;top:12px;font:800 22px Cairo;color:#1EA05F">الجزء ${ar(C.part)}</div>
<div style="position:absolute;left:24px;right:24px;top:62px;height:14px;border-radius:7px;background:rgba(16,42,67,.15)"></div>
${ST.map(x=>`<div style="position:absolute;top:56px;width:${x.k=='p'?16:4}px;height:${x.k=='p'?16:26}px;border-radius:${x.k=='p'?'50%':'2px'};background:${x.k=='p'?'#f5b301':'#102a43'};${x.k=='p'?'border:2px solid #102a43;top:59px;':''}right:${(24+x.at/C.total_final*1064-(x.k=='p'?8:2)).toFixed(1)}px"></div>`).join('')}
</div>`,`${dir}/rail${a}.png`,true)}
await b.close()})();
