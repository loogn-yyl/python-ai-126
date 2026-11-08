# p1_str_repr.py 能打印：给 Book 写 __str__ 和 __repr__，验证 print(b) 和 print([b, b]) 输出不同
class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self):
        return f"《{self.title}》: {self.price} 元"

    def __repr__(self):
        return f"Book({self.title!r}, {self.price!r})"

b = Book("钢铁是怎样炼成的", 29.9)
print(b)
print(repr(b))
print([b, b])