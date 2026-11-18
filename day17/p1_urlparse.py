# p1_urlparse.py 拆 URL：用 urlparse 拆出 scheme / hostname / port / path / query，并用 parse_qs 把查询串转成字典
from urllib.parse import urlparse, parse_qs, urljoin

u = "https://example.com:8443/search?q=python&page=2#top"
p = urlparse(u)

print("scheme  :", p.scheme)
print("hostname:", p.hostname)
print("port    :", p.port)
print("path    :", p.path)
print("query   :", p.query)
print("fragment:", p.fragment)
print("netloc  :", p.netloc)
print()
print("参数     :", parse_qs(p.query))
print("拼回去   :", urljoin("https://example.com/a/b", "../c/d"))