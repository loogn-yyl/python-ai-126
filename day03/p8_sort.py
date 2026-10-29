# p8_sort.py 成绩排名：把上面的 (姓名, 分数) 列表按分数从高到低排（用 sorted + key）

students = [("张三", 88), ("李四", 95), ("王五", 76)]

for name, score in sorted(students, key=lambda x: x[1], reverse=True):
    print(name, score)