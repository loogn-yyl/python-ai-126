# p3_count.py 计数器：用类属性 count 统计一共造了多少个 Contact，造 3 个看数字

class Contact:
    count = 0

    def __init__(self, name, phone, email=""):
            self.name = name
            self.phone = phone
            self.email = email
            Contact.count += 1

a = Contact("张三", "13800001111")
b = Contact("李四", "13900002222", "ls@example.com")
c = Contact("王五", "13800003333")

print("一共创建了", Contact.count, "个联系人")