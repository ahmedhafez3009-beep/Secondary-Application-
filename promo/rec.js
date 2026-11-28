const { chromium } = require('playwright');const fs=require('fs');const {spawn}=require('child_process');
const FD='/home/claude/secondary-application-/tools/khutwa-work/video/fonts/';
const css=fs.readFileSync(FD+'fonts.css','utf8').replace(/url\(['"]?([^'")]+)['"]?\)/g,(m,u)=>'url(file://'+FD+u.split('/').pop()+')');
const [,,M,out]=process.argv;const W=1080,H=M=='V'?1920:1080,fps=25;
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:W,height:H}});
await p.goto('file:///home/claude/promo/m.html?m='+M);await p.evaluate(c=>{document.getElementById('fonts').textContent=c},css);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(500);
const D=await p.evaluate(()=>D);
const ff=spawn('ffmpeg',['-v','error','-y','-f','image2pipe','-framerate',String(fps),'-i','-','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p',out]);
for(let f=0;f<D*fps;f++){await p.evaluate(t=>render(t),f/fps);const buf=await p.screenshot({type:'jpeg',quality:92});if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r));}
ff.stdin.end();await new Promise(r=>ff.on('close',r));await b.close()})();
