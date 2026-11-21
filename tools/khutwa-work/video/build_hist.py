import json,re
src=open('addvalue_studio.html',encoding='utf8').read().split('\n')
md=open('/home/claude/khutwa/video/hist_u1l1_script_v3.md',encoding='utf8').read().split('\n')
end=next(i for i,l in enumerate(md) if l.startswith('## إزاي اتطبقت'))
EP=[];ep=seg=None
for l in md[282:end]:
    m=re.match(r'# الفصل (\d) — «(.+?)»',l)
    if m:
        ep={'n':int(m[1]),'s':1,'k':int(m[1]),'title':m[2],'status':'السكريبت v3 — مستني تسجيل صوتك','segs':[]};EP.append(ep);continue
    m=re.match(r'## ([A-D]\d) — (.+)',l)
    if m:
        seg={'slide':m[1],'title':re.sub(r'\s*— السبورة.*$','',m[2]).strip(),'lines':[]};ep['segs'].append(seg);continue
    m=re.match(r'\| ([A-D]\d\.\d+) \|',l)
    if m and seg is not None:
        c=[x.strip() for x in l.strip().strip('|').split(' | ')]
        if len(c)<6: c=[x.strip() for x in l.strip().strip('|').split('|')]
        rid,t,en,board,summ,srcp=c[0],c[1],c[2],c[3],c[4],c[5]
        t=t.replace('[نَفَس]','[[0.5]]'); t=re.sub(r'\[وقفة ثانية\]','[[1.0]]',t); t=re.sub(r'\[وقفة ثانيتين\]','[[2.0]]',t); t=re.sub(r'\[وقفة (\d) ثواني\]',r'[[\1.0]]',t)
        tones=[]
        if 'وقّف' in t and 'فكّر' in t: tones.append('وقفة تفكير')
        elif '؟' in t: tones.append('سؤال')
        if 'بالبلدي' in t: tones.append('شرح بالبلدي')
        if t.startswith('«'): tones.append('مصطلح')
        board=board.replace('**','')
        scr=board+('' if summ in ('—','') else ' ｜ ملخص الشريحة: '+summ.lstrip('• '))
        seg['lines'].append({'t':t,'style':rid+' · '+srcp+' · EN: '+en,'screen':scr,'arrow':'','tones':tones,'vt':None})
D={'EP':EP,'SERIES':{'1':'تاريخ تانية بكالوريا · و1 د1: بناء الدولة المصرية'}}
print([(e['k'],e['title'],[(s['slide'],len(s['lines'])) for s in e['segs']]) for e in EP]); print('lines',sum(len(s['lines']) for e in EP for s in e['segs']))
left=[l for e in EP for s in e['segs'] for x in s['lines'] for l in re.findall(r'\[[^\[\]]*\]',re.sub(r'\[\[[\d.]+\]\]','',x['t']))]; print('leftover brackets',set(left))
out=[]
for i,l in enumerate(src):
    if i==98: l='<script id="data" type="application/json">'+json.dumps(D,ensure_ascii=False).replace('</','<\\/')+'</script>'
    else:
        l=l.replace('استوديو Add Value','استوديو خُطوة').replace('Add Value','خُطوة').replace('av3_','kh1_').replace('#AVSYNC','#KHSYNC').replace('#AV ','#KH ').replace('let cur=6,','let cur=1,').replace('الأداء: ','')
    out.append(l)
open('khutwa_history_studio.html','w',encoding='utf8').write('\n'.join(out)); print(len('\n'.join(out)))
