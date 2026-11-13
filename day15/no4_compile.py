# no.4
import re

s = "张三 13800001111 李四 13900002222 王五 13700003333"

print("简单分组:", re.findall(r"(\S+) (\d{11})", s))
print()
pat = re.compile(r"(?P<name>\S+) (?P<phone>\d{11})")
for m in pat.finditer(s):
    print(m.groupdict())
print()
print("非捕获组:", re.findall(r"(?:\S+) (\d{11})", s))
print("整个匹配:", [m.group(0) for m in pat.finditer(s)])