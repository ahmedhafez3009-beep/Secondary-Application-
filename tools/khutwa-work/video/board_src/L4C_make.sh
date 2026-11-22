#!/bin/bash
# usage: L4C_make.sh  → build + word check + gaps
cd /home/claude/out/tools && python3 L4C_build.py && python3 L4C_chk.py
export BOARD=/home/claude/out/khutwa_hist_board_L4C.html NODE_PATH=$(npm root -g)
cd /home/claude/out/L4C_work && node /home/claude/out/tools/L4C_err.js && node /home/claude/secondary-application-/tools/khutwa-work/video/gaps.js 3.2
