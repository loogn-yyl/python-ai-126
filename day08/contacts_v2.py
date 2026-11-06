# contacts_v2.py
"""命令行通讯录 v2: Contact 类 + JSON 持久化 + 菜单循环"""

import json
import os
import unicodedata

FILE = "contacts.json"

def dw(s):
    """字符串占几个显示格: 中文/全角算 2, 其余算 1"""
    return sum(2 if unicodedata.east_asian_width(c) in "WF" else 1 for c in s)

def pad(s, width):
    """右侧补空格, 补到占满 width 个显示格"""
    return s + " " * (width - dw(s))

# ---------- 数据层 ----------
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    @staticmethod
    def is_phone(s):
        return s.isdigit() and len(s) == 11

    def line(self):
        parts = [self.name, self.phone]
        if self.email:
            parts.append(self.email)
        return "  ".join(parts)

    def to_dict(self):
        return {"phone": self.phone, "email": self.email}

    @classmethod
    def from_dict(cls, name, d):
        if isinstance(d, str):
            return cls(name, d)
        return cls(name, d.get("phone", ""), d.get("email", ""))

def load():
    """读数据: 文件不存在就返回空字典"""
    if not os.path.exists(FILE):
        return {}
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            raw = json.load(f)
    except json.JSONDecodeError:
        print(f"  {FILE} 内容损坏, 已按空通讯录启动")
        return {}
    return {name: Contact.from_dict(name, d) for name, d in raw.items()}

def save(data):
    """写数据"""
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump({n: c.to_dict() for n, c in data.items()}, f, ensure_ascii=False, indent=2)

# ---------- 功能层 ----------
def show_all(data):
    if not data:
        print("  通讯录是空的")
        return
    print("  " + pad("序号", 5) + pad("姓名", 12) + "电话")
    for i, (name, phone) in enumerate(data.items(), start=1):
        print("  " + pad(str(i), 5) + pad(name, 12) + phone)

def add_contact(data):
    name = input("  要添加的姓名: ").strip()
    if not name:
        print("  姓名不能为空")
        return
    if name in data:
        print(f"  {name} 已存在, 电话是 {data[name]}")
        return
    phone = input("  电话: ").strip()
    if not Contact.is_phone(phone):
        print("  电话必须是 11 位数字")
        return
    email = input("  邮箱(可回车跳过):").strip()
    data[name] = Contact(name, phone, email)
    save(data)
    print(f"  已添加 {name}")

def delete_contact(data):
    name = input("  要删除的姓名: ").strip()
    if not name:
        print("  姓名不能为空")
        return
    if name not in data:
        print(f"  没找到 {name}")
        return
    del data[name]
    save(data)
    print(f"  已删除 {name}")

def find_contact(data):
    keyword = input("  要查找的姓名: ").strip()
    if not keyword:
        print("  姓名不能为空")
        return
    hits = {c for n, c in data.items() if keyword in n}
    if not hits:
        print("  没有匹配的联系人")
        return
    for c in hits:
        print("  " + c.line())

# ---------- 界面层 ----------
def show_menu(menu):
    print("\n" + "=" * 30)
    for i, item in enumerate(menu, start=1):
        print(f"  {i}) {item}")

    print("=" * 30)

def main():
    data = load()
    menu = ["添加联系人", "删除联系人", "查找联系人", "显示全部", "退出"]

    while True:
        show_menu(menu)
        choice = input("请选择: ").strip()
        
        if choice == "1":
            add_contact(data)
        elif choice == "2":
            delete_contact(data)
        elif choice == "3":
            find_contact(data)
        elif choice == "4":
            show_all(data)
        elif choice == "5":
            print("  再见")
            break
        else:
            print("  无效选项, 请输入 1-5")


if __name__ == "__main__":
    main()