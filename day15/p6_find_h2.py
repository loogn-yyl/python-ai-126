# p6_find_h2.py 抓所有 h2 标题：给一段 HTML，取出每个 <h2> 里的文字。这题的关键是那个问号
import re

page = "<h2>第一章</h2><p>x</p><h2>第二章</h2>"
print("标题:", re.findall(r"<h2>(.*?)</h2>", page))