# p5_shelf.py 像容器：Shelf 写 __len__ / __getitem__ / __iter__，验证 len()、下标、负下标、切片、for、推导式
class Shelf:
    def __init__(self):
        self.books = []

    def add(self, title):
        self.books.append(title)

    def __len__(self):
        return len(self.books)

    def __getitem__(self, key):
        return self.books[key]

    def __iter__(self):
        return iter(self.books)

s = Shelf()
s.add("钢铁是怎样炼成的")
s.add("假如给我三天光明")
print(len(s))
print(s[0])
print(s[-1])
print(s[0: 2])
for name in s:
    print("  读完了:", name)
print([n for n in s if "三天" in n])