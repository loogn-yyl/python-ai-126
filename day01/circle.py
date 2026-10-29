# circle.py 输入圆的半径，输出面积和周长（结果保留两位小数）

import math

r = float(input("请输入圆的半径: "))

a = math.pi * r * r
c = 2 * math.pi * r

print(f"圆的面积: {a:.2f}")
print(f"圆的周长: {c:.2f}")
