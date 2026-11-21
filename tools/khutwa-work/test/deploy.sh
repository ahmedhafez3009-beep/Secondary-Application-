#!/bin/sh
# usage: deploy.sh "commit message"
set -e
R=/home/claude/secondary-application-; S=$R/src/site
cp $S/app/index.html $S/app/sw.js $S/app/curriculum.json $S/app/curriculum2.json $S/app/version.json $R/app/
mkdir -p $R/app/quiz && cp $S/app/quiz/*.json $R/app/quiz/
cp $S/index.html $S/report.html $S/story.html $R/
cd $R && git add -A && git commit -qm "$1

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01WsJEfSAo7hbjLUWMryTEGq"
git -c push.negotiate=true push -q origin main main:gh-pages 2>&1 | grep -v "moved\|new location\|^remote: *$" || true
git log --oneline -1
