import base64,os,sys
s=open('explainer.src.html',encoding='utf-8').read()
f=lambda p,m:'data:%s;base64,%s'%(m,base64.b64encode(open(p,'rb').read()).decode())
s=s.replace('__LALEZAR__',f('fonts/Lalezar-Regular.ttf','font/ttf')).replace('__CAIRO__',f('fonts/Cairo.ttf','font/ttf'))
s=s.replace('__AUDIO__',f('khutwa_audio.m4a','audio/mp4') if os.path.exists('khutwa_audio.m4a') else '')
open('explainer.html','w',encoding='utf-8').write(s); print(len(s))
