#!/bin/bash
V=/home/claude/secondary-application-/tools/khutwa-work/video
F=/home/claude/out/khutwa_hist_board_A45.html
cd /home/claude/out/tools && python3 A45_v8_build.py && python3 $V/inject_lrec.py $F
export BOARD=$F NODE_PATH=$(npm root -g)
mkdir -p /home/claude/out/A45_v8_work && cd /home/claude/out/A45_v8_work && node $V/gaps.js 3.2
