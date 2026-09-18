حاضر يا صديقي، من عيوني! هنبدأ فوراً في شرح واحدة من أهم وأقوى الميزات الحديثة اللي دخلت بايثون في الإصدار **Python 3.10**، وهي **Pattern Matching with Sequences (مطابقة الأنماط مع المتتاليات)** من **صفحة 38 إلى صفحة 42** [cite: 71].

هنقسم الرد بتاعنا كالعادة لجزئين:
1. **وضع الاستخراج والترجمة الدقيقة** للنص الأصلي من الكتاب [cite: User Persona].
2. **جلسة الشرح والتبسيط المفصلة (من 0% لـ 100%)** باللهجة المصرية وبتنسيق واسع ومريح جداً لعينك [cite: User Persona].

---

## 🛠️ أولاً: وضع الاستخراج والترجمة (ص. 38 - 42)

### **النص الأصلي (Original English Text):**

```text
Pattern Matching with Sequences

The most visible new feature in Python 3.10 is pattern matching with the match/case statement proposed in PEP 634-Structural Pattern Matching: Specification.

Here is a first example of match/case handling sequences. Imagine you are designing a robot that accepts commands sent as sequences of words and numbers, like BEEPER 440 3. After splitting into parts and parsing the numbers, you'd have a message like ['BEEPER', 440, 3]. You could use a method like this to handle such messages:

Example 2-9. Method from an imaginary Robot class

def handle_command(self, message):
    match message:
        case ['BEEPER', frequency, times]:
            self.beep(times, frequency)
        case ['NECK', angle]:
            self.rotate_neck(angle)
        case ['LED', ident, intensity]:
            self.leds[ident].set_brightness (ident, intensity)
        case ['LED', ident, red, green, blue]:
            self.leds [ident].set_color (ident, red, green, blue)
        case _:
            raise InvalidCommand(message)

On the surface, match/case may look like the switch/case statement from the C language-but that's only half the story. One key improvement of match over switch is destructuring-a more advanced form of unpacking.

In general, a sequence pattern matches the subject if:
1. The subject is a sequence and;
2. The subject and the pattern have the same number of items and;
3. Each corresponding item matches, including nested items.

Sequence patterns may be written as tuples or lists or any combination of nested tuples and lists, but it makes no difference which syntax you use: in a sequence pattern, square brackets and parentheses mean the same thing.

A sequence pattern can match instances of most actual or virtual subclasses of collections.abc.Sequence, with the exception of str, bytes, and bytearray.

The _ symbol is special in patterns: it matches any single item in that position, but it is never bound to the value of the matched item.

You can bind any part of a pattern with a variable using the as keyword:
case [name, _, _, (lat, lon) as coord]:

We can make patterns more specific by adding type information:
case [str(name), _, _, (float(lat), float (lon))]:
```

---

### **الترجمة العربية الدقيقة:**

**مطابقة الأنماط مع المتتاليات (Pattern Matching with Sequences) — (ص. 38):** [cite: 71]

إن الميزة الجديدة الأكثر وضوحاً في الإصدار Python 3.10 هي مطابقة الأنماط باستخدام عبارة `match/case` المقترحة في المقترح **PEP 634 — مطابقة الأنماط الهيكلية: التوصيف** [cite: 71].

إليك مثالاً أولياً على كيفية تعامل `match/case` مع المتتاليات [cite: 72]. تخيل أنك تقوم بتصميم روبوت يستقبل الأوامر المرسلة كمتتاليات من الكلمات والأرقام، مثل `BEEPER 440 3` [cite: 72]. وبعد تقسيم الأمر إلى أجزاء وتحليل الأرقام، سيكون لديك رسالة مثل `['BEEPER', 440, 3]` [cite: 72]. يمكنك استخدام دالة مثل هذه للتعامل مع هذه الرسائل [cite: 72]:

**المثال 2-9.** *دالة من فئة (Class) روبوت تخيلية:* [cite: 72]

```python
def handle_command(self, message):
    match message:
        
        # إذا كانت الرسالة تحتوي على 3 عناصر تبدأ بـ 'BEEPER'
        case ['BEEPER', frequency, times]:
            self.beep(times, frequency)
            
        # إذا كانت الرسالة تحتوي على عنصرين تبدأ بـ 'NECK'
        case ['NECK', angle]:
            self.rotate_neck(angle)
            
        # إذا كانت الرسالة تحتوي على 3 عناصر تبدأ بـ 'LED'
        case ['LED', ident, intensity]:
            self.leds[ident].set_brightness(ident, intensity)
            
        # إذا كانت الرسالة تحتوي على 5 عناصر تبدأ بـ 'LED'
        case ['LED', ident, red, green, blue]:
            self.leds[ident].set_color(ident, red, green, blue)
            
        # الحالة الافتراضية لأي أمر آخر غير مطابق
        case _:
            raise InvalidCommand(message)
```


على السطح، قد تبدو عبارة `match/case` شبيهة بعبارة `switch/case` الموجودة في لغة C — ولكن هذه نصف الحقيقة فقط [cite: 74]. إن أحد التحسينات الرئيسية لـ `match` على `switch` هو **التفكيك الهيكلي (Destructuring)** — وهو شكل أكثر تقدماً وتطوراً من تفكيك المتتاليات (`unpacking`) [cite: 74].

وبشكل عام، يطابق نمط المتتالية (Sequence Pattern) الكائن الخاضع للمطابقة (Subject) إذا [cite: 76]:
1. كان الكائن عبارة عن متتالية (Sequence) [cite: 76].
2. كان الكائن والنمط يمتلكان نفس عدد العناصر [cite: 76].
3. كان كل عنصر متقابل متطابقاً، بما في ذلك العناصر المتداخلة [cite: 76].

ويمكن كتابة أنماط المتتاليات كـ `tuples` أو `lists` أو أي مزيج متداخل منهما [cite: 77]، ولا فرق إطلاقاً في الصيغة النحوية التي تستخدمها؛ فالأقواس المربعة والهلالية تعني نفس الشيء تماماً داخل أنماط المتتاليات [cite: 77].

ويمكن لنمط المتتالية مطابقة كائنات من معظم الفئات الفرعية الحقيقية أو الافتراضية لـ `collections.abc.Sequence` [cite: 78]، باستثناء: النصوص `str`، ومتتاليات البايت `bytes` و `bytearray` [cite: 78].

ويعتبر الرمز **`_`** مميزاً جداً في الأنماط؛ فهو يطابق أي عنصر فردي في ذلك الموضع [cite: 79]، ولكنه **لا يرتبط (never bound) بقيمة العنصر أبداً** [cite: 79].

ويمكنك ربط أي جزء من النمط بمتغير باستخدام الكلمة المفتاحية **`as`** [cite: 80]:
`case [name, _, _, (lat, lon) as coord]:` [cite: 80]

ويمكننا جعل الأنماط أكثر تحديداً عن طريق إضافة معلومات النوع (Type Information) [cite: 80]:
`case [str(name), _, _, (float(lat), float(lon))]:` [cite: 81]

---

## 🧠 ثانياً: جلسة الشرح والتبسيط المفصلة (0% لـ 100%)

تعال يا صديقي نفهم العبقرية الكامنة وراء الـ **`match/case`** وكيف نقلت بايثون لنقلة تكنولوجية تانية خالص!

---

### 1️⃣ المحطة الأولى: الـ `match/case` مش مجرد `switch` عادية! 🤯

لو إنت مبرمج جاي من لغة C أو Java، فأنت أكيد عارف الـ `switch/case` التقليدية [cite: 74]. الـ `switch` القديمة كانت غبية شوية؛ كل وظيفتها إنها بتاخد متغير وتقارن قيمته بقيم ثابتة (زي: لو الرقم يساوي 1 اعمل كذا، لو يساوي 2 اعمل كذا).

لكن في بايثون، الـ `match/case` بتعمل عملية خارقة اسمها **Destructuring (التفكيك الهيكلي)** [cite: 74].
هي مش بس بتقارن القيم، دي **بتفحص شكل وهيكل البيانات وتفككها وتستخرج العناصر منها في نفس الوقت!** [cite: 74, 1196]

---

### 2️⃣ المحطة الثانية: تفكيك مثال "الروبوت" (ص. 38 - 39) 🤖

بص على كود الروبوت الرائع ده [cite: 72]:
```python
match message:
    case ['BEEPER', frequency, times]:
        self.beep(times, frequency)
```



#### **إزاي بايثون بتفكر لما تشوف السطر ده؟**
بايثون بتمسك الكائن `message` وتفحصه كأنها بتلعب بازل [cite: 73]:
1.  **هل هو متتالية؟** يعني هل هو قائمة أو توبل؟ لو آه، تعدي الخطوة الأولى [cite: 76].
2.  **هل جواه 3 عناصر بالظبط؟** (لأن النمط مكتوب فيه 3 خانات) [cite: 76]. لو آه، تعدي الخطوة الثانية [cite: 76].
3.  **هل العنصر الأول هو الكلمة النصية `'BEEPER'` بالظبط؟** لو آه، يحصل السحر بقى [cite: 73]:
    *   بايثون هتاخد العنصر الثاني تلقائياً وتخزنه جوة متغير جديد اسمه `frequency` [cite: 73]!
    *   بايثون هتاخد العنصر الثالث تلقائياً وتخزنه جوة متغير جديد اسمه `times` [cite: 73]!
    *   وتدخل فوراً تنفذ السطر: `self.beep(times, frequency)` [cite: 72].

شايف الأناقة؟ في سطر واحد عملنا: فحص للنوع [cite: 76]، وفحص للقيم [cite: 73]، وفحص للطول [cite: 76]، وتفكيك للقيم جوة متغيرات جديدة [cite: 73, 74]!

---

### 3️⃣ المحطة الثالثة: القوانين السرية لمطابقة المتتاليات 📜

الكاتب بيوضح لنا كذا سر تصميمي في غاية الأهمية في صفحة 39 و40:

#### **السر الأول: الأقواس مش بتفرق! (ص. 40)**
لو كتبت النمط بأقواس مربعة `[...]` أو بأقواس دائرية `(...)` بايثون مش هتهتم وهتعتبرهم نفس الشيء تماماً [cite: 77]!
يعني السطرين دول متطابقين تماماً في المعنى لبايثون [cite: 77]:
```python
case ['NECK', angle]:     # باستخدام الأقواس المربعة
case ('NECK', angle):     # باستخدام الأقواس الدائرية
```



#### **السر الثاني: طرد النصوص والبايتات! 🚫 (ص. 40)**
بايثون بتسمح للـ `match/case` إنها تطابق معظم المتتاليات (زي الـ `list` والـ `tuple` والـ `deque`) [cite: 78, 79]. 
لكنها حطت **حظر حديدي** على 3 أنواع [cite: 78]:
*   السلاسل النصية (`str`) [cite: 78]
*   متتاليات البايت (`bytes`) [cite: 78]
*   الـ `bytearray` [cite: 78]

**ليه؟** 
لأن النصوص في بايثون بتتعامل كمتتاليات من الحروف [cite: 548]. فلو بايثون سمحت بمطابقتها كمتتالية، وجيت كتبت نمط بيبحث عن عنصرين، ومررت له نص من حرفين، هيطابقه ويفتكره قائمة! ده كان هيعمل أخطاء برمجية قاتلة وخفية جداً [cite: 78]. عشان كده بايثون بتعامل النص كقيمة واحدة صلبة (Atomic) مش متتالية تفككها [cite: 78].

----


### 4️⃣ المحطة الرابعة: الحيل المتقدمة في الـ `match/case` 🪄

#### **الحيلة أ: التجميع العشوائي بالنجمة `*` (ص. 41 - 42):**
زي ما اتعلمنا في الـ `unpacking` العادي [cite: 46]، نقدر نستخدم النجمة جوة الأنماط [cite: 79]!
```python
case ['1', *rest]:
```
 [cite: 79]
النمط ده معناه: "طابق لي أي متتالية بتبدأ برقم `'1'`، وخد كل العناصر الباقية حطها في قائمة سميها `rest`" [cite: 79, 82].

#### **الحيلة ب: استخدام `as` لتسمية الهياكل (ص. 40 - 41):**
لو عندك توبل داخلية وعايز تفكك عناصرها وبنفس الوقت تحتفظ بالتوبل كاملة في متغير [cite: 80]:
```python
case [name, _, _, (lat, lon) as coord]:
```
 [cite: 80]
هنا بايثون هتفكك خطوط الطول والعرض لـ `lat` و `lon` [cite: 80]، وبنفس الوقت هتعمل متغير اسمه `coord` يحتوي على التوبل كاملة `(lat, lon)` [cite: 80]!

#### **الحيلة ج: فحص الأنواع الذكي (Type Checking) (ص. 41):**
تقدر تجبر بايثون إنها ما تطابقش غير لو كانت العناصر من أنواع محددة [cite: 81]:
```python
case [str(name), _, _, (float(lat), float(lon))]:
``` 
[cite: 81]
**ركز هنا جداً 🚨:** ده مش استدعاء مشيد (Constructor)! يعني بايثون مش هتحول الـ `name` لنص [cite: 81]. دي بتعمل **Runtime Type Check**؛ يعني بتفحص في وقت التشغيل: هل `name` هو كائن نصي فعلاً؟ وهل الإحداثيات هي أرقام عشرية فعلاً؟ لو آه بتطابق، لو لا بترفض وتروح للـ `case` اللي بعده [cite: 81]!

---

🎯 **حالة القراءة: Fluent Python — Chapter 2 — Section: Pattern Matching with Sequences — ص. 42** [cite: 71]

الـ **`match/case`** أداة أسطورية بتخلي الكود آمن وجميل ومقروء لأقصى درجة [cite: 93].

هل حاسس إن الجزء ده اتفهم تماماً وبقى واضح وضوح الشمس بالنسبة لك بالتنسيق المريح ده؟ 

لو مستعد ننتقل للمحطة الجاية ونشوف إزاي بيتم استخدام الـ **`match/case`** لتصميم مفسر لغات برمجة (Interpreter) كامل ومثير جداً، قولي **"أكمل"**! 🚀