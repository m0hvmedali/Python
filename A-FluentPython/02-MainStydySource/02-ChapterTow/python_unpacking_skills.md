# Python — Tuple & Iterable Unpacking

## 1. Basic Tuple Unpacking
```python
person = ("Mohamed", 18)
name, age = person
```
التوزيع حسب الترتيب. عدم تطابق عدد المتغيرات والقيم يسبب `ValueError`.

## 2. Star Unpacking `*` في Assignment
```python
numbers = (10, 20, 30, 40, 50)
first, *rest = numbers
# first = 10
# rest = [20, 30, 40, 50]
```
المتغير الذي يستخدم `*` يحصل على `list`.

```python
first, *middle, last = numbers
# middle = [20, 30, 40]
```
يمكن أن تكون القائمة المجمعة فارغة:
```python
a, *rest = (10,)       # rest = []
a, *rest, b = (10, 20) # rest = []
```
ولا يمكن وجود أكثر من starred expression:
```python
a, *b, *c = (1, 2, 3)  # SyntaxError
```

## 3. Nested Unpacking
```python
data = ("Mohamed", (18, "Egypt"))
name, (age, country) = data
```
شكل الـ unpacking في الطرف الأيسر يعكس بنية البيانات.

```python
name, (age, *skills) = ("Mohamed", (18, "Python", "SQL"))
```

## 4. Unpacking داخل `for`
```python
students = [("Mohamed", 18), ("Ahmed", 20)]
for name, age in students:
    print(name, age)
```
وهو مكافئ مفهوميًا لـ:
```python
for student in students:
    name, age = student
```

## 5. `enumerate()` + Unpacking
`enumerate()` تنتج tuples من `index` و `value`:
```python
for index, language in enumerate(languages):
    print(index, language)
```

## 6. Star Unpacking داخل `for`
```python
data = [
    ("Python", 3, 10, 20, 30),
    ("SQL", 4, 100),
]

for language, version, *numbers in data:
    print(language, version, numbers)
```
`numbers` تكون `list` وقد تكون فارغة.

## 7. `*` في Function Call
يفك أي iterable إلى positional arguments:
```python
def add(a, b, c):
    print(a + b + c)

numbers = (10, 20, 30)
add(*numbers)
```
مكافئ لـ:
```python
add(10, 20, 30)
```
يعمل مع `tuple` و`list` و`string` وغيرها من iterables.

## 8. `*args` في Function Definition
يجمع positional arguments في `tuple`:
```python
def add(*numbers):
    print(numbers)

add(10, 20, 30)
# numbers = (10, 20, 30)
```
اسم `args` اختياري؛ النجمة هي المهمة.

## 9. Fixed Parameters + `*args`
```python
def test(a, b, *numbers):
    print(a, b, numbers)

test(10, 20, 30, 40, 50)
# a = 10
# b = 20
# numbers = (30, 40, 50)
```

## 10. `**kwargs`
يجمع keyword arguments في `dict`:
```python
def test(**data):
    print(data)

test(name="Mohamed", age=18)
# {'name': 'Mohamed', 'age': 18}
```
اسم `kwargs` اختياري.

## 11. Normal Parameters + `*args` + `**kwargs`
```python
def person(name, *skills, **info):
    print(name)
    print(skills)
    print(info)

person("Mohamed", "Python", "SQL", age=18, country="Egypt")
```
النتيجة:
```text
name = "Mohamed"
skills = ("Python", "SQL")
info = {"age": 18, "country": "Egypt"}
```

## 12. `**` في Function Call
يفك dictionary إلى keyword arguments:
```python
data = {"name": "Mohamed", "age": 18}

def person(name, age):
    print(name, age)

person(**data)
```
مكافئ لـ:
```python
person(name="Mohamed", age=18)
```
مفاتيح الـ dictionary يجب أن تتوافق مع أسماء parameters.

## 13. `*` و `**` معًا في Function Call
```python
def person(a, b, name, age):
    print(a, b, name, age)

args = (10, 20)
kwargs = {"name": "Mohamed", "age": 18}

person(*args, **kwargs)
```
مكافئ لـ:
```python
person(10, 20, name="Mohamed", age=18)
```

## 14. `zip()` + Unpacking
```python
names = ["Mohamed", "Ahmed", "Ali"]
ages = [18, 20, 19]

for name, age in zip(names, ages):
    print(name, age)
```
`zip()` تنتج tuples مثل:
```python
("Mohamed", 18)
```
ثم يحدث unpacking داخل `for`.

## 15. `dict.items()` + Unpacking
```python
student = {"name": "Mohamed", "age": 18}

for key, value in student.items():
    print(key, value)
```
كل عنصر من `items()` يكون زوجًا من `(key, value)`.

## 16. تجاهل القيم باستخدام `_`
```python
person = ("Mohamed", 18, "Egypt")
name, _, country = person
```
`_` اسم متغير شائع للدلالة على أن القيمة غير مهمة لنا.

```python
data = ("Mohamed", 18, "Python", "Egypt")
name, _, language, _ = data
```

## 17. Unpacking مع `return`
الدالة يمكن أن ترجع أكثر من قيمة:
```python
def get_data():
    return "Mohamed", 18

name, age = get_data()
```
مفهوميًا:
```python
name, age = ("Mohamed", 18)
```
ومع `*`:
```python
def get_data():
    return "Mohamed", 18, "Python", "Egypt"

name, *rest = get_data()
# rest = [18, "Python", "Egypt"]
```

## 18. Swapping باستخدام Unpacking
```python
a = 10
b = 20

a, b = b, a
```
النتيجة:
```text
a = 20
b = 10
```
مفهوميًا:
```python
a, b = (b, a)
```

## 19. Packing vs Unpacking
### Packing
تجميع عدة قيم في container:
```python
numbers = 10, 20, 30
# numbers = (10, 20, 30)
```
وكذلك:
```python
def test(*args):
    print(args)

test(10, 20, 30)
# args = (10, 20, 30)
```

### Unpacking
تفكيك container إلى قيم:
```python
numbers = (10, 20, 30)
a, b, c = numbers
```
أو:
```python
test(*numbers)
```

# القواعد الأساسية للحفظ
```text
* في Function Definition
→ يجمع positional arguments
→ النتيجة tuple

* في Function Call
→ يفك iterable
→ إلى positional arguments

** في Function Definition
→ يجمع keyword arguments
→ النتيجة dict

** في Function Call
→ يفك dict
→ إلى keyword arguments
```

## Mastery Checklist
- [x] Basic tuple unpacking
- [x] Positional matching
- [x] `*` extended unpacking
- [x] Nested unpacking
- [x] Unpacking in `for`
- [x] `enumerate()` + unpacking
- [x] `*args`
- [x] `**kwargs`
- [x] `*` in function calls
- [x] `**` in function calls
- [x] `*` + `**` together
- [x] `zip()` + unpacking
- [x] `dict.items()` + unpacking
- [x] `_` to ignore values
- [x] Unpacking function returns
- [x] Swapping variables
- [x] Packing vs Unpacking
