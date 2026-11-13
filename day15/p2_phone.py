# p2_phone.py 校验手机号：11 位、1 开头、第二位 3–9。用 fullmatch，不要用 match，并测一个 10 位的反例
import re

print("手机号:", bool(re.fullmatch(r"1[^012]+\d{9}", "13800001111")))
print("假手机号:", bool(re.fullmatch(r"1[^012]+\d{9}", "1380000111")))