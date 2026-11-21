#!/bin/sh
cd /home/claude/secondary-application-/tools/khutwa-work/video/board_src
cat $(ls L2A_p[0-9].js) > L2A_content.js && python3 L2A_build.py
