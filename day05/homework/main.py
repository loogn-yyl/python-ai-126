# main.py
import utils

print(f"圆面积: {utils.area(3):.2f}")
print(utils.greet("王五"))
print(f"平均值: {utils.average(2, 3, 4)}")
print(f"空参数: {utils.average()}")
utils.describe(name="赵六", age=27)
print(utils.stats([3, 1, 4]))

# p6_lambda.py lambda 排序：学生列表 [("张三",88), ...]，按分数从高到低排
students = [("张三", 88), ("李四", 95), ("王五", 76)]
for name, score in sorted(students, key=lambda s: s[1], reverse=True):
    print(f"{name}: {score}分")