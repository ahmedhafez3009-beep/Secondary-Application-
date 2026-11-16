# Exam-style review for «خُطوة» Baccalaureate quizzes

Input: a quiz JSON {"by":{lesson:[{q,o,a,e}]}}, the book dump it came from ("=== pN" markers), and /home/claude/khutwa/quiz/exam_style.md (what the ministry's Baccalaureate exams and sample papers ask, per subject).

Goal: make each lesson's questions look like what the student will meet in the exam, without leaving the book.

For each lesson:
1. Classify every question as recall (حفظ), understanding (فهم), or application/thinking (تطبيق/تفكير).
2. Target per lesson of 6: about 2 recall, 2 understanding, 2 application/thinking (at least 1 application). Use the exam_style.md question forms for the subject (e.g. "علل", "ماذا يحدث لو", a short given situation, a small calculation, a data/graph statement in words, choose the incorrect statement, sentence completion in English, etc.), as long as they work as 4-option multiple choice.
3. Rewrite or replace questions to reach the target. Every fact, rule, number and answer must come from the book dump or be standard, certain subject knowledge that the book's lesson teaches. Never invent data the book does not support.
4. Keep the existing rules: 4 distinct options, short and parallel; the correct option is never the longest; exactly one option correct (no arguable distractors); "e" ≤ 25 words, explaining why the answer is right and, where useful, why the tempting wrong one is wrong. Spread "a" across 0–3.
5. Mark every question you added or changed with "chg": true. Leave untouched questions without it. Do not change lesson keys. Keep ≥6 questions per lesson.

Write the result to the output path given, validate with python json, and reply with: per-lesson mix before → after (totals only), number changed/added, and up to 8 lines of examples of the new exam-style questions.
