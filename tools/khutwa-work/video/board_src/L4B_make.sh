#!/bin/bash
# usage: L4B_make.sh  → build + word check + gaps
cd /home/claude/out/tools && python3 L4B_build.py && python3 L4B_chk.py
export BOARD=/home/claude/out/khutwa_hist_board_L4B.html NODE_PATH=$(npm root -g)
cd /home/claude/out/L4B_work && node /home/claude/out/tools/L4B_err.js && node /home/claude/secondary-application-/tools/khutwa-work/video/gaps.js 3.2
