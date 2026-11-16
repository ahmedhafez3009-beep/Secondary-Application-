# Native-speaker language review (French / German quizzes)

Input: a quiz JSON {"by":{lesson:[{q,o,a,e}]}} for Egyptian Baccalaureate grade 2 learners (beginner level, about A1–A2), and the textbook dump it came from.

Act as a native-speaker teacher of the language. For EVERY question and option:
1. Spelling, accents/umlauts, capitalisation (German nouns), punctuation and spacing (French: space before ? ! : ;), articles and gender, agreement, verb forms, word order (German V2 / verb-final in subordinate clauses), prepositions and cases.
2. Exactly one option is correct. Reject any distractor that a native speaker would also accept (e.g. two acceptable prepositions, both word orders possible, synonyms). Fix it by changing that distractor.
3. Wrong options must be wrong for a clear learner-level reason, not because of a typo or a rare rule.
4. Natural, idiomatic phrasing at the book's level; vocabulary the book uses. Keep content consistent with the book (names, dialogues).
5. "e" (explanation) stays short (≤ 25 words); it may be in Egyptian Arabic or the target language as the file already does; it must be correct.
6. Keep the correct option from being the longest. Do not change lesson keys. Keep ≥6 questions per lesson.

Mark every question you changed with "chg": true. Write the result to the output path given, validate with python json, and reply with: number checked, number changed, and up to 10 lines of the most important corrections (before → after).
