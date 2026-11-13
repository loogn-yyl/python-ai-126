# no.1
line = '127.0.0.1 - - [13/Nov/2026:02:15:33 +0800] "GET /index.html HTTP/1.1" 200 512'

print("IP     :", line.split()[0])
print("第 4 段:", line.split()[3])
print("第 9 段:", line.split()[8])

# 换一种日志格式, 同一个下标就错位了
line2 = '127.0.0.1 [13/Nov/2026:02:15:33] "GET /index.html" 200'
print("第 9 段:", line2.split()[8] if len(line2.split()) > 8 else "IndexError")
print("状态码在哪:", [x for x in line2.split() if x.isdigit()])