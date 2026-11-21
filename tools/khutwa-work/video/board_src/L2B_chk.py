import re,json,subprocess,sys
sys.argv=['x','x']
exec(open('/home/claude/out/tools/L2B_build.py').read().split("if len(sys.argv)>1")[0])
txt=''.join(open('/home/claude/out/tools/L2B_p%d.js'%i,encoding='utf-8').read() for i in range(1,5))
# split by L('id'
parts=re.split(r"\bL\('([^']+)',",txt)
bad=0
for i in range(1,len(parts),2):
    id=parts[i];body=parts[i+1]
    nxt=re.search(r"\nL\('|\ngo\(|\nslide\(",body)
    toks=[t for t in re.sub(r'\[\[[\d.]+\]\]','',S[id]).split()]
    for m in re.finditer(r"at\('([^']+)'(?:,(\d+))?\)",body):
        sub,n=m.group(1),int(m.group(2) or 0)
        c=sum(1 for t in toks if sub in t)
        if c<=n: print(id,'MISSING',sub,n,'| toks:',' '.join(toks)[:160]);bad+=1
    for m in re.finditer(r"atp\((\d*)\)",body):
        pz=len(re.findall(r'\[\[',S[id]))
        if pz<=int(m.group(1) or 0): print(id,'no pause');bad+=1
print('bad',bad)
