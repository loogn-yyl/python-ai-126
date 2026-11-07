# p6_abstract.py 抽象基类：用 ABC + @abstractmethod 改造 Shape，用 try 接住实例化时的 TypeError 并打印出来
import math
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        ...

class Circle(Shape):
    def __init__(self, r):
        super().__init__("圆")
        self.r = r

    def area(self):
        return math.pi * self.r ** 2
    
print(f"{Circle(2).area():.2f}")

try:
    Shape("抽象图形")
except TypeError as e:
    print("报错:", e)