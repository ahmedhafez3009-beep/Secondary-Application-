import sys,json,re,base64,zlib
src,dst=sys.argv[1],sys.argv[2]
t=open(src).read()
try: t=json.loads(t)[0]['text']
except Exception: pass
m=re.search(r'GZB64:([A-Za-z0-9+/=\\n]+?):END',t)
b=m.group(1).replace('\\n','')
d=zlib.decompressobj(31).decompress(base64.b64decode(b)).decode('utf8')
open(dst,'w').write(d); print(dst,len(d),d.count('=== p'),d.count('ERR '))
