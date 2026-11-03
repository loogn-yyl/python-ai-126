# 常用小工具函数

def area_circle(r):
    # 圆面积
    return 3.14159 * r * r

def celsius_to_fahrenheit(c):
    # 摄氏度转华氏度
    return c * 9 / 5 + 32

def is_leap(year):
    # 判断闰年
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def minmax(nums):
    # 同时返回最小值和最大值
    return min(nums), max(nums)

# 只有直接运行 utils.py 时才执行, 被 import 时不执行
if __name__ == "__main__":
    print("这是 utils.py 的自测")
    print(area_circle(2))
    print(is_leap(2024))