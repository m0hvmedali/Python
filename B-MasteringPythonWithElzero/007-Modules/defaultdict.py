from collections import defaultdict
# ╭──────────────────────╮
# │ -- │ defaultdict │-- │
# ╰──────────────────────╯
# ال dict هو نوع بيانات في بايثون بيسمحلك تكتب key => value
my_dict ={
    "fname":"mohamed",
    "lname":"aly",
    "age": 19
}
print(my_dict)
# OUTPUT: {'fname': 'mohamed', 'lname': 'aly', 'age': 19}
print("="*50)
# ونقدر نوصل لقيمه واحده عن طريق مفتاحها 
print(my_dict["fname"])
print(my_dict.get("fname"))
print("="*50)
# OUTPUT: mohamed
# نقدر نوصل لكل القيم او كل المفاتيح
print(my_dict.keys())
print(my_dict.values())
print("="*50)
# OUTPUT: dict_keys(['fname', 'lname', 'age'])  dict_values(['mohamed', 'aly', 19])
# واقدر اجيب عدد العناصر
print(len(my_dict))
print(len(my_dict["fname"]))
print("="*50)
# ══════════════════════════════════════════════════════════════════════════════
# FUNCTION: clear() => مهمه بسيطه عندك قاموس وعايز تفضيه
user_skills = {
    "mohamed":{
        "language" : "python",
        "progress" : "90%"
    },
    "rahma":{
            "language" : "c++",
            "progress" : "80%"
        }
}
user_skills.clear()
print(user_skills)
# OUTPUT: {}
print("="*50)
# ══════════════════════════════════════════════════════════════════════════════
# FUNCTION: update()=> بتضيف مفتاح وقيمه جديده 
member = {
    "name": "Osama"
}
print(member)
member["age"] = 36
print(member)
member.update({"country": "Egypt"})
print(member)
print("="*50)
# ══════════════════════════════════════════════════════════════════════════════
# FUNCTION: copy()=> بتاخد نسخه من القاموس بتاعك وتحفظها في متغير
main = {
    "name": "Osama"
}
b = main.copy()
print(b)
main.update({"skills": "Fighting"})
print(main)
print(b)
print("="*50)
# ══════════════════════════════════════════════════════════════════════════════
# FUNCTION: setdefault()=>اضافه مفتاح بقيمه افتراضيه
user = {
    "name": "Osama"
}
print(user)
print(user.setdefault("age", 19))
print(user)
print("=" * 40)
# ══════════════════════════════════════════════════════════════════════════════
# FUNCTION: items()=> بتاخد dict وترجعلي كائن باسم dict_items في list عبارة عن tuples كل tuple عبارة عن (key,value)
view = {
  "name": "Osama",
  "skill": "XBox"
}

allItems = view.items()
print(view)
view["age"] = 36

print(allItems)
# OUTPUT: {'name': 'Osama', 'skill': 'XBox'} , dict_items([('name', 'Osama'), ('skill', 'XBox'), ('age', 36)])
print("=" * 40)
# ══════════════════════════════════════════════════════════════════════════════
# FUNCTION: fromkeys => بتاخد مني iterable يمثل ال keys و بتاخد مني value
# dict.fromkeys(iterable, value=None)
keys = ["status", "code", "retry"]

# إنشاء قاموس بقيمة افتراضية None
res1 = dict.fromkeys(keys)
print(res1)  # Output: {'status': None, 'code': None, 'retry': None}

# إنشاء قاموس بقيمة افتراضية مخصصة
res2 = dict.fromkeys(keys, 0)
print(res2)  # Output: {'status': 0, 'code': 0, 'retry': 0}
print("=" * 40)
# ══════════════════════════════════════════════════════════════════════════════
# FUNCTION: popitem()=> بتحذف اخر عنصر وترجعهولي في tuple يحتوي على (Key, Value)
user = {"name": "Ahmed", "role": "Engineer", "level": 5}

# إزالة آخر عنصر تم إضافته
last_item = user.popitem()

print(last_item)  # Output: ('level', 5)
print(user)  # Output: {'name': 'Ahmed', 'role': 'Engineer'}
print("=" * 40)
# ══════════════════════════════════════════════════════════════════════════════
# NOTE: الحقيقه ان المشكله الاساسيه اللي واجهتنا هى لما نحاول نوصل لمفتاح غير موجود هنلاقي ان بايثون مطلعلنا KeyError , وده يجبرني على اضافه شرط اختبار ان ال key بتاعنا if is not in myDict: myDict[key]=0     myDict[key]+=1 كدا عملنا اختبار للمفتاح لو موجود بايثون هتتخطى الشرط لو مش موجود هينشئه اولا ثم يخرج من الشرط ويزود عليه واحد بايثون قدمت حل ظريف 
# بدل ما اكتبها كدا counts = {}
# هيبقا الشكل 
# use int
counts = defaultdict(int)
# دلوقتي نجرب
counts['apple'] +=1
counts['apple'] +=1
print(counts)
print("=" * 40)
# NOTE: انواع القيم الافتراضيه [defaultdict(int): القيمة الافتراضية للمفتاح الجديد هي 0 (ممتاز لحساب التكرارات)., defaultdict(list): القيمة الافتراضية هي قائمة فارغة [] (ممتاز لتجميع العناصر في مجموعات) , defaultdict(set): القيمة الافتراضية هي مجموعة فارغة set() (ممتاز لتجميع عناصر فريدة بدون تكرار)]
# ══════════════════════════════════════════════════════════════════════════════
# use list
sales_data = [
    ('القاهرة', 'شاشة', 5000),
    ('الإسكندرية', 'هاتف', 8000),
    ('القاهرة', 'لوحة مفاتيح', 300),
    ('الإسكندرية', 'سماعة', 1200),
    ('القاهرة', 'شاشة', 5000)  # تكرار عملية شراء
]
# الهدف نعمل قاموس بيضم المدينه كمفتاح والقيمه بتاعتها هتكون ال product,price 
# بما انها اكثر من عنصر واحد الافضل نخليه في list يبقا
city_sales = defaultdict(list)
# نعمل loop ونطلع قيم المدن
for city, product, price in sales_data :
    city_sales[city].append((product,price))
print(dict(city_sales))
print("=" * 40)
# OUTPUT: {'القاهرة': [('شاشة', 5000), ('لوحة مفاتيح', 300), ('شاشة', 5000)], 'الإسكندرية': [('هاتف', 8000), ('سماعة', 1200)]}
# ══════════════════════════════════════════════════════════════════════════════
# use set
skills_log = [
    ('أحمد', 'Python'),
    ('سارة', 'SQL'),
    ('أحمد', 'Git'),
    ('أحمد', 'Python'),  # مهارة مكررة
    ('سارة', 'Python')
]
employee_skills = defaultdict(set)
for name, skill in skills_log:
    employee_skills[name].add(skill)
print(dict(employee_skills))
# OUTPUT: {'أحمد': {'Python', 'Git'}, 'سارة': {'SQL', 'Python'}}
print('='*40)
# ══════════════════════════════════════════════════════════════════════════════
# Topic: (Nested Grouping) => defaultdict(lambda: defaultdict(...))
# عشان نفهم الموضوع ده لازم نفهم حاجه بسيطه جدا بس عن طريق المثال الاتي
# app_logs = defaultdict(lambda: defaultdict(list))
# app_logs['App_A']['ERROR'].append('فشل الاتصال')
# اللي بيحصل هنا ان مترجم بايثون اولا يقوم بانشاء الكائن app_logs بعدها هيلاقي الوسيط الممرر lambda: defaultdict(list) هيحتفظ بيه في ال default_factory. والمفهوم ده هنرجعله بعدين بس خليك معايا وهينشا كائن جديد من الكلاس dict ثم يربط app_logs بمكان هذا الكائن كدا خلصنا من السطر الاول تقريبا بعدها app_logs['App_A'] الامر ده خلاه يستدعي داله البحث __getitem__('App_A') داخل app_logs ثم ملقاش القيمه موجوده فورا يستدعي __missing__('App_A') تقوم ب
# --> استدعاء الداله المخزنه في default_factory وهى lambda()
# --> تشغيل lambda()
# --> انشاء dict فرعي >default_factory = list
# --> اسناد هذا القاموس لمعامل __missing__ = App_A
# --> ارجاع القاموس الفرعي الجديد لتكمله الكود 
# --> الشكل الحالي في الذاكرة {'App_A': defaultdict(list, {})}
##########################################################
# الان يبحث عن ERROR داخل App_A ملقهاش
# ينفذ يتم استدعاء دالة __missing__('ERROR') الخاصة بالقاموس الفرعي
# default_factory -->تنشئ قائمة فارغة جديدة [], تُسند هذه القائمة للمفتاح 'ERROR' داخل القاموس الفرعي.
# الشكل الحالي بالذاكرة {'App_A': {'ERROR': []}}
# تنفيذ  append على القائمه المستدعاه
# اضافه فشل الاتصال
# دلوقتي نقدر ناخد مثال عملي 
app_logs = defaultdict(lambda: defaultdict(list)) # الحصول على قاموس داخل قاموس
logs = [
    ('App_A', 'ERROR', 'فشل الاتصال بالخادم'),
    ('App_B', 'WARNING', 'الذاكرة منخفضة'),
    ('App_A', 'ERROR', 'خطأ في قاعدة البيانات'),
    ('App_A', 'INFO', 'تم تسجيل الدخول')
] #تسجيل اخطاء تطبيق (اسم التطبيق , درجه الخطا,رساله الخطا)
for appName,level,msg in logs :
    app_logs[appName][level].append(msg)

print(app_logs['App_A']['ERROR'])


