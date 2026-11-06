# p4_from_text.py 类方法：Contact.from_text("张三,13800001111") 从一行文本造对象，两边空格要去掉
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    @classmethod
    def from_text(cls, line):
        name, phone = line.split(",")
        return cls(name.strip(), phone.strip())

a = Contact.from_text("李四, 13900002222")
print(repr(a.name), repr(a.phone))