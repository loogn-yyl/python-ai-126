# calculator.py 输入两个整数，输出它们的和、差、积、商（商保留两位小数）

a = int(input("请输入第一个整数: "))
b = int(input("请输入第二个整数: "))

print(f"它们的和: {a + b}")
print(f"它们的差: {a - b}")
print(f"它们的积: {a * b}")

if b == 0:
    print("它们的商不存在，因为除数为零，非法")
else:
    print(f"它们的商: {a / b:.2f}")