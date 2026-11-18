# p5_head_to_csv.py 合并多个页面的标题：抓 3 个页面（用假 html 代替），输出成 csv，两列 url,title
import csv
import io
import re

TITLE = re.compile(r"<title[^>]*>(.*?)</title>", re.S | re.I)

pages = [
    ("https://a.com", "<title>站点 A</title>"),
    ("https://b.com", "<TITLE>站点 B</TITLE>"),
    ("https://c.com", "<p>没有标题</p>")
]

rows = []
for url, html in pages:
    m = TITLE.search(html)
    rows.append({"url": url, "title": " ".join(m.group(1).split()) if m else ""})

buf = io.StringIO()
w = csv.DictWriter(buf, fieldnames=["url", "title"])
w.writeheader()
w.writerows(rows)
print("\n".join(buf.getvalue().splitlines()))