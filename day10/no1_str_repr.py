# no.1
class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self):
        return f"《{self.title}》{self.price} 元"

    def __repr__(self):
        return f"Book({self.title!r}, {self.price!r})"

b = Book("流畅的 Python", 128.0)
print(b)
print(str(b))
print(repr(b))
print([b])