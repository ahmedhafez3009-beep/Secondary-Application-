// Records the Khutwa walkthrough: one webm per scene page, with step time markers.
const {chromium,devices}=require('playwright');const fs=require('fs');const path=require('path');
const BASE='https://ahmedhafez3009-beep.github.io/Secondary-Application-/';const SITE='/home/claude/khutwa/site/';
const MIME={html:'text/html; charset=utf-8',js:'application/javascript',json:'application/json',png:'image/png',svg:'image/svg+xml',webmanifest:'application/manifest+json',txt:'text/plain',css:'text/css'};const OUT='/home/claude/khutwa/promo/rec/raw/';
fs.mkdirSync(OUT,{recursive:true});
const TOUCH=`(()=>{const st=document.createElement('style');st.textContent='.kwT{position:fixed;z-index:2147483647;pointer-events:none;border-radius:50%;border:5px solid #1EA05F;background:rgba(30,160,95,.22);transform:translate(-50%,-50%)}';
document.addEventListener('DOMContentLoaded',()=>document.head.appendChild(st));
window.__aim=(x,y)=>{const d=document.createElement('div');d.className='kwT';d.style.left=x+'px';d.style.top=y+'px';d.style.width='70px';d.style.height='70px';d.style.opacity='0';document.body.appendChild(d);
 d.animate([{opacity:0,width:'110px',height:'110px'},{opacity:1,width:'56px',height:'56px'}],{duration:420,fill:'forwards',easing:'ease-out'});setTimeout(()=>{d.animate([{opacity:1,width:'56px',height:'56px'},{opacity:0,width:'120px',height:'120px'}],{duration:500,fill:'forwards'});setTimeout(()=>d.remove(),520)},620)};})();`;
let META={scenes:[]};let cur=null,t0=0;
const W=ms=>new Promise(r=>setTimeout(r,ms));
function mark(key){cur.steps.push({key,t:(Date.now()-t0)/1000});console.log('  step',key)}
async function tap(p,sel,o={}){const el=typeof sel==='string'?p.locator(sel).first():sel;await el.scrollIntoViewIfNeeded({timeout:4000}).catch(()=>{});await W(150);const b=await el.boundingBox();if(!b)throw new Error('no box '+sel);
 const x=b.x+b.width/2,y=b.y+b.height/2;await p.evaluate(([x,y])=>window.__aim(x,y),[x,y]);await W(450);if(o.check)await el.check({force:true}).catch(()=>el.click());else await el.click({force:!!o.force}).catch(()=>p.mouse.click(x,y));await W(o.after||900)}
async function aim(p,sel){const el=typeof sel==='string'?p.locator(sel).first():sel;await el.scrollIntoViewIfNeeded({timeout:4000}).catch(()=>{});const b=await el.boundingBox();if(b)await p.evaluate(([x,y])=>window.__aim(x,y),[b.x+b.width/2,b.y+b.height/2]);await W(1100)}
async function type(p,sel,txt){const el=typeof sel==='string'?p.locator(sel).first():sel;await tap(p,el,{after:200});await el.fill('');await el.pressSequentially(txt,{delay:85});await W(500)}
async function scrollTo(p,sel,off=-120){const el=typeof sel==='string'?p.locator(sel).first():sel;let y;try{y=await el.evaluate((e,off)=>e.getBoundingClientRect().top+scrollY+off,off,{timeout:4000})}catch(e){console.log('  scrollTo miss',String(sel).slice(0,80));return}const from=await p.evaluate(()=>scrollY);const n=18;for(let i=1;i<=n;i++){const k=i/n,e=k*k*(3-2*k);await p.evaluate(v=>scrollTo(0,v),from+(y-from)*e);await W(28)}await W(500)}
async function top(p){const from=await p.evaluate(()=>scrollY);for(let i=1;i<=12;i++){await p.evaluate(v=>scrollTo(0,v),from*(1-i/12));await W(25)}await W(300)}
async function scene(ctx,name,fn,o={}){if(process.env.ONLY&&!process.env.ONLY.split(',').includes(name))return;const p=await ctx.newPage();t0=Date.now();cur={name,steps:[],video:null};
 await p.goto(BASE+(o.url!==undefined?o.url:'app/'));await p.waitForLoadState('networkidle').catch(()=>{});await W(900);cur.ready=(Date.now()-t0)/1000;
 try{await fn(p)}catch(e){console.log('ERR',name,e.message.split('\n')[0])}
 await W(800);cur.end=(Date.now()-t0)/1000;const v=p.video();await p.close();cur.video=path.basename(await v.path());META.scenes.push(cur);console.log('scene',name,cur.steps.length,'steps',cur.end.toFixed(1)+'s')}
(async()=>{const b=await chromium.launch();
 const mk=async(dev)=>{const c=await b.newContext({...(dev||{viewport:{width:390,height:844},deviceScaleFactor:2,isMobile:true,hasTouch:false}),serviceWorkers:'block',locale:'ar-EG',acceptDownloads:true,recordVideo:{dir:OUT,size:{width:390,height:844}}});await c.addInitScript(TOUCH);await c.grantPermissions(['clipboard-read','clipboard-write'],{origin:'https://ahmedhafez3009-beep.github.io'});
   await c.route('**/*',async r=>{const u=new URL(r.request().url());if(u.host==='ahmedhafez3009-beep.github.io'){let f=decodeURIComponent(u.pathname.replace('/Secondary-Application-/',''));if(!f||f.endsWith('/'))f+='index.html';const fp=SITE+f;if(fs.existsSync(fp)){return r.fulfill({status:200,body:fs.readFileSync(fp),headers:{'content-type':MIME[fp.split('.').pop()]||'application/octet-stream'}})}return r.fulfill({status:404,body:''})}return r.abort()});
   c.on('page',pg=>{pg.on('popup',pp=>pp.close().catch(()=>{}))});
   await c.addInitScript(()=>{window.open=()=>null;});return c};
 const ctx=await mk();
 // 0 landing
 await scene(ctx,'landing',async p=>{mark('hook');for(let i=1;i<=60;i++){await p.evaluate(v=>scrollTo(0,v),i*4);await W(40)}mark('scroll');await scrollTo(p,'#install');await W(1800);mark('open');await top(p);await tap(p,'a.cta',{after:1500})},{url:'index.html'});
 // 1 setup
 await scene(ctx,'setup',async p=>{mark('name');await type(p,'#setupName','يوسف');mark('gender');await tap(p,'#setupGender [data-g="m"]');await tap(p,'#setupNext1',{after:900});
  mark('year');await tap(p,'#setupStages .opt[data-k="g3"]');await tap(p,'#setupNext2',{after:900});
  mark('track');await tap(p,'#setupOpts .opt >> nth=0');await tap(p,'#setupGo',{after:1000});
  mark('contacts');await type(p,'#setupContacts [data-cnum="0"]','01000000000');await tap(p,'#setupGo4',{after:1800});mark('home');await W(1500)});
 // 2 android install card
 await scene(ctx,'android',async p=>{await p.evaluate(()=>{const e=new Event('beforeinstallprompt');e.prompt=()=>{};e.userChoice=new Promise(r=>setTimeout(()=>r({}),800));window.dispatchEvent(e)});await W(600);mark('card');await scrollTo(p,'#installCard',-80);await W(800);mark('tap');await tap(p,'#installBtn',{after:1500})});
 // 11 iPhone
 const state=await (async()=>{const p=await ctx.newPage();await p.goto(BASE+'app/');const s=await p.evaluate(()=>localStorage.getItem('khutwa-v1'));await p.close();return s})();
 const ic=await mk({viewport:{width:390,height:844},deviceScaleFactor:2,isMobile:true,hasTouch:false,userAgent:devices['iPhone 13'].userAgent});const ip0=await ic.newPage();await ip0.goto(BASE+'app/');await ip0.evaluate(s=>localStorage.setItem('khutwa-v1',s),state);await ip0.close();
 await scene(ic,'ios',async p=>{await W(1200);mark('card');await scrollTo(p,'#installCard',-80).catch(()=>{});await W(2500)});
 // 3 curriculum
 await scene(ctx,'curr',async p=>{mark('tab');await tap(p,'nav [data-p="curr"]',{after:1200});
  mark('subject');await tap(p,'#subjTabs button >> nth=2',{after:1200});
  mark('part');await tap(p,'#subjTabs button >> nth=1',{after:900});const pt=p.locator('#partTabs button');if(await pt.count()>1){await tap(p,pt.nth(1));await tap(p,pt.nth(0))}await tap(p,'#subjTabs button >> nth=2',{after:900});
  mark('unit');const u=p.locator('#units details summary').first();await p.evaluate(()=>document.querySelectorAll('#units details').forEach(d=>d.open=false));await tap(p,u,{after:1000});
  const sb=s=>p.locator('#units details[open] .topic').first().locator('button.sb[data-s="'+s+'"]');
  mark('listen');await tap(p,sb('l'));mark('understand');await tap(p,sb('u'));mark('solve');await tap(p,sb('s'));mark('review');await tap(p,sb('r'),{after:1600});
  mark('prior');await tap(p,p.locator('#units details[open] [data-prior]').first(),{after:1500});
  mark('timer');await tap(p,p.locator('#units details[open] [data-tm]').nth(2),{after:2200});await tap(p,'#tmPause',{after:900});await tap(p,'#tmStop',{after:1200});
  mark('mist');await tap(p,p.locator('#units details[open] [data-mi]').nth(2),{after:900});await type(p,'#mQ','قانون أوم: ت = ج ÷ م');await type(p,'#mA','التيار = الجهد ÷ المقاومة');await tap(p,'#mAdd',{after:1000});await tap(p,'#toolClose');
  mark('links');await tap(p,p.locator('#units details[open] [data-li]').nth(2),{after:900}).catch(async()=>{await tap(p,p.locator('#units details[open] .ttools button').nth(8))});await type(p,'#lT','فيديو شرح الدرس');await type(p,'#lU','https://youtube.com/');await tap(p,'#lAdd',{after:1000});await tap(p,'#toolClose');
  mark('addlesson');const ta=p.locator('#units details[open] textarea[data-add]').first();await type(p,ta,'درس مراجعة إضافي');await tap(p,p.locator('#units details[open] [data-addbtn]').first(),{after:1400});
  mark('edit');await tap(p,p.locator('#units details[open] [data-ren]').nth(1),{after:900});await tap(p,'#dlgNo',{after:600});await aim(p,p.locator('#units details[open] [data-del]').nth(1));const pu=p.locator('#units details[open] [data-prioru]').first();if(await pu.count())await aim(p,pu);
  mark('newunit');await type(p,'#newUnit','وحدة المراجعة النهائية');await W(800)});
 // bulk progress (video discarded)
 await scene(ctx,'_bulk',async p=>{await p.click('nav [data-p="curr"]');await W(300);const n=await p.locator('#subjTabs button').count();
  for(let s=0;s<n;s++){await p.locator('#subjTabs button').nth(s).click();await W(120);await p.evaluate(()=>document.querySelectorAll('#units details').forEach(d=>d.open=true));
   const k=[22,16,12,10,8,6,5][s%7];for(let j=0;j<k;j++){const bt=p.locator('#units button.sb:not(.on)').first();if(await bt.count())await bt.click({timeout:1500}).catch(()=>{})}}
  // backdate some finished lessons so reviews are due, and spread steps over past days
  await p.evaluate(()=>{const k='khutwa-v1';const s=JSON.parse(localStorage.getItem(k));const ids=Object.keys(s.prog);const today=new Date();
   ids.forEach((id,i)=>{const back=(i%12);const d=new Date(today-back*864e5).toISOString().slice(0,10);for(const st of ['l','u','s','r'])if(s.prog[id][st]&&s.prog[id][st]!=='P')s.prog[id][st]=d});
   localStorage.setItem(k,JSON.stringify(s))});await p.reload();await W(800)});
 // 5 plan
 await scene(ctx,'plan',async p=>{mark('tab');await tap(p,'nav [data-p="plan"]',{after:1000});
  mark('goal');await type(p,'#goalPct','80');await p.dispatchEvent('#goalPct','change');const gd=new Date(Date.now()+40*864e5).toISOString().slice(0,10);await tap(p,'#goalDate',{after:200});await p.fill('#goalDate',gd);await p.dispatchEvent('#goalDate','change');await W(1600);
  mark('week');await scrollTo(p,'#weekPlan',-90);await W(600);const wb=p.locator('#weekPlan [data-pid]').first();if(await wb.count())await tap(p,wb,{after:1300});
  mark('exams');await scrollTo(p,'#exTitle',-120);await type(p,'#exTitle','شهري فيزياء');const ed=new Date(Date.now()+23*864e5).toISOString().slice(0,10);await tap(p,'#exDate',{after:200});await p.fill('#exDate',ed);await p.dispatchEvent('#exDate','change');await tap(p,'#exAdd',{after:1500});
  mark('exammode');await scrollTo(p,'#examMode',-160);await tap(p,'#examMode',{after:1400});
  mark('rev');await scrollTo(p,'#revStats',-160);await W(1600)});
 // 4 home
 await scene(ctx,'home',async p=>{mark('tab');await tap(p,'nav [data-p="home"]',{after:1000});mark('levels');await top(p);await aim(p,'#lvlName');await W(600);mark('quote');await tap(p,'#qNext',{after:1400});mark('exambanner');await scrollTo(p,'#examBanner',-200);await W(1400);
  mark('time');await scrollTo(p,'#timeStart',-200);await W(1000);
  mark('ring');await scrollTo(p,p.locator('h3',{hasText:'كام %'}).first(),-60);await W(1500);
  mark('tiles');await scrollTo(p,p.locator('text=إجمالي أيام المذاكرة').first(),-200);await W(1500);
  mark('subjects');await scrollTo(p,p.locator('h3',{hasText:'تقدمك في كل مادة'}).first(),-40);await W(1600);
  mark('reviews');await scrollTo(p,p.locator('h3',{hasText:'مراجعات النهارده'}).first(),-40);await W(800);const rb=p.locator('#revCard button').first();if(await rb.count())await tap(p,rb,{after:1300});
  mark('tasks');await scrollTo(p,'#today',-60);await tap(p,p.locator('#today button').first(),{after:1500});
  mark('range');await scrollTo(p,'#rPresets',-140);await tap(p,'#rPresets button >> nth=0',{after:900});const d=new Date(Date.now()-14*864e5).toISOString().slice(0,10);await tap(p,'#rFrom',{after:300});await p.fill('#rFrom',d);await p.dispatchEvent('#rFrom','change');await W(1200);
  mark('charts');await scrollTo(p,p.locator('h3',{hasText:'خطواتك في الفترة'}).first(),-40);await W(1600);await scrollTo(p,p.locator('h3',{hasText:'نسبة المنهج في الفترة'}).first(),-40);await W(1400);
  mark('pace');await scrollTo(p,p.locator('h3',{hasText:'الوتيرة المطلوبة'}).first(),-40);await W(1600)});
 // 6 attendance (+ enable monthly in settings first, hidden)
 await scene(ctx,'_monthly',async p=>{await p.click('nav [data-p="set"]');await W(300);await p.check('#sMonthly').catch(()=>{});await W(300)});
 await scene(ctx,'att',async p=>{mark('tab');await tap(p,'nav [data-p="att"]',{after:1200});
  mark('week');await scrollTo(p,'#attWeek',-150);await tap(p,'#attWeek',{after:1300});
  mark('absent');const ab=p.locator('#attList [data-v="a"]').nth(1);await tap(p,ab,{after:1100});mark('holiday');await tap(p,p.locator('#attList [data-v="h"]').nth(2),{after:1100});
  mark('older');await scrollTo(p,'#attMore',-300);await tap(p,'#attMore',{after:1300});
  mark('rate');await top(p);await W(1600);
  mark('monthly');await scrollTo(p,'#monthlyCard',-60);await W(500);const mi=p.locator('#mGrid input').first();if(await mi.count()){await tap(p,mi,{after:200});await mi.fill('17');await mi.dispatchEvent('change');}await W(1400);
  mark('info');await scrollTo(p,'#infoCard',-60);await W(1500)});
 // 7 more: tiles, badges, mistakes notebook, share, watch
 let repLink='';
 await scene(ctx,'more',async p=>{mark('tab');await tap(p,'nav [data-p="set"]',{after:1300});
  mark('badges');await tap(p,'[data-go="badges"]',{after:2200});await scrollTo(p,'#badgeGrid',-40);for(let i=0;i<6;i++){await p.mouse.wheel(0,150);await W(140)}await W(800);await tap(p,'[data-p="badges"] [data-back]',{after:800});
  mark('notebook');await top(p);await tap(p,'[data-go="mist"]',{after:1200});await type(p,'#mzQ','تاريخ ثورة 1919');await type(p,'#mzA','مارس 1919');await tap(p,'#mzAdd',{after:1200});
  mark('quiz');await scrollTo(p,'#mqShow',-200).catch(()=>{});await tap(p,'#mqShow',{after:1200});await tap(p,'#mqOk',{after:1300});
  mark('share');await tap(p,'[data-p="mist"] [data-back]',{after:700});await top(p);await tap(p,'[data-go="share"]',{after:1300});await tap(p,'#sendBtns a >> nth=0',{after:1300});
  mark('image');await scrollTo(p,'#imgSave',-420);await W(1200);
  mark('link');await scrollTo(p,'#repCopy',-160);repLink=await p.inputValue('#repLink');await tap(p,'#repCopy',{after:1200});
  mark('msg');await scrollTo(p,'#msgCopy',-260);await tap(p,'#msgCopy',{after:1200});await tap(p,'[data-p="share"] [data-back]',{after:800});
  mark('watch');await top(p);await tap(p,'[data-go="watch"]',{after:1000});await tap(p,'#watchIn',{after:200});await p.fill('#watchIn',repLink);await W(500);await tap(p,'#watchAdd',{after:1800});mark('sort');await tap(p,'#watchSort',{after:300});await p.selectOption('#watchSort',{index:1}).catch(()=>{});await p.dispatchEvent('#watchSort','change').catch(()=>{});await W(1300);await tap(p,'[data-p="watch"] [data-back]',{after:600})});
 fs.writeFileSync(OUT+'replink.txt',repLink);
 // 8 parent report page
 await scene(ctx,'report',async p=>{mark('open');await W(2600);for(let i=0;i<10;i++){await p.mouse.wheel(0,120);await W(120)}await W(800);await aim(p,p.locator('a',{hasText:'جرّب'}).first());},{url:repLink.replace(/^https?:\/\/[^/]+\/[^#]*?(report\.html)/,'$1')||'report.html'});
 // 9 settings
 await scene(ctx,'settings',async p=>{await tap(p,'nav [data-p="set"]',{after:800});
  mark('profile');await scrollTo(p,'#sName',-120);await W(1500);
  mark('contacts');await scrollTo(p,'#saveContacts',-300);await tap(p,'#repDay',{after:600});await tap(p,'#saveContacts',{after:1200});
  mark('dates');await scrollTo(p,'#sStart',-140);await W(900);await scrollTo(p,'#sEval',-60);await tap(p,'#sEval button >> nth=0',{after:1200});
  mark('target');await scrollTo(p,'#sTarget',-200);await aim(p,'#sTarget');await aim(p,'#sMonthly');
  mark('theme');await scrollTo(p,'#sTheme',-140);await tap(p,'#sTheme',{after:200});await p.selectOption('#sTheme','dark');await p.dispatchEvent('#sTheme','change');await W(1600);await p.selectOption('#sTheme','');await p.dispatchEvent('#sTheme','change');await W(700);
  mark('prior');await scrollTo(p,'#pDays',-140);await type(p,'#pDays','25');await p.dispatchEvent('#pDays','change');await W(900);
  mark('backup');await scrollTo(p,'#bExport',-200);await tap(p,'#bExport',{after:1400});await aim(p,'#bImport');await tap(p,p.locator('summary',{hasText:'نسخ يدوي'}),{after:800});await tap(p,'#bCopy',{after:1200});
  mark('reset');await scrollTo(p,'#bReset',-200);await tap(p,'#bReset',{after:1200});await tap(p,'#dlgNo',{after:900});
  mark('about');for(let i=0;i<8;i++){await p.mouse.wheel(0,140);await W(100)}await W(1500)});
 // 10 update toast
 await scene(ctx,'update',async p=>{await p.evaluate(()=>localStorage.setItem('khutwa-curr-seen','1'));await p.reload();await W(450);mark('open');await W(1300);mark('done');await W(1500)});
 fs.writeFileSync(OUT+'meta.json',JSON.stringify(META,null,1));await b.close()})();
