# p1_email.py 抓邮箱：从一段文字里找出所有邮箱地址。用 findall，注意 . 在正则里是元字符，要用 \. 转义

import re

text = "联系 zs@example.com 或 ls@test.org, 无效的 a@b"
print("邮箱地址:", re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", text))