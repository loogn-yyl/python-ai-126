# strinfo.py 输入一句话，输出它的字符数、全大写形式、以及第一个和最后一个字符

s = input("请输入一句话: ")

print(f"字符数: {len(s)}")
print(f"全大写形式: {s.upper()}")
print(f"第一个字符: {s[0]}")
print(f"最后一个字符: {s[-1]}")
