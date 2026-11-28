import json,subprocess,sys,os
cfgf=sys.argv[1];C=json.load(open(cfgf));D=os.path.dirname(os.path.abspath(C['out']))+'/w_'+os.path.basename(C['out'])[:-4];os.makedirs(D,exist_ok=True)
run=lambda a:subprocess.run(a,check=True)
dur=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',C['src']]))
P=sorted(C['pauses'],key=lambda p:p['at']);PD=[p.get('dur',6) for p in P]
def fin(t,incl=False):  # map source time -> final time
    return t+sum(d for p,d in zip(P,PD) if p['at']<t or (incl and p['at']<=t))
for p in P: p['back_final']=fin(p['back'],True) if p['back']>0 else 0; p['at_final']=fin(p['at'])
for s in C['sections']: s['at_final']=fin(s['at'],True)
C['pauses']=P;C['total_final']=dur+sum(PD);cf=D+'/cfg.json';json.dump(C,open(cf,'w'),ensure_ascii=False)
for i,p in enumerate(P): run(['ffmpeg','-v','error','-y','-ss',str(max(p['at']-.08,0)),'-i',C['src'],'-frames:v','1',f'{D}/bg{i}.jpg'])
run(['node','/home/claude/montage/cards.js',cf,D])
# pieces
cuts=[0]+[p['at'] for p in P]+[dur];lst=[]
for i in range(len(cuts)-1):
    f=f'{D}/v{i}.mp4'
    if cuts[i+1]-cuts[i]>0.2:
      run(['ffmpeg','-v','error','-y','-ss',f'{cuts[i]:.3f}','-to',f'{cuts[i+1]:.3f}','-i',C['src'],'-c:v','libx264','-preset','veryfast','-crf','20','-r','25','-c:a','aac','-ar','48000','-ac','2','-b:a','160k',f]);lst.append(f)
    if i<len(P):
        n=PD[i];g=f'{D}/pz{i}.mp4'
        run(['ffmpeg','-v','error','-y','-framerate','1','-i',f'{D}/p{i}_%d.png','-f','lavfi','-t',str(n),'-i','anullsrc=r=48000:cl=stereo','-vf','fps=25,format=yuv420p','-t',str(n),'-c:v','libx264','-preset','veryfast','-crf','20','-c:a','aac','-b:a','160k',g]);lst.append(g)
open(D+'/list.txt','w').write(''.join(f"file '{f}'\n" for f in lst))
run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',D+'/list.txt','-c','copy',D+'/cat.mp4'])
# overlays: section titles (2.6s fade) + progress bar
T=C['total_final'];ST=json.load(open(D+'/st.json'))
inp=['-i',D+'/cat.mp4'];fc="color=c=0xfbf8f1:s=1280x720:r=25[bg];[0:v]scale=1088:612[sv];[bg][sv]overlay=192:0:shortest=1[c0];color=c=0x1EA05F:s=1064x14:r=25[pc];";cur='c0';n=1
for a in range(len(ST)):
    inp+=['-i',f'{D}/rail{a}.png'];e=ST[a+1]['at'] if a+1<len(ST) else T+1
    fc+=f"[{cur}][{n}:v]overlay=0:0:enable='between(t,{ST[a]['at']:.2f},{e:.2f})'[r{a}];";cur=f'r{a}';n+=1
fc+=f"[{cur}][pc]overlay=x='1280-24-1064*t/{T:.2f}':y=674:enable='gte(t,0)'[p0];";cur='p0'
fc=fc.replace("[pc]overlay=x='1280-24-1064*t/","[pc]overlay=x='1256-1064*t/")
for i,s in enumerate(C['sections']):
    a=s['at_final']+.3
    inp+=['-loop','1','-framerate','25','-t','3.1','-i',f'{D}/s{i}.png']
    fc+=f"[{n}:v]format=rgba,fade=t=in:st=0:d=0.35:alpha=1,fade=t=out:st=2.6:d=0.4:alpha=1,setpts=PTS-STARTPTS+{a:.2f}/TB[t{i}];[{cur}][t{i}]overlay=0:0:eof_action=pass[w{i}];";cur=f'w{i}';n+=1
fc=fc.rstrip(';')
run(['ffmpeg','-v','error','-y']+inp+['-filter_complex',fc,'-t',f'{T:.2f}','-map',f'[{cur}]','-map','0:a','-c:v','libx264','-preset','veryfast','-crf','20','-c:a','copy','-movflags','+faststart',C['out']])
ch=[(s['at_final'],s['title']) for s in C['sections']]+[(p['at_final'],'⏸ وقفة: '+p['head']) for p in P];ch.sort()
mm=lambda s:f"{int(s)//60}:{int(s)%60:02d}"
open(C['out'][:-4]+'_chapters.txt','w').write('\n'.join(f"{mm(t)} {n}" for t,n in ch)+'\n');print('OK',T)
