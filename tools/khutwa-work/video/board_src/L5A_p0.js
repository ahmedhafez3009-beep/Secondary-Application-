/* ============ السبورة L5A: الدرس ٥ · الفصل ١ · افتتاح الوحدة والقناع الفرنسي ============ */
const BLU='#3E8FCF',BRN='#B8860B',SKY='#DCEEFB',PUR='#8E44AD',CREAM='#FBF3DC',PAP='#F3D9B8',SKIN='#D9A877',LGN='#d9f0e3',BUB='#EEF8F1';
/* خريطة مصر (نفس موتيف السبورة A45): وحدة 400×300 */
const EGU={W:[[0,300],[0,6]],N:[[0,6],[40,12],[74,8],[131,25],[165,12],[181,5],[205,0],[228,3],[245,10],[280,16],[309,9]],E:[[309,9],[333,66]],AQ:[[333,66],[311,122]],SG:[[311,122],[290,95],[252,52]],RS:[[252,52],[262,80],[296,136],[345,215],[400,300]],
 NL:[[212,300],[240,262],[265,234],[262,200],[259,169],[242,173],[225,150],[208,137],[203,100],[210,48]]};
const mp=(pts,x,y,s,dx,dy)=>pts.map((p,i)=>(i?'L':'M')+(x+p[0]*s+(dx||0)).toFixed(0)+','+(y+p[1]*s+(dy||0)).toFixed(0)).join(' ')+' ';
const EGO=(x,y,s)=>mp([].concat(EGU.W,EGU.N.slice(1),EGU.E.slice(1),EGU.AQ.slice(1),EGU.SG.slice(1),EGU.RS.slice(1)),x,y,s)+'Z';
const NILE=(x,y,s)=>{const q=EGU.NL.map(p=>[Math.round(x+p[0]*s),Math.round(y+p[1]*s)]);let d=`M${q[0]}`;for(let i=1;i<q.length-1;i++)d+=` Q${q[i]} ${[(q[i][0]+q[i+1][0])/2,(q[i][1]+q[i+1][1])/2]}`;
 const c=q[q.length-1],f=(u,v)=>`${Math.round(x+u*s)},${Math.round(y+v*s)}`;return d+` L${c} M${c} L${f(181,5)} M${c} L${f(228,3)} `};
const DELTA=(x,y,s)=>mp([[210,48],[181,5],[205,0],[228,3]],x,y,s)+'Z ';
const WV=(x,y,n,w)=>`M${x},${y} q${w/2},${-w*.4} ${w},0 `+Array(n-1).fill(`t${w},0`).join(' ')+' ';
const HOUSE=(x,y,s=1)=>`M${x},${y} v${-12*s} l${9*s},${-8*s} l${9*s},${8*s} v${12*s} Z `;
const COLS=(xs,y1,y2)=>xs.map(x=>`M${x-20},${y1} V${y2} M${x+20},${y1} V${y2} M${x-27},${y1+12} Q${x},${y1+30} ${x+27},${y1+12} `);
const FEN=(x,y)=>`M${x-30},${y} h60 M${x-24},${y} v-24 M${x-10},${y} v-20 M${x+4},${y} v-20 M${x+18},${y} v-20 M${x-24},${y-12} h48 `;
const HAND=(x,y,s)=>`M${x-9*s},${y} v${-15*s} M${x-3*s},${y} v${-20*s} M${x+3*s},${y} v${-20*s} M${x+9*s},${y} v${-15*s} M${x-12*s},${y} v${10*s} q${12*s},${10*s} ${24*s},0 v${-10*s} M${x+12*s},${y+4*s} l${8*s},${-9*s} `;
const F=n=>(+n).toFixed(1);
const ARW=(x1,y1,x2,y2,h=11)=>{const a=Math.atan2(y2-y1,x2-x1);return `M${x1},${y1} L${x2},${y2} M${x2},${y2} L${F(x2-h*Math.cos(a-.5))},${F(y2-h*Math.sin(a-.5))} M${x2},${y2} L${F(x2-h*Math.cos(a+.5))},${F(y2-h*Math.sin(a+.5))} `};
const RC=(x,y,w,h)=>`M${x},${y} h${w} v${h} h${-w} Z `;
const TICK=(x,y,s=1)=>`M${x-7*s},${y} l${5*s},${5*s} l${9*s},${-10*s} `;
const XX=(x,y,s=1)=>`M${x-7*s},${y-7*s} l${14*s},${14*s} M${x+7*s},${y-7*s} l${-14*s},${14*s} `;
/* معبد صغير: x المنتصف، y القاعدة */
const TEMPLE=(x,y,s=1)=>`M${x-50*s},${y-54*s} h${100*s} v${10*s} h${-100*s} Z M${x-34*s},${y-44*s} V${y} M${x-11*s},${y-44*s} V${y} M${x+11*s},${y-44*s} V${y} M${x+34*s},${y-44*s} V${y} M${x-54*s},${y} h${108*s} `;
const WHEAT=(x,y,s=1)=>`M${x},${y} V${y-56*s} `+[0,1,2,3].map(i=>`M${x},${F(y-(22+i*10)*s)} q${-9*s},${-3*s} ${-8*s},${-13*s} M${x},${F(y-(22+i*10)*s)} q${9*s},${-3*s} ${8*s},${-13*s} `).join('');
/* التاج المزدوج الصغير (نفس رسمة «مركزية» في A1.1): x المنتصف، y القاعدة */
const PSCH=(x,y,s=1)=>`M${F(x-22*s)},${y} V${F(y-30*s)} Q${F(x-7*s)},${F(y-52*s)} ${F(x+8*s)},${F(y-30*s)} V${y} Z M${F(x+8*s)},${y} H${F(x+30*s)} L${F(x+36*s)},${F(y-40*s)} L${F(x+20*s)},${F(y-14*s)} `;
const SHD=(x,y,s=1)=>`M${F(x-12*s)},${F(y-16*s)} h${24*s} v${12*s} q0,${14*s} ${-12*s},${20*s} q${-12*s},${-6*s} ${-12*s},${-20*s} Z `;
const DROP=(x,y,s=1)=>`M${x},${F(y-13*s)} q${9*s},${11*s} ${9*s},${17*s} a${9*s},${9*s} 0 1,1 ${-18*s},0 q0,${-6*s} ${9*s},${-17*s} Z `;
const PIN=(x,y,s=1)=>`M${x},${y} q${-13*s},${-18*s} ${-13*s},${-28*s} a${13*s},${13*s} 0 1,1 ${26*s},0 q0,${10*s} ${-13*s},${28*s} Z `;
const SAIL=(x,y,s=1)=>`M${F(x-24*s)},${y} h${48*s} l${-9*s},${11*s} h${-30*s} Z M${x},${y} V${F(y-38*s)} l${20*s},${30*s} h${-20*s} `;
const PLANT=(x,y,s=1)=>`M${x},${y} V${F(y-60*s)} `+[[-16,-14],[-9,-21],[0,-24],[9,-21],[16,-14]].map(([a,b])=>`M${x},${F(y-60*s)} l${a*s},${b*s} `).join('');
const SCROLL=(x,y,w,h)=>`M${x},${y} H${x+w} V${y+h} H${x} Z M${x-7},${y-5} H${x+w+7} M${x-7},${y+h+5} H${x+w+7} `;
const FPR=(x,y,s=1)=>[6,13,20,27].map((r,i)=>`M${F(x-r*s)},${F(y+(6+i*5)*s)} V${y} a${r*s},${r*s} 0 0,1 ${2*r*s},0 V${F(y+(14-i*2)*s)} `).join('');
const GEAR=(x,y,r)=>CI(x,y,r)+CI(x,y,r*.35)+[0,1,2,3,4,5,6,7].map(i=>{const a=i*Math.PI/4;return `M${F(x+r*Math.cos(a))},${F(y+r*Math.sin(a))} L${F(x+r*1.4*Math.cos(a))},${F(y+r*1.4*Math.sin(a))} `}).join('');
const STAR=(x,y,r)=>[0,1,2,3,4,5,6,7,8,9].map(i=>{const a=-Math.PI/2+i*Math.PI/5,q=i%2?r*.42:r;return (i?'L':'M')+F(x+q*Math.cos(a))+','+F(y+q*Math.sin(a))}).join(' ')+' Z ';
const DUNE=(x,y,n,w)=>`M${x},${y} `+Array(n).fill(`q${w*.5},${-w*.45} ${w},0`).join(' ')+' ';
const TREE=(x,y,s=1)=>`M${x},${y} V${F(y-34*s)} `+EL(x,F(y-52*s),22*s,20*s);
const BUBBLE=(o,x,y,w,h)=>P(o,RC(x,y,w,h),GD,2,.6,BUB);
const chime=o=>SFX.push({t:T0+o*OS,k:'chime'});
/* التاج المزدوج (أحمر + أبيض) بقطعتين: x المنتصف، y القاعدة */
function CRW(o,x,y,s=1,d=.5){P(o,`M${F(x-23*s)},${y} L${F(x-25*s)},${F(y-24*s)} H${F(x+13*s)} L${F(x+21*s)},${F(y-62*s)} L${F(x+27*s)},${F(y-62*s)} L${F(x+25*s)},${y} Z`,'#B3261E',3,d,'#E58A7F');
 P(o+d*.6,`M${F(x-17*s)},${F(y-24*s)} Q${F(x-20*s)},${F(y-52*s)} ${F(x-6*s)},${F(y-72*s)} Q${F(x+7*s)},${F(y-52*s)} ${F(x+5*s)},${F(y-24*s)} Z`,N,3,d,'#fff');
 P(o+d*1.1,`M${F(x+9*s)},${F(y-26*s)} Q${F(x-6*s)},${F(y-46*s)} ${F(x-24*s)},${F(y-38*s)} q${F(-5*s)},${F(4*s)} ${F(-1*s)},${F(8*s)}`,'#B3261E',2.5,d*.6)}
const BLOB=(x,y,w,h)=>`M${x},${F(y+h*.5)} Q${x},${y} ${F(x+w*.4)},${F(y+h*.08)} Q${F(x+w*.8)},${F(y-h*.05)} ${F(x+w)},${F(y+h*.35)} Q${F(x+w*1.02)},${F(y+h*.8)} ${F(x+w*.6)},${F(y+h)} Q${F(x+w*.15)},${F(y+h*1.02)} ${x},${F(y+h*.5)} Z `;
const CAMEL=(x,y,s=1)=>`M${x},${y} q${6*s},${-14*s} ${13*s},${-2*s} q${5*s},${-9*s} ${11*s},0 l${7*s},${-13*s} l${6*s},${2*s} M${x},${y} v${13*s} M${F(x+22*s)},${y} v${13*s} `;
const TAB=(o,x,y,w,t,pg)=>{P(o,RC(x,y,w,40),BRN,3,.5,CREAM);W(o+.2,x+w-12,y+28,t,19,N);if(pg)WC(o+.45,pg,GR)};
/* عيون بترمش: الإزاحة جوّه المسار نفسه (أنيميشن الرمش بيلغي translate) */
const EYES=(o,x1,x2,y,l)=>{P(o,`M${ox+x1},${oy+y} h${l} M${ox+x2},${oy+y} h${l}`,N,5,.2,null,'blink');const it=IT[IT.length-1];it.tx=0;it.ty=0};
const BADGE=(o,x,y,n)=>{P(o,CI(x,y,17),R,3,.3,'#fff');W(o+.1,x,y+9,n,24,R,'middle')};
const GHO='#c9cfd2',PNK='#F8D7D3';
const L=(id,fn)=>line(id,SRC[id]||'',S[id],fn);
/* ألوان القوى: الفرس بنفسجي، الإغريق أزرق، البطالمة بني */
const PT=n=>[...Array(n).keys()];
/* بيت الدرس ١ بأعمدته الأربعة: x,y الركن الأيمن-العلوي للسقف، w العرض، h الارتفاع */
const HB=(x,y,w,h)=>({roof:`M${x-10},${y+60} L${F(x+w/2)},${y} L${x+w+10},${y+60} Z M${x},${y+60} h${w}`,cols:[.1,.37,.63,.9].map(k=>`M${F(x+w*k)},${y+60} V${y+h}`),base:`M${x-10},${y+h} h${w+20}`,cx:[.1,.37,.63,.9].map(k=>x+w*k)});
/* رأس لابس: kind c تاج، h خوذة، d إكليل */
const HG=(x,y,h,kind)=>{const r=h*.15;if(kind=='c')return `M${F(x-r)},${F(y+.2*r)} L${F(x-r)},${F(y-.9*r)} L${F(x-.5*r)},${F(y-.2*r)} L${x},${F(y-1.1*r)} L${F(x+.5*r)},${F(y-.2*r)} L${F(x+r)},${F(y-.9*r)} L${F(x+r)},${F(y+.2*r)} Z`;
 if(kind=='h')return `M${F(x-1.15*r)},${F(y+1.1*r)} a${F(1.15*r)},${F(1.2*r)} 0 0,1 ${F(2.3*r)},0 M${x},${F(y-.1*r)} q${F(.5*r)},${F(-.7*r)} ${F(1.1*r)},${F(-.1*r)}`;
 return `M${F(x-1.05*r)},${F(y+.5*r)} q${F(1.05*r)},${F(-.5*r)} ${F(2.1*r)},0 M${F(x-.6*r)},${F(y+.2*r)} l${F(-.4*r)},${F(-.5*r)} M${F(x+.6*r)},${F(y+.2*r)} l${F(.4*r)},${F(-.5*r)}`};
/* شخص حقيقي: رسم تخيّلي + اسم */
function FIG(o,x,y,h,kind,col,name,sz){P(o,MAN(x,y,h),col,3,.6);P(o+.25,HG(x,y,h,kind),col,3,.4,kind=='c'?'#fff':null);
 W(o+.3,x+h*.34,y+h+22,'رسم تخيّلي',15,GR,'middle');if(name)W(o+.3,x+h*.4,y+h+46,name,sz||20,col,'middle')}
/* ميزان: x مركز، y الرافعة، w نص الطول، t ميل (موجب = الشمال أخفض). يرجع المسارات */
const BAL=(x,y,w,t)=>{const lx=x-w,ly=y+t,rx=x+w,ry=y-t,pan=(ex,ey)=>`M${ex},${ey} L${ex-55},${ey+70} M${ex},${ey} L${ex+55},${ey+70} M${ex-62},${ey+70} q62,46 124,0 Z`;
 return {post:`M${x},${y} V${y+210} M${x-56},${y+210} h112 M${x-14},${y-14} L${x},${y} L${x+14},${y-14}`,beam:`M${lx},${ly} L${rx},${ry}`,pl:pan(lx,ly),pr:pan(rx,ry),L:[lx,ly+70],R:[rx,ry+70]}};
/* دلتا: ذروة (x,y) والنهر تحتها، s مقياس */
const DEL=(x,y,s)=>({coast:`M${F(x-95*s)},${F(y-92*s)} Q${F(x-60*s)},${F(y-126*s)} ${F(x-20*s)},${F(y-120*s)} Q${F(x+20*s)},${F(y-114*s)} ${F(x+50*s)},${F(y-124*s)} Q${F(x+80*s)},${F(y-122*s)} ${F(x+100*s)},${F(y-96*s)}`,
 riv:`M${x},${F(y+120*s)} V${y} M${x},${y} L${F(x-90*s)},${F(y-94*s)} M${x},${y} L${F(x-38*s)},${F(y-118*s)} M${x},${y} L${F(x+28*s)},${F(y-118*s)} M${x},${y} L${F(x+98*s)},${F(y-98*s)}`,east:[x+100*s,y-96*s]});
const EYE=(x,y,s=1)=>EL(x,y,22*s,11*s)+CI(x,y,5*s);
const SACK=(x,y,s=1)=>`M${F(x-34*s)},${y} q${F(-24*s)},${F(-36*s)} ${F(8*s)},${F(-60*s)} h${F(52*s)} q${F(32*s)},${F(24*s)} ${F(8*s)},${F(60*s)} Z M${F(x-12*s)},${F(y-60*s)} l${F(-6*s)},${F(-14*s)} h${F(48*s)} l${F(-6*s)},${F(14*s)}`;
const STAIR=(x,y,w,h,n)=>`M${x},${y} `+PT(n).map(i=>`h${-w} v${h} `).join('');
const LIGHT=(x,y,s=1)=>`M${F(x-12*s)},${y} l${F(4*s)},${F(-60*s)} h${F(16*s)} l${F(4*s)},${F(60*s)} Z M${F(x-10*s)},${F(y-60*s)} h${F(20*s)} v${F(-14*s)} h${F(-20*s)} Z M${F(x+14*s)},${F(y-68*s)} l${F(28*s)},${F(-6*s)} M${F(x-14*s)},${F(y-68*s)} l${F(-28*s)},${F(-6*s)}`;
const DOOR=(x,y,w,h)=>`M${x},${y+h} V${y} H${x+w} V${y+h}`;
const PIE=(x,y,r)=>CI(x,y,r)+`M${x},${y} L${x+r},${y} M${x},${y} L${F(x-r*.5)},${F(y-r*.87)} M${x},${y} L${F(x-r*.5)},${F(y+r*.87)}`;
const FIST=(x,y,s=1)=>HAND(x,y,s);
const LINK=(x,y,r)=>EL(x,y,r*1.5,r)+EL(x+r*2.2,y,r*1.5,r);
const crop=(o,t)=>t;
/* WC بفجوة أوسع شوية علشان ما يتلامسوش */
WC=function(o,txt,col,gap){const p=LASTW;IT.push(LASTW={k:'w',t:T0+o*OS,x:p.x,y:p.y,txt,sz:p.sz,col:col||p.col,a:'end',d:Math.min(1.4,.06*txt.length+.3),cx:p.cx,cy:p.cy,af:p,gp:gap==null?p.sz*.5:gap})};
TAB2=(o,x,y,w,t,pg)=>{P(o,RC(x,y,w,40),BRN,3,.5,CREAM);W(o+.2,x+w-12,y+28,t,19,N);if(pg)WC(o+.45,pg,GR,16)};

/* ---------- إضافات L2C ---------- */
const ROM='#B3261E',LRD='#FBE3E0',LYL='#FFF4CC';
const mark=()=>IT.length,OFFS=(a,b,o)=>{for(let i=a;i<b;i++)IT[i].off=T0+o*OS};
function WR(x,y,sz,col,parts){parts.forEach((p,i)=>{const k=p[0],t=typeof k=='number'?k:Array.isArray(k)?at(k[0],k[1]):at(k),c=p[2]||col;if(i==0)W(t,x,y,p[1],sz,c);else WC(t,p[1],c)})}
const RR=(x,y,w,h,r=10)=>`M${x+r},${y} h${w-2*r} q${r},0 ${r},${r} v${h-2*r} q0,${r} ${-r},${r} h${-(w-2*r)} q${-r},0 ${-r},${-r} v${-(h-2*r)} q0,${-r} ${r},${-r} Z `;
const RTEMP=(x,y,s=1)=>TEMPLE(x,y,s)+`M${F(x-56*s)},${F(y-54*s)} L${x},${F(y-84*s)} L${F(x+56*s)},${F(y-54*s)} `;
const CHURCH=(x,y,s=1)=>`M${F(x-28*s)},${y} V${F(y-46*s)} L${x},${F(y-72*s)} L${F(x+28*s)},${F(y-46*s)} V${y} Z M${x},${F(y-72*s)} V${F(y-102*s)} M${F(x-9*s)},${F(y-92*s)} h${F(18*s)} M${F(x-8*s)},${y} v${F(-22*s)} a${F(8*s)},${F(8*s)} 0 0,1 ${F(16*s)},0 v${F(22*s)} `;
const CROSS=(x,y,s=1)=>`M${x},${y} v${F(44*s)} M${F(x-13*s)},${F(y+13*s)} h${F(26*s)} `;
const HEART=(x,y,s=1)=>`M${x},${F(y+12*s)} C${F(x-34*s)},${F(y-16*s)} ${F(x-20*s)},${F(y-40*s)} ${x},${F(y-18*s)} C${F(x+20*s)},${F(y-40*s)} ${F(x+34*s)},${F(y-16*s)} ${x},${F(y+12*s)} Z `;
/* غصن زيتون: يبدأ من x,y ويطلع يمين */
const OLIVE=(x,y,s=1)=>`M${x},${y} Q${F(x+34*s)},${F(y-8*s)} ${F(x+70*s)},${F(y-36*s)} `+[[14,-3],[30,-9],[46,-19],[60,-30]].map(([a,b],i)=>EL(+F(x+a*s),+F(y+(b+(i%2?9:-9))*s),+F(8*s),+F(4.5*s))).join('');
const FLAG=(x,y,s=1)=>`M${x},${y} V${F(y-70*s)} h${F(-46*s)} v${F(28*s)} h${F(46*s)} `;
const BRIDGE=(x,y,w,n)=>{const a=w/n,r=a*.33;return `M${x},${y} h${w} M${x},${y+16} h${w} `+PT(n).map(i=>`M${F(x+i*a+a/2-r)},${y+90} V${F(y+24+r)} a${F(r)},${F(r)} 0 0,1 ${F(2*r)},0 V${y+90} `).join('')};
const STELE=(x,y,w,h)=>`M${x},${y+h} V${y+44} Q${F(x+w/2)},${y-30} ${x+w},${y+44} V${y+h} Z `;
const SILO=(x,y,s=1)=>`M${F(x-24*s)},${y} v${F(-58*s)} q${F(24*s)},${F(-28*s)} ${F(48*s)},0 v${F(58*s)} Z M${F(x-24*s)},${F(y-30*s)} h${F(48*s)} `;
const CRK=(x,y1,y2)=>`M${x},${y1} l7,${F((y2-y1)*.25)} l-12,${F((y2-y1)*.25)} l12,${F((y2-y1)*.25)} l-7,${F((y2-y1)*.25)} `;
const GATE=(x,y,s=1)=>`M${x},${y} v${F(-70*s)} h${F(54*s)} v${F(70*s)} M${F(x+54*s)},${F(y-70*s)} l${F(26*s)},${F(8*s)} v${F(70*s)} l${F(-26*s)},${F(-8*s)} `;
const LOCK=(x,y,s=1)=>RC(+F(x-14*s),y,28*s,22*s)+`M${F(x-9*s)},${y} v${F(-10*s)} a${F(9*s)},${F(9*s)} 0 0,1 ${F(18*s)},0 v${F(10*s)} `;
const FLAME=(x,y,s=1)=>`M${x},${y} q${F(-17*s)},${F(-16*s)} 0,${F(-38*s)} q${F(17*s)},${F(22*s)} 0,${F(38*s)} Z `;
const TORCH=(x,y,s=1)=>`M${x},${y} v${F(-48*s)} M${F(x-10*s)},${F(y-48*s)} l${F(-4*s)},${F(-14*s)} h${F(28*s)} l${F(-4*s)},${F(14*s)} Z `;
const WHEEL=(x,y,r)=>CI(x,y,r)+CI(x,y,+F(r*.2))+[0,1,2,3,4,5].map(i=>{const a=i*Math.PI/3;return `M${F(x+r*.2*Math.cos(a))},${F(y+r*.2*Math.sin(a))} L${F(x+r*Math.cos(a))},${F(y+r*Math.sin(a))} `}).join('');
const SCIS=(x,y,s=1)=>`M${F(x-26*s)},${F(y-26*s)} L${F(x+28*s)},${F(y+28*s)} M${F(x-26*s)},${F(y+26*s)} L${F(x+28*s)},${F(y-28*s)} `+CI(+F(x-32*s),+F(y-32*s),7*s)+CI(+F(x-32*s),+F(y+32*s),7*s);
const PENCIL=(x,y,s=1)=>`M${x},${y} l${F(6*s)},${F(-18*s)} l${F(36*s)},${F(-36*s)} l${F(12*s)},${F(12*s)} l${F(-36*s)},${F(36*s)} Z `;
const GLOBE=(x,y,r)=>CI(x,y,r)+`M${x-r},${y} h${2*r} M${x},${y-r} q${-r*.7},${r} 0,${2*r} M${x},${y-r} q${r*.7},${r} 0,${2*r} `;
const CLASH=(x,y)=>`M${x-18},${y+4} l12,-10 l12,20 l12,-20 `;
const RT=(x,y,a)=>(px,py)=>[Math.round(x+px*Math.cos(a)-py*Math.sin(a)),Math.round(y+px*Math.sin(a)+py*Math.cos(a))].join(',');
/* سيف (نفس موتيف كارت ١ في L2A) */
const SWB=(x,y,len,deg,side)=>{const r=RT(x,y,deg*Math.PI/180);const e=side>0?[[0,14],[len*.86,16],[len,0]]:[[0,-14],[len*.86,-16],[len,0]];return 'M'+r(...e[0])+' L'+r(...e[1])+' L'+r(...e[2])+' '};
const SWH=(x,y,len,deg)=>{const r=RT(x,y,deg*Math.PI/180);return 'M'+r(0,0)+' L'+r(len,0)+' M'+r(0,-24)+' L'+r(0,24)+' M'+r(0,0)+' L'+r(-34,0)+' '+CI(...r(-42,0).split(',').map(Number),8)};
const CARDT=(o,t)=>{CARD(o,16,78,1034,450,G);W(o+.15,1030,110,t,22,G)};
const Z=(t,x,y,w,d)=>camTo(t,ox+x,oy+y,w,w*9/16,d||.9);
const DIG=(o,xs,y,t,sz,col)=>t.split('').forEach((c,i)=>W(o[i]!=null?o[i]:o[o.length-1],xs[i],y,c,sz,col,'middle'));

/* ---------- إضافات L3B ---------- */
const LBL='#E3F0FA',LPU='#F1E6F7';
const Zm=(o,x,y,w,d)=>camTo(o*OS,ox+x,oy+y,w,w*9/16,d||.9);
/* فقاعة «بالبلدي»: ترسم الإطار وتكتب «بالبلدي:» وبعدها كمّل بـ WC */
const BB=(o,x,y,w,h,sz)=>{BUBBLE(o,x,y,w,h);W(o+.05,x+w-10,y+(sz||18)+11,'بالبلدي:',sz||18,GD)};
const TICKP=(o,x,y,s)=>P(o,TICK(x,y,s||1.6),G,6,.3);
/* عمامة فوق راس MAN(x,y,h) */
const TURB=(x,y,h)=>{const r=h*.15;return `M${F(x-1.3*r)},${F(y+.55*r)} Q${x},${F(y-1.5*r)} ${F(x+1.3*r)},${F(y+.55*r)} Q${x},${F(y-.1*r)} ${F(x-1.3*r)},${F(y+.55*r)} Z `};
/* شخص بعمامة (عام أو باسم) + «رسم تخيّلي» */
function TMAN(o,x,y,h,col,lab,name,sz){P(o,MAN(x,y,h),col,3,.5);P(o+.15,TURB(x,y,h),col,3,.3,'#fff');if(lab)W(o+.25,x,y+h+20,'رسم تخيّلي',14,GR,'middle');if(name)W(o+.3,x,y+h+44,name,sz||20,col,'middle')}
/* شخص قاعد: x المنتصف، y أعلى الراس */
const SIT=(x,y,h)=>{const r=h*.15;return CI(x,+F(y+r),+F(r))+`M${x},${F(y+2*r)} V${F(y+h*.6)} M${F(x-h*.2)},${F(y+h*.5)} L${x},${F(y+h*.38)} L${F(x+h*.2)},${F(y+h*.5)} M${F(x-h*.3)},${F(y+h*.76)} Q${x},${F(y+h*.5)} ${F(x+h*.3)},${F(y+h*.76)} Z `};
const BALS=(x,y,s=1)=>`M${x},${y} V${F(y+44*s)} M${F(x-16*s)},${F(y+44*s)} h${F(32*s)} M${F(x-30*s)},${F(y+6*s)} H${F(x+30*s)} M${F(x-30*s)},${F(y+6*s)} l${F(-11*s)},${F(22*s)} h${F(22*s)} Z M${F(x+30*s)},${F(y+6*s)} l${F(-11*s)},${F(22*s)} h${F(22*s)} Z `;
const TABLET=(x,y,s=1)=>RC(+F(x-17*s),y,+F(34*s),+F(44*s))+`M${F(x-6*s)},${y} v${F(-9*s)} h${F(12*s)} v${F(9*s)} M${F(x-10*s)},${F(y+13*s)} h${F(20*s)} M${F(x-10*s)},${F(y+23*s)} h${F(20*s)} M${F(x-10*s)},${F(y+33*s)} h${F(12*s)} `;
/* منبر: x الطرف اليمين للسلم، y الأرض */
const MINBAR=(x,y,s=1)=>`M${x},${y} h${F(-18*s)} v${F(-13*s)} h${F(-18*s)} v${F(-13*s)} h${F(-18*s)} v${F(-13*s)} h${F(-22*s)} V${y} Z M${F(x-76*s)},${F(y-39*s)} v${F(-34*s)} l${F(11*s)},${F(-12*s)} l${F(11*s)},${F(12*s)} v${F(34*s)} `;
const IDC=(x,y,w,h)=>RR(x,y,w,h,8)+CI(+F(x+w*.78),+F(y+h*.38),+F(h*.17))+`M${F(x+w*.66)},${F(y+h*.8)} q${F(w*.12)},${F(-h*.3)} ${F(w*.24)},0 M${F(x+w*.1)},${F(y+h*.3)} h${F(w*.4)} M${F(x+w*.1)},${F(y+h*.52)} h${F(w*.4)} M${F(x+w*.1)},${F(y+h*.74)} h${F(w*.25)} `;
const NAIL=(x,y,s=1)=>`M${F(x-9*s)},${y} h${F(18*s)} M${x},${y} v${F(22*s)} `;
/* قاعدة حجر: x,y الركن العلوي الشمال، w العرض العلوي */
const STONE=(x,y,w,h)=>`M${x},${y} h${w} l16,${h} h${-(w+32)} Z `;
/* مبنى بقبة ومدنة: x المنتصف، y القاعدة */
const MOSQ=(x,y,s=1)=>`M${F(x-46*s)},${y} V${F(y-36*s)} H${F(x+34*s)} V${y} Z M${F(x-28*s)},${F(y-36*s)} a${F(22*s)},${F(22*s)} 0 0,1 ${F(44*s)},0 M${F(x-6*s)},${F(y-58*s)} v${F(-10*s)} M${F(x-12*s)},${y} v${F(-16*s)} a${F(6*s)},${F(6*s)} 0 0,1 ${F(12*s)},0 v${F(16*s)} M${F(x+40*s)},${y} V${F(y-74*s)} l${F(7*s)},${F(-12*s)} l${F(7*s)},${F(12*s)} V${y} M${F(x+36*s)},${F(y-52*s)} h${F(22*s)} `;
/* مدنة طويلة: x المنتصف، y القاعدة */
const MINA=(x,y,s=1)=>`M${F(x-11*s)},${y} V${F(y-104*s)} h${F(22*s)} V${y} M${F(x-17*s)},${F(y-104*s)} h${F(34*s)} M${F(x-17*s)},${F(y-62*s)} h${F(34*s)} M${F(x-7*s)},${F(y-104*s)} V${F(y-128*s)} q${F(7*s)},${F(-18*s)} ${F(14*s)},0 V${F(y-104*s)} M${x},${F(y-142*s)} v${F(-12*s)} `;
/* صف بواكي: x الطرف الشمال، y القاعدة، w عرض الباكية، h الارتفاع، n العدد */
const ARCS=(x,y,w,h,n)=>PT(n).map(i=>`M${x+i*w},${y} V${F(y-h+w*.5)} a${F(w*.5)},${F(w*.5)} 0 0,1 ${w},0 `).join('')+`M${x+n*w},${y-h+w*.5} V${y} `;
/* مسجد عمرو (تخيّلي): ساحة وبواكي بسيطة. x الطرف الشمال، y القاعدة، w العرض */
const AMR=(x,y,w,h)=>`M${x},${y} h${w} M${x-8},${y-h} h${w+16} M${x-8},${F(y-h-12)} h${w+16} M${x-8},${F(y-h-12)} v12 M${x+w+8},${F(y-h-12)} v12 `+ARCS(x,y,w/4,h,4);
/* الأزهر (تخيّلي): صحن ببواكي + مدنة + قبة */
const AZH=(x,y,w,h)=>`M${x},${y} h${w} M${x-6},${y-h} h${w+12} `+ARCS(x,y,w/3,h,3)+`M${F(x+w*.3)},${y-h} a${F(w*.14)},${F(w*.14)} 0 0,1 ${F(w*.28)},0 `;
const SPROUT=(x,y,s=1)=>EL(x,y,+F(9*s),+F(6*s))+`M${x},${F(y-6*s)} q${F(-3*s)},${F(-18*s)} 0,${F(-34*s)} M${x},${F(y-26*s)} q${F(-16*s)},${F(-2*s)} ${F(-18*s)},${F(-16*s)} q${F(14*s)},0 ${F(18*s)},${F(16*s)} M${x},${F(y-34*s)} q${F(16*s)},${F(-2*s)} ${F(18*s)},${F(-16*s)} q${F(-14*s)},0 ${F(-18*s)},${F(16*s)} `;
const RAYS=(x,y,r1,r2,n,a0=0,a1=Math.PI*2)=>PT(n).map(i=>{const a=a0+(a1-a0)*i/(a1-a0>6?n:n-1);return `M${F(x+r1*Math.cos(a))},${F(y+r1*Math.sin(a))} L${F(x+r2*Math.cos(a))},${F(y+r2*Math.sin(a))} `}).join('');
const ARC=(x,y,r,a0,a1)=>`M${F(x+r*Math.cos(a0))},${F(y+r*Math.sin(a0))} A${r},${r} 0 0,1 ${F(x+r*Math.cos(a1))},${F(y+r*Math.sin(a1))} `;
const FUNNEL=(x,y,s=1)=>`M${F(x-80*s)},${y} H${F(x+80*s)} L${F(x+16*s)},${F(y+70*s)} V${F(y+112*s)} H${F(x-16*s)} V${F(y+70*s)} Z `;
const MAGNET=(x,y,s=1)=>`M${F(x-34*s)},${y} V${F(y-34*s)} a${F(34*s)},${F(34*s)} 0 0,1 ${F(68*s)},0 V${y} h${F(-22*s)} V${F(y-34*s)} a${F(12*s)},${F(12*s)} 0 0,0 ${F(-24*s)},0 V${y} Z M${F(x-34*s)},${F(y-14*s)} h${F(22*s)} M${F(x+12*s)},${F(y-14*s)} h${F(22*s)} `;
/* مدينة بسور: x المنتصف، y القاعدة، w نص العرض، n بيوت */
const WALL=(x,y,w,h=30)=>{let d=`M${x-w},${y} V${y-h} `;const n=Math.round(w/11);for(let i=0;i<n;i++)d+=`v-8 h${F(w/n)} v8 h${F(w/n)} `;return d+`V${y} Z M${x-10},${y} v-14 a10,10 0 0,1 20,0 v14 `};
const ROOFS=(x,y,w,k)=>PT(k).map(i=>{const hx=x-w+ (i+.5)*2*w/k;return i%2?`M${F(hx-13)},${y} v-16 a13,13 0 0,1 26,0 v16 `:`M${F(hx-13)},${y} v-14 l13,-11 l13,11 v14 `}).join('');
const TOWER=(x,y,s=1)=>`M${F(x-14*s)},${y} V${F(y-50*s)} h${F(-5*s)} v${F(-13*s)} h${F(8*s)} v${F(6*s)} h${F(7*s)} v${F(-6*s)} h${F(8*s)} v${F(6*s)} h${F(7*s)} v${F(-6*s)} h${F(8*s)} v${F(13*s)} h${F(-5*s)} V${y} Z `;
const SHOP=(x,y,s=1)=>`M${F(x-22*s)},${y} V${F(y-30*s)} h${F(44*s)} V${y} Z M${F(x-28*s)},${F(y-30*s)} l${F(8*s)},${F(-12*s)} h${F(40*s)} l${F(8*s)},${F(12*s)} Z `;
/* علم بشريط (تبعية) أو من غيره */
const STRIPE=(x,y,s=1)=>`M${x},${F(y-56*s)} h${F(-46*s)} `;
const LENS=(x,y,r)=>CI(x,y,r)+`M${F(x+r*.7)},${F(y+r*.7)} l${F(r*.9)},${F(r*.9)} `;
const NOTEB=(x,y,s=1)=>RC(+F(x-17*s),+F(y-22*s),+F(34*s),+F(44*s))+`M${F(x-9*s)},${F(y-10*s)} h${F(18*s)} M${F(x-9*s)},${y} h${F(18*s)} M${F(x-9*s)},${F(y+10*s)} h${F(12*s)} M${F(x+11*s)},${F(y-22*s)} v${F(44*s)} `;
const STAMP=(x,y,s=1)=>`M${F(x-13*s)},${y} h${F(26*s)} v${F(-8*s)} h${F(-26*s)} Z M${F(x-5*s)},${F(y-8*s)} v${F(-12*s)} h${F(10*s)} v${F(12*s)} `+CI(x,+F(y-27*s),+F(7*s));
const OBOOK=(x,y,s=1)=>`M${x},${y} q${F(-18*s)},${F(-10*s)} ${F(-34*s)},0 v${F(30*s)} q${F(16*s)},${F(-10*s)} ${F(34*s)},0 q${F(18*s)},${F(-10*s)} ${F(34*s)},0 v${F(-30*s)} q${F(-16*s)},${F(-10*s)} ${F(-34*s)},0 v${F(30*s)} `;
/* كتاب واقف على رف: x الطرف الشمال، y الرف */
const SPINE=(x,y,w,h)=>RC(x,y-h,w,h)+`M${x},${F(y-h*.82)} h${w} M${x},${F(y-h*.16)} h${w} `;
const SCHOOL=(x,y,s=1)=>`M${F(x-60*s)},${y} V${F(y-70*s)} H${F(x+60*s)} V${y} Z M${F(x-68*s)},${F(y-70*s)} L${x},${F(y-104*s)} L${F(x+68*s)},${F(y-70*s)} M${F(x-12*s)},${y} v${F(-30*s)} h${F(24*s)} v${F(30*s)} M${F(x-44*s)},${F(y-54*s)} h${F(20*s)} v${F(18*s)} h${F(-20*s)} Z M${F(x+24*s)},${F(y-54*s)} h${F(20*s)} v${F(18*s)} h${F(-20*s)} Z M${x},${F(y-104*s)} v${F(-26*s)} h${F(-20*s)} v${F(12*s)} h${F(20*s)} `;
const DSH=(x1,y1,x2,y2,n)=>PT(n).map(i=>`M${F(x1+(x2-x1)*i/n)},${F(y1+(y2-y1)*i/n)} L${F(x1+(x2-x1)*(i+.55)/n)},${F(y1+(y2-y1)*(i+.55)/n)} `).join('');
const PLUS=(x,y,s)=>`M${x-s},${y} h${2*s} M${x},${y-s} v${2*s} `;
const BOLT=(x,y,s=1)=>`M${x},${y} l${F(-12*s)},${F(22*s)} h${F(12*s)} l${F(-8*s)},${F(22*s)} `;
const PALMF=(x,t,b)=>RR(x-28,t,56,b-t+16,24);
const TABLE=(x,y,w)=>`M${x},${y} h${w} M${x+14},${y} v46 M${x+w-14},${y} v46 `;
const CAL=(x,y,s=1)=>RC(x,y,+F(70*s),+F(64*s))+`M${x},${F(y+16*s)} h${F(70*s)} M${F(x+16*s)},${F(y-7*s)} v${F(14*s)} M${F(x+54*s)},${F(y-7*s)} v${F(14*s)} `;
const CARDN=(o,n)=>{CARD(o,16,78,1034,450,G);W(o+.1,1030,112,'احفظ دي '+n,24,G)};
const QK=(o,x,y,d)=>Q(o,x,y,d);
/* عدّاد الوقفة بيختفي أول ما الوقفة تخلص */
function CDR2(o,x,y,r,n){const a=IT.length;CDR(o,x,y,r,n);for(let i=a;i<IT.length;i++)IT[i].off=T0+o*OS+n+.15}
const QM=(x,y,s=1)=>`M${F(x-10*s)},${F(y-14*s)} q${F(2*s)},${F(-16*s)} ${F(14*s)},${F(-14*s)} q${F(14*s)},${F(4*s)} ${F(4*s)},${F(20*s)} q${F(-6*s)},${F(6*s)} ${F(-6*s)},${F(14*s)} M${F(x+2*s)},${F(y+18*s)} v${F(3*s)} `;
const POLYD=(pts,n)=>pts.slice(1).map((p,i)=>DSH(pts[i][0],pts[i][1],p[0],p[1],n)).join('');

/* ---------- من L3A ---------- */
/* سلّم طالع لليمين: يبدأ من تحت الشمال (x,y) */
const STUP=(x,y,w,h,n)=>`M${x},${y} `+PT(n).map(()=>`h${w} v${-h} `).join('');
const TENT=(x,y,s=1)=>`M${F(x-28*s)},${y} L${x},${F(y-42*s)} L${F(x+28*s)},${y} Z M${x},${F(y-42*s)} v${F(-10*s)} M${x},${y} L${F(x-5*s)},${F(y-20*s)} `;
/* بوابة بعقد: x المنتصف، y القاعدة */
const ARCH=(x,y,w,h)=>`M${x-w/2-16},${y} V${y-h-18} H${x+w/2+16} V${y} M${x-w/2},${y} V${F(y-h*.55)} Q${x-w/2},${y-h} ${x},${y-h} Q${x+w/2},${y-h} ${x+w/2},${F(y-h*.55)} V${y} `;
const CROWN=(x,y,s=1)=>`M${F(x-60*s)},${y} L${F(x-72*s)},${F(y-62*s)} L${F(x-36*s)},${F(y-30*s)} L${x},${F(y-80*s)} L${F(x+36*s)},${F(y-30*s)} L${F(x+72*s)},${F(y-62*s)} L${F(x+60*s)},${y} Z `;
const CHR=(x,y,s=1)=>`M${x},${y} V${F(y-78*s)} M${x},${F(y-38*s)} H${F(x+46*s)} V${y} `;
const BULB=(x,y,s=1)=>CI(x,y,+F(14*s))+`M${F(x-6*s)},${F(y+15*s)} h${F(12*s)} M${F(x-4*s)},${F(y+21*s)} h${F(8*s)} `;
const NOTE=(x,y,w,h)=>RC(x,y,w,h)+`M${x+8},${F(y+h*.3)} h${w-16} M${x+8},${F(y+h*.55)} h${w-16} M${x+8},${F(y+h*.8)} h${F((w-16)*.6)} `;
const DESK=(x,y,w)=>`M${x},${y} h${w} M${x+12},${y} v40 M${x+w-12},${y} v40 `;
const WAVY=(x1,y,x2,a=8)=>{const n=Math.max(2,Math.round(Math.abs(x2-x1)/40)),w=(x2-x1)/n;return `M${x1},${y} q${F(w/2)},${-a} ${F(w)},0 `+PT(n-1).map(()=>`t${F(w)},0 `).join('')};
const COMP=(x,y,r)=>CI(x,y,r)+`M${x},${F(y-r*.7)} L${F(x+r*.25)},${y} L${x},${F(y+r*.7)} L${F(x-r*.25)},${y} Z `;
const DOME=(x,y,s=1)=>`M${F(x-34*s)},${y} V${F(y-34*s)} H${F(x+34*s)} V${y} Z M${F(x-22*s)},${F(y-34*s)} a${F(22*s)},${F(22*s)} 0 0,1 ${F(44*s)},0 M${x},${F(y-56*s)} v${F(-10*s)} M${F(x+34*s)},${y} V${F(y-70*s)} l${F(8*s)},${F(-12*s)} l${F(8*s)},${F(12*s)} V${y} `;
const DASH=(x1,y,x2,n)=>{const w=(x2-x1)/(2*n-1);return PT(n).map(i=>`M${F(x1+2*i*w)},${y} h${F(w)} `).join('')};
const PEARL=(x,y,r)=>CI(x,y,r)+`M${F(x-r*.45)},${F(y-r*.25)} q${F(r*.2)},${F(-r*.35)} ${F(r*.5)},${F(-r*.3)} `;
const CARDX=(o,x,y,w,h,n)=>{CARD(o,x,y,w,h,G);W(o+.15,x+w-16,y+34,'احفظ دي '+n,22,G)};
const BUBB=(o,x,y,w,h)=>{BUBBLE(o,x,y,w,h||46);W(o+.1,x+w-12,y+(h||46)-15,'بالبلدي:',18,GD)};
/* راية بشريط: السارية عند x، القاعدة y */
const RIB=(x,y,s,x2,y2)=>`M${x},${F(y-70*s)} Q${F((x+x2)/2)},${F(Math.min(y-70*s,y2)-26)} ${x2},${y2} `;
/* إيدين بيسلّموا: x,y المنتصف — يرجع [يمين، شمال، القبضة] */
const SHK=(x,y,s=1)=>[`M${F(x+70*s)},${F(y+14*s)} L${F(x+10*s)},${y}`,`M${F(x-70*s)},${F(y+14*s)} L${F(x-10*s)},${y}`,EL(x,y,+F(15*s),+F(11*s))];
/* عالِم بعمامة: رسم تخيّلي + اسم (x المنتصف) */
const DAD=(o,x,y,sz,col)=>W(o,x,y,'ض',sz,col||G,'middle');
/* شخبطة حروف غريبة عامّة */
const SCR=(x,y,n,a=9)=>`M${x},${y} `+PT(n).map(i=>`l6,${i%2?a:-a} `).join('');

/* ---------- إضافات L3C ---------- */
const ORG='#D9822B',LOR='#FDEBD3',GLS='#7FB8D6';
/* مقياس النيل: عمود مدرّج واقف في الميّه. x المنتصف، y القاعدة، h الطول */
const NILOM=(x,y,h)=>RC(x-14,y-h,28,h)+PT(Math.floor(h/22)).map(i=>`M${x-14},${y-14-i*22} h${i%2?9:16} `).join('')+`M${x-22},${y-h} h44 `;
/* مؤشر بنزين: x,y المركز (نص دايرة فوق) */
const GAUGE=(x,y,r)=>ARC(x,y,r,Math.PI,2*Math.PI)+`M${x-r},${y} H${x+r} `+RAYS(x,y,r*.78,r,5,Math.PI,2*Math.PI);
const NEEDLE=(x,y,r,a)=>`M${x},${y} L${F(x+r*.8*Math.cos(a))},${F(y+r*.8*Math.sin(a))} `+CI(x,y,5);
const CAR=(x,y,s=1)=>`M${F(x-50*s)},${y} v${F(-18*s)} l${F(16*s)},${F(-20*s)} h${F(58*s)} l${F(16*s)},${F(20*s)} h${F(10*s)} v${F(18*s)} Z `+CI(+F(x-28*s),y,+F(10*s))+CI(+F(x+30*s),y,+F(10*s));
/* ساقية: عجلة وعليها قواديس */
const SAQ=(x,y,r)=>WHEEL(x,y,r)+PT(8).map(i=>{const a=i*Math.PI/4;return RC(+F(x+r*Math.cos(a)-6),+F(y+r*Math.sin(a)-6),12,12)}).join('');
/* نول: x,y الركن الشمال فوق */
const LOOM=(x,y,w,h)=>`M${x},${y+h} V${y} M${x+w},${y+h} V${y} M${x-10},${y} h${w+20} M${x-10},${F(y+h*.72)} h${w+20} `+PT(6).map(i=>`M${F(x+w*(i+.5)/6)},${y} V${F(y+h*.72)} `).join('');
const CLOTH=(x,y,w,h)=>RC(x+6,F(y+h*.42),w-12,F(h*.3))+`M${x+6},${F(y+h*.57)} h${w-12} `;
/* حزمة كتان: سيقان رفيعة مربوطة. x المنتصف، y القاعدة */
const FLAX=(x,y,s=1)=>[-10,-4,3,10].map(d=>`M${F(x+d*.4*s)},${y} Q${F(x+d*.2*s)},${F(y-30*s)} ${F(x+d*1.3*s)},${F(y-62*s)} `).join('')+`M${F(x-9*s)},${F(y-16*s)} h${F(18*s)} `;
const FLXF=(x,y,s=1)=>[-10,-4,3,10].map(d=>CI(+F(x+d*1.3*s),+F(y-66*s),+F(4*s))).join('');
const CANE=(x,y,h)=>`M${x},${y} V${y-h} `+PT(4).map(i=>`M${x-6},${F(y-h*(i+1)/5)} h12 `).join('')+`M${x},${y-h} q16,-10 24,-2 M${x},${y-h} q-16,-12 -22,-4 `;
const PRESS=(x,y,s=1)=>CI(+F(x-17*s),y,+F(16*s))+CI(+F(x+17*s),y,+F(16*s))+`M${F(x-42*s)},${F(y+26*s)} h${F(84*s)} M${F(x-36*s)},${F(y+26*s)} v${F(-24*s)} M${F(x+36*s)},${F(y+26*s)} v${F(-24*s)} `;
const CONE=(x,y,s=1)=>`M${F(x-18*s)},${y} L${x},${F(y-46*s)} L${F(x+18*s)},${y} Z `;
const VASE=(x,y,s=1)=>`M${F(x-6*s)},${F(y-44*s)} h${F(12*s)} M${F(x-6*s)},${F(y-44*s)} q${F(-18*s)},${F(20*s)} ${F(-10*s)},${F(36*s)} q${F(4*s)},${F(8*s)} ${F(16*s)},${F(8*s)} q${F(12*s)},0 ${F(16*s)},${F(-8*s)} q${F(8*s)},${F(-16*s)} ${F(-10*s)},${F(-36*s)} `;
const FLASK=(x,y,r)=>CI(x,y,r)+`M${x+r*.4},${y-r*.9} l${r*.9},${-r*.5} M${x-r*.1},${y-r} l${r*.9},${-r*.5} `;
const SHIRT=(x,y,s=1)=>`M${F(x-14*s)},${F(y-30*s)} l${F(-16*s)},${F(10*s)} l${F(6*s)},${F(12*s)} l${F(8*s)},${F(-4*s)} V${y} h${F(32*s)} V${F(y-12*s)} l${F(8*s)},${F(4*s)} l${F(6*s)},${F(-12*s)} l${F(-16*s)},${F(-10*s)} q${F(-14*s)},${F(10*s)} ${F(-28*s)},0 Z `;
/* ميناء: رصيف بخوازيق. x الطرف الشمال، y سطح الرصيف */
const PIER=(x,y,w)=>RC(x,y,w,12)+PT(Math.max(2,Math.round(w/30))).map(i=>`M${x+10+i*30},${y+12} v22 `).join('');
const COIN=(x,y,r)=>CI(x,y,r)+CI(x,y,+F(r*.62));
const SAFE=(x,y,s=1)=>RC(+F(x-30*s),+F(y-56*s),+F(60*s),+F(50*s))+CI(x,+F(y-31*s),+F(10*s))+`M${F(x+10*s)},${F(y-31*s)} h${F(8*s)} M${F(x-24*s)},${F(y-6*s)} v${F(6*s)} M${F(x+24*s)},${F(y-6*s)} v${F(6*s)} `;
const FOLDER=(x,y,w,h)=>`M${x},${y} h${w} v${h} h${-w} Z M${x},${y} l14,-16 h70 l12,16 `;
const MUSC=(x,y,s=1)=>`M${x},${y} v${F(-22*s)} q${F(2*s)},${F(-20*s)} ${F(22*s)},${F(-30*s)} l${F(4*s)},${F(-18*s)} q${F(12*s)},${F(-4*s)} ${F(16*s)},${F(6*s)} l${F(-6*s)},${F(16*s)} q${F(26*s)},${F(2*s)} ${F(28*s)},${F(26*s)} q${F(2*s)},${F(20*s)} ${F(-20*s)},${F(22*s)} Z `;
const BREAD=(x,y,s=1)=>EL(x,y,+F(26*s),+F(13*s))+`M${F(x-10*s)},${F(y-8*s)} l${F(6*s)},${F(10*s)} M${F(x+2*s)},${F(y-10*s)} l${F(6*s)},${F(10*s)} `;
/* ميدان بتلات شوارع: يرجع {d, e:[نهايات]} */
const PLAZA=(x,y,r,ends)=>{let d=CI(x,y,r);ends.forEach(([ex,ey])=>{const a=Math.atan2(ey-y,ex-x),nx=-Math.sin(a)*14,ny=Math.cos(a)*14,sx=x+r*Math.cos(a),sy=y+r*Math.sin(a);d+=`M${F(sx+nx)},${F(sy+ny)} L${F(ex+nx)},${F(ey+ny)} M${F(sx-nx)},${F(sy-ny)} L${F(ex-nx)},${F(ey-ny)} `});return d};
/* سطر اختيار فاضي: شارة حرف + خط رمادي */
const OPT=(o,x,y,l,w)=>{BADGE(o,x,y,l);P(o+.05,`M${x-28},${y+6} H${x-28-w}`,GHO,3,.3)};
const RING=(x,y,a,b)=>EL(x,y,a,b);
/* كارت صغير مقلوب/مرجع: إطار + شارة رقم */
const MINI=(o,x,y,w,h,n)=>{P(o,RC(x,y,w,h),G,3,.4,'#fff');BADGE(o+.1,x+w-6,y+6,n)};
const SCH=(x,y,s=1)=>`M${F(x-40*s)},${y} V${F(y-50*s)} H${F(x+40*s)} V${y} Z M${F(x-8*s)},${y} v${F(-20*s)} h${F(16*s)} v${F(20*s)} M${F(x-28*s)},${F(y-38*s)} h${F(14*s)} v${F(12*s)} h${F(-14*s)} Z M${F(x+14*s)},${F(y-38*s)} h${F(14*s)} v${F(12*s)} h${F(-14*s)} Z M${x},${F(y-50*s)} v${F(-22*s)} h${F(-16*s)} v${F(10*s)} h${F(16*s)} `;

/* ---------- إضافات L4B ---------- */
const FRN='#3E5BA9',LFR='#E4E9F7',GOLD='#E0A800',CTN='#FFFFFF';
/* كتابة نص منطوق كلمة بكلمة: كل كلمة بتظهر لحظة نطقها (بيدوّر على العبارة في السطر الحالي) */
const NRM=s=>s.replace(/[«»،.:؛؟!()"]/g,'');
function FIND(text,n){const ws=text.split(/\s+/).map(NRM).filter(Boolean);const tk=CUR.filter(k=>!k.p);let c=0;
 for(let i=0;i+ws.length<=tk.length;i++){let ok=true;for(let j=0;j<ws.length;j++)if(NRM(tk[i+j].w)!==ws[j]){ok=false;break}
  if(ok){if(c==(n||0))return tk.slice(i,i+ws.length).map(k=>k.s/OS);c++}}
 throw new Error('FIND: «'+text+'» مش في السطر: '+CUR.map(k=>k.w).join(' '))}
/* SAYW(x,y,sz,col,text,{w,lh,n,hl,cont,dt}) يرجع y بتاع آخر سطر */
function SAYW(x,y,sz,col,text,o={}){const ts=FIND(text,o.n),ws=text.split(/\s+/).filter(w=>NRM(w));const mw=o.w||960,lh=o.lh||Math.round(sz*1.45),hl=o.hl||{};
 let cw=o.cont?(o.cw||0):0,first=!o.cont,yy=y;
 ws.forEach((w,i)=>{const ew=(NRM(w).length+(w.length-NRM(w).length)*.6)*sz*.48+sz*.5;const c=hl[NRM(w)]||col;const t=ts[i]+(o.dt||0);
  if(!first&&cw+ew>mw){yy+=lh;cw=0;first=true}
  if(first){W(t,x,yy,w,sz,c);first=false}else WC(t,w,c);cw+=ew});return yy}
/* فقاعة «بالبلدي» بنصها المنطوق كامل: الفقاعة بتترسم على «بالبلدي» رقم n */
function BBS(x,y,w,sz,text,n,o={}){const t0=at('بالبلدي',n||0);const lh=Math.round(sz*1.42);
 const lines=EST(text,sz,w-24,sz*.45*8+sz*.5);const h=lines*lh+16;BUBBLE(t0-.05,x,y,w,h);W(t0,x+w-12,y+sz+6,'بالبلدي:',sz,GD);
 SAYW(x+w-12,y+sz+6,sz,N,text,Object.assign({w:w-24,lh,cont:true,cw:sz*.45*8+sz*.5},o));return y+h}
/* فقاعة من غير «بالبلدي» */
function BBN(o0,x,y,w,sz,text,o={}){const lh=Math.round(sz*1.42),lines=EST(text,sz,w-24,0),h=lines*lh+16;BUBBLE(o0,x,y,w,h);SAYW(x+w-12,y+sz+6,sz,N,text,Object.assign({w:w-24,lh},o));return y+h}
function EST(text,sz,mw,c0){let n=1,cw=c0||0;text.split(/\s+/).filter(w=>NRM(w)).forEach(w=>{const ew=(NRM(w).length+(w.length-NRM(w).length)*.6)*sz*.48+sz*.5;if(cw>0&&cw+ew>mw){n++;cw=0}cw+=ew});return n}
const WALLET=(x,y,s=1)=>RR(+F(x-44*s),+F(y-58*s),+F(88*s),+F(58*s),+F(9*s))+`M${F(x-44*s)},${F(y-40*s)} h${F(88*s)} M${F(x+20*s)},${F(y-40*s)} v${F(14*s)} h${F(24*s)} `;
const FURN=(x,y,s=1)=>`M${F(x-46*s)},${y} A${F(46*s)},${F(42*s)} 0 0,1 ${F(x+46*s)},${y} Z M${F(x-16*s)},${y} v${F(-12*s)} a${F(16*s)},${F(14*s)} 0 0,1 ${F(32*s)},0 v${F(12*s)} `;
const BUFF=(x,y,s=1)=>EL(x,+F(y-34*s),+F(40*s),+F(20*s))+EL(+F(x+46*s),+F(y-44*s),+F(13*s),+F(10*s))+`M${F(x+40*s)},${F(y-52*s)} q${F(-4*s)},${F(-14*s)} ${F(-16*s)},${F(-12*s)} M${F(x+54*s)},${F(y-52*s)} q${F(6*s)},${F(-14*s)} ${F(18*s)},${F(-10*s)} M${F(x-26*s)},${F(y-18*s)} v${F(18*s)} M${F(x-10*s)},${F(y-16*s)} v${F(16*s)} M${F(x+14*s)},${F(y-16*s)} v${F(16*s)} M${F(x+28*s)},${F(y-18*s)} v${F(18*s)} M${F(x-40*s)},${F(y-36*s)} q${F(-10*s)},${F(6*s)} ${F(-8*s)},${F(20*s)} `;
const SHIP=(x,y,s=1)=>`M${F(x-70*s)},${y} h${F(140*s)} l${F(-18*s)},${F(26*s)} h${F(-104*s)} Z M${F(x-40*s)},${y} v${F(-24*s)} h${F(60*s)} v${F(24*s)} M${F(x-4*s)},${F(y-24*s)} v${F(-30*s)} h${F(16*s)} v${F(30*s)} M${F(x-30*s)},${F(y-12*s)} h${F(10*s)} M${F(x-12*s)},${F(y-12*s)} h${F(10*s)} `;
const FACT=(x,y,s=1)=>`M${F(x-54*s)},${y} V${F(y-40*s)} l${F(24*s)},${F(-18*s)} v${F(18*s)} l${F(24*s)},${F(-18*s)} v${F(18*s)} l${F(24*s)},${F(-18*s)} v${F(18*s)} H${F(x+36*s)} V${F(y-96*s)} h${F(16*s)} V${y} Z M${F(x-40*s)},${F(y-24*s)} h${F(14*s)} v${F(12*s)} h${F(-14*s)} Z M${F(x-12*s)},${F(y-24*s)} h${F(14*s)} v${F(12*s)} h${F(-14*s)} Z `;
const SMOKE=(x,y,s=1)=>`M${x},${y} q${F(-14*s)},${F(-10*s)} 0,${F(-20*s)} q${F(16*s)},${F(-10*s)} ${F(4*s)},${F(-24*s)} q${F(-12*s)},${F(-12*s)} ${F(6*s)},${F(-26*s)} `;
const SWD=(x,y,s=1)=>`M${x},${F(y-74*s)} l${F(-7*s)},${F(12*s)} V${F(y-18*s)} h${F(14*s)} V${F(y-62*s)} Z M${F(x-16*s)},${F(y-18*s)} h${F(32*s)} M${x},${F(y-18*s)} v${F(18*s)} `;
const HELM=(x,y,s=1)=>`M${F(x-26*s)},${y} a${F(26*s)},${F(26*s)} 0 0,1 ${F(52*s)},0 Z M${F(x-34*s)},${y} h${F(68*s)} M${x},${F(y-26*s)} v${F(-12*s)} `;
const BRICKS=(x,y,w,h,n)=>{const rh=h/n;let d=RC(x,y,w,h);for(let i=1;i<n;i++)d+=`M${x},${F(y+i*rh)} h${w} `;for(let i=0;i<n;i++){const off=i%2?0:20;for(let k=x+off+20;k<x+w-6;k+=40)d+=`M${F(k)},${F(y+i*rh)} v${F(rh)} `}return d};
const CHIPS=(x,y,s=1)=>`M${F(x-20*s)},${y} V${F(y-54*s)} l${F(5*s)},${F(-6*s)} l${F(5*s)},${F(6*s)} l${F(5*s)},${F(-6*s)} l${F(5*s)},${F(6*s)} l${F(5*s)},${F(-6*s)} l${F(5*s)},${F(6*s)} l${F(5*s)},${F(-6*s)} l${F(5*s)},${F(6*s)} V${y} Z `;
const SANDW=(x,y,s=1)=>`M${F(x-30*s)},${y} h${F(60*s)} L${x},${F(y-40*s)} Z M${F(x-24*s)},${F(y-6*s)} h${F(48*s)} `;
const PTAG=(x,y,w,h)=>`M${x},${y} l${F(h/2)},${F(-h/2)} h${w} v${h} h${-w} Z `+CI(+F(x+h/2+4),y,3);
const TREATY=(x,y,w,h)=>RC(x,y,w,h)+`M${x+14},${y+20} h${w-28} M${x+14},${y+36} h${w-28} M${x+14},${y+52} h${F((w-28)*.7)} `;
const HAT=(x,y,s=1)=>`M${F(x-26*s)},${y} h${F(52*s)} M${F(x-15*s)},${y} v${F(-26*s)} h${F(30*s)} v${F(26*s)} `;
const TARB=(x,y,s=1)=>`M${F(x-12*s)},${y} l${F(3*s)},${F(-18*s)} h${F(18*s)} l${F(3*s)},${F(18*s)} Z M${F(x+6*s)},${F(y-18*s)} q${F(8*s)},${F(2*s)} ${F(8*s)},${F(12*s)} `;
const PASS=(x,y,w,h)=>RR(x,y,w,h,6)+`M${x},${F(y+h*.35)} h${w} `;
const BHAND=(x,y,s=1)=>`M${F(x-60*s)},${y} q${F(-10*s)},${F(-30*s)} ${F(10*s)},${F(-34*s)} h${F(100*s)} q${F(24*s)},0 ${F(24*s)},${F(16*s)} q0,${F(14*s)} ${F(-20*s)},${F(18*s)} Z M${F(x+50*s)},${F(y-34*s)} q${F(22*s)},${F(-22*s)} ${F(36*s)},${F(-8*s)} M${F(x-60*s)},${y} l${F(-30*s)},${F(30*s)} M${F(x+64*s)},${F(y-16*s)} l${F(10*s)},${F(36*s)} `;
const PIGGY=(x,y,s=1)=>EL(x,+F(y-30*s),+F(40*s),+F(28*s))+`M${F(x+38*s)},${F(y-38*s)} h${F(12*s)} v${F(14*s)} h${F(-12*s)} M${F(x+10*s)},${F(y-56*s)} l${F(8*s)},${F(-12*s)} l${F(6*s)},${F(14*s)} M${F(x-22*s)},${F(y-6*s)} v${F(10*s)} M${F(x+20*s)},${F(y-6*s)} v${F(10*s)} M${F(x-10*s)},${F(y-58*s)} h${F(18*s)} M${F(x-40*s)},${F(y-34*s)} q${F(-12*s)},${F(-4*s)} ${F(-8*s)},${F(-14*s)} `;
const GLAS=(x,y,s=1)=>CI(+F(x-14*s),y,+F(11*s))+CI(+F(x+14*s),y,+F(11*s))+`M${F(x-3*s)},${y} h${F(6*s)} `;
const SCAF=(x,y,w,h)=>`M${x},${y} v${-h} M${x+w},${y} v${-h} M${F(x+w/2)},${y} v${-h} `+PT(3).map(i=>`M${x},${F(y-h*(i+1)/3)} h${w} `).join('')+`M${x},${y} L${F(x+w/2)},${F(y-h/3)} M${F(x+w/2)},${y} L${x+w},${F(y-h/3)} M${x},${F(y-h/3)} L${F(x+w/2)},${F(y-2*h/3)} `;
const BALE=(x,y,s=1)=>RR(+F(x-30*s),+F(y-40*s),+F(60*s),+F(40*s),+F(8*s))+`M${F(x-12*s)},${F(y-40*s)} v${F(40*s)} M${F(x+12*s)},${F(y-40*s)} v${F(40*s)} `;
const BOX3=(x,y,s=1)=>`M${F(x-26*s)},${y} V${F(y-40*s)} H${F(x+26*s)} V${y} Z M${F(x-26*s)},${F(y-40*s)} l${F(12*s)},${F(-12*s)} H${F(x+38*s)} l${F(-12*s)},${F(12*s)} M${F(x+38*s)},${F(y-52*s)} V${F(y-12*s)} L${F(x+26*s)},${y} M${x},${F(y-40*s)} v${F(40*s)} `;
const BOLL=(x,y,s=1)=>CI(+F(x-12*s),y,+F(13*s))+CI(+F(x+12*s),y,+F(13*s))+CI(x,+F(y-14*s),+F(13*s))+`M${F(x-14*s)},${F(y+12*s)} l${F(14*s)},${F(8*s)} l${F(14*s)},${F(-8*s)} M${x},${F(y+20*s)} v${F(22*s)} `;
const DOMI=(x,y,w,h,deg)=>{const r=RT(x,y,deg*Math.PI/180);return 'M'+r(-w/2,0)+' L'+r(-w/2,-h)+' L'+r(w/2,-h)+' L'+r(w/2,0)+' Z M'+r(-w/2,-h/2)+' L'+r(w/2,-h/2)+' '};
const CHART=(x,y,w,h)=>`M${x},${y-h} V${y} H${x+w} `;
const RISE=(x,y,w,h)=>`M${x+8},${y-10} L${F(x+w*.3)},${F(y-h*.2)} L${F(x+w*.55)},${F(y-h*.35)} L${F(x+w*.8)},${F(y-h*.7)} L${x+w-4},${y-h+4} `;
const DOVE=(x,y,s=1)=>`M${F(x-30*s)},${y} q${F(20*s)},${F(-4*s)} ${F(34*s)},${F(-16*s)} q${F(6*s)},${F(-8*s)} ${F(14*s)},${F(-4*s)} l${F(6*s)},${F(4*s)} l${F(-6*s)},${F(2*s)} q${F(-4*s)},${F(16*s)} ${F(-24*s)},${F(22*s)} Z M${F(x-4*s)},${F(y-10*s)} q${F(-6*s)},${F(-26*s)} ${F(-24*s)},${F(-30*s)} q${F(10*s)},${F(18*s)} ${F(10*s)},${F(30*s)} `;
const QUILL=(x,y,s=1)=>`M${x},${y} Q${F(x+10*s)},${F(y-40*s)} ${F(x+40*s)},${F(y-70*s)} Q${F(x+26*s)},${F(y-30*s)} ${x},${y} Z M${x},${y} l${F(-6*s)},${F(10*s)} `;
const HUT=(x,y,s=1)=>`M${F(x-16*s)},${y} V${F(y-16*s)} L${x},${F(y-30*s)} L${F(x+16*s)},${F(y-16*s)} V${y} Z `;
const BLDG=(x,y,ws,fh)=>{let d='',yy=y;ws.forEach((w,i)=>{d+=`M${F(x-w/2)},${yy} V${yy-fh} H${F(x+w/2)} V${yy} `;yy-=fh});return d+`M${F(x-ws[0]/2-14)},${y} H${F(x+ws[0]/2+14)} `};
const BAG=(x,y,s=1)=>RC(+F(x-16*s),+F(y-24*s),+F(32*s),+F(24*s))+`M${F(x-7*s)},${F(y-24*s)} v${F(-7*s)} h${F(14*s)} v${F(7*s)} `;
const HOE=(x,y,s=1)=>`M${x},${y} l${F(26*s)},${F(-46*s)} M${F(x+20*s)},${F(y-52*s)} l${F(14*s)},${F(8*s)} `;
const STETH=(x,y,s=1)=>`M${F(x-14*s)},${F(y-40*s)} q0,${F(26*s)} ${F(14*s)},${F(26*s)} q${F(14*s)},0 ${F(14*s)},${F(-26*s)} M${x},${F(y-14*s)} q0,${F(14*s)} ${F(12*s)},${F(14*s)} `+CI(+F(x+16*s),y,+F(6*s));
const NEWS=(x,y,w,h)=>RC(x,y,w,h)+`M${x+6},${y+10} h${w-12} M${x+6},${y+22} h${F((w-12)*.45)} M${x+6},${y+32} h${F((w-12)*.45)} M${F(x+w*.55)},${y+22} h${F(w*.38)} v${F(h-30)} h${F(-w*.38)} Z `;
const HAMM=(x,y,s=1)=>`M${x},${y} l${F(28*s)},${F(-28*s)} M${F(x+18*s)},${F(y-38*s)} l${F(20*s)},${F(20*s)} l${F(6*s)},${F(-6*s)} l${F(-20*s)},${F(-20*s)} Z `;
const SAW=(x,y,s=1)=>`M${x},${y} h${F(50*s)} l${F(-6*s)},${F(-16*s)} h${F(-44*s)} Z M${F(x+50*s)},${F(y-8*s)} h${F(14*s)} `;
const ROBE=(x,y,s=1)=>`M${F(x-12*s)},${F(y-44*s)} h${F(24*s)} l${F(12*s)},${F(44*s)} h${F(-48*s)} Z M${x},${F(y-44*s)} v${F(44*s)} `;
const SEAL=(x,y,r)=>CI(x,y,r)+CI(x,y,+F(r*.8));
const CHAIN=(x,y,n,r=10)=>PT(n).map(i=>i%2?`M${x+i*r*1.6-r*.4},${y} h${F(r*.8+r)} `:EL(+F(x+i*r*1.6+r*.4),y,+F(r*1.1),+F(r*.7))).join('');
const BOOKS=(x,y)=>SPINE(x,y,18,60)+SPINE(x+20,y,18,52)+SPINE(x+40,y,18,64);
const OFFICE=(x,y,s=1)=>RC(+F(x-50*s),+F(y-60*s),+F(100*s),+F(60*s))+`M${F(x-58*s)},${F(y-60*s)} L${x},${F(y-82*s)} L${F(x+58*s)},${F(y-60*s)} Z `;
const PSCR=(x,y,w,h)=>RC(x,y,w,h)+`M${x+w-12},${y+14} H${x+12} M${x+w-12},${y+28} H${x+12} M${x+w-12},${y+42} H${F(x+w*.4)} `;
/* إيد غريبة: كم أزرق + إيد */
const FHAND=(x,y,s=1)=>`M${F(x+60*s)},${F(y-12*s)} h${F(-34*s)} v${F(24*s)} h${F(34*s)} M${F(x+26*s)},${F(y-10*s)} h${F(-30*s)} q${F(-8*s)},${F(4*s)} 0,${F(8*s)} h${F(12*s)} M${F(x+26*s)},${F(y+10*s)} h${F(-24*s)} `;
const MOUTH=(x,y)=>`M${x-8},${y} q8,6 16,0 `;
/* ختم دايري ومكتوب جوّاه */
function SEALW(o,x,y,r,txt,col){P(o,SEAL(x,y,r),col||R,4,.4,'#fff');W(o+.1,x,y+Math.round(r*.22),txt,Math.round(r*.55),col||R,'middle')}
/* شخص بطربوش / ببرنيطة: x المنتصف، y أعلى الراس */
const TMANP=(x,y,h)=>MAN(x,y,h);
function PERS(o,x,y,h,col,hat,lab){P(o,MAN(x,y,h),col,3,.5);if(hat=='t')P(o+.15,TARB(x,y+2,h/90),R,3,.3,'#E58A7F');else if(hat=='h')P(o+.15,HAT(x,y+3,h/110),N,3,.3,N);else if(hat=='u')P(o+.15,TURB(x,y,h),col,3,.3,'#fff');if(lab)W(o+.25,x,y+h+20,'رسم تخيّلي',14,GR,'middle')}
/* لحية (محمد علي): تحت راس MAN(x,y,h) */
const BEARD=(x,y,h)=>{const r=h*.15;return `M${F(x-r*.8)},${F(y+r*1.5)} Q${F(x-r*.9)},${F(y+r*3.6)} ${x},${F(y+r*4)} Q${F(x+r*.9)},${F(y+r*3.6)} ${F(x+r*.8)},${F(y+r*1.5)} `};
function MALI(o,x,y,h,lab){P(o,MAN(x,y,h),N,4,.5);P(o+.15,TURB(x,y,h),N,3,.3,'#fff');P(o+.25,BEARD(x,y,h),GR,3,.3,'#eee');if(lab!==0)W(o+.3,x,y+h+20,'رسم تخيّلي',14,GR,'middle')}

/* ---------- من L4A (نفس رسم إسماعيل والمراية وموتيفات الدرس) ---------- */
const RED2='#C0392B',GRY='#7a8285',SHADE='#3a3f41';
const FEZH=(x,y,h)=>{const r=h*.15;return `M${F(x-r*.95)},${F(y+r*.45)} L${F(x-r*.72)},${F(y-r*.9)} H${F(x+r*.72)} L${F(x+r*.95)},${F(y+r*.45)} Z `};
const TASS=(x,y,h)=>{const r=h*.15;return `M${x},${F(y-r*.9)} q${F(r*.9)},${F(r*.1)} ${F(r*1.05)},${F(r*1.2)} `};
const TURBA=(x,y,h,k=1.6)=>{const r=h*.15;return EL(x,+F(y-r*.15),+F(r*k),+F(r*.95))+`M${F(x-r*k*.8)},${F(y-r*.35)} q${F(r*k*.8)},${F(r*.5)} ${F(r*k*1.6)},0 `};
const BEARDA=(x,y,h,L=1.6)=>{const r=h*.15;return `M${F(x-r*.9)},${F(y+r*1.25)} Q${F(x-r*.8)},${F(y+r*(2+L))} ${x},${F(y+r*(2.3+L))} Q${F(x+r*.8)},${F(y+r*(2+L))} ${F(x+r*.9)},${F(y+r*1.25)} `};
/* الخديو إسماعيل (نفس رسمة L4A: طربوش وشُرّابة ودقن قصيرة ونيشان) */
function ISMA(o,x,y,h,lab){const r=h*.15;P(o,MAN(x,y,h),N,3,.6);P(o+.2,FEZH(x,y,h),RED2,3,.35,RED2);P(o+.3,TASS(x,y,h),N,2.5,.2);P(o+.35,BEARDA(x,y,h,.5),N,2.5,.3,'#6b5a4a');
 P(o+.45,`M${F(x-h*.12)},${F(y+h*.4)} L${F(x+h*.1)},${F(y+h*.62)} `+CI(+F(x+h*.08),+F(y+h*.46),+F(h*.035))+CI(+F(x-h*.07),+F(y+h*.52),+F(h*.035)),YD,3,.3,Y);
 if(lab!==false)W(o+.3,x,y+h+20,'رسم تخيّلي',14,GR,'middle')}
const MIRR=(x,y,s=1)=>EL(x,y,+F(34*s),+F(46*s))+`M${x},${F(y+46*s)} v${F(18*s)} M${F(x-20*s)},${F(y+64*s)} h${F(40*s)} `;
const BOATS=(x,y,s=1)=>SAIL(x,y,s)+CI(+F(x-12*s),+F(y-6*s),+F(4*s))+CI(+F(x+12*s),+F(y-6*s),+F(4*s));
const TGT=(x,y,r)=>CI(x,y,r)+CI(x,y,+F(r*.66))+CI(x,y,+F(r*.33));
const DART=(x1,y1,x2,y2)=>{const a=Math.atan2(y2-y1,x2-x1),p=(d,k)=>F(x1+d*Math.cos(a+k))+','+F(y1+d*Math.sin(a+k));return `M${x1},${y1} L${x2},${y2} M${x1},${y1} L${p(18,.5)} M${x1},${y1} L${p(18,-.5)} M${p(10,0)} L${p(26,.45)} M${p(10,0)} L${p(26,-.45)} `};
const XSW=(x,y,s=1)=>`M${F(x-40*s)},${F(y+40*s)} L${F(x+36*s)},${F(y-36*s)} M${F(x+40*s)},${F(y+40*s)} L${F(x-36*s)},${F(y-36*s)} M${F(x-36*s)},${F(y+22*s)} l${F(16*s)},${F(16*s)} M${F(x+36*s)},${F(y+22*s)} l${F(-16*s)},${F(16*s)} `;
const MIC=(x,y,s=1)=>RR(+F(x-12*s),+F(y-40*s),+F(24*s),+F(40*s),+F(12*s))+`M${F(x-20*s)},${F(y-14*s)} q0,${F(26*s)} ${F(20*s)},${F(26*s)} q${F(20*s)},0 ${F(20*s)},${F(-26*s)} M${x},${F(y+12*s)} v${F(30*s)} M${F(x-16*s)},${F(y+42*s)} h${F(32*s)} `;
const THRONE=(x,y,s=1)=>`M${F(x-40*s)},${y} V${F(y-120*s)} q${F(40*s)},${F(-30*s)} ${F(80*s)},0 V${y} M${F(x-52*s)},${F(y-50*s)} h${F(104*s)} M${F(x-52*s)},${F(y-50*s)} v${F(-30*s)} M${F(x+52*s)},${F(y-50*s)} v${F(-30*s)} `;
const GRAB=(x,y,s=1)=>RR(+F(x-14*s),+F(y-12*s),+F(28*s),+F(24*s),+F(8*s))+`M${F(x-6*s)},${F(y-12*s)} v${F(24*s)} M${F(x+3*s)},${F(y-12*s)} v${F(24*s)} `;

/* ---------- إضافات L4C ---------- */
const LMP='#FFF6D6';
/* شخص حقيقي برسم تخيّلي: afg الأفغاني (عمامة كبيرة ودقن طويلة)، abd محمد عبده (عمامة أصغر ودقن قصيرة)، lut لطفي السيد (طربوش ونضارة)،
   tah الطهطاوي (نفس رسمة L4B: عمامة)، kam مصطفى كامل (طربوش وشنب)، far محمد فريد (طربوش ودقن) */
function FIGX(o,x,y,h,kind,col,lab){const r=h*.15;P(o,MAN(x,y,h),col,3,.5);
 if(kind=='afg'){P(o+.15,TURBA(x,y,h,1.75),col,3,.3,'#fff');P(o+.25,BEARDA(x,y,h,1.6),GRY,2.5,.3,'#eef0f0')}
 else if(kind=='abd'){P(o+.15,TURBA(x,y,h,1.3),col,3,.3,'#fff');P(o+.25,BEARDA(x,y,h,.8),N,2.5,.3,'#8a7a6a')}
 else if(kind=='tah'){P(o+.15,TURB(x,y,h),col,3,.3,'#fff')}
 else if(kind=='lut'){P(o+.15,TARB(x,y+2,h/90),R,3,.3,'#E58A7F');P(o+.25,GLAS(x,+F(y+r*.95),+F(r/16)),N,2,.3)}
 else if(kind=='kam'){P(o+.15,TARB(x,y+2,h/90),R,3,.3,'#E58A7F');P(o+.25,`M${F(x-r*.6)},${F(y+r*1.45)} q${F(r*.3)},${F(-r*.25)} ${F(r*.6)},0 q${F(r*.3)},${F(-r*.25)} ${F(r*.6)},0`,N,3,.2)}
 else if(kind=='far'){P(o+.15,TARB(x,y+2,h/90),R,3,.3,'#E58A7F');P(o+.25,BEARDA(x,y,h,.9),N,2.5,.3,'#6b5a4a')}
 if(lab!==false)W(o+.2,x,y+h+20,'رسم تخيّلي',14,GR,'middle')}
/* كارت عنوان */
function TITLE(o,text,hl,sz){P(o,RC(16,84,1034,70),BRN,4,.6,CREAM);SAYW(1030,134,sz||34,N,text,{hl:hl||{}})}
/* مركب البعثة (موتيف L4A) */
const BOATB=(o,x,y,s)=>{P(o,BOATS(x,y,s),BLU,3,.4,'#fff');P(o+.2,WAVY(x-60*s,y+14*s,x+60*s,5),BLU,3,.3)};
/* لمبة الأفكار */
const LAMP=(o,x,y,s)=>{P(o,BULB(x,y,s),YD,4,.4,LYL);P(o+.2,RAYS(x,y,18*s,26*s,8),YD,3,.3)};
/* ميكروسكوب: x,y القاعدة */
const MICRO=(x,y,s=1)=>`M${F(x-30*s)},${y} h${F(60*s)} M${F(x+16*s)},${y} V${F(y-34*s)} q0,${F(-26*s)} ${F(-24*s)},${F(-40*s)} M${F(x-20*s)},${F(y-58*s)} l${F(14*s)},${F(-20*s)} l${F(12*s)},${F(8*s)} l${F(-14*s)},${F(20*s)} Z M${F(x-16*s)},${F(y-20*s)} h${F(32*s)} `;
/* راس فيه ترس */
const HEADG=(x,y,s=1)=>`M${F(x+30*s)},${F(y+50*s)} V${F(y+20*s)} Q${F(x+50*s)},${F(y-10*s)} ${F(x+40*s)},${F(y-40*s)} Q${F(x+20*s)},${F(y-80*s)} ${F(x-20*s)},${F(y-70*s)} Q${F(x-56*s)},${F(y-60*s)} ${F(x-52*s)},${F(y-20*s)} l${F(-10*s)},${F(16*s)} l${F(12*s)},${F(4*s)} v${F(14*s)} q${F(6*s)},${F(10*s)} ${F(26*s)},${F(6*s)} V${F(y+50*s)} `;
/* صندوق انتخاب بورقة */
const BALLOT=(x,y,s=1)=>RC(+F(x-36*s),+F(y-56*s),+F(72*s),+F(56*s))+`M${F(x-16*s)},${F(y-56*s)} h${F(32*s)} `;
const VOTE=(x,y,s=1)=>RC(+F(x-12*s),+F(y-86*s),+F(24*s),+F(32*s))+`M${F(x-6*s)},${F(y-72*s)} l${F(4*s)},${F(5*s)} l${F(8*s)},${F(-9*s)} `;
/* يافطة على عصاية */
const SIGN=(x,y,w,h)=>RC(x,y,w,h)+`M${F(x+w/2)},${y+h} v${F(Math.min(50,h*.6))} `;
/* ورقة نتيجة (تقويم) */
const CALP=(x,y,w,h)=>RC(x,y,w,h)+`M${x},${F(y+h*.26)} h${w} M${F(x+w*.25)},${y-8} v16 M${F(x+w*.75)},${y-8} v16 `;
/* غربال */
const SIEVE=(x,y,s=1)=>`M${F(x-60*s)},${y} h${F(120*s)} l${F(-14*s)},${F(30*s)} h${F(-92*s)} Z `+PT(5).map(i=>`M${F(x-40*s+i*20*s)},${F(y+6*s)} v${F(18*s)} `).join('');
/* قطر بعربيتين */
const TRAIN=(x,y,s=1)=>RC(+F(x-60*s),+F(y-40*s),+F(50*s),+F(40*s))+RC(+F(x-4*s),+F(y-40*s),+F(60*s),+F(40*s))+`M${F(x+56*s)},${F(y-40*s)} v${F(-14*s)} h${F(10*s)} v${F(14*s)} `+CI(+F(x-44*s),+F(y+4*s),+F(7*s))+CI(+F(x-24*s),+F(y+4*s),+F(7*s))+CI(+F(x+12*s),+F(y+4*s),+F(7*s))+CI(+F(x+40*s),+F(y+4*s),+F(7*s));
/* سحابة */
const CLOUD=(x,y,s=1)=>`M${F(x-60*s)},${y} q${F(-24*s)},${F(-30*s)} ${F(10*s)},${F(-40*s)} q${F(14*s)},${F(-36*s)} ${F(50*s)},${F(-20*s)} q${F(30*s)},${F(-24*s)} ${F(52*s)},${F(8*s)} q${F(36*s)},${F(10*s)} ${F(10*s)},${F(52*s)} Z `;
/* موبايل */
const MOB=(x,y,w,h)=>RR(x,y,w,h,12)+`M${F(x+w/2-10)},${y+h-10} h20 `+RC(x+10,y+16,w-20,F(h*.6));
/* طير صغير */
const BIRD=(x,y,s=1)=>`M${F(x-14*s)},${y} q${F(7*s)},${F(-10*s)} ${F(14*s)},0 q${F(7*s)},${F(-10*s)} ${F(14*s)},0 `;
/* كوبري بين شطين */
const KOBRI=(x,y,w)=>`M${x},${y} h${w} M${x},${y+12} h${w} M${x},${y+12} Q${F(x+w/2)},${y+80} ${x+w},${y+12} `+PT(5).map(i=>`M${F(x+w*(i+1)/6)},${y+12} v${F(14+Math.sin(Math.PI*(i+1)/6)*50)} `).join('');
const SHORE=(x,y,w,h)=>`M${x},${y} h${w} v${h} h${-w} `;
/* حلقة سلسلة (الدرس ٣) */
const CHLINK=(x,y,s=1)=>EL(x,y,+F(26*s),+F(14*s))+EL(+F(x+40*s),y,+F(26*s),+F(14*s));
/* عملة بوشّين */
const DISC=(x,y,r)=>CI(x,y,r)+CI(x,y,+F(r*.86));
/* شط بحر */
const SEA=(x1,y,x2)=>WAVY(x1,y,x2,6)+WAVY(x1,y+16,x2,6);
/* تاج مايل (واقع): نفس CROWN متلفّ بزاوية */
const CROWNR=(x,y,s,deg)=>{const r=RT(x,y,deg*Math.PI/180);return 'M'+[[-60,0],[-72,-62],[-36,-30],[0,-80],[36,-30],[72,-62],[60,0]].map(([a,b])=>r(a*s,b*s)).join(' L')+' Z '};
/* كاس دوري */
const CUP=(x,y,s=1)=>`M${F(x-34*s)},${y} q0,${F(56*s)} ${F(34*s)},${F(56*s)} q${F(34*s)},0 ${F(34*s)},${F(-56*s)} Z M${x},${F(y+56*s)} v${F(20*s)} M${F(x-22*s)},${F(y+80*s)} h${F(44*s)} M${F(x-34*s)},${F(y+10*s)} q${F(-20*s)},0 ${F(-14*s)},${F(22*s)} l${F(16*s)},${F(8*s)} M${F(x+34*s)},${F(y+10*s)} q${F(20*s)},0 ${F(14*s)},${F(22*s)} l${F(-16*s)},${F(8*s)} `;
/* طريق داخل لبعيد */
const ROAD=(x,y,w,h)=>`M${x},${y} L${F(x+w*.42)},${y-h} M${x+w},${y} L${F(x+w*.58)},${y-h} `+PT(4).map(i=>{const t=i/4,t2=(i+.5)/4;return `M${F(x+w/2)},${F(y-h*t)} L${F(x+w/2)},${F(y-h*t2)} `}).join('');
/* ورقة امتحان */
const EXAM=(x,y,w,h)=>RC(x,y,w,h)+`M${x+10},${y+18} h${w-20} M${x+10},${y+34} h${w-20} M${x+10},${y+50} h${F((w-20)*.6)} `;
/* خريطة مصر بقناة: يرجع نقطة بداية/نهاية القناة على EGO(x,y,s) */
const CANP=(x,y,s)=>({a:[+F(x+290*s),+F(y+10*s)],b:[+F(x+300*s),+F(y+100*s)]});
const SPK=(x,y,s=1)=>`M${x},${F(y-8*s)} h${F(10*s)} l${F(12*s)},${F(-10*s)} v${F(36*s)} l${F(-12*s)},${F(-10*s)} h${F(-10*s)} Z M${F(x+30*s)},${F(y-4*s)} q${F(8*s)},${F(9*s)} 0,${F(18*s)} `;
/* سؤال مراجعة: ؟ + عدّاد الوقفة على أول وقفة */
const RQ=(y,qx,qy)=>{Q(atp(),qx,qy,2);CDR2(atp(),qx-80,qy-10,14,2)};

/* ---------- إضافات L5A ---------- */
const MSK='#6C3483',LMS='#F4ECF7',ORN='#E67E22',KHK='#8A7A3A';
/* من L4A: كف بخمس صوابع، وعين مقفولة، وملعب */
const FING=(x,y,s=1)=>[[-.95,-.35],[-.55,-1.25],[0,-1.45],[.55,-1.3],[1.0,-.75]].map(([a,b])=>[+F(x-a*100*s),+F(y+b*100*s)]);
function PALM(o,x,y,s,col,d){const t=FING(x,y,s);P(o,EL(x,y,+F(62*s),+F(48*s)),N,4,.5,SKIN);P(o+(d||.3),t.map((q,i)=>`M${F(x+(q[0]-x)*.35)},${F(y+(q[1]-y)*.3)} L${q[0]},${q[1]}`).join(' '),N,+F(14*s),.7);return t}
const EYEC=(x,y,s=1)=>`M${F(x-22*s)},${y} q${F(22*s)},${F(12*s)} ${F(44*s)},0 M${F(x-12*s)},${F(y+8*s)} l-4,8 M${x},${F(y+10*s)} v9 M${F(x+12*s)},${F(y+8*s)} l4,8 `;
const FIELD=(x,y,w,h)=>RC(x,y,w,h)+`M${F(x+w/2)},${y} v${h} `+CI(+F(x+w/2),+F(y+h/2),+F(h*.18))+RC(x,+F(y+h*.3),+F(w*.1),+F(h*.4))+RC(+F(x+w*.9),+F(y+h*.3),+F(w*.1),+F(h*.4));
/* الإيد الغريبة (موتيف الدرس ٥): كم أزرق داخل من الشمال (برّه) + قبضة بخمس صوابع مقفولة. x,y مركز القبضة. يرجع مكان الصوابع */
const GHF=(x,y,s=1)=>PT(4).map(i=>[+F(x+34*s),+F(y-27*s+i*18*s)]).concat([[+F(x-4*s),+F(y-44*s)]]);
function GHAND(o,x,y,s,L){s=s||1;L=L||200;P(o,`M${F(x-34*s)},${F(y-30*s)} H${F(x-34*s-L*s)} M${F(x-34*s)},${F(y+30*s)} H${F(x-34*s-L*s)} M${F(x-34*s)},${F(y-34*s)} v${F(68*s)} M${F(x-50*s)},${F(y-32*s)} v${F(64*s)}`,FRN,5,.4,null);
 P(o+.25,RR(+F(x-32*s),+F(y-36*s),+F(66*s),+F(72*s),+F(18*s)),N,4,.4,SKIN);
 P(o+.45,PT(4).map(i=>`M${F(x+26*s)},${F(y-36*s+i*18*s)} q${F(16*s)},${F(9*s)} 0,${F(18*s)} `).join('')+`M${F(x-24*s)},${F(y-36*s)} q${F(24*s)},${F(-18*s)} ${F(40*s)},${F(2*s)} `,N,3,.4);return GHF(x,y,s)}
/* قناع مسرح: وش مبتسم (k=1) أو عابس (k=-1). x,y المركز */
const MFACE=(x,y,s=1)=>`M${F(x-40*s)},${F(y-40*s)} Q${x},${F(y-62*s)} ${F(x+40*s)},${F(y-40*s)} Q${F(x+48*s)},${F(y+22*s)} ${x},${F(y+58*s)} Q${F(x-48*s)},${F(y+22*s)} ${F(x-40*s)},${F(y-40*s)} Z `;
const MFEAT=(x,y,s,k)=>(k>0?`M${F(x-26*s)},${F(y-8*s)} q${F(9*s)},${F(-12*s)} ${F(18*s)},0 M${F(x+8*s)},${F(y-8*s)} q${F(9*s)},${F(-12*s)} ${F(18*s)},0 M${F(x-22*s)},${F(y+16*s)} q${F(22*s)},${F(24*s)} ${F(44*s)},0 `
 :`M${F(x-26*s)},${F(y-16*s)} l${F(18*s)},${F(8*s)} M${F(x+26*s)},${F(y-16*s)} l${F(-18*s)},${F(8*s)} M${F(x-22*s)},${F(y+34*s)} q${F(22*s)},${F(-22*s)} ${F(44*s)},0 `);
function MASK(o,x,y,s,k){P(o,MFACE(x,y,s),MSK,4,.5,k>0?'#FFF6D6':'#E3DCEA');P(o+.3,MFEAT(x,y,s,k),N,4,.4)}
/* قناع بوشّين على عصاية: المبتسم قدام يمين، والعابس ورا شمال */
function MASK2(o,x,y,s,front){P(o,`M${F(x-10*s)},${F(y+56*s)} v${F(90*s)}`,BRN,6,.3);
 if(front==-1){MASK(o+.1,Math.round(x+34*s),Math.round(y-6*s),s*.9,1);MASK(o+.3,Math.round(x-24*s),y,s,-1)}else{MASK(o+.1,Math.round(x-44*s),Math.round(y-6*s),s*.9,-1);MASK(o+.3,x,y,s,1)}}
/* نابليون: بدلة وقبعة بقرنين */
const BICORN=(x,y,h)=>{const r=h*.15;return `M${F(x-r*2)},${F(y+r*.5)} Q${x},${F(y-r*1.9)} ${F(x+r*2)},${F(y+r*.5)} Q${x},${F(y-r*.2)} ${F(x-r*2)},${F(y+r*.5)} Z `};
function NAPO(o,x,y,h,lab){const r=h*.15;P(o,MAN(x,y,h),FRN,4,.5);P(o+.2,BICORN(x,y,h),N,3,.3,N);P(o+.3,`M${F(x-h*.12)},${F(y+h*.34)} h${F(h*.24)} M${F(x-h*.1)},${F(y+h*.42)} l${F(h*.1)},${F(h*.06)} l${F(h*.1)},${F(-h*.06)}`,YD,3,.3);if(lab!==false)W(o+.3,x,y+h+20,'رسم تخيّلي',14,GR,'middle')}
/* شامبليون: بكراسة وقلم */
function CHAMP(o,x,y,h,lab){P(o,MAN(x,y,h),BLU,4,.5);P(o+.2,`M${F(x-h*.35)},${F(y+h*.3)} h${F(h*.18)} v${F(h*.24)} h${F(-h*.18)} Z`,N,3,.3,'#fff');P(o+.3,PENCIL(+F(x+h*.2),+F(y+h*.5),h/200),N,2,.3,Y);if(lab!==false)W(o+.3,x,y+h+20,'رسم تخيّلي',14,GR,'middle')}
/* عسكري ببدلة كاكي وخوذة، دراعه ممدود لليمين */
function SOLD(o,x,y,h){const r=h*.15;P(o,MAN(x,y,h),KHK,4,.5);P(o+.2,`M${F(x-r*1.4)},${F(y+r*.6)} a${F(r*1.4)},${F(r*1.3)} 0 0,1 ${F(r*2.8)},0 Z M${F(x-r*1.9)},${F(y+r*.6)} h${F(r*3.8)}`,KHK,3,.3,'#D8CFA0')}
/* حجر رشيد: لوح غامق بتلات طبقات. x,y الركن الشمال فوق */
const ROSE=(x,y,w,h)=>`M${x},${y+h} V${y+22} Q${x+4},${y} ${x+26},${y-2} L${F(x+w*.6)},${y+8} L${x+w-18},${y+2} Q${x+w},${y+6} ${x+w},${y+26} V${y+h} Z `;
const ROSEL=(x,y,w,h)=>`M${x},${F(y+h*.36)} H${x+w} M${x},${F(y+h*.68)} H${x+w} `;
/* مكنة جعانة: صندوق ببقّ مفتوح على الشمال ومدخنة. x,y المركز */
const MACH=(x,y,s=1)=>RR(+F(x-70*s),+F(y-60*s),+F(140*s),+F(120*s),+F(14*s))+`M${F(x+30*s)},${F(y-60*s)} v${F(-50*s)} h${F(22*s)} v${F(50*s)} `+GEAR(+F(x+22*s),+F(y+14*s),+F(18*s));
const JAW=(x,y,s=1)=>`M${F(x-70*s)},${F(y-34*s)} L${F(x-22*s)},${F(y-6*s)} L${F(x-70*s)},${F(y+28*s)} M${F(x-62*s)},${F(y-29*s)} l${F(4*s)},${F(9*s)} l${F(8*s)},${F(-4*s)} l${F(4*s)},${F(9*s)} l${F(8*s)},${F(-4*s)} M${F(x-62*s)},${F(y+23*s)} l${F(4*s)},${F(-9*s)} l${F(8*s)},${F(4*s)} l${F(4*s)},${F(-9*s)} l${F(8*s)},${F(4*s)} `;
/* كشك عصير */
const KIOSK=(x,y,s=1)=>RC(+F(x-60*s),+F(y-60*s),+F(120*s),+F(60*s))+`M${F(x-70*s)},${F(y-60*s)} l${F(12*s)},${F(-30*s)} h${F(116*s)} l${F(12*s)},${F(30*s)} Z M${F(x-34*s)},${F(y-90*s)} l${F(-6*s)},${F(30*s)} M${x},${F(y-90*s)} v${F(30*s)} M${F(x+34*s)},${F(y-90*s)} l${F(6*s)},${F(30*s)} M${F(x+44*s)},${F(y-60*s)} v${F(-56*s)} `;
const CRATE=(x,y,s=1)=>RC(+F(x-30*s),+F(y-28*s),+F(60*s),+F(28*s))+`M${F(x-30*s)},${F(y-14*s)} h${F(60*s)} `;
const ORNG=(x,y,s=1)=>CI(+F(x-16*s),+F(y-36*s),+F(9*s))+CI(x,+F(y-38*s),+F(9*s))+CI(+F(x+16*s),+F(y-36*s),+F(9*s));
/* ماسورة شافطة: من (x1,y1) لـ (x2,y2) بخطين متوازيين */
const PIPE=(x1,y1,x2,y2,w=10)=>`M${x1},${y1-w} L${x2},${y2-w} M${x1},${y1+w} L${x2},${y2+w} M${x2},${y2-w-6} v${2*w+12} `;
/* جزمة عسكري مغروسة: x الطرف الشمال، y الأرض */
const BOOT=(x,y,s=1)=>`M${x},${F(y-90*s)} V${F(y-10*s)} H${F(x+50*s)} q${F(10*s)},0 ${F(10*s)},${F(10*s)} V${y} H${F(x-4*s)} V${F(y-90*s)} Z M${F(x-6*s)},${F(y-90*s)} h${F(32*s)} `;
/* ساعة رملية */
const HGL=(x,y,s=1)=>`M${F(x-24*s)},${F(y-40*s)} h${F(48*s)} M${F(x-24*s)},${F(y+40*s)} h${F(48*s)} M${F(x-18*s)},${F(y-40*s)} L${F(x+18*s)},${F(y+40*s)} M${F(x+18*s)},${F(y-40*s)} L${F(x-18*s)},${F(y+40*s)} `;
/* جدر شجرة طويل نازل */
const ROOT=(x,y,s=1)=>`M${x},${y} V${F(y+90*s)} M${x},${F(y+30*s)} q${F(-30*s)},${F(20*s)} ${F(-40*s)},${F(70*s)} M${x},${F(y+40*s)} q${F(30*s)},${F(20*s)} ${F(36*s)},${F(66*s)} M${x},${F(y+70*s)} q${F(-14*s)},${F(14*s)} ${F(-16*s)},${F(40*s)} `;
const CLK=(x,y,r)=>CI(x,y,r)+`M${x},${y} V${F(y-r*.65)} M${x},${y} L${F(x+r*.45)},${F(y+r*.2)} `;
const FRAME=(x,y,w,h)=>RC(x,y,w,h)+RC(x+12,y+12,w-24,h-24);
/* مكنة طباعة قديمة (مكبس): x المنتصف، y الأرض */
const PRSS=(x,y,s=1)=>`M${F(x-50*s)},${y} V${F(y-110*s)} H${F(x+50*s)} V${y} M${F(x-60*s)},${y} h${F(120*s)} M${x},${F(y-110*s)} v${F(40*s)} M${F(x-26*s)},${F(y-90*s)} h${F(52*s)} M${F(x-34*s)},${F(y-70*s)} h${F(68*s)} v${F(12*s)} h${F(-68*s)} Z M${F(x-40*s)},${F(y-30*s)} h${F(80*s)} `;
/* ورقة طالعة من المكنة */
const SHEET=(x,y,w,h)=>RC(x,y,w,h)+`M${x+8},${y+12} h${w-16} M${x+8},${y+24} h${w-16} M${x+8},${y+36} h${F((w-16)*.6)} `;
/* شعلة مطفية: لهب + دخان صغير */
const OUTF=(x,y,s=1)=>`M${x},${y} q${F(-12*s)},${F(-12*s)} 0,${F(-26*s)} q${F(12*s)},${F(14*s)} 0,${F(26*s)} Z M${F(x-14*s)},${F(y+2*s)} h${F(28*s)} `;
/* منشور ملفوف */
const ROLL=(x,y,s=1)=>RC(+F(x-30*s),+F(y-12*s),+F(60*s),+F(24*s))+EL(+F(x-30*s),y,+F(6*s),+F(12*s))+EL(+F(x+30*s),y,+F(6*s),+F(12*s));
/* هدية متغلّفة: x المنتصف، y الأرض */
const GIFT=(x,y,s=1)=>RC(+F(x-22*s),+F(y-36*s),+F(44*s),+F(36*s))+`M${x},${F(y-36*s)} v${F(36*s)} M${F(x-22*s)},${F(y-20*s)} h${F(44*s)} M${x},${F(y-36*s)} q${F(-14*s)},${F(-14*s)} ${F(-16*s)},0 M${x},${F(y-36*s)} q${F(14*s)},${F(-14*s)} ${F(16*s)},0 `;
/* شق كبير بين حاجتين */
const SPLIT=(x,y1,y2)=>`M${x},${y1} l-14,${F((y2-y1)*.2)} l20,${F((y2-y1)*.2)} l-20,${F((y2-y1)*.2)} l20,${F((y2-y1)*.2)} l-6,${F((y2-y1)*.2)} `;
/* ورقة مقطوعة نصين */
const TORN=(x,y,w,h)=>`M${x},${y} h${F(w*.45)} l-8,${F(h*.3)} l10,${F(h*.3)} l-6,${F(h*.4)} H${x} Z M${F(x+w*.55)},${y} H${x+w} V${y+h} H${F(x+w*.55-4)} l6,${F(-h*.4)} l-10,${F(-h*.3)} Z `;
/* بوست صغير */
const POST=(x,y,w)=>RR(x,y,w,30,6)+CI(x+w-14,y+15,7)+`M${x+w-28},${y+12} h${F(-(w-44))} M${x+w-28},${y+21} h${F(-(w-60))} `;
/* سهم بيلف (دوامة) */
const SWIRL=(x,y,r)=>`M${F(x+r)},${y} A${r},${r} 0 1,1 ${x},${F(y-r)} M${x},${F(y-r)} l10,-8 M${x},${F(y-r)} l10,8 `;
/* طفل صغير بتاج فرعوني */
function KID(o,x,y,h){P(o,MAN(x,y,h),G,3,.4);P(o+.2,PSCH(x,+F(y+h*.1),h/220),R,3,.3,'#fff')}
/* سقالة على مبنى صغير */
const BADGE2=(o,x,y,n,c)=>{P(o,CI(x,y,15),c||R,3,.25,'#fff');W(o+.08,x,y+8,n,20,c||R,'middle')};
const EXC=(x,y,s=1)=>`M${x},${F(y-60*s)} v${F(42*s)} `+CI(x,+F(y-4*s),+F(4*s));
const WIND=(x,y,s=1)=>`M${x},${y} h${F(-60*s)} q${F(-20*s)},0 ${F(-20*s)},${F(-14*s)} q0,${F(-12*s)} ${F(12*s)},${F(-12*s)} M${x},${F(y+18*s)} h${F(-80*s)} M${x},${F(y+36*s)} h${F(-50*s)} q${F(-16*s)},0 ${F(-16*s)},${F(12*s)} `;
