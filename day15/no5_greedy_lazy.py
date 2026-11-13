# no.5
import re

html = '<a href="a.html">A</a> <a href="b.html">B</a>'

print("贪婪  :", re.findall(r'<a href="(.*)">', html))
print("非贪婪:", re.findall(r'<a href="(.*?)">', html))
print()
s ="a1b2c3"
print("贪婪  \\d+ :", re.findall(r"\d+", s))
print("贪婪  .+   :", re.search(r".+", s).group())
print("非贪婪 .+? :", re.search(r".+?", s).group())
print()
print("为什么 .+? 只到 1 :", re.search(r".+?(\d)", s).groups())