import json,os,subprocess,sys,wave,re
sys.path.insert(0,'.');from steps import S
M=json.load(open('../rec/raw/meta.json'));SC={s['name']:s for s in M['scenes']}
VO='vo/wav/'
def vdur(i):
    f=VO+'line_%02d.wav'%(i+1)
    if os.path.exists(f):
        w=wave.open(f);return w.getnframes()/w.getframerate()
    return len(S[i][3].split())/2.5+0.4
SECS=[];[SECS.append(x[2]) for x in S if x[2] not in SECS]
plan=[]
for i,(sc,key,sec,en,ar) in enumerate(S):
    d=vdur(i)
    if sc=='outro': plan.append(dict(i=i,sc=sc,key=key,sec=sec,en=en,ar=ar,vd=d,D=d+3.0,src=None));continue
    s=SC[sc];ks=[x['key'] for x in s['steps']];k=ks.index(key)
    a=s['steps'][k]['t']-0.15; b=s['steps'][k+1]['t']-0.15 if k+1<len(ks) else s['end']-0.6
    ds=b-a; D=max(d+0.45, min(ds, d+1.4)); sp=max(1.0, ds/D)
    if sp>6: sp=6
    plan.append(dict(i=i,sc=sc,key=key,sec=sec,en=en,ar=ar,vd=d,D=round(D,3),src='../rec/raw/'+s['video'],a=a,ds=ds,sp=sp,crop=False))
t=0
for p in plan: p['t0']=round(t,3); t+=p['D']
json.dump(plan,open('plan.json','w'),ensure_ascii=False,indent=0)
print('steps',len(plan),'total',round(t,1),'s')
