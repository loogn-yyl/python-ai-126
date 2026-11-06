# no.1
# D007 的写法: 一个字典
c = {"name": "张三", "phone": "13800001111"}
print(c["name"], c["phone"])

# 类
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

c = Contact("张三", "13800001111")
print(c.name, c.phone)

# no.2
class Contact:
    def __init__(self, name):
        self.name = name
    def hello(self):
        return f"我是 {self.name}"

a = Contact("张三")
b = Contact("李四")
print(a.hello())
print(b.hello())
print(a is b)
print(a.name, b.name)

# no.3
# class Bad:
#     def __init__(name):
#         self.name = name

# Bad("张三")

# no.4
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

a = Contact("张三", "13800001111")
b = a
b.name = "李四"
print(a.name, a is b)

c = Contact("李四", "13800001111")
print(a == c, a is c)

# no.5
class Contact: 
    def __init__(self, name):
        self.name = name

print(Contact("张三"))

# no.6
class Contact:
    count = 0    # 类属性, 所有实例共用一份
    def __init__(self, name):
        self.name = name      # 实例属性: 每个对象各有一份
        Contact.count += 1    # 更改类属性, 必须有类名

a = Contact("张三")
b = Contact("李四")
print(Contact.count, a.count, b.count)

a.count = 100    # 新建 a 自己的实例属性
print(Contact.count, a.count, b.count)

# no.7
class Contact:
    tags = []    # 类属性是可变对象 -> 所有实例共用一个列表
    def __init__(self, name):
        self.name = name

a = Contact("张三")
b = Contact("李四")
a.tags.append("同学")
print(a.tags, b.tags, Contact.tags)

# 类属性只放不可变的东西(数字、字符串、元组)
# 列表、字典、集合这类, 一律在 __init__ 里用 self.tags = [] 创建

# no.8
class Bad:
    def __init__(self, tags=[]):
        self.tags = tags

a = Bad()
a.tags.append("同学")
b = Bad()
print(a.tags, b.tags, a.tags is b.tags)

class Good:
    def __init__(self, tags=None):
        self.tags = [] if tags is None else tags

a = Good()
a.tags.append("同学")
b = Good()
print(a.tags, b.tags, a.tags is b.tags)

# no.9
class Contact:
    total = 0

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        Contact.total += 1

    @classmethod
    def from_text(cls, line):
        """从 '张三, 13800001111' 这样的一行构造对象"""
        name, phone = line.split(",")
        return cls(name.strip(), phone.strip())

    @staticmethod
    def is_phone(s):
        """纯校验, 不需要 self 也不需要 cls"""
        return s.isdigit() and len(s) == 11

c = Contact.from_text("张三, 13800001111")
print(c.name, c.phone, Contact.total)
print(Contact.is_phone("13800001111"), Contact.is_phone("abc"))