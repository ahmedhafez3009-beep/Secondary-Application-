#!/bin/sh
# يجمّع أجزاء السبورة C ويبني الملف: sh tools/C_make.sh
cd /home/claude/out/tools && cat C_p0.js C_p1.js C_p2.js C_p3.js C_p4.js C_p5.js > C_content.js && python3 C_build.py
