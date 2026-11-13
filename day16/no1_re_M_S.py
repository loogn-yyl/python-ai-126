# no.1
import re

text = """200 OK
404 Not Found
500 Error"""

print("不加标志 :", re.findall(r"^\d+", text))
print("re.M    :", re.findall(r"^\d+", text, re.M))
print("re.M + $:", re.findall(r"^\d+$", text, re.M))
print()
block = """<div class="a">
  内容
</div>"""
print("不加标志   :", re.findall(r'<div class="a">(.*)</div>', block))
print("re.S      :", re.findall(r'<div class="a">(.*)</div>', block, re.S))
print("re.S 非贪婪:", re.findall(r'<div class="a">(.*?)</div>', block, re.S))