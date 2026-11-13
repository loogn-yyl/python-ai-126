# no.2-1
import re

text = "订单 A1024 金额 299 元, 订单 A2048 金额 1580 元"

print("match  :", re.match(r"A\d+", text))
print("search :", re.search(r"A\d+", text))
print("findall:", re.findall(r"A\d+", text))
print("sub    :", re.sub(r"A\d+", "A***", text))

m = re.search(r"A(\d+)", text)
print("group()  :", m.group())
print("group(1) :", m.group(1))
print("start/end:", m.start(), m.end())

# no.2-2
import re

print("1", re.match(r"\d+", "abc123"))
print("2", re.search(r"\d+", "abc123"))
print("3", re.match(r"abc", "abcdef"))
print("4", re.fullmatch(r"\d+", "123"))
print("5", re.fullmatch(r"\d+", "123abc"))
print("6", re.search(r"^abc", "xxabc"))
print("7", re.search(r"abc$", "abcxx"))