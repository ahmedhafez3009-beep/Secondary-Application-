import json,sys
# usage: apply_curr.py sk curr.json  — renames units/lessons in data.js line 6; refuses if counts/order shape differ
sk,cf=sys.argv[1],sys.argv[2]
P='/home/claude/secondary-application-/src/data.js'
L=open(P,encoding='utf8').read().split('\n')
i=next(n for n,l in enumerate(L) if l.startswith('var CURR = '))
C=json.loads(L[i][len('var CURR = '):].rstrip().rstrip(';'))
new=json.load(open(cf))['parts']; old=C[sk]['parts']
assert len(new)==len(old),'parts'
for (pn,nu),(po,ou) in zip(new,old):
  assert len(nu)==len(ou),('units',pn)
  for a,b in zip(nu,ou): assert len(a[1].split('|'))==len(b[1].split('|')),('lessons',a[0])
ch=0
for pi,(pn,nu) in enumerate(new):
  for ui,u in enumerate(nu):
    if old[pi][1][ui]!=list(u): ch+=1; old[pi][1][ui]=list(u)
L[i]='var CURR = '+json.dumps(C,ensure_ascii=False)+';'
open(P,'w',encoding='utf8').write('\n'.join(L)); print(sk,'units changed',ch)
