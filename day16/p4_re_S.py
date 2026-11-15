# p4_re_S.py 用 re.S 抓多行内容：给一段跨行的 HTML，把每个 <p> 里的文字取出来（去掉首尾空白）
import re

page = """<div>
<p>
  第一段
  跨了两行
</p>
<p>
  第二段
</p>
</div>"""

got = re.findall(r"<p>(.*?)</p>", page, re.S)
print("原始      :", got)
print("去掉首尾空白:", [s.strip() for s in got])
print("压平后     :", ["  ".join(s.split()) for s in got])