# p6_tags.py 避开可变陷阱：Contact(name, tags=None)，tags 不传时每个人都拿到自己的空列表

class Contact:
    def __init__(self, name, tags=None):
        self.name = name
        self.tags = [] if tags is None else tags

a = Contact("张三")
a.tags.append("同学")
b = Contact("李四")
print(a.tags, b.tags)
print(a.tags is b.tags)