# ╭────────────────────────────────────────────────────╮
# │ Topic: [classMethods, normalMothos& staticMethods] │
# ╰────────────────────────────────────────────────────╯
# Normal Method — Instance Method => hanble a object =دي الطريقة العادية، وبتتعامل مع نسخة معينة (object) من الـ class.
# هنا قصدنا ال method مرتبطه بال class نفسه ولا ب object معين ولا داله داخل ال class 

class User:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return f"Hello {self.name}"

user = User("mohamed")
print(user.say_hello())
# NOTE: so normal methods can reach self.anything
# ══════════════════════════════════════════════════════════════════════════════ #
# 2. Class Method => بتكون مرتبطه بال class نفسه مش ب object معين وبتاخد ال parameter الاول غالباcls

class Car :
    wheels = 4
    @classmethod
    def show_wheels(cls):
        return cls.wheels

print(Car.show_wheels()) 
# OUTPUT: 4

# NOTE: so classmethod can reach class.anything
# ══════════════════════════════════════════════════════════════════════════════ #
# 3. Static Method