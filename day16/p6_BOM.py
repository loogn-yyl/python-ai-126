# p6_BOM.py 读带 BOM 的文本：手工造一段 b"\xef\xbb\xbf..."，对比 utf-8 和 utf-8-sig 读出来的差别
raw = b"\xef\xbb\xbfip,count\n10.0.0.5,2"

a = raw.decode("utf-8")
b = raw.decode("utf-8-sig")
print("utf-8    :", repr(a.split("\n")[0]))
print("utf-8-sig:", repr(b.split("\n")[0]))
print("第一个字段相同吗:", a.split("\n")[0] == b.split("\n")[0])

import csv
import io
print("用 utf-8     读的列名:", list(csv.DictReader(io.StringIO(a)).fieldnames))
print("用 utf-8-sig 读的列名:", list(csv.DictReader(io.StringIO(b)).fieldnames))