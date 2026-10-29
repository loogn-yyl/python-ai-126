# sum.py 逗号分隔求和：输入 `1,2,3,4`，输出总和 10（用 split + 列表推导式）

s = input("请输入: ")

nums = s.split(",")
total = 0

for x in nums:
    total += int(x)

print(total)