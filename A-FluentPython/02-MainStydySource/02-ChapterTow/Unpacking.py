# ╭─────────────╮
# │ [UNPACKING] │
# ╰─────────────╯
# visit file:///C:\Users\moham\Documents\dev\Python\A-FluentPython\02-MainStydySource\02-ChapterTow\python_unpacking_skills.md
person = ('mohamed', 18)
# name = person[0] , age = person[1] #<1>
name, age = person #<2>
print(name)
print(age)
# OUTPUT: mohamed /n 18
# Topic: Unpacking, now we can ask a Q: what is hapoening here?
# person -> ('mohamed',18)
#                ↓      ↓
#              name    age 
#                ↓      ↓
#             mohamed   18
# NOTE: unpacking use ro unpack elem in an iter obj and def single elem to var
# NOTE: elem and var must be tje same number of values
# ══════════════════════════════════════════════════════════════════════════════
# ╭──────────────────╮
# │ [STAR UNPACKING] │
# ╰──────────────────╯
numbers = (10,20,30,40,50)

first,*rest = numbers
print(first,rest)
# OUTPUT: 10 [20, 30, 40, 50]
# Topic: Star unpacking, now ask Q: what is happend
# first we defind a valuse to (first,*rest) and we got a first number , list included the rest 
# ومش مهم انت حاطط ال rest فين بالمناسبه
# star can not take a value it can returns a empty list []
data = (10, 20)

a, *rest, b = data

print(a)
print(f"{rest}")
print(b)
# OUTPUT: 10 \n [] \n 20
# NOTE: الـ starred variable بياخد كل ما يمكنه أخذه \n لكن مع ترك عدد كافٍ من العناصر للمتغيرات العادية الموجودة حوله.
# ══════════════════════════════════════════════════════════════════════════════
# ╭────────────────────╮
# │ [Nested Unpacking] │
# ╰────────────────────╯
# Topic: عندنا Tuple بداخلها Tuple: 
data = ("Mohamed", (18, "Egypt")) #ممكن نفكها كده
name, (age, country) = data

print(name)
print(age)
print(country)
# OUTPUT: data → mohamed [name] 
#          ↓
#          18 → age , egypt → country

# Topic:  nested and star 
data = ("pyrhon ",(10,20,30,40)) # data 
language ,(*numbers,) = data #pattern:[pattern must match a data you unpacking it]
print(f"{language} \n{numbers}")
# OUTPUT: pyrhon \n [10, 20, 30, 40]
# ══════════════════════════════════════════════════════════════════════════════
# TODO: [x] basic unpacking -- [x] star unpacking -- [x] zero remainig elem -- [x] * -- [x] nested unpacking
# ══════════════════════════════════════════════════════════════════════════════
# ╭──────────────────────────────╮
# │ [Nested Unpacking in loops ] │
# ╰──────────────────────────────╯
students = [
    ("Mohamed", (18, "Python")),
    ("Ahmed", (20, "Java")),
    ("Ali", (19, "C++"))
]
for name , (age, lang) in students:
    print(name) 
    print(age)

# enumerate() في كل iteration بترجع tuple بالشكل:
# (0, "Python")
# (1, "SQL")
# (2, "JavaScript")

languages = ["Python", "SQL", "JavaScript"]

for index, language in enumerate(languages):
    print(index, language)

# OUTPUT: 0 Python 1 SQL 2 JavaScript
# ══════════════════════════════════════════════════════════════════════════════
# ╭─────────────────────────────────╮
# │ [Unpacking Arguments with sart] │
# ╰─────────────────────────────────╯
# NOTE: * في assignment  → يجمع * عند استدعاء function → يفك
def multiply(a, b, c):
    print(a * b * c)

numbers = (2, 3, 4)
multiply(*numbers)

def add(*numbers):
    print(numbers)

result =add(10,20,30)
# print(result)
def add(*numbers):
    print(type(numbers))
    print(numbers)


add(5, 10, 15)

def add(*numbers):
    print(numbers)


values = (10, 20, 30)

add(*values)
def test(a, b, *numbers):
    print(a)
    print(b)
    print(numbers)


values = (10, 20, 30, 40, 50)

test(*values)
def test(a, *numbers):
    print(a)
    print(numbers)

test(10, 20, 30, 40)
# ══════════════════════════════════════════════════════════════════════════════
# ╭─────────────────────╮
# │ [*args VS **kwargs] │
# ╰─────────────────────╯
# *args
#    ↓
# positional arguments
#    ↓
# tuple
# ----------------------
# **kwargs
#    ↓
# keyword arguments
#    ↓
# dictionary
def person(**info):
    print(info["name"])
    print(info["age"])


person(name="Mohamed", age=18)

def show(**data):
    print(type(data))
    print(data)

show(name="Mohamed", age=18, language="Python")

def person(name, *skills, **info):
    print(name)
    print(skills)
    print(info)

person(
    "Mohamed",
    "Python",
    "SQL",
    "Algorithms",
    age=18,
    country="Egypt"
)
# OUTPUT: Mohamed ('Python', 'SQL', 'Algorithms') \n {'age': 18, 'country': 'Egypt'}
# "Python"       ─┐
# "SQL"          ─┼── → *skills → tuple
# "Algorithms"   ─┘
# age=18          ─┐
# country="Egypt" ─┴── → **info → dict

def test(a, *numbers, **data):
    print(a)
    print(numbers)
    print(data)

test(10, 20, 30, 40, name="Mohamed", age=18)
# OUTPUT: 10 \n  (20, 30, 40) \n {'name': 'Mohamed', 'age': 18}

def student(name, age, language):
    print(name)
    print(age)
    print(language)


data = {
    "name": "Mohamed",
    "age": 18,
    "language": "Python"
}

student(**data)
# ══════════════════════════════════════════════════════════════════════════════
# Topic:  now we can see all screen 
# *args
# arguments → tuple

# *values
# tuple → arguments

# **kwargs
# arguments → dict

# **data
# dict → arguments
# args = (10, 20)
# kwargs = {"name": "Mohamed"}
# function(*args, **kwargs)
print('='*60)
def person(a, b, name, age):
    print(a)
    print(b)
    print(name)
    print(age)


args = (10, 20)
kwargs = {
    "name": "Mohamed",
    "age": 18
}

person(*args, **kwargs)

print('='*60)

def student(name, age, city):
    print(name, age, city)


data = ("Mohamed", 18)
info = {"city": "Alexandria"}

student(*data, **info)
print("="*60)
# ══════════════════════════════════════════════════════════════════════════════
# ╭────────────────────────╮
# │ [unpacking with zip()] │
# ╰────────────────────────╯
# NOTE: zip()generate a couple of data 
names = ["Mohamed", "Ahmed", "Ali"]
scores = [90, 85, 95]

for name, score in zip(names, scores): # zip take the first elem from name and score → gen  <1>
    # loop unpack <2>
    print(name, score)
print("="*60)

# Topic: dict.items() + unpacking 
student = {
    "name": "Mohamed",
    "age": 18,
    "language": "Python"
}
# NOTE: dict.items() return tuble contain key,value
for key, value in student.items(): #items() make couple of data, key,value → unpacking couples
    print(key, value)
print("="*60)

# ══════════════════════════════════════════════════════════════════════════════
# ╭───────────────────╮
# │ [dummy variables] │
# ╰───────────────────╯
# NOTE: dummy var is my tush in code 
person = ("Mohamed", 18, "Egypt")

name, _, country = person
# name, ignor this, cojntry
print(name)
print(country)