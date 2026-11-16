import json,sys,subprocess
# usage: integrate.py sk "src text" file1.json [file2.json ...]
sk,src,files=sys.argv[1],sys.argv[2],sys.argv[3:]
R='/home/claude/secondary-application-/src/'
titles=json.loads(subprocess.check_output(['node','-e','''const fs=require("fs");eval(fs.readFileSync("%sdata.js","utf8")+";global.C=CURR");const o=[];C["%s"].parts.forEach(p=>p[1].forEach(u=>u[1].split("|").forEach(l=>o.push(l))));console.log(JSON.stringify(o))'''%(R,sk)]))
by={}
for f in files: by.update(json.load(open(f))['by'])
bad=[k for k in by if k not in titles]; missing=[t for t in titles if t not in by]
for k,qs in by.items():
  for q in qs:
    assert isinstance(q['q'],str) and len(q['o'])==4 and len(set(q['o']))==4 and q['a'] in (0,1,2,3) and q.get('e'), (k,q)
out={'v':1,'sk':sk,'src':src,'by':{t:by[t] for t in titles if t in by}}
json.dump(out,open(R+'quiz/%s.json'%sk,'w'),ensure_ascii=False,separators=(',',':'))
print(sk,'lessons',len(out['by']),'/',len(titles),'questions',sum(map(len,out['by'].values())),'| not-in-curriculum:',bad,'| no-quiz:',missing)
