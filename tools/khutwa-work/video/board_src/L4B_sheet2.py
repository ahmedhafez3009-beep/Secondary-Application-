import sys,subprocess,os
from PIL import Image
name=sys.argv[1];ids=sys.argv[2:]
W='/home/claude/out/L4B_work/'
env=dict(os.environ,BOARD='/home/claude/out/khutwa_hist_board_L4B.html',NODE_PATH=subprocess.check_output(['npm','root','-g']).decode().strip())
print(subprocess.run(['node','/home/claude/out/tools/L4B_frt.js']+ids,cwd=W,env=env,capture_output=True,text=True).stderr.strip()[:300])
ims=[Image.open(W+'h_'+i.replace(':','_').replace('@','_')+'.png') for i in ids]
cols=3;w,h=ims[0].size;s=0.5;w2,h2=int(w*s),int(h*s);rows=(len(ims)+cols-1)//cols
sh=Image.new('RGB',(w2*cols,h2*rows),'white')
for k,im in enumerate(ims): sh.paste(im.resize((w2,h2)),((k%cols)*w2,(k//cols)*h2))
sh.save(W+name+'.png');print(sh.size)
