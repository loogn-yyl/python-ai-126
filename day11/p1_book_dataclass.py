# p1_book_dataclass.py 第一个 dataclass：Book(title, price, count=1)，造两本看 __repr__ 自动长什么样
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    price: float
    count: int = 1

a = Book("钢铁是怎样炼成的", 29.9)
b = Book("假如给我三天光明", 39.9, 3)
print(a)
print(b)
print(a.count, b.count)