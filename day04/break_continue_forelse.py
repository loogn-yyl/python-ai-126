# no.1
for x in [1, 3, 5, 8, 9]:
    if x % 2 == 0:
        print("找到第一个偶数: ", x)
        break
else:
    print("一个偶数都没有")

# no.2
nums = [1, -2, 3, -4, 5]
total = 0

for x in nums:
    if x < 0:
        continue
    total += x

print("正数之和: ", total)