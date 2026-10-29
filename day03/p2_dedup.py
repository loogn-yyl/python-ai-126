# p2_dedup.py 去重保序：输入一串数字，去掉重复但保持原来顺序（不能直接用 set，会乱序）

s = input("请输入一串数字, 用逗号隔开: ")

nums = [int(x) for x in s.split(",")]
res = []

for x in nums:
    if x not in res:
        res.append(x)

print(res)