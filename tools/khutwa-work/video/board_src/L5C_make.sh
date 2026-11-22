#!/bin/bash
# usage: L5C_make.sh  → build + word check + gaps
cd /home/claude/out/tools && python3 L5C_build.py && python3 L5C_chk.py
export BOARD=/home/claude/out/khutwa_hist_board_L5C.html NODE_PATH=$(npm root -g)
cd /home/claude/out/L5C_work && node /home/claude/out/tools/L5C_err.js && node /home/claude/secondary-application-/tools/khutwa-work/video/gaps.js 3.2
