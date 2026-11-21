# Devil's-advocate review v2: hist_u1l1_script_v2.md

Checked against HIST_VIDEO_SPEC.md, my v1 notes (review_devil.md) and ocr/b2hi1.txt p6–p20, with hires_pages.txt used for p13.
Timings come from the script's own rate (0.65 s/word, running total, pauses not included). They match the header to within about 10 s.

**Verdict.** v2 applies the v1 fixes and the content is faithful to the book. The new risks come from the 3-sheet, 22-minute format:
- Sheet C is far too crowded to draw.
- The 22-card memory board can't be read on a phone.
- Chapter 3 doesn't stand alone.
- After 3:30 there are no real pauses.
- A few examples and recap phrasings will plant wrong answers. The worst is «25 غربًا» for the 25° E line, which the quiz tests directly.

---

## TOP 8 (fix before recording)

### 1. Recap wording turns the coordinates into wrong exam answers (A4.10 bullet, A5.4, C6.3, card 8)
- A4.7 and A4.10 say the lines correctly: «دائرة عرض 22 شمالًا» and «خط طول 25 شرقًا».
- Every later recap says it differently. A4.10's bullet reads «22° جنوبًا … 25° غربًا». A5.4 says «اتنين وعشرين جنوبًا … وخمسة وعشرين غربًا». C6.3 says «اتنين وعشرين جنوبًا وخمسة وعشرين غربًا».
- What the student remembers is «25 غربًا / 22 جنوبًا». Quiz question 4 is «خط طول 25 شرقًا». Recaps also drop the «دائرة عرض» vs «خط طول» distinction, which is a classic mix-up.
- **Fix:** every recap, bullet and card 8 should read «الجنوب: دائرة عرض 22° **شمالًا** (1899) · الغرب: خط طول 25° **شرقًا** (1925)». Spoken in A5.4/C6.3: «في الجنوب دائرة عرض اتنين وعشرين شمال، وفي الغرب خط طول خمسة وعشرين شرق». This adds about 4 words.

### 2. Sheet C can't be drawn legibly, and the memory board collides with the hero map (C1–C7)
- Element count by board (each icon, label, banner, arrow group and card counts as 1):

| Sheet | Boards | Elements | «احفظ دي» cards | Banners «نشاط» | Spoken time |
|---|---|---|---|---|---|
| A | A1–A5 | ~90 (A1 13, A2 20, A3 28, A4 30) | 10 | 7 | 7:20 |
| B | B1–B6 | ~45 | 6 | 4 | 5:00 |
| C | C1–C7 | **~115** (C1 8, C2 27, C3 25, C4 16, C5 18, C6 22 mini-cards, C7 4) | 6 + the 22-card board | **17** | 9:25 |

- C1.1 puts the hero map **in the centre** of C, and C1.3 hangs 6 boxes around it. Then C6.1 asks for «لوحة كبيرة في نص السبورة C». Both claim the centre.
- C7.1 also asks for a «لقطة سريعة لسهم ✓ بتاع السبورة A», which is a different sheet. It's unclear whether that means a cut to sheet A or a redraw.
- **Fix: split chapter 3 into two chapters, each on its own sheet.**
  - **Chapter 3 «مقومات الدولة المصرية»** (sheet C): C1–C3, 12:05→17:01, about 4:55, about 60 elements.
  - **Chapter 4 «ركن الامتحان + لوحة الحفظ»** (new sheet D): C4–C7, 17:01→end, about 4:30. The exam corner is the chapter students skip to the night before the exam, so it's the most natural standalone chapter. D gets the memory board in its centre, a ✓-arrow copy for C7, and the mini pillars icon and mini chair.
  - With this split the four chapters run 7:20 / 5:00 / 4:55 / 4:30.
- **Sheet A is also at its limit (~90 elements).** Recommended: also split chapter 1 at A4.1 (4:01). That gives 1a «الدولة والشعب» (4:01) and 1b «الحيز والحدود» (3:20), on sheets A and A′, with five chapters in total.
  - If chapter 1 stays whole, cut these drawings and keep the lines spoken only: A3.6 players, A4.1 pitch, A4.11 balcony, A4.14 drone. That's about 10 elements fewer.
  - In any case, write the A3.8–A3.12 roles on card 5 as 2–3 keywords each, not the full spoken sentence.
- **Cut drawing-only clutter on C** (no spoken change):
  - Use one «نشاط ص__» tag style, a small corner tab, instead of 17 full question banners. The long ones are C2.13 «كيف أسهمت الحاجة إلى التنظيم…» and B3.2 «ما العلاقة بين قوة المؤسسات…».
  - Drop the C3.10 wall (see #5).
  - Drop the C4.5 banner (see #6).

### 3. The 22-card memory board (C6) is illegible, unspoken in places, and too short to screenshot
- **Legibility arithmetic.** 22 cards in a 6×4 grid on a 1920×1080 frame gives about 280×200 px per card. Card 8 (4 borders plus 3 dates), card 12 (3 powers plus 4 articles) and card 5 (5 roles) each need about 6 lines. That forces handwriting around 22 px.
  - A phone shows the frame about 390 pt wide (×0.2), so 22 px becomes about 4–5 pt. It can't be read, and Arabic handwriting is worse than print at that size.
  - Card 1 (a 25-word definition) can't be shrunk to fit at all.
- **Timing.** C6.1–C6.6 is 54 words, about 35 s for 22 cards, or about 1.6 s per card. «صوّرها» only works if the full board holds still for several seconds, and nothing in the script provides that.
- **Unspoken lights.** C6.2 lights cards 1–5 but only says «4 أركان + مصدر السلطات», so the 5 roles light up silently. C6.5 lights cards 17–22 but never says Menes, the army's role or the identity measures.
- **Fix:**
  - Make the memory board **3 panels, one per part**: الدولة والحيز (cards 1–10), السلطة والسيادة (11–16), المقومات (17–22).
  - Each panel fills the frame with at most 8 cards in 2 columns × 4 rows, about 900×230 px each, with handwriting at 40 px or more.
  - **Keywords only, 8 words or fewer per card.** Examples: card 1 «الدولة = وحدة سياسية: حيز + شعب + سلطة + سيادة», card 12 «تشريعية (م101) · تنفيذية (م139، م163) · قضائية (م184)».
  - Hold each panel 5 s in silence with a «📸 وقّف وصوّر» tag: +15 s total. Put the same three panels as an image in the خُطوة app and in the pinned comment.
  - Speak one keyword per card, or say «والكروت دي…» while it lights.

### 4. Chapter 3 (and the hook payoff) doesn't stand alone (C1.1, C4.6–C4.7, C4.11, C5.5, C7.1, A1.3)
- C1.1 says «الدولة أربع أركان» but never names them. C4.4, C4.6–C4.7, C4.11, C5.1, C5.5 and C5.9 all assume chapter 1 and 2 content.
- **C5.5's model answer is «الكرسي، ركن ركن».** A student who jumped to chapter 3 doesn't know the chair. Any student would also get zero for writing "the chair" in an exam.
- A1.3 promises «الإجابة هتلاقيها في آخر الفيديو», 21 minutes away. That conflicts with the "each chapter stands alone" design, and most chapter-jumpers never hear C7. C7.1 «فاكر سؤال البداية؟» means nothing to someone who started at 12:19.
- **Fix:**
  - C1.1: «الدولة أربع أركان: شعب، وحيز جغرافي، وسلطة، وسيادة. بس دي مش كفاية.» (+6 words)
  - C5.5: speak the book-gradable answer: «الشعب لو غاب وعيه الدولة تضعف؛ الحيز من غير حدود مفيش دولة؛ السلطة لو غابت يضيع النظام والحقوق؛ السيادة لو غابت الدولة تفقد قرارها.» Keep the mini chair only as the drawing.
  - A1.3: «والإجابة هنبنيها حتة حتة، وآخر الفيديو هنقفلها.» Then pay off part of the answer at A5 («أول نص في الإجابة: الأركان») and at B6.4.
  - C7.1: restate the question in full for a cold viewer: «سؤال الدرس: ليه دول عاشت عبر التاريخ ودول اندثرت؟» Draw a copy of the ✓ arrow on sheet D; never cut back to sheet A.
  - B4.9 «من الدرس ده: ثورة 1919» → «ثورة 1919 اللي مختلف فئات الشعب شاركت فيها ضد الاحتلال». That's self-contained for chapter 2 viewers.

### 5. Examples that plant the wrong idea (A2.1, C2.4, C3.10, B5.1, C3.1, B2.4)
- **"Wall" means three different things:**
  - A2.1: walls = «حيز» (territory).
  - C2.4: «أسوار بسيطة» = natural borders.
  - C3.10: «سور البيت» = the army.
  - Students will write «الحيز = الحدود» (the book separates them in A4.4) and will blur foundation 1 (natural borders) with foundation 5 (army).
  - **Fix:**
    - A2.1: the **floor/flat area** = «حيز», and walls = «حدوده». The spoken line becomes «فيه ناس ساكنة، ومساحة ليها حدود، وحد بيدير…».
    - C2.4: draw desert, sea and cataract icons, not walls.
    - Cut C3.10 (7 words, adds nothing). C3.11's shield on the border already says "army".
- **B2.4 «حدّد مكونات السلطة في أربع مواد»** comes right as card 12 is drawn with 3 boxes. Expect «السلطات أربعة» on exam papers.
  - **Fix:** «تلات سلطات، في أربع مواد، لأن التنفيذية ليها مادتين: الرئيس والحكومة.» On card 12, bracket م139 and م163 together under box 2.
- **B5.1 chair: «الكرسي يقع».** The book says «تأثّر» (p9) and «مهددة بالانهيار» (p20), and B5.4–B5.6 then give graded effects. Only the borders effect is "no state at all".
  - **Fix:** «الكرسي يميل، ويبقى مهدد يقع.» That also matches the drawing column, which already says «يميل».
- **C3.1 «بتحتفل بنفس المناسبات».** Muslim and Christian Egyptians don't share every religious holiday, and the comments will say so.
  - **Fix:** «عيلة كبيرة بتتكلم نفس اللهجة، وبتفرح وتزعل مع بعض. صعب حد يفرّقها، صح؟»
- **"Most important factor" overload.** The video crowns three different things:
  - the Nile (C2.9 «أهمها النيل»; C7.4 asks «النيل ولا الموقع»),
  - location (C2.8, Hamdan),
  - central government (C3.8 «الأساس الحقيقي», C4.2 «العامل الحاسم», C5.7).
  - In the p19 «اختر» the answer is (د) السلطة المركزية. A student fresh from C7.4's comment debate will be torn between Nile and location.
  - **Fix:** add one line after C4.2: «خد بالك من التلاتة: أهم مورد = النيل، حمدان = الموقع، العامل الحاسم في «اختر» = السلطة المركزية.» Draw it as a 3-row mini table.
- **Card 4 vs card 14.** Card 4 reads «السيادة للشعب وحده» (A3.4) and card 14 reads «السيادة = استقلال الدولة» (B4.3). Both cards sit on the memory board, so a student asked «عرّف السيادة» may write card 4.
  - **Fix:** card 4 becomes «م4: **الشعب مصدر السلطات**», which is exactly what the quiz tests, and the full Article 4 text is spoken only. Add Ahmed's optional bridge from decision 4 at B4.3.

### 6. No real pauses after 3:30; the "re-hooks" from there on are mostly fake (B2, C4–C5)
- The header counts 32 [↺], but only **two** are real «وقّف وفكّر» pauses: A2.6 (1:26) and A3.13 (3:30). After 3:30 there's no genuine pause for 18 minutes. C3.13 has a 1 s beat.
- Many marked re-hooks are questions answered in the same breath, so the viewer never gets a turn: A4.8 «الحد الشمالي إيه؟», B2.4 «تفتكر مين بيعمل القوانين؟», B2.8 «مين رئيسها؟». Others are just labels: C4.1, C5.1, C5.8, C6.1.
- **Drop-off zones:**

| Time | Rows | Why viewers leave | Fix |
|---|---|---|---|
| 0:18–0:48 | A1.4–A1.7 | 30 s of agenda right after a 15 s hook | Show the 4 questions on screen while saying only «أربع أسئلة، واحد في كل فصل — اكتبهم من الشاشة». About 12 words. |
| 7:30–9:07 | B2.5–B2.14 | 9 rows of near-verbatim constitution articles, no turn for the viewer | Say B2.14 «تعمل / تنفّذ / تحكم» **first** as the frame. Add «وقّف وخمّن: الموازنة العامة مين بيقرّها؟» (3 s), answer «مجلس النواب». |
| 10:56 | B5.1 | the chair question is answered instantly | 2-s pause before «يميل». |
| 13:25 | C2.8 | Hamdan read as a quote | Turn it into a pause: «وقّف وفكّر: لو مفيش نيل، مصر كانت هتبقى مهمة؟» (3 s), then Hamdan. |
| 17:07–17:29 | C4.2–C4.4 | three «اختر» items answered before the student can choose | «وقّف واختار» 3 s on each, the natural place for pauses. +9 s |
| 17:29–19:54 | C4.5, C4.10, C5.8, C5.10 | ~50 s of "check your book / pick and justify" with no answers | Cut C4.5 «ارجع لصورته في كتابك» (dead air; keep the question in the description). Merge C4.10 and C5.8 into one line. Give C5.10 a model answer: «الحيز: حدود القرية؛ ومصدر السلطة: أهلها، زي ما الشعب مصدر السلطات (م4).» |

### 7. Neutrality: three new exposures (A1.2, A4.13, C3.4–C3.5), plus one inherited wording
- **A1.2 «دول تانية كتير قامت ووقعت… بتفشل».** Without «عبر التاريخ» the comments will name present-day states, and sheet A then labels **السودان** and **ليبيا** on the map.
  - **Fix:** use the book's p11 framing: «ودول تانية كتير عبر التاريخ قامت واندثرت. ليه؟» In A1.2 the two blank squares read «دولة قديمة», and in C7.1 «اندثرت».
- **A4.13 «خط بحري متقطع في المتوسط».** A drawn maritime line in the eastern Mediterranean sits on a live dispute between neighbouring states, and the book's map doesn't draw one.
  - **Fix:** no line. Put a small treasure or fish icon in the blue strip with the text «حدود بحرية محددة».
- **C3.4 → C3.5.** The spoken order is «ما اتأثروش بثقافة المحتل» immediately followed by «…وبعدين القبطية، وبعدين العربية».
  - Heard back to back, it either sounds like a contradiction ("not affected, yet changed language twice?") or puts Arabic next to "occupier". v1's fix only separated them visually.
  - The verb is also uncertain (decision 16: «تأثّر» or «ذوبان»).
  - **Fix:**
    - Move C3.5 to after C3.17, framed as «اللغة اتغيرت عبر العصور، والهوية فضلت مصرية».
    - In C3.4 use «ما ذابوش في ثقافة المحتل» if the print copy says ذوبان. That's softer and more accurate than "unaffected".
- **A3.13 still says «كل فئات المجتمع».** The book (and A3.15) says «مختلف فئات المجتمع». Align them as v1 asked.
- Watch item, no change needed: A4.4/B5.4 say «مفيش دولة من غير حدود معترف بها», and the same sheet labels «فلسطين» across a border. Keep «فلسطين» in card 8's text in the book's wording, but **don't** write it as a map label. That avoids putting the two side by side in a frame people screenshot. The narrator should add nothing.

### 8. «احفظ دي» cards and bullets that appear before the words that carry them
| Row | What appears early | Spoken when | Fix |
|---|---|---|---|
| B2.4 | Card 12 «السلطات التلاتة» + 3 boxes | «تلاتة» is never said in B2.4; the row says «أربع مواد» | Draw on «تلات سلطات» (see #5). |
| C3.11 | Card 20 «دور الجيش» at the start of the row | the role is spoken from «الأداة…» | Anchor on «الأداة». |
| C3.18 | Bullet «6 مقومات: موقع، موارد…» | the list of 6 is **not spoken** until C6.5 | C3.18 bullet → «• الهوية: تعريف + إجراءات الدولة (على «الثقافة»)». Keep the list bullet at C6.5. |
| A4.12 | Card 9 «= 12» | «اتناشر» is mid-row | Anchor on «اتناشر». |
| C1.3 | Card 17 frames «طبيعية / بشرية» | the classification is the writer's inference (decision 8) | Keep only after Ahmed confirms it in print. Otherwise use plain numbered boxes. |
| C6.2 / C6.5 | Cards 5, 19, 20, 22 light up | never named | Speak one keyword per card (see #3). |

Also, two lesson-level items have **no card** but are exam targets:
- **Nile → central authority** (C2.10–C2.13). This is a stated lesson objective (p9 «يفسّر العلاقة بين نهر النيل ونشأة السلطة المركزية»).
- **The effect of losing each pillar** (B5.4–B5.6, p20 «حلّل… موضحًا أثر غياب كل ركن»).

Add them as cards 23–24 on the memory board's panels 3 and 2.

---

## Other issues

### Examples: keep / cut / fix
| Row | Example | Verdict |
|---|---|---|
| A2.1 | House = 4 pillars | Keep. Fix walls vs area (#5). |
| A3.1 | Enrolled absent classmate = citizens abroad | **Keep, best example in the video.** |
| A3.6 / A4.1 | Football team, then football pitch 80 s later | Football twice in a row. Keep A4.1 (pitch lines = territory and the referee's reach = sovereignty, a real link). Change A3.6 to "a group project: everyone has a role", or cut it. |
| A4.11 | Balcony = territorial waters | Keep. |
| A4.14 | Drone «السما دي بتاعتك» | Slightly misleading: individuals don't own airspace. Change to «فوق بيتكم من غير إذن؟ أكيد تعترضوا. والدولة كمان». |
| B2.1 / B3.1 | School twice | B3.1 adds nothing that B3.2's quote doesn't already say. Cut B3.1 (−12 words) and keep B2.1. |
| B4.1 | Neighbours choose your summer trip | Fine, a bit young. Optional: «حد من برّه البيت يقرر إنتو هتصرفوا فلوسكم في إيه؟» |
| B5.1 | Chair | Keep, with «يميل، ويبقى مهدد يقع» (#5). |
| C2.1 | Dad's shop on a main street | Keep. |
| C2.11 | One water tank in a building | **Keep, excellent**: it explains Nile → central authority. |
| C3.1 | Family | Fix "same occasions" (#5). |
| C3.6 | Two uncoordinated villages | Keep. |
| C3.10 | Wall = army | Cut (#5). |
| C3.14 | Old photo + holiday dish = identity | Keep. |

16 analogies in 22 min, always in the same "analogy → «الكتاب بيقول»" rhythm, becomes predictable by chapter 3. Cutting B3.1, C3.10 and A3.6 breaks the pattern a little.

### Misremember risks (smaller)
- **A2.3–A2.4 / card 1**: the spoken definition skips «تباشر اختصاصاتها بما يحقق الأمن والاستقرار». Fine aloud under the 15-word quote rule, but **card 1 is what gets memorized**, so write the full book definition on the card (small font is OK on the zoomed-in card, and the memory panel uses keywords).
- **A4.7 / A4.9 dates**: hires p13 reads **1898**. b2hi1.txt reads «1099» (garbled) for the south and **«1907»** for the east. The script uses 1899 and 1906 from the text layer. Decision 1 flags only 1898/1899; flag 1906/1907 too. These go on a memorized card, so check the print copy before drawing.
- **C2.16 «يعني حافظ على المية»**: the quote is a negative-confession line (not withholding water from others). The book's sidebar frames it as conservation, so it's acceptable, but «يعني ما منعش المية عن غيره» is more exact and still supports C4.9.
- **C5.11** answers only the Menes half of p18. The second half («ولماذا هي بحاجة في الوقت الحالي إلى قوات مسلحة في أعلى جاهزية؟») is skipped. It can be answered neutrally from p17 alone: «ونفس السبب النهارده: تحمي الحدود وتضمن الاستقرار، وعقيدتها «لا يعتدي».» (+12 words)
- **C5.8** has 19 words, over the 18-word spoken limit. Split it.

### Re-hook accounting
- Count only real turns for the viewer (a pause, an unanswered beat or a surprising book fact). By that count the longest gaps are 3:39→10:56 (with only the rhetorical A4.8/B2.4/B2.8 between) and 13:25→17:07.
- The fixes in #6 bring the real gaps under about 90 s. Under 60 s isn't realistic for 22 minutes of curriculum, so say that honestly in the header instead of claiming 32 re-hooks.

### Duration after these fixes
Cuts: A1.4–A1.7 shortened (−30 words), B3.1 (−12), C3.10 (−7), C4.5 (−6), C4.10 and C5.8 merged (−15). Adds: #1 (+4), #4 (+40), #5 (+35), #6 pauses (+20 s), #3 panels (+15 s), C5.11 (+12). The net is about +25 words plus about 35 s, so roughly **22:30**. That fits the 4 or 5 chapters proposed in #2, each 3:20–5:00.
