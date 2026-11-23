import sys,subprocess,os
from PIL import Image
ids=sys.argv[2:];name=sys.argv[1]
W='/home/claude/out/L6C_work/'
env=dict(os.environ,BOARD='/home/claude/out/khutwa_hist_board_L6C.html',TAG='L6C_',NODE_PATH=subprocess.check_output(['npm','root','-g']).decode().strip())
print(subprocess.run(['node','/home/claude/secondary-application-/tools/khutwa-work/video/fr.js']+ids,cwd=W,env=env,capture_output=True,text=True).stdout.strip())
ims=[Image.open(W+'g_L6C_%s.png'%i) for i in ids]
cols=3;w,h=ims[0].size;s=0.5;w2,h2=int(w*s),int(h*s)
rows=(len(ims)+cols-1)//cols
sh=Image.new('RGB',(w2*cols,h2*rows),'white')
for k,im in enumerate(ims): sh.paste(im.resize((w2,h2)),((k%cols)*w2,(k//cols)*h2))
sh.save(W+name+'.png');print(sh.size)
