# p4_hash.py 能去重：补 __hash__，用 set 去掉重复的书，并验证 in 能查到
class Book:
    def __init__(self, title):
        self.title = title

    def __eq__(self, other):
        return isinstance(other, Book) and self.title == other.title
    
    def __hash__(self):
        return hash(self.title)

books = {Book("算法导论"), Book("算法导论"), Book("流畅的 Python")}
print(len(books))
print(sorted(b.title for b in books))
print(Book("算法导论") in books)