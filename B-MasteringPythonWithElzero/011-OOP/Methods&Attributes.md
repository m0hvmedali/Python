## 1. Attributes يعني إيه؟

**Attribute = معلومة أو خاصية موجودة في الـ Object.**

يعني حاجة **تصف حالة الـ Object**.

مثلاً عندنا:

```python
class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

لما نعمل:

```python
user = User("Mohamed", 18)
```

الـ Object بقى عنده:

```text
user
├── name = "Mohamed"  ← Attribute
└── age = 18          ← Attribute
```

إذن:

```python
user.name
user.age
```

دول Attributes.

### تخيل الـ User شخص حقيقي:

```text
User
│
├── name       ← صفة
├── age        ← صفة
├── email      ← صفة
└── password   ← صفة
```

كل دي **بيانات تصف الـ User**.

---

# 2. Methods يعني إيه؟

**Method = دالة موجودة داخل الـ Class، وتمثل سلوكًا يستطيع الـ Object القيام به.**

مثلاً:

```python
class User:

    def login(self):
        print("User logged in")
```

هنا:

```text
login()
```

هي Method.

ولما تعمل:

```python
user.login()
```

أنت بتقول:

> يا `user`، نفّذ السلوك `login`.

---

# الفرق بينهم

فكر في Object كأنه شخص:

```text
                 User Object
                     │
          ┌──────────┴──────────┐
          ↓                     ↓
      Attributes             Methods
          │                     │
      name = Mohamed          login()
      age = 18                logout()
      email = ...             change_password()
```

**Attributes = "هو عنده إيه؟"**

**Methods = "هو يقدر يعمل إيه؟"**

---

## مثال كامل

```python
class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}")

    def login(self):
        print(f"{self.name} logged in")
```

لما نعمل:

```python
user = User("Mohamed", 18)
```

عندنا:

### Attributes:

```python
user.name
user.age
```

### Methods:

```python
user.introduce()
user.login()
```

---

## ولاحظ حاجة مهمة جدًا

الـ `__init__` نفسها **Method**.

يعني عندنا:

```python
class User:

    def __init__(self, name, age):
        ...
```

`__init__` = Method خاصة.

وعندنا:

```python
def login(self):
    ...
```

`login` = Method عادية.

فممكن نقول:

```text
Class
│
├── Attributes
│
└── Methods
      │
      ├── __init__()
      ├── login()
      └── introduce()
```

---

### احفظها بالشكل ده:

> **Attribute = شيء يملكه/يصف الـ Object.**

> **Method = شيء يستطيع الـ Object فعله.**

وده هيقودنا مباشرة للسؤال المهم جدًا التالي: **إيه الفرق بين Function و Method؟** لأن `Method` أصلًا هي Function لكن لما تكون مرتبطة بـ Object/Class بيحصل فرق مهم.
بالضبط، ودي نقطة مهمة جدًا لأن **كل Method هي Function، لكن مش كل Function هي Method**.

## 1. Function

الـ **Function** هي دالة عادية مستقلة عن الـ Class.

```python
def say_hello():
    print("Hello")
```

وتشغلها مباشرة:

```python
say_hello()
```

هي مش مرتبطة بـ Object معين.

---

## 2. Method

الـ **Method** هي Function مكتوبة داخل Class ومرتبطة بالـ Object/Class.

```python
class User:

    def login(self):
        print("Logged in")
```

هنا `login` تعتبر Method.

وبتشغلها من خلال Object:

```python
user = User()

user.login()
```

لاحظ الفرق:

```text
Function
   ↓
say_hello()
```

مستقلة.

بينما:

```text
Object
  ↓
user
  ↓
login()
```

الـ `login()` مرتبطة بالـ `user`.

---

# طب إيه قصة `self`؟

هنا الفرق بيبان أكتر.

Function عادية:

```python
def add(a, b):
    return a + b
```

تناديها:

```python
add(5, 3)
```

لكن Method:

```python
class Calculator:

    def add(self, a, b):
        return a + b
```

تناديها:

```python
calc = Calculator()

calc.add(5, 3)
```

Python بتتعامل معها بحيث الـ Object الحالي يُمرر كأول argument، وهو اللي بنسميه:

```python
self
```

فممكن تفكر فيها بشكل مبسط:

```text
calc.add(5, 3)

        ↓

add(calc, 5, 3)
```

وده **تصور مبسط جدًا ومفيد** لفهم `self`.

---

# مثال يوضح الفكرة أكثر

عندنا:

```python
class User:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}")
```

نعمل:

```python
user1 = User("Mohamed")
user2 = User("Ahmed")
```

وبعدين:

```python
user1.introduce()
```

الـ Method تعرف إن:

```text
self → user1
```

فتقرأ:

```python
self.name
```

كأنها:

```python
user1.name
```

فتطبع:

```text
My name is Mohamed
```

أما:

```python
user2.introduce()
```

فـ:

```text
self → user2
```

فتقرأ:

```python
user2.name
```

وتطبع:

```text
My name is Ahmed
```

---

## الخلاصة

| Function                   | Method                           |
| -------------------------- | -------------------------------- |
| مستقلة                     | موجودة داخل Class                |
| لا تحتاج Object لاستدعائها | غالبًا تُستدعى من Object         |
| `self` مش موجود تلقائيًا   | أول parameter تقليديًا هو `self` |
| `add(5, 3)`                | `user.login()`                   |

فلو شفت:

```python
def something():
```

خارج Class → **Function**

ولو شفت:

```python
class User:
    def something(self):
```

داخل Class → **Method**

**والـ `__init__` اللي كنا بنتكلم عنها هي Method خاصة، لأننا كتبناها داخل الـ Class، لكن Python لها تعامل خاص معها عند إنشاء الـ Instance.**
