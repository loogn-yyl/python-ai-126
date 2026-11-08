# no.4
class Shelf:
    def __init__(self, books):
        self.books = list(books)

    def __len__(self):
        return len(self.books)

    def __getitem__(self, i):
        return self.books[i]

    def __iter__(self):
        return iter(self.books)

s = Shelf(["C 程序设计", "流畅的 Python", "算法导论"])
print(len(s))
print(s[0])
print(s[-1])
for name in s:
    print("  读完了:", name)
print([n for n in s if "Python" in n])