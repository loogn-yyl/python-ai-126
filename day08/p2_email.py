# p2_email.py 默认参数：给 Contact 加第三个属性 email，不传时是空字符串
class Contact:
    def __init__(self, name, phone, email=""):
        self.name = name
        self.phone = phone
        self.email = email

a = Contact("张三", "13800001111")
b = Contact("李四", "13900002222", "ls@example.com")
print(a.name, a.phone, repr(a.email))
print(b.name, b.phone, b.email)