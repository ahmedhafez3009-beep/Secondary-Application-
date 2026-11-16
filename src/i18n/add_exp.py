"""Add English-medium (experimental school) Math/Science subjects to data.js as <key>X, from notes_exp.md."""
import re, json, os
here = os.path.dirname(os.path.abspath(__file__)); DJ = os.path.join(here, '..', 'data.js')
MAP = {'p1 math':'p1math','p1 science':'p1sci','p2 math':'p2math','p2 science':'p2sci','p3 math':'p3math','p3 science':'p3sci',
 'e1 math':'e1math','e2 math':'e2math','e3 math':'e3math','e4 math':'e4math','e4 science':'e4sci','e5 math':'e5math','e5 science':'e5sci',
 'e6 math':'e6math','e6 science':'e6sci','a1 math':'a1math','a1 science':'a1sci',
 'g2 chemistry':'g2chem','g2 physics':'g2phys','g2 pure math':'g2math','g2 general math':'g2gmath','g3 chemistry':'g3chem','g3 physics':'g3phys','g3 biology':'g3bio','g3 pure math':'g3pmath','g3 applied math':'g3amath'}
NAME = {'math':'Mathematics','sci':'Science','chem':'Chemistry','phys':'Physics','bio':'Biology','gmath':'General Mathematics','pmath':'Pure Mathematics','amath':'Applied Mathematics'}
secs = {}; cur = None
for line in open(os.path.join(here,'notes_exp.md'), encoding='utf8'):
    line = line.rstrip('\n')
    m = re.match(r'## (\S+ [a-z ]+?)(?: \(|$)', line)
    if m: cur = m.group(1).strip(); secs[cur] = []; continue
    if cur is None or not line.strip(): continue
    if line.startswith('CH:'): secs[cur].append(['Term 1 chapters', line[3:].strip()]); continue
    m = re.match(r'U(\d+) (.+?): (.+)$', line)
    if m: secs[cur].append(['Unit %s: %s' % (m.group(1), m.group(2)), m.group(3).strip()])
t = open(DJ, encoding='utf8').read()
a = t.index('var CURR = ')+11; b = t.index('var STAGES'); C = json.loads(t[a:b].strip().rstrip(';'))
for k in [k for k in C if k.endswith('X')]: del C[k]
n = 0
for sec, units in secs.items():
    base = MAP.get(sec)
    if not base or base not in C or not units: continue
    src = C[base]; suf = re.sub(r'^[a-z]\d', '', base)
    parts = [[p[0], []] for p in src['parts']]; parts[0][1] = units
    d = {'name': NAME.get(suf, src['name']), 'icon': src['icon'], 'color': src['color']}
    if len(parts) > 1: d['note'] = 'وحدات الترم التاني ضيفيها أول ما تبدأ.'
    d['parts'] = parts; d['lang'] = 'en'; C[base+'X'] = d; n += 1
t = t[:a] + json.dumps(C, ensure_ascii=False) + ';\n' + t[b:]
t = re.sub(r'var CURR_VERSION = \d+;', lambda m: 'var CURR_VERSION = %d;' % (int(re.search(r'\d+', m.group(0)).group(0)) + 0), t)
open(DJ, 'w', encoding='utf8').write(t); print('added', n, sorted(k for k in C if k.endswith('X')))
