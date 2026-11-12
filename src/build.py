import os, json, shutil, re, zipfile
OUT='site';
import pathlib
GC=(pathlib.Path('gc.txt').read_text().strip() if pathlib.Path('gc.txt').exists() else '')
assert GC=='' or __import__('re').fullmatch(r'[a-z0-9-]{2,40}',GC)
shutil.rmtree(OUT,ignore_errors=True); os.makedirs(OUT+'/app')
VER='kw-v2'
t=open('app.html',encoding='utf-8').read()
q=open('quotes.js',encoding='utf-8').read().replace('["كلمة","فخورين بيكي يا {N} 💜","أحمد"]','["كلمة","فخورين بيكي يا {N} 💜","خُطوة"]')
html=t.replace('/*DATA*/',open('data.js',encoding='utf-8').read().replace('__GC__',GC)).replace('/*QUOTES*/',q).replace('__TITLE__','خُطوة')
head_add='''<meta http-equiv="Content-Security-Policy" content="default-src 'none'; script-src 'self' 'unsafe-inline'; style-src 'unsafe-inline'; img-src 'self' data: blob:; manifest-src 'self'; connect-src 'self'__GCCSP__; worker-src 'self'; base-uri 'none'; form-action 'none'; object-src 'none'">
<meta name="referrer" content="no-referrer">
<meta name="description" content="خُطوة: نسبة المذاكرة من المنهج والحضور لطلاب الثانوي. Created by Add Value.">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" type="image/png" href="icon-192.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="خُطوة">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
'''
head_add=head_add.replace('__GCCSP__',(' https://'+GC+'.goatcounter.com') if GC else '')
html=html.replace('<meta name="theme-color" content="#103B3C">','<meta name="theme-color" content="#103B3C">\n'+head_add,1)
inst='''<script>
(function(){
  if("serviceWorker" in navigator){ window.addEventListener("load",function(){ navigator.serviceWorker.register("sw.js").catch(function(){}); }); }
  var standalone = (window.matchMedia && window.matchMedia("(display-mode: standalone)").matches) || window.navigator.standalone === true;
  if(standalone) return;
  var ios = /iphone|ipad|ipod/i.test(navigator.userAgent), deferred = null;
  function card(html){ var n = document.getElementById("nudge"); if(!n || document.getElementById("installCard")) return null; var c = document.createElement("div"); c.className = "card"; c.id = "installCard"; c.style.borderColor = "var(--accent)"; c.innerHTML = html; n.parentNode.insertBefore(c, n); return c; }
  window.addEventListener("beforeinstallprompt", function(e){ e.preventDefault(); deferred = e;
    var c = card('<h3>📲 تثبيت خُطوة على الموبايل</h3><div class="muted" style="margin-bottom:8px">أيقونة على الشاشة، وبيشتغل من غير نت، والتقدم بيفضل محفوظ.</div><button class="btn" type="button" id="installBtn">تثبيت التطبيق</button>');
    if(c) document.getElementById("installBtn").onclick = function(){ deferred.prompt(); deferred.userChoice.then(function(){ c.remove(); deferred = null; }); };
  });
  if(ios) setTimeout(function(){ card('<h3>📲 تثبيت خُطوة على الآيفون</h3><div class="muted">من Safari: زرار المشاركة ⬆️ ← «إضافة إلى الشاشة الرئيسية». وبعد كده التطبيق يتفتح من الأيقونة دايمًا عشان التقدم يفضل محفوظ.</div>'); }, 1500);
  window.addEventListener("appinstalled", function(){ var c = document.getElementById("installCard"); if(c) c.remove(); });
})();
</script>
</body>'''
html=html.replace('</body>',inst,1)
open(OUT+'/app/index.html','w',encoding='utf-8').write(html)
for fn in ['icon-192.png','icon-512.png','icon-maskable-512.png','apple-touch-icon.png']: shutil.copy('brand/'+fn, OUT+'/app/'+fn)
shutil.copy('brand/logo.svg', OUT+'/logo.svg')
man={"name":"خُطوة","short_name":"خُطوة","description":"نسبة المذاكرة من المنهج والحضور لطلاب الثانوي. Created by Add Value.","lang":"ar","dir":"rtl","start_url":"./","scope":"./","display":"standalone","orientation":"portrait","background_color":"#F2F5F3","theme_color":"#103B3C",
 "icons":[{"src":"icon-192.png","sizes":"192x192","type":"image/png"},{"src":"icon-512.png","sizes":"512x512","type":"image/png"},{"src":"icon-maskable-512.png","sizes":"512x512","type":"image/png","purpose":"maskable"}]}
json.dump(man,open(OUT+'/app/manifest.webmanifest','w',encoding='utf-8'),ensure_ascii=False,indent=1)
sw='''const CACHE = "%s";
const ASSETS = ["./","./index.html","./manifest.webmanifest","./icon-192.png","./icon-512.png","./icon-maskable-512.png","./apple-touch-icon.png"];
self.addEventListener("install", e => { e.waitUntil(caches.open(CACHE).then(c => c.addAll(ASSETS)).then(() => self.skipWaiting())); });
self.addEventListener("activate", e => { e.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => k.startsWith("kw-") && k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim())); });
self.addEventListener("fetch", e => {
  const req = e.request; if (req.method !== "GET" || new URL(req.url).origin !== location.origin) return;
  if (req.url.endsWith("curriculum.json")) { e.respondWith(fetch(req).catch(() => caches.match(req).then(r => r || new Response("null", {status: 504, headers: {"Content-Type": "application/json"}})))); return; }
  if (req.mode === "navigate") {
    e.respondWith(fetch(req).then(res => { const copy = res.clone(); caches.open(CACHE).then(c => c.put("./index.html", copy)); return res; }).catch(() => caches.match("./index.html")));
    return;
  }
  e.respondWith(caches.match(req).then(hit => hit || fetch(req).then(res => { const copy = res.clone(); caches.open(CACHE).then(c => c.put(req, copy)); return res; })));
});
''' % VER
open(OUT+'/app/sw.js','w',encoding='utf-8').write(sw)
def page(src,dst,path,title):
    s=open(src,encoding='utf-8').read()
    if GC:
        js='<script>(function(){try{if(navigator.doNotTrack==="1")return;var u="https://%s.goatcounter.com/count?p=%s&t=%s&s="+(screen.width||0)+(document.referrer&&document.referrer.indexOf(location.host)<0?"&r="+encodeURIComponent(document.referrer.split("?")[0].slice(0,200)):"")+"&rnd="+Math.random().toString(36).slice(2);if(navigator.sendBeacon)navigator.sendBeacon(u);else{var i=new Image();i.src=u;}}catch(e){}})();</script>' % (GC, path, title)
        s=s.replace('<!--GC-->',js)
        if "connect-src 'self'" in s: s=s.replace("connect-src 'self'", "connect-src 'self' https://%s.goatcounter.com" % GC, 1)
        else: s=__import__('re').sub(r"(content=\"default-src 'none';)", r"\1 connect-src https://%s.goatcounter.com;" % GC, s, count=1)
        if "script-src" not in s: s=s.replace("default-src 'none';","default-src 'none'; script-src 'unsafe-inline';",1)
    else:
        s=s.replace('<!--GC-->','')
    open(OUT+'/'+dst,'w',encoding='utf-8').write(s)
page('landing.html','index.html','%2F','%D8%A7%D9%84%D8%B5%D9%81%D8%AD%D8%A9%20%D8%A7%D9%84%D8%B1%D8%A6%D9%8A%D8%B3%D9%8A%D8%A9')
page('story.html','story.html','%2Fstory','%D8%A7%D9%84%D8%AD%D9%83%D8%A7%D9%8A%D8%A9')
page('report.html','report.html','%2Freport','%D8%AA%D9%82%D8%B1%D9%8A%D8%B1%20%D9%88%D9%84%D9%8A%20%D8%A3%D9%85%D8%B1')
import subprocess
cj=subprocess.run(['node','-e','const fs=require("fs");const vm=require("vm");const c={};vm.createContext(c);vm.runInContext(fs.readFileSync("data.js","utf8").replace(/var CFG[\\s\\S]*$/,"")+";this.o={v:CURR_VERSION,CURR:CURR,STAGES:STAGES};",c);process.stdout.write(JSON.stringify(c.o));'],capture_output=True,text=True,cwd='.')
assert cj.returncode==0, cj.stderr
open(OUT+'/app/curriculum.json','w',encoding='utf-8').write(cj.stdout)
open(OUT+'/robots.txt','w').write('User-agent: *\nAllow: /\n')
open(OUT+'/README.md','w',encoding='utf-8').write('''# خُطوة

تطبيق مجاني لطلاب الثانوي في مصر: كل درس بيتذاكر على 4 خطوات (سماع، فهم، حل، مراجعة)، والتطبيق بيحسب نسبة المذاكرة من المنهج، والحضور، والتقدم يوم بيوم.

- الصفحة الرئيسية: `index.html`
- التطبيق: `app/` (بيتثبت على الموبايل ويشتغل من غير نت)
- كل البيانات بتتحفظ على موبايل المستخدم بس.

Created by **Add Value**
''')
print('built', os.path.getsize(OUT+'/app/index.html'))
