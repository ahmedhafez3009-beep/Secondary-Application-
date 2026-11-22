/* ============ السبورة L4A: الدرس ٤ · الفصل ١ · المفتاح في رحلة: التحولات السياسية ============ */
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
function WR(x,y,sz,col,parts){parts.forEach((p,i)=>{const k=p[0],t=typeof k=='number'?k:Array.isArray(k)?at(k[0],k[1]):at(k),c=p[2]||col;if(i==0)W(t,x,y,p[1],sz,c);else WC(t,p[1],c,p[3])})}
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

/* ---------- إضافات L3A ---------- */
const SCH=(x,y,s=1)=>`M${F(x-40*s)},${y} V${F(y-50*s)} H${F(x+40*s)} V${y} Z M${F(x-8*s)},${y} v${F(-20*s)} h${F(16*s)} v${F(20*s)} M${F(x-28*s)},${F(y-38*s)} h${F(14*s)} v${F(12*s)} h${F(-14*s)} Z M${F(x+14*s)},${F(y-38*s)} h${F(14*s)} v${F(12*s)} h${F(-14*s)} Z M${x},${F(y-50*s)} v${F(-22*s)} h${F(-16*s)} v${F(10*s)} h${F(16*s)} `;
/* سلّم طالع لليمين: يبدأ من تحت الشمال (x,y) */
const STUP=(x,y,w,h,n)=>`M${x},${y} `+PT(n).map(()=>`h${w} v${-h} `).join('');
const TENT=(x,y,s=1)=>`M${F(x-28*s)},${y} L${x},${F(y-42*s)} L${F(x+28*s)},${y} Z M${x},${F(y-42*s)} v${F(-10*s)} M${x},${y} L${F(x-5*s)},${F(y-20*s)} `;
/* بوابة بعقد: x المنتصف، y القاعدة */
const ARCH=(x,y,w,h)=>`M${x-w/2-16},${y} V${y-h-18} H${x+w/2+16} V${y} M${x-w/2},${y} V${F(y-h*.55)} Q${x-w/2},${y-h} ${x},${y-h} Q${x+w/2},${y-h} ${x+w/2},${F(y-h*.55)} V${y} `;
const CROWN=(x,y,s=1)=>`M${F(x-60*s)},${y} L${F(x-72*s)},${F(y-62*s)} L${F(x-36*s)},${F(y-30*s)} L${x},${F(y-80*s)} L${F(x+36*s)},${F(y-30*s)} L${F(x+72*s)},${F(y-62*s)} L${F(x+60*s)},${y} Z `;
const CHR=(x,y,s=1)=>`M${x},${y} V${F(y-78*s)} M${x},${F(y-38*s)} H${F(x+46*s)} V${y} `;
const BULB=(x,y,s=1)=>CI(x,y,+F(14*s))+`M${F(x-6*s)},${F(y+15*s)} h${F(12*s)} M${F(x-4*s)},${F(y+21*s)} h${F(8*s)} `;
const IDC=(x,y,w,h)=>RR(x,y,w,h,8)+CI(+F(x+w-h*.36),+F(y+h*.4),+F(h*.16))+`M${F(x+w-h*.6)},${F(y+h*.82)} q${F(h*.24)},${F(-h*.3)} ${F(h*.48)},0 M${x+12},${F(y+h*.3)} h${F(w-h*.85-12)} M${x+12},${F(y+h*.52)} h${F(w-h*.85-12)} M${x+12},${F(y+h*.74)} h${F((w-h*.85-12)*.6)} `;
const NOTE=(x,y,w,h)=>RC(x,y,w,h)+`M${x+8},${F(y+h*.3)} h${w-16} M${x+8},${F(y+h*.55)} h${w-16} M${x+8},${F(y+h*.8)} h${F((w-16)*.6)} `;
const DESK=(x,y,w)=>`M${x},${y} h${w} M${x+12},${y} v40 M${x+w-12},${y} v40 `;
const STAMP=(x,y,s=1)=>`M${F(x-14*s)},${y} h${F(28*s)} M${F(x-10*s)},${y} v${F(-8*s)} h${F(20*s)} v${F(8*s)} M${x},${F(y-8*s)} v${F(-14*s)} `+CI(x,+F(y-28*s),+F(6*s));
const WAVY=(x1,y,x2,a=8)=>{const n=Math.max(2,Math.round(Math.abs(x2-x1)/40)),w=(x2-x1)/n;return `M${x1},${y} q${F(w/2)},${-a} ${F(w)},0 `+PT(n-1).map(()=>`t${F(w)},0 `).join('')};
const MIRR=(x,y,s=1)=>EL(x,y,+F(34*s),+F(46*s))+`M${x},${F(y+46*s)} v${F(18*s)} M${F(x-20*s)},${F(y+64*s)} h${F(40*s)} `;
const PHONE=(x,y,w,h)=>RR(x,y,w,h,12)+`M${x+w/2-10},${y+h-10} h20 `;
const COMP=(x,y,r)=>CI(x,y,r)+`M${x},${F(y-r*.7)} L${F(x+r*.25)},${y} L${x},${F(y+r*.7)} L${F(x-r*.25)},${y} Z `;
const CAL=(x,y,w,h)=>RC(x,y,w,h)+`M${x},${F(y+h*.28)} h${w} M${F(x+w*.25)},${y-8} v16 M${F(x+w*.75)},${y-8} v16 `;
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
function FIGT(o,x,y,h,col,name,sz){P(o,MAN(x,y,h),col,3,.6);const r=h*.15;P(o+.25,EL(x,+F(y+r*.2),+F(r*1.4),+F(r*.75)),col,3,.4,'#fff');P(o+.4,`M${F(x-r*.6)},${F(y+r*1.9)} q${F(r*.6)},${F(r*1.1)} ${F(r*1.2)},0`,col,3,.3);
 W(o+.3,x,y+h+20,'رسم تخيّلي',15,GR,'middle');if(name)W(o+.3,x,y+h+46,name,sz||20,col,'middle')}
const DAD=(o,x,y,sz,col)=>W(o,x,y,'ض',sz,col||G,'middle');
/* شخبطة حروف غريبة عامّة */
const SCR=(x,y,n,a=9)=>`M${x},${y} `+PT(n).map(i=>`l6,${i%2?a:-a} `).join('');

/* ---------- إضافات L4A ---------- */
const RED2='#C0392B',GLD='#D4A017',GRY='#7a8285',SHADE='#3a3f41';
/* طربوش فوق راس MAN(x,y,h) */
const FEZH=(x,y,h)=>{const r=h*.15;return `M${F(x-r*.95)},${F(y+r*.45)} L${F(x-r*.72)},${F(y-r*.9)} H${F(x+r*.72)} L${F(x+r*.95)},${F(y+r*.45)} Z `};
const TASS=(x,y,h)=>{const r=h*.15;return `M${x},${F(y-r*.9)} q${F(r*.9)},${F(r*.1)} ${F(r*1.05)},${F(r*1.2)} `};
/* عمامة كبيرة ودقن */
const TURB=(x,y,h,k=1.6)=>{const r=h*.15;return EL(x,+F(y-r*.15),+F(r*k),+F(r*.95))+`M${F(x-r*k*.8)},${F(y-r*.35)} q${F(r*k*.8)},${F(r*.5)} ${F(r*k*1.6)},0 `};
const BEARD=(x,y,h,L=1.6)=>{const r=h*.15;return `M${F(x-r*.9)},${F(y+r*1.25)} Q${F(x-r*.8)},${F(y+r*(2+L))} ${x},${F(y+r*(2.3+L))} Q${F(x+r*.8)},${F(y+r*(2+L))} ${F(x+r*.9)},${F(y+r*1.25)} `};
/* شخص حقيقي: رسم تخيّلي + اسم. kind: ma محمد علي، is إسماعيل، fz طربوش، tb عمامة */
function PERS(o,x,y,h,kind,col,name,sz,lab){const r=h*.15;P(o,MAN(x,y,h),col,3,.6);
 if(kind=='ma'){P(o+.2,TURB(x,y,h,1.75),col,3,.4,'#fff');P(o+.3,`M${F(x-r*1.5)},${F(y-r*.55)} q${F(r*1.5)},${F(r*.7)} ${F(r*3)},0 M${F(x-r*1.3)},${F(y+r*.15)} q${F(r*1.3)},${F(-r*.6)} ${F(r*2.6)},0 `,GRY,2,.3);P(o+.35,BEARD(x,y,h,1.7),GRY,2.5,.4,'#eef0f0');P(o+.45,`M${F(x-r*.4)},${F(y+r*2.2)} v${F(r*1.2)} M${F(x+r*.4)},${F(y+r*2.2)} v${F(r*1.2)} M${x},${F(y+r*2.4)} v${F(r*1.4)} `,GRY,1.5,.2)}
 else if(kind=='is'){P(o+.2,FEZH(x,y,h),RED2,3,.35,RED2);P(o+.3,TASS(x,y,h),N,2.5,.2);P(o+.35,BEARD(x,y,h,.5),N,2.5,.3,'#6b5a4a');
  P(o+.45,`M${F(x-h*.12)},${F(y+h*.4)} L${F(x+h*.1)},${F(y+h*.62)} `+CI(+F(x+h*.08),+F(y+h*.46),+F(h*.035))+CI(+F(x-h*.07),+F(y+h*.52),+F(h*.035)),YD,3,.3,Y)}
 else if(kind=='fz'){P(o+.2,FEZH(x,y,h),RED2,3,.35,RED2);P(o+.3,TASS(x,y,h),N,2.5,.2)}
 else if(kind=='tb'){P(o+.25,EL(x,+F(y+r*.2),+F(r*1.4),+F(r*.75)),col,3,.4,'#fff');P(o+.4,BEARD(x,y,h,.9),col,2.5,.3)}
 if(lab!==false)W(o+.3,x,y+h+20,'رسم تخيّلي',15,GR,'middle');if(name)W(o+.3,x,y+h+46,name,sz||20,col,'middle')}
/* عالِم/راجل عام بعمامة من غير تسمية */
const TBM=(o,x,y,h,col)=>{const r=h*.15;P(o,MAN(x,y,h),col,3,.5);P(o+.2,EL(x,+F(y+r*.2),+F(r*1.4),+F(r*.75)),col,3,.3,'#fff')};
/* كف: x,y مركز الكف — يرجع أطراف الصوابع (من الإبهام لليمين للخنصر للشمال) */
const FING=(x,y,s=1)=>[[-.95,-.35],[-.55,-1.25],[0,-1.45],[.55,-1.3],[1.0,-.75]].map(([a,b])=>[+F(x-a*100*s),+F(y+b*100*s)]);
function PALM(o,x,y,s,col,d){const t=FING(x,y,s);P(o,EL(x,y,+F(62*s),+F(48*s)),N,4,.5,SKIN);P(o+(d||.3),t.map((q,i)=>`M${F(x+(q[0]-x)*.35)},${F(y+(q[1]-y)*.3)} L${q[0]},${q[1]}`).join(' '),N,+F(14*s),.7);return t}
/* مركب شراعي صغير بطلبة */
const BOATS=(x,y,s=1)=>SAIL(x,y,s)+CI(+F(x-12*s),+F(y-6*s),+F(4*s))+CI(+F(x+12*s),+F(y-6*s),+F(4*s));
/* لوحة نيشان */
const TGT=(x,y,r)=>CI(x,y,r)+CI(x,y,+F(r*.66))+CI(x,y,+F(r*.33));
/* سهم مزروع: من (x1,y1) لحد (x2,y2) بريشة */
const DART=(x1,y1,x2,y2)=>{const a=Math.atan2(y2-y1,x2-x1),q=(px,py,d,k)=>F(px-d*Math.cos(a+k))+','+F(py-d*Math.sin(a+k));return `M${x1},${y1} L${x2},${y2} M${x2},${y2} L${q(x2,y2,16,.45)} M${x2},${y2} L${q(x2,y2,16,-.45)} M${x1},${y1} L${q(x1,y1,14,.7)} M${x1},${y1} L${q(x1,y1,14,-.7)} M${q(x1,y1,-10,0)} L${q(x1,y1,4,.7)} M${q(x1,y1,-10,0)} L${q(x1,y1,4,-.7)} `};
/* سيفين متقاطعين */
const XSW=(x,y,s=1)=>`M${F(x-40*s)},${F(y+40*s)} L${F(x+36*s)},${F(y-36*s)} M${F(x+40*s)},${F(y+40*s)} L${F(x-36*s)},${F(y-36*s)} M${F(x-36*s)},${F(y+22*s)} l${F(16*s)},${F(16*s)} M${F(x+36*s)},${F(y+22*s)} l${F(-16*s)},${F(16*s)} `;
/* مرجيحة توازن: x المنتصف، y الأرض، t الميل */
const SEESAW=(x,y,w,t)=>({base:`M${x-26},${y} L${x},${y-40} L${x+26},${y} Z`,plank:`M${x-w},${y-40-t} L${x+w},${y-40+t}`,L:[x-w,y-40-t],R:[x+w,y-40+t]});
/* فرمان ملفوف بختم */
const FIRM=(x,y,w,h)=>SCROLL(x,y,w,h)+`M${x+14},${y+h*.3} h${w-28} M${x+14},${y+h*.55} h${w-28} M${x+14},${y+h*.8} h${F((w-28)*.5)} `;
/* شجرة عيلة صغيرة: x,y الأب — يرجع {d, kids:[...]} الابن الأكبر أول واحد يمين */
const FTREE=(x,y,s=1)=>{const k=[-60,-20,20,60].map(a=>[+F(x-a*s),+F(y+70*s)]);return {d:CI(x,y,+F(14*s))+`M${x},${F(y+14*s)} v${F(24*s)} M${k[0][0]},${F(y+38*s)} H${k[3][0]} `+k.map(q=>`M${q[0]},${F(y+38*s)} V${F(q[1]-10*s)} `).join(''),kids:k}};
/* عملة */
const COIN=(x,y,r)=>CI(x,y,r)+CI(x,y,+F(r*.78));
/* سقالة مبنى */
const SCAF=(x,y,w,h)=>RC(x,y,w,h)+`M${x},${F(y+h/3)} h${w} M${x},${F(y+2*h/3)} h${w} M${F(x+w/2)},${y} v${h} M${x},${y+h} L${x+w},${y} `;
/* قناة بين بحرين */
const CANAL=(x,y,w,h)=>`M${x},${y} V${y+h} M${x+w},${y} V${y+h} `;
/* محفظة */
const WAL=(x,y,w,h)=>RR(x,y,w,h,10)+`M${x},${F(y+h*.35)} H${F(x+w*.6)} q12,0 12,12 v${F(h*.2)} q0,12 -12,12 H${x+w} `;
/* ميكروفون */
const MIC=(x,y,s=1)=>RR(+F(x-12*s),+F(y-40*s),+F(24*s),+F(40*s),+F(12*s))+`M${F(x-20*s)},${F(y-14*s)} q0,${F(26*s)} ${F(20*s)},${F(26*s)} q${F(20*s)},0 ${F(20*s)},${F(-26*s)} M${x},${F(y+12*s)} v${F(30*s)} M${F(x-16*s)},${F(y+42*s)} h${F(32*s)} `;
const SPK=(x,y,s=1)=>`M${x},${F(y-8*s)} h${F(10*s)} l${F(12*s)},${F(-10*s)} v${F(36*s)} l${F(-12*s)},${F(-10*s)} h${F(-10*s)} Z M${F(x+30*s)},${F(y-4*s)} q${F(8*s)},${F(9*s)} 0,${F(18*s)} `;
/* خوذة عسكري (أيقونة) */
const HELM=(x,y,s=1)=>`M${F(x-24*s)},${y} a${F(24*s)},${F(22*s)} 0 0,1 ${F(48*s)},0 Z M${F(x-30*s)},${y} h${F(60*s)} `+CI(x,+F(y+18*s),+F(12*s));
/* سماعة ودن متلخبطة */
const BUDS=(x,y,s=1)=>EL(+F(x-60*s),+F(y-40*s),+F(14*s),+F(18*s))+EL(+F(x+60*s),+F(y-40*s),+F(14*s),+F(18*s));
const TANG=(x,y,s=1)=>`M${F(x-60*s)},${F(y-22*s)} C${F(x-60*s)},${F(y+60*s)} ${F(x+50*s)},${F(y-20*s)} ${F(x+10*s)},${F(y+40*s)} S${F(x-50*s)},${F(y+20*s)} ${F(x-10*s)},${F(y+70*s)} S${F(x+60*s)},${F(y+30*s)} ${F(x+60*s)},${F(y-22*s)} M${F(x-10*s)},${F(y+70*s)} v${F(30*s)} `;
/* ملعب */
const FIELD=(x,y,w,h)=>RC(x,y,w,h)+`M${F(x+w/2)},${y} v${h} `+CI(+F(x+w/2),+F(y+h/2),+F(h*.18))+RC(x,+F(y+h*.3),+F(w*.1),+F(h*.4))+RC(+F(x+w*.9),+F(y+h*.3),+F(w*.1),+F(h*.4));
/* عين مقفولة / مفتوحة */
const EYEC=(x,y,s=1)=>`M${F(x-22*s)},${y} q${F(22*s)},${F(12*s)} ${F(44*s)},0 M${F(x-12*s)},${F(y+8*s)} l-4,8 M${x},${F(y+10*s)} v9 M${F(x+12*s)},${F(y+8*s)} l4,8 `;
/* عدّاد بإبرة: x,y مركز القاعدة، r — والإبرة بزاوية a (0 = شمال/تحت، 180 = يمين/فوق) */
const GAUGE=(x,y,r)=>`M${x-r},${y} a${r},${r} 0 0,1 ${2*r},0 Z `+[30,60,90,120,150].map(a=>{const t=a*Math.PI/180;return `M${F(x-r*Math.cos(t))},${F(y-r*Math.sin(t))} L${F(x-r*.85*Math.cos(t))},${F(y-r*.85*Math.sin(t))} `}).join('');
const NEED=(x,y,r,a)=>{const t=a*Math.PI/180;return `M${x},${y} L${F(x-r*.8*Math.cos(t))},${F(y-r*.8*Math.sin(t))} `+CI(x,y,6)};
/* ختم دايري (أختام الدرس ٢) */
const SEAL=(x,y,r)=>CI(x,y,r)+CI(x,y,+F(r*.8));
/* موبايل بزراير */
const OLDPH=(x,y,w,h)=>RR(x,y,w,h,10)+RC(x+10,y+12,w-20,F(h*.32))+PT(3).map(i=>PT(3).map(j=>CI(+F(x+w*(.27+j*.23)),+F(y+h*(.58+i*.13)),4)).join('')).join('');
/* ريح */
const WIND=(x,y,s=1)=>`M${x},${y} h${F(-60*s)} q${F(-20*s)},0 ${F(-20*s)},${F(-14*s)} q0,${F(-12*s)} ${F(12*s)},${F(-12*s)} M${x},${F(y+18*s)} h${F(-80*s)} M${x},${F(y+36*s)} h${F(-50*s)} q${F(-16*s)},0 ${F(-16*s)},${F(12*s)} `;
/* إيد بتشدّ (قبضة صغيرة) */
const GRAB=(x,y,s=1)=>RR(+F(x-14*s),+F(y-12*s),+F(28*s),+F(24*s),+F(8*s))+`M${F(x-6*s)},${F(y-12*s)} v${F(24*s)} M${F(x+3*s)},${F(y-12*s)} v${F(24*s)} `;
/* كرسي حكم كبير */
const THRONE=(x,y,s=1)=>`M${F(x-40*s)},${y} V${F(y-120*s)} q${F(40*s)},${F(-30*s)} ${F(80*s)},0 V${y} M${F(x-52*s)},${F(y-50*s)} h${F(104*s)} M${F(x-52*s)},${F(y-50*s)} v${F(-30*s)} M${F(x+52*s)},${F(y-50*s)} v${F(-30*s)} `;
/* عَلامة تعجب */
const EXC=(x,y,s=1)=>`M${x},${F(y-60*s)} v${F(42*s)} `+CI(x,+F(y-4*s),+F(4*s));
/* كتاب مقفول */
const CBK=(x,y,w,h)=>RC(x,y,w,h)+`M${x+8},${y} v${h} `;
