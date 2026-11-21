# Second foreign language (Baccalaureate grade 2) — curriculum + quiz
Source: book text dump (PDF text layer). Page markers "=== pNNNN": first digit = book part (1 = الجزء الأول / term 1, 2 = الجزء الثاني / term 2), remaining digits = PDF page number.
Step 1 — Curriculum: from each part's table of contents (sommaire / Inhalt) and unit openers, write the units and lessons exactly as the book names them (in the book's language; keep it short; a unit name like "Unité 1 : <title>" / "Lektion 1: <title>", lessons as the book divides each unit, e.g. its leçons/sections). Write /home/claude/khutwa/quiz/<OUT>_curr.json:
{"parts":[["الجزء الأول",[["<unit name>","<lesson>|<lesson>|..."],...]],["الجزء الثاني",[...]]]}
Lesson names must be unique within the subject.
Step 2 — Quiz: 6 questions per lesson (minimum 5) following /home/claude/khutwa/quiz/SPEC_GEN.md, written in the book's language at the book's level (beginner/A1-A2: vocabulary, grammar points the lesson teaches, short comprehension of the lesson's texts/dialogues, civilisation facts the book states). Explanations ("e") in Arabic (short, Egyptian-exam style MSA) so students understand why. Only one option correct; correct option never the longest.
Step 3 — Full independent check pass per /home/claude/khutwa/quiz/CHECK.md (grammar of every option; facts per the book).
Write /home/claude/khutwa/quiz/<OUT>_quiz.json as {"by":{lesson:[...]}} with keys exactly the lesson names from step 1.
Reply with: the units/lessons list, per-lesson counts, check fixes.
