# no.6
import re

html = """<html><head><title>Python 官方教程</title></head>
<body><h1>欢迎</h1></body></html>"""

m = re.search(r"<title>(.*?)</title>", html, re.S | re.I)
print("标题:", m.group(1).strip() if m else None)

dirty = "<title>\n   多个空格   的标题\n</title>"
m2 = re.search(r"<title>(.*?)</title>", dirty, re.S | re.I)
print("原始:", repr(m2.group(1)))
print("清理:", " ".join(m2.group(1).split()))