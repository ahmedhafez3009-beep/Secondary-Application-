import numpy as np, wave
SR=48000; DUR=76.0; N=int(SR*DUR); L=np.zeros(N); Rr=np.zeros(N)
rng=np.random.default_rng(7)
def add(sig,t,g=1.0,pan=0.0):
    i=int(t*SR); n=min(len(sig),N-i)
    if n<=0: return
    L[i:i+n]+=sig[:n]*g*(1-pan)/1.0; Rr[i:i+n]+=sig[:n]*g*(1+pan)/1.0
def env(n,a,d):
    t=np.arange(n)/SR; return np.minimum(1,t/a)*np.exp(-t/d)
def marimba(f,dur=1.2):
    n=int(dur*SR); t=np.arange(n)/SR
    s=np.sin(2*np.pi*f*t)+.35*np.sin(2*np.pi*f*4*t)*np.exp(-t/.08)+.15*np.sin(2*np.pi*f*10*t)*np.exp(-t/.03)
    return s*env(n,.003,.35)
def pluck(f,dur=.6):
    n=int(dur*SR); t=np.arange(n)/SR
    return (np.sin(2*np.pi*f*t)+.3*np.sin(2*np.pi*2*f*t))*env(n,.002,.12)
def tick(dur=.05):
    n=int(dur*SR); return rng.standard_normal(n)*env(n,.0005,.006)*.6+np.sin(2*np.pi*2200*np.arange(n)/SR)*env(n,.0005,.01)
def whoosh(dur=.45):
    n=int(dur*SR); x=rng.standard_normal(n); t=np.arange(n)/SR
    # moving one-pole lowpass
    y=np.zeros(n); a=0; c=np.interp(t,[0,dur*.6,dur],[.02,.35,.05])
    for i in range(n): a+= c[i]*(x[i]-a); y[i]=a
    return y*np.sin(np.pi*t/dur)**2*1.4
def chord(fs,dur=2.4):
    n=int(dur*SR); t=np.arange(n)/SR; s=sum(np.sin(2*np.pi*f*t)+.25*np.sin(2*np.pi*2*f*t+.3) for f in fs)/len(fs)
    return s*np.minimum(1,t/.06)*np.exp(-t/.9)
def boom(dur=1.2):
    n=int(dur*SR); t=np.arange(n)/SR; f=np.interp(t,[0,.4],[90,45])
    return np.sin(2*np.pi*np.cumsum(f)/SR)*env(n,.005,.35)
def pad(dur,fs):
    n=int(dur*SR); t=np.arange(n)/SR; s=sum(np.sin(2*np.pi*f*t+np.sin(2*np.pi*.2*t)) for f in fs)/len(fs)
    return s*np.sin(np.pi*np.clip(t/dur,0,1))**1.5
G,C,E,G5,C5=392.0,523.25,659.25,783.99,1046.5
def jingle(t0,hit):
    add(whoosh(.5),t0-.3,.5)
    for k,f in enumerate([G,C5,E*2,G5*2][:0] or [G,C5,659.25*1,783.99]): pass
    for k,f in enumerate([392.0,523.25,659.25,783.99]): add(marimba(f),t0+k*.16,.42,(-.3+.2*k))
    add(chord([261.63,329.63,392.0,523.25]),hit,.32); add(boom(),hit,.55)
SC=[0,5,10.5,18,24.5,31,37.5,43.5,50,55.5,62.5,67.5]
# hook: suspense pad + hit
add(pad(5.0,[110,164.8,220]),0,.10); add(tick(),.15,.25)
for k in range(8): add(tick(),.45+k*.5,.12)
add(pluck(C5),1.25,.35); add(boom(.8),1.25,.25)
for b in SC[1:]: add(whoosh(.4),b-.22,.32)
jingle(5.35,6.5)
# steps: plucks rising + check ticks
for i,f in enumerate([C,587.33,659.25,783.99]): a=10.5+1.0+i*.75; add(pluck(f),a,.3,.2); add(pluck(f*2,.3),a+.45,.18,-.2)
# progress: ticks during count, pluck at end, bars
for k in range(12): add(tick(),18.7+k*.1,.10)
add(pluck(783.99),19.9,.35)
for i in range(5): add(pluck([C,587.33,659.25,698.46,783.99][i],.4),18+2.3+i*.28,.2)
# chips
for i in range(5): add(pluck([C,659.25,783.99,880,1046.5][i],.4),24.5+.9+i*.2,.22)
add(tick(),24.5+4.2,.4); add(pluck(659.25),24.5+4.25,.25)
# focus: clock ticks + review dots
for k in range(10): add(tick(),31+1.0+k*.26,.12)
for i in range(4): add(pluck([C,659.25,783.99,1046.5][i]),31+3.1+i*.62,.25)
# plan blocks + countdown
for i in range(11): add(tick(),37.5+.9+i*.12,.14)
for k in range(7): add(tick(),37.5+3.3+k*.14,.14)
add(pluck(783.99),37.5+4.3,.3)
# attendance + flip
for i in range(6): add(pluck(C if i!=3 else 349.23,.35),43.5+.9+i*.14,.18)
add(whoosh(.35),43.5+4.0,.25); add(pluck(1046.5),43.5+4.6,.25)
# badges
for i in range(12): add(pluck([C,587.33,659.25,783.99][i%4]*(1+(i//4)),.3),50+.9+i*.1,.14,(i%2-.5)*.4)
add(chord([523.25,659.25,783.99],1.4),52.6,.18)
# whatsapp: tap + message pop
add(tick(),56.9,.4); add(pluck(880,.5),57.4,.35); add(pluck(1318.5,.4),57.5,.2)
# privacy
for i in range(3): add(pluck([C,659.25,783.99][i]),62.5+.75+i*.9,.28)
# CTA: logo chime, url pop, Add Value jingle
add(marimba(523.25),67.6,.3); add(pluck(783.99),69.3,.25)
jingle(71.5,72.65)
m=max(np.abs(L).max(),np.abs(Rr).max()); st=np.stack([L,Rr],1)/m*.8
fade=int(.6*SR); st[-fade:]*=np.linspace(1,0,fade)[:,None]
w=wave.open('khutwa_audio_raw.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st*32767).astype('<i2').tobytes()); w.close()
