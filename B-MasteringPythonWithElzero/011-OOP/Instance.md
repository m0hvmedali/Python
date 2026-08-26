## يعني إيه Instance؟

ببساطة جدًا:

> **Instance = Object تم إنشاؤه من Class معين.**

يعني لو عندنا:

```python
class User:
    pass
```

فالـ `User` هنا هو **Class**.

ولما نكتب:

```python
user1 = User()
```

Python تنشئ **Object** جديد من الـ `User`.

هذا الـ Object نقول عليه:

> **An instance of `User`**

يعني:

```text
User
 ↓
Class
 ↓
ينشئ
 ↓
user1
 ↓
Instance of User
```

---

## طيب ليه بنقول Instance بدل Object؟

لأن كلمة **Object** عامة جدًا.

كل Instance هو Object، لكن كلمة Instance بتضيف معلومة مهمة:

> **Object ده اتعمل من أنهي Class؟**

مثلاً:

```python
class User:
    pass

class Car:
    pass

user1 = User()
car1 = Car()
```

عندنا:

```text
user1
↓
Object
↓
Instance of User
```

و:

```text
car1
↓
Object
↓
Instance of Car
```

الاتنين Objects، لكن كل واحد **Instance من Class مختلف**.

---

## في مثالنا

لما تعمل:

```python
user = User("Mohamed", 18)
```

ممكن تقول:

> `User` هو الـ Class.

> `user` هو الـ Object.

> `user` هو **Instance of `User`**.

والـ Instance دي بعد تهيئتها بـ `__init__` أصبحت:

```text
user
├── name = "Mohamed"
└── age = 18
```

---

### تخيلها كده:

**Class = قالب تصنيع**

```text
┌──────────────┐
│     User     │
│   Blueprint  │
└──────────────┘
       │
       ├──────────────┐
       ↓              ↓
    user1           user2
   Instance         Instance
      ↓                ↓
 Mohamed            Ahmed
 18 years           25 years
```

فالـ **Instance مش حاجة مختلفة عن الـ Object** في المستوى اللي بنتعلم فيه الآن؛ غالبًا هتستخدم الكلمتين تقريبًا بنفس المعنى.

لكن لما حد يقول:

> "`user1` is an instance of `User`"

فهو بيقول لك تحديدًا:

> "`user1` هو Object تم إنشاؤه من الـ Class `User`."
