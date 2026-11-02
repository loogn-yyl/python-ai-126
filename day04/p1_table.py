# p1_table.py 九九乘法表：用双层 for 循环打印左下三角（对齐！见下方提示）
for x in range(1, 10):
    row = []
    for y in range(1, x + 1):
        row.append(f"{y}x{x}={x*y:<3}")
    print("".join(row))