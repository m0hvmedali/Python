## Constructor يعني إيه؟

**Constructor = آلية/دالة مرتبطة بإنشاء Object وتهيئته.**

في Python، لما تتعلم OOP، غالبًا هتسمع إن:

```python
__init__()
```

هو الـ **Constructor**.

لكن لو عايزين نكون دقيقين جدًا:

> `__init__` في Python **ليست عملية إنشاء الـ Object نفسها**؛ هي Method تُستدعى لتهيئة الـ Object بعد إنشائه.

لكن في مستواك الحالي، ممكن تتعامل مع:

> `__init__` = الـ Constructor

لأن ده الاستخدام التعليمي الشائع.

---

## نرجع لمثالنا

```python
class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

لما تكتب:

```python
user = User("Mohamed", 18)
```

يحصل بشكل مبسط:

```text
User("Mohamed", 18)
        ↓
إنشاء Instance
        ↓
تشغيل __init__
        ↓
تهيئة الـ Instance
        ↓
user
├── name = "Mohamed"
└── age = 18
```

إذن `__init__` بتساعدنا إن الـ Object **يبدأ بحالة معينة** بدل ما يكون فاضي.

---

## ليه اسمه Constructor؟

كلمة:

> **Construct**

معناها تقريبًا:

> يبني / ينشئ.

لكن هنا لازم نفرق:

```text
Creation
   ↓
إنشاء الـ Object نفسه
```

و:

```text
Initialization
   ↓
تجهيز الـ Object بالبيانات الأولية
```

في Python الاتنين **مش نفس العملية**.

لكن:

```python
__init__
```

مسؤولة عن **Initialization**.

وعشان كده لو حد دخل معاك في Python بعمق وقال:

> "`__init__` مش Constructor حقيقي."

فهو **عنده نقطة صحيحة تقنيًا**.

الـ method المسؤولة عن إنشاء الـ instance فعليًا هي:

```python
__new__()
```

بينما:

```python
__init__()
```

تقوم بتهيئته.

لكن **ما ندخلش `__new__` دلوقتي**؛ لأنها مرحلة متقدمة ومش محتاجينها عشان نفهم أساسيات OOP.

---

### فحاليًا ثبت في دماغك:

```text
Class
 ↓
User

User("Mohamed", 18)
 ↓
Instance
 ↓
__init__
 ↓
تهيئة الـ Instance
 ↓
self.name = "Mohamed"
self.age = 18
```

**Constructor** هو المصطلح العام اللي هتقابله في OOP، وفي Python تحديدًا لازم تعرف إن الناس غالبًا تقصد بـ Constructor الـ `__init__`، رغم إن الفرق التقني بين الإنشاء والتهيئة موجود.
