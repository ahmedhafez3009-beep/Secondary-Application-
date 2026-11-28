import json,re,sys
# usage: srt2.py <board> <cfg.json> <out.srt> [w0]
b,cf,out=sys.argv[1:4];w0=float(sys.argv[4]) if len(sys.argv)>4 else 0
C=json.load(open(cf));tl=json.load(open(f'/home/claude/render/{b}_tl.json'));d=json.load(open(f'/home/claude/voice/src_{b}.json'))
TX={f"{l['id']}#{l['ix']}":l['txt'] for l in d['L']}
import subprocess
dur=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',C['src']]))
P=[(p['at'],p.get('dur',15)) for p in C['pauses']]
fin=lambda t:t-w0+sum(dd for a,dd in P if a<=t)
ts=lambda s:f"{int(s//3600):02d}:{int(s%3600//60):02d}:{int(s%60):02d},{int(round((s%1)*1000))%1000:03d}"
cues=[]
for s in tl['segs']:
    k=s.get('key');
    if not k or k not in TX: continue
    a,e=s['w'],s['w']+s['dur']
    if a<w0-0.01 or a>=dur+w0: continue
    t=re.sub(r'\s*\[\[[\d.]+\]\]\s*',' ',TX[k]).strip();words=t.split()
    if not words: continue
    n=max(1,round(len(words)/11));per=len(words)/n;chunks=[' '.join(words[round(i*per):round((i+1)*per)]) for i in range(n)]
    L=sum(len(c) for c in chunks);x=a
    for c in chunks:
        y=x+(e-a)*len(c)/L;cues.append((fin(x),fin(min(y,dur+w0)),c));x=y
open(out,'w').write(''.join(f"{i+1}\n{ts(a)} --> {ts(e)}\n{t}\n\n" for i,(a,e,t) in enumerate(cues)))
print(len(cues),'cues',ts(cues[-1][1]))
