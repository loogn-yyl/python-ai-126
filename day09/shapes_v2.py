import math

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError("子类必须实现 area()")

    def describe(self):
        return f"{self.name}, 面积 {self.area():.2f}"

class Circle(Shape):
    def __init__(self, r):
        super().__init__("圆")
        self.r = r

    def area(self):
        return math.pi * self.r ** 2

class Rect(Shape):
    def __init__(self, w, h):
        super().__init__("矩形")
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

for s in [Circle(2), Rect(3, 4)]:
    print(s.describe())

print(isinstance(Circle(2), Shape))
print(type(Circle(2)) is Shape)