const { chromium } = require('playwright');const fs=require('fs');
const FD='/home/claude/secondary-application-/tools/khutwa-work/video/fonts/';
const css=fs.readFileSync(FD+'fonts.css','utf8').replace(/url\(['"]?([^'")]+)['"]?\)/g,(m,u)=>'url(file://'+FD+u.split('/').pop()+')');
const S=JSON.parse(fs.readFileSync('shorts.json'));
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
for(const s of S){fs.writeFileSync('/home/claude/shorts/t.html',`<html dir="rtl"><style>${css}body{margin:0;width:1080px;height:1920px;background:#fbf8f1;background-image:radial-gradient(#c9c2b3 2px,transparent 2px);background-size:34px 34px;font-family:Cairo;position:relative;overflow:hidden}</style><body>
<div style="position:absolute;top:0;left:0;right:0;height:130px;background:#102a43;color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 50px;font:900 50px Cairo"><span>تاريخ تانية <b style="color:#f5b301">بكالوريا</b></span><span style="font-size:46px">خُطوة</span></div>
<div style="position:absolute;top:200px;left:50px;right:50px;text-align:center;font-family:Lalezar;font-size:${s.fs||96}px;line-height:1.2;color:#102a43">${s.title}</div>
<div style="position:absolute;top:640px;left:0;width:1080px;height:608px;background:#000;border-top:6px solid #102a43;border-bottom:6px solid #102a43"></div>
<div style="position:absolute;top:1330px;left:0;right:0;text-align:center"><span style="background:#1EA05F;color:#fff;font:900 46px Cairo;padding:10px 44px;border-radius:50px;border:4px solid #102a43">${s.badge}</span></div>
<div style="position:absolute;top:1480px;left:60px;right:60px;text-align:center;font:800 44px Cairo;color:#102a43;line-height:1.5">${s.sub}</div>
<div style="position:absolute;bottom:120px;left:0;right:0;text-align:center;font:900 48px Cairo;color:#d63a2f">الشرح كامل على القناة ▶</div>
</body></html>`);await p.goto('file:///home/claude/shorts/t.html');await p.evaluate(()=>document.fonts.ready);await p.screenshot({path:`/home/claude/shorts/bg_${s.id}.png`});}
await b.close()})();
