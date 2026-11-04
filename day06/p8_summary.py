# p8_summary.py 成绩统计脚本（综合）：读 scores_csv.csv，逐行转数字（坏数据跳过），
# 算出每人总分/平均分、每科平均分，最后写一份 summary.csv

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


subjects = ["语文", "数学", "英语"]

students = []
subject_acc = {s: [] for s in subjects}   # 必须在循环外，只建一次
skipped = 0

with open("scores_csv.csv", "r", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        name = row["姓名"]

        scores = [to_number(row[s]) for s in subjects]   # 一定是列表

        if None in scores:                               # 数据不完整就整行跳过
            skipped += 1
            print(f"跳过(数据不完整): {name}")
            continue

        for subject, n in zip(subjects, scores):
            subject_acc[subject].append(n)

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
    print(f"{s['姓名']} 总分 {s['总分']} 平均 {s['平均分']}")

if students:
    class_avg = sum(s["平均分"] for s in students) / len(students)
    print(f"\n班级平均分: {class_avg:.1f}")

for subject, vs in subject_acc.items():
    print(f"{subject}平均 {sum(vs) / len(vs):.1f}")

print(f"共处理 {len(students)} 人，跳过 {skipped} 人")