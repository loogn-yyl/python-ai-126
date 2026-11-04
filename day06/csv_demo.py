# no.1
import csv

with open("scores.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["姓名", "成绩"])
    w.writerow(["张三", 88])
    w.writerow(["李四", 95])

print("csv 写入完成")

# no.2
import csv

with open("scores.csv", "r", encoding="utf-8") as f:
    r = csv.reader(f)
    for row in r:
        print(row)

with open("scores.csv", "r", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        print(row)