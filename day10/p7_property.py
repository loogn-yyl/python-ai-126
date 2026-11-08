# p7_property.py 带校验的属性：price 用 @property + setter 拦住负数，total 做成只读计算属性
class Book:
    def __init__(self, title, price, count=1):
        self.title = title
        self.price = price
        self.count = count

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, v):
        if v < 0:
            raise ValueError("价格不能为负")
        self._price = v

    @property
    def total(self):
        return round(self._price * self.count, 2)

b = Book("算法导论", 99.0, 3)
print(b.price, b.total)
b.price = 100.0
print(b.total)
try:
    b.price = -5
except ValueError as e:
    print("ValueError:", e)
print(b.total)