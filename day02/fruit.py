# fruit.py 打印水果对齐表格

rows = [("苹果", 3, 12.5), ("香蕉", 10, 4.0), ("西瓜", 1, 30.0)]

print(f"{'商品':<4}{'数量':>4}{'单价':>6}")
print("-" * 18)
for name, qty, price in rows:
	print(f"{name:<6}{qty:>4}{price:>8.1f}")
