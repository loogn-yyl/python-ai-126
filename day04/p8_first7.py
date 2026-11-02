# p8_first7.py 找第一个：列表里找第一个能被 7 整除的数，找到就停；找不到输出「没有」。用 for-else 写
nums = [3, 5, 9, 14, 21]

for x in nums:
    if x % 7 == 0:
        print("找到", x)
        break
else:
    print("没有")