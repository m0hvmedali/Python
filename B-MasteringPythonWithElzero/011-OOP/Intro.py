# ┌─────────────────────────┐
# │   OOP Introduction      │
# └─────────────────────────┘
# ══════════════════════════════════════════════════════════════════════════════
# NOTE : in the past we used procedures paradigm : بيانات
#        ↓
#        Functions
#        ↓
#        بيانات
#        ↓
#        Functions
# NOTE: :  in oop we use : data -> method -> data -> method 
# ══════════════════════════════════════════════════════════════════════════════
# تاريخ البرمجه الكائنيه هو لغه simula___1960s طورت اللغه مفهوم class و object بشكل مبكر خصوصا للمحاكات الفكره كانت كالاتي
# لو عندك محاكاه لمجموعه اشخاص 
#  Person:
#  ├── name
#  ├── age
#  ├── position
#  └── move()
# بدلا ن ان تكون البيانات منفصله بدات فكره :Everything is an object.
# QUESTION: What is a object?
# ANSWER: An object is a collection of data (variables) and methods (functions)
# for example: user have a name and age and can move, also have a behavior (methods) like move() and eat() and sleep()
# IMPORTANT: Object = State + Behavior

#            User
#             │
#       ┌─────┴─────┐
#       ↓           ↓
#    user1        user2
#  Mohamed         Ahmed
# Now we can ask a QUESTION: what is a class?
# its a blueprint for creating objects, imagine with me you want to creat a app include users every user have a shared info such as [name, age, email] & have a behavior [login(), logout(), update_profile()] wait a minute actuakky we can use a function and old way we learn to create a user but the case is we do not wanna repeat the same code for every user we want to create, so we can use a class to create a blueprint for creating users and then we can create as many users as we want from that class follow the example below:
class User:
    # NOTE: هنا انت فعليا بتقول ل python انا دلوقتي هبدا تعريف class اسمه user والكود اللي جاي تابع لل class ده وده معناه ان ال class ده هيكل ومخطط لكائن اللي هيتعمل منه object
     #ok the system expected indented=(suffix space) block=(groub of code) after `class` definition
    #  المخطط ده ليه صفات (Attributes)ودي المعلومات اللتي تصف الكائن 
    # وليه سلوكيات (Methods) ودي اللي بتحدد تصرفات الكائن
    name = "Mohamed"
    age = 36
user = User() # هنا انت فعليا بتقول ل python انا دلوقتي هبدا تعريف object اسمه user والكود اللي جاي تابع لل object ده وده معناه ان ال object ده هيتم انشاءه من ال class اللي اسمه user
print(user.name) 
# OUTPUT:  Mohamed
print(user.age)
# OUTPUT: 36
# ═══════════════════════════════════ ***END***  ═══════════════════════════════════════════
                                                                                