# contacts_v1.py
"""命令行通讯录 v1 —— 字典存储 + JSON 持久化 + 菜单循环"""

import json
import os

FILE = "contacts.json"

# ---------- 数据层 ----------
def load():
    """读数据: 文件不存在就返回空字典"""
    if not os.path.exists(FILE):
        return {}
    with open(FILE, "r", encoding="utf-8") as f:
        return json.loads(f)

def save(data):
    """写数据"""
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# ---------- 功能层 ----------
def show_all(data):
    if not data:
        print("  通讯录是空的")
        return
    print(f"  {'序号':<4}{'姓名':<8}{'电话'}")
    for i, (name, phone) in enumerate(data.items(), start=1):
        print(f"  {i:<4}{name:<8}{phone}")

def add_contact(data):
    name = input("  要添加的姓名: ").strip()
    if not name:
        print("  姓名不能为空")
        return
    if name in data:
        print(f"  {name} 已存在, 电话是 {data[name]}")
        return
    phone = input("  电话: ").strip()
    if not phone:
        print("  电话不能为空")
        return
    data[name] = phone
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
    hits = {k: v for k, v in data.items() if keyword in k}
    if not hits:
        print("  没有匹配的联系人")
        return
    for name, phone in hits.items():
        print(f"  {name}: {phone}")

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