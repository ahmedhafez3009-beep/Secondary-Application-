#!/bin/bash
# usage: L3A_make.sh  → build + word check + gaps
cd /home/claude/out/tools && python3 L3A_build.py && python3 L3A_chk.py
export BOARD=/home/claude/out/khutwa_hist_board_L3A.html NODE_PATH=$(npm root -g)
cd /home/claude/out/L3A_work && node /home/claude/out/tools/L3A_err.js && node /home/claude/secondary-application-/tools/khutwa-work/video/gaps.js 3.2
