import re,sys
def wc(s):
    s=re.sub(r'\[\[[\d.]+\]\]','',s); s=re.sub(r'\[[^\]]*\]','',s)
    return len([w for w in s.split() if re.search(r'\w',w)])
def rows(path,spcol):
    out={}
    for l in open(path,encoding='utf8'):
        c=[x.strip() for x in l.split('|')]
        if len(c)>4 and re.match(r'^[A-D]\d\.\d+[a-z]?$',c[1]): out.setdefault(c[1],c)
    return out
v3=rows('/home/claude/khutwa/video/hist_u1l1_script_v3.md',2)
v5=rows('/home/claude/khutwa/video/hist_final_v5.md',2)
def board(i):
    return 'A45' if i[:2] in('A4','A5') else i[0] if i[0] in 'BCD' else None
tot={}
for k,c in v3.items():
    b=board(k)
    if b: tot.setdefault(b,[0,0,0,0,0])[0]+=wc(c[2])
for k,c in v5.items():
    b=board(k); t=tot[b]; t[1]+=wc(c[2]); t[2]+=1
    st=c[5]
    if st.startswith('جديد'): t[3]+=1
    elif st.startswith('معدّل'): t[4]+=1
    # verify
    if st.startswith('زي'):
        a=re.sub(r'\[[^\]]*\]|\[\[[\d.]+\]\]','',v3[k][2]).split(); b2=re.sub(r'\[\[[\d.]+\]\]','',c[2]).split()
        if a!=b2: print('DIFF',k,'\n ',v3[k][2],'\n ',c[2])
    if max(len(x.split()) for x in re.split(r'[.؟!:]|\[\[',c[2]))>18: print('LONG',k)
for k in v3:
    if board(k) and k not in v5: print('MISSING',k)
for b,t in tot.items(): print(b,'v3',t[0],'v5',t[1],'+',t[1]-t[0],'%.1f%%'%(100*(t[1]-t[0])/t[0]),'rows',t[2],'new',t[3],'mod',t[4])
# quotes check
import itertools
for k,c in v5.items():
    if k in v3:
        for q in re.findall(r'«[^»]*»',v3[k][2]):
            if q not in c[2]: print('QUOTE CHANGED',k,q)
