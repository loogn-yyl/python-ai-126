from contacts import AddressBook, Contact

book = AddressBook(path="demo.json")
print(book.add(Contact("张三", "13800001111")))
print(book.add(Contact("李四", "13900002222", "ls@example.com")))
print(book.remove("张三"))
print("剩余:", [c.name for c in book])
print("--- actions.log 全文 ---")
with open("actions.log", encoding="utf-8") as f:
    print(f.read().strip())