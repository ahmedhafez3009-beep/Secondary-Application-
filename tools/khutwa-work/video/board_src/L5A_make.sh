#!/bin/bash
# usage: L5A_make.sh  → build + word check + gaps
cd /home/claude/out/tools && python3 L5A_build.py && python3 L5A_chk.py
export BOARD=/home/claude/out/khutwa_hist_board_L5A.html NODE_PATH=$(npm root -g)
cd /home/claude/out/L5A_work && node /home/claude/out/tools/L5A_err.js && node /home/claude/secondary-application-/tools/khutwa-work/video/gaps.js 3.2
