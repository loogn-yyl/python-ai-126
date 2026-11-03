# D005 练习 utils.py

import math

def area(r):
    """圆面积"""
    return math.pi * r * r

def greet(name, greeting="你好"):
    """生成问候语"""
    return f"{greeting}, {name}"

def average(*nums):
    """平均数"""
    if not nums:
        return 0
    return sum(nums) / len(nums)

def describe(**info):
    """打印所有配置项"""
    for k, v in info.items():
        print(f"{k}: {v}")

def stats(nums):
    """返回最小值, 最大值, 平均值"""
    if not nums:
        return 0, 0, 0
    return min(nums), max(nums), sum(nums) / len(nums)

if __name__ == "__main__":
    print("这是 utils.py 的自测")
    print(f"{area(2):.2f}")
    print(greet("张三"))
    print(average(1, 2, 3))
    describe(name="李四", age=20)
    print(stats([3, 1, 4, 1, 5]))