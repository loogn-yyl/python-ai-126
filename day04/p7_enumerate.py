# p7_enumerate.py 带序号菜单：用 enumerate 打印一个 5 项菜单，格式 1) 添加
menu = ["添加联系人", "删除联系人", "查找", "显示全部", "退出"]
for i, item in enumerate(menu, start=1):
    print(f"{i}) {item}")