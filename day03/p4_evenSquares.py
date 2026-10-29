# p4_evenSquares.py 列表推导式：一行生成 1–100 内所有偶数的平方

print([x * x for x in range(1, 101) if x % 2 == 0])