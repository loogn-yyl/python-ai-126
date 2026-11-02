# p5_filter.py 筛选平方：一行推导式，取出 1–20 里所有能被 3 整除的数的平方

print([x * x for x in range(1, 21) if x % 3 == 0])