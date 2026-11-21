// «خُطوة» — قارئ كتب البكالوريا في المتصفح المدمج (لصق على مراحل في javascript_tool)
// افتح التاب على: https://egyptianbaccalaureate.blob.core.windows.net/egyptianbaccalaureate/x404
// (1) المكتبات — الصفحة XML، فالسكربت بيتحمّل بـ fetch+eval
window.pdfjsLib = await import('https://cdn.jsdelivr.net/npm/pdfjs-dist@4.0.379/build/pdf.min.mjs');
(0,eval)(await (await fetch('https://cdn.jsdelivr.net/npm/tesseract.js@5.1.1/dist/tesseract.min.js')).text());
window.WURL = URL.createObjectURL(new Blob([await (await fetch('https://cdn.jsdelivr.net/npm/pdfjs-dist@4.0.379/build/pdf.worker.min.mjs')).text()],{type:'text/javascript'}));
// (2) الدوال
window.HD=document.implementation.createHTMLDocument('x');
window.BASE='https://egyptianbaccalaureate.blob.core.windows.net/egyptianbaccalaureate/';
window.OCR={}; window.OST={}; window.DONE={}; window.LOG=[]; window.DOCS={};
window.TO=(p,ms)=>Promise.race([p,new Promise((_,j)=>setTimeout(()=>j('timeout'),ms))]);
window.openDoc=async(k,p)=>{ const w=new pdfjsLib.PDFWorker({port:new Worker(WURL,{type:'module'})}); DOCS[k]=await pdfjsLib.getDocument({url:BASE+p, worker:w, ownerDocument:HD, isEvalSupported:false, disableFontFace:true}).promise; return DOCS[k]; };
window.render=async(k,i,scale)=>{ const pg=await DOCS[k].getPage(i); const vp=pg.getViewport({scale}); const c=HD.createElement('canvas'); c.width=vp.width|0; c.height=vp.height|0; const ctx=c.getContext('2d'); ctx.fillStyle='#fff'; ctx.fillRect(0,0,c.width,c.height); await TO(pg.render({canvasContext:ctx, viewport:vp, intent:'print'}).promise,120000); pg.cleanup(); return c; };
window.WS=[]; for(let i=0;i<3;i++) WS.push(await Tesseract.createWorker(['ara','eng'],1));
window.ocrOne=async(W,k,i)=>{ try{ const c=await render(k,i,2.2); const {data}=await TO(W.recognize(c),180000); c.width=c.height=0; return data.text; }catch(e){ return 'ERR '+e; } };
window.processBook=async(k,p)=>{ try{ await TO(openDoc(k,p),300000); }catch(e){ LOG.push(k+' open fail '+e); return; } const n=DOCS[k].numPages; OCR[k]={}; OST[k]={done:0,total:n,err:0}; let next=1; await Promise.all(WS.map(async W=>{ while(next<=n){ const i=next++; const t=await ocrOne(W,k,i); OCR[k][i]=t; if(t.startsWith('ERR')) OST[k].err++; OST[k].done++; } })); DONE[k]=1; try{ await TO(DOCS[k].destroy(),5000);}catch(e){} delete DOCS[k]; };
window.tlBook=async(k,p)=>{ const key='tl_'+k; await openDoc(key,p); const n=DOCS[key].numPages; OCR[key]={}; OST[key]={done:0,total:n}; for(let i=1;i<=n;i++){ const pg=await DOCS[key].getPage(i); const tc=await pg.getTextContent(); let s='',ly=null; for(const it of tc.items){ const y=Math.round(it.transform[5]); if(ly!==null&&Math.abs(y-ly)>3) s+='\n'; s+=it.str+' '; ly=y; } OCR[key][i]=s; OST[key].done++; } await DOCS[key].destroy(); delete DOCS[key]; };
window.gzsave=async(k)=>{ const n=OST[k].total; let s=''; for(let i=1;i<=n;i++) s+='=== p'+i+'\n'+(OCR[k][i]||'')+'\n'; const buf=new Uint8Array(await new Response(new Blob([s]).stream().pipeThrough(new CompressionStream('gzip'))).arrayBuffer()); let b=''; for(let i=0;i<buf.length;i+=32768) b+=String.fromCharCode.apply(null,buf.subarray(i,i+32768)); return ('GZB64:'+btoa(b)+':END').padEnd(320000,' '); };
window.BOOKS=[['ma1','Mathematics-Ar-EB-Part1.pdf'],['ma2','Mathematics-Ar-EB-Part2.pdf'],['pr1','Programming-ArtificialIntelligence-Ar-EB-part1.pdf'],['pr2','Programming-ArtificialIntelligence-Ar-EB-part2.pdf'],['ac1','Accuonting-Ar-EB-Part1.pdf'],['ac2','Accuonting-Ar-EB-Part2.pdf'],['bz1','Business-AR-EB-Part1.pdf'],['bz2','Business-AR-EB-Part2.pdf'],['ps1','Psychology-EB-part1.pdf'],['ps2','Psychology-EB-part2.pdf'],['sar','Story-Ar-EB.pdf'],['sen','Story-En-EB-L1.pdf'],['ch1','Chemistry-Ar-EB-part1.pdf'],['ch2','Chemistry-Ar-EB-part2.pdf']];
window.runAll=async()=>{ while(BOOKS.length){ const [k,p]=BOOKS.shift(); await processBook(k,p); } LOG.push('ALL DONE'); };
// (3) runAll(); ثم تابع OST. لما كتاب يخلص: await gzsave('k') → الناتج بيتحفظ في ملف → python3 dec.py <file> <out.txt>
// للمواد الحسابية كمان: await tlBook('k','file.pdf'); await gzsave('tl_k')
