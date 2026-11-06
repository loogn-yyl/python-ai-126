# p1_book.py 第一个类：Book 类，两个属性 title / price，造两本书并打印

class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

a = Book("假如给我三天光明", 20)
b = Book("钢铁是怎样炼成的", 25)

print(a.title, a.price)
print(b.title, b.price)