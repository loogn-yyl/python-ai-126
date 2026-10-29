# phonemask.py 手机号打码：输入 `13812345678`，输出 `138****5678`（用切片拼接）

phonenumber = input("请输入手机号: ")

print(phonenumber[0:3] + "*" * 4 + phonenumber[-4:])