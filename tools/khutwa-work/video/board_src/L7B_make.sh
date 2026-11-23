#!/bin/bash
# usage: L7B_make.sh  → build + word check + gaps
cd /home/claude/out/tools && python3 L7B_build.py && python3 L7B_chk.py
export BOARD=/home/claude/out/khutwa_hist_board_L7B.html NODE_PATH=$(npm root -g)
cd /home/claude/out/L7B_work && node /home/claude/out/tools/L7B_err.js && node /home/claude/secondary-application-/tools/khutwa-work/video/gaps.js 3.2
