#!/bin/bash
# build + lrec + page errors + gaps
V=/home/claude/secondary-application-/tools/khutwa-work/video
cd /home/claude/out/tools && python3 A_v8_build.py && python3 $V/inject_lrec.py /home/claude/out/khutwa_hist_board_A.html
export BOARD=/home/claude/out/khutwa_hist_board_A.html NODE_PATH=$(npm root -g)
mkdir -p /home/claude/out/A_v8_work && cd /home/claude/out/A_v8_work && node /home/claude/out/tools/L5C_err.js && node $V/gaps.js 3.2
