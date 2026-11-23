#!/bin/bash
# usage: L6D_make.sh  → build + word check + err + gaps
cd /home/claude/out/tools && python3 L6D_build.py && python3 /home/claude/secondary-application-/tools/khutwa-work/video/inject_lrec.py /home/claude/out/khutwa_hist_board_L6D.html && python3 L6D_chk.py
export BOARD=/home/claude/out/khutwa_hist_board_L6D.html NODE_PATH=$(npm root -g)
cd /home/claude/out/L6D_work && node /home/claude/out/tools/L6D_err.js && node /home/claude/secondary-application-/tools/khutwa-work/video/gaps.js 3.2
