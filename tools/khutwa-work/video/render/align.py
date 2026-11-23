import json,wave,numpy as np,sys,math
D=json.load(open('lines_A.json'));SL=D['SL'];L=D['L'];END=D['END']
def slide_lines(i):
    a=SL[i]['t'];b=SL[i+1]['t'] if i+1<len(SL) else END
    return [l for l in L if l['txt'] and a-1e-3<=l['t']<b-1e-3]
def vad(fn):
    w=wave.open(fn);sr=w.getframerate();x=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(np.float32)/32768
    hop=sr//100;n=len(x)//hop;env=np.sqrt((x[:n*hop].reshape(n,hop)**2).mean(1))
    sm=np.convolve(env,np.ones(7)/7,'same');so=np.sort(sm);fl=so[int(len(so)*.08)];pk=so[int(len(so)*.985)]
    th=fl+(pk-fl)*.1;on=sm>th;segs=[];st=-1
    for i,v in enumerate(on):
        if v and st<0: st=i
        if not v and st>=0: segs.append([st,i]);st=-1
    if st>=0: segs.append([st,len(on)])
    segs=[s for s in segs if s[1]-s[0]>=7];m=[]
    for s in segs:
        if m and s[0]-m[-1][1]<18: m[-1][1]=s[1]
        else: m.append(list(s))
    return [(a*.01,b*.01) for a,b in m],n*.01
def align(lines,segs):
    N=len(lines);S=len(segs)
    exp=np.array([max(.5,l['d']-.45) for l in lines]);
    # cumulative: boundary after segment j (gap j between seg j and j+1)
    tot=segs[-1][1]-segs[0][0];k=tot/exp.sum()
    INF=1e18;C=np.full((N+1,S+1),INF);P=np.zeros((N+1,S+1),int);C[0][0]=0
    # line i covers segs[a:b]
    for i in range(1,N+1):
        for b in range(i,S+1-(N-i)):
            best=INF;arg=-1
            for a in range(i-1,b):
                if C[i-1][a]>=INF: continue
                act=segs[b-1][1]-segs[a][0]
                c=(math.log(act/(k*exp[i-1])))**2*4
                if b<S: c-=min(segs[b][0]-segs[b-1][1],1.5)*1.0
                v=C[i-1][a]+c
                if v<best: best=v;arg=a
            C[i][b]=best;P[i][b]=arg
    out=[];b=S
    for i in range(N,0,-1):
        a=P[i][b];out.append((a,b));b=a
    return out[::-1],k
res={}
for i,n in enumerate(['A0','A1','A2','A3']):
    segs,dur=vad(n+'.wav');ls=slide_lines(i);sp,k=align(ls,segs)
    print(f'## {n} lines {len(ls)} segs {len(segs)} audio {dur:.1f} k={k:.2f}')
    for l,(a,b) in zip(ls,sp):
        act=segs[b-1][1]-segs[a][0];print(f"  {l['id']:6} exp {l['d']-.45:5.1f} act {act:5.1f} r={act/(k*(l['d']-.45)):.2f} [{segs[a][0]:6.2f}-{segs[b-1][1]:6.2f}] nseg {b-a} gapAfter {(segs[b][0]-segs[b-1][1]) if b<len(segs) else 0:.2f} | {l['txt'][:40]}")
    res[n]={'segs':segs,'dur':dur,'lines':[{'ix':l['ix'],'id':l['id'],'a':a,'b':b} for l,(a,b) in zip(ls,sp)]}
json.dump(res,open('align.json','w'))
