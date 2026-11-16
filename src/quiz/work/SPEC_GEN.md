# Quiz-writing spec for «خُطوة» (Egyptian secondary, ministry books 2026/2027)

Source: an OCR/text dump of the ministry student book, split by "=== pN" page markers (pN = PDF page).
OCR quality: prose mostly readable (some letters swapped, e.g. ت/ن, ق/ف, ى/ي); numbers, formulas, tables and maps are often garbled.

Write multiple-choice questions for each lesson listed for you. First locate each lesson's pages in the dump (search for its heading/keywords), then write from those pages only.
1. Every question must be answerable from what the book itself teaches in those pages. Use only readable prose. If a date/number/name is garbled, use it only if you are certain of the correct value AND it fits the surrounding readable text; otherwise skip that fact.
2. 6 questions per lesson (minimum 5). Mix: definitions/concepts, causes/results (علل/ما نتيجة), comparisons, ordering, applying a rule; calculations only if the book shows that type (exact numbers; check arithmetic yourself, step by step).
3. Each question: exactly 4 options, one correct. Distractors plausible but clearly wrong per the book. No "all/none of the above". Options short.
4. Language: the book's language (Arabic subjects: clear Modern Standard Arabic as in Egyptian exam papers, using the book's terms; English subjects: simple correct English as in the book). Math/science symbols in Latin letters with plain digits (x^2, sqrt(x), 3/4, Fe2O3); no LaTeX, no special subscript characters.
5. Explanation "e": one short sentence (≤ 25 words) saying why the answer is right, as the book states it.
6. Write original questions. Do not copy the book's exercise questions verbatim.
7. Do not invent facts that are not in the book, even if true elsewhere. Stay neutral on religion/politics: state only what the book states.
8. Vary the position of the correct answer (roughly equal use of 0-3).

Output: a JSON file (UTF-8) of this exact shape — keys must match the lesson names EXACTLY as given (copy-paste them):
{"by": {"<lesson name>": [{"q": "...", "o": ["...","...","...","..."], "a": 0, "e": "..."}]}}
"a" is the 0-based index of the correct option.
Validate with: python3 -c "import json;d=json.load(open('FILE'));print({k:len(v) for k,v in d['by'].items()})"
