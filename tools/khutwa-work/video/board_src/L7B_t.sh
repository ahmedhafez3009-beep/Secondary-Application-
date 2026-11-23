#!/bin/bash
# usage: L7B_t.sh sheetname id...   → tb(bad/ov) + txt + sheet
cd /home/claude/out/L7B_work && export BOARD=/home/claude/out/khutwa_hist_board_L7B.html TAG=L7B_ NODE_PATH=$(npm root -g)
V=/home/claude/secondary-application-/tools/khutwa-work/video
node $V/tb.js | python3 -c "
import sys,json
l=sys.stdin.read().splitlines();d=json.loads(l[0]);print('bad',d['bad']);print('ov',d['ov']);print(l[-1])"
node ../tools/L7B_txt.js
n=$1;shift;[ -n "$1" ] && python3 ../tools/L7B_sheet.py $n "$@"
