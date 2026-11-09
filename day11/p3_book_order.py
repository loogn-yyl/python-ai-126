# p3_book_order.py 能排序：加 order=True，按价格排序；顺便试试 books[0] > books[1] 也能用
from dataclasses import dataclass

@dataclass(order=True)
class Book:
    price: float
    title: str

books = [Book(29.9, "钢铁是怎样炼成的"), Book(39.9, "假如给我三天光明"), Book(25.9, "鲁滨逊漂流记")]
print(books[0] > books[1])
for b in sorted(books):
    print(b.title, b.price)
print(books[0] > books[1])