# ────────────────────────────────── __init__ ───────────────────────────────────#
# عندنا  
class User:
    pass
# وعايزين نعمل كائن 
user1 = User()
# بايثون انشئت الكائن بنجاح ولكن الuser ده في ايه؟ حاليه مفيهوش اي بيانات هاصه بالمستخدم احنا عايزين لما نعمل كائن جديد من ال class User نقدر نخزن فيه بيانات المستخدم زي الاسم والعمر مثلا
class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age
# User
# ┌──────────────┐
# │ Name:        │
# │ Age:         │
# │ Email:       │
# └──────────────┘
# step 1: user = User("Mohamed", 18)
# pythos:  ok i do this now , where is __init__
#__init__ : what python ?
# python : dev need to create name & age attributes for the user object dev gave me "mohamed" and 18 
# # __init__ : ok i understand he want a create name as mohamed and age as 18, ok python i am done tak it : __init__
#    │
#    ├── name = "Mohamed"
#    └── age = 18
# self: hello world, I received data and i do that: self.name = mohamed, self.age= 18, Python take it :user
# ├── name = "Mohamed"
# └── age = 18
# المبرمج
#    │
#    │ User("Mohamed", 18)
#    ↓
# Python
#    │
#    │ تنشئ Instance
#    ↓
# Object
#    │
#    │ تستدعي __init__
#    ↓
# __init__
#    │
#    ├── self → الـ Object
#    ├── name → "Mohamed"
#    └── age  → 18
#    │
#    │ تنفذ:
#    │
#    ├── self.name = name
#    └── self.age = age
#    │
#    ↓
# Object
# ├── name = "Mohamed"
# └── age = 18