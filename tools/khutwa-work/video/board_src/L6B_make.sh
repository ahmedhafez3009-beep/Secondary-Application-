#!/bin/bash
# usage: L6B_make.sh  → build + word check + gaps
cd /home/claude/out/tools && python3 L6B_build.py && python3 L6B_chk.py
export BOARD=/home/claude/out/khutwa_hist_board_L6B.html NODE_PATH=$(npm root -g)
cd /home/claude/out/L6B_work && node /home/claude/out/tools/L6B_err.js && node /home/claude/secondary-application-/tools/khutwa-work/video/gaps.js 3.2
