# p6_no_title.py 处理没有 title 的页面：正则匹配不到时返回什么？写一个用例证明你的处理方式
import re

TITLE = re.compile(r"<title[^>]*>(.*?)</title>", re.S | re.I)

def get_title(html):
    m = TITLE.search(html)
    return " ".join(m.group(1).split()) if m else ""

print("有标题:",repr(get_title("<title>Hi</title>")))
print("空标题:",repr(get_title("<title></title>")))
print("没标题:",repr(get_title("<p>x</p>")))
print("空输入:",repr(get_title("")))