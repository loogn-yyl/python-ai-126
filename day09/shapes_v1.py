import math

class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r ** 2

    def describe(self):
        return f"圆, 面积 {self.area():.2f}"

class Rect:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def describe(self):
        return f"矩阵, 面积 {self.area():.2f}"

for s in [Circle(2), Rect(3, 4)]:
    print(s.describe())