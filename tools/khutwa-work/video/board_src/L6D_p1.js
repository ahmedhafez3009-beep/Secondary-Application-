/* ============ L6D_p1: محرك «قالب ركن الامتحان» (من D_v8_h: السؤال ← طريقة الحل ← الإجابة) — متعدّل لقواعد الدرس ٦: كل كلمة بتتكتب لحظة نطقها ============ */
let CIX=1;const NX=()=>{const r=Math.floor(CIX/3),k=CIX%3,c=r%2?2-k:k;CIX++;go(c,r)};
const SP=S;
const TKS=()=>CUR.filter(k=>!k.p);
const toks=s=>s.replace(/\[\[[\d.]+\]\]/g,' ').trim().split(/\s+/).filter(Boolean);
function TI(sub,n,arr){const t=arr||TKS().map(k=>k.w);let c=0;for(let i=0;i<t.length;i++)if(t[i].includes(sub)){if(c==(n||0))return i;c++}throw new Error('TI: «'+sub+'» مش في: '+t.join(' '))}
const EW=(s,sz)=>s.length*sz*.5;
const MARK0=o=>P(o,'M0,0',N,1,.1);
/* أكبر وقفة في السطر (وقفة التفكير) */
const PZMAX=()=>{const p=CUR.filter(k=>k.p);let b=0;p.forEach((k,i)=>{if(+k.v>+p[b].v)b=i});return b};
function LAY(ws,w,sz,brkSet,w0){const L=[[]];let cw=0;ws.forEach((t,i)=>{const tw=EW(t,sz)+sz*.56,lim=L.length==1&&w0?w0:w;if(L[L.length-1].length&&(cw+tw>lim||(brkSet&&brkSet.has(i)))){L.push([]);cw=0}L[L.length-1].push(i);cw+=tw});return L}
/* كلمات i0..i1 من السطر الحالي، كل كلمة على وقتها (mx=1) */
function FLOW(i0,i1,x,y,w,sz,col,lh,opt={}){const t=TKS(),ws=[];for(let i=i0;i<=i1;i++)ws.push(t[i].w);
 const nl=new Set((opt.nl||[]).map(i=>i-i0)),lines=LAY(ws,w,sz,nl,opt.w0),ch=[],cut=new Set(opt.cut||[]),cf=opt.cf||(()=>col);
 lines.forEach((ln,li)=>{let c=null;ln.forEach(j=>{const i=i0+j;if(!c||c.n>=(opt.mx||1)||cut.has(i)||cf(i)!=c.col){c={a:i,b:i,n:1,ws:[t[i].w],li,col:cf(i)};ch.push(c)}else{c.b=i;c.n++;c.ws.push(t[i].w)}})});
 ch.forEach((c,k)=>{const o=t[c.a].s/OS+(opt.dt||0),s=c.ws.join(' ');if(!k||ch[k-1].li!=c.li)W(o,x,y+c.li*lh,s,sz,c.col);else WC(o,s,c.col);c.it=LASTW});
 return {ch,n:lines.length,last:y+(lines.length-1)*lh}}
function HLR(ch,a,b,o,col,deco){ch.forEach(c=>{if(c.a>=a&&c.b<=b){c.it.hl=T0+o*OS;c.it.hc=col;c.it.hd=deco}})}
const STEP=(o,x,y,n,col)=>{P(o,RR(x,y,30,30,7),col,2.5,.25,'#fff');W(o+.08,x+15,y+22,n,18,col,'middle')};

/* ---- أيقونات الكروت (مركز x,y؛ تقريبًا ٦٠×٦٠): كارت صغير + بادج رقمه + رسمته ---- */
const AD=n=>String(n).replace(/[0-9]/g,d=>'٠١٢٣٤٥٦٧٨٩'[d]);
const HAND4=(x,y,s=1)=>`M${F(x-20*s)},${F(y+18*s)} Q${x},${F(y+26*s)} ${F(x+20*s)},${F(y+18*s)} `+[-14,-5,4,13].map((d,i)=>`M${F(x+d*s-3*s)},${F(y+18*s)} V${F(y-6*s-[2,8,8,3][i]*s)} a${F(3.5*s)},${F(3.5*s)} 0 0,1 ${F(7*s)},0 V${F(y+18*s)} `).join('')+`M${F(x+20*s)},${F(y+18*s)} l${F(8*s)},${F(-10*s)} `;
const HAND5=(x,y,s=1)=>`M${F(x-24*s)},${F(y+18*s)} Q${x},${F(y+26*s)} ${F(x+24*s)},${F(y+18*s)} `+[-18,-9,0,9,18].map((d,i)=>`M${F(x+d*s-3.5*s)},${F(y+18*s)} V${F(y-6*s-[0,7,10,7,2][i]*s)} a${F(3.5*s)},${F(3.5*s)} 0 0,1 ${F(7*s)},0 V${F(y+18*s)} `).join('');
const MAH2=(x,y,s=1)=>`M${F(x-40*s)},${y} h${F(80*s)} l${F(-12*s)},${F(-12*s)} h${F(-56*s)} Z M${F(x-30*s)},${F(y-12*s)} v${F(-20*s)} M${x},${F(y-12*s)} v${F(-20*s)} M${F(x+30*s)},${F(y-12*s)} v${F(-20*s)} M${F(x-36*s)},${F(y-32*s)} h${F(72*s)} L${x},${F(y-50*s)} Z `;
const PFRM=(x,y,w,h)=>RC(x,y,w,h)+RC(x+6,y+6,w-12,h-12);
const CICON={
 5:(x,y)=>[[FLAG(x+12,y+24,.6),G,LGN]],
 7:(x,y)=>[[MAH2(x,y+22,.6),BRN,SAND]],
 8:(x,y)=>[[SPK8(x+10,y-8,.9),FLM,Y],[SAIL(x-10,y+14,.6),N]],
 13:(x,y)=>[[PSEC(x,y,6,24,-Math.PI/2,Math.PI/6)+PSEC(x,y,6,24,Math.PI/6,Math.PI*5/6),BLU,SKY]],
 16:(x,y)=>[[SEAL(x,y+12,13),R,'#fff'],[TREE3(x,y+4,.25).d,G]],
 17:(x,y)=>[[RC(x+8,y-18,18,30),N,'#e9ecee'],[SIEVE(x-6,y+16,.18),GR],[GEM(x-18,y-18,.22),GD,LGN]],
 18:(x,y)=>[[HAND4(x,y,1),FRN,LFR]],
 22:(x,y)=>[[SAIL(x+8,y+16,.55),N],[FLAME(x-16,y+18,.7),R,'#F6B26B']],
 23:(x,y)=>[[PFRM(x-22,y-18,44,40),BRN,CREAM],[HILAL(x-4,y+2,7),G,LGN],[CROSS(x+8,y-6,.4),R]]};
/* MCARD: كارت مرجع صغير (٧٢×٦٤) برقمه ورسمته؛ x,y المركز */
function MCARD(o,x,y,n){P(o,RC(x-34,y-30,68,62),G,3,.3,'#fff');BADGE2(o+.08,x+32,y-28,AD(n),G);(CICON[n]||(()=>[]))(x,y).forEach(([d,c,f],j)=>P(o+.12+j*.08,d,c,2.5,.3,f))}
/* أيقونات تانية للأجزاء */
const ICN={
 track:(x,y)=>[[TRACK(x+34,x-34,y-4,14),TRK],[STN(x+20,y-6,20)+STN(x,y-6,20)+STN(x-20,y-6,20),N]],
 goals:(x,y)=>[[RC(x-26,y-26,52,52),BRN,CREAM],['M'+(x-16)+','+(y-12)+' h32 M'+(x-16)+','+y+' h32 M'+(x-16)+','+(y+12)+' h20',N]],
 hand5:(x,y)=>[[HAND5(x,y-4,1),FRN,LFR]],
 nile:(x,y)=>[[NILE(x-34,y-30,.2),BLU,null],[TORCH(x+18,y+26,.5),BRN,PAP],[FLAME(x+18,y-2,.5),FLM,Y]],
 scale:(x,y)=>[[BALS(x,y-22,.8),N]],
 hands:(x,y)=>[[HAND(x-10,y+6,1.5),N,SKIN],[HAND(x+10,y+6,1.5),G,LGN]],
 eye:(x,y)=>[[EYE(x,y,1.1),BLU,SKY]],
 bal:(x,y)=>[[BALS(x,y-22,.8),GD]],
 ballot:(x,y)=>[[BALLOT(x,y+26,.7),N,'#fff'],[HEART(x,y-14,.45),R,LRD]]};
const DRAWI=(o,k,x,y)=>{if(typeof k=='number')return MCARD(o,x,y,k);ICN[k](x,y).forEach(([d,c,f],j)=>P(o+j*.08,d,c,3,.4,f))};

/* ---- تخطيط السؤال ---- */
const SZS=[[22,34,20,36,21,31],[21,32,19,34,20,29],[20,30,18,32,19,28],[19,28,17,30,18,26],[18,27,16,28,17,25],[17,25,15,26,16,23],[16,24,15,25,15,22]];
function QPARTS(Q){const qt=toks(SP[Q.id+'-س']);
 const rng=(Q.qr||[[null,null,N]]).map(([f,e,c,gp])=>{const a=f==null?qt.findIndex(w=>w.startsWith('«')):TI(f,0,qt);let b;if(e)b=TI(e,0,qt);else{b=qt.length-1;if(Q.ch){b=qt.indexOf('(أ)')-1}}return [a,b,c||N,gp||0]});
 let chs=null;if(Q.ch){chs=['أ','ب','ج','د'].map((l,k,A)=>{const a=qt.indexOf('('+l+')'),b=k<3?qt.indexOf('('+A[k+1]+')')-1:qt.length-1;return {l,a,b}})}
 const at_=toks(SP[Q.id+'-ج']);let a0=Q.a0!=null?TI(Q.a0,0,at_):at_.findIndex(w=>w.startsWith('«')||/^\(.\)$/.test(w));
 const tl=at_.lastIndexOf('ودي');if(tl<0||!at_[tl+2].startsWith('اجتهادية'))throw new Error('QJ: مفيش «ودي إجابة اجتهادية» '+Q.id);
 const end=tl-1,nl=(Q.anl||[]).map(([s,n,bk])=>TI(s,n||0,at_)-(bk||0));
 const t0=tl+3<at_.length?tl+3:-1;   /* ذيل بعد «ودي إجابة اجتهادية» (زي «وأي … مقبول») بيتكتب سطر لوحده */
 return {qt,rng,chs,at:at_,a0,tl,end,nl,t0}}
/* محاكاة لفّ نص طريقة الحل: عدد السطور */
function MLINES(Q,w,sz){let n=1,cw=0,first=true;Q.m.forEach(op=>{if(op[0]=='t'){const ws=op[1].split(/\s+/);ws.forEach(s=>{const tw=EW(s,sz)+sz*.56;if(!first&&cw+tw>w){n++;cw=0}first=false;cw+=tw})}else if(op[0]=='nl'){n++;cw=0;first=true}});return n}
function QLAY(Q){const p=QPARTS(Q),top=Q.top||78,X0=20,X1=1046,bs='اجتهاد · '+Q.ap,bw=EW(bs,15)+24;
 const nic=Q.m.filter(o=>o[0]=='ic').length,slot=nic?Math.max(110,nic*88):0;
 for(const sz of SZS){const [qs,ql,cs,crow,as,al]=sz,qw=X1-56-(X0+50);let qn=0;
  let gq=0;p.rng.forEach(([a,b,c,gp])=>{qn+=LAY(p.qt.slice(a,b+1),qw,qs).length;gq+=gp});
  const qh=Math.max(18+gq+qn*ql+(p.chs?2*crow+4:0)+(Q.qx||0)+10,Q.qmin||110);
  const aw=X1-24-(X0+16),an=LAY(p.at.slice(0,p.end+1),aw,as,new Set(p.nl),aw-bw-50-(Q.jr||0)).length+(p.t0>0?LAY(p.at.slice(p.t0),aw,as).length:0),ah=14+an*al+10;
  const ms=Math.min(19,as+1),ml=MLINES(Q,X1-14-(X0+46+slot+(nic?36:0)),ms),mh=Math.max(nic?100:56,18+ml*(ms+10)+14),tot=qh+8+mh+8+ah;
  if(top+tot<=526||sz==SZS[SZS.length-1]){const y1=top+qh,m0=y1+8,m1=m0+mh,a0=m1+8;return {p,sz,top,X0,X1,qh,qw,bw,bs,ms,slot,nic,q:{y0:top,y1},mb:{x0:X0,x1:X1,y0:m0,y1:m1},ab:{x0:X0,x1:X1,y0:a0,y1:a0+ah},an}}}}
/* (١) السؤال */
function QS(Q){const Lo=QLAY(Q);Q.L=Lo;const {p,sz,X0,X1,qw}=Lo,[qs,ql,cs,crow]=sz,y0=Lo.q.y0,t=TKS();
 if(t.length!=p.qt.length)throw new Error('QS tokens '+Q.id);
 P(.02,RR(X0,y0,X1-X0,Lo.qh,14),N,3,.6,'#fff');STEP(.12,X0+8,y0+8,'١',N);
 P(.05,CI(X1-26,y0+26,17),R,3,.3,R);W(.12,X1-26,y0+33,Q.b,Q.b.length>1?16:20,'#fff','middle');
 if(Q.pg)W(.3,X0+23,y0+62,Q.pg,14,GR,'middle');
 const keyI=(Q.keys||[]).map(([s,n,occ])=>{const a=TI(s,occ||0);return [a,a+(n||1)-1]}),cut=[];keyI.forEach(([a,b])=>cut.push(a,b+1));
 let y=y0+18+ql*.75;Q.F=[];
 p.rng.forEach(([a,b,c,gp])=>{const f=FLOW(a,b,X1-56,y,qw,qs,c,ql,{cut});Q.F.push(f);y=f.last+ql+gp});
 Q.keyI=keyI;y=y-ql+(Q.qx||0);
 if(p.chs){Q.C={};p.chs.forEach(({l,a,b},k)=>{const col=k%2,row=k>>1,cx=col?(X0+X1)/2-22:X1-36,cy=y+crow*(row+1)-4;
  P(t[a].s/OS,CI(cx,cy-7,14),N,2.5,.25,'#fff');W(t[a].s/OS+.05,cx,cy,l,17,N,'middle');
  const f=FLOW(a+1,b,cx-24,cy,440,cs,N,crow);Q.C[l]={f,a,b,cx,cy}})}
 if(CUR.some(k=>k.p)){const i=PZMAX(),v=+CUR.filter(k=>k.p)[i].v;CDR2(atp(i),X0+23,y0+92,13,Math.round(v))}
 if(Q.qf)Q.qf(Lo)}
/* (٢) طريقة الحل. ops:
   ['t',phrase,col,n,strike]  كتابة عبارة منطوقة كلمة بكلمة (n = رقم التكرار في السطر؛ strike = تتشطب بعد آخر كلمة)
   ['nl'] سطر جديد · ['h',k,word,n] تعليم الكلمة المفتاحية k في السؤال · ['x',word,letter,n] شطب اختيار
   ['ok',word,letter,n] تعليم اختيار (فاضل) · ['ic',word,card|icon,label,n] كارت/أيقونة الجزء من الدرس (+سهم) · ['f',word,fn,n] رسم خاص */
function QMT(Q){const Lo=Q.L,b=Lo.mb,sz=Lo.ms,lh=sz+10;
 P(.02,RR(b.x0,b.y0,b.x1-b.x0,b.y1-b.y0,12),YD,2.5,.4,'#FFFBEA');STEP(.08,b.x0+8,b.y0+8,'٢',YD);
 const nic=Lo.nic,slot=Lo.slot,xR=b.x1-14,xL=b.x0+46+slot+(nic?36:0);
 let cy=b.y0+12+sz,cw=0,first=true,ki=0,arrowed=false,lf=null;Q.icp=[];
 const icx=k=>b.x0+46+slot-(k+.5)*(slot/nic),icy=b.y0+(b.y1-b.y0)/2-(Q.m.some(o=>o[0]=='ic'&&o[3])?8:0);
 Q.m.forEach(op=>{const k=op[0];
  if(k=='t'){const ts=FIND(op[1],op[3]),ws=op[1].split(/\s+/).filter(w=>NRM(w)),its=[];
   ws.forEach((s,i)=>{const tw=EW(s,sz)+sz*.56;if(!first&&cw+tw>xR-xL){cy+=lh;cw=0;first=true}
    if(first){W(ts[i],xR,cy,s,sz,op[2]||N);first=false}else{LASTW=lf;WC(ts[i],s,op[2]||N)}lf=LASTW;its.push(LASTW);cw+=tw});
   if(op[4]){const o=ts[ts.length-1]+.35;its.forEach(it=>{it.hl=T0+o*OS;it.hc='#9AA5AE';it.hd='line-through'});MARK0(o)}}
  else if(k=='nl'){cy+=lh;cw=0;first=true}
  else if(k=='h'){const [x,y]=Q.keyI[op[1]],o=at(op[2],op[3]||0);for(const f of Q.F)HLR(f.ch,x,y,o,R,'underline');MARK0(o)}
  else if(k=='x'){const c=Q.C[op[2]],o=at(op[1],op[3]||0);HLR(c.f.ch,c.a,c.b,o,'#9AA5AE','line-through');P(o,XX(c.cx,c.cy-7,1.3),R,4,.3)}
  else if(k=='ok'){const c=Q.C[op[2]],o=at(op[1],op[3]||0);HLR(c.f.ch,c.a,c.b,o,BLU,'underline');P(o,CI(c.cx,c.cy-7,19),BLU,3,.3)}
  else if(k=='ic'){const o=at(op[1],op[4]||0),x=icx(ki),y=icy;Q.icp.push([x,y]);DRAWI(o,op[2],x,y);if(op[3])W(o+.15,x,b.y1-8,op[3],15,GR,'middle');
   if(!arrowed){P(o+.05,ARW(xL-6,y,b.x0+46+slot-2,y,8),GR,3,.3);arrowed=true}ki++}
  else if(k=='f')op[2](at(op[1],op[3]||0),b,Q)});
 if(cy>b.y1-6)console.warn('QM overflow',Q.id,cy,b.y1)}
/* (٣) الإجابة النموذجية: كارت أخضر مسطّر زي ورقة الامتحان + بادج «اجتهاد · ص…» */
function QJ(Q){const Lo=Q.L,b=Lo.ab,p=Lo.p,[qs,ql,cs,crow,as,al]=Lo.sz,t=TKS();if(t.length!=p.at.length)throw new Error('QJ tokens '+Q.id);
 P(.02,RR(b.x0,b.y0,b.x1-b.x0,b.y1-b.y0,12),G,4,.6,'#fff');STEP(.1,b.x0+8,b.y0+8,'٣',G);
 let rl='';for(let i=0;i<Lo.an;i++)rl+=`M${b.x0+16},${F(b.y0+14+al*.72+i*al+8)} H${b.x1-16} `;P(.15,rl,'#CFE3D6',1.5,.6);
 const aw=b.x1-24-(b.x0+16);
 const f=FLOW(0,p.end,b.x1-24,b.y0+14+al*.72,aw,as,N,al,{w0:aw-Lo.bw-50-(Q.jr||0),nl:p.nl,cf:i=>i<p.a0?G:N});
 if(p.t0>0)FLOW(p.t0,t.length-1,b.x1-24,f.last+al,aw,as,GD,al);
 const m=/^\((.)\)$/.exec(t[p.a0].w);if(m&&Q.C){const c=Q.C[m[1]],o=t[p.a0].s/OS;P(o,CI(c.cx,c.cy-7,21),G,4,.4);HLR(c.f.ch,c.a,c.b,o,G,'underline')}
 const o=t[p.tl+2].s/OS,bw=Lo.bw;
 P(o,RR(b.x0+46,b.y0+9,bw,28,14),YD,2.5,.3,'#FFF4D6');W(o+.1,b.x0+46+bw-12,b.y0+29,Lo.bs,15,YD);chime(o);
 if(Q.jf)Q.jf(Lo)}
/* سؤال كامل = ٣ سطور في خلية واحدة */
function QQ(Q){L(Q.id+'-س',()=>QS(Q));L(Q.id+'-ح',()=>QMT(Q));L(Q.id+'-ج',()=>QJ(Q))}
