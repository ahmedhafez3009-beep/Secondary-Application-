# python3 mix.py <prefix> <recordings.json>  → <prefix>_a.wav (صوت أحمد + مؤثرات واطية)
import json,sys,subprocess,base64,numpy as np,os,tempfile,wave
pre,recf=sys.argv[1],sys.argv[2];SR=48000
tl=json.load(open(pre+'_tl.json'));R=json.load(open(recf))['lines'];ev=json.load(open(pre+'_sfx.json'))
N=int(tl['total']*SR)+SR;out=np.zeros(N,np.float32);voice=np.zeros(N,bool)
def dec(b64):
    with tempfile.NamedTemporaryFile(suffix='.webm',delete=False) as f: f.write(base64.b64decode(b64));fn=f.name
    raw=subprocess.run(['ffmpeg','-v','error','-i',fn,'-ac','1','-ar',str(SR),'-f','f32le','-'],capture_output=True).stdout;os.unlink(fn)
    return np.frombuffer(raw,np.float32)
for s in tl['segs']:
    if 'key' not in s: continue
    x=dec(R[s['key']]['b64']);a=int(s['start']*SR);n=int(s['dur']*SR);seg=x[a:a+n];i=int(s['w']*SR)
    out[i:i+len(seg)]+=seg;voice[i:i+len(seg)]=True
# مؤثرات (نفس محرك السبورة تقريبًا)
def tone(f,d,v,f2=None):
    t=np.arange(int(d*SR))/SR;fr=f*np.ones_like(t) if not f2 else f*(f2/f)**(t/d);ph=2*np.pi*np.cumsum(fr)/SR
    return (np.sin(ph)*v*np.exp(np.log(1e-4/v)*t/d)).astype(np.float32)
def whoosh():
    n=int(.5*SR);x=np.random.randn(n).astype(np.float32);env=np.interp(np.arange(n),[0,.2*SR,.5*SR],[0,.12,0]).astype(np.float32)
    X=np.fft.rfft(x);fq=np.fft.rfftfreq(n,1/SR);X*=np.exp(-((np.log(fq+1)-np.log(1000))**2)/1.0);return (np.fft.irfft(X,n)*env*3).astype(np.float32)
S={'tick':tone(1200,.06,.06),'boom':tone(120,.7,.3,40),'whoosh':whoosh()}
c=tone(784,.5,.07);c2=np.zeros_like(c);k=int(.08*SR);c2[k:]=tone(1047,.42,.07)[:len(c)-k];S['chime']=c+c2
for e in ev:
    s=S.get(e['k']);
    if s is None: continue
    i=int(e['w']*SR);g=.3 if voice[i:i+len(s)].any() else 1.0;out[i:i+len(s)]+=s[:N-i]*g
pk=np.abs(out).max();out=out/pk*0.92 if pk>0.92 else out
w=wave.open(pre+'_a.wav','wb');w.setnchannels(1);w.setsampwidth(2);w.setframerate(SR);w.writeframes((out*32767).astype(np.int16).tobytes());w.close();print('audio',len(out)/SR)
