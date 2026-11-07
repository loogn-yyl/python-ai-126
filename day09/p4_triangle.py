# p4_triangle.py 第三个子类：Triangle(a, b, c)，用海伦公式，3/4/5 的答案正好是 6
import math

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError("子类必须实现 area()")

class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__("三角形")
        self.a, self.b, self.c = a, b, c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

t = Triangle(3, 4, 5)
print(t.name, t.area())
print(t.a, t.b, t.c)