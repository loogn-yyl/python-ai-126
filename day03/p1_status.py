# p1_status.py 数字统计：输入 3,1,4,1,5，输出最大值、最小值、平均值（拆分 → 转数字 → 用 max/min/sum）

s = input("请输入一串数字, 用逗号隔开: ")

if s == "":
    print("无输入")
else:
    nums = [int(x) for x in s.split(",")]
    print(f"最大值: {max(nums)}")
    print(f"最小值: {min(nums)}")
    print(f"平均值: {sum(nums) / len(nums)}")