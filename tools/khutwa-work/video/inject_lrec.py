# يحط استوديو «جملة جملة» (lrec.js) في سبورة أو أكتر: python3 inject_lrec.py file1.html file2.html ...
import sys,re,os
js=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'lrec.js'),encoding='utf8').read()
blk0='<script id="lrec">\n'+js+'\n</script>'
for f in sys.argv[1:]:
    s=open(f,encoding='utf8').read()
    s=re.sub(r'<script id="lrec(Data)?"[^>]*>.*?</script>','',s,flags=re.S)
    m=re.search(r'khutwa_hist_board_(\w+)\.html',f);rp=os.path.join(os.path.dirname(os.path.abspath(__file__)),'rec',(m.group(1) if m else '')+'.json')
    blk=(('<script id="lrecData" type="application/json">'+open(rp,encoding='utf8').read().replace('</','<\\/')+'</script>') if m and os.path.exists(rp) else '')+blk0
    i=s.rindex('</body>'); s=s[:i]+blk+s[i:]
    open(f,'w',encoding='utf8').write(s); print('ok',os.path.basename(f))
