# يجمع كل سبورات الدرس في ملف HTML واحد (كل سبورة في تاب، بكامل أدوات التسجيل والظبط)
import json,os,re,sys
D='/home/claude/out'
BOARDS=[('A','الافتتاحية + يعني إيه دولة؟ ومين شعبها؟','A0–A3'),('A45','فين حدودها؟ + ملخص الفصل ١','A4–A5'),('B','الفصل ٢: السلطة والسيادة','B1–B6'),('C','الفصل ٣: ليه مصر قامت واستمرت؟','C1–C4'),('D','الفصل ٤: ركن الامتحان والختام','D1–D7')]
only=sys.argv[1:]  # اختياري: أسماء السبورات الجاهزة فقط
tabs=[];data={}
for k,title,rng in BOARDS:
    f=f'{D}/khutwa_hist_board_{k}.html'
    ok=os.path.exists(f) and (not only or k in only)
    tabs.append({'k':k,'title':title,'rng':rng,'ready':ok})
    if ok: data[k]=open(f,encoding='utf8').read()
html='''<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>خُطوة · تاريخ تانية بكالوريا · و1 د1 · كل السبورات</title>
<style>
*{box-sizing:border-box}html,body{margin:0;height:100%;background:#0b1620;color:#e8eef0;font-family:Cairo,Tahoma,"Segoe UI",sans-serif}
body{display:flex;flex-direction:column}
header{display:flex;gap:8px;align-items:center;flex-wrap:wrap;padding:8px 10px;background:#0E2A47;border-bottom:1px solid #2a3945}
header b{color:#F5BE32;font-size:15px;margin-inline-end:6px;white-space:nowrap}
nav{display:flex;gap:6px;flex-wrap:wrap}
nav button{font:inherit;font-size:13px;cursor:pointer;border-radius:8px;border:1px solid #2a3945;background:#16212c;color:#e8eef0;padding:6px 10px;text-align:right;line-height:1.3}
nav button small{display:block;color:#9aa9ad;font-size:11px}
nav button[aria-selected=true]{background:#1EA05F;border-color:#1EA05F}nav button[aria-selected=true] small{color:#eafff3}
nav button:disabled{opacity:.45;cursor:not-allowed}
main{flex:1;min-height:0;position:relative}
iframe{position:absolute;inset:0;width:100%;height:100%;border:0;background:#0b1620}iframe[hidden]{display:none}
</style></head><body>
<header><b>خُطوة · بناء الدولة المصرية واستمرارها عبر التاريخ</b><nav id="nav"></nav></header>
<main id="main"></main>
<script id="tabs" type="application/json">__TABS__</script>
<script id="boards" type="application/json">__DATA__</script>
<script>
const TABS=JSON.parse(document.getElementById('tabs').textContent),B=JSON.parse(document.getElementById('boards').textContent),F={},nav=document.getElementById('nav'),main=document.getElementById('main');
function show(k){for(const t of TABS){const b=document.getElementById('t_'+t.k);b.setAttribute('aria-selected',t.k==k)}
 for(const x in F){if(x!=k){F[x].hidden=true;try{F[x].contentWindow.document.getElementById('play').textContent.startsWith('⏸')&&F[x].contentWindow.document.getElementById('play').click()}catch(e){}}}
 if(!F[k]){const f=document.createElement('iframe');f.setAttribute('allow','fullscreen; clipboard-write; autoplay');f.setAttribute('allowfullscreen','');f.title=k;f.srcdoc=B[k];main.appendChild(f);F[k]=f}
 F[k].hidden=false;try{localStorage.setItem('kh_board',k)}catch(e){}}
TABS.forEach((t,i)=>{const b=document.createElement('button');b.id='t_'+t.k;b.innerHTML=(i+1)+' · '+t.title+'<small>'+t.rng+(t.ready?'':' · لسه بتترسم')+'</small>';b.disabled=!t.ready;b.onclick=()=>show(t.k);nav.appendChild(b)});
let st=null;try{st=localStorage.getItem('kh_board')}catch(e){}
show(TABS.find(t=>t.ready&&t.k==st)?st:TABS.find(t=>t.ready).k);
</script></body></html>'''
esc=lambda o:json.dumps(o,ensure_ascii=False).replace('</','<\\/')
out=html.replace('__TABS__',esc(tabs)).replace('__DATA__',esc(data))
open(f'{D}/khutwa_hist_lesson1_all.html','w',encoding='utf8').write(out)
print('boards in file:',[t['k'] for t in tabs if t['ready']],'size',len(out.encode())//1024,'KB')
