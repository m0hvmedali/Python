# ------------------------------------------------
# -- Object Oriented Programming => Inheritance --
# ------------------------------------------------

class Food:  # Base Class

  def __init__(self, name, price):

    self.name = name

    self.price = price

    print(f"{self.name} Is Created From Base Class")

  def eat(self):

    print("Eat Method From Base Class")

class Apple(Food):  # Derived Class

  def __init__(self, name, price, amount):

    # Food.__init__(self, name)  # Create Instance From Base Class

    super().__init__(name, price) #هتادي نفس النتيجه اللي فاتت بس دي مش هتكتب ال self ولا حتى اسم ال parent

    self.amount = amount

    print(f"{self.name} Is Created From Derived Class And Price Is {self.price} And Amount Is {self.amount}")

  def get_from_tree(self):

      print("Get From Tree From Derived Class")

# food_one = Food("Pizza")
food_two = Apple("Pizza", 150, 500)
food_two.eat()
food_two.get_from_tree()
# ══════════════════════════════════════════════════════════════════════════════
# ---------------------------------------------------------
# -- Object Oriented Programming => Multiple Inheritance --
# ---------------------------------------------------------

class BaseOne:

  def __init__(self):

    print("Base One")

  def func_one(self):

    print("One")

class BaseTwo:

  def __init__(self):

    print("Base Two")

  def func_two(self):

    print("Two")

class Derived(BaseOne, BaseTwo):

  pass

my_var = Derived()

# print(Derived.mro())

print(my_var.func_one)
print(my_var.func_two)

my_var.func_one()
my_var.func_two()

class Base:

  pass

class DerivedOne(Base):

  pass

class DerivedTwo(DerivedOne):

  pass