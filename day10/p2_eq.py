# p2_eq.py 能比较：__eq__ 按标题比，测四组：同书同名、同书异价、异书、跟字符串比
class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __eq__(self, other):
        return isinstance(other, Book) and self.title == other.title

a = Book("钢铁是怎样炼成的", 29.9)
b = Book("钢铁是怎样炼成的", 49.9)
c = Book("假如给我三天光明", 39.9)
print(a == b, a == c, a != c, a == "钢铁是怎样炼成的")