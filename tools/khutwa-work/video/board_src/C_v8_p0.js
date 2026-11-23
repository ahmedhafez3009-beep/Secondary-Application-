/* ============ السبورة C: الفصل الثالث · مقومات الدولة المصرية (C1–C4) + دقيقة المراجعة ============ */
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
const L=(id,fn)=>line(id,SRC[id]!=null?SRC[id]:(id[0]=='R'?'مراجعة':'رابط حفظ'),S[id],fn);
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
/* v8: إخفاء كل اللي اترسم من a لآخر السطر (إضاءة مؤقتة) */
const OFFEOL=a=>{for(let i=a;i<IT.length;i++)IT[i].off=T0+LD};
