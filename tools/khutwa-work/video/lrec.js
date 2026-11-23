/* lrec.js — استوديو «جملة جملة» لسبورات خُطوة.
   بيتحط بعد سكريبت المحرك، وبيستعمل متغيراته العامة: LINES, SL, SFX, END, T, AC, render, seek, stop, sfx.
   الفكرة: كل جملة بتتسجل لوحدها بالمايك، وبعدين البرنامج يقيس صوتك (فين بتتكلم وفين ساكت)
   ويوزّع كلمات الجملة على صوتك، فالرسم والكاريوكي يمشوا على كلامك إنت مش على توقيت ثابت. */
(()=>{
const TL=LINES.map((l,i)=>Object.assign(l,{ix:i})).filter(l=>l.txt);
const KEY='kh|'+document.title+'|'+Math.round(END)+'|';
const lid=l=>KEY+l.id+'#'+l.ix;
const LA={};let li=0,stream=null,mr=null,recOn=false,lp=null,BUS=null,SFXG=null,DEST=null,vrec=null;
const $$=s=>document.querySelector(s);
const css=document.createElement('style');css.textContent=`
#lr{margin-top:8px;font-size:14px}#lr button,#lr label{background:#16212c;color:#e8eef0;border:1px solid #2a3945;border-radius:8px;padding:6px 12px;font:inherit;cursor:pointer}
#lrT{background:#C99A1B!important;border-color:#C99A1B!important;color:#0b1620!important;font-weight:700}
#lrp{background:#0f1d29;border:1px solid #2a3945;border-radius:10px;padding:10px;margin-top:8px}#lrp[hidden]{display:none}
#lrp .row{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-top:8px}
#lrn{color:#9fd8b8;font-size:13px}#lrx{font:700 clamp(16px,2.4vw,26px)/1.6 Cairo,Tahoma,sans-serif;color:#fff;margin-top:6px}
#lrRec{background:#D7463C!important;border-color:#D7463C!important;font-weight:700}#lrRec.on{animation:lrb 1s infinite}
@keyframes lrb{50%{opacity:.55}}
#lrBar{display:flex;flex-wrap:wrap;gap:3px;margin-top:8px}#lrBar i{width:14px;height:14px;border-radius:3px;background:#2a3945;cursor:pointer;display:block}
#lrBar i.ok{background:#1EA05F}#lrBar i.cur{outline:2px solid #F5BE32}#lrBar i.sl{margin-right:8px}
#lrMsg{color:#F5BE32;font-size:13px;margin-top:6px;min-height:1.2em}#lrHelp{color:#9aa9ad;font-size:12.5px;line-height:1.8;margin-top:6px}`;
document.head.appendChild(css);
const box=document.createElement('div');box.id='lr';box.innerHTML=`<button id="lrT">🎙 سجّل جملة جملة</button>
<div id="lrp" hidden><div id="lrn"></div><div id="lrx"></div>
<div class="row"><button id="lrPrev">→ اللي قبلها</button><button id="lrRec">● سجّل الجملة (Enter)</button><button id="lrPlay">▶ اسمعها مع الرسم (P)</button><button id="lrNext">اللي بعدها ←</button>
<label><input type="checkbox" id="lrAuto" checked> بعد ما أخلّص جملة، ابدأ اللي بعدها لوحدها</label></div>
<div class="row"><button id="lrAll">▶ شغّل من أول الشريحة بصوتي</button><button id="lrFull">▶ السبورة كلها بصوتي</button><button id="lrVid">🎬 صدّر فيديو بصوتي</button><button id="lrWav">⬇ الصوت كله WAV</button>
<button id="lrSave">💾 احفظ التسجيلات في ملف</button><label>📂 افتح ملف تسجيلات<input id="lrLoad" type="file" accept=".json,application/json" hidden></label><button id="lrDel">🗑 امسح تسجيل الجملة دي</button></div>
<div id="lrBar"></div><div id="lrMsg"></div>
<div id="lrHelp">دوس <b>Enter</b> وقول الجملة اللي مكتوبة، ودوس <b>Enter</b> تاني لما تخلص. البرنامج بيشيل السكوت اللي في الأول والآخر، ويقيس صوتك، ويوزّع الكتابة والرسم على كلامك (السكتات اللي في الجملة بتتربط بوقفاتك). لو مش عاجباك دوس Enter عليها تاني تتسجل من جديد. التسجيلات بتتحفظ في المتصفح ده لوحدها، وخد منها نسخة بـ«احفظ التسجيلات في ملف». في الآخر «صدّر فيديو» بيعمل فيديو للسبورة بصوتك (اختار التاب ده لما يسألك).</div></div>`;
$$('#ctl').after(box);
const say=t=>{$$('#lrMsg').textContent=t};
const slideOf=l=>{let s=SL[0];for(const x of SL)if(l.t>=x.t-.001)s=x;return s};
function bar(){const b=$$('#lrBar');if(!b.children.length){let ps=null;TL.forEach((l,i)=>{const e=document.createElement('i');const s=slideOf(l);if(ps&&s!==ps)e.className='sl';ps=s;e.title=l.id+' · '+l.txt.slice(0,50);e.onclick=()=>pick(i);b.appendChild(e)})}
 [...b.children].forEach((e,i)=>{e.classList.toggle('ok',!!LA[lid(TL[i])]);e.classList.toggle('cur',i==li)})}
function show(){const L=TL[li];const n=TL.filter(l=>LA[lid(l)]).length;$$('#lrn').textContent=`جملة ${li+1} من ${TL.length} · ${L.id} · ${slideOf(L).name}${LA[lid(L)]?' · ✓ متسجلة':''} — اتسجل ${n} من ${TL.length}`;
 $$('#lrx').textContent=L.txt;bar()}
function pick(i){if(recOn)return;lstop();stop();li=Math.max(0,Math.min(TL.length-1,i));seek(TL[li].t);show()}
function ac(){if(!AC)AC=new (window.AudioContext||window.webkitAudioContext)();if(!BUS){BUS=AC.createGain();BUS.connect(AC.destination);SFXG=AC.createGain();SFXG.connect(BUS);
 const oc=AudioNode.prototype.connect;AudioNode.prototype.connect=function(t,...r){if(BUS&&t===AC.destination&&this!==BUS)return oc.call(this,SFXG,...r);return oc.call(this,t,...r)}}
 if(AC.state=='suspended')AC.resume();return AC}
/* ---------- قياس الصوت ---------- */
async function analyze(blob){const buf=await ac().decodeAudioData(await blob.arrayBuffer());const d=buf.getChannelData(0),sr=buf.sampleRate,hop=Math.max(1,Math.round(sr*.01)),env=[];
 for(let i=0;i+hop<=d.length;i+=hop){let s=0;for(let j=i;j<i+hop;j++)s+=d[j]*d[j];env.push(Math.sqrt(s/hop))}
 const smv=env.map((v,i)=>{let a=0,n=0;for(let k=i-3;k<=i+3;k++)if(k>=0&&k<env.length){a+=env[k];n++}return a/n});
 const so=[...smv].sort((a,b)=>a-b),fl=so[Math.floor(so.length*.08)]||0,pk=so[Math.floor(so.length*.985)]||1e-6;if(pk<.004)return{dur:buf.duration,segs:[]};
 const th=fl+(pk-fl)*.1;let segs=[],st=-1;smv.forEach((x,i)=>{const on=x>th;if(on&&st<0)st=i;if(!on&&st>=0){segs.push([st,i]);st=-1}});if(st>=0)segs.push([st,smv.length]);
 segs=segs.filter(s=>s[1]-s[0]>=7);const m=[];for(const s of segs){if(m.length&&s[0]-m[m.length-1][1]<18)m[m.length-1][1]=s[1];else m.push(s.slice())}
 return{dur:buf.duration,segs:m.map(s=>[+(s[0]*.01).toFixed(2),+(s[1]*.01).toFixed(2)])}}
/* ---------- ربط كلام الجملة بصوتك ---------- */
function anchors(L,an){const lt=L.tk[L.tk.length-1],tp=lt&&lt.p?+lt.v:0;const ph=[];let cur=[];L.tk.forEach(k=>{if(k.p){if(cur.length)ph.push(cur);cur=[]}else cur.push(k)});if(cur.length)ph.push(cur);
 const sg=an.segs,P=ph.length,wl=k=>k.w.replace(/[^؀-ۿa-zA-Z0-9٠-٩]/g,'').length+1;let sp;
 if(sg.length>=P){const gi=sg.slice(1).map((s,i)=>({i,g:s[0]-sg[i][1]})).sort((a,b)=>b.g-a.g).slice(0,P-1).map(x=>x.i).sort((a,b)=>a-b);sp=[];let a=0;for(const g of gi){sp.push([sg[a][0],sg[g][1]]);a=g+1}sp.push([sg[a][0],sg[sg.length-1][1]])}
 else{const a0=sg[0][0],a1=sg[sg.length-1][1],ch=ph.map(p=>p.reduce((s,k)=>s+wl(k),0)),tt=ch.reduce((a,b)=>a+b,0);let c=a0;sp=ch.map(x=>{const s=[c,c+(a1-a0)*x/tt];c=s[1];return s})}
 const A=[];ph.forEach((p,pi)=>{const[s,e]=sp[pi],ch=p.map(wl),tt=ch.reduce((a,b)=>a+b,0);let c=s;p.forEach((k,j)=>{A.push([c,k.s]);c+=(e-s)*ch[j]/tt});A.push([e,p[p.length-1].e]);if(pi==ph.length-1&&tp)A.push([e+tp,L.d-.45])});
 const start=Math.max(0,sg[0][0]-.15),end=Math.min(an.dur,sg[sg.length-1][1]+.35+tp);A.unshift([start,0]);A.push([end,L.d]);
 for(let i=1;i<A.length;i++){if(A[i][0]<A[i-1][0]+.01)A[i][0]=A[i-1][0]+.01;if(A[i][1]<A[i-1][1])A[i][1]=A[i-1][1]}return{A,start,end}}
const mapA=(L,R,ta)=>{const A=R.A;if(ta<=A[0][0])return L.t;for(let i=1;i<A.length;i++)if(ta<A[i][0]){const a=A[i-1],b=A[i];return L.t+a[1]+(b[1]-a[1])*(ta-a[0])/(b[0]-a[0])}return L.t+L.d};
async function setRec(L,blob,an,save){const al=anchors(L,an),url=URL.createObjectURL(blob);const o=LA[lid(L)];if(o)URL.revokeObjectURL(o.url);
 LA[lid(L)]=Object.assign({blob,an,url,a:new Audio(url)},al);if(save)await dbPut(lid(L),{blob,an})}
/* ---------- حفظ في المتصفح ---------- */
let DB=null;const db=()=>DB||(DB=new Promise((res,rej)=>{try{const r=indexedDB.open('khutwa_rec',1);r.onupgradeneeded=()=>r.result.createObjectStore('a');r.onsuccess=()=>res(r.result);r.onerror=()=>rej(r.error)}catch(e){rej(e)}}));
async function dbPut(k,v){try{const d=await db();await new Promise(r=>{const tx=d.transaction('a','readwrite');v===null?tx.objectStore('a').delete(k):tx.objectStore('a').put(v,k);tx.oncomplete=tx.onerror=r})}catch(e){}}
async function dbLoad(){try{const d=await db();await new Promise(r=>{const q=d.transaction('a').objectStore('a').openCursor();q.onsuccess=async()=>{const c=q.result;if(!c){r();return}if(String(c.key).startsWith(KEY)){const L=TL.find(l=>lid(l)==c.key);if(L&&c.value&&c.value.blob)setRec(L,c.value.blob,c.value.an,false)}c.continue()};q.onerror=r})}catch(e){}}
/* ---------- التسجيل ---------- */
async function recStart(){if(recOn)return;lstop();stop();const L=TL[li];
 const AO={audio:{echoCancellation:false,noiseSuppression:true,autoGainControl:true}};try{stream=stream||await navigator.mediaDevices.getUserMedia(AO).catch(e=>{if(window.parent!==window)return parent.navigator.mediaDevices.getUserMedia(AO);throw e})}catch(e){say('المايك مش متاح. اسمح للصفحة تستعمل المايك (ولو فاتح الملف جوه برنامج، افتحه في Chrome).');return}
 const ch=[];mr=new MediaRecorder(stream);mr.ondataavailable=e=>e.data.size&&ch.push(e.data);
 mr.onstop=async()=>{const blob=new Blob(ch,{type:mr.mimeType||'audio/webm'});say('بقيس صوتك…');let an;try{an=await analyze(blob)}catch(e){say('مقدرتش أقرا التسجيل، عيده.');return}
  if(!an.segs.length){say('مسمعتش صوت في التسجيل ده. قرّب من المايك وعيده (Enter).');seek(L.t);return}
  await setRec(L,blob,an,true);const dur=(LA[lid(L)].end-LA[lid(L)].start).toFixed(1);say(`✓ اتسجلت «${L.id}» (${dur} ث، ${an.segs.length} مقطع صوت) والرسم اتظبط عليها.`);
  if($$('#lrAuto').checked&&li<TL.length-1){pick(li+1);setTimeout(recStart,450)}else{show();lplay(li,true)}};
 seek(L.t);mr.start();recOn=true;$$('#lrRec').classList.add('on');$$('#lrRec').textContent='■ خلّصت (Enter)';say('🔴 بيسجّل… قول الجملة، ولما تخلص دوس Enter.');
 const t0=performance.now();const pv=now=>{if(!recOn)return;T=Math.min(L.t+L.d-.02,L.t+(now-t0)/1000);render();requestAnimationFrame(pv)};requestAnimationFrame(pv)}
function recStop(){if(!recOn)return;recOn=false;$$('#lrRec').classList.remove('on');$$('#lrRec').textContent='● سجّل الجملة (Enter)';mr&&mr.state!='inactive'&&mr.stop()}
/* ---------- التشغيل بصوتك ---------- */
function lineAt(t){let l=null;for(const x of LINES)if(t>=x.t-1e-6)l=x;return l}
function lplay(i,only,full){lstop();stop();ac();const L=TL[i];const t0=full?0:only?L.t:slideOf(L).t;seek(t0);lp={L:null,a:null,R:null,last:performance.now(),only:only?L:null,stopAt:only?L.t+L.d-.01:full?END:(SL[SL.indexOf(slideOf(L))+1]||{t:END}).t};requestAnimationFrame(lstep)}
function lstep(now){if(!lp)return;const dt=Math.max(0,Math.min(.1,(now-lp.last)/1000));lp.last=now;const prev=T;
 if(lp.a){T=mapA(lp.L,lp.R,lp.a.currentTime);if(lp.a.ended||lp.a.currentTime>=lp.R.end){lp.a.pause();lp.a=null;T=lp.L.t+lp.L.d}}
 else{let nT=T+dt;const nx=LINES.find(l=>l.t>T+1e-6&&l.t<=nT);if(nx)nT=nx.t;T=nT}
 if(!lp.a){const C=lineAt(T);if(C&&C!==lp.L){lp.L=C;const R=C.txt&&LA[lid(C)];if(R){lp.R=R;lp.a=R.a;lp.a.currentTime=R.start;if(DEST&&!R.src){R.src=AC.createMediaElementSource(R.a);R.src.connect(BUS)}lp.a.play().catch(()=>{});T=C.t}}}
 if(SFXG)SFXG.gain.value=lp.a?.3:1;for(const e of SFX)if(e.t>prev&&e.t<=T)sfx(e.k);
 if(T>=lp.stopAt-1e-6||T>=END){T=Math.min(T,END);render();lend();return}render();requestAnimationFrame(lstep)}
function lstop(){if(lp){lp.a&&lp.a.pause();lp=null}}
function lend(){const was=lp;lstop();if(vrec&&was&&was.full!==false)vstop()}
/* ---------- تصدير ---------- */
function wav(buf){const n=buf.length,sr=buf.sampleRate,d=buf.getChannelData(0),b=new ArrayBuffer(44+n*2),v=new DataView(b);const w=(o,s)=>[...s].forEach((c,i)=>v.setUint8(o+i,c.charCodeAt(0)));
 w(0,'RIFF');v.setUint32(4,36+n*2,true);w(8,'WAVE');w(12,'fmt ');v.setUint32(16,16,true);v.setUint16(20,1,true);v.setUint16(22,1,true);v.setUint32(24,sr,true);v.setUint32(28,sr*2,true);v.setUint16(32,2,true);v.setUint16(34,16,true);w(36,'data');v.setUint32(40,n*2,true);
 for(let i=0;i<n;i++)v.setInt16(44+i*2,Math.max(-1,Math.min(1,d[i]))*32767,true);return new Blob([b],{type:'audio/wav'})}
const dl=(blob,name)=>{const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download=name;document.body.appendChild(a);a.click();setTimeout(()=>a.remove(),500)};
const fname=s=>'khutwa_'+(slideOf(TL[0]).name.split(' ')[0]||'board').replace(/[^\w؀-ۿ]+/g,'_')+s;
async function exportWav(){const x=ac();say('بجهّز الصوت…');const parts=[];let tot=0;const sr=44100;
 for(const L of LINES){const R=L.txt&&LA[lid(L)];if(R){const b=await x.decodeAudioData(await R.blob.arrayBuffer());parts.push({b,s:R.start,e:R.end});tot+=R.end-R.start}else{parts.push({sil:L.d});tot+=L.d}}
 const oc=new OfflineAudioContext(1,Math.ceil(tot*sr),sr);let c=0;for(const p of parts){if(p.sil){c+=p.sil;continue}const s=oc.createBufferSource();s.buffer=p.b;s.connect(oc.destination);s.start(c,p.s,p.e-p.s);c+=p.e-p.s}
 dl(wav(await oc.startRendering()),fname('_voice.wav'));say('✓ نزل الصوت كله بنفس توقيت «السبورة كلها بصوتي».')}
async function exportVid(){if(!TL.some(l=>LA[lid(l)])){say('سجّل جمل الأول.');return}
 let ds;const DO={video:{frameRate:30},audio:false,preferCurrentTab:true,selfBrowserSurface:'include'};try{ds=await navigator.mediaDevices.getDisplayMedia(DO).catch(e=>{if(window.parent!==window)return parent.navigator.mediaDevices.getDisplayMedia(DO);throw e})}catch(e){say('تصدير الفيديو محتاج تسمح بتصوير التاب (افتح الملف في Chrome).');return}
 try{const ct=await CropTarget.fromElement($$('#stage'));await ds.getVideoTracks()[0].cropTo(ct)}catch(e){}
 const x=ac();DEST=DEST||x.createMediaStreamDestination();BUS.connect(DEST);
 const ms=new MediaStream([...ds.getVideoTracks(),...DEST.stream.getAudioTracks()]);const mt=['video/webm;codecs=vp9,opus','video/webm;codecs=vp8,opus','video/webm'].find(t=>MediaRecorder.isTypeSupported(t));
 const ch=[];vrec=new MediaRecorder(ms,{mimeType:mt,videoBitsPerSecond:6e6});vrec.ondataavailable=e=>e.data.size&&ch.push(e.data);
 vrec.onstop=()=>{ds.getTracks().forEach(t=>t.stop());document.body.classList.remove('rec');dl(new Blob(ch,{type:'video/webm'}),fname('.webm'));say('✓ الفيديو نزل.');vrec=null};
 document.body.classList.add('rec');$$('#lr').style.display='none';say('');await new Promise(r=>setTimeout(r,900));vrec.start(500);lplay(0,false,true)}
function vstop(){if(vrec&&vrec.state!='inactive')setTimeout(()=>{vrec.stop();$$('#lr').style.display=''},700)}
/* ---------- ملف التسجيلات ---------- */
async function saveFile(){const o={key:KEY,lines:{}};for(const L of TL){const R=LA[lid(L)];if(!R)continue;const b=new Uint8Array(await R.blob.arrayBuffer());let s='';for(let i=0;i<b.length;i+=32768)s+=String.fromCharCode.apply(null,b.subarray(i,i+32768));o.lines[L.id+'#'+L.ix]={type:R.blob.type,an:R.an,b64:btoa(s)}}
 dl(new Blob([JSON.stringify(o)],{type:'application/json'}),fname('_recordings.json'));say('✓ اتحفظ ملف التسجيلات.')}
async function loadFile(f,txt){try{const o=JSON.parse(txt||await f.text());let n=0;for(const L of TL){const v=o.lines&&o.lines[L.id+'#'+L.ix];if(!v)continue;const s=atob(v.b64),u=new Uint8Array(s.length);for(let i=0;i<s.length;i++)u[i]=s.charCodeAt(i);await setRec(L,new Blob([u],{type:v.type}),v.an,true);n++}say(`✓ اتفتح ${n} تسجيل.`);show()}catch(e){console.log('lrec load',e);say('الملف ده مش ملف تسجيلات السبورة دي.')}}
/* ---------- الأزرار ---------- */
$$('#lrT').onclick=()=>{const p=$$('#lrp');p.hidden=!p.hidden;if(!p.hidden){stop();li=Math.max(0,TL.indexOf(lineAt(T)&&lineAt(T).txt?lineAt(T):TL.find(l=>l.t>=T)||TL[0]));pick(li)}};
$$('#lrRec').onclick=()=>recOn?recStop():recStart();$$('#lrPrev').onclick=()=>pick(li-1);$$('#lrNext').onclick=()=>pick(li+1);
$$('#lrPlay').onclick=()=>lplay(li,true);$$('#lrAll').onclick=()=>lplay(li,false);$$('#lrFull').onclick=()=>lplay(0,false,true);
$$('#lrWav').onclick=exportWav;$$('#lrVid').onclick=exportVid;$$('#lrSave').onclick=saveFile;$$('#lrLoad').onchange=e=>{e.target.files[0]&&loadFile(e.target.files[0]);e.target.value=''};
$$('#lrDel').onclick=async()=>{const L=TL[li];if(!LA[lid(L)])return;URL.revokeObjectURL(LA[lid(L)].url);delete LA[lid(L)];await dbPut(lid(L),null);say('اتمسح تسجيل الجملة دي.');show()};
addEventListener('keydown',e=>{if($$('#lrp').hidden||e.target.tagName=='INPUT')return;
 if(e.key=='Enter'){e.preventDefault();e.stopImmediatePropagation();recOn?recStop():recStart()}
 else if(e.key=='ArrowLeft'){e.preventDefault();e.stopImmediatePropagation();pick(li+1)}else if(e.key=='ArrowRight'){e.preventDefault();e.stopImmediatePropagation();pick(li-1)}
 else if(e.key=='p'||e.key=='P'||e.key=='ح'){e.stopImmediatePropagation();lplay(li,true)}
 else if(e.key==' '){e.preventDefault();e.stopImmediatePropagation();if(recOn)recStop();else if(lp)lstop();else lplay(li,true)}
 else if(e.key=='Escape'&&vrec){vstop()}},true);
const k0=window.__K||{};window.__LR={LA,TL,anchors,analyze,mapA,setRec,pick,lplay,recStart,recStop,get li(){return li},get lp(){return lp}};
dbLoad().then(async()=>{const pre=document.getElementById('lrecData');if(pre&&!TL.some(l=>LA[lid(l)]))await loadFile(null,pre.textContent);bar();if(TL.some(l=>LA[lid(l)])){const n=TL.filter(l=>LA[lid(l)]).length;$$('#lrT').textContent='🎙 سجّل جملة جملة ('+n+' متسجلة)'}});
})();
