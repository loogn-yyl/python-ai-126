# no.1
# 不推荐写法
f = open("hello.txt", "w", encoding="utf-8")
f.write("第一行\n")
f.write("第二行\n")
f.close()    # 这一行必须写

# 推荐写法
with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("第一行\n")
    f.write("第二行\n")

print("写入完成")

# no.2
# 一次性读成大字符串
with open("hello.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(content)

# 逐行读
with open("hello.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())