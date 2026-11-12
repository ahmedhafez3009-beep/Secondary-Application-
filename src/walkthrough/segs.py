import json,subprocess,os,sys
P=json.load(open('plan.json'));only=sys.argv[1:]
for p in P:
    out='seg/s%02d.mp4'%p['i']
    if only and str(p['i']) not in only: continue
    D=p['D'];card='cards/c%02d.png'%p['i']
    if p['src'] is None:
        cmd=['ffmpeg','-loglevel','error','-y','-loop','1','-framerate','30','-i',card,'-t',str(D),'-vf','format=yuv420p','-c:v','libx264','-preset','veryfast','-crf','20','-r','30',out+'.tmp.mp4']
    else:
        cr='scale=454:982:flags=lanczos,crop=454:964:0:9,'
        v=f"[1:v]trim=start={p['a']:.3f}:duration={p['ds']:.3f},setpts=(PTS-STARTPTS)/{p['sp']:.4f},fps=30,{cr}pad=454:964:0:0:color=#F2F5F3,tpad=stop_mode=clone:stop_duration={D+1:.2f},trim=duration={D:.3f}[v];[0:v][v]overlay=178:58[a];[a][2:v]overlay=0:0,format=yuv420p[o]"
        cmd=['ffmpeg','-loglevel','error','-y','-loop','1','-framerate','30','-t',str(D),'-i',card,'-i',p['src'],'-loop','1','-framerate','30','-t',str(D),'-i','cards/frame.png','-filter_complex',v,'-map','[o]','-t',str(D),'-c:v','libx264','-preset','veryfast','-crf','20','-r','30',out+'.tmp.mp4']
    r=subprocess.run(cmd,capture_output=True,text=True)
    if r.returncode==0: os.replace(out+'.tmp.mp4',out)
    else: print('FAIL',p['i'],r.stderr[-400:])
print('done')
