# no.3
import re

print(r"\d 数字   :", re.findall(r"\d", "a1b2c3"))
print(r"\w 单词字符:", re.findall(r"\w", "a1 中文_-"))
print(r"\s 空白   :", re.findall(r"\s", "a b\tc\nd"))
print(r". 任意字符 :", re.findall(r".", "abc"))
print("[abc]     :", re.findall(r"[abc]", "a1b2c3"))
print("[^abc]    :", re.findall(r"[^abc]", "a1b2c3"))
print("[0-9]{2}  :", re.findall(r"[0-9]{2}", "a1234b"))
print()
print("退格符     :", repr("\bword"), "长度", len("\bword"))
print("原始字符串  :", repr(r"\bword"), "长度", len(r"\bword"))