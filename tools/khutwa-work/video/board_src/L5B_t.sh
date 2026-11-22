#!/bin/bash
# usage: L5B_t.sh sheetname id...   → tb(bad/ov) + txt + sheet
cd /home/claude/out/L5B_work && export BOARD=/home/claude/out/khutwa_hist_board_L5B.html TAG=B5_ NODE_PATH=$(npm root -g)
V=/home/claude/secondary-application-/tools/khutwa-work/video
node $V/tb.js | python3 -c "
import sys,json
l=sys.stdin.read().splitlines();d=json.loads(l[0]);print('bad',d['bad']);print('ov',d['ov']);print(l[-1])"
node ../tools/L5B_txt.js
n=$1;shift;[ -n "$1" ] && python3 ../tools/L5B_sheet.py $n "$@"
