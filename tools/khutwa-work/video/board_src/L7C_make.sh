#!/bin/bash
# usage: L7C_make.sh  → build + word check + gaps
cd /home/claude/out/tools && python3 L7C_build.py && python3 L7C_chk.py
export BOARD=/home/claude/out/khutwa_hist_board_L7C.html NODE_PATH=$(npm root -g)
cd /home/claude/out/L7C_work && node /home/claude/out/tools/L7C_err.js && node /home/claude/secondary-application-/tools/khutwa-work/video/gaps.js 3.2
