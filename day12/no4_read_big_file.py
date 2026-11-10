# no.4
import os
import tracemalloc

with open("big.txt", "w", encoding="utf-8") as f:
    for i in range(200000):
        f.write(f"第 {i} 行 一些内容\n")

print("文件大小:", round(os.path.getsize("big.txt") / 1024 / 1024, 1), "MB")

tracemalloc.start()
total = 0
for line in open("big.txt", encoding="utf-8"):
    total += int(line.split()[1])
cur, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print("逐行读  累加 =", total, " 峰值内存 =", round(peak / 1024 / 1024, 1), "MB")

tracemalloc.start()
lines = open("big.txt", encoding="utf-8").readlines()
total2 = sum(int(l.split()[1]) for l in lines)
cur2, peak2 = tracemalloc.get_traced_memory()
tracemalloc.stop()
print("readlines 累加 =", total2, " 峰值内存 =", round(peak2 / 1024 / 1024, 1), "MB")
print("结果一样吗:", total == total2)

os.remove("big.txt")