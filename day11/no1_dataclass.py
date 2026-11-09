# no.1
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    price: float
    count: int = 1    # 有默认值的必须排在没有的后面, 否则会报错 TypeError

b = Book("流畅的 Python", 128.0)
print(b)
print(b.title, b.price, b.count)
print(b == Book("流畅的 Python", 128.0))
print(b == Book("流畅的 Python", 99.0))