from contacts import AddressBook, Contact

import os

c1 = Contact("张三", "13800001111")
c2 = Contact("李四", "13900002222", "ls@example.com", ["同事", "技术部"])

print(c1)
print(c2)
print(c1.line())
print(c2.line())

book = AddressBook(path="demo.json")
print(book.add(c1))
print(book.add(c2))
print("剩余:", [c.name for c in book])
print("--- actions.log ---")
with open("actions.log", encoding="utf-8") as f:
    print(f.read().strip())

os.remove("demo.json")