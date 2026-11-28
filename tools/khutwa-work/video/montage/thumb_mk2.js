const { chromium } = require('playwright');const fs=require('fs');
const FD='/home/claude/secondary-application-/tools/khutwa-work/video/fonts/';
const css=fs.readFileSync(FD+'fonts.css','utf8').replace(/url\(['"]?([^'")]+)['"]?\)/g,(m,u)=>'url(file://'+FD+u.split('/').pop()+')');
const CFG=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));const T0=[["يعني إيه","دولة؟","1/6"],["حدود","مصر","2/6"],["السلطة","والسيادة","3/6"],["ليه مصر","استمرت؟","4/6"],["حل أسئلة","الكتاب ١","5/6"],["حل أسئلة","الكتاب ٢","6/6"]];
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1280,height:720}});
for(let i=0;i<CFG.length;i++){const {a,c,n,exam,img,pos,out,les,cs}=CFG[i];
fs.writeFileSync('/home/claude/thumb/t.html',`<html dir="rtl"><style>${css}
body{margin:0;width:1280px;height:720px;overflow:hidden;background:${exam?'#e9f6ee':'#fbf8f1'};background-image:radial-gradient(#c9c2b3 1.6px,transparent 1.6px);background-size:28px 28px;font-family:Cairo;position:relative}
.img{position:absolute;left:24px;top:120px;width:640px;height:560px;border-radius:18px;overflow:hidden;border:5px solid #102a43;box-shadow:8px 8px 0 #102a43;background:#fff}
.img img{width:100%;height:100%;object-fit:cover;object-position:${pos}}
.top{position:absolute;right:0;top:0;left:0;height:92px;background:#102a43;color:#fff;font:900 46px Cairo;display:flex;align-items:center;padding:0 34px;justify-content:space-between}
.top b{color:#f5b301}
.t{position:absolute;right:40px;top:150px;width:580px;text-align:center;font-family:Lalezar;line-height:1.08}
.t .a{font-size:104px;color:#102a43}.t .c{font-size:${cs||128}px;color:${exam?'#1EA05F':'#d63a2f'}}
.badge{position:absolute;right:150px;bottom:44px;background:#1EA05F;color:#fff;font:900 54px Cairo;padding:4px 36px;border-radius:50px;border:4px solid #102a43}
${exam?'.chk{position:absolute;left:560px;top:96px;font:900 150px Cairo;color:#1EA05F;text-shadow:4px 4px 0 #102a43}':''}
</style><body><div class="top"><span>تاريخ تانية ثانوي <b>بكالوريا</b></span><span style="font-size:40px">خُطوة</span></div>
<div class="img"><img src="file://${img}"></div>${exam?'<div class="chk">✓</div>':''}
<div class="t"><div class="a">${a}</div><div class="c">${c}</div></div><div class="badge">الدرس ${les} · ${n}</div></body></html>`);await p.goto('file:///home/claude/thumb/t.html');await p.evaluate(()=>document.fonts.ready);
await p.waitForTimeout(400);await p.screenshot({path:out,type:'jpeg',quality:90});}
await b.close()})();
