# no.3
class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self):
        return f"{self.title}({self.price})"

    def __lt__(self, other):
        return self.price < other.price

books = [Book("C 程序设计", 59.0), Book("流畅的 Python", 128.0), Book("算法导论", 99.0)]
print("默认按 price 升序:")
for b in sorted(books):
    print(" ", b)

print("按书名排 (key 优先于 __lt__):")
for b in sorted(books, key=lambda x: x.title):
    print(" ", b)