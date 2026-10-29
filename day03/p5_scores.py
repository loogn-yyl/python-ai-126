# p5_scores.py 成绩管理：用字典存三门成绩，输出平均分和最高分的科目名（提示：max(d, key=d.get)）

scores = {"语文": 88, "数学": 95, "英语": 76}

print(f"平均分: {sum(scores.values()) / len(scores):.1f}")

best = max(scores, key=scores.get)
print(f"最高分: {best} {scores[best]}")