# Fact-check spec for «خُطوة» quizzes
You get a quiz JSON {"by":{lesson:[{q,o,a,e}]}} and the book dump it was written from ("=== pN" markers).
For EVERY question:
1. Find the supporting text in the book dump (the lesson's pages). The marked answer must be exactly what the book says; the other three options must be wrong per the book (not also arguably correct).
2. Check names, dates, numbers, terms against readable book text; recompute any arithmetic step by step.
3. Check language: correct, clear, no typos; options short and parallel; "e" ≤ 25 words and true.
4. Fix what can be fixed (reword, change a distractor, change "a"). DROP a question if the book does not clearly support it. Keep ≥5 questions per lesson; if a lesson falls below 5, write replacement questions strictly from the book.
5. Do not change lesson keys.
Write the corrected file to the output path given, validate it with python json, and reply with: total questions in/out, number fixed, number dropped, number added, and a short list (max 10 lines) of the most important fixes.
