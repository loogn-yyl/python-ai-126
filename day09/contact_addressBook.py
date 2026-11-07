class Contact:
    def __init__(self, name):
        self.name = name

class AddressBook:
    # 组合：把字典装进来
    def __init__(self):
        self.items = {}

    def add(self, contact):
        self.items[contact.name] = contact

    def names(self):
        return sorted(self.items)

class BadBook(dict):
    # 继承：自己也变成了一个字典
    def add(self, contact):
        self[contact.name] = contact

b = AddressBook()
b.add(Contact("张三"))
b.add(Contact("李四"))
print(b.names())
print(hasattr(b, "clear"))

d = BadBook()
d.add(Contact("张三"))
d["随便塞一个"] = "我不是联系人"
print(sorted(d.keys()))
print(hasattr(d, "clear"))