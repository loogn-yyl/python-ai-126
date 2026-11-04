# p8_summary.py 成绩统计脚本（综合）：读 scores.csv，逐行转数字（坏数据跳过），算出每人总分/平均分、每科平均分，最后写一份 summary.csv

import csv

def to_number(s):
    """能转数字就转，转不了返回 None"""
    try:
        return int(s)
    except ValueError:
        pass
    try:
        return float(s)
    except ValueError:
        return None

students = []
skipped = 0

with open("scores_csv.csv", "r", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        name = row["姓名"]
        scores = []
        for subject in ["语文", "数学", "英语"]:
            n = to_number(row[subject])
            if n is None:
                scores = None
                break
            scores.append(n)

        if scores is None:
            skipped += 1
            print(f"跳过(数据不完整): {name}")
            continue

        total = sum(scores)
        students.append({"姓名": name, "总分": total, 
                         "平均分": round(total / len(scores), 1)})

with open("summary.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["姓名", "总分", "平均分"])
    for s in students:
        w.writerow([s["姓名"], s["总分"], s["平均分"]])

print()

for s in students:
    print(f"{s["姓名"]} 总分 {s["总分"]} 平均 {s["平均分"]}")

if students:
    class_avg = sum(s["平均分"] for s in students) / len(students)
    print(f"\n班级平均分: {class_avg:.1f}")

print(f"共处理 {len(students)} 人， 跳过 {skipped} 人")