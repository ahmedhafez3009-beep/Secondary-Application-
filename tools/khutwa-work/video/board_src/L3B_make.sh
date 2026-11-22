#!/bin/bash
# usage: L3B_make.sh  → build + word check + gaps
cd /home/claude/out/tools && python3 L3B_build.py && python3 L3B_chk.py
export BOARD=/home/claude/out/khutwa_hist_board_L3B.html NODE_PATH=$(npm root -g)
cd /home/claude/out/L3B_work && node /home/claude/out/tools/L3B_err.js && node /home/claude/secondary-application-/tools/khutwa-work/video/gaps.js 3.2
