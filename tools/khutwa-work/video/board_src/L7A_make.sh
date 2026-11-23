#!/bin/bash
# usage: L7A_make.sh  → build + word check + gaps
cd /home/claude/out/tools && python3 L7A_build.py && python3 L7A_chk.py
export BOARD=/home/claude/out/khutwa_hist_board_L7A.html NODE_PATH=$(npm root -g)
cd /home/claude/out/L7A_work && node /home/claude/out/tools/L7A_err.js && node /home/claude/secondary-application-/tools/khutwa-work/video/gaps.js 3.2
