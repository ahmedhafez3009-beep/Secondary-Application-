const {chromium}=require('playwright');const {spawn}=require('child_process');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file:///home/claude/khutwa/video/explainer.html?render');await p.evaluate(()=>document.fonts.ready);
const SC=await p.evaluate(()=>SC);const only=process.argv.slice(2);
for(const [id,a,z] of SC){ if(only.length&&!only.includes(id))continue;
  const tmp=`parts/${id}.tmp.mp4`, out=`parts/${id}.mp4`;
  const ff=spawn('ffmpeg',['-loglevel','error','-y','-f','image2pipe','-framerate','30','-c:v','mjpeg','-i','-','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','-r','30',tmp]);
  const n=Math.round((z-a)*30);
  for(let f=0;f<n;f++){const T=a+f/30;await p.evaluate(T=>render(T),T);const buf=await p.screenshot({type:'jpeg',quality:92});if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r));}
  ff.stdin.end();const code=await new Promise(r=>ff.on('close',r));if(code===0){fs.renameSync(tmp,out);console.log(id,n)}else console.log('FAIL',id);
}
await b.close();})();
