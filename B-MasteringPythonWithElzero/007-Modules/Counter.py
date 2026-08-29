from collections import Counter
# print(dir(Counter))
# Iterable = المكان/المصدر الذي أستطيع التكرار عليه.
# Iterator = الكائن الذي يمشي خلال هذا المصدر ويخبرني بالعنصر التالي.
MyList = ("aplle","banna","coc","apple")
counts = Counter(MyList)
print(counts)
# OUTPUT: Counter({'aplle': 1, 'banna': 1, 'coc': 1, 'apple': 1})
# NOTE: counter put output in dict becaude it's a Subclass from dict
# ══════════════════════════════════════════════════════════════════════════════
text = "hello world"
LetterCounts = Counter(text)
print(LetterCounts)
# OUTPUT: Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
# NOTE: the key => letter , the value => counts
# ══════════════════════════════════════════════════════════════════════════════
print(LetterCounts['o'])
# OUTPUT: 2
print(LetterCounts['x'])
# OUTPUT: 0
# NOTE: counter handle the undefined object and return zero instead of error reverse normal dict
# ══════════════════════════════════════════════════════════════════════════════
# ╭───────────────────────────────╮
# │ Topic:  [Functions in Counter │
# ╰───────────────────────────────╯
#  FUNCTION:  most_common(n) use to return a Most frequent items =>Counter[str],n: int | None = None) -> list[tuple[str, int]]

data = Counter(['apple', 'banana', 'apple', 'orange', 'banana', 'apple'])
print(data.most_common(2))
# OUTPUT: [('apple', 3), ('banana', 2)]
# ══════════════════════════════════════════════════════════════════════════════
# FUNCTION: update() it taks a str list or dict{key,value=>number of repetitions} and return a new iterable with counts 

counts = Counter({'apple': 2, 'banana': 1})

# إضافة عناصر جديدة وتحديث التكرارات
counts.update({'apple':2, 'orange':5})
print(counts)
# OUTPUT: Counter({'apple': 4, 'banana': 1, 'orange': 5})
# ══════════════════════════════════════════════════════════════════════════════
# FUNCTION: subtract the same logic in update but its not addetion
# ══════════════════════════════════════════════════════════════════════════════
# TODO: تخيل أن لديك نصًا وتحتاج إلى حساب تكرار الكلمات، واستبعاد الكلمات الشائعة (Stop Words) مثل "في"، "من"، "على"، ثم تحديث النتيجة بنص جديد.

text1 = "الذكاء الاصطناعي يغير العالم الذكاء الاصطناعي هو المستقبل"
text2 = "المستقبل يعتمد على الذكاء الاصطناعي والتكنولوجيا"
# plan اول حاجه هنعملها نحول النص الطويل ده ل list عشان نعرف نتعامل معاه
WordsOne = text1.split()
WordsTow = text2.split()
# دلوقتي نخليهم في list واحده
Words = WordsOne + WordsTow
# نعمل ال counter
WordsCounts = Counter(Words)
# نختبره
print(WordsCounts)
# OUTPUT: Counter({'الذكاء': 3, 'الاصطناعي': 3, 'المستقبل': 2, 'يغير': 1, 'العالم': 1, 'هو': 1, 'يعتمد': 1, 'على': 1, 'والتكنولوجيا': 1})
# دلوقتي نشيل ال Stop Words بعد ما اكتشفنا عددها و هى اي {"علي":1, "هو":1, }
StopWords = Counter(["على","هو"]) # هنا عملناها في متغير عشان لو النص اتغير والكلمات زادت يبقا في مرونه 
# دلوقتي هنشيل ال counter StopWords من ال counter WordsCounts باستخدام داله subtract
WordsCounts.subtract(StopWords)
# نختبر WordsCounts
print(WordsCounts)
# OUTPUT: Counter({'الذكاء': 3, 'الاصطناعي': 3, 'المستقبل': 2, 'يغير': 1, 'العالم': 1, 'يعتمد': 1, 'والتكنولوجيا': 1, 'هو': 0, 'على': 0})
# دلوقتي فاضل ننضف العناصر اللي قيمتها 0 وده نعمله بكل سهوله باستخدام الداله element
CleanWordsCounts =list( WordsCounts.elements())
# دلوقتي نختبره ونشوف ايه اللي طلع 
print (CleanWordsCounts)
# OUTPUT: ['الذكاء', 'الذكاء', 'الذكاء', 'الاصطناعي', 'الاصطناعي', 'الاصطناعي', 'يغير', 'العالم', 'المستقبل', 'المستقبل', 'يعتمد', 'والتكنولوجيا']
