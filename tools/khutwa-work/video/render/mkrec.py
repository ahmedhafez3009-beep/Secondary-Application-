# python3 mkrec.py <board> <slideTag:audioWav:srcM4a>...   → rec json (يدمج مع الموجود)
import json,subprocess,base64,sys,os,glob
src=open('align.py').read().split('res={}')[0].replace("D=json.load(open('lines_A.json'))","D=json.load(open(sys.argv[1]))")
board=sys.argv[2];exec(src)
recp=f'/home/claude/secondary-application-/tools/khutwa-work/video/rec/{board}.json'
out=json.load(open(recp)) if os.path.exists(recp) else {'key':board,'lines':{}}
names=[s['name'].split(' ')[0] for s in SL]
for tag in sys.argv[3:]:
    i=names.index(tag);srcm=max(glob.glob(f'/mnt/user-data/uploads/*-{tag}.m4a'),key=os.path.getmtime)
    segs,dur=vad(tag+'.wav');ls=slide_lines(i);sp,k=align(ls,segs)
    print(f'## {tag} lines {len(ls)} segs {len(segs)} audio {dur:.1f} k={k:.2f}')
    for l,(a,b) in zip(ls,sp):
        s0=segs[a][0];s1=segs[b-1][1];prevEnd=segs[a-1][1] if a>0 else 0;nextSt=segs[b][0] if b<len(segs) else dur
        cs=max(prevEnd+.05,s0-.3,0);ce=min(nextSt-.05,s1+.4);lt=l['tk'][-1]
        if lt['p']: ce=min(nextSt-.05,s1+float(lt['w'].strip('[]'))+.6)
        act=s1-s0;print(f"  {l['id']:7} exp {l['d']-.45:5.1f} act {act:5.1f} r={act/(k*(l['d']-.45)):.2f} nseg {b-a} | {l['txt'][:45]}")
        rel=[[round(x-cs,2),round(y-cs,2)] for x,y in segs[a:b]];fn=f'clip_{board}_{l["id"]}.webm'
        subprocess.run(['ffmpeg','-v','error','-y','-ss',f'{cs:.3f}','-to',f'{ce:.3f}','-i',srcm,'-ac','1','-c:a','libopus','-b:a','40k','-f','webm',fn],check=True)
        out['lines'][f"{l['id']}#{l['ix']}"]={'type':'audio/webm','an':{'dur':round(ce-cs,2),'segs':rel},'b64':base64.b64encode(open(fn,'rb').read()).decode()}
json.dump(out,open(recp,'w'));print('total lines',len(out['lines']))
