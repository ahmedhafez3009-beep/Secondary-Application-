#!/bin/sh
# usage: save.sh <outname>  — decodes newest browser tool result into ocr/<outname>.txt
f=$(ls -t /tmp/claude-tool-results/*/*.txt | head -1)
python3 /home/claude/khutwa/ocr/dec.py "$f" /home/claude/khutwa/ocr/$1.txt
