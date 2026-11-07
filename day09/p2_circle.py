# p2_circle.py 第一个子类：Circle(r)，用 super().__init__("圆")，算出面积 12.57
import math

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError("子类必须实现 area()")

class Circle(Shape):
    def __init__(self, r):
        super().__init__("圆")
        self.r = r

    def area(self):
        return math.pi * self.r ** 2

c = Circle(2)
print(c.name, f"{c.area():.2f}")
print(c.r)