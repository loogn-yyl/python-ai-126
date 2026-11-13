# p3_urls.py 提取域名：给一串 URL（https:// / http:// / ftp:// 都有），取出域名部分
import re

urls = ["https://a.com/x", "http://b.org/y", "ftp://c.net"]
print("域名:", [re.search(r"://([^/]+)", u).group(1) for u in urls])