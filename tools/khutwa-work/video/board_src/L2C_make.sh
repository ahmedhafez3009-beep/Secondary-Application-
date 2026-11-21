#!/bin/bash
# usage: L2C_make.sh  → build + word check + gaps
cd /home/claude/out/tools && python3 L2C_build.py && python3 L2C_chk.py
export BOARD=/home/claude/out/khutwa_hist_board_L2C.html NODE_PATH=$(npm root -g)
cd /home/claude/out/L2C_work && node /home/claude/out/tools/L2C_err.js && node /home/claude/secondary-application-/tools/khutwa-work/video/gaps.js 3.2
