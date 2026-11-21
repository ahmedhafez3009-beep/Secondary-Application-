# Quiz-writing spec for «خُطوة» (Arabic ministry books 2026/2027; the subject and source file are given in your task)

Source: the OCR text file named in your task, split by "=== pN" page markers.
OCR quality: prose is mostly readable (some letters swapped, e.g. ت/ن, ق/ف); chemical formulas, equations and tables are often garbled.

Write multiple-choice questions for each lesson listed for you. Rules:
1. Every question must be answerable from what the book teaches in the pages given. Base facts on the readable prose. Where OCR of a formula/equation/number is garbled, only use it if you are certain of the standard value AND it is consistent with the surrounding readable text; otherwise skip that fact.
2. 6 questions per lesson (minimum 5). Mix: definitions/concepts, "علل/why" turned into MCQ, applying a rule, simple calculations only if the book shows that type (give exact numbers; check the arithmetic yourself).
3. Each question: exactly 4 options, one correct. Distractors must be plausible and clearly wrong per the book. No "all of the above"/"none of the above". Options short.
4. Language: clear Modern Standard Arabic as in Egyptian exam papers. Use the book terms. Formulas, symbols and units in Latin letters with plain digits (e.g. Fe2O3, V = IR, 5 Ω, 2 × 10^-3 T); no LaTeX, no subscript characters.
5. Explanation "e": one short sentence (≤ 25 words) saying why the answer is right, stated as the book states it.
6. Write original questions. Do not copy the book's exercise questions verbatim.
7. Do not invent facts that are not in the book, even if true elsewhere.

Output: a JSON file (UTF-8) of this exact shape — keys must match the lesson names EXACTLY as given:
{"by": {"<lesson name>": [{"q": "...", "o": ["...","...","...","..."], "a": 0, "e": "..."}]}}
"a" is the 0-based index of the correct option. Vary the position of the correct answer across questions.
Validate with: python3 -c "import json;d=json.load(open('FILE'));print({k:len(v) for k,v in d['by'].items()})"
