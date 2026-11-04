# p7_scores_csv.py CSV 生成：手工造一个 scores.csv，5 个学生 × 3 门课

import csv

with open("scores_csv.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["姓名", "语文", "数学", "英语"])
    w.writerow(["张三", 88, 95, 76])
    w.writerow(["李四", 92, 78, 85])
    w.writerow(["王五", 70, "缺考", 90])       # 故意留一条坏数据
    w.writerow(["赵六", 85, 88, 79])