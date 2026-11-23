# usage: python3 A_v8_sheet.py name id...  → frames (fr.js, 93% of each line) pasted 3 per row
import sys,subprocess,os
from PIL import Image
name=sys.argv[1];ids=sys.argv[2:];W='/home/claude/out/A_v8_work/'
env=dict(os.environ,BOARD='/home/claude/out/khutwa_hist_board_A.html',TAG='A8_',NODE_PATH=subprocess.check_output(['npm','root','-g']).decode().strip())
print(subprocess.run(['node','/home/claude/secondary-application-/tools/khutwa-work/video/fr.js']+ids,cwd=W,env=env,capture_output=True,text=True).stdout.strip())
ims=[Image.open(W+'g_A8_%s.png'%i) for i in ids];cols=3;w,h=ims[0].size;s=0.5;w2,h2=int(w*s),int(h*s);rows=(len(ims)+cols-1)//cols
sh=Image.new('RGB',(w2*cols,h2*rows),'white')
for k,im in enumerate(ims): sh.paste(im.resize((w2,h2)),((k%cols)*w2,(k//cols)*h2))
sh.save(W+name+'.png');print(sh.size)
