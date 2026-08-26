# ╔════════════════════════════════════════════════════════════════════════════╗
# ║ O ║ [class syntax and info] ║                                              ║
# ║ ╚═══════════════════════════════╝                                          ║
# ║ [01] Class is The Blueprint Or Construtor Of The Object                    ║
# ║ [02] Class Instantiate Means Create Instance of A Class                    ║
# ║ [03] Instance => Object Created From Class And Have Their Methods and      ║
# ║ Attributes                                                                 ║
# ║ [04] Class Defined With Keyword class                                      ║
# ║ [05] Class Name Written With PascalCase [UpperCamelCase]                   ║
# ║ [06] Class May Contains Methods and Attributes                             ║
# ║ [07] When Creating Object Python Look For The Built In __init__ Method     ║
# ║ [08] IMPORTANT:  __init__ Method Called Every Time You Create Object From  ║
# ║ Class                                                                      ║
# ║ [09] __init__ Method Is Initialize The Data For The Object                 ║
# ║ [10] Any Method With Two Underscore in The Start and End Called            ║
# ║ IMPORTANT:  Dunder or Magic Method                                         ║
# ║ [11] self Refer To The Current Instance Created From The Class And Must Be ║
# ║ First Param                                                                ║
# ║ [12] self Can Be Named Anything                                            ║
# ║ [13] In Python You Dont Need To Call new() Keyword To Create Object        ║
# ║ NOTE: Syntax                                                               ║
# ║ NOTE:  class Name:                                                         ║
# ║ NOTE:     Constructor => Do Instantiation [ Create Instance From A Class ] ║
# ║ NOTE:     Each Instance Is Separate Object                                 ║
# ║ NOTE:     def __init__(self, other_data)                                   ║
# ║ NOTE:         Body Of Function                                             ║
# ║ TODO: lean more information about the core and logic of OOP.               ║
# ╚════════════════════════════════════════════════════════════════════════════╝
# creat class
class User:
    # create constructor
    def __init__(self, name, age):
    # what is __init__? هنا حرفيا انت لما تنشئ object جديد بايثون بتشغل ال method دي تلقائيا وبتاخد ال data اللي انت عايز تخزنها في ال object وبتخزنها في attributes
        # create attributes
        self.name = name
        self.age = age
# create objects
user1 = User("Mohamed", 36)
user2 = User("Ahmed", 30)
# print attributes
print(user1.name, user1.age)
# OUTPUT: Mohamed 36
print(user2.name, user2.age)
# OUTPUT: Ahmed 30


# ══════════════════════════════════════════════════════════════════════════════
# مثال على ال init__ method
class User: 
    def hello(self):
        print("Hello From User Class")
# لازم عشان النتيجه تشتغل تشغل انت ال class بنفسك 
user = User()
user.hello() # OUTPUT: Hello From User Class 
# لو السطر ده مش موجود الداله بتاعتك مش هتتنفذ ولكن
# ----------------------------------------

class User:
    def __init__(self):
        print("Hello From User Class")
user = User()
# ══════════════════════════════════════════════════════════════════════════════
# مثال على ال self
# لما نكتب def __init__(self, name, age): ال self بيمثل ال object الحالي اللي بيتم التعامل معاه عمليا:
class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

user1 = User("Mohamed", 18)
# اثناء تنفيذ init ال self بتمثل ال object اللي هو user1 وبتخزن فيه ال attributes name و age في الميموري بتاعت ال object user1
# NOTE: self هو ممثل ومرجع للكائن الحالي داخل ال method 
# NOTE: user ==> استدعاء self ==> user1