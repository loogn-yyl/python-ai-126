# no.1
nums = [10, 20, 30]

# C 思维
total = 0
for i in range(len(nums)):
    total += nums[i]
print(total)

# Python 思维
print(sum(nums))

# no.2
nums = [10, 20, 30]

# C 思维
for i in range(len(nums)):
    print(nums[i])

# Python 思维
for x in nums:
    print(x)

# no.3
nums = [10, 20, 30]

# C 思维
for i in range(len(nums)):
    print(str(i + 1) + ". " + str(nums[i]))

# Python 思维
for i, x in enumerate(nums, start=1):
    print(f"{i}. {x}")

# no.4
nums = [10, 20, 30]

# C 思维
for i in range(len(nums) - 1, -1, -1):
    print(nums[i])

# Python 思维：只需要元素
for x in reversed(nums):
    print(x)

# Python 思维：需要下标时
for i in range(len(nums) - 1, -1, -1):
    print(i, nums[i])

# no.5
a = [1, 2, 3]
b = [10, 20, 30]

# C 思维
for i in range(len(a)):
    print(a[i] + b[i])

# Python 思维
for x, y in zip(a, b):
    print(x + y)