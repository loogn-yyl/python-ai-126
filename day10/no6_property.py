# no.6-1
class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, v):
        if v < 0:
            raise ValueError("价格不能为负")
        self._price = v

b = Book("流畅的 Python", 128.0)
print(b.price)
b.price = 99.9
print(b.price)
try:
    b.price = -1
except ValueError as e:
    print("ValueError:", e)
print("价格还是:", b.price)

# no.6-2
class Order:
    def __init__(self, price, count):
        self.price = price
        self.count = count

    @property
    def total(self):
        return self.price * self.count

o = Order(59.0, 3)
print(o.total)
try:
    o.total = 100
except AttributeError as e:
    print("AttributeError:", e)

# no.6-3
class Demo:
    count = 0

    def __init__(self, v):
        self.v = v
        Demo.count += 1

    def normal(self):
        return f"normal: {self.v}"

    @classmethod
    def cls_info(cls):
        return f"cls: {cls.__name__}, count={cls.count}"

    @staticmethod
    def helper(x):
        return f"static: {x}"

    @property
    def double(self):
        return self.v * 2

d = Demo(21)
print(d.normal())
print(Demo.cls_info())
print(Demo.helper("不用对象"))
print(d.double, d.double)