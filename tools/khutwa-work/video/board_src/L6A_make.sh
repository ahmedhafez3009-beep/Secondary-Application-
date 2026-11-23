#!/bin/bash
# usage: L6A_make.sh  → build + word check + gaps
cd /home/claude/out/tools && python3 L6A_build.py && python3 L6A_chk.py
export BOARD=/home/claude/out/khutwa_hist_board_L6A.html NODE_PATH=$(npm root -g)
cd /home/claude/out/L6A_work && node /home/claude/out/tools/L6A_err.js && node /home/claude/secondary-application-/tools/khutwa-work/video/gaps.js 3.2
