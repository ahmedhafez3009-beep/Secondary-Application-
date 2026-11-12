import json,wave,numpy as np
SR=48000;P=json.load(open('plan.json'));T=P[-1]['t0']+P[-1]['D'];N=int(SR*(T+0.5));V=np.zeros(N);S=np.zeros(N);rng=np.random.default_rng(5)
def rd(f):
    w=wave.open(f);return np.frombuffer(w.readframes(w.getnframes()),'<i2').astype(float)/32768
def add(b,s,t,g=1):
    i=int(t*SR);n=min(len(s),N-i)
    if n>0:b[i:i+n]+=s[:n]*g
def env(n,a,d):t=np.arange(n)/SR;return np.minimum(1,t/a)*np.exp(-t/d)
def whoosh(d=.5):
    n=int(d*SR);x=rng.standard_normal(n);t=np.arange(n)/SR;y=np.zeros(n);a=0;c=np.interp(t,[0,d*.6,d],[.02,.3,.04])
    for i in range(n):a+=c[i]*(x[i]-a);y[i]=a
    return y*np.sin(np.pi*t/d)**2*1.3
def marimba(f):n=int(1.2*SR);t=np.arange(n)/SR;return (np.sin(2*np.pi*f*t)+.35*np.sin(8*np.pi*f*t)*np.exp(-t/.08))*env(n,.003,.35)
def chord(fs,d=2.4):n=int(d*SR);t=np.arange(n)/SR;return sum(np.sin(2*np.pi*f*t) for f in fs)/len(fs)*np.minimum(1,t/.06)*np.exp(-t/.9)
def boom():n=int(1.2*SR);t=np.arange(n)/SR;f=np.interp(t,[0,.4],[90,45]);return np.sin(2*np.pi*np.cumsum(f)/SR)*env(n,.005,.35)
for i,p in enumerate(P):
    add(V,rd('vo/wav/line_%02d.wav'%(i+1)),p['t0']+0.25)
    if i and P[i-1]['sec']!=p['sec']:add(S,whoosh(),p['t0']-0.15,.35)
o=P[-1]['t0']
for k,f in enumerate([392,523.25,659.25,783.99]):add(S,marimba(f),o+0.1+k*.16,.45)
add(S,chord([261.63,329.63,392,523.25]),o+0.8,.35);add(S,boom(),o+0.8,.5)
venv=np.convolve(np.abs(V),np.ones(4800)/4800,'same');mix=V+S*(1-0.6*np.clip(venv/0.03,0,1))
f=int(.8*SR);mix[-f:]*=np.linspace(1,0,f);mix=mix/np.abs(mix).max()*0.9
w=wave.open('mix_raw.wav','wb');w.setnchannels(1);w.setsampwidth(2);w.setframerate(SR);w.writeframes((mix*32767).astype('<i2').tobytes());w.close()
