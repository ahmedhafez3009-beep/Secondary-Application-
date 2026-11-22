# يجمع كل سبورات منهج التاريخ (تانية بكالوريا) في ملف HTML واحد: وحدة ← درس ← سبورة
import json,os,re
D='/home/claude/out'
READY={
 1:[('A','الافتتاحية + يعني إيه دولة؟ ومين شعبها؟'),('A45','فين حدودها؟ + ملخص الفصل ١'),('B','الفصل ٢: السلطة والسيادة'),('C','الفصل ٣: ليه مصر قامت واستمرت؟'),('D','الفصل ٤: ركن الامتحان والختام')],
 2:[('L2A','الفصل ١: ليه كانت عينهم على مصر؟ والهكسوس'),('L2B','الفصل ٢: الفرس والإسكندر والبطالمة'),('L2C','الفصل ٣: الرومان والمقاومة والختام')],
 3:[('L3A','الفصل ١: من ولاية لمركز قيادي'),('L3B','الفصل ٢: العلماء والعلم والعواصم'),('L3C','الفصل ٣: الاقتصاد والمكانة والختام')],
 4:[('L4A','الفصل ١: التحولات السياسية — المفتاح في رحلة'),('L4B','الفصل ٢: الاقتصاد والمجتمع'),('L4C','الفصل ٣: الأفكار والمكانة + لمّة الوحدة والختام')],
 5:[('L5A','الفصل ١: افتتاحية الوحدة ٢ + الحملة الفرنسية ومحمد علي'),('L5B','الفصل ٢: التدخل الأوروبي والاحتلال البريطاني'),('L5C','الفصل ٣: سياسات الاحتلال + التدريبات والختام')],
}
cur=open(os.path.dirname(os.path.abspath(__file__))+'/hist_curriculum.md',encoding='utf8').read()
units=[];n=0
for l in cur.splitlines():
    m=re.match(r'- (الوحدة \d+): (.*)',l)
    if m: units.append({'name':m.group(1),'title':m.group(2),'lessons':[]});continue
    m=re.match(r'\s+- (.*)',l)
    if m:
        n+=1;bs=[]
        for k,t in READY.get(n,[]):
            f=f'{D}/khutwa_hist_board_{k}.html'
            if os.path.exists(f): bs.append({'k':k,'title':t})
        units[-1]['lessons'].append({'n':n,'title':m.group(1),'boards':bs})
data={}
for u in units:
    for L in u['lessons']:
        for b in L['boards']: data[b['k']]=open(f"{D}/khutwa_hist_board_{b['k']}.html",encoding='utf8').read()
html='''<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>خُطوة · تاريخ تانية بكالوريا · المنهج كله</title>
<style>
*{box-sizing:border-box}html,body{margin:0;height:100%;background:#0b1620;color:#e8eef0;font-family:Cairo,Tahoma,"Segoe UI",sans-serif}
body{display:flex;flex-direction:column}
header{display:flex;gap:8px;align-items:center;flex-wrap:wrap;padding:8px 10px;background:#0E2A47;border-bottom:1px solid #2a3945}
header b{color:#F5BE32;font-size:15px;white-space:nowrap}
#menuBtn{font:inherit;font-size:14px;cursor:pointer;border-radius:8px;border:1px solid #1EA05F;background:#1EA05F;color:#fff;padding:6px 12px}
#cur{font-size:13px;color:#cfe;flex:1;min-width:150px}
nav#boards{display:flex;gap:6px;flex-wrap:wrap;width:100%}
nav#boards button{font:inherit;font-size:13px;cursor:pointer;border-radius:8px;border:1px solid #2a3945;background:#16212c;color:#e8eef0;padding:6px 10px;text-align:right;line-height:1.3}
nav#boards button[aria-selected=true]{background:#1EA05F;border-color:#1EA05F}
main{flex:1;min-height:0;position:relative}
iframe{position:absolute;inset:0;width:100%;height:100%;border:0;background:#0b1620}iframe[hidden]{display:none}
#drawer{position:fixed;inset:0;background:rgba(0,0,0,.55);display:none;z-index:9}
#drawer.open{display:block}
#panel{position:absolute;top:0;bottom:0;right:0;width:min(420px,92vw);background:#0f1d29;overflow:auto;padding:12px;border-left:1px solid #2a3945}
#panel h2{margin:4px 0 10px;font-size:17px;color:#F5BE32}
.unit{margin:12px 0 4px;font-size:14px;color:#9fd8b8}
.unit small{display:block;color:#9aa9ad;font-size:12px}
.les{display:block;width:100%;text-align:right;font:inherit;font-size:14px;margin:4px 0;padding:8px 10px;border-radius:8px;border:1px solid #2a3945;background:#16212c;color:#e8eef0;cursor:pointer}
.les small{color:#9aa9ad;font-size:11px;display:block}
.les.on{border-color:#1EA05F;background:#143524}
.les:disabled{opacity:.4;cursor:not-allowed}
#home{position:absolute;inset:0;overflow:auto;padding:24px 16px;text-align:center}
#home h1{color:#F5BE32;font-size:24px;margin:8px 0}#home p{color:#cfe;max-width:560px;margin:8px auto;line-height:1.8}
#home .go{font:inherit;font-size:16px;margin:10px 6px;padding:10px 18px;border-radius:10px;border:0;background:#1EA05F;color:#fff;cursor:pointer}
</style></head><body>
<header><button id="menuBtn">☰ المنهج</button><b>خُطوة · تاريخ تانية بكالوريا</b><span id="cur"></span><nav id="boards"></nav></header>
<main id="main"><div id="home"></div></main>
<div id="drawer"><div id="panel"><h2>المنهج — أحمد الألفي · خُطوة من Add Value</h2><div id="list"></div></div></div>
<script id="units" type="application/json">__UNITS__</script>
<script id="data" type="application/json">__DATA__</script>
<script>
const U=JSON.parse(document.getElementById('units').textContent),B=JSON.parse(document.getElementById('data').textContent),F={};
const $=id=>document.getElementById(id),main=$('main'),drawer=$('drawer');
const LES=[];U.forEach(u=>u.lessons.forEach(l=>{l.unit=u;LES.push(l)}));
const ready=LES.filter(l=>l.boards.length);
let curL=null,curB=null;
function pauseAll(ex){for(const x in F)if(x!=ex){F[x].hidden=true;try{const p=F[x].contentWindow.document.getElementById('play');if(p&&p.textContent.startsWith('⏸'))p.click()}catch(e){}}}
function showBoard(k){curB=k;pauseAll(k);$('home').hidden=true;
 if(!F[k]){const f=document.createElement('iframe');f.setAttribute('allow','fullscreen; clipboard-write; autoplay');f.setAttribute('allowfullscreen','');f.title=k;f.srcdoc=B[k];main.appendChild(f);F[k]=f}
 F[k].hidden=false;document.querySelectorAll('#boards button').forEach(b=>b.setAttribute('aria-selected',b.dataset.k==k));
 try{localStorage.setItem('kh_all',JSON.stringify({l:curL.n,b:k}))}catch(e){}}
function openLesson(l,k){curL=l;$('cur').textContent=l.unit.name+' · الدرس '+l.n+': '+l.title;
 const nb=$('boards');nb.innerHTML='';l.boards.forEach((b,i)=>{const e=document.createElement('button');e.dataset.k=b.k;e.textContent=(i+1)+' · '+b.title;e.onclick=()=>showBoard(b.k);nb.appendChild(e)});
 drawer.classList.remove('open');renderList();showBoard(k&&l.boards.some(b=>b.k==k)?k:l.boards[0].k)}
function renderList(){const L=$('list');L.innerHTML='';U.forEach(u=>{const h=document.createElement('div');h.className='unit';h.innerHTML=u.name+'<small>'+u.title+'</small>';L.appendChild(h);
 u.lessons.forEach(l=>{const b=document.createElement('button');b.className='les'+(curL===l?' on':'');b.disabled=!l.boards.length;
  b.innerHTML='الدرس '+l.n+': '+l.title+'<small>'+(l.boards.length?l.boards.length+' سبورات':'لسه بيتجهّز')+'</small>';b.onclick=()=>openLesson(l);L.appendChild(b)})})}
$('menuBtn').onclick=()=>{renderList();drawer.classList.add('open')};drawer.onclick=e=>{if(e.target===drawer)drawer.classList.remove('open')};
$('home').innerHTML='<h1>تاريخ تانية بكالوريا · خُطوة</h1><p>المنهج كله في مكان واحد: '+U.length+' وحدات و'+LES.length+' درس. الجاهز دلوقتي '+ready.length+' دروس. افتح «المنهج» واختار الدرس، وكل درس مقسوم سبورات.</p>'+ready.map(l=>'<button class="go" data-n="'+l.n+'">الدرس '+l.n+': '+l.title+'</button>').join('');
$('home').querySelectorAll('.go').forEach(b=>b.onclick=()=>openLesson(LES.find(l=>l.n==b.dataset.n)));
let st=null;try{st=JSON.parse(localStorage.getItem('kh_all'))}catch(e){}
const sl=st&&ready.find(l=>l.n==st.l);if(sl)openLesson(sl,st.b);else renderList();
</script></body></html>'''
esc=lambda o:json.dumps(o,ensure_ascii=False).replace('</','<\\/')
out=html.replace('__UNITS__',esc(units)).replace('__DATA__',esc(data))
open(f'{D}/khutwa_hist_all.html','w',encoding='utf8').write(out)
print('boards',list(data),'size',len(out.encode())//1024,'KB')
