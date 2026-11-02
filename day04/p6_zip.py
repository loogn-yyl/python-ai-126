# p6_zip.py 配对打印：两个列表（姓名、分数），用 zip 打印「张三 88 分」

names = ["张三", "李四", "王五"]
scores = [88, 95, 76]

for n, s in zip(names, scores):
    print(f"{n} {s}分")