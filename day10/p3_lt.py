# p3_lt.py 能排序：__lt__ 按价格，验证 sorted(books) 和 reverse=True 都正常
class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self):
        return f"{self.title}({self.price})"
    
    def __lt__(self, other):
        return self.price < other.price
    
books = [Book("C 程序设计", 59.0), Book("流畅的 Python", 128.0), Book("算法导论", 99.0)]
for b in sorted(books):
    print("  ", b)
for b in sorted(books, reverse=True):
    print("  ", b)