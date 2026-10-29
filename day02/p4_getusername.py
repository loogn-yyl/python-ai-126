# getusername.py 提取用户名：输入邮箱 `abc@qq.com`，输出 `abc`（用 split）

email = input("请输入邮箱: ")

user = email.split("@")
print(user[0])