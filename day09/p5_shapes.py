# p5_three.py 把三种图形放进一个列表，用同一个循环打印它们的 describe()
import math

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError("子类必须实现 area()")

    def describe(self):
        return f"{self.name} 面积 {self.area():>6.2f}"

class Circle(Shape):
    def __init__(self, r):
        super().__init__("圆")
        self.r = r

    def area(self):
        return math.pi * self.r ** 2

class Rect(Shape):
    def __init__(self, w, h):
        super().__init__("矩形")
        self.w, self.h = w, h

    def area(self):
        return self.w * self.h

class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__("三角形")
        self.a, self.b, self.c = a, b, c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

for s in [Circle(2), Rect(3, 4), Triangle(3, 4, 5)]:
    print(s.describe())