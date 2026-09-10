
import math

class Vector :
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __repr__(self):
        return f"({self.x!r},{self.y!r})"

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
        return Vector(x,y)

    def __mul__(self,scalar):
        return Vector(self.x*scalar,self.y*scalar)

    def dot (self,other):
        return (self.x * other.x)+(self.y * other.y)

    def cross(self,other):
        return (self.x * other.y) - (self.y * other.x)

v1=Vector(1,2)
v2 =Vector(3,4)
print(abs(v1))
print(v1+v2)
print(v1.cross(v2))
print(v1*5)
print(v1.dot(v2))
