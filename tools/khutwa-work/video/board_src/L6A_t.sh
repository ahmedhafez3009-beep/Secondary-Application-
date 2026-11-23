#!/bin/bash
# usage: L4C_t.sh sheetname id...   → tb(bad/ov) + txt + sheet
cd /home/claude/out/L6A_work && export BOARD=/home/claude/out/khutwa_hist_board_L6A.html TAG=L6A_ NODE_PATH=$(npm root -g)
V=/home/claude/secondary-application-/tools/khutwa-work/video
node $V/tb.js | python3 -c "
import sys,json
l=sys.stdin.read().splitlines();d=json.loads(l[0]);print('bad',d['bad']);print('ov',d['ov']);print(l[-1])"
node ../tools/L6A_txt.js
n=$1;shift;[ -n "$1" ] && python3 ../tools/L6A_sheet.py $n "$@"
