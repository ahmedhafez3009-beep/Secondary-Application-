cd /home/claude/montage
declare -A N=([01]="يعني_إيه_دولة" [02]="حدود_مصر_وملخص_الفصل1" [03]="السلطة_والسيادة" [04]="ليه_مصر_قامت_واستمرت" [05]="حل_أسئلة_الكتاب_ص18-19" [06]="حل_أسئلة_الكتاب_ص20_والمراجعة")
for k in 01 02 03 04 05 06; do
 [ -f /home/claude/final/done_$k ] && continue
 NODE_PATH=$(npm root -g) python3 montage.py cfg/d1_$k.json > log_$k.txt 2>&1 || { echo FAIL $k >> run.log; continue; }
 ffmpeg -v error -y -i d1_${k}_final.mp4 -i /home/claude/thumb/thumb_d1_$k.jpg -map 0 -map 1 -c copy -disposition:v:1 attached_pic -movflags +faststart "/home/claude/final/تاريخ2ث_د1_${k}_${N[$k]}.mp4" >> log_$k.txt 2>&1
 cp d1_${k}_final_chapters.txt "/home/claude/final/فصول_د1_${k}.txt"; touch /home/claude/final/done_$k; echo OK $k >> run.log
done
echo ALL >> run.log
