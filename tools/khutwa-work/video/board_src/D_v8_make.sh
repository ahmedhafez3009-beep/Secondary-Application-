#!/bin/bash
V=/home/claude/secondary-application-/tools/khutwa-work/video
cd /home/claude/out/tools && python3 D_v8_build.py || exit 1
export NODE_PATH=$(npm root -g)
mkdir -p /home/claude/out/D_v8_work && cd /home/claude/out/D_v8_work
for F in /home/claude/out/khutwa_hist_board_D.html /home/claude/out/khutwa_hist_board_D2.html; do
 [ -f "$F" ] || continue; [ "$F" -nt /home/claude/out/tools/D_v8_build.py ] || true
 python3 $V/inject_lrec.py $F; BOARD=$F node /home/claude/out/tools/L5C_err.js; BOARD=$F node $V/gaps.js 3.2
done
