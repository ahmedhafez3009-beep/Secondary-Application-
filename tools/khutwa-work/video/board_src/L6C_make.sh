#!/bin/bash
# usage: L6C_make.sh  → build + word check + gaps
cd /home/claude/out/tools && python3 L6C_build.py && python3 L6C_chk.py
export BOARD=/home/claude/out/khutwa_hist_board_L6C.html NODE_PATH=$(npm root -g)
cd /home/claude/out/L6C_work && node /home/claude/out/tools/L6C_err.js && node /home/claude/secondary-application-/tools/khutwa-work/video/gaps.js 3.2
