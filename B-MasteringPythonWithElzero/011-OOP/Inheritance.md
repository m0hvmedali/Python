| Front (Question) | Back (Answer) |
| --- | --- |
| What does object-oriented inheritance mean in Python? | A mechanism where a child class derives attributes and methods from a parent class without rewriting them. |
| What is the parent class called in Python OOP? | Base class (or parent class). |
| What is the child class called in Python OOP? | Derived class (or child class). |
| How do you declare that class `Apple` inherits from class `Food`? | Define the class as `class Apple(Food):`. |
| Does a child class automatically invoke the parent's `__init__` constructor? | No, it must be explicitly called inside the child's constructor. |
| What is the modern way to call a parent class constructor in Python? | Use `super().__init__(args)`. |
| What is the legacy way to call a parent class constructor directly? | Use `ParentClassName.__init__(self, args)`. |
| Why is `super()` preferred over calling the parent class by name? | It is cleaner and correctly resolves method lookup order in multiple inheritance. |
| What is method overriding in Python OOP? | Defining a method in the child class with the same name as one in the parent class to replace its behavior. |
| What is method resolution order (MRO)? | The order Python follows to search for a method or attribute up the class hierarchy. |
| What happens when a child class calls a method it does not define? | Python searches for and executes the method from the base class. |