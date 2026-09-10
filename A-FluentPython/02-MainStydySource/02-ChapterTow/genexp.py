# ╭─────────────────────────╮
# │ [Generator Expressions] │
# ╰─────────────────────────╯
import array
# نفس اللعبه بس المرة دي tuple, array مش list
symbols = '$¢£¥€¤'
result = tuple(ord(symbol) for symbol in symbols)
print(result)
result = array.array('I', (ord(symbol) for symbol in symbols))
print(result)
# ══════════════════════════════════════════════════════════════════════════════
colors=["red","blue","black"]
sizes=["s","m","l"]
for tshirt in (f'{c} {s}' for c in colors for s in sizes):
    print(tshirt)

# إليك استخراج وترجمة قسم **"Generator Expressions" (تعبيرات المولدات)** من **الصفحة 29** في الكتاب [cite: 174, 256]، يليه شرح متكامل وتفصيلي من 0% إلى 100% يدمج الفكرة مع الأجزاء الأخرى المتقدمة في الكتاب و**وثائق بايثون المرفقة** لتفهم هذا المفهوم وكأنك مخترع بايثون نفسه!



## 🛠️ أولاً: وضع الاستخراج والترجمة (ص. 29)

### **النص الأصلي (Original English Text) — (ص. 29):**

# ```text
# Generator Expressions

# To initialize tuples, arrays, and other types of sequences, you could also start from a listcomp, but a genexp (generator expression) saves memory because it yields items one by one using the iterator protocol instead of building a whole list just to feed another constructor.

# Genexps use the same syntax as listcomps, but are enclosed in parentheses rather than brackets.

# Example 2-5 shows basic usage of genexps to build a tuple and an array.

# Example 2-5. Initializing a tuple and an array from a generator expression

# >>> symbols = '$¢£¥€¤'
# >>> tuple(ord(symbol) for symbol in symbols)
# (36, 162, 163, 165, 8364, 164)
# >>> import array
# >>> array.array('I', (ord(symbol) for symbol in symbols))
# array('I',)

# If the generator expression is the single argument in a function call, there is no need to duplicate the enclosing parentheses.

# The array constructor takes two arguments, so the parentheses around the generator expression are mandatory. The first argument of the array constructor defines the storage type used for the numbers in the array, as we'll see in "Arrays" on page 59.

# Example 2-6 uses a genexp with a Cartesian product to print out a roster of T-shirts of two colors in three sizes. In contrast with Example 2-4, here the six-item list of T-shirts is never built in memory: the generator expression feeds the for loop producing one item at a time. If the two lists used in the Cartesian product had a thousand items each, using a generator expression would save the cost of building a list with a million items just to feed the for loop.

# Example 2-6. Cartesian product in a generator expression

# >>> colors = ['black', 'white']
# >>> sizes = ['S', 'M', 'L']
# >>> for tshirt in (f'{c} {s}' for c in colors for s in sizes):
# ...     print(tshirt)
# ...
# black S
# black M
# black L
# white S
# white M
# white L

# The generator expression yields items one by one; a list with all six T-shirt variations is never produced in this example.

# Chapter 17 explains how generators work in detail. Here the idea was just to show the use of generator expressions to initialize sequences other than lists, or to produce output that you don't need to keep in memory.
# ```

# ---

# ### **الترجمة العربية الدقيقة:**

# **تعبيرات المولدات (Generator Expressions) — (ص. 29)** [cite: 256]

# لتهيئة الـ tuples، والمصفوفات (arrays)، وغيرها من أنواع المتتاليات (sequences)، يمكنك أيضاً البدء من صيغة استيعاب القوائم (`listcomp`)، ولكن **تعبيرات المولدات (`genexp`)** توفر الذاكرة لأنها تنتج العناصر (yields) واحداً تلو الآخر باستخدام **بروتوكول المكرر (iterator protocol)**، بدلاً من بناء قائمة كاملة في الذاكرة لمجرد تغذية مشيد (constructor) آخر [cite: 256].

# تستخدم تعبيرات المولدات (`Genexps`) نفس بناء الجملة الخاص بـ `listcomps`، ولكنها تُحاط **بأقواس دائرية `()`** بدلاً من الأقواس المربعة `[]` [cite: 256].

# يوضح المثال 2-5 الاستخدام الأساسي لتعبيرات المولدات لبناء كائن `tuple` ومصفوفة `array` [cite: 256].

# **المثال 2-5.** *تهيئة tuple ومصفوفة من تعبير مولد:* [cite: 256]
# ```python
# >>> symbols = '$¢£¥€¤'
# >>> tuple(ord(symbol) for symbol in symbols)
# (36, 162, 163, 165, 8364, 164)
# >>> import array
# >>> array.array('I', (ord(symbol) for symbol in symbols))
# array('I',)
# ```

# إذا كان تعبير المولد هو **المعامل الوحيد (single argument)** في استدعاء الدالة، فلا داعي لتكرار الأقواس الدائرية المحيطة به (يكفي قوس الدالة نفسه) [cite: 257].

# يأخذ مشيد المصفوفة `array` معاملين، لذا فإن الأقواس المحيطة بتعبير المولد هنا **إلزامية** [cite: 257]. يحدد المعامل الأول لمشيد المصفوفة نوع التخزين المستخدم للأرقام في المصفوفة، كما سنرى في قسم "المصفوفات" في صفحة 59 [cite: 257].

# يستخدم المثال 2-6 تعبير المولد (`genexp`) مع ضرب ديكارتي لطباعة قائمة بقمصان (T-shirts) بلونين وثلاثة مقاسات [cite: 258, 259]. وعلى عكس المثال 2-4، فإن قائمة التيشيرتات المكونة من ستة عناصر **لا يتم بناؤها أبداً في الذاكرة**؛ حيث يقوم تعبير المولد بتغذية حلقة `for` لإنتاج عنصر واحد في كل مرة [cite: 258, 259]. إذا كانت القائمتان المستخدمتان في الضرب الديكارتي تحتويان على ألف عنصر لكل منهما، فإن استخدام تعبير المولد سيوفر تكلفة بناء قائمة تحتوي على **مليون عنصر** لمجرد تغذية حلقة `for` [cite: 258].

# **المثال 2-6.** *الضرب الديكارتي في تعبير المولد:* [cite: 259]
# ```python
# >>> colors = ['black', 'white']
# >>> sizes = ['S', 'M', 'L']
# >>> for tshirt in (f'{c} {s}' for c in colors for s in sizes):
# ...     print(tshirt)
# ...
# black S
# black M
# black L
# white S
# white M
# white L
# ```

# يقوم تعبير المولد بإنتاج العناصر واحداً تلو الآخر؛ ولا يتم أبداً إنتاج قائمة تحتوي على جميع بدائل التيشيرتات الستة في هذا المثال [cite: 259].

# يشرح الفصل 17 بالتفصيل كيفية عمل المولدات [cite: 259]. وكانت الفكرة هنا مجرد توضيح استخدام تعبيرات المولد لتهيئة متتاليات أخرى غير القوائم، أو لإنتاج مخرجات لا تحتاج إلى الاحتفاظ بها في الذاكرة [cite: 259].

# ---

# ## 🧠 ثانياً: الشرح التقني والعميق (0% لـ 100%)

# عشان تفهم الفكرة دي بنسبة 100% وبدون أي تعقيد، تعال نقارن بين مفهومين في منتهى الجمال:

# ### 🍨 1. تشبيه كرتوني: "بوفيه الحلوى" 🆚 "شيف المطعم الشخصي"

# تخيل إن عندك حفلة فيها 1000 ضيف، وعايز تقدم لهم كب كيك:
# * **استيعاب القوائم (`listcomp`):** هو **بوفيه مفتوح** [cite: 256]. الشيف بيحضر الـ 1000 قطعة كب كيك كلها فوراً ويرصها على طاولات ضخمة جداً في القاعة قبل ما الحفلة تبدأ [cite: 256]!
#   * **الميزة:** الحاجة جاهزة قدام عيونك [cite: 245].
#   * **العيب:** الطاولات حجزت مساحة ضخمة جداً من القاعة (استهلاك رهيب للذاكرة/RAM)، وممكن الضيوف ياكلوا قطعتين بس ويمشوا، ويبقى الشيف ضيّع وقته ومجهوده ومساحة المكان على الفاضي [cite: 1026]!
# * **تعبير المولد (`genexp`):** هو **شيف شخصي** واقف على البوابة [cite: 256]. أول ما الضيف الأول يوصل ويقول "أنا جعان"، الشيف يخبز له قطعة واحدة طازة ويديها له [cite: 256]. ولما الضيف التاني يطلب، يخبز له قطعة تانية بالطلب [cite: 256]!
#   * **الميزة:** ما حجزناش طاولات ولا رصينا حلوى (الذاكرة فاضية ومستريحة تماماً) [cite: 256, 1026].
#   * **العيب:** ما تقدرش تبص على الـ 1000 قطعة كب كيك دفعة واحدة، لأنهم مش موجودين في الواقع؛ هما بيتصنعوا "عند الطلب" (On demand/Lazily) [cite: 1019, 1026]!

# ---

# ### ⚙️ 2. كيف نكتب الـ `genexp` برمجياً؟ (ص. 29)
# الفرق الوحيد والعبقري في الكتابة بين القائمة والمولد هو **نوع الأقواس** [cite: 256]:
# * أقواس مربعة `[ ]` = قائمة حقيقية في الذاكرة (`listcomp`) [cite: 245].
# * أقواس دائرية `( )` = مولد سحري كسول (`genexp`) [cite: 256].

# #### **الحالة الخاصة بحذف الأقواس الدائرية (ص. 29):**
# بايثون لغة أنيقة وبتكره الكتابة الكتير. لو إنت بتمرر المولد كمعامل **وحيد** داخل دالة (زي دالة `tuple` اللي بتاخد حاجة تلف عليها وتحولها لـ tuple)، مش محتاج تكتب الأقواس مرتين [cite: 257]!
# * ❌ **كتابة صحيحة بس شكلها مكرر:** `tuple( (x for x in list) )`
# * ✅ **كتابة بايثونية أنيقة:** `tuple(x for x in list)` [cite: 257]
# هنا بايثون بتفهم تلقائياً إن الأقواس دي هي أقواس استدعاء الدالة وفي نفس الوقت هي أقواس المولد [cite: 257]!

# ولكن، لو الدالة بتاخد معاملين أو أكتر (زي كلاس المصفوفات `array.array` اللي بياخد معامل لنوع البيانات ومعامل للمولد نفسه)، هنا بايثون بتجبرك تحط أقواس المولد الدائرية عشان ما تتلخبطش بين المعاملات [cite: 257]:
# `array.array('I', (ord(s) for s in symbols))` [cite: 257]

# ---

# ### ⚡ 3. توضيح سحر الأداء والذاكرة بالأرقام:
# تخيل إنك بتعمل ضرب ديكارتي (ألوان تيشيرتات ومقاسات) زي المثال 2-6 [cite: 258]:
# * لو عندك **1000 لون** و **1000 مقاس**:
#   * باستخدام الـ `listcomp` `[...]`: بايثون هتقوم في جزء من الثانية بحساب وبناء قائمة تحتوي على **مليون تيشيرت** وتخزينهم في الذاكرة فوراً [cite: 258]! ده ممكن يخلي البرنامج يستهلك ميجابايتس كتير جداً من الذاكرة وممكن يقف خالص [cite: 258, 1045].
#   * باستخدام الـ `genexp` `(...)`: الذاكرة هتفضل **صفر** تقريباً [cite: 256, 1026]! لأن المولد مش هينتج المليون تيشيرت؛ هو هيفضل واقف، وكل ما حلقة الـ `for` تلف لفة، يديها تيشيرت واحد، ولما تخلص لفتها وتطلب اللي بعده، يحسب التاني ويمسح الأولاني من الذاكرة [cite: 258, 259]!

# ---

# ### 📜 4. كشف المستور: الربط السحري مع وثائق بايثون المرفقة (الفصل 17 - ص. 611-613)

# عشان تفهم المولدات دي بتشتغل إزاي تحت السرير وتصدق إنها كسلانة (Lazy)، تعال نربط الفكرة دي بـ **المثال 17-9 من صفحة 611** في الكتاب [cite: 174, 1029]:

# المؤلف عمل كود يطبع كلمات في النص عشان نشوف مين بيتنفذ الأول [cite: 1029]:
# ```python
# def gen_AB():
#     print('start')
#     yield 'A'
#     print('continue')
#     yield 'B'
#     print('end.')
# ```

# #### **التجربة الأولى: مع الـ `listcomp` (الاستعجال التام) [cite: 1030]:**
# ```python
# >>> res1 = [x*3 for x in gen_AB()]
# start
# continue
# end.
# ```
# **ماذا حدث؟** بمجرد كتابة السطر ده، وقبل ما المبرمج يلف على القائمة `res1` أصلاً، بايثون جرت فوراً ونفذت الدالة بالكامل وطبعت الكلمات وعملت القائمة [cite: 1030]!

# #### **التجربة الثانية: مع الـ `genexp` (الكسل التام) [cite: 1030]:**
# ```python
# >>> res2 = (x*3 for x in gen_AB())
# >>> res2
# <generator object <genexpr> at 0x10063c240>
# ```
# **ماذا حدث؟** صمت تام! بايثون ما نفذتش أي حاجة من الدالة، ولا طبعت "start" ولا أي شيء [cite: 1030]! هي مجرد جهزت كائن مولد كسول مستني الإشارة [cite: 1030].
# لما نبدأ نلف عليه في حلقة `for` [cite: 1030]:
# ```python
# >>> for i in res2:
# ...     print('-->', i)
# ...
# start
# --> AAA
# continue
# --> BBB
# end.
# ```
# هنا، مع كل لفة، الكود الداخلي بيتنفذ خطوة بخطوة بالطلب والترتيب [cite: 1030]!

# ---

# 🎯 **هل شيف المولدات الكسول `genexp` بقى واضح ومفهوم بنسبة 100%؟** 

# إذا كنت مستعداً للانتقال إلى **صفحة 30** ودخول عالم الـ **`Tuples`** ومعرفة السر وراء المقولة الصادمة للكاتب: **"الـ Tuples ليست مجرد قوائم غير قابلة للتعديل! بل لها دور سري كسجلات برمجية"** [cite: 260]، أرسل لي **"أكمل"**!