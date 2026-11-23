/* ============ السبورة D · الفصل الرابع: ركن الامتحان ولوحات «احفظ دي» (D1–D7 + الدرس في دقيقة + التوقيع) ============ */
/* ---- أدوات مساعدة للرسم (مسارات بس، المحرك زي ما هو) ---- */
const BLU='#3E8FCF',BRN='#B8860B',SKY='#DCEEFB',PUR='#8E44AD',CREAM='#FBF3DC',PAP='#F3D9B8',SKIN='#E8C39E',LGN='#d9f0e3',GHO='#b9c0c4',PNK='#F8D7D3';
const L=(id,fn)=>line(id,SRC[id]||'',SP[id],fn);
/* مقاسات الخط ثابتة مهما الكاميرا بعدت (السبورة دي بتبعد ٩ مرات في الآخر، فالتقريب بيبوّظ أماكن WC) */
document.getElementById('world').style.textRendering='geometricPrecision';
const F=n=>+(+n).toFixed(1);
const AN='١٢٣٤٥٦٧٨٩';
/* S: ينقل ويكبّر أي مسار مرسوم حوالين (0,0) — نفس أداة السبورة B */
const S=(d,x,y,s=1)=>d.replace(/([MLHVCQTAZmlhvcqtaz])([^MLHVCQTAZmlhvcqtaz]*)/g,(m,c,a)=>{const n=(a.match(/-?[\d.]+/g)||[]).map(Number),up=c==c.toUpperCase(),C=c.toUpperCase(),f=v=>+v.toFixed(1);let o=[];
 if(C=='Z')return 'Z ';if(C=='H')o=n.map(v=>f(v*s+(up?x:0)));else if(C=='V')o=n.map(v=>f(v*s+(up?y:0)));
 else if(C=='A')for(let i=0;i<n.length;i+=7)o.push(f(n[i]*s),f(n[i+1]*s),n[i+2],n[i+3],n[i+4],f(n[i+5]*s+(up?x:0)),f(n[i+6]*s+(up?y:0)));
 else n.forEach((v,i)=>o.push(f(v*s+(up?(i%2?y:x):0))));return c+o.join(',')+' '});
/* خريطة مصر والنيل (نفس موتيف A45 وC): وحدة 400×300 */
const EGU={W:[[0,300],[0,6]],N:[[0,6],[40,12],[74,8],[131,25],[165,12],[181,5],[205,0],[228,3],[245,10],[280,16],[309,9]],E:[[309,9],[333,66]],AQ:[[333,66],[311,122]],SG:[[311,122],[290,95],[252,52]],RS:[[252,52],[262,80],[296,136],[345,215],[400,300]],
 NL:[[212,300],[240,262],[265,234],[262,200],[259,169],[242,173],[225,150],[208,137],[203,100],[210,48]]};
const mp=(pts,x,y,s)=>pts.map((p,i)=>(i?'L':'M')+(x+p[0]*s).toFixed(0)+','+(y+p[1]*s).toFixed(0)).join(' ')+' ';
const EGO=(x,y,s)=>mp([].concat(EGU.W,EGU.N.slice(1),EGU.E.slice(1),EGU.AQ.slice(1),EGU.SG.slice(1),EGU.RS.slice(1)),x,y,s)+'Z';
const NILE=(x,y,s)=>{const q=EGU.NL.map(p=>[Math.round(x+p[0]*s),Math.round(y+p[1]*s)]);let d=`M${q[0]}`;for(let i=1;i<q.length-1;i++)d+=` Q${q[i]} ${[(q[i][0]+q[i+1][0])/2,(q[i][1]+q[i+1][1])/2]}`;
 const c=q[q.length-1],f=(u,v)=>`${Math.round(x+u*s)},${Math.round(y+v*s)}`;return d+` L${c} M${c} L${f(181,5)} M${c} L${f(228,3)} `};
const EGN=mp(EGU.W.concat(EGU.N.slice(1),EGU.E.slice(1),EGU.AQ.slice(1),EGU.SG.slice(1),EGU.RS.slice(1)).filter((p,i)=>1),0,0,1);
/* أشكال صغيرة */
const RC=(x,y,w,h)=>`M${x},${y} h${w} v${h} h${-w} Z `;
const RR=(x,y,w,h,r=10)=>`M${x+r},${y} h${w-2*r} q${r},0 ${r},${r} v${h-2*r} q0,${r} ${-r},${r} h${-(w-2*r)} q${-r},0 ${-r},${-r} v${-(h-2*r)} q0,${-r} ${r},${-r} Z `;
const TICK=(x,y,s=1)=>`M${F(x-7*s)},${y} l${F(5*s)},${F(5*s)} l${F(9*s)},${F(-10*s)} `;
const XX=(x,y,s=1)=>`M${F(x-7*s)},${F(y-7*s)} l${14*s},${14*s} M${F(x+7*s)},${F(y-7*s)} l${-14*s},${14*s} `;
const ARW=(x1,y1,x2,y2,h=11)=>{const a=Math.atan2(y2-y1,x2-x1);return `M${x1},${y1} L${x2},${y2} M${x2},${y2} L${F(x2-h*Math.cos(a-.5))},${F(y2-h*Math.sin(a-.5))} M${x2},${y2} L${F(x2-h*Math.cos(a+.5))},${F(y2-h*Math.sin(a+.5))} `};
const DROP=(x,y,s=1)=>`M${x},${F(y-13*s)} q${9*s},${11*s} ${9*s},${17*s} a${9*s},${9*s} 0 1,1 ${-18*s},0 q0,${-6*s} ${9*s},${-17*s} Z `;
const PIN=(x,y,s=1)=>`M${x},${y} q${-13*s},${-18*s} ${-13*s},${-28*s} a${13*s},${13*s} 0 1,1 ${26*s},0 q0,${10*s} ${-13*s},${28*s} Z `;
const SHD=(x,y,s=1)=>`M${F(x-12*s)},${F(y-16*s)} h${24*s} v${12*s} q0,${14*s} ${-12*s},${20*s} q${-12*s},${-6*s} ${-12*s},${-20*s} Z `;
const GEAR=(x,y,r)=>CI(x,y,r)+CI(x,y,F(r*.35))+[0,1,2,3,4,5,6,7].map(i=>{const a=i*Math.PI/4;return `M${F(x+r*Math.cos(a))},${F(y+r*Math.sin(a))} L${F(x+r*1.4*Math.cos(a))},${F(y+r*1.4*Math.sin(a))} `}).join('');
const STAR=(x,y,r)=>[0,1,2,3,4,5,6,7,8,9].map(i=>{const a=-Math.PI/2+i*Math.PI/5,q=i%2?r*.42:r;return (i?'L':'M')+F(x+q*Math.cos(a))+','+F(y+q*Math.sin(a))}).join(' ')+' Z ';
const FEN=(x,y,s=1)=>S('M-30,0 h60 M-24,0 v-24 M-10,0 v-20 M4,0 v-20 M18,0 v-20 M-24,-12 h48',x,y,s);
const WV=(x,y,n,w)=>`M${x},${y} q${w/2},${-w*.4} ${w},0 `+Array(n-1).fill(`t${w},0`).join(' ')+' ';
/* عمود المعبد (نفس عمود A وB) + عمود تخين سادة */
const COL=(x,y,h,w=24)=>{const f=v=>+v.toFixed(1);return `M${f(x-w)},${y} V${y+h} M${f(x+w)},${y} V${y+h} M${f(x-w*1.33)},${f(y+h*.08)} Q${x},${f(y+h*.2)} ${f(x+w*1.33)},${f(y+h*.08)} M${f(x-w*.42)},${f(y+h*.18)} V${y+h} M${f(x+w*.42)},${f(y+h*.18)} V${y+h} M${f(x-w*1.5)},${y+h+10} v-10 h${f(w*3)} v10 `};
/* أيقونات الموتيفات (نفس مسارات السبورة B) */
const I={paper:'M-16,-22 h32 v44 h-32 Z M-9,-10 h18 M-9,0 h18 M-9,10 h18',
 bell:'M-18,12 q5,-6 5,-18 q0,-15 13,-15 q13,0 13,15 q0,12 5,18 Z M-5,12 q5,9 10,0 M0,-21 v-6',
 whistle:'M-18,4 a12,12 0 1,0 24,0 a12,12 0 1,0 -24,0 M2,-6 H26 V3 H6 M-10,-10 q0,-9 8,-11',
 scale:'M0,-24 V22 M-14,22 h28 M-26,-16 H26 M-26,-16 l-10,20 h20 Z M26,-16 l-10,20 h20 Z',
 reg:'M-30,-40 h60 v80 h-60 Z M-22,-18 h44 M-22,-2 h44 M-22,14 h44 M-22,28 h44',
 scroll:'M-18,-22 h36 v42 q-18,8 -36,0 Z M-10,-11 h20 M-10,-2 h20 M-10,10 q5,-7 9,0 t9,0',
 house:'M-50,0 L0,-40 L50,0 M-40,-8 V60 H40 V-8 M-10,60 V28 H10 V60',
 hand:'M-80,-12 H-24 q14,-12 26,-3 l-9,8 h17 q8,0 8,7 q0,7 -8,7 h-30 q-8,6 -20,6 H-80',
 plane:'M-30,0 L22,-6 q10,0 10,6 q0,6 -10,6 Z M-6,-3 L-18,-22 h9 L8,-5 M-6,3 L-18,22 h9 L8,5 M-28,0 l-8,-11 h6 l8,10',
 lawbook:'M-20,-16 h34 q6,0 6,6 v26 h-34 q-6,0 -6,-6 Z M-20,10 q0,-6 6,-6 h34 M-8,-8 h18',
 box:'M-18,-6 h36 v24 h-36 Z M-10,-6 v-9 h20 v9 M-6,-14 h12',
 pencil:'M-20,16 l4,-12 l26,-26 l8,8 l-26,26 Z M-16,4 l8,8 M6,-18 l8,8',
 crown:'M-24,0 L-26,-25 H12 L20,-62 L26,-62 L24,0 Z M-18,-25 Q-21,-52 -7,-72 Q6,-52 4,-25',
 bundle:'M-16,34 V-30 M-8,34 V-36 M0,34 V-40 M8,34 V-36 M16,34 V-30 M-16,-30 l-5,-12 M-8,-36 l-3,-12 M0,-40 v-13 M8,-36 l3,-12 M16,-30 l5,-12 M-21,2 h42 v10 h-42 Z',
 cam:'M-34,-18 h20 l6,-10 h18 l6,10 h18 v44 h-68 Z',lens:'M-13,4 a13,13 0 1,0 26,0 a13,13 0 1,0 -26,0',
 lens2:'M-22,-6 a22,22 0 1,0 44,0 a22,22 0 1,0 -44,0 M15,11 L36,34',
 tap:'M-26,-8 h30 q12,0 12,12 v10 h-12 v-8 h-30 Z M-8,-8 v-12 M-20,-20 h24',
 passport:'M-22,-30 h44 v60 h-44 Z M-10,-6 a10,10 0 1,0 20,0 a10,10 0 1,0 -20,0 M-12,16 h24',
 bubble:'M-70,-40 h140 q12,0 12,12 v50 q0,12 -12,12 h-90 l-22,20 v-20 h-28 q-12,0 -12,-12 v-50 q0,-12 12,-12 Z'};
const TAB=(o,x,y,w,t,pg,sz)=>{P(o,RC(x,y,w,40),BRN,3,.5,CREAM);W(o+.2,x+w-12,y+28,t,sz||19,N);if(pg)WC(o+.45,pg,GR)};
const BADGE=(o,x,y,n,col)=>{P(o,CI(x,y,14),col||R,3,.3,'#fff');W(o+.1,x,y+8,n,20,col||R,'middle')};
const chime=o=>SFX.push({t:T0+o*OS,k:'chime'});
const mark=()=>IT.length,OFFS=(a,b,o)=>{for(let i=a;i<b;i++)IT[i].off=T0+o*OS};
const HIDE=(a,b,o1,o2)=>{for(let i=a;i<b;i++)if(IT[i].k=='w')IT[i].h=[T0+o1*OS,T0+o2*OS]};
/* الكرسي بأربع رجول (موتيف الأركان، من B5) بمنظور يبيّن الرجول الأربعة؛ الرجول بترتيب الأركان ①..④ من اليمين */
function CH2(cx,cy,s=1,ang=0){const px=80,py=55,a=ang*Math.PI/180,c=Math.cos(a),sn=Math.sin(a),q=(x,y)=>{const dx=x-px,dy=y-py;return [F(cx+s*(px+dx*c-dy*sn)),F(cy+s*(py+dx*sn+dy*c))]},p=(x,y)=>q(x,y).join(',');
 const LG=[[80,-30,80,55],[40,0,40,90],[-20,-30,-20,55],[-60,0,-60,90]];
 return {body:`M${p(-60,0)} L${p(40,0)} L${p(80,-30)} L${p(-20,-30)} Z M${p(-20,-30)} L${p(-20,-130)} L${p(80,-130)} L${p(80,-30)} M${p(-20,-96)} L${p(80,-96)} `,
  legs:LG.map(([x1,y1,x2,y2])=>`M${p(x1,y1+(y1?0:0))} L${p(x2,y2)} `),mid:LG.map(([x1,y1,x2,y2])=>q(x1,(y1+y2)/2+8)),tip:LG.map(([x1,y1,x2,y2])=>q(x2,y2)),top:q(30,-130)}}
/* الأرض الثابتة (المقومات): سطح + وش فيه ٦ خانات */
function GND(cx,cy,s=1){const p=(x,y)=>F(cx+s*x)+','+F(cy+s*y);
 return {top:`M${p(-110,100)} L${p(-60,45)} L${p(140,45)} L${p(90,100)} `,front:`M${p(-110,100)} L${p(-110,140)} L${p(90,140)} L${p(90,100)} Z `,side:`M${p(90,140)} L${p(140,85)} L${p(140,45)} `,
  cuts:[1,2,3,4,5].map(i=>`M${p(90-i*200/6,100)} L${p(90-i*200/6,140)} `).join(''),num:[0,1,2,3,4,5].map(i=>[F(cx+s*(90-(i+.5)*200/6)),F(cy+s*128)])}}
/* يرسم الأرض كلها */
const GDRAW=(o,g,col=BRN)=>{P(o,g.top,col,4,.5);P(o+.25,g.front,col,4,.5,SAND);P(o+.4,g.side,col,4,.3)};
const LEGC=[G,N,R,YD];
/* البيت (موتيف السيادة) */
const HOU=(x,y,s=1)=>S(I.house,x,y,s);

const pauseIc=(x,y)=>CI(x,y,15)+`M${x-5},${y-7} v14 M${x+5},${y-7} v14 `;

/* ================= محرك «قالب ركن الامتحان» (v8) =================
   كل سؤال = خلية: كارت السؤال (١) ← شريط طريقة الحل (٢) ← كارت الإجابة النموذجية الأخضر (٣).
   النص بيتكتب كلمة بكلمة مع النطق (FLOW: كل ≤٣ كلمات = W/WC على وقت أول كلمة فيهم).
   التعليم على كلمة/اختيار: خاصية hl على عنصر النص (لون + خط تحت/شطب) — باتش صغير في المحرك. */
const TKS=()=>CUR.filter(k=>!k.p);
const toks=s=>s.replace(/\[\[[\d.]+\]\]/g,' ').trim().split(/\s+/).filter(Boolean);
function TI(sub,n,arr){const t=arr||TKS().map(k=>k.w);let c=0;for(let i=0;i<t.length;i++)if(t[i].includes(sub)){if(c==(n||0))return i;c++}throw new Error('TI: «'+sub+'» مش في: '+t.join(' '))}
const TOFF=i=>TKS()[i].s/OS;
const EW=(s,sz)=>s.length*sz*.5;           /* تقدير عرض النص (أوسع شوية من الحقيقي، عشان Lalezar) */
const MARK0=o=>P(o,'M0,0',N,1,.1);           /* لحظة تغيّر لون/علامة على نص موجود */
/* تقسيم كلمات لسطور: brkSet = أماكن لازم يبدأ عندها سطر جديد؛ w0 = عرض أول سطر */
function LAY(ws,w,sz,brkSet,w0){const L=[[]];let cw=0;ws.forEach((t,i)=>{const tw=EW(t,sz)+sz*.28,lim=L.length==1&&w0?w0:w;if(L[L.length-1].length&&(cw+tw>lim||(brkSet&&brkSet.has(i)))){L.push([]);cw=0}L[L.length-1].push(i);cw+=tw});return L}
/* يكتب الكلمات من i0 لـi1 (أرقام كلمات السطر الحالي) في صندوق يمينه x، أول سطر y */
function FLOW(i0,i1,x,y,w,sz,col,lh,opt={}){const t=TKS(),ws=[];for(let i=i0;i<=i1;i++)ws.push(t[i].w);
 const nl=new Set((opt.nl||[]).map(i=>i-i0)),lines=LAY(ws,w,sz,nl,opt.w0),ch=[],cut=new Set(opt.cut||[]),cf=opt.cf||(()=>col);
 lines.forEach((ln,li)=>{let c=null;ln.forEach(j=>{const i=i0+j;if(!c||c.n>=(opt.mx||3)||cut.has(i)||cf(i)!=c.col){c={a:i,b:i,n:1,ws:[t[i].w],li,col:cf(i)};ch.push(c)}else{c.b=i;c.n++;c.ws.push(t[i].w)}})});
 ch.forEach((c,k)=>{const o=t[c.a].s/OS+(opt.dt||0),s=c.ws.join(' ');if(!k||ch[k-1].li!=c.li)W(o,x,y+c.li*lh,s,sz,c.col);else WC(o,s,c.col);c.it=LASTW});
 return {ch,n:lines.length,last:y+(lines.length-1)*lh}}
/* تعليم: كل كتل النص اللي جوّه الكلمات [a..b] تتلوّن (وتتخط تحت/تتشطب) من لحظة o */
function HLR(ch,a,b,o,col,deco){ch.forEach(c=>{if(c.a>=a&&c.b<=b){c.it.hl=T0+o*OS;c.it.hc=col;c.it.hd=deco}})}
const STEP=(o,x,y,n,col)=>{P(o,RR(x,y,30,30,7),col,2.5,.25,'#fff');W(o+.08,x+15,y+22,n,18,col,'middle')};
/* ---- أيقونات الأجزاء (مركز x,y؛ تقريبًا ٥٠×٥٠) ---- */
const ICN={
 crown:(x,y)=>[[S(I.crown,x+3,y+22,.6),'#B3261E','#F3B9B1']],
 key:(x,y)=>[[KEY(x-24,y,.8),YD]],
 bundle:(x,y)=>[[S(I.bundle,x,y,.62),GD]],
 reg:(x,y)=>[[S(I.reg,x,y,.5),G,'#fff']],
 bell:(x,y)=>[[S(I.bell,x,y+2,1),R]],
 scale:(x,y)=>[[S(I.scale,x,y,.85),N]],
 plane:(x,y)=>[[S(I.plane,x,y,.9),N,'#fff']],
 scroll:(x,y)=>[[S(I.scroll,x,y,.95),BRN,CREAM]],
 passport:(x,y)=>[[S(I.passport,x,y,.7),GD,LGN]],
 house:(x,y)=>[[S(I.house,x,y-6,.45),N]],
 chair:(x,y)=>{const c=CH2(x-12,y+10,.3);return [[c.body+c.legs.join(''),N]]},
 book:(x,y)=>[[BOOK(x,y-12),G]],
 tap:(x,y)=>[[S(I.tap,x+4,y-6,1),BLU],[DROP(x-18,y+16,.8),BLU,SKY]],
 drop:(x,y)=>[[DROP(x,y+4,1.5),BLU,SKY]],
 shield:(x,y)=>[[SHD(x,y+2,1.4),GD,LGN]],
 map:(x,y)=>[[EGO(x-26,y-20,.13),N,SAND],[NILE(x-26,y-20,.13),BLU]],
 star:(x,y)=>[[STAR(x,y,20),YD,Y]],
 pin:(x,y)=>[[PIN(x,y+20,1.15),R,R]],
 gear:(x,y)=>[[GEAR(x,y,13),N]],
 gnd:(x,y)=>{const g=GND(x-14,y-22,.3);return [[g.top+g.front+g.side+g.cuts,BRN,SAND]]},
 lens:(x,y)=>[[S(I.lens2,x-6,y,.8),N]],
 people:(x,y)=>[[MAN(x-16,y-20,34)+MAN(x+2,y-16,30)+MAN(x+18,y-20,34),G]],
 cycle:(x,y)=>[[COL(x+16,y-18,30,9),BRN],[GEAR(x-18,y-2,10),N],[`M${x+2},${y-26} q-12,-8 -22,4`+` m0,0 l2,-9 m-2,9 l9,-1`,R]],
 hand5:(x,y)=>[[`M${x-24},${y+20} Q${x},${y+28} ${x+24},${y+20} `+[-18,-9,0,9,18].map((d,i)=>`M${x+d-4},${y+20} V${y-8-[0,7,10,7,2][i]} a4,4 0 0,1 8,0 V${y+20} `).join(''),GD]],
 table:(x,y)=>[[RC(x-26,y-20,52,40)+`M${x},${y-20} V${y+20} M${x-26},${y-8} H${x+26}`,N,'#fff']],
 half:(x,y)=>[[CI(x,y,18),G],[`M${x},${y-18} A18,18 0 0,1 ${x},${y+18} Z`,G,LGN]],
 village:(x,y)=>[[S(I.house,x-12,y-4,.3)+S(I.house,x+12,y,.25),N],[`M${x-30},${y+16} h60`,BLU],[RC(x-30,y-28,60,50),R]]};
const DRAWI=(o,k,x,y)=>ICN[k](x,y).forEach(([d,c,f],j)=>P(o+j*.08,d,c,3,.4,f));

/* ---- تخطيط السؤال: بيتحسب مرة واحدة أول سطر -س من نصوص السطور التلاتة ---- */
const SZS=[[21,33,20,36,20,31],[20,31,19,34,19,29],[19,29,18,32,18,27],[18,27,17,30,17,25]];
function QPARTS(Q){const qt=toks(SP[Q.id+'-س']);
 const rng=(Q.qr||[[null,null,N]]).map(([f,e,c,gp])=>{const a=f==null?qt.findIndex(w=>w.startsWith('«')):TI(f,0,qt);let b;if(e)b=TI(e,0,qt);else{b=qt.length-1;if(Q.ch){b=qt.indexOf('(أ)')-1}}return [a,b,c||N,gp||0]});
 let chs=null;if(Q.ch){chs=['أ','ب','ج','د'].map((l,k,A)=>{const a=qt.indexOf('('+l+')'),b=k<3?qt.indexOf('('+A[k+1]+')')-1:qt.length-1;return {l,a,b}})}
 const at_=toks(SP[Q.id+'-ج']);let a0=Q.a0!=null?TI(Q.a0,0,at_):at_.findIndex(w=>w.startsWith('«')||/^\(.\)$/.test(w));
 let tl=Q.op?at_.lastIndexOf('وأي'):at_.lastIndexOf('إجابة');if(!Q.op&&tl>0&&at_[tl-1]=='ودي')tl--;
 const end=Q.op?at_.length-1:tl-1,nl=(Q.anl||[]).map(([s,n,bk])=>TI(s,n||0,at_)-(bk||0));
 return {qt,rng,chs,at:at_,a0,tl,end,nl}}
function QLAY(Q){const p=QPARTS(Q),top=Q.top||78,X0=20,X1=1046;
 for(const sz of SZS){const [qs,ql,cs,crow,as,al]=sz,qw=X1-56-(X0+50);let qn=0;
  let gq=0;p.rng.forEach(([a,b,c,gp])=>{qn+=LAY(p.qt.slice(a,b+1),qw,qs).length;gq+=gp});
  const qh=Math.max(18+gq+qn*ql+(p.chs?2*crow+4:0)+(Q.qx||0)+10,Q.pg?86:0);
  const an=LAY(p.at.slice(0,p.end+1),X1-24-(X0+16),as,new Set(p.nl),X1-24-(X0+16)-240).length,ah=14+an*al+10;
  const mh=Q.mh||(Q.m.length>14?112:96),tot=qh+8+mh+8+ah;
  if(top+tot<=526||sz==SZS[SZS.length-1]){const y1=top+qh,m0=y1+8,m1=m0+mh,a0=m1+8;return {p,sz,top,X0,X1,qh,qw,q:{y0:top,y1},mb:{x0:X0,x1:X1,y0:m0,y1:m1},ab:{x0:X0,x1:X1,y0:a0,y1:a0+ah},an}}}}
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
  const f=FLOW(a+1,b,cx-24,cy,400,cs,N,crow,{mx:4});Q.C[l]={f,a,b,cx,cy}})}
 if(CUR.some(k=>k.p))CDR(atp(),X0+23,y0+96,13,Math.round(+CUR.find(k=>k.p).v));
 if(Q.qf)Q.qf(Lo)}
/* (٢) طريقة الحل: ops = ['t',at,text,col] كتابة · ['h',k,at] تعليم كلمة مفتاحية · ['x',at,letter] شطب اختيار
   · ['ic',at,icon,label] أيقونة الجزء من الدرس (+سهم) · ['xi',at,letter,icon] أيقونة صغيرة جنب اختيار · ['f',at,fn] رسم خاص */
function QM(Q){const b=Q.L.mb,[qs,ql,cs,crow,as,al]=Q.L.sz;
 P(.02,RR(b.x0,b.y0,b.x1-b.x0,b.y1-b.y0,12),YD,2.5,.4,'#FFFBEA');STEP(.08,b.x0+8,b.y0+8,'٢',YD);
 const nic=Q.m.filter(o=>o[0]=='ic').length,slot=nic?Math.max(120,nic*72):0,xR=b.x1-14,xL=b.x0+46+slot+(nic?36:0),sz=19,lh=29;
 let cy=b.y0+30,cw=0,first=true,ki=0,arrowed=false,lf=null;Q.icp=[];
 const icx=k=>b.x0+46+slot-(k+.5)*(slot/nic),icy=b.y0+(b.y1-b.y0)/2-(Q.m.some(o=>o[0]=='ic'&&o[3])?8:0);
 Q.m.forEach(op=>{const [k,a]=op;
  if(k=='t'){const o=at(a,op[4]||0),s=op[2],tw=EW(s,sz)+6;if(!first&&cw+tw>xR-xL){cy+=lh;cw=0;first=true}
   if(first){W(o,xR,cy,s,sz,op[3]||N);first=false}else{LASTW=lf;WC(o,s,op[3]||N)}lf=LASTW;cw+=tw}
  else if(k=='nl'){cy+=lh;cw=0;first=true}
  else if(k=='h'){const [x,y]=Q.keyI[op[1]],o=at(op[2],op[3]||0);for(const f of Q.F)HLR(f.ch,x,y,o,R,'underline');MARK0(o)}
  else if(k=='x'){const c=Q.C[op[2]],o=at(a,op[3]||0);HLR(c.f.ch,c.a,c.b,o,'#9AA5AE','line-through');P(o,XX(c.cx,c.cy-7,1.3),R,4,.3)}
  else if(k=='xi'){const c=Q.C[op[2]],cx0=c.cx>533?557:35;DRAWI(at(a,op[4]||0),op[3],cx0+30,c.cy-10)}
  else if(k=='ic'){const o=at(a,op[4]||0),x=icx(ki),y=icy;Q.icp.push([x,y]);DRAWI(o,op[2],x,y);if(op[3])W(o+.15,x,b.y1-10,op[3],15,GR,'middle');
   if(!arrowed){P(o+.05,ARW(xL-6,y,b.x0+46+slot-2,y,8),GR,3,.3);arrowed=true}ki++}
  else if(k=='f')op[2](at(a,op[3]||0),b,Q)});
 if(cy>b.y1-6)console.warn('QM overflow',Q.id,cy,b.y1)}
/* (٣) الإجابة النموذجية: كارت أخضر مسطّر زي ورقة الامتحان + بادج «اجتهاد · ص…» */
function QJ(Q){const Lo=Q.L,b=Lo.ab,p=Lo.p,[qs,ql,cs,crow,as,al]=Lo.sz,t=TKS();if(t.length!=p.at.length)throw new Error('QJ tokens '+Q.id);
 P(.02,RR(b.x0,b.y0,b.x1-b.x0,b.y1-b.y0,12),G,4,.6,'#fff');STEP(.1,b.x0+8,b.y0+8,'٣',G);
 let rl='';for(let i=0;i<Lo.an;i++)rl+=`M${b.x0+16},${F(b.y0+14+al*.72+i*al+8)} H${b.x1-16} `;P(.15,rl,'#CFE3D6',1.5,.6);
 const f=FLOW(0,p.end,b.x1-24,b.y0+14+al*.72,b.x1-24-(b.x0+16),as,N,al,{w0:b.x1-24-(b.x0+16)-240,nl:p.nl,cf:i=>i<p.a0?G:(Q.op&&i>=p.tl?GD:N)});
 const m=/^\((.)\)$/.exec(t[p.a0].w);if(m&&Q.C){const c=Q.C[m[1]],o=t[p.a0].s/OS;P(o,CI(c.cx,c.cy-7,21),G,4,.4);HLR(c.f.ch,c.a,c.b,o,G,'underline')}
 const o=t[Q.op?Math.min(p.tl+2,t.length-1):p.tl].s/OS,s='اجتهاد · '+Q.ap,bw=EW(s,15)+24;
 P(o,RR(b.x0+46,b.y0+9,bw,28,14),YD,2.5,.3,'#FFF4D6');W(o+.1,b.x0+46+bw-12,b.y0+29,s,15,YD);chime(o)}
/* سؤال كامل = ٣ سطور */
function QQ(Q){L(Q.id+'-س',()=>QS(Q));L(Q.id+'-ح',()=>QM(Q));L(Q.id+'-ج',()=>QJ(Q))}
