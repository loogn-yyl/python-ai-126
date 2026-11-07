# p1_shape.py 基类：Shape(name)，area() 抛 NotImplementedError，写好 describe()，验证调用 area() 会抛错
import math

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError("子类必须实现 area()")

    def describe(self):
        return f"{self.name}, 面积 {self.area():.2f}"

s = Shape("神秘图形")
print(s.name)
try:
    s.area()
except NotImplementedError as e:
    print("报错:", e)