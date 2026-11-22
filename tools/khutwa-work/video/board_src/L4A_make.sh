#!/bin/bash
# usage: L4A_make.sh  → build + word check + gaps
cd /home/claude/out/tools && python3 L4A_build.py && python3 L4A_chk.py
export BOARD=/home/claude/out/khutwa_hist_board_L4A.html NODE_PATH=$(npm root -g)
cd /home/claude/out/L4A_work && node /home/claude/out/tools/L4A_err.js && node /home/claude/secondary-application-/tools/khutwa-work/video/gaps.js 3.2
