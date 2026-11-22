#!/bin/bash
# usage: L5B_make.sh  → build + word check + gaps
cd /home/claude/out/tools && python3 L5B_build.py && python3 L5B_chk.py
export BOARD=/home/claude/out/khutwa_hist_board_L5B.html NODE_PATH=$(npm root -g)
cd /home/claude/out/L5B_work && node /home/claude/out/tools/L5B_err.js && node /home/claude/secondary-application-/tools/khutwa-work/video/gaps.js 3.2
