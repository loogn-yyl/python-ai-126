# p8_books.py 图书清单（综合）：四个方法齐上，sorted() 按价格、按书名各排一次，set() 去重，最后算总价
class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self):
        return f"《{self.title}》{self.price:.1f} 元"

    def __repr__(self):
        return f"Book({self.title!r}, {self.price!r})"

    def __lt__(self, other):
        return self.price < other.price

    def __eq__(self, other):
        return isinstance(other, Book) and self.price == other.price

    def __hash__(self):
        return hash(self.title)

books = [
    Book("流畅的 Python", 128.0),
    Book("算法导论", 99.0),
    Book("C 程序设计", 59.0),
    Book("算法导论", 99.0),          # 重复的一本
]

print("按价格从低到高:")
for b in sorted(books):
    print("  ", b)

print("按书名:")
# 中文按拼音序无关，这里是码点序
for b in sorted(books, key=lambda x: x.title):
    print("  ", b)

unique = sorted(set(books))
print("去掉重复后: ", len(unique), "本")
print("总价: ", sum(b.price for b in unique))
print(unique[0] < unique[-1], unique[0] == Book("C 程序设计", 0))