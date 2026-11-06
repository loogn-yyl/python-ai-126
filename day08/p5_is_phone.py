# p4_is_phone.py 静态方法：Contact.is_phone(s)，11 位纯数字才算合法，测 4 个输入

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    @staticmethod
    def is_phone(s):
        return s.isdigit() and len(s) == 11

for s in ["13800001111", "1380000111", "1380000111a", ""]:
    print(repr(s), Contact.is_phone(s))