from contacts import AddressBook, Contact

book = AddressBook(path="demo2.json")
for n in ["张三", "李四", "王五"]:
    book.add(Contact(n, "13800001111"))

print("find('张'):", [c.name for c in book.find("张")])
print("len(book):", len(book))
print("for 循环:", [c.name for c in book])
print("有 __getitem__ 吗:", hasattr(book, "__getitem__"))