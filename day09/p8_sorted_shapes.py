# p8_sort_three.py 图形报告（综合）：三种图形按面积从小到大排序输出，最后打印总面积
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

shapes = [Circle(2), Rect(3, 4), Triangle(3, 4, 5)]
for s in sorted(shapes, key=lambda x: x.area()):
    print(s.describe())

print(f"总面积:", f"{sum(s.area() for s in shapes):.2f}")