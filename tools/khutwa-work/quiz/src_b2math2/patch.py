# helper: patch(ch, question-prefix, old, new) replaces text inside one question tuple (question line + next line)
import sys
def run(ch, edits):
    p=f'/home/claude/khutwa/quiz/src_b2math2/ch{ch}.py'; L=open(p).read().split('\n')
    for qp,old,new in edits:
        idx=[i for i,l in enumerate(L) if l.startswith('("'+qp)]
        assert len(idx)==1,(qp,len(idx))
        i=idx[0]; blk=L[i]+'\n'+L[i+1]
        assert blk.count(old)>=1,(qp,old)
        if blk.count(old)>1: print('multi',qp,old)
        blk=blk.replace(old,new,1) if not old.startswith('ALL:') else blk
        L[i],L[i+1]=blk.split('\n')
    open(p,'w').write('\n'.join(L))
