/* ============ السبورة L2A: الدرس ٢ · الفصل ١ · ليه كانت عينهم على مصر؟ والهكسوس (ص٢١–٢٤) + كروت الحفظ + دقيقة المراجعة RA ============ */
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
const SLD={'2A.1':'L2A.1 · إنت هنا والمفتاح','2A.3':'L2A.2 · بيت على ميدان — اسمه مصر','2A.5':'L2A.3 · سلاح ذو حدين وأهداف الدرس','2A.8':'L2A.4 · الفكرة الرئيسة (احفظ دي ١)','2A.10':'L2A.5 · أولًا: دوافع احتلال مصر','2A.12':'L2A.6 · الاحتلال (احفظ دي ٢)','2A.14':'L2A.7 · مثال الجار والحديقة','2A.17':'L2A.8 · التنافس الدولي (احفظ دي ٢)','2A.19':'L2A.9 · الأمن القومي (احفظ دي ٢)','2A.21':'L2A.10 · الدوافع الستة (احفظ دي ٣)','2A.26':'L2A.11 · أربع أختام على مصر','2A.27':'L2A.12 · ثانيًا: غزو الهكسوس','2A.30':'L2A.13 · قيمة وعجلة حربية','2A.32':'L2A.14 · ليه نجح الهكسوس (احفظ دي ٤)','2A.35':'L2A.15 · الدلتا وأواريس','2A.37':'L2A.16 · المقاومة من الجنوب','2A.38':'L2A.17 · لوحة كامس (احفظ دي ٥)','2A.40':'L2A.18 · مراحل الطرد (احفظ دي ٦)','2A.45':'L2A.19 · كامس: ليه شمالًا (احفظ دي ٧)','2A.48':'L2A.20 · مهارة التخطيط','2A.49':'L2A.21 · هل كامس مهندس النصر؟','2A.51':'L2A.22 · أحمس: الحسم والنصر','2A.52':'L2A.23 · أحمس: التلات أفعال (احفظ دي ٨)','2A.54':'L2A.24 · الملكة إياح حتب (احفظ دي ٩)','2A.56':'L2A.25 · الدرس المستفاد والعجلة (احفظ دي ١٠)','2A.58':'L2A.26 · الفصل الجاي: الفرس','RA1':'RA.1 · دقيقة المراجعة','RA5':'RA.2 · دقيقة المراجعة (كمّل)'};
const L=(id,fn)=>{if(SLD[id])slide(SLD[id]);return line(id,SRC[id]!=null?SRC[id]:(id[0]=='R'?'مراجعة':'رابط حفظ'),S[id],fn)};
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
/* ---------- إضافات L2A ---------- */
const GHO='#9aa3a8',LRD='#FBE3E0',LYL='#FFF4CC';
const RT=(x,y,a)=>(px,py)=>[Math.round(x+px*Math.cos(a)-py*Math.sin(a)),Math.round(y+px*Math.sin(a)+py*Math.cos(a))].join(',');
/* سيف: نقطة المقبض x,y، الطول، الزاوية بالدرجات (سالب = لفوق)، side: +1 حد، -1 حد، 0 كامل */
const SWB=(x,y,len,deg,side)=>{const r=RT(x,y,deg*Math.PI/180);const e=side>0?[[0,14],[len*.86,16],[len,0]]:[[0,-14],[len*.86,-16],[len,0]];return 'M'+r(...e[0])+' L'+r(...e[1])+' L'+r(...e[2])+' '};
const SWH=(x,y,len,deg)=>{const r=RT(x,y,deg*Math.PI/180);return 'M'+r(0,0)+' L'+r(len,0)+' M'+r(0,-24)+' L'+r(0,24)+' M'+r(0,0)+' L'+r(-34,0)+' '+CI(...r(-42,0).split(',').map(Number),8)};
const EYE=(x,y,s=1)=>`M${F(x-22*s)},${y} Q${x},${F(y-20*s)} ${F(x+22*s)},${y} Q${x},${F(y+20*s)} ${F(x-22*s)},${y} Z `+CI(x,y,6*s);
const LOCK=(x,y,s=1)=>RC(F(x-14*s),y,28*s,22*s)+`M${F(x-9*s)},${y} v${F(-10*s)} a${F(9*s)},${F(9*s)} 0 0,1 ${F(18*s)},0 v${F(10*s)} `;
const BAG=(x,y,s=1)=>`M${F(x-15*s)},${y} q${F(-13*s)},${F(20*s)} 0,${F(32*s)} h${F(30*s)} q${F(13*s)},${F(-12*s)} 0,${F(-32*s)} Z M${F(x-9*s)},${y} l${F(-4*s)},${F(-11*s)} h${F(26*s)} l${F(-4*s)},${F(11*s)} `+CI(x,F(y+16*s),6*s);
const WHEEL=(x,y,r)=>CI(x,y,r)+CI(x,y,r*.2)+[0,1,2,3,4,5].map(i=>{const a=i*Math.PI/3;return `M${F(x+r*.2*Math.cos(a))},${F(y+r*.2*Math.sin(a))} L${F(x+r*Math.cos(a))},${F(y+r*Math.sin(a))} `}).join('');
const TORCH=(x,y,s=1)=>`M${x},${y} v${F(-48*s)} M${F(x-10*s)},${F(y-48*s)} l${F(-4*s)},${F(-14*s)} h${F(28*s)} l${F(-4*s)},${F(14*s)} Z `;
const FLAME=(x,y,s=1)=>`M${x},${y} q${F(-17*s)},${F(-16*s)} 0,${F(-38*s)} q${F(17*s)},${F(22*s)} 0,${F(38*s)} Z `;
const SCIS=(x,y,s=1)=>`M${F(x-26*s)},${F(y-26*s)} L${F(x+28*s)},${F(y+28*s)} M${F(x-26*s)},${F(y+26*s)} L${F(x+28*s)},${F(y-28*s)} `+CI(F(x-32*s),F(y-32*s),7*s)+CI(F(x-32*s),F(y+32*s),7*s);
const GATE=(x,y,s=1)=>`M${x},${y} v${F(-70*s)} h${F(54*s)} v${F(70*s)} M${F(x+54*s)},${F(y-70*s)} l${F(26*s)},${F(8*s)} v${F(70*s)} l${F(-26*s)},${F(-8*s)} `;
const BOLT=(x,y,s=1)=>RC(x,y,F(64*s),F(12*s))+`M${F(x+64*s)},${F(y+6*s)} h${F(18*s)} v${F(-9*s)} `;
const SILO=(x,y,s=1)=>`M${F(x-24*s)},${y} v${F(-58*s)} q${F(24*s)},${F(-28*s)} ${F(48*s)},0 v${F(58*s)} Z M${F(x-24*s)},${F(y-30*s)} h${F(48*s)} `;
const SCALE=(x,y,s=1)=>`M${x},${y} V${F(y-74*s)} M${F(x-42*s)},${F(y-74*s)} h${F(84*s)} M${F(x-42*s)},${F(y-74*s)} l${F(-17*s)},${F(36*s)} h${F(34*s)} Z M${F(x+42*s)},${F(y-74*s)} l${F(-17*s)},${F(36*s)} h${F(34*s)} Z M${F(x-20*s)},${y} h${F(40*s)} `;
const PHONE=(x,y,s=1)=>RC(x,y,F(40*s),F(70*s))+CI(F(x+20*s),F(y+60*s),4*s)+`M${F(x+12*s)},${F(y+8*s)} h${F(16*s)} `;
const GRAB=(x,y,s=1)=>`M${F(x-100*s)},${y} h${F(86*s)} `+CI(x,y,14*s)+`M${F(x+14*s)},${F(y-8*s)} l${F(17*s)},${F(-7*s)} M${F(x+14*s)},${y} l${F(20*s)},0 M${F(x+14*s)},${F(y+8*s)} l${F(17*s)},${F(7*s)} `;
const CHAR=(x,y,s=1)=>WHEEL(F(x+18*s),F(y+34*s),20*s)+`M${F(x-14*s)},${F(y+2*s)} h${F(62*s)} v${F(-34*s)} h${F(-48*s)} Z M${F(x+48*s)},${F(y-14*s)} h${F(26*s)} `;
const CRK=(x,y1,y2)=>`M${x},${y1} l7,${F((y2-y1)*.25)} l-12,${F((y2-y1)*.25)} l12,${F((y2-y1)*.25)} l-7,${F((y2-y1)*.25)} `;
const WCARD=(x,y,w,h)=>RC(x,y,w,h);
/* بيت الدرس 1: سقف + 4 أعمدة (الأول من اليمين = شعب). يرجّع إحداثيات الأعمدة */
const BHX=(cx,s)=>[cx+75*s,cx+25*s,cx-25*s,cx-75*s].map(Math.round);
function BH(o,cx,by,s=1,col){const c=col||BRN;P(o,`M${F(cx-118*s)},${F(by-100*s)} L${F(cx)},${F(by-166*s)} L${F(cx+118*s)},${F(by-100*s)} Z`,c,3,.5,SAND);
 P(o+.15,BHX(cx,s).map(x=>`M${x},${F(by-100*s)} V${by}`).join(' '),c,4,.6);P(o+.3,`M${F(cx-110*s)},${by} H${F(cx+110*s)}`,N,4,.4)}
/* رسم تخيّلي لشخص: o توقيت، x منتصف، y أعلى الراس، h الطول */
function ROYAL(o,x,y,h,name,tail,col){const r=h*.15;P(o,MAN(x,y,h)+`M${F(x-r*1.35)},${F(y+r*1.8)} L${F(x-r*1.15)},${F(y+r*.1)} Q${x},${F(y-r*.7)} ${F(x+r*1.15)},${F(y+r*.1)} L${F(x+r*1.35)},${F(y+r*1.8)} `,col||N,3,.7);
 W(o+.25,x,y+h+24,name,19,col||N,'middle');W(o+.45,x,y+h+44,'رسم تخيّلي',14,GR,'middle')}
/* تقسيم نص على كلمات منطوقة: parts = [[مفتاح,نص,(n),(لون)],...] — أول جزء W والباقي WC */
function WR(x,y,sz,col,parts,anc){parts.forEach((p,i)=>{const t=at(p[0],p[2]||0),c=p[3]||col;if(i==0)W(t,x,y,p[1],sz,c,anc);else WC(t,p[1],c,sz*.28+14)})}
/* بطاقة «احفظ دي» */
const MEMT=(o,x,y,id,title)=>{W(o,x,y,'احفظ دي '+id+' · '+title,22,G);chime(o)};
/* مسار نيل بسيط بين نقطتين (متعرّج) */
const RIV=(x,y1,y2)=>{let d=`M${x},${y1} `;const n=Math.round(Math.abs(y2-y1)/60);for(let i=0;i<n;i++)d+=`q${i%2?-18:18},${(y2-y1)/n/2} 0,${(y2-y1)/n} `;return d};
const HEART=(x,y,s=1)=>`M${x},${F(y+12*s)} C${F(x-34*s)},${F(y-16*s)} ${F(x-20*s)},${F(y-40*s)} ${x},${F(y-18*s)} C${F(x+20*s)},${F(y-40*s)} ${F(x+34*s)},${F(y-16*s)} ${x},${F(y+12*s)} Z `;
